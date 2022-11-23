arrowhart | 2017-01-02 01:11:25 UTC | #1

I have followed the instructions according to the documentation on how to build directly on the Raspberry Pi. It states that the build process is similar to the Linux instructions.
[url]http://urho3d.wikia.com/wiki/Build_Urho3D_on_Linux_(GCC)[/url]

Instead of using cmake_generic.sh, I used the cmake_rpi.sh to build. When I tried to [i]make[/i] in the dev folder, the process reached pretty far, but encountered the following error at 76%

[code]
[ 46% ] Built target tolua++
[ 76% ] Built target Urho3D
../../../lib/libUrho3D.a(loslib.c.o): In function 'os_tmpname' :
loslib.c:(.text ox208): warning: the use of 'tmpnam' is dangeUrous, better use 'mkstemp'
../../../lib/libUrho3D.a(loslib.c.o): In function 'Urho3D::Script::Script(Urho3D::Contextx)' :
Script.cpp:(.text 0x2624): undefined reference to 'Urho3D::RegisterInputAPI(asIScriptEnginex)'
Script.cpp:(.text 0x2623c): undefined reference to 'Urho3D::RegisterNextworkAPI(asIScriptEnginex)'
collect2: error: Id returned 1 exit status
Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/build.make:92: recipe for target 'bin/Urho3DPlayer' failed
make[2]: xxx [bin/Urho3DPlayer] Error 1
CMakeFiles/MakeFile2:1332: recipe for target 'Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/all' failed
make[1]: xxx [Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/all] Error 2
Makefile:137: recipe for target 'all' failed
make: xxx [all] Error 2[/code]

If I made a mistake when building on the Pi using cmake_rpi.sh, I am curious as to how I can fix my issue. Should I have just used cmake_generic.sh instead? If so, then what is the proper use of the cmake_rpi.sh?

-------------------------

weitjong | 2017-01-02 01:11:25 UTC | #2

First of all when you are doing a native build directly on the Pi device itself then there is no difference whether you are using cmake_generic.sh or cmake_rpi.sh. The latter script invokes the former internally. Since you are doing a native build then the convenience script knows that you don't need a cross-compiling toolchain file. Anyway, I think you are using Urho3D 1.5 instead of latest master branch (I let you know why I think so in a moment). Correct? And if so, there was a little bug in 1.5 in our buildsystem that it always include Urho3DPlayer in the build regardless of whether AngelScript or LuaScript subsystems are enabled. I suppose you have disabled both scripting subsystems in your build, correct? That bug has been fixed in the master branch recently. It excludes Urho3DPlayer target now when none of the scripting subsystem is enabled. For a quick fix in your case, you can just remove the "add_subdirectory (Urho3DPlayer)" in the Source/Tools/CMakeLists.txt file.

If you intend to build it natively then I won't advice you to use latest master branch right now. There are a couple of TODOs that we have planned but have no time to do it yet. One of them is to verify the build on RPI natively. We have now tightened our checks before letting CMake proceed to generate the build tree. I have a comment somewhere in the script that the check needs to be fine-tuned for RPI but I have no time to do it yet. So, that's the reason I know why you are not using the latest master as your build can go that far. Of course, I am happy if I am wrong here, i.e. my worry is unfounded.

-------------------------

arrowhart | 2017-01-02 01:11:25 UTC | #3

[quote="weitjong"]First of all when you are doing a native build directly on the Pi device itself then there is no difference whether you are using cmake_generic.sh or cmake_rpi.sh. The latter script invokes the former internally. Since you are doing a native build then the convenience script knows that you don't need a cross-compiling toolchain file. Anyway, I think you are using Urho3D 1.5 instead of latest master branch (I let you know why I think so in a moment). Correct? And if so, there was a little bug in 1.5 in our buildsystem that it always include Urho3DPlayer in the build regardless of whether AngelScript or LuaScript subsystems are enabled. I suppose you have disabled both scripting subsystems in your build, correct? That bug has been fixed in the master branch recently. It excludes Urho3DPlayer target now when none of the scripting subsystem is enabled. For a quick fix in your case, you can just remove the "add_subdirectory (Urho3DPlayer)" in the Source/Tools/CMakeLists.txt file.

If you intend to build it natively then I won't advice you to use latest master branch right now. There are a couple of TODOs that we have planned but have no time to do it yet. One of them is to verify the build on RPI natively. We have now tightened our checks before letting CMake proceed to generate the build tree. I have a comment somewhere in the script that the check needs to be fine-tuned for RPI but I have no time to do it yet. So, that's the reason I know why you are not using the latest master as your build can go that far. Of course, I am happy if I am wrong here, i.e. my worry is unfounded.[/quote]

Okay, I think I understand. To answer your suspicions, yes I am using build 1.5 for this. When you stated that making the change to the CMakeLists.txt will fix my error, do you mean it should successfully reach 100% during the make? My current goal is to try and get some of the game samples working on my Pi by natively building. What you described will allow me to reach that goal?

Also, I am a little confused by what you meant by the latest build is not set up properly for natively building on the RPI. If that is the case, is there a previous build that has had success when building natively? I have seen a few posts in the past regarding those who have successfully got theirs to work with the sample games. If I am mistaken about them natively building, then I imagine this is because they have cross-compiled?

-------------------------

weitjong | 2017-01-02 01:11:25 UTC | #4

Your last build error only caused by the failure in building Urho3DPlayer target due to its dependency on scripting subystem. So, removing that obstacle should let your build to progress to the end. And if you have enabled sample targets (which is enabled by default) then you should get all the C++ samples built.

As for the latest master branch, it should be working as well. But we have only tested and verified it in cross-compiling setup. I just want to highlight that the newly added checks may back fire on native RPI build. If you are technical savvy then of course that alone won't stop you. The check could be bypassed or fine tuned. Or I take back what I just said earlier, go there, use the latest master branch and help us to verify it or report any problems that you find.

-------------------------

