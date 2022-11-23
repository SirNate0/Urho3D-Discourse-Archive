Sir_Nate | 2017-01-02 01:04:56 UTC | #1

What is the correct way to remove scene nodes from a script object attached to the scene node? I ask as the way I currently do it is not working correctly. 

I am attempting to remove a scene node and its components after a set delay. As such, I DelayedExecute a Terminate() method in the Start() method with the given delay (4.5 seconds, in this case). 
[code]void Terminate()
    {
        //scriptFile.ClearDelayedExecute(); Using this causes a null pointer in the AngelScript stack, so I am not using it anymore (removing the ScriptObject should take care of delayed calls anyways)
        node.RemoveAllChildren();

        node.Remove();
        //node.RemoveAllComponents(); This also causes a null pointer exception
    }[/code]
Interestingly, the code works fine when I run the program normally, but when I run debug, it receives a SigSegV when it tries to remove the DelayedCall in ScriptInstance::HandleSceneUpdate (see below). I assume that this is because at this point the scene node and components have already been freed/deleted (Adding a break point I was able to observe that the delayedCalls_ vector in the script instance was filled with the values 0xFEEEFEEE, which is win32's freed memory pattern).

I am considering adding a deadNodeRoot as described in topic1004 ("Invalid/Dead nodes in Lua causing segfaults"), having it remove its children each tick, but before I do so I wanted to be sure that I wasn't a better solution.

[b]Stack Trace:[/b]
[spoiler]#0 00A8CDA4	Urho3D::DelayedCall::operator=(this=0xfeeefeeefeeefeee) (../../../Source/Urho3D/Script/../Script/../Script/ScriptEventListener.h:35)
#1 00C286C8	Urho3D::Vector<Urho3D::DelayedCall>::MoveRange(this=0xbe48c70, dest=0, src=1, count=4277075693) (H:/Projects/Urho/UrhoRepo/Source/Urho3D/Container/../Container/Vector.h:421)
#2 00C283F7	Urho3D::Vector<Urho3D::DelayedCall>::Erase(this=0xbe48c70, pos=0, length=1) (H:/Projects/Urho/UrhoRepo/Source/Urho3D/Container/../Container/Vector.h:252)
#3 0041A460	Urho3D::ScriptInstance::HandleSceneUpdate(this=0xbe48b40, eventType=..., eventData=...) (..\..\..\Source\Urho3D\Script\ScriptInstance.cpp:714)
#4 00AC0AAA	Urho3D::EventHandlerImpl<Urho3D::ScriptInstance>::Invoke(this=0xbe30350, eventData=...) (../../../Source/Urho3D/Script/../Core/../Core/Object.h:263)
#5 0041B84C	Urho3D::Object::OnEvent(this=0xbe48b40, sender=0xbb8c870, eventType=..., eventData=...) (..\..\..\Source\Urho3D\Core\Object.cpp:71)
#6 0041C192	Urho3D::Object::SendEvent(this=0xbb8c870, eventType=..., eventData=...) (..\..\..\Source\Urho3D\Core\Object.cpp:252)
#7 0047CB98	Urho3D::Scene::Update(this=0xbb8c870, timeStep=0.0079020001) (..\..\..\Source\Urho3D\Scene\Scene.cpp:617)
#8 0047E12A	Urho3D::Scene::HandleUpdate(this=0xbb8c870, eventType=..., eventData=...) (..\..\..\Source\Urho3D\Scene\Scene.cpp:966)
#9 00AC2DDA	Urho3D::EventHandlerImpl<Urho3D::Scene>::Invoke(this=0xbb8d610, eventData=...) (../../../Source/Urho3D/Scene/../Scene/../Scene/../Scene/../Core/Object.h:263)
#10 0041B88E	Urho3D::Object::OnEvent(this=0xbb8c870, sender=0x4379890, eventType=..., eventData=...) (..\..\..\Source\Urho3D\Core\Object.cpp:79)
#11 0041C36F	Urho3D::Object::SendEvent(this=0x4379890, eventType=..., eventData=...) (..\..\..\Source\Urho3D\Core\Object.cpp:285)
#12 00454640	Urho3D::Engine::Update(this=0x4379890) (..\..\..\Source\Urho3D\Engine\Engine.cpp:614)
#13 00453C89	Urho3D::Engine::RunFrame(this=0x4379890) (..\..\..\Source\Urho3D\Engine\Engine.cpp:424)
#14 00444512	Urho3D::Application::Run(this=0x4379720) (..\..\..\Source\Urho3D\Engine\Application.cpp:83)
#15 004037EE	RunApplication() (Game.hpp:32)
#16 0040388D	main(argc=1, argv=0x4372b70) (Game.hpp:32)[/spoiler]

-------------------------

GoogleBot42 | 2017-01-02 01:04:56 UTC | #2

That seems strange... I thought that references to objects in angelscript are properly wrapped in a "SharedPtr".  Is this is a bug perhaps?  Did the reference count number get changed somewhere it shouldn't?  Or am I not understanding what is happening here.   :neutral_face:

-------------------------

weitjong | 2017-01-02 01:04:56 UTC | #3

Welcome to our forum.

Yes, AngelScript scripting API does not have problem with respect to object reference counting as Lua scripting API does. As I understand it, the call to "Node.Remove()" should instruct the parent of the node to erase itself as children and in doing so may call the node's destructor (if the refcount reaches 0) which in turn destroy all the node's children and components automatically. In other words, there is no need for you to clean up the node yourself in the Terminate() function. Assuming you don't have have other AngelScript node handle that references the same object, once this remaining node handle used in the Terminate() function goes out of scope then the object will be guaranteed to be destroyed along with its children and components. I am not sure why your code work when runs normally but not when stepping through the code in Debug mode without looking more closely to the rest of your code though, but your guess is as good as anyone of us. Probably the node's children/components has been deleted when you stepping through the code that still try to use them. So, perhaps don't do the clean up yourself may actually prevent this.

-------------------------

Sir_Nate | 2017-01-02 01:05:12 UTC | #4

Simply using node.Remove is working as expected, but it only works if I call it from the actual Update(timestep) method, not from a DelayedExecute call. I would guess this has to do with how the ScriptInstance::HandleSceneUpdate(StringHash eventType, VariantMap& eventData) is organized -- the script's Update(float) angelscript call occurs right at the end of the HandleSceneUpdate method, so there is nothing to cause a SigSegV if the node (and by extension the script component) is deleted, while because of the for loop around the delayedExecute checks and the later stuff in that method, if the script is deleted in a delayed call, you can end up with one (or at least with some problems). Interestingly, something, perhaps in how the angelscript is implemented, keeps it from crashing even with the delayedExecute that removes the node, though at that point it does spew forth lots of "Exception 'Null pointer access' in 'void Battlemon::FixedUpdate(float)'    AngelScript callstack: ... " errors and the node does not actually seem to be removed. While it didn't crash with me this time from this, it did crash when I later attempted to create an object from that node (but that may be related to having stored a LogicComponent derivative in a SharedPtr, which only stores the node in a regular pointer). Regardless of that, the 'Null pointer access' error is quite annoying on its own.

In any case, its easy to work around -- either a boolean set by the delayed execute that causes it to be removed, a simple counter in the Update(float) method that then removes it, or attaching it to another node that removes it.

Overall, though, I don't think I've seen any problems with the angelscript reference counting -- I think all of that has worked fine (I just wasn't certain how I needed to remove nodes and their components). The one possible issue that I've seen, which isn't with the reference counting itself, is that with the delayed execute and removing a node.

Would you say that would be considered a bug?

-------------------------

cadaver | 2017-01-02 01:05:12 UTC | #5

I'll have to verify, but that looks like a bug. Using DelayedExecute() for delayed removal should be a valid usecase, as it's easier than manually maintaining a lifetime counter.

-------------------------

cadaver | 2017-01-02 01:05:13 UTC | #6

Remove through DelayedExecute() should work OK, just observe the proper use of function parameters and the lookup of function by full declaration (not just name). Add for example the following line in the SpawnObject function in the Ragdolls example. This will make each ball you spawn remove itself after 1 second from first collision.

[code]
    boxNode.CreateScriptObject(scriptFile, "SelfDestroyer");
[/code]
And the SelfDestroyer class code:

[code]
class SelfDestroyer : ScriptObject
{
    void Start()
    {
        // Subscribe physics collisions that concern this scene node
        SubscribeToEvent(node, "NodeCollision", "HandleNodeCollision");
    }
    
    void RemoveSelf()
    {
        node.Remove();
    }
    
    void HandleNodeCollision(StringHash eventType, VariantMap& eventData)
    {
        // Remove self after 1 second from collision
        DelayedExecute(1.0f, false, "void RemoveSelf()");
        // No further event response required
        UnsubscribeFromEvent("NodeCollision");
    }
}
[/code]

EDIT: pushed a change to master branch that allows to just submit the function name to DelayedExecute, if it's a void function without parameters. If it's anything else, you need to give the full declaration ( like "bool FunctionWithFloatParameter(float)" )

-------------------------

