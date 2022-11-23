rogerdv | 2017-01-02 01:00:51 UTC | #1

Yesterday I tested at home the windows compilation, cmake worked perfectly and generated the projects, but compilation fails:

[code]Build started 22/10/2014 19:30:54.
     1>Project "D:\work\dnt-u3d\Build\dnt.vcxproj" on node 3 (build target(s)).
     1>InitializeBuildStatus:
         Creating "dnt.dir\Release\dnt.unsuccessfulbuild" because "AlwaysCreate" was specified.
       CustomBuild:
         Building Custom Rule D:/work/dnt-u3d/Source/CMakeLists.txt
         CMake does not need to re-run because D:\work\dnt-u3d\Build\CMakeFiles\generate.stamp is up-to-date.
       ClCompile:
         C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\bin\CL.exe /c /I"C:\Program Files (x86)\Microsoft DirectX SDK (June 2010)\Include" /ID:\work\Urho3D\Source\Engine /ID:\work\Urho3D\Source\Engine\Audio /ID:\work\Urho3D\Source\Engine\Container /ID:\work\Urho3D\Source\Engine\Core /ID:\work\Urho3D\Source\Engine\Engine /ID:\work\Urho3D\Source\Engine\Graphics /ID:\work\Urho3D\Source\Engine\Input /ID:\work\Urho3D\Source\Engine\IO /ID:\work\Urho3D\Source\Engine\LuaScript /ID:\work\Urho3D\Source\Engine\Math /ID:\work\Urho3D\Source\Engine\Navigation /ID:\work\Urho3D\Source\Engine\Network /ID:\work\Urho3D\Source\Engine\Physics /ID:\work\Urho3D\Source\Engine\Resource /ID:\work\Urho3D\Source\Engine\Scene /ID:\work\Urho3D\Source\Engine\Script /ID:\work\Urho3D\Source\Engine\UI /ID:\work\Urho3D\Source\Engine\Urho2D /ID:\work\Urho3D\Source\ThirdParty\Box2D /ID:\work\Urho3D\Source\ThirdParty\Bullet\src /ID:\work\Urho3D\Source\ThirdParty\kNet\include /ID:\work\Urho3D\Source\ThirdParty\SDL\include /ID:\work\Urho3D\Source\ThirdParty\AngelScript\include /ID:\work\Urho3D\Build\Engine /Zi /nologo /W3 /WX- /O2 /Ob2 /Oy- /D WIN32 /D _WINDOWS /D NDEBUG /D _SECURE_SCL=0 /D URHO3D_SSE /D URHO3D_PROFILING /D URHO3D_LOGGING /D URHO3D_ANGELSCRIPT /D URHO3D_NAVIGATION /D URHO3D_PHYSICS /D URHO3D_STATIC_DEFINE /D _CRT_SECURE_NO_WARNINGS /D "CMAKE_INTDIR=\"Release\"" /D _MBCS /Gm- /EHsc /MD /GS- /arch:SSE /fp:fast /Zc:wchar_t /Zc:forScope /GR /Fo"dnt.dir\Release\\" /Fd"dnt.dir\Release\vc100.pdb" /Gd /TP /analyze- /errorReport:prompt ..\Source\main.cpp
         main.cpp
     1>..\Source\main.cpp(7): error C4430: missing type specifier - int assumed. Note: C++ does not support default-int
     1>Done Building Project "D:\work\dnt-u3d\Build\dnt.vcxproj" (build target(s)) -- FAILED.

Build FAILED.

Time Elapsed 00:00:01.17[/code]

The line producing the error is this:

[code]DEFINE_APPLICATION_MAIN(App)[/code]

I have copied code from Samples.h and .inl, trying to make my opwn project, but seems I missed something here.

-------------------------

JTippetts | 2017-01-02 01:00:52 UTC | #2

What does line 7 of your main.cpp file look like?

-------------------------

rogerdv | 2017-01-02 01:00:52 UTC | #3

[quote="JTippetts"]What does line 7 of your main.cpp file look like?[/quote]

[code]DEFINE_APPLICATION_MAIN(App)[/code]

-------------------------

cin | 2017-01-02 01:00:52 UTC | #4

Minimal app:

[spoiler][b]UrhoQuickStart.h[/b]
[code]#pragma once
#include "Application.h"
using namespace Urho3D;

class UrhoQuickStart : public Application
{
    OBJECT(UrhoQuickStart);
public:
    UrhoQuickStart(Context* context);
    virtual void Start();
private:
    void CreateText();
    void HandleUpdate(StringHash eventType, VariantMap& eventData);
    void HandleKeyDown(StringHash eventType, VariantMap& eventData);
    void HandleSceneUpdate(StringHash eventType, VariantMap& eventData);
};[/code]

[b]UrhoQuickStart.cpp[/b]
[code]#include "CoreEvents.h"
#include "SceneEvents.h"
#include "Engine.h"
#include "Font.h"
#include "Input.h"
#include "ProcessUtils.h"
#include "Text.h"
#include "UI.h"
#include "ResourceCache.h"
#include "DebugNew.h"
#include "Scene.h"
#include "Graphics.h"
#include "UrhoQuickStart.h"

DEFINE_APPLICATION_MAIN(UrhoQuickStart)

UrhoQuickStart::UrhoQuickStart(Context* context) : Application(context)
{
    engineParameters_["WindowTitle"] = GetTypeName();
    engineParameters_["FullScreen"]  = false;
    engineParameters_["Headless"]    = false;
}

void UrhoQuickStart::Start()
{
    SubscribeToEvent(E_KEYDOWN, HANDLER(UrhoQuickStart, HandleKeyDown));
    SubscribeToEvent(E_SCENEUPDATE, HANDLER(UrhoQuickStart, HandleSceneUpdate));
    SubscribeToEvent(E_UPDATE, HANDLER(UrhoQuickStart, HandleUpdate));
    CreateText();
}

void UrhoQuickStart::CreateText()
{
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    SharedPtr<Text> helloText(new Text(context_));
    helloText->SetText("Hello World from Urho3D!");
    helloText->SetFont(cache->GetResource<Font>("Fonts/Anonymous Pro.ttf"), 30);
    helloText->SetColor(Color(0.0f, 1.0f, 0.0f));
    helloText->SetHorizontalAlignment(HA_CENTER);
    helloText->SetVerticalAlignment(VA_CENTER);
    GetSubsystem<UI>()->GetRoot()->AddChild(helloText);
}

void UrhoQuickStart::HandleUpdate(StringHash eventType, VariantMap& eventData)
{
}

void UrhoQuickStart::HandleKeyDown(StringHash eventType, VariantMap& eventData)
{
	using namespace KeyDown;
	int key = eventData[P_KEY].GetInt();
	if (key == KEY_ESC)
	{
		engine_->Exit();
	}
}

void UrhoQuickStart::HandleSceneUpdate(StringHash eventType, VariantMap& eventData)
{
}[/code][/spoiler]

-------------------------

rogerdv | 2017-01-02 01:00:55 UTC | #5

Thanks, I tested thi s minimal apps and it compiles (and runs) perfectly.

-------------------------

