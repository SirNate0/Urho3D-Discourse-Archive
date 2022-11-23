Lunarovich | 2017-01-02 01:10:34 UTC | #1

Hello! I'm trying to run Lua scripts. Everything is going fine except for the event subscribing. 

So, I start by loading and executing lua files in the .cpp:

[code]    
cache->GetResource<LuaFile>("LuaScripts/01_HelloWorld.lua");
cache->GetResource<LuaFile>("LuaScripts/Utilities/Sample.lua");

LuaScript* script = new LuaScript(context_);

script->ExecuteFile("LuaScripts/01_HelloWorld.lua");
LuaFunction* start = script->GetFunction("Start");
start->BeginCall();
start->EndCall();
[/code]

After building and running the project I get following messages:

[img]http://i.imgur.com/XblZPyQ.png?1[/img]

Apparently, something is preventing Lua scripts from registering events... Or should I put something specific in the .cpp code?

-------------------------

Lunarovich | 2017-01-02 01:10:35 UTC | #2

I'll post the entire program here in order to make it clear what I'm doing. So, I'm just trying to hook in Lua script into Main.cpp and continue development in Lua from that point (I know I'm not supposed to do all the dev in Lua, but I want to do it for the sake of learning and fun). Here is the entire code:

[code]
#include <Urho3D/Engine/Application.h>
#include <Urho3D/Engine/Engine.h>
#include <Urho3D/Input/InputEvents.h>
using namespace Urho3D;
class MyApp : public Application
{
public:
  MyApp(Context* context) :
    Application(context)
  {
  }
  virtual void Setup()
  {
    // Called before engine initialization. engineParameters_ member variable can be modified here
    engineParameters_["FullScreen"] = false;

    context_->RegisterSubsystem(new LuaScript(context_));
  }
  virtual void Start()
  {
    // Called after engine initialization. Setup application & subscribe to events here
    SubscribeToEvent(E_KEYDOWN, URHO3D_HANDLER(MyApp, HandleKeyDown));

    LuaScript* luaScript = new LuaScript(context_);
    luaScript->ExecuteFile("Data/LuaScripts/TestScene.lua");
    LuaFunction* lf = luaScript->GetFunction("Start");
    lf->BeginCall();
    lf->EndCall();
  }
  virtual void Stop()
  {
    // Perform optional cleanup after main loop has terminated
  }
  void HandleKeyDown(StringHash eventType, VariantMap& eventData)
  {
    using namespace KeyDown;
    // Check for pressing ESC. Note the engine_ member variable for convenience access to the Engine object
    int key = eventData[P_KEY].GetInt();
    if (key == KEY_ESC)
      engine_->Exit();
  }
};
URHO3D_DEFINE_APPLICATION_MAIN(MyApp)
[/code]

The example works just fine. However, I cannot subscribe to any event via Lua script. Lua complains that it cannot find callback functions specified in respective SubscribeToEvent function calls. So, everything gets loaded, displayed and animated, but there is no input handling, no scene update, etc.

-------------------------

Lunarovich | 2017-01-02 01:10:56 UTC | #3

OK, I've figured it out. I was forgetting to register a particular Lua script with the context:

[code]
#include <Urho3D/Engine/Application.h>
#include <Urho3D/Engine/Engine.h>
#include <Urho3D/Input/InputEvents.h>
using namespace Urho3D;
class MyApp : public Application
{
public:
  MyApp(Context* context) :
    Application(context)
  {
  }
  virtual void Setup()
  {
    // Called before engine initialization. engineParameters_ member variable can be modified here
    engineParameters_["FullScreen"] = false;
    
    // THIS LINE HAS NO EFFECT SINCE THE POINTER TO THE new LuaScript IS LOST
    context_->RegisterSubsystem(new LuaScript(context_));
  }
  virtual void Start()
  {
    // Called after engine initialization. Setup application & subscribe to events here
    SubscribeToEvent(E_KEYDOWN, URHO3D_HANDLER(MyApp, HandleKeyDown));

    LuaScript* luaScript = new LuaScript(context_);

    // REGISTER luaScript WITH the context_
    context_->RegisterSubsystem(luaScript);

    luaScript->ExecuteFile("Data/LuaScripts/TestScene.lua");
    LuaFunction* lf = luaScript->GetFunction("Start");
    lf->BeginCall();
    lf->EndCall();
  }
  virtual void Stop()
  {
    // Perform optional cleanup after main loop has terminated
  }
  void HandleKeyDown(StringHash eventType, VariantMap& eventData)
  {
    using namespace KeyDown;
    // Check for pressing ESC. Note the engine_ member variable for convenience access to the Engine object
    int key = eventData[P_KEY].GetInt();
    if (key == KEY_ESC)
      engine_->Exit();
  }
};
URHO3D_DEFINE_APPLICATION_MAIN(MyApp)
[/code]

-------------------------

thebluefish | 2017-01-02 01:11:04 UTC | #4

Instead of creating a new LuaScript subsystem, why not just use the existing?

[code]
LuaScript* luaScript = context_->GetSubsystem<LuaScript>();
[/code]

-------------------------

