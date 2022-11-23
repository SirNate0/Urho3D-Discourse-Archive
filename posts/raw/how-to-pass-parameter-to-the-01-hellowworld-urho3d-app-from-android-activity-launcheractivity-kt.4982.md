majhong | 2019-03-01 08:59:30 UTC | #1

i have a string of user's profile in anddroid LauncherActivity

i want paas it to  a urho app

-------------------------

Leith | 2019-03-01 10:01:36 UTC | #2

im sorry i cant advise yet, but i am getting there rapidly - within two weeks I guess, I will have an android build

-------------------------

Miegamicis | 2019-03-01 11:03:59 UTC | #3

There is @Lumak repositories on Github which provide samples for that.
https://github.com/Lumak/Urho3D-Android-Project
See the `ServiceCmd` class for more details.

-------------------------

majhong | 2019-03-04 04:44:06 UTC | #4

i can invode function between activity and .so through jni.
i want a  urho3d 'offical'  solution .

-------------------------

majhong | 2019-03-04 06:57:12 UTC | #5

    /**
     * This method is called by SDL before starting the native application thread.
     * It can be overridden to provide the arguments after the application name.
     * The default implementation returns an empty array. It never returns null.
     * @return arguments for the native application.
     */
    protected String[] getArguments() {
        // Urho3D: the default implementation returns the "app_process" as the first argument instead of empty array
        return new String[]{"app_process"};
    }





this is a graceful solution

-------------------------

weitjong | 2019-03-04 07:02:42 UTC | #6

Yes. Just remember that Urho3D engine expects the arguments in the same format as other platforms. i.e. Arg 0th in the array for the name of the program/process, arg 1st is the first argument from the app's perspective, and so on.

-------------------------

Miegamicis | 2019-04-11 13:21:56 UTC | #7

Spent last few days working with the Android build system and came across the same issue. I see that the engine doesn't support out of the box solution how the custom events could be handled between the Android app and the Urho application at runtime. Shouldn't we think of a way how to implement this in the engine core? Basically implementing the same thing that @Lumak achieved and adding some sort of documentation how to use it.

-------------------------

weitjong | 2019-04-11 15:23:49 UTC | #8

Personally I don't see what's wrong with the current approach of how Application and Engine classes handles the parameters.

-------------------------

Miegamicis | 2019-04-11 16:00:41 UTC | #9

No, I mean when the application is actually running and I need to send some sort of events back and forth for ads, login events etc. and I would like to keep the game running in the background and waiting for specific events.

-------------------------

weitjong | 2019-04-11 16:11:34 UTC | #10

I guess it’s a different topic then. I have no comment on that.

-------------------------

Leith | 2019-04-12 04:00:00 UTC | #11

You can use custom events, which are handled by your gamestate implementation(s)  via your gamestatemanager fsm...
Well, that's how I handled things in my gamestate manager. High-level requests are monitored by gamestatemanager, which operates in the background, and owns in my case, four states - intro, loading, menu and gameplay (all remain resident, but usually, only one is active). Next level down, the gamestate implementations for each major state have a chance to monitor for custom events too, and finally, in the custom urho component classes, we can do this one more time, so there are many levels at which we can take control. It's a lot of control.

I chose to make my game overlord object be derived from Urho's object class, so that it can deal with events...

[code]
    class GameStateManager : public Object
    {
        URHO3D_OBJECT(GameStateManager, Object);
    public:

        /// Factory Function
        static void RegisterObject(Context* context){
            context->RegisterFactory<ClassName>();
        }
[/code]

-------------------------

Leith | 2019-04-12 03:49:59 UTC | #12

The short answer is - create a background layer object that owns the game scene, and possibly other scenes too - I can show you my pattern for a game state machine for urho that handles a custom event: request for change game scene, and has a handler for handling notification of scene change completion

-------------------------

Leith | 2019-04-12 04:11:18 UTC | #13

There is a long answer too.
Here is my current top level code.
The application object is the top level object.
Under it, lives our state manager, and under that, the game states.

[code]
class MyApp : public Urho3D::Application
{

private:
    WeakPtr<Scene> mgrscene_;
    WeakPtr<Scene> gamescene_;
    WeakPtr<Text> text_;
    WeakPtr<Node> cameraNode_;
    SharedPtr<GameState::GameStateManager> handler;

public:
    MyApp(Context* context) :
        Application(context)
    {
    }
    virtual void Setup()
    {
        // Called before engine initialization. engineParameters_ member variable can be modified here
        engineParameters_["FullScreen"]=false;
        engineParameters_["WindowWidth"]=1280;
        engineParameters_["WindowHeight"]=720;
        engineParameters_["WindowResizable"]=true;
        //engine_->DumpResources();
    }
    virtual void Start()
    {

        // Engine has FPS capped at max. 200
        // Let's remove that cap for debug purposes
        //
        engine_->SetMaxFps(9999);

        // Register the AngelScript subsystem (a non-core subsystem)
        context_->RegisterSubsystem(new Script(context_));

        // Create 'Manager Scene' and 'Game Scene'
        mgrscene_  = new Scene(context_); mgrscene_->SetName("Manager Scene");

        // Create GameState Manager
        // This will register all relevant classes
        handler = new GameState::GameStateManager(context_);

        // Initialize GameState Manager
        // This will instantiate all gamestate classes
        handler->start(mgrscene_);



        // Register application handlers for "Core Events":
        // E_BEGINFRAME                 (Start of frame event)
        // E_UPDATE                     (Logic update event, usually used to do "normal" stuff each frame)
        // E_POSTUPDATE                 (Logic post-update event)
        // E_RENDERUPDATE               (Render update event)
        // E_POSTRENDERUPDATE           (Post-render update event)
        // E_ENDFRAME                   (End frame event)
        // See https://github.com/urho3d/Urho3D/wiki/Events for a complete list of possible events
        //
        SubscribeToEvent(E_KEYDOWN,URHO3D_HANDLER(MyApp,HandleKeyDown)); // we're just watching the ESCAPE and TAB keys here

        // Set mouse behaviour
        //GetSubsystem<Input>()->SetMouseMode(MM_RELATIVE);

    }
[/code]

Amusingly, I don't actually use the gamescene defined in this class - gameplaystate is a substate of the gamestate manager, so some redundant code here but you get the idea

-------------------------

Miegamicis | 2019-04-12 06:52:34 UTC | #14

I was talking about events between Java and C++, I know how to send a command from C++ to Java but not the other way around. I see that Lumak updated the SDL library in the engine to support additional method which would process custom events between C++ and Java but the code at the moment is not a part of the engine and I would like to change that.

-------------------------

orefkov | 2019-11-07 14:23:50 UTC | #15

There is old thread, but look at this PR - https://github.com/urho3d/Urho3D/pull/2538
Maybe it will be useful to someone.

-------------------------

