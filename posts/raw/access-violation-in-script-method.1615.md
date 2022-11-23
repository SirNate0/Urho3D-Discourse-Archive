godan | 2017-01-02 01:08:56 UTC | #1

So, I'm trying to expose some simple methods via Angelscript in one of my projects. The basic logistics of hooking up the script stuff is all working great. For instance, as a sanity check, the following method is exposed properly and runs as you would expect:

[code]
void AppAPI::LoadModel(String path)
{
     URHO3D_LOGINFO("hello");
}
[/code]

When I try to actually do something in that same function (see below), I get an access violation error:

[code]
void AppAPI::LoadModel(String path)
{
	GetScene()->CreateChild("TestNode");
}
[/code]

The actual error is:

"The thread tried to read from or write to an address for which it does not have the appropriate access"

Here is my little API class in its entirety:

[code]
#include "AppAPI.h"
#include "AppConsole.h"
#include <Urho3D/Script/APITemplates.h>

AppAPI* AppAPI::instance_;

AppAPI::AppAPI(Context* context): Component(context)
{
	instance_ = this; 
	//scene_ = GetScene();
	AppAPI::RegisterObject(context);
}

AppAPI::~AppAPI()
{

}

void AppAPI::RegisterObject(Context* context)
{
	asIScriptEngine* engine = AppConsole::instance_->script_engine_->GetScriptEngine();
	RegisterComponent<AppAPI>(engine, "AppAPI");
	engine->RegisterObjectMethod("AppAPI", "void LoadModel(String)", asMETHOD(AppAPI, LoadModel), asCALL_THISCALL);
	engine->RegisterGlobalProperty("AppAPI @api", instance_);
	//engine->RegisterObjectProperty("AppAPI", "Scene@ scene", offsetof(AppAPI, scene_));
}

void AppAPI::LoadModel(String path)
{
	GetScene()->CreateChild("TestNode");
}
[/code]

Any thoughts?

-------------------------

godan | 2017-01-02 01:08:56 UTC | #2

Also, it's worth adding that my scene is all set up and working fine. In fact, I can call that same function in C++ without any errors. It seems that it's just the access from the script.

-------------------------

