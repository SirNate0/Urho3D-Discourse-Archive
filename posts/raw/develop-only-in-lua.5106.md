Lunarovich | 2019-04-17 07:32:05 UTC | #1

Is it a viable solution to develop an entiry game only in Lua? And if it is, how one proceeds with it? Can we use, for example, only Urho3DPlayer with a resource path prefix specified? Or is it OK to use some minimal Lua C++ hook file, something like the following

    using namespace Urho3D;

    Game::Game(Context* context):
        Application(context)
    {

    }

    void Game::Setup()
    {
        engineParameters_["FullScreen"] = false;
    }

    void Game::Start()
    {
        LuaScript* script = new LuaScript(context_);
        context_->RegisterSubsystem(script);

        script->ExecuteFile("LuaScripts/01_HelloWorld.lua");
        LuaFunction* start = script->GetFunction("Start");
        start->BeginCall();
        start->EndCall();    
    }

    void Game::Stop()
    {

    }

    URHO3D_DEFINE_APPLICATION_MAIN(Game)

Or there's some other more canonic way to do it?

-------------------------

orefkov | 2019-04-17 07:52:57 UTC | #2

I have some games for android in playmarket, writed only on Urho3dPlayer + AngelScript (it worked on desktop too).
And since the script wrapper is done for both AngelScript and Lua, I see no reason why this was impossible. Current player check script file extension and run AngelScript or Lua engines.

-------------------------

Bluemoon | 2019-04-17 07:56:03 UTC | #3

As much as I know, you can develop an entire game either with lua or AngelScript in Urho3D with just the Urho3DPlayer  as it is. But if you feel you need additional functionalities exposed then you would have to create bindings for those.

The bottom line is that most of the things needed are already exposed to the scripting subsystems by default

-------------------------

JTippetts | 2019-04-17 09:29:21 UTC | #4

The initial prototype of my game was written in Lua. It is viable.

In my experience, the AngelScript side of things is tighter and probably superior to the Lua side, as there are still some [issues](https://github.com/urho3d/Urho3D/issues/649) with Lua garbage collection that are intrinsic to using tolua++ to generate the bindings. Some care needs to be used when using Lua; ie, avoid generating Urho3D object garbage inside large range loops, or explicitly calling collectgarbage() at intervals inside those loops to clear out garbage before it accumulates. Where this has bitten me in the ass before has been double-nested loops iterating on images and generating Color garbage, and double-nested loops iterating on a tile map and generating Vector3 garbage. The issue manifests as increasing time spent in garbage collection every cycle, as the GC iterates large internal tables, and if allowed to grow large enough it can severely reduce framerate and cause tangible hitches or hiccups.

To circumvent issues like this, it is best to limit the amount of Lua object garbage you generate in a frame. My solution was to implement the 'heavy' routines (procedural level generation tasks, iterating tilemaps or images, etc...) as C++ routines exposed to Lua script so that they don't generate 65k temporary objects all in one whack to choke the GC. (This is probably a good idea anyway, even without the GC issue, to keep performance of these tasks as tight as possible.)

-------------------------

