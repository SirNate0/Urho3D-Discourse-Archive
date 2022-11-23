rogerdv | 2017-01-02 01:01:23 UTC | #1

Im planning to start an RPG project and I would like to get some feedback from more experienced users. I would like to script as much as possible, but I cant define what should I implement in C and what in scripting language. My first idea was to have a basic launcher, game states and the data structures (the game data, entities/items class, etc) in C++, but then I noticed that such thing would require generating glue code with some tool. So, Im thinking that perhaps everything should be declared in scripts: data, states,. everything and keep the launcher minimal. 
Any suggestions about this?

-------------------------

OvermindDL1 | 2017-01-02 01:01:24 UTC | #2

AngelScript is the fastest scripting language in Urho3D right now due to luajit using the LUA API instead of its FFI layer, however AS is also quite blazingly fast, should not worry too much about doing all your scripting in it.  If necessary you can write some things in C++ later if the need arises due to speed or so reasons, but should start with scripting.

-------------------------

rogerdv | 2017-01-02 01:01:24 UTC | #3

After reading a lot the docs last night and studying the samples, I couldnt find a way to share C++ declared classes with scripts, except for using an external tool to create the wrapper code. So, I guess that I have to stick to full scripting, including all classes declarations and such.

-------------------------

rogerdv | 2017-01-02 01:01:25 UTC | #4

Well, then the question is: how to expose my C++ code to AngelScript? Or lua, in case I switch later to it.

-------------------------

silverkorn | 2017-01-02 01:01:25 UTC | #5

I guess you can follow these files as guidelines:
AngelScript bindings: [github.com/urho3d/Urho3D/tree/m ... ine/Script](https://github.com/urho3d/Urho3D/tree/master/Source/Engine/Script) (Exposed by CMake [url=https://github.com/urho3d/Urho3D/blob/master/Source/Engine/Script/CMakeLists.txt#L24]here[/url])
Lua bindings (using tolua++ with ".pkg" files): [github.com/urho3d/Urho3D/tree/m ... cript/pkgs](https://github.com/urho3d/Urho3D/tree/master/Source/Engine/LuaScript/pkgs) (Exposed by CMake [url=https://github.com/urho3d/Urho3D/blob/master/Source/Engine/LuaScript/CMakeLists.txt#L44]here[/url])

-------------------------

OvermindDL1 | 2017-01-02 01:01:25 UTC | #6

You can easily make your own library and link in to your C++ project as well (which is what I am doing if scripting is enabled).  I do admit that we need a method of importing our bindings into the normal Script class, perhaps an even that is sent when a Script or so instance is created so you can link in your own bindings to it.

-------------------------

rogerdv | 2017-01-02 01:01:25 UTC | #7

I was thinking to get the aslScriptEngine from the Urho3D::Script class and register my classes and variables directly there. Probably is going to be my homework for this weekend to check if this idea works or not.

-------------------------

Azalrion | 2017-01-02 01:01:25 UTC | #8

Yep thats the way to do it.

-------------------------

OvermindDL1 | 2017-01-02 01:01:25 UTC | #9

Problem with that method is that your registrations will not happen if it is, say, loaded from a scene or something.  We really need a callback event or so.  :slight_smile:

-------------------------

Azalrion | 2017-01-02 01:01:25 UTC | #10

Um what, no you dont just follow the same practice as base urho3d after script subsystem has been created but before you use anything register your apps own bindings. Script is a subsystem so is application scope not scene scope and can be done right at startup.

In MyGame : Application i have:
[code]
MyGame::MyGame(Context* context) :
    Application(context)
{
    context->RegisterSubsystem(new Script(context));

    RegisterScriptAPI(GetSubsystem<Script>()->GetScriptEngine());
}
[/code]

Then a static function (separate header file for me)
[code]
class asIScriptEngine;

void RegisterIOAPI(asIScriptEngine* engine);

void RegisterScriptAPI(asIScriptEngine* engine)
{
    ...
    RegisterIOAPI(engine);
    ...
}
[/code]

Then in a cpp file:
[code]
#include "ScriptAPI.h"
#include "IO/Locale.h"
#include "IO/Settings.h"
#include "IO/Bindings.h"

#include <APITemplates.h>
#include <angelscript.h>

using namespace Urho3D;

static void LocaleReplacePODVector(String& line, CScriptArray* tokens, Locale* ptr)
{
    ptr->Replace(line, ArrayToVector<String>(tokens));
}

static Locale* GetLocale()
{
    return GetScriptContext()->GetSubsystem<Locale>();
}

static Settings* GetSettings()
{
    return GetScriptContext()->GetSubsystem<Settings>();
}

static Bindings* GetBindings()
{
    return GetScriptContext()->GetSubsystem<Bindings>();
}

static void RegisterSettings(asIScriptEngine* engine)
{
    RegisterObject<Settings>(engine, "Settings");
    engine->RegisterObjectMethod("Settings", "const Variant& GetSetting(const String&in, const Variant&in = Variant()) const", asMETHOD(Settings, GetSetting), asCALL_THISCALL);
    engine->RegisterObjectMethod("Settings", "void SetSetting(const String&in, const Variant&in)", asMETHOD(Settings, SetSetting), asCALL_THISCALL);
    engine->RegisterGlobalFunction("Settings@+ get_settings()", asFUNCTION(GetSettings), asCALL_CDECL);
}

static void RegisterLocale(asIScriptEngine* engine)
{
    RegisterObject<Locale>(engine, "Locale");
    engine->RegisterObjectMethod("Locale", "String Localize(uint,uint) const", asMETHOD(Locale, Localize), asCALL_THISCALL);
    engine->RegisterObjectMethod("Locale", "void Replace(String&in, uint, const String&in) const", asMETHODPR(Locale, Replace, (Urho3D::String& line, unsigned token, const Urho3D::String& value) const, void), asCALL_THISCALL);
    engine->RegisterObjectMethod("Locale", "void Replace(String&in, Array<String>@+) const", asFUNCTION(LocaleReplacePODVector), asCALL_CDECL_OBJLAST);
    engine->RegisterGlobalFunction("Locale@+ get_locale()", asFUNCTION(GetLocale), asCALL_CDECL);
}

static void RegisterBindings(asIScriptEngine* engine)
{
    RegisterObject<Bindings>(engine, "Bindings");
    engine->RegisterObjectMethod("Bindings", "int get_actionKey(const String&in) const", asMETHOD(Bindings, GetActionScanCode), asCALL_THISCALL);
    engine->RegisterObjectMethod("Bindings", "void set_actionKey(const String&in, int)", asMETHOD(Bindings, SetActionScanCode), asCALL_THISCALL);
    engine->RegisterGlobalFunction("Bindings@+ get_bindings()", asFUNCTION(GetBindings), asCALL_CDECL);
}

void RegisterIOAPI(asIScriptEngine* engine)
{
    RegisterLocale(engine);
    RegisterSettings(engine);
    RegisterBindings(engine);
}
[/code]

Doesnt really need to be in separate cpp files from the actual classes but i prefer it that way.

-------------------------

cadaver | 2017-01-02 01:01:26 UTC | #11

When you use custom C++ classes in AngelScript, then those should be always bound by the executable(s) that you're running in your project. I don't think runtime dynamic binding is a good idea, because in AngelScript the whole interface should be registered before you start running scripts at all. This means also that you should make a custom executable for running eg. the editor with your classes bound in, basically a replacement for Urho3DPlayer. It's very simple, just instantiate the Urho3D engine, instantiate the AngelScript subsystem, add your own classes' bindings, load the script, run it.

-------------------------

