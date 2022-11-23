TheComet | 2017-01-02 01:09:36 UTC | #1

Hi!

I'm trying to load a scene XML in lua but Urho3DPlayer is segfaulting. Am I doing something wrong, or is this an issue that needs to be fixed?

I created a scene in Urho3D's editor and saved it under Data/Scenes/ramps.xml.

Loading the scene using C++ [i]works fine[/i]:
[code]void App::CreateScene()
{
	ResourceCache* cache = GetSubsystem<ResourceCache>();

	scene_ = SharedPtr<Scene>(new Scene(context_));
	XMLFile* sceneFile = cache->GetResource<XMLFile>("Scenes/Ramps.xml");
	scene_->LoadXML(sceneFile->GetRoot());
}[/code]

I then tried to re-write the above in Lua and ran it using [b]Urho3DPlayer[/b], but it segfaults.
[code]function CreateScene()
    scene_ = Scene()
    local sceneXML = cache:GetResource("XMLFile", "Scenes/Ramps.xml")
    scene_:LoadXML(sceneXML:GetRoot()) -- This line causes the segfault.
end[/code]

Exact command and backtrace:
[code][1]    2680 segmentation fault  /usr/urho3d/bin/Urho3DPlayer MyScript.lua -w
#0  0x0000000000d877c4 in Urho3D::XMLFile::BeginLoad(Urho3D::Deserializer&) ()
#1  0x0000000000d94201 in Urho3D::Resource::Load(Urho3D::Deserializer&) ()
#2  0x0000000000d2a5f2 in Urho3D::Scene::LoadXML(Urho3D::Deserializer&) ()
#3  0x0000000000bf8955 in tolua_SceneLuaAPI_Scene_LoadXML01(lua_State*) ()
#4  0x0000000001184f07 in lj_BC_FUNCC ()
#5  0x0000000000a6d8bd in lua_pcall ()
#6  0x000000000104342f in Urho3D::LuaFunction::EndCall(int) ()
#7  0x000000000063117f in Urho3DPlayer::Start() ()[/code]

My version of Urho3D is on the master branch, commit hash 0906da48badacb227701e85b186581b580f9f778 (Fri Jan 15 21:02:56 2016 +0800). I built using the following options:
[code]$ git clone git://github.com/urho3d/urho3d && cd urho3d
$ mkdir build && cd build
$ cmake                                   \
    -DURHO3D_C++11=ON                     \
    -DURHO3D_DOCS=ON                      \
    -DURHO3D_LUA=ON                       \
    -DURHO3D_LUAJIT=ON                    \
    -DCMAKE_INSTALL_PREFIX=/usr/urho3d \
    ..
$ make -j7
$ make install[/code]

OS:
[code]$ uname -a
Linux rainbowdash 4.1.12-gentoo #1 SMP Tue Nov 10 00:33:50 CET 2015 x86_64 Intel(R) Core(TM) i5-2410M CPU @ 2.30GHz GenuineIntel GNU/Linux[/code]

-------------------------

TheComet | 2017-01-02 01:09:37 UTC | #2

[b][size=150]Update[/size][/b]

I re-built Urho3D and enabled all of the debug options and here's the error message:

[code][Mon Jan 25 02:04:56 2016] ERROR: Execute Lua function failed: [string "hound"]:20: error in function 'LoadXML'.
     argument #2 is 'XMLFile'; 'File' expected.[/code]

Code:
[code]    scene_ = Scene()
    local sceneFile = cache:GetResource("XMLFile", "Scenes/Ramps.xml")
    scene_:LoadXML(sceneFile)[/code]

I'm pretty sure this is wrong and I'm not sure what Lua is really expecting.

-------------------------

cadaver | 2017-01-02 01:09:37 UTC | #3

Due to technical reasons (scene wants to be able to get a file checksum for e.g. networking) there isn't an overload of Scene::LoadXML which takes a XMLFile. For Lua, it can take either a File* (which you get with ResourceCache::GetFile, be careful with memory management) or a string containing pathname.

Due to tolua++ being what it is, getting crashes with wrong parameters is easy. This is unfortunate, for now if you want a more robust scripting environment I'd recommend using AngelScript instead.

-------------------------

TheComet | 2017-01-02 01:09:39 UTC | #4

Thanks for the insight!

-------------------------

