codefive | 2019-06-19 02:56:16 UTC | #1

Hello everyone !!
I have created a class, but when i "call" the Update method i can see a update but a certain ping-pong effect. What is the correct way to do this? My class inherits from LogicComponent and i draw a series of subnodes in OnNodeSet method, then in the Update method i only move the node that i have used in OnNodeSet. Thank you in advance !!

-------------------------

Leith | 2019-06-19 06:30:40 UTC | #2


You don't need to call the Update method yourself - it will get "ticked" by Urho3D every frame.
All objects deriving from Component will get "ticked" every frame.
To prevent this, you can disable individual components, their parent scene nodes, or entire scene node subtrees and all the components they hold - and in the latter case, there is a mechanism to undo such a change.

The component update method is not what you want for drawing stuff - it's meant for logic updates, at full frame rate.

Stuff that you draw tends to derive from Drawable.

If you elaborate on what you're trying to achieve, I might be able to help further - I've worked a lot with node hierarchies, including Urho's scene hierarchy, and custom node hierarchies too.

Hope that's helpful :slight_smile:

-------------------------

codefive | 2019-06-20 02:10:06 UTC | #3

Im trying to create a Tetris game, i have already created the clases for each Tetris figure, what im stuck is how to put all that logic in my app. For what i know in the update method i would like the figures to fall down from above of the screen i also need to make them move with keyboard keys, but as im so new in this everyday is a new begining for me. LOL

-------------------------

Leith | 2019-06-20 03:44:56 UTC | #4


I typically handle player input in my Update method, and depending on the user input, I do some kind of logic to control the player. Update method is called every graphics frame, as fast as the engine can render, unless the framerate is being capped (default cap is 200fps). 

More rarely, I sometimes deal with player input in the FixedUpdate method... this one is not called every graphics frame (whose rate can vary!), instead it is "called from" the physicsworld component (via urho3d engine events) at a fixed rate.
It depends on the game, but since I figure you have no physics yet, the Update method would be the place to do it...

-------------------------

jmiller | 2019-06-20 18:07:26 UTC | #5

 Sample.inl is included by all samples to handle common single key events (like take screenshot).
  https://github.com/urho3d/Urho3D/blob/master/Source/Samples/Sample.inl#L92
  https://github.com/urho3d/Urho3D/blob/master/Source/Samples/Sample.inl#L245

More sophisticated samples like NinjaSnowWar and CharacterDemo also do *constant* input polling with `Input::GetKeyDown()` and others from class [Input](https://urho3d.github.io/documentation/HEAD/_input.html).

[Character](https://github.com/urho3d/Urho3D/blob/master/Source/Samples/18_CharacterDemo/Character.h)::controls_  holds the control states like keys and mouse buttons down.
The app clears and sets these states on normal Update event: https://github.com/urho3d/Urho3D/blob/master/Source/Samples/18_CharacterDemo/CharacterDemo.cpp#L258

`Character` has subscribed to FixedUpdate ( with the LogicComponent `SetUpdateEventMask(USE_FIXEDUPDATE)` in Start() ) where it is continually acting on those.
 https://github.com/urho3d/Urho3D/blob/master/Source/Samples/18_CharacterDemo/Character.cpp#L84

Hope that helps -- let us know how it is going!

Offtopic @codefive:  I never met a language I did not like. :slight_smile: (non-programming language :laughing:)

-------------------------

codefive | 2019-06-20 16:59:04 UTC | #6

@jmiller Thank you !!
Yes !! I was looking right now at the CharacterDemo sample, and i think i will do something based on that, i already knew i needed some globals to hold my Class "sprite" or figure and also the controls so i can link both, but i wasnt shure how to do that, i will try and tell you how it goes. It isnt that i dont like Spanish, not at all, but when you are talking with friends and topics you really like, sometimes makes me wish i knew English native. Hugs to eveyone my friends !!

-------------------------

codefive | 2019-06-21 17:14:40 UTC | #7

So this is what i did, i added a rigid body, and linked to the keys the figures like

subNode_->Translate(Vector3::LEFT * 0.2f);

for the left movement and

subNode_->Translate(Vector3::RIGHT * 0.2f);

for the right movement, however i cant succed to move it down, perhaps i can add some gravity ? or why doesnt Vector3::DOWN seem to work ? Thank you again :slight_smile:

-------------------------

Dave82 | 2019-06-21 18:30:40 UTC | #8

[quote="codefive, post:7, topic:5239"]
subNode_->Translate(Vector3::LEFT * 0.2f);
[/quote]
Use deltaTime to calculate your movement. The code above will result in different movement speed on various computers (lower fps slower movement and vice versa).
Also be aware that Translate() is performed in local space by default.

-------------------------

codefive | 2019-06-21 21:23:07 UTC | #9

Then will SetPosition would be a better solution?

-------------------------

Modanung | 2019-06-21 23:12:48 UTC | #10

When using rigid bodies it's better to apply forces to them instead of moving the nodes directly. This should happen during the `FixedUpdate(float timeStep)` of your `Component` using functions like:
- `RigidBody::ApplyForce(newtonsVec3 * timeStep)`
- `RigidBody::ApplyImpulse(newtonsVec3)`
- `RigidBody::ApplyTorque(newtonsVec3 * timeStep)`
- `RigidBody::ApplyTorqueImpulse(newtonsVec3)`

-------------------------

Modanung | 2019-06-21 23:22:04 UTC | #11

Furthermore there are several functions available to control passive slowing of your rigid bodies like:
- `RigidBody::SetLinearDamping(float)`
- `RigidBody::SetAngularDamping(float)`
- `RigidBody::SetFriction(float)`
- `RigidBody::SetRollingFriction(float)`
- `RigidBody::SetRestitution(float)`

-------------------------

Dave82 | 2019-06-22 03:58:16 UTC | #12

[quote="codefive, post:9, topic:5239, full:true"]
Then will SetPosition would be a better solution?
[/quote]

Just use Translate(delta * deltaTime , TS_WORLD) when you need world coords. (If you want to apply gravity , etc).

-------------------------

codefive | 2019-06-22 05:09:57 UTC | #13

Oh such a precious information, and those constants TS_WORLD and such as what name i cant find them in Urho documentation? Are more like those? I think now im starting to understand

-------------------------

Leith | 2019-06-22 05:44:05 UTC | #14

We don't yet support SpinningFriction...

-------------------------

Dave82 | 2019-06-22 06:25:14 UTC | #15

[quote="codefive, post:13, topic:5239, full:true"]
Oh such a precious information, and those constants TS_WORLD and such as what name i cant find them in Urho documentation? Are more like those? I think now im starting to understand
[/quote]

I never read the documentation because i found it useless. Well in some rare situations when i need some info about materials or techniques etc. But for simple things like this is usually use intellisense (VS) which gives me enough information about a function/class/enum once i type in my -> or . operator. Or i just type in / click a variable/function/enum and the code definition window opens the file and scrolls to the definition of the enum/class/function. Very useful and convenient feature. Way faster than searching hundreds of pages of  documentation which will give you the same information as opening the file... since Urho3d uses Doxygen.

-------------------------

Leith | 2019-06-22 06:37:32 UTC | #16

I wish Dave! I remember the "good old days of msvc" - lol!

Back on CodeBlocks, this time on Linux.
There's some kind of bug that forces me to turn off symbolic lookups, otherwise the entire editor runs at a snail pace. This means I don't get debug info from external libs, like Urho3D. Makes life interesting.

-------------------------

codefive | 2019-06-22 06:42:42 UTC | #17

I dont want to tell what to do to a programming guru as you @Leith but i find Netbeans IDE very good, especially version 11, i like it even better than Eclipse, intellisense very good and very few bugs.

-------------------------

Leith | 2019-06-22 06:51:52 UTC | #18

Yep its nice to have options.
I probably should look further into them.

I did not like the Linux version of microsoft's crossplatform "Code" IDE, I had used CodeBlocks previously on Windows, so I was already familiar with that IDE.

CodeBlocks on Linux has a lot of problems I could talk about, I am constantly closing and restarting it during my development day.

-------------------------

codefive | 2019-06-22 07:00:55 UTC | #19

I know what you are saying, i have it also installed here at my Linux and i never use it, i dont know if it would be silly from my part to say that i even like more SublimeText3 if i have to decide now between the two. But lots of people like code i think it has many bugs, but i dont want to throw dirt here.

-------------------------

codefive | 2019-06-22 07:05:14 UTC | #20

Could anybody help me to apply a Rigidbody to a node that has 3 sub-nodes ? When i try to do it i make the Engine crash :frowning: Well infact it crashes when i add a ApplyImpulse to that rigid body, and i dont know why

-------------------------

Modanung | 2019-06-22 08:31:23 UTC | #21

What does the debugger say?
Could you maybe also share the code or xml clarifying your node/component structure?

-------------------------

Leith | 2019-06-22 09:56:54 UTC | #22

Sure I can help you do that.
In one example, I have a rigidbody on my root node for an outer hull, and I also attached rigidbodies to some of the skeleton bones, these bodies are typically animated with the skeleton.
Do you just need an outer hull, or do you need child hulls as well?
The more you describe your use-case, the more help you're likely to get.

-------------------------

codefive | 2019-06-22 21:13:05 UTC | #23

All i want to create in the first class is a line, you know the tipical tetris line for that i used to use this code on the OnNodeSet method.- 

        for(int x=0; x<4; x++)
        {
            subNode = node->CreateChild("Box");
            subNode->SetPosition(Vector3(x, 0, 0));
            subNode->SetScale(node->GetScale());                    
            StaticModel* lineaObject=subNode->CreateComponent<StaticModel>();
            lineaObject->SetModel(cache->GetResource<Model>("Models/Box.mdl"));
            lineaObject->SetMaterial(cache->GetResource<Material>("Materials/Stone.xml"));
            lineaObject->SetCastShadows(true);

            auto* body = subNode->CreateComponent<RigidBody>();
            body->SetCollisionLayer(2);
            auto* shape = subNode->CreateComponent<CollisionShape>();
            shape->SetBox(subNode->GetPosition());
            
      }

The problem with this aproach is that i cannot access subnodes created with this method, i can only access the last one
I have modified the code to this.-

            subNode = node->CreateChild("Box");
            subNode->SetPosition(Vector3(0, 0, 0));
            subNode->SetScale(node->GetScale());                    
            StaticModel* lineaObject=subNode->CreateComponent<StaticModel>();
            lineaObject->SetModel(cache->GetResource<Model>("Models/Box.mdl"));
            lineaObject->SetMaterial(cache->GetResource<Material>("Materials/Stone.xml"));
            lineaObject->SetCastShadows(true);
            
            subNodeDos = subNode->CreateChild("Box");
            subNodeDos->SetPosition(Vector3(1, 0, 0));
            subNodeDos->SetScale(subNode->GetScale());                    
            StaticModel* lineaObjectDos=subNodeDos->CreateComponent<StaticModel>();
            lineaObjectDos->SetModel(cache->GetResource<Model>("Models/Box.mdl"));
            lineaObjectDos->SetMaterial(cache->GetResource<Material>("Materials/Stone.xml"));
            lineaObjectDos->SetCastShadows(true);
            
            subNodeTres = subNode->CreateChild("Box");
            subNodeTres->SetPosition(Vector3(2, 0, 0));
            subNodeTres->SetScale(subNode->GetScale());                    
            StaticModel* lineaObjectTres=subNodeTres->CreateComponent<StaticModel>();
            lineaObjectTres->SetModel(cache->GetResource<Model>("Models/Box.mdl"));
            lineaObjectTres->SetMaterial(cache->GetResource<Material>("Materials/Stone.xml"));
            lineaObjectTres->SetCastShadows(true);
            
            subNodeCuatro = subNode->CreateChild("Box");
            subNodeCuatro->SetPosition(Vector3(3, 0, 0));
            subNodeCuatro->SetScale(subNode->GetScale());                    
            StaticModel* lineaObjectCuatro=subNodeCuatro->CreateComponent<StaticModel>();
            lineaObjectCuatro->SetModel(cache->GetResource<Model>("Models/Box.mdl"));
            lineaObjectCuatro->SetMaterial(cache->GetResource<Material>("Materials/Stone.xml"));
            lineaObjectCuatro->SetCastShadows(true);
            
            auto* body = subNode->CreateComponent<RigidBody>();
            body->SetCollisionLayer(2);
            auto* shape = subNode->CreateComponent<CollisionShape>();
            shape->SetBox(subNode->GetPosition());
            
But now it crashes when in the FixedUpdate method i do the following.-

     auto* body = GetComponent<RigidBody>();
    
     Input* input=GetSubsystem<Input>();
	
        body->ApplyImpulse(Vector3::DOWN * timeStep);
    if(input->GetKeyDown(KEY_A))
        body->ApplyImpulse(Vector3::LEFT * timeStep);
    if(input->GetKeyDown(KEY_D))
        body->ApplyImpulse(Vector3::RIGHT * timeStep);

That is the class Line as it tryies to draw a line and so on i have arround 6 of them

-------------------------

jmiller | 2019-06-23 14:25:28 UTC | #24

Some brainstorming..

If CreateChild("BoxUno") / GetChild("BoxUno") is not just what you need, there are GetChildren(), GetChildrenByTagName(), etc.
  https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_node.html

    // Iterate immediate child nodes and output names; can be shorter as with auto or if you do not need the iterator.
    const Vector<SharedPtr<Node>>& children(node->GetChildren());
    for (Vector<SharedPtr<Node>>::ConstIterator n(children.Begin()); n != children.End(); ++n) {
      URHO3D_LOGINFO((*n)->GetName());
    }

-------------------------

Modanung | 2019-06-23 05:55:04 UTC | #25

...or using a range-based for loop:
```
for (SharedPtr<Node> n: node->GetChildren()) {
    URHO3D_LOGINFO(n->GetName());
}
```

-------------------------

Leith | 2019-06-23 06:39:58 UTC | #26

The only reason that the code you showed could be crashing, is that the node you are at, has no rigidbody component, and so your call to get that component returned a null pointer.
You have a classic null pointer access violation on your hands.
If we trace the execution stack, the last class (RigidBody) method we landed in at the moment of the crash, has "pThis=nullptr" - I am absolutely certain of this, without seeing your stack trace.

Here is what I suggest!
After you finish creating your scene using your code, dump the entire scene to XML file... this is super easy to do... now we can load the resulting XML file into the Urho3D Editor to examine the node hierarchy, and/or we can inspect the XML plaintext.
You may find the explanation for the null pointer by observing the data structure that resulted from your code. This is just one approach vector of course.

My current project used to create a scene in code and dump it to a file before proceeding. Currently, I just load that file, and use the Urho3D editor to modify it. I can always go back to square one.

-------------------------

Modanung | 2019-06-23 13:01:44 UTC | #27

Indeed, `node_ != subNode`
@codefive Maybe you're looking for `Node::GetChildrenWithComponent<RigidBody>(...)`?

-------------------------

codefive | 2019-06-23 18:20:05 UTC | #28

Thank you everyone for their help, i will try all that you told me and let you know !!!

-------------------------

Leith | 2019-06-24 07:55:52 UTC | #29

For future reference: if you "get a pointer to something", always check if the result is nullptr before attempting to use that pointer in a call. Always do error checking. Always. You cannot assume that you will be handed a valid pointer to something you asked for, particularly if it has already been destroyed. We can talk about smart pointers all day, but at the end of the day, it is your responsibility as a diligent coder to check. Use the debug logging facilities to loudly complain when something goes wrong, and check the log file to see what happened after the console closed.

URHO3D_LOGERROR("Oh dear something went wrong inside method X of class Y involving component Z connected to node W");

-------------------------

codefive | 2019-06-24 18:36:11 UTC | #30

@Leith i cant seem to debug under Linux, Netbeans says it cant find the "Linux executable" even though i provided the path :thinking:

-------------------------

SirNate0 | 2019-06-25 04:18:36 UTC | #31

I haven't used Netbeans in a while as I switched to using QtCreator a few years ago, so I'm not sure I can help with that (maybe it's a debug vs run configuration type of problem, or maybe it can't find gdb...). However, if you just want to get a stack trace to see where it's failing and maybe inspect one or two variables using gdb directly isn't that awful an experience.

-------------------------

