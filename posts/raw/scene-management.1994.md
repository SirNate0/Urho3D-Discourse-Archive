shipiz | 2017-01-02 01:12:08 UTC | #1

Hi everyone,

I've just started using Urho and i'm curious how do you guys manage your scenes that are creating only within code.
In all the examples scene instance is created in a class which extends Application. But how would you do it if you have multiple scenes

I've tried creating a class that extends Object and creating a scene, but i'm not sure if this is the right way.
The idea is to have a class that represents single scene.

Best

-------------------------

1vanK | 2017-01-02 01:12:08 UTC | #2

Not sure I understand the question correctly, but 
[code]
Scene* myScene20 = new Scene(context_);[/code]
or
[code]SharedPtr<Scene> myScene(new Scene(context_));[/code]
will be work in any Object.

For multiples scenes you can see 10_RenderToTexture example

-------------------------

shipiz | 2017-01-02 01:12:08 UTC | #3

What i mean is scene changing, for example, i might have menu scene and when i click play i would create a game scene where all of my game nodes will be.

How would you organise code like that ? Lets assume that i won't be loading anything from scene files and ill be creating all nodes programatically.
Now to gain access to subsystems, events etc. in a arbitrary class where scene object will be instantiated i would be required to either pass Application instance or extend Object, is that correct ?

-------------------------

1vanK | 2017-01-02 01:12:08 UTC | #4

U can use own subsystem for global variables. Also never switch the current scene in the middle of the game cycle. Only in beginning game cycle prior to the occurrence of any events (just use varibale nextScene_ for it). For real example u can see [github.com/1vanK/FlappyUrho](https://github.com/1vanK/FlappyUrho) . There's no switching of scenes, but there are switching game states (in HandleBeginFrame). To switch scenes use the same code

-------------------------

1vanK | 2017-01-02 01:12:08 UTC | #5

If you want to separate the processing of events of scenes from other code, you can also make scene components like node components (see component PhysicsWorld)

-------------------------

shipiz | 2017-01-02 01:12:09 UTC | #6

I've inspected your code, i already saw few examples like yours. But still it doesn't answer my question. Here is the deal

Lets say i have few scenes, like

- Menu
- Settings
- Game
- Game Over

All of the scenes for example will be loaded from xml files, and on top of that i'll add more objects that are dynamic and not hardcoded into scene xml file, like populating list view from my model etc.

What i don't get it is how would you switch those scenes. The idea i have is to wrap a scene in a custom class, that will be responsible for all of the events/data/assets for that particular scene. This way i can logically divide scenes into different classes and instantiate them whenever i need it to replace the current scene. But i'm not sure how will this impact main loop, because scene switch could happen on a button click or a timed event.

-------------------------

1vanK | 2017-01-02 01:12:09 UTC | #7

[quote="shipiz"]The idea i have is to wrap a scene in a custom class, that will be responsible for all of the events/data/assets for that particular scene[/quote]

use scene component

-------------------------

rasteron | 2017-01-02 01:12:09 UTC | #8

Hey there,

Welcome to the forums. Hmm.. I think you're looking for a typical FSM implementation inside Urho3D. It should be the same as any typical FSM since the engine works mostly with events. A related topic here: [topic67.html](http://discourse.urho3d.io/t/event-handler-concurrency/89/1) 

If you're new to Urho, I think you should familiarize yourself first on how events, updates, fixed updates, script instance and subscriptions works with Urho. If you already know that then creating your own FSM won't be a problem.

Hope that helps.

-------------------------

shipiz | 2017-01-02 01:12:09 UTC | #9

[quote="1vanK"]

use scene component[/quote]

Aha, so idea is to subclass component, that will basically hold all the elements for a particular "scene", and attach it to main scene as necessary right ?

-------------------------

1vanK | 2017-01-02 01:12:09 UTC | #10

[quote="shipiz"][quote="1vanK"]

use scene component[/quote]

Aha, so idea is to subclass component, that will basically hold all the elements for a particular "scene", and attach it to main scene as necessary right ?[/quote]

no, attach special components to particular scenes :)

[code]HandleNewGame()
{
    level1 = new Scene(context);
    level1->CreateComponent<Level1Logic>();
}

class Level1Logic:public Component
{
    OnSceneSet()
    {
         // Creating the scene
    }

     HandleUpdate()
     {
          ...
     }
}
[/code]

-------------------------

shipiz | 2017-01-02 01:12:11 UTC | #11

Thanks, will try that. 

So basically i'll have only one scene, and menus, gameplay etc will practically be components. But going this way, can i have for example part of the scene menu component loaded from scene file and part dynamically added ?

-------------------------

1vanK | 2017-01-02 01:12:11 UTC | #12

[code]        scene_ = new Scene(context_);
        /// Load scene from file
        SharedPtr<File> file = cache->GetFile("Scenes/SceneLoadExample.xml");
        scene_->LoadXML(*file);
        scene_->CreateComponent<SceneLogic>();

void SceneLogic::OnSceneSet(Scene* scene)
{
    /// Add dynamic parts
    auto cameraNode = scene->CreateChild("Camera");
    cameraNode->CreateComponent<Camera>();
    cameraNode->SetPosition(Vector3(0.0f, 5.0f, 0.0f));
}
[/code]

-------------------------

