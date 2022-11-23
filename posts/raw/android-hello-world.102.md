zaynyatyi | 2017-01-02 00:58:00 UTC | #1

Hi
First of all thank you for great engine.
Is there any hello world example (Something like in samples) for android target.
Just a simple app using libUrho3d.a, without player.

Regards

-------------------------

weitjong | 2017-01-02 00:58:00 UTC | #2

Welcome to our forum.

Due to the limitation of Android development environment, at the moment we could not add all the sample targets into a single Android project. However, that does not mean the sample targets (we have over 20 of them) do not work for Android build. I reckon all you have to do is:
- Remove the line that says "add_subdirectory (Urho3DPlayer)"
- And then replace it with one of the sample targets, say, "add_subdirectory (01_HelloWorld)".

HTH.

-------------------------

zaynyatyi | 2017-01-02 00:58:00 UTC | #3

Thank you.
I commented 
[code]#if (NOT ANDROID AND ENABLE_SAMPLES)
    add_subdirectory (Samples)
#endif ()[/code]
in Source/CMakeList.txt
and
[code]# Add samples
add_subdirectory (01_HelloWorld)
#add_subdirectory (02_HelloGUI)
#add_subdirectory (03_Sprites)
#add_subdirectory (04_StaticScene)
#add_subdirectory (05_AnimatingScene)
#add_subdirectory (06_SkeletalAnimation)
#add_subdirectory (07_Billboards)
#add_subdirectory (08_Decals)
#add_subdirectory (09_MultipleViewports)
#add_subdirectory (10_RenderToTexture)
#add_subdirectory (11_Physics)
#add_subdirectory (12_PhysicsStressTest)
#add_subdirectory (13_Ragdolls)
#add_subdirectory (14_SoundEffects)
#add_subdirectory (15_Navigation)
#add_subdirectory (16_Chat)
#add_subdirectory (17_SceneReplication)
#add_subdirectory (18_CharacterDemo)
#add_subdirectory (19_VehicleDemo)
#add_subdirectory (20_HugeObjectCount)
#if (ENABLE_ANGELSCRIPT)
#    add_subdirectory (21_AngelScriptIntegration)
#endif ()
#if (ENABLE_LUA)
#    add_subdirectory (22_LuaIntegration)
#endif ()
#add_subdirectory (23_Water)[/code]
in Source/Samples/CMakeList.txt

-------------------------

weitjong | 2017-01-02 00:58:00 UTC | #4

Yup. That's what I meant. Keep in mind that you can only have one target that is setup as main executable (done by setup_main_executable macro) for Android build.

-------------------------

zaynyatyi | 2017-01-02 00:58:00 UTC | #5

I need that just to give it a try.
Will make app from scratch with simple CMake file.

-------------------------

weitjong | 2017-01-02 00:58:00 UTC | #6

You didn't say what is your development platform. If you are using Linux like myself then there is one quick way to set everything up with minimal CMakeList.txt that using Urho3D library as external library. In case you are using Linux or Mac OSX then:
- First, install "Ruby" and "rake" rubygem. Probably Ruby already comes pre-install on most modern distro. For Mac OSX, get them via homebrew.
- Second, run this rake command in a command line terminal after cd to Urho3D project root directory: rake scaffolding dir=/path/to/your/new/project
- Last, follow the instructions in the terminal output

Last time I check, these steps still work for Android build on Linux host/build system. Note: this only works after you have built Urho3D library for the respective platform you targeted in your local filesystem. I do not dare to document this officially in Urho3D website because it is not yet applicable for Windows platform.

-------------------------

