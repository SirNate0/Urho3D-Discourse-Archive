weitjong | 2017-01-02 01:02:22 UTC | #1

We have a new build system in the master branch now. Below summarizes the changes that may impact you:
[ul][li] Shell scripts and batch jobs require external user input to determine the build tree location, similar to cmake-gui. All the scripts or batches now expect a "build-tree path" as the first parameter. e.g. cmake_generic.sh ~/MyBuildTree -D URHO3D_64BIT=1.[/li]
[li] The CMake modules now expect to find the main CMakeLists.txt in the project root directory, instead of in the "Source" directory. So, does the "CMake" subdir which contains the "Modules" and "Toolchains" subdirs.[/li]
[li] Cross-compiling build with Lua or LuaJIT enabled is now made simpler. The Urho3D cross-compiling build tree can be configured, generated, and built in one go, instead of jumping back and forth between cross-compiling build tree and native build tree to build the host tool first. Android build with LuaJIT enabled on a Windows host is also now possible with Android NDK toolchain (for the cross-compiling target) and MinGW toolchain (for the host tool target).[/li]
[li] Enforcing SDK include path. For example: #include <Urho3D/Urho3D.h>, instead of #include "Urho3D.h" like in the past. The actual path to the header files need to be specified. For example: #include <Urho3D/Scene/Scene.h>. See sample apps on how the new include path should look like now.[/li][/ul]
There are other smaller changes that may not impact you directly, among others:
[ul][li] Rename cmake_gcc.sh to cmake_generic.sh. Add cmake_generic.bat which is now the base file for all the batch files. The "generic" here means it lets CMake itself to detect and choose which generator to use.[/li]
[li] On Windows host, URHO3D_MKLINK variable is automatically initialized based on Windows user account capability to use MKLINK command.[/li]
[li] Move the "Android" subdirectory from "Source" directory to project root.[/li]
[li] On Android platform, the SDK installs the library with ANDROID_ABI appended similar to the Android library output path, e.g. ${CMAKE_INSTALL_PREFIX}/libs/x86_64 or ${CMAKE_INSTALL_PREFIX}/libs/armeabi-v7a.[/li]
[li] When cross-compiling on Raspberry Pi platform, rename RPI_TOOL variable to RPI_PREFIX and it now expects the "prefix" to the cross-compiling tools similar to how the MINGW_PREFIX is defined.[/li]
[li] All the cross-compiling build trees now have their CMAKE_INSTALL_PREFIX reset to "/usr/local". That is, it is not "rooted" as in the old build system.[/li][/ul]
Please check the updated documentation for more detail.
[ul][li] For creating a new project using the library: [urho3d.github.io/documentation/H ... brary.html](http://urho3d.github.io/documentation/HEAD/_using_library.html)[/li]
[li] For installing the library as SDK: [urho3d.github.io/documentation/H ... ng_Library](http://urho3d.github.io/documentation/HEAD/_building.html#Building_Library)[/li][/ul]

-------------------------

friesencr | 2017-01-02 01:02:22 UTC | #2

Thanks for your hard work weitjong.  I am not a pro cpp user but have always had reliable working builds since day one of Urho, and feel well taken care of.  I tested the builds on my machines and they worked like a charm on both windows and linux.  I also feel like major changes to the build system should merit a new release.  Keeping stable in line with the current build system is good for new users.  This is just my opinion though.  Thanks again.

-------------------------

Faizol | 2017-01-02 01:02:22 UTC | #3

I don't have any problem with the Linux building but I can't get my Android code to be compiled. What's the ideal cpp folder tree structure for Android development from the new build system? The previous Rake scallfolding sets up a fairly straighfoward makefile to include your own cpp files. Do we have to write our own CMakeList.txt to include the source code?

Thanks.

-------------------------

weitjong | 2017-01-02 01:02:22 UTC | #4

[quote="friesencr"]Thanks for your hard work weitjong.  I am not a pro cpp user but have always had reliable working builds since day one of Urho, and feel well taken care of.  I tested the builds on my machines and they worked like a charm on both windows and linux.  I also feel like major changes to the build system should merit a new release.  Keeping stable in line with the current build system is good for new users.  This is just my opinion though.  Thanks again.[/quote]
I should actually thank Lasse for trusting me to work on the Urho3D build system since the beginning. Practice makes perfect. The truth is, I was a CMake newbie too back then (I think he didn't know that! :wink: )  We all learn something from this wonderful project in our own interest areas.

Re. making a new release. I have thought about that too. When I first created this issue soon after the Urho3D v1.32 release, I thought the changes could be merged into the master branch fairly quick and a new release won't be necessary. Little had I known that it would take about one month elapse time to complete the work, partly due to increase in the changes scope. So, it is valid point to raise. I can understand some of you would want to start a new project with the new build system on a more stable branch. @cadaver, this is your call.

I would also take this opportunity to make a point of my own. We only have a handful of platforms now and yet it has taken me a lot of effort to make sure the build works well on all of them. Having the Travis CI to perform the automatic build tests help, but I couldn't imagine how it would be like when/if in future Urho supports more platforms than we are today. I think this should not be a one man show. In short, we need some new blood in this area. Now, this is a call for you.

-------------------------

weitjong | 2017-01-02 01:02:22 UTC | #5

[quote="Faizol"]I don't have any problem with the Linux building but I can't get my Android code to be compiled. What's the ideal cpp folder tree structure for Android development from the new build system? The previous Rake scallfolding sets up a fairly straighfoward makefile to include your own cpp files. Do we have to write our own CMakeList.txt to include the source code?

Thanks.[/quote]
You should know that for Android build, you should structure your project according to Google specification. See [topic378.html](http://discourse.urho3d.io/t/solved-using-scripting-with-android/386/1).

-------------------------

Faizol | 2017-01-02 01:02:22 UTC | #6

[quote="weitjong"][quote="Faizol"]I don't have any problem with the Linux building but I can't get my Android code to be compiled. What's the ideal cpp folder tree structure for Android development from the new build system? The previous Rake scallfolding sets up a fairly straighfoward makefile to include your own cpp files. Do we have to write our own CMakeList.txt to include the source code?

Thanks.[/quote]
You should know that for Android build, you should structure your project according to Google specification. See [topic378.html](http://discourse.urho3d.io/t/solved-using-scripting-with-android/386/1).[/quote]

Thanks, that was the link that I followed before and managed to get my code compiled. According to Zakk as he quoted your reply, 
"Quoting Weitjong:

Notice that "rake scaffolding" simply copies the Urho3DPlayer.cpp and
Urho3DPlayer.h there as placeholders. Normally, you should replace these two
files with your own project source files. But for you case, you can leave them
because that is exactly what you want."

Is this still the same, that Urho3DPlayer.cpp and Urho3DPlayer.h are there as placeholders? I followed the prevous methods from the thread you linked and deleted these two files in several tests (including the Tool directory in some of them) and replaced the files with my sources and headers but Urho3DPlayer.cpp and Urho3DPlayer.h are again copied and compiled instead of my sources when I run makefile.

Any pointers?

Thanks.

-------------------------

weitjong | 2017-01-02 01:02:23 UTC | #7

Not exactly sure at which step you have done wrong, so it is a little difficult for me to advice you on the corrective action.

The rake scaffolding task still does not support creating a new project suitable for Android build. Perhaps I will fix that one day but for now, you have to complement the missing bits yourself as has been outlined by Zakk in his post. The scaffolding task, as of this writing, still tries to copy the Urho3DPlayer.cpp and Urho3DPlayer.h as the placeholder of source files in the newly created project. For Zakk's case, it is a little different because he wanted to use scripting language in his Android app. The placeholder source files are exactly what it needs for Zakk's case. In a more general case, however, once the new project is created then one should delete these two source files and replace them with their own source files. Note that, I am talking about the newly created project here. You should leave the "Tools" sub-project in the Urho3D project as it is in any case.

If this is the first time you build for Android platform, perhaps it would be beneficial that you first try to learn from the basic examples provided by Google. This should help you understand what else are missing in the new project created by the current rake scaffolding task.

-------------------------

Bluemoon | 2017-01-02 01:02:23 UTC | #8

Words cannot express how impressed I am with Urho3D as a project :smiley: , watching Urho3D develop and grow is really something awesome.

For this new build system I seem to be having a problem with my build procedure... It terminated with the below (error) log
[code]
[ 50%] Generating GIT revision number (tag + last commit SHA-1)
Scanning dependencies of target Urho3D
[ 50%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Audio/Audio.cpp.o
bj
In file included from C:/Urho_Master/Source/Urho3D/Container/HashMap.h:25:0,
                 from C:/Urho_Master/Source/Urho3D/Precompiled.h:25,
                 from C:\Urho_Master\Source\Urho3D\Audio\Audio.cpp:23:
C:/Urho_Master/Source/Urho3D/Container/../Container/HashBase.h:25:23: fatal erro
r: ../Urho3D.h: No such file or directory
 #include "../Urho3D.h"
                       ^
compilation terminated.
Source\Urho3D\CMakeFiles\Urho3D.dir\build.make:74: recipe for target 'Source/Urh
o3D/CMakeFiles/Urho3D.dir/Audio/Audio.cpp.obj' failed
mingw32-make[2]: *** [Source/Urho3D/CMakeFiles/Urho3D.dir/Audio/Audio.cpp.obj] E
rror 1
CMakeFiles\Makefile2:957: recipe for target 'Source/Urho3D/CMakeFiles/Urho3D.dir
/all' failed
mingw32-make[1]: *** [Source/Urho3D/CMakeFiles/Urho3D.dir/all] Error 2
Makefile:132: recipe for target 'all' failed
mingw32-make: *** [all] Error 2
[/code]


I traced and found out that the missing file, which is "Urho3D.h", was actually in "${BUILD_FOLDER}\Source\Urho3D\" but it seems the build procedure doesn't see it, could I have made mistake in my build setup. I used cmake to configure my build and I'm building with minGw-w64 on Windows Vista 32bit

-------------------------

weitjong | 2017-01-02 01:02:23 UTC | #9

Interesting that you have this issue also using MinGW compiler on Windows host. I thought only MSVC compiler on Windows host get it. Try changing this line [github.com/urho3d/Urho3D/blob/m ... s.txt#L132](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/CMakeLists.txt#L132) to read: "if (CMAKE_HOST_WIN32)" and see whether it helps.

-------------------------

Faizol | 2017-01-02 01:02:24 UTC | #10

I can make own cmake rules to link my source to the newly compiled library so it shouldn't be a big problem. However a standardized cmake rules will make a huge difference in helping new users setting up their projects.

May I make a suggestion? I'm basing this on the way the previous rake scallfolding handles the files and also looking at how other framework such as cococs2d-x organized their folders and cmake rules.

The previous rake scallfolding generates a skeleton directory with Urho3DPlayer.cpp and Urho3DPlayer.h as placeholders and then we can generate makefiles after that in which any file in that directory will be scanned. 

The cmake_generic.sh right now directly prepares the directory from Urho3D SDK folder. Instead of two steps process previously now the build is done faster simply in just one step. 

My suggestion, is it posssible to include one placeholder folder directly like "Application" for example into your cmake rules which will be setup together with the generated makefiles to just scan source code in it?

Thanks.

-------------------------

cnccsk | 2017-01-02 01:02:24 UTC | #11

for android:

-- Found Urho3D: as CMake target
CMake Error at CMake/Modules/Urho3D-CMake-common.cmake:696 (message):
  Could not find SDL_android_main.c source file in the Urho3D build tree or
  SDK installation.  Please reconfigure and rebuild your Urho3D build tree;
  or reinstall the SDK.
Call Stack (most recent call first):
  Source/Tools/Urho3DPlayer/CMakeLists.txt:30 (setup_main_executable)

-- Configuring incomplete, errors occurred!
See also "F:/dev/Urho3D_master/Android/CMakeFiles/CMakeOutput.log".

-------------------------

weitjong | 2017-01-02 01:02:24 UTC | #12

[quote="Bluemoon"]I traced and found out that the missing file, which is "Urho3D.h", was actually in "${BUILD_FOLDER}\Source\Urho3D\" but it seems the build procedure doesn't see it, could I have made mistake in my build setup. I used cmake to configure my build and I'm building with minGw-w64 on Windows Vista 32bit[/quote]
As explained before that I also encountered this build error for MSVC on Windows host. Today I have time to try the MinGW build on Windows host myself and I can confirm that the problem is reproducible. I am testing a fix that works for both MSVC and MinGW on Window host/build system. Expect to get a patch soon in the master branch.

-------------------------

Bluemoon | 2017-01-02 01:02:25 UTC | #13

[quote="weitjong"]Interesting that you have this issue also using MinGW compiler on Windows host. I thought only MSVC compiler on Windows host get it. Try changing this line [github.com/urho3d/Urho3D/blob/m ... s.txt#L132](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/CMakeLists.txt#L132) to read: "if (CMAKE_HOST_WIN32)" and see whether it helps.[/quote]

Unfortunately I still get the same error :frowning: . I even tried building with mingw build script and it is still giving me that same error

-------------------------

weitjong | 2017-01-02 01:02:25 UTC | #14

[quote="Bluemoon"][quote="weitjong"]Interesting that you have this issue also using MinGW compiler on Windows host. I thought only MSVC compiler on Windows host get it. Try changing this line [github.com/urho3d/Urho3D/blob/m ... s.txt#L132](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/CMakeLists.txt#L132) to read: "if (CMAKE_HOST_WIN32)" and see whether it helps.[/quote]

Unfortunately I still get the same error :frowning: . I even tried building with mingw build script and it is still giving me that same error[/quote]
I believe your problem should be fixed now in the master branch. It was not due to the same root cause as MSVC. I found what could be a CMake bug in which file(TO_NATIVE_PATH) converts to forward slash in MinGW build on Windows host, instead of backward slash. The wrong slash direction has caused all the symlinks failed to be created. BTW, I am assuming you are using MKLINK here.

Having said that, I think your reported problem with MinGW on Windows host is a blessing in disguise, as it also reveals an error in my earlier header search path setup for GCC in general. I have applied a hack/patch to fix it. Unfortunately, the MSVC "workaround" is still needed even after this, which is really annoying.

-------------------------

weitjong | 2017-01-02 01:02:25 UTC | #15

[quote="Faizol"]My suggestion, is it posssible to include one placeholder folder directly like "Application" for example into your cmake rules which will be setup together with the generated makefiles to just scan source code in it?
Thanks.[/quote]
Thanks for your suggestion. The scaffolding task is not designed to be a one task to rule them all. To me, its purpose is just to get the project started with a sane structure (sane means as expected by our CMake modules). The user should then replace the placeholders and add more structures that suit their own project need. I want to avoid the same mistake that we had made in the past in our build scripts that they assumed too much on user behalf.

-------------------------

weitjong | 2017-01-02 01:02:25 UTC | #16

[quote="cnccsk"]for android:

-- Found Urho3D: as CMake target
CMake Error at CMake/Modules/Urho3D-CMake-common.cmake:696 (message):
  Could not find SDL_android_main.c source file in the Urho3D build tree or
  SDK installation.  Please reconfigure and rebuild your Urho3D build tree;
  or reinstall the SDK.
Call Stack (most recent call first):
  Source/Tools/Urho3DPlayer/CMakeLists.txt:30 (setup_main_executable)

-- Configuring incomplete, errors occurred!
See also "F:/dev/Urho3D_master/Android/CMakeFiles/CMakeOutput.log".[/quote]
I am not able to reproduce your problem with a new clean Android build tree on Linux host. Make sure you have run cmake_clean.bat or cmake_clean.sh if you are reusing an old build tree. If this is not cause of your problem then can you tell us which host system are you using?

EDIT: Sorry. I did not see the "F:/" earlier. So, it was an Android build tree on Windows host then. However, I am also not able to reproduce the problem on my Win7 VM with MKLINK privilege on my Windows user account. I get this in the CMakeCache.txt in my Android build tree.

//Path to SDL_android_main.c
ANDROID_MAIN_C_PATH:FILEPATH=C:/Users/weitjong/SDKs/urho3d/android-Build/include/Urho3D/ThirdParty/SDL/android/SDL_android_main.c

Do you get something similar? If not, can you check in your build tree whether you have this SDL_android_main.c file in this path "include/Urho3D/ThirdParty/SDL/android". Without the MKLINK, the new buildsystem should also perform a hard file copy of the files to their respective locations. But that logic is the least being tested at the moment. So, I will not surprise if something is wrong there.

-------------------------

Bluemoon | 2017-01-02 01:02:25 UTC | #17

[quote="weitjong"]

I believe your problem should be fixed now in the master branch. It was not due to the same root cause as MSVC. I found what could be a CMake bug in which file(TO_NATIVE_PATH) converts to forward slash in MinGW build on Windows host, instead of backward slash. The wrong slash direction has caused all the symlinks failed to be created. BTW, I am assuming you are using MKLINK here.

Having said that, I think your reported problem with MinGW on Windows host is a blessing in disguise, as it also reveals an error in my earlier header search path setup for GCC in general. I have applied a hack/patch to fix it. Unfortunately, the MSVC "workaround" is still needed even after this, which is really annoying.[/quote]

Would I still need to do the below quoted line:

[quote="weitjong"]Try changing this line [github.com/urho3d/Urho3D/blob/m ... s.txt#L132](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/CMakeLists.txt#L132) to read: "if (CMAKE_HOST_WIN32)" [/quote]

-------------------------

weitjong | 2017-01-02 01:02:25 UTC | #18

[quote="Bluemoon"][quote="weitjong"]

I believe your problem should be fixed now in the master branch. It was not due to the same root cause as MSVC. I found what could be a CMake bug in which file(TO_NATIVE_PATH) converts to forward slash in MinGW build on Windows host, instead of backward slash. The wrong slash direction has caused all the symlinks failed to be created. BTW, I am assuming you are using MKLINK here.

Having said that, I think your reported problem with MinGW on Windows host is a blessing in disguise, as it also reveals an error in my earlier header search path setup for GCC in general. I have applied a hack/patch to fix it. Unfortunately, the MSVC "workaround" is still needed even after this, which is really annoying.[/quote]

Would I still need to do the below quoted line:

[quote="weitjong"]Try changing this line [github.com/urho3d/Urho3D/blob/m ... s.txt#L132](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/CMakeLists.txt#L132) to read: "if (CMAKE_HOST_WIN32)" [/quote][/quote]
No. Just pull and you should be all good. Finger cross.

-------------------------

practicing01 | 2017-01-02 01:02:25 UTC | #19

I'd like to chime in here to say that I'm not digging the new build system, infact I reverted the merge.  With the old system all I had to do was cmake_eclipse.sh and rake (plus a few additional trivial steps for android).  With this system I was able to compile but couldn't rake.  I hope it gets easier in the near future as I'm going to need to merge bug fixes.

-------------------------

weitjong | 2017-01-02 01:02:25 UTC | #20

[quote="practicing01"]I'd like to chime in here to say that I'm not digging the new build system, infact I reverted the merge.  With the old system all I had to do was cmake_eclipse.sh and rake (plus a few additional trivial steps for android).  With this system I was able to compile but couldn't rake.  I hope it gets easier in the near future as I'm going to need to merge bug fixes.[/quote]
What do you mean exactly by "able to compile but couldn't rake"?

-------------------------

weitjong | 2017-01-02 01:02:25 UTC | #21

[quote="weitjong"]Having said that, I think your reported problem with MinGW on Windows host is a blessing in disguise, as it also reveals an error in my earlier header search path setup for GCC in general. I have applied a hack/patch to fix it. Unfortunately, the MSVC "workaround" is still needed even after this, which is really annoying.[/quote]
Good news. I think I have found the culprit which caused MSVC requiring the "workaround" search path to be added. More commits coming soon.

-------------------------

weitjong | 2017-01-02 01:02:25 UTC | #22

[quote="weitjong"][quote="cnccsk"]for android:

-- Found Urho3D: as CMake target
CMake Error at CMake/Modules/Urho3D-CMake-common.cmake:696 (message):
  Could not find SDL_android_main.c source file in the Urho3D build tree or
  SDK installation.  Please reconfigure and rebuild your Urho3D build tree;
  or reinstall the SDK.
Call Stack (most recent call first):
  Source/Tools/Urho3DPlayer/CMakeLists.txt:30 (setup_main_executable)

-- Configuring incomplete, errors occurred!
See also "F:/dev/Urho3D_master/Android/CMakeFiles/CMakeOutput.log".[/quote]
I am not able to reproduce your problem with a new clean Android build tree on Linux host. Make sure you have run cmake_clean.bat or cmake_clean.sh if you are reusing an old build tree. If this is not cause of your problem then can you tell us which host system are you using?

EDIT: Sorry. I did not see the "F:/" earlier. So, it was an Android build tree on Windows host then. However, I am also not able to reproduce the problem on my Win7 VM with MKLINK privilege on my Windows user account. I get this in the CMakeCache.txt in my Android build tree.

//Path to SDL_android_main.c
ANDROID_MAIN_C_PATH:FILEPATH=C:/Users/weitjong/SDKs/urho3d/android-Build/include/Urho3D/ThirdParty/SDL/android/SDL_android_main.c

Do you get something similar? If not, can you check in your build tree whether you have this SDL_android_main.c file in this path "include/Urho3D/ThirdParty/SDL/android". Without the MKLINK, the new buildsystem should also perform a hard file copy of the files to their respective locations. But that logic is the least being tested at the moment. So, I will not surprise if something is wrong there.[/quote]
I think I have fixed this Android build problem on Windows host without MKLINK. For those on Windows host without MKLINK, please try to pull and recreate your build tree again. Thanks for reporting any errors back.

-------------------------

friesencr | 2017-01-02 01:02:27 UTC | #23

I can't tell if this is by design or not.  I am using cmake_generic and set the build tree to 'Build'.  I go in and run make and it completes.  It makes a Bin folder inside the Build folder for the artifacts.  Whereas my visual studio builds push binaries to the Bin folder like it used to.  I am setting a CMAKE_INSTALL_PREFIX to the bin folder and running make install after a build to copy of the binaries to the old bin folder as an easy solution to move the binaries.

-------------------------

weitjong | 2017-01-02 01:02:27 UTC | #24

[quote="friesencr"]I can't tell if this is by design or not.  I am using cmake_generic and set the build tree to 'Build'.  I go in and run make and it completes.  It makes a Bin folder inside the Build folder for the artifacts.  Whereas my visual studio builds push binaries to the Bin folder like it used to.  I am setting a CMAKE_INSTALL_PREFIX to the bin folder and running make install after a build to copy of the binaries to the old bin folder as an easy solution to move the binaries.[/quote]
For the Visual Studio build: no it should not happen as you described. Bin output folder should be always created relative to the build tree location regardless of which compiler toolchain or generator being used.
For moving the binaries, you may want to consider to use the URHO3D_PREFIX_PATH environment variable as described here in the updated documentation. [urho3d.github.io/documentation/H ... ing_Native](http://urho3d.github.io/documentation/HEAD/_building.html#Building_Native). Instead of bringing your binaries to the assets. This environment variable brings the assets to the binaries wherever they are in their own build trees.

-------------------------

cnccsk | 2017-01-02 01:02:27 UTC | #25

[quote="weitjong"]
I think I have fixed this Android build problem on Windows host without MKLINK. For those on Windows host without MKLINK, please try to pull and recreate your build tree again. Thanks for reporting any errors back.[/quote]

 :smiley: 
Yes, It's fixed, and I make it, another problem::

F:\dev\Urho3D_master\Android>make -j4
[  5%] "Built target FreeType"
[  6%] "Built target JO"
[  6%] "Built target LZ4"
[  6%] "Built target PugiXml"
[  6%] "Built target rapidjson"
[ 19%] "Built target SDL"
[ 19%] "Built target StanHull"
[ 19%] "Built target STB"
[ 24%] "Built target AngelScript"
[ 28%] "Built target Lua"
[ 29%] "Built target lua_interpreter"
[ 29%] "Built target luac"
[ 30%] "Built target toluapp"
[ 30%] "Built target Civetweb"
[ 33%] "Built target kNet"
[ 34%] "Built target Detour"
[ 36%] "Built target Recast"
[ 56%] "Built target Bullet"
[ 62%] "Built target Box2D"
[ 62%] Performing configure step for 'tolua++'
-- The C compiler identification is unknown
-- The CXX compiler identification is unknown
CMake Error at CMakeLists.txt:25 (project):
  No CMAKE_C_COMPILER could be found.

  Tell CMake where to find the compiler by setting either the environment
  variable "CC" or the CMake cache entry CMAKE_C_COMPILER to the full path to
  the compiler, or to the compiler name if it is in the PATH.


CMake Error at CMakeLists.txt:25 (project):
  No CMAKE_CXX_COMPILER could be found.

  Tell CMake where to find the compiler by setting either the environment
  variable "CXX" or the CMake cache entry CMAKE_CXX_COMPILER to the full path
  to the compiler, or to the compiler name if it is in the PATH.


-- Configuring incomplete, errors occurred!
See also "F:/dev/Urho3D_master/Android/Source/Urho3D/tolua++-prefix/src/tolua++-build/CMakeFiles/CMakeOutput.log".
See also "F:/dev/Urho3D_master/Android/Source/Urho3D/tolua++-prefix/src/tolua++-build/CMakeFiles/CMakeError.log".
make[2]: *** [Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-configure] Error 1
make[1]: *** [Source/Urho3D/CMakeFiles/tolua++.dir/all] Error 2
make: *** [all] Error 2

-------------------------

weitjong | 2017-01-02 01:02:27 UTC | #26

[quote="cnccsk"][quote="weitjong"]
I think I have fixed this Android build problem on Windows host without MKLINK. For those on Windows host without MKLINK, please try to pull and recreate your build tree again. Thanks for reporting any errors back.[/quote]

 :smiley: 
Yes, It's fixed, and I make it, another problem::

F:\dev\Urho3D_master\Android>make -j4
[  5%] "Built target FreeType"
[  6%] "Built target JO"
[  6%] "Built target LZ4"
[  6%] "Built target PugiXml"
[  6%] "Built target rapidjson"
[ 19%] "Built target SDL"
[ 19%] "Built target StanHull"
[ 19%] "Built target STB"
[ 24%] "Built target AngelScript"
[ 28%] "Built target Lua"
[ 29%] "Built target lua_interpreter"
[ 29%] "Built target luac"
[ 30%] "Built target toluapp"
[ 30%] "Built target Civetweb"
[ 33%] "Built target kNet"
[ 34%] "Built target Detour"
[ 36%] "Built target Recast"
[ 56%] "Built target Bullet"
[ 62%] "Built target Box2D"
[ 62%] Performing configure step for 'tolua++'
-- The C compiler identification is unknown
-- The CXX compiler identification is unknown
CMake Error at CMakeLists.txt:25 (project):
  No CMAKE_C_COMPILER could be found.

  Tell CMake where to find the compiler by setting either the environment
  variable "CC" or the CMake cache entry CMAKE_C_COMPILER to the full path to
  the compiler, or to the compiler name if it is in the PATH.


CMake Error at CMakeLists.txt:25 (project):
  No CMAKE_CXX_COMPILER could be found.

  Tell CMake where to find the compiler by setting either the environment
  variable "CXX" or the CMake cache entry CMAKE_CXX_COMPILER to the full path
  to the compiler, or to the compiler name if it is in the PATH.


-- Configuring incomplete, errors occurred!
See also "F:/dev/Urho3D_master/Android/Source/Urho3D/tolua++-prefix/src/tolua++-build/CMakeFiles/CMakeOutput.log".
See also "F:/dev/Urho3D_master/Android/Source/Urho3D/tolua++-prefix/src/tolua++-build/CMakeFiles/CMakeError.log".
make[2]: *** [Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-configure] Error 1
make[1]: *** [Source/Urho3D/CMakeFiles/tolua++.dir/all] Error 2
make: *** [all] Error 2[/quote]
When cross-compiling (such as Android build) on Windows host that requires host tool building (such as Lua/LuaJIT), the host tool target will be built by using host native compiler toolchain. The error you received indicates that CMake cannot find one. Make sure you have also installed MinGW toolchain in your host system and the MinGW toolchain path has been added into the PATH environment variable in your host before attempting this. I have updated my first post in this topic to reflect this.

-------------------------

friesencr | 2017-01-02 01:02:27 UTC | #27

I cannot tell if by design but URHO3D_PREFIX_PATH  is missing from the large table of variables.  That was the table I was looking to for solutions.

-------------------------

cnccsk | 2017-01-02 01:02:27 UTC | #28

[quote="weitjong"]
When cross-compiling (such as Android build) on Windows host that requires host tool building (such as Lua/LuaJIT), the host tool target will be built by using host native compiler toolchain. The error you received indicates that CMake cannot find one. Make sure you have also installed MinGW toolchain in your host system and the MinGW toolchain path has been added into the PATH environment variable in your host before attempting this. I have updated my first post in this topic to reflect this.[/quote]

Hmm, I added MinGW to PATH, it works,

Thanks.

-------------------------

weitjong | 2017-01-02 01:02:27 UTC | #29

[quote="friesencr"]I cannot tell if by design but URHO3D_PREFIX_PATH  is missing from the large table of variables.  That was the table I was looking to for solutions.[/quote]
That's because URHO3D_PREFIX_PATH is an "environment variable". It is not one of the CMake variables or build options, so it it is not listed in the build option table. This environment variable is dealing with Urho3D runtime, while the build options are for  building Urho3D with CMake. As such, it is actually listed here. [urho3d.github.io/documentation/H ... ommandline](http://urho3d.github.io/documentation/HEAD/_running.html#Running_Commandline)

You can also tell CMake to use the Urho3D project root as your *native* build tree and then forget about all this "moving" assets or binaries business all together. However, be warned that this will clutter your source tree with build tree stuff and sort of beat the purpose of us keep refining the build system.

-------------------------

weitjong | 2017-01-02 01:02:27 UTC | #30

[quote="cnccsk"][quote="weitjong"]
When cross-compiling (such as Android build) on Windows host that requires host tool building (such as Lua/LuaJIT), the host tool target will be built by using host native compiler toolchain. The error you received indicates that CMake cannot find one. Make sure you have also installed MinGW toolchain in your host system and the MinGW toolchain path has been added into the PATH environment variable in your host before attempting this. I have updated my first post in this topic to reflect this.[/quote]

Hmm, I added MinGW to PATH, it works,

Thanks.[/quote]
Glad to hear that.

-------------------------

Faizol | 2017-01-02 01:02:27 UTC | #31

the new changes break cmake_generic.sh on Linux;

[code]$ ./cmake_generic.sh ../myGame
CMake Error at CMake/Modules/Urho3D-CMake-common.cmake:279 (create_symlink):
  Unknown CMake command "create_symlink".
Call Stack (most recent call first):
  CMakeLists.txt:47 (include)


-- Configuring incomplete, errors occurred!
See also "/data/urho3d/myGame/CMakeFiles/CMakeOutput.log".
[/code]

Also, if there are major changes made to the Urho3D-CMake-common.cmake file, can the skeleton CMakeLists.txt on [urho3d.github.io/documentation/1 ... brary.html](http://urho3d.github.io/documentation/1.32/_using_library.html) be updated if needed so that the skeleton CMakelIsts.txt can still be used?

Thanks.

-------------------------

weitjong | 2017-01-02 01:02:28 UTC | #32

The new macro create_symlink() is in our Urho3D CMake common module. Please kindly make sure you have got rid of all the old files (CMakeLists.txt and *.cmake) from the old build system. Your error message indicates somehow you still have an old file in the mix. Also Please refer to the updated documentation here [urho3d.github.io/documentation/H ... brary.html](http://urho3d.github.io/documentation/HEAD/_using_library.html). Note the 'HEAD' in the path instead of '1.32'!

-------------------------

Faizol | 2017-01-02 01:02:29 UTC | #33

[quote="weitjong"]The new macro create_symlink() is in our Urho3D CMake common module. Please kindly make sure you have got rid of all the old files (CMakeLists.txt and *.cmake) from the old build system. Your error message indicates somehow you still have an old file in the mix. Also Please refer to the updated documentation here [urho3d.github.io/documentation/H ... brary.html](http://urho3d.github.io/documentation/HEAD/_using_library.html). Note the 'HEAD' in the path instead of '1.32'![/quote]

yeah, that was it. I customized some of the cmake rules in the root folder before updating it with the latest from the repository.

Btw, even though the current structure shouldn't pose a problem to long time users of Urho3D, but if you really want Urho3D framework adoption to rise quickly, you should consider use cases for the newbies who are just being exposed to this awesome framework. We should learn from other popular frameworks such as Cocos2d-x on how they lower their entry barrier to the new users thus helping the new users to adapt to the framework environment quickly. And after they are becoming more familiar with the framework, they can customize their own build systems according to what they want. We definitely can't expect all new users to be familiar with cmake rules for them to come up with their own build system right away after discovering Urho3D framework.

Just my 2 cents.

-------------------------

weitjong | 2017-01-02 01:02:30 UTC | #34

[quote="Faizol"][quote="weitjong"]The new macro create_symlink() is in our Urho3D CMake common module. Please kindly make sure you have got rid of all the old files (CMakeLists.txt and *.cmake) from the old build system. Your error message indicates somehow you still have an old file in the mix. Also Please refer to the updated documentation here [urho3d.github.io/documentation/H ... brary.html](http://urho3d.github.io/documentation/HEAD/_using_library.html). Note the 'HEAD' in the path instead of '1.32'![/quote]

yeah, that was it. I customized some of the cmake rules in the root folder before updating it with the latest from the repository.

Btw, even though the current structure shouldn't pose a problem to long time users of Urho3D, but if you really want Urho3D framework adoption to rise quickly, you should consider use cases for the newbies who are just being exposed to this awesome framework. We should learn from other popular frameworks such as Cocos2d-x on how they lower their entry barrier to the new users thus helping the new users to adapt to the framework environment quickly. And after they are becoming more familiar with the framework, they can customize their own build systems according to what they want. We definitely can't expect all new users to be familiar with cmake rules for them to come up with their own build system right away after discovering Urho3D framework.

Just my 2 cents.[/quote]
I have commented on this before. This is not the place to pick up the CMake basic or the Android development basic. Having said that, one of the recent GitHub issue has made me to realize that project structure described in the "Using Urho3D as external library" page can be made simpler to avoid misleading the newbie and the page is updated just now.

And although it has not been documented in that page, we have explained before in the other forum topics that your project can use Urho3D library as external library without the aid of our CMake modules or even without using CMake for that matter. Treat the library as any of the third party libraries you have encountered and wanted to use in your project. Do what you need to do to integrate them. Our modules are just an aid.

-------------------------

cnccsk | 2017-01-02 01:02:30 UTC | #35

after android build, can't normal run, has crashed, the logcat is below, any one know it?  (before change build system is normal) 

* daemon not running. starting it now on port 5037 *
* daemon started successfully *
--------- beginning of /dev/log/system
--------- beginning of /dev/log/main
W/Urho3D  ( 3443): Could not get application preferences directory
I/Urho3D  ( 3443): Created 3 worker threads
I/Urho3D  ( 3443): Added resource path /apk/Data/
I/Urho3D  ( 3443): Added resource path /apk/CoreData/
I/Urho3D  ( 3443): Set screen mode 1920x1080 fullscreen
I/Urho3D  ( 3443): Initialized input
I/Urho3D  ( 3443): Initialized user interface
I/Urho3D  ( 3443): Initialized renderer
I/Urho3D  ( 3443): Set audio mode 44100 Hz stereo interpolated
I/Urho3D  ( 3443): Initialized engine

-------------------------

weitjong | 2017-01-02 01:02:30 UTC | #36

[quote="cnccsk"]after android build, can't normal run, has crashed, the logcat is below, any one know it?  (before change build system is normal) 

* daemon not running. starting it now on port 5037 *
* daemon started successfully *
--------- beginning of /dev/log/system
--------- beginning of /dev/log/main
W/Urho3D  ( 3443): Could not get application preferences directory
I/Urho3D  ( 3443): Created 3 worker threads
I/Urho3D  ( 3443): Added resource path /apk/Data/
I/Urho3D  ( 3443): Added resource path /apk/CoreData/
I/Urho3D  ( 3443): Set screen mode 1920x1080 fullscreen
I/Urho3D  ( 3443): Initialized input
I/Urho3D  ( 3443): Initialized user interface
I/Urho3D  ( 3443): Initialized renderer
I/Urho3D  ( 3443): Set audio mode 44100 Hz stereo interpolated
I/Urho3D  ( 3443): Initialized engine[/quote]
I am not able to reproduce your problem on my Linux host system. I have tested running the NinjaSnowWar in the sample APK successfully in the following setup:

32-bit ARM:
API=19 ABI=armeabi-v7a URHO3D_LIB_TYPE=SHARED AVD=test_19_armeabi-v7a
API=21 ABI=armeabi-v7a URHO3D_LIB_TYPE=SHARED AVD=test_21_armeabi-v7a

32-bit INTEL:
API=21 ABI=x86 URHO3D_LIB_TYPE=SHARED AVD=test_21_x86

64-bit INTEL:
API=21 ABI=x86_64 URHO3D_LIB_TYPE=SHARED AVD=test_21_x86_64

If you are on Windows host, double check the "Android/assets" directory to ensure it contains both the "CoreData" and "Data" subdirs and that they are not empty. Also make sure you have configured your Android build tree to target the correct Android API and Android ABI; then install the APK into the compatible AVD or actual device.

-------------------------

friesencr | 2017-01-02 01:02:32 UTC | #37

I have heard, in iirc, some people are trying to implement their a different scripting language.  I think an amalgamation of each subsystem's headers into 1 file would be useful for them.  Personally, if the files could be generated cleanly, I would like the aesthetics of fewer files in the include folder, and increased readability to be a bonus.  Food for thought.

-------------------------

jmiller | 2017-01-02 01:02:33 UTC | #38

Thanks for your efforts on the build system, [b]weitjong[/b]. It has always worked like a dream for me.

I decided to try building out-of-source SDK (completely fresh HEAD checked out today, with mingw-w64)

'mingw32-make install'
[... builds everything, installs many ...]
[code]
-- Up-to-date: C:/dev/urho/share/Urho3D/Scripts/cmake_vs2013.bat
-- Installing: C:/dev/urho/include/Urho3D/ThirdParty/SDL
CMake Error at Source/ThirdParty/AngelScript/cmake_install.cmake:31 (FILE):
  file INSTALL destination: C:/dev/urho/include/Urho3D/ThirdParty/AngelScript
  is not a directory.
Call Stack (most recent call first):
  Source/cmake_install.cmake:40 (INCLUDE)
  cmake_install.cmake:64 (INCLUDE)

Makefile:64: recipe for target 'install' failed
mingw32-make: *** [install] Error 1
[/code]
[b]urho/include/Urho3D/ThirdParty/AngelScript/[/b] does exist as a symlink to the source tree (c:/dev/urho3d/Source/ThirdParty/AngelScript/include/).
Install created other symlinks and regular dirs (like SDL) successfully there..

Could probably hack around this but thought I'd report anyway (maybe tracker is preferred?)
Maybe I missed something, sleep/caffeine?

-------------------------

weitjong | 2017-01-02 01:02:33 UTC | #39

[quote="carnalis"]Thanks for your efforts on the build system, [b]weitjong[/b]. It has always worked like a dream for me.

I decided to try building out-of-source SDK (completely fresh HEAD checked out today, with mingw-w64)

'mingw32-make install'
[... builds everything, installs many ...]
[code]
-- Up-to-date: C:/dev/urho/share/Urho3D/Scripts/cmake_vs2013.bat
-- Installing: C:/dev/urho/include/Urho3D/ThirdParty/SDL
CMake Error at Source/ThirdParty/AngelScript/cmake_install.cmake:31 (FILE):
  file INSTALL destination: C:/dev/urho/include/Urho3D/ThirdParty/AngelScript
  is not a directory.
Call Stack (most recent call first):
  Source/cmake_install.cmake:40 (INCLUDE)
  cmake_install.cmake:64 (INCLUDE)

Makefile:64: recipe for target 'install' failed
mingw32-make: *** [install] Error 1
[/code]
[b]urho/include/Urho3D/ThirdParty/AngelScript/[/b] does exist as a symlink to the source tree (c:/dev/urho3d/Source/ThirdParty/AngelScript/include/).
Install created other symlinks and regular dirs (like SDL) successfully there..

Could probably hack around this but thought I'd report anyway (maybe tracker is preferred?)
Maybe I missed something, sleep/caffeine?[/quote]
You should not choose the SDK install destination location to be the same as your build tree location. You mention that you find the symlink in the 'c:/dev/urho/include/Urho3D/' path. That indicates 'c:/dev/urho' is your build tree. So, why would you want to install the SDK there again in the build tree? Our FindUrho3D CMake module has been designed to find Urho3D library from both its build tree directly and from installed SDK. It makes no difference to the module or external project referencing Urho3D  library either ways.

Try to correct your build tree to change its CMAKE_INSTALL_PREFIX to point to other location. You can edit the CMakeCache.txt in the build tree to modify this variable directly or invoke 'cmake -DCMAKE_INSTALL_PREFIX=/other/path/to/install/SDK .' in the build tree itself (replace the dot with the actual path to your build tree location if your working dir is not the build tree). And then perform the 'make install' again.

-------------------------

weitjong | 2017-01-02 01:02:33 UTC | #40

[quote="friesencr"]I have heard, in iirc, some people are trying to implement their a different scripting language.  I think an amalgamation of each subsystem's headers into 1 file would be useful for them.  Personally, if the files could be generated cleanly, I would like the aesthetics of fewer files in the include folder, and increased readability to be a bonus.  Food for thought.[/quote]
I think we have discussed this before in the other topic. IMHO, a good practice is to prefer forward declaration over include and to only include what it is needed. Having a few header files that amalgamated other header files would not only slow down the build but would also promote a bad practice, although it looks more tidy and convenient to use.

-------------------------

jmiller | 2017-01-02 01:02:33 UTC | #41

[quote="weitjong"]You should not choose the SDK install destination location to be the same as your build tree location.[/quote]

Don't park a car in an occupied parking space, got it.

But I was trying SDK because my project cannot CMake: It can't find Urho3D CMake/Modules (FindUrho3D, etc) in the build tree, pointed to by URHO3D_HOME. They only exist in the source tree. I'll go over my build again, guess I'm missing the obvious...

-------------------------

weitjong | 2017-01-02 01:02:33 UTC | #42

[quote="carnalis"][quote="weitjong"]You should not choose the SDK install destination location to be the same as your build tree location.[/quote]

Don't park a car in an occupied parking space, got it.

But I was trying SDK because my project cannot CMake: It can't find Urho3D CMake/Modules (FindUrho3D, etc) in the build tree, pointed to by URHO3D_HOME. They only exist in the source tree. I'll go over my build again, guess I'm missing the obvious...[/quote]
Yes, I have simplified the CMake module search path in the new build system. While in the old build system, it was relying on the URHO3D_HOME environment variable in the first approach (when using build tree). In the old system the URHO3D_HOME pointed to the location of the Urho3D project root (repo root), the module then made an assumption where to find the build tree location based on this project root path. We have a few negative feedback in the past because of this since the location of build tree was predetermined by our scripts and modules (not by user).

Old build system (when using build tree)
[code]# Set CMake modules search path
set (CMAKE_MODULE_PATH $ENV{URHO3D_HOME}/Source/CMake/Modules CACHE PATH "Path to Urho3D-specific CMake modules")[/code]
In the second approach (when using the installed SDK), the old build system was relying on the CMAKE_PREFIX_PATH environment variable. The search path differed between Windows host and non-Windows hosts, which was also not so nice.

Old build system (when using SDK on Windows host)
[code]# Set CMake modules search path
set (CMAKE_MODULE_PATH $ENV{CMAKE_PREFIX_PATH}/share/CMake/Modules CACHE PATH "Path to Urho3D-specific CMake modules")[/code]
Old build system (when using SDK on non-Windows host)
[code]# Set CMake modules search path
set (CMAKE_MODULE_PATH $ENV{CMAKE_PREFIX_PATH}/share/Urho3D/CMake/Modules CACHE PATH "Path to Urho3D-specific CMake modules")[/code]

In the new build system I try to simplify all this. It now always expects that each project has its own "CMake" subdir in its root, regardless of whether build tree or installed SDK is being used. User would have to manually copy or symlink this subdir when preparing the new project structure. When the SDK is installed in the system-wide default location then that is all required to find the library. However, when the SDK is installed in a non-default location or not being installed at all (i.e. when using build tree directly), only then the URHO3D_HOME environment variable is required to be set to point to the path of this non-default SDK installation location or to the path of the build tree itself. Again, in any cases the CMake module search path as shown below never changes now in the new system.

New build system:
[code]# Set CMake modules search path
set (CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/CMake/Modules)[/code]
And since it is not depending on any environment variable, it does not need to be cached now, which simplify the construct even further.

In short, if CMake complains that it cannot find the "Urho3D-CMake-common" module then fix the search path according to the new build system and remember to copy/symlink the "CMake" subdir to your own project root.

-------------------------

jmiller | 2017-01-02 01:02:34 UTC | #43

Thanks - with your explanation, I got it working right away. Does seem to be a better system.

-------------------------

weitjong | 2017-01-02 01:02:45 UTC | #44

I did it again. The what used to be the "Bin" dir in the source tree is now renamed to "bin" (small letter case). Supposedly this should not impact users on Windows host or Mac OS X host with case-insensitive journaled filesystem. However, it is exactly because of this, the 'git mv Bin bin' in the recent commit in the master branch may not be applied consistently in this situation. i.e. after a git pull from master branch, users using these filesystem may want to do a manual 'mv Bin bin' in your source tree to change it to small letter case. Although not doing so will not break your build as the filesystem cannot tell the differences, but it will be good to do so for consistency sake. Other case-sensitive filesystems should get the changes correctly after a git pull.

I promise this will be the last change in the new build system that may impact you directly.

-------------------------

OvermindDL1 | 2017-01-02 01:02:45 UTC | #45

[quote="weitjong"]I did it again. The what used to be the "Bin" dir in the source tree is now renamed to "bin" (small letter case). Supposedly this should not impact users on Windows host or Mac OS X host with case-insensitive journaled filesystem. However, it is exactly because of this, the 'git mv Bin bin' in the recent commit in the master branch may not be applied consistently in this situation. i.e. after a git pull from master branch, users using these filesystem may want to do a manual 'mv Bin bin' in your source tree to change it to small letter case. Although not doing so will not break your build as the filesystem cannot tell the differences, but it will be good to do so for consistency sake. Other case-sensitive filesystems should get the changes correctly after a git pull.

I promise this will be the last change in the new build system that may impact you directly.[/quote]
Ooo, yay, really prefer the lowercase as it is what all others do, you have no idea how often I type `cd bin` and it say that it does not exist and I sit confused for a second.  ^.^
Now, what about Source -> src?  :wink:

-------------------------

weitjong | 2017-01-02 01:02:45 UTC | #46

I did promise to myself this will be the last change, remember?  :wink:

-------------------------

OvermindDL1 | 2017-01-02 01:02:45 UTC | #47

[quote="weitjong"]I did promise to myself this will be the last change, remember?  :wink:[/quote]
Can always hope.  ^.^

-------------------------

cnccsk | 2017-01-02 01:02:49 UTC | #48

Hi,

I tested Android again today, can't run normal, I confirm that assets dir is correct,

[code]
I/DEBUG   (  284): backtrace:
I/DEBUG   (  284):     #00  pc 00516380  /data/app-lib/com.github.urho3d-1/libUrho3DPlayer.so
I/DEBUG   (  284):          7a65f614  78ba0299  /data/app-lib/com.github.urho3d-1/libUrho3DPlayer.so (asCParser::~asCParser()+18)
I/DEBUG   (  284):          7a65f624  78bbcfc7  /data/app-lib/com.github.urho3d-1/libUrho3DPlayer.so (asCCompiler::CompileFunction(asCBuilder*, asCScriptCode*, asCArray<asCString>&, asCScriptNode*, asCScriptFunction*, sClassDeclaration*)+758)
I/DEBUG   (  284):          7a65f62c  78b97b31  /data/app-lib/com.github.urho3d-1/libUrho3DPlayer.so (asCScriptFunction::GetDeclarationStr(bool, bool, bool) const+1012)
I/DEBUG   (  284):          7a65f63c  78a66007  /data/app-lib/com.github.urho3d-1/libUrho3DPlayer.so (asCDataType::GetSizeOnStackDWords() const+46)
I/DEBUG   (  284):          7a65f64c  78bbd1a7  /data/app-lib/com.github.urho3d-1/libUrho3DPlayer.so (CallSystemFunctionNative(asCContext*, asCScriptFunction*, void*, unsigned long*, void*, unsigned long long&)+374)
I/DEBUG   (  284):          7a65f680  7243202c  /system/framework/framework-res.apk
I/DEBUG   (  284):          7a65f684  00000005  
I/DEBUG   (  284):          7a65f688  00000000  
I/DEBUG   (  284):          7a65f68c  40880000  /system/lib/libicui18n.so (icu_51::Region::getInstance(int, UErrorCode&)+467)
.....
E/ActivityManager( 1059): App crashed! Process: com.github.urho3d
[/code]

the full log is :

[gist.github.com/zenithght/50f31931a368cb7c2824](https://gist.github.com/zenithght/50f31931a368cb7c2824)


Thanks,

Zenith.

-------------------------

weitjong | 2017-01-02 01:02:49 UTC | #49

I am afraid I have no idea why.

EDIT: But I am able to reproduce the problem this time. I was not able reproduce the app crash two weeks ago. So, probably one of the commit since then break it.

-------------------------

weitjong | 2017-01-02 01:02:52 UTC | #50

I figure out what happened on my case. Perhaps it is the same root cause for your Android build too. My problem was caused by outdated symlinks in the Urho3D project root (source tree). The symlinks were outdated due to renaming of "Bin" subdir to "bin". For your case, it could be already made outdated due to moving of "Android" subdir from "Source" to project root. Anyway, to correct this, I simply deleted the outdated symlinks found inside the "Android/assets" directory and let the symlinks be recreated again by invoking Urho3D build scripts. I have tested to deploy the sample app to my actual Android devices (Samsung Tab3 and S3) this time and they work correctly without crashes. However, I observe a weird color output on S3, which is totally another issue. I haven't observed this before. On Tab3 everything is ok.

-------------------------

friesencr | 2017-01-02 01:02:52 UTC | #51

I am looking forward to our next release.  The new include folder structure with packed libs/bins will package really well.

-------------------------

cnccsk | 2017-01-02 01:02:52 UTC | #52

[quote="weitjong"]I figure out what happened on my case. Perhaps it is the same root cause for your Android build too. My problem was caused by outdated symlinks in the Urho3D project root (source tree). The symlinks were outdated due to renaming of "Bin" subdir to "bin". For your case, it could be already made outdated due to moving of "Android" subdir from "Source" to project root. Anyway, to correct this, I simply deleted the outdated symlinks found inside the "Android/assets" directory and let the symlinks be recreated again by invoking Urho3D build scripts. I have tested to deploy the sample app to my actual Android devices (Samsung Tab3 and S3) this time and they work correctly without crashes. However, I observe a weird color output on S3, which is totally another issue. I haven't observed this before. On Tab3 everything is ok.[/quote]

Thanks, @weitjong

Today I upgrade my android_ndk to android-ndk-r10, everything is ok,

Thanks again.

-------------------------

devrich | 2017-01-02 01:02:52 UTC | #53

[quote="friesencr"]I am looking forward to our next release.  The new include folder structure with packed libs/bins will package really well.[/quote]

+1 I'm all for packaging better especially for bigger games and complex 3D simulation projects like what I have i mind for Urho3D   :smiley:

-------------------------

sabotage3d | 2017-01-02 01:02:52 UTC | #54

Hey guys any chance we can get relative paths when we build Xcode projects for OSX and IOS ?
At the moment everything is hardcoded with fullpaths which means changing the folder name above will result into errors.

-------------------------

weitjong | 2017-01-02 01:02:52 UTC | #55

[quote="sabotage3d"]Hey guys any chance we can get relative paths when we build Xcode projects for OSX and IOS ?
At the moment everything is hardcoded with fullpaths which means changing the folder name above will result into errors.[/quote]
I am not really sure what you are referring to by "relative paths" here. If you are referring to the build tree location and source tree location that use fully qualified paths, which make it impossible to move the build tree after it has been configured and generated, then you are quite right about it. But there is nothing we could do about it, I think.

-------------------------

cadaver | 2017-01-02 01:02:52 UTC | #56

Yeah that seems the same on Windows / MSVC too. CMake likes to burn absolute paths into the solution / project files.

-------------------------

sabotage3d | 2017-01-02 01:02:53 UTC | #57

Have anyone tried this option: [cmake.org/cmake/help/v3.0/va ... PATHS.html](http://www.cmake.org/cmake/help/v3.0/variable/CMAKE_USE_RELATIVE_PATHS.html)

-------------------------

weitjong | 2017-01-02 01:02:53 UTC | #58

No, have you? Regardless, I think that link itself has said it all. If I understanding it correctly then it will only be beneficial in a very limited use cases.

-------------------------

cnccsk | 2017-01-02 01:03:05 UTC | #59

Hi, weitjong,
I update your new cmake_generic.bat, can't build

cmake_vs2013.bat windows
CMake Error: The source directory "G:/pro5/Urho3D_tttt/windows" does not appear to contain CMakeLists.txt.

I rolled back cmake_generic.bat, it's worked

I think it need to fix, 

Revision: 8e81d3ff364617bd3dec7dbcb42ec69d4ef149f3
Date: 2015/1/29 15:36:04
Message:
Use regex replacement to handle path with spaces in between correctly.
  ===>  Modified: cmake_generic.bat

-------------------------

weitjong | 2017-01-02 01:03:06 UTC | #60

My apology. I got lazy the other day and applied the similar changes that I have to made for cmake_generic.sh (for handling source/build tree paths with spaces in between) to the cmake_generic.bat as well, without actually testing/verifying the changes on Windows host. The changes has been reverted now in the master branch. I am not entirely sure, but as the result probably on Windows host our build scripts do not work with the source/build tree paths containing spaces. I did not test that before making the change the other day even. Really hate to boot up the operating system that slashes "backward".  :wink:

-------------------------

cadaver | 2017-01-02 01:03:09 UTC | #61

I now get this when trying to create a Lua -including build using MinGW. Guess this is related to the added GCC precompiled header support. Is it a matter of using too old GCC / MinGW? (I have 4.8.1 here)

[code]
g++.exe: fatal error: cannot specify -o with -c, -S or -E with multiple files compilation terminated.
Source\Urho3D\CMakeFiles\Urho3D.dir\build.make:1107: recipe for target 'Source/Urho3D/CMakeFiles/Urho3D.dir/generated/AudioLuaAPI.cpp.obj' failed
[/code]

-------------------------

weitjong | 2017-01-02 01:03:10 UTC | #62

I am using MinGW-W64 version 4.9.1 which I installed it quite some time ago already. So it may not be the latest but it is able to precompile the header just fine. Test it with Lua and LuaJIT enabled, separately.

-------------------------

practicing01 | 2017-01-02 01:03:38 UTC | #63

I'm able to compile urho3d on linux and the apk for android.  I've raked into a test folder elsewhere and can compile for linux there.  I try to run cmake_android.sh however, I get this error: 
[code]
./cmake_android.sh ./android_Build/
-- Found Urho3D: /home/practicing01/Desktop/Programming/Urho3D/Build/lib/libUrho3D.a
-- Configuring incomplete, errors occurred!
See also "/home/practicing01/Desktop/Programming/test/android_Build/CMakeFiles/CMakeOutput.log".
CMake Error at CMake/Modules/Urho3D-CMake-common.cmake:831 (message):
  Could not find SDL_android_main.c source file in the Urho3D build tree or
  SDK installation.  Please reconfigure and rebuild your Urho3D build tree;
  or reinstall the SDK.
Call Stack (most recent call first):
  CMakeLists.txt:38 (setup_main_executable)
[/code]

Edit:  I tried following [url=http://discourse.urho3d.io/t/solved-using-scripting-with-android/386/1]this[/url] post but there's no cmake_gcc.sh so I used cmake_android.sh instead.  Not sure if the gcc version did something special.

-------------------------

weitjong | 2017-01-02 01:03:42 UTC | #64

That post is rather out-dated now by the new build system improvement in the master branch. The cmake_gcc.sh is now renamed to cmake_generic.sh. The cmake_android.sh is basically just a convenient script which supplies additional build options for the Android build but otherwise also calls the cmake_generic.sh under the hood.

Back to your project configuration/generation problem. I suspect you have not set the URHO3D_HOME variable correctly.

-------------------------

practicing01 | 2017-01-02 01:03:44 UTC | #65

I have it set to /home/practicing01/Desktop/Programming/Urho3D/Build .  That's what I passed to cmake_generic.sh, the source root is at  /home/practicing01/Desktop/Programming/Urho3D .  The project in question was raked into  /home/practicing01/Desktop/Programming/Project .

-------------------------

weitjong | 2017-01-02 01:03:44 UTC | #66

I am a bit confused now. Are you trying to do an Android build or a native (desktop) build? For sure you cannot use Urho3D [b]native[/b] build tree (which your URHO3D_HOME points to) in your attempt to generate an [b]Android[/b] build for your newly rake-scaffolded project. The missing "SDL_android_main.c" file is only "installed" in the Urho3D [b]Android [/b]build tree and not the native one.

-------------------------

practicing01 | 2017-01-02 01:03:44 UTC | #67

I need both, native is working, how do I get android working?

-------------------------

weitjong | 2017-01-02 01:03:44 UTC | #68

You can have both of them working as long as you don't mix the build trees between different platforms.

-------------------------

practicing01 | 2017-01-02 01:03:44 UTC | #69

For both the engine and my raked project, when I ran cmake_android.sh I specified ../android-Build as the destination.  The engine native/android compile/run fine and the raked native compiles/runs fine.  After I raked, I ran cmake_android.sh ../android-Build within the raked project's root and got the error mentioned above.

-------------------------

weitjong | 2017-01-02 01:03:45 UTC | #70

[b]Don't[/b] mix build trees!

For native build targeting desktop platform:
[ol][li] To build Urho3D library
./cmake_generic.sh [color=#00BF00]URHO3D-NATIVE-BUILD-TREE-PATH[/color] -DTURN-ON-WHATEVER-BUILD-OPTIONS=1 && cd [color=#00BF00]URHO3D-NATIVE-BUILD-TREE-PATH[/color] && make[/li]
[li] To build your own project referencing the [b]native[/b] Urho3D library
URHO3D_HOME=[color=#00BF00]URHO3D-NATIVE-BUILD-TREE-PATH[/color] ./cmake_generic.sh [color=#BFBF00]YOUR-NATIVE-BUILD-TREE-PATH[/color] -DTURN-ON-WHATEVER-BUILD-OPTIONS=1 && cd [color=#BFBF00]YOUR-NATIVE-BUILD-TREE-PATH[/color] && make[/li][/ol]

For cross-platform build targeting Android platform:
[ol][li] To build Urho3D library
./cmake_android.sh [color=#0080FF]URHO3D-ANDROID-BUILD-TREE-PATH[/color] -DTURN-ON-WHATEVER-BUILD-OPTIONS=1 && cd [color=#0080FF]URHO3D-ANDROID-BUILD-TREE-PATH[/color] && make[/li]
[li] To build your own project referencing the [b]Android[/b] Urho3D library
URHO3D_HOME=[color=#0080FF]URHO3D-ANDROID-BUILD-TREE-PATH[/color] ./cmake_android.sh [color=#BF80FF]YOUR-ANDROID-BUILD-TREE-PATH[/color] -DTURN-ON-WHATEVER-BUILD-OPTIONS=1 && cd [color=#BF80FF]YOUR-ANDROID-BUILD-TREE-PATH[/color] && make[/li][/ol]

Replace URHO3D-NATIVE-BUILD-TREE-PATH, YOUR-NATIVE-BUILD-TREE-PATH, URHO3D-ANDROID-BUILD-TREE-PATH, YOUR-ANDROID-BUILD-TREE-PATH with the real paths that you use. Under NO circumstances these paths are pointing to a same directory, i.e. no sharing.

[quote="practicing01"]The engine native/android compile/run fine[/quote]
Sharing build trees for different platforms are not supported. You are on your own to make it works in all the use cases if you insist to do so.

-------------------------

practicing01 | 2017-01-02 01:03:45 UTC | #71

I had not tried changing URHO3D_HOME to point to the engine android build folder.  After trying that, same error. Maybe some pictures will help.

Urho3D root:
[spoiler][img]http://img.ctrlv.in/img/15/02/26/54eeb5f3bef1e.png[/img][/spoiler]

Urho3D build:
[spoiler][img]http://img.ctrlv.in/img/15/02/26/54eeb63a7bee9.png[/img][/spoiler]

Urho3D android build:
[spoiler][img]http://img.ctrlv.in/img/15/02/26/54eeb65db1b4b.png[/img][/spoiler]

project root after rake:
[spoiler][img]http://img.ctrlv.in/img/15/02/26/54eeb68047518.png[/img][/spoiler]

project build after cmake_generic:
[spoiler][img]http://img.ctrlv.in/img/15/02/26/54eeb6a56ad6c.png[/img][/spoiler]

project android build after cmake_android attempt:
[spoiler][img]http://img.ctrlv.in/img/15/02/26/54eeb6d60d098.png[/img][/spoiler]

-------------------------

weitjong | 2017-01-02 01:03:45 UTC | #72

[quote="practicing01"]I had not tried changing URHO3D_HOME to point to the engine android build folder.  After trying that, same error. Maybe some pictures will help.[/quote]
That's exactly the problem. Unless you have Urho3D SDK installed in your host's system wide default installation location, you should and must set URHO3D_HOME correctly at the time when you invoke the build script initially to configure and generate your project file. Afterward, the URHO3D_HOME is cached.

BTW, your screenshots do not tell me anything new.

-------------------------

practicing01 | 2017-01-02 01:03:45 UTC | #73

Ok I *think* I got it working.  I deleted the android build folder incase it was "caching" bad things, set the urho home variable to that android build folder, then ran cmake_android plus went through the apk creation steps.  Then I went back to my project, deleted the previous android build folder, ran cmake_android but got the same damn error... it did create a cmake file though which I opened in cmake-gui and set the urho home variable to point to the android-Build folder that I created for the engine.  Then I ran cmake_android again and viola.  After that I copied the missing android files based on the previously mentioned link, followed the apk generation steps and it was successfull.  I haven't tested the apk but it will probably work.

Thanks for the help but I'd like to suggest two things: that either seperate environment variables be used for each platform or just one variable that would work for all.  Second, to make the build process easier :stuck_out_tongue:

-------------------------

weitjong | 2017-01-02 01:03:46 UTC | #74

[quote="practicing01"]Thanks for the help but I'd like to suggest two things: that either seperate environment variables be used for each platform or just one variable that would work for all.  Second, to make the build process easier :stuck_out_tongue:[/quote]
Glad to hear you have figured it out. Regarding your suggestions. Your first suggestion would make build scripting harder than necessary (see how our Rakefile can use the same build tasks for all the Urho3D supported platforms without any issues). For your second suggestion, you have to be more concrete on what can be improved further, but otherwise I agree with you that there are still rooms for improvement.

-------------------------

NiteLordz | 2017-01-02 01:03:47 UTC | #75

Is it possible to build the emscripten platform within a Windows environment, (i don't have MinGW installed at the moment. I have the emscripten sdk and visual studio).

-------------------------

weitjong | 2017-01-02 01:03:48 UTC | #76

In theory I think it should be possible. In the Emscripten original CMake "toolchain" file there is a reference to experimental support for VS. However, we use our own modified version of CMake/Emscripten toolchain file and that experimental part does not get included in our version. I am not familiar enough with VS but if you are interested in getting it to work in VS, I/we should be able to help you to fix any problems you would encounter along.

-------------------------

thebluefish | 2017-01-02 01:04:15 UTC | #77

I am finally upgrading to the latest branch from 1.32 because 1.32 is simply too out of date.

Currently in Windows, the build path is appended to my user folder. Is there a way to change this to be a path relative to the Urho3D root folder?

I need to ensure that I don't use environment variables when building. When I do build on Linux, is there anything I need to keep in mind because of this?

-------------------------

weitjong | 2017-01-02 01:04:15 UTC | #78

[quote="thebluefish"]Currently in Windows, the build path is appended to my user folder. Is there a way to change this to be a path relative to the Urho3D root folder?[/quote]
I think so. You should be able to specify the CMake build tree path anywhere you like using an absolute path or a relative path to Urho3D project root (which is also now the CMake source tree in the new build system). In Linux host system, I think I could even specify a build tree owned by a different user than the source tree's owner. For example:

# Build tree is created inside the source tree using relative path
cmake_generic.bat native-Build

# Build tree is created outside the source tree using relative path
cmake_generic.bat ..\native-Build

I hope this answered your question.

[quote="thebluefish"]I need to ensure that I don't use environment variables when building. When I do build on Linux, is there anything I need to keep in mind because of this?[/quote]
You don't say why you don't like to use environment variables when building. Personally, I think using the environment variables is one way to get thing done without hard-coding across different environments (read: host systems). Also there are two more things you would want to know regarding this:
[ol][li] Most of the supported environment variables for building and using Urho3D can also be specified as if they are build options. So using '-DURHO3D_HOME=/some/path' also works.[/li]
[li] The value is cached for subsequent CMake invocation. So you don't have to specify the same environment variable or build option again and again each time.[/li][/ol]
To answer you question directly - No, you don't have to use them if you really don't like them.

You can specify a build option (which is a CMake variable under the hood) similarly between Windows and Linux hosts systems. You can specify an environment variable [b]almost[/b] similarly between these two systems.

# Windows
set "URHO3D_HOME=%HOMEPATH%\Urho3D-SDK"

# Linux using Bash shell
export URHO3D_HOME=$HOME/Urho3D-SDK

I suppose it is important to keep in mind to check what is your login shell. There are more shells out there than I could hope for to master them all in my life time. Having said that, Bash shell is the default shell in most of the modern Linux distros these days. So, you should be fine by sticking to it.

-------------------------

thebluefish | 2017-01-02 01:04:16 UTC | #79

Hm, that's weird. I put ../Build after the cmake command and it still put the folder in my user folder.

I don't like environment variables because we have multiple builds of Urho3D. This is to ensure portability and to ensure that we're not breaking an older project by working against the latest version of Urho3D. For portability, I can just move my project wherever and it will still build without needing to worry about different versions and the like. That's the reason I dislike CMake, but it works fine enough for this.

Edit: It looks like GLEW isn't added to the /include/Urho3D/ThirdParty directory after building. I cannot include GraphicsImpl.h when building against OpenGL for this purpose.

-------------------------

vivienneanthony | 2017-01-02 01:04:22 UTC | #80

Hello

I compiled Urho3D master with the following command line

[b] ./cmake_generic.sh /media/home2/vivienne/Urho3D-mastercurrent  -DURHO3D_64BIT=1 -DURHO3D_SAMPLES=1 -DCMAKE_BUILD_TYPE=RelWithDebInfo[/b]

which produced this structure..

[code]-rwxrwxr-x  1 vivienne vivienne 66741466 Mar 24 01:24 01_HelloWorld
-rwxrwxr-x  1 vivienne vivienne 66883438 Mar 24 01:24 02_HelloGUI
-rwxrwxr-x  1 vivienne vivienne 66767950 Mar 24 01:24 03_Sprites
-rwxrwxr-x  1 vivienne vivienne 66799779 Mar 24 01:24 04_StaticScene
-rwxrwxr-x  1 vivienne vivienne 67026175 Mar 24 01:24 05_AnimatingScene
-rwxrwxr-x  1 vivienne vivienne 67059597 Mar 24 01:24 06_SkeletalAnimation
-rwxrwxr-x  1 vivienne vivienne 66842575 Mar 24 01:25 07_Billboards
-rwxrwxr-x  1 vivienne vivienne 66836910 Mar 24 01:25 08_Decals
-rw-rw-r--  1 vivienne vivienne      625 Mar 22 21:30 ConvertModels.bat
drwxrwxr-x  7 vivienne vivienne     4096 Mar 22 21:30 CoreData
drwxrwxr-x 16 vivienne vivienne     4096 Mar 23 22:03 Data
-rw-rw-r--  1 vivienne vivienne      298 Mar 22 21:30 Editor.bat
-rwxr-xr-x  1 vivienne vivienne      216 Mar 22 21:30 Editor.sh
-rw-rw-r--  1 vivienne vivienne      918 Mar 22 21:30 NinjaSnowWar.bat
-rwxr-xr-x  1 vivienne vivienne      819 Mar 22 21:30 NinjaSnowWar.sh
drwxrwxr-x  2 vivienne vivienne     4096 Mar 24 01:24 tool
-rwxrwxr-x  1 vivienne vivienne 89662057 Mar 24 01:21 Urho3DPlayer
[/code]

If I try make install, it is putting all the binaries at /usr/local/bin and the reseoruces are placed in the /usr/local/share/Urho3D

[code]-- Installing: /usr/local/share/Urho3D/Resources/Data/Urho2D/GoldIcon/1.png
-- Installing: /usr/local/share/Urho3D/Resources/Data/Urho2D/GoldIcon/5.png
-- Installing: /usr/local/share/Urho3D/Resources/Data/Urho2D/GoldIcon/2.png
-- Installing: /usr/local/share/Urho3D/Resources/Data/Urho2D/GoldIcon/4.png
-- Installing: /usr/local/share/Urho3D/Resources/Data/Fonts
-- Installing: /usr/local/share/Urho3D/Resources/Data/Fonts/BlueHighway.png
-- Installing: /usr/local/share/Urho3D/Resources/Data/Fonts/BlueHighway.sdf
-- Installing: /usr/local/share/Urho3D/Resources/Data/Fonts/read_me.html
-- Installing: /usr/local/bin/29_SoundSynthesis
-- Installing: /usr/local/bin/30_LightAnimation
-- Installing: /usr/local/bin/31_MaterialAnimation[/code]

I would like the executables to be in /usr/local/share/Urho3D where the resources are.

Am I doing something wrong?

Viv

-------------------------

weitjong | 2017-01-02 01:04:23 UTC | #81

Please do not cross post the same question on multiple forums.

-------------------------

vivienneanthony | 2017-01-02 01:04:23 UTC | #82

No problem.

-------------------------

globus | 2017-01-02 01:04:24 UTC | #83

Hi all.

On [u]Windows[/u] platform (XP) i try to build the engine on [u]MinGW w64 and Code::Blocks[/u]

[b]Error In the build time[/b]:
CMakeFiles\Makefile2   1012   recipe for target 'Source/Urho3D/CMakeFiles/Urho3D.dir/all' failed
E:\U3D\2\Makefile        135    recipe for target 'all' failed

[b]Makefile2 line 1012 content[/b]:
    $(MAKE) -f Source\Urho3D\CMakeFiles\Urho3D.dir\build.make Source/Urho3D/CMakeFiles/Urho3D.dir/depend

[b]Makefile  line  135  content[/b]:
    $(CMAKE_COMMAND) -E cmake_progress_start E:\U3D\2\CMakeFiles E:\U3D\2\CMakeFiles\progress.marks
 
[b]And Build Log say[/b]:

Built target LibCpuId
C:/mingw32/bin/mingw32-make.exe -f Source\Urho3D\CMakeFiles\Urho3D.dir\build.make Source/Urho3D/CMakeFiles/Urho3D.dir/depend

mingw32-make.exe[2]: *** [b]No rule to make target[/b] '../Source/Urho3D/[color=#0000BF]Precompiled.h[/color] E:/U3D/2/Source/Urho3D/[color=#0000BF]Urho3D.h[/color]', [b]needed by[/b] 'Source/Urho3D/[color=#0000BF]Precompiled.h.Release.pch.trigger[/color]'.  Stop.

mingw32-make.exe[1]: *** [Source/Urho3D/CMakeFiles/Urho3D.dir/all] Error 2
mingw32-make.exe: *** [all] Error 2
mingw32-make.exe[2]: Entering directory 'E:/U3D/2'
mingw32-make.exe[2]: Leaving directory 'E:/U3D/2'
CMakeFiles\Makefile2:1012: recipe for target 'Source/Urho3D/CMakeFiles/Urho3D.dir/all' failed
mingw32-make.exe[1]: Leaving directory 'E:/U3D/2'
E:/U3D/2/Makefile:135: recipe for target 'all' failed
Process terminated with status 2 (0 minute(s), 19 second(s))
2 error(s), 0 warning(s) (0 minute(s), 19 second(s))

-------------------------

globus | 2017-01-02 01:04:25 UTC | #84

[b]Full Build Log[/b] (from Code::Blocks) in txt file:
[url]https://yadi.sk/i/kHuxD4bjfWB4K[/url]

[b]Advanced info[/b]:
When i generate and compile engine with VS2008 it ok.

Description form [url]http://urho3d.github.io/about.html[/url]
Supported build tools and IDEs: 
Visual Studio, Xcode, Eclipse, CodeBlocks, QtCreator, GCC, [b]LLVM/Clang[/b], MinGW

Anybody compile engine with LLVM/Clang ?

-------------------------

weitjong | 2017-01-02 01:04:25 UTC | #85

Regarding your problem with Code::Blocks on Windows XP, I think it is more useful if you post the output of CMake when it configured and generated the *.cbp project file. I have not seen XP in action for a few years now, so I could not comment more on your particular problem. Having said that, we have a number of success stories from users who use C::B as their IDE on both Windows and Linux host systems. I myself have no problem with it on my Linux. I do recall a few cases where Code::Blocks users on Windows encountering problem due to the default TDM-GCC MinGW that come bundled with C::B. Our standard recommendation is, install the standalone MinGW-W64 compiler toolchain separately and then configure your C::B and CMake to find and use the MinGW-W64 compiler toolchain. This can be done by ensuring the toolchain executables are in the PATH environment variable.

One last note on this. We have recently also enhanced our common CMake module to enable precompiled header for GCC/Clang. One beneficial side effect of this is, any incompatible or too-old-version compiler toolchain would already falter at the time of CMake attempting to configure and generate the project file, instead of have to wait until the actual build time. BTW, this is the reason why I ask you to double check the output of CMake first. TDM-GCC MinGW is one of the confirmed compiler that doesn't cut it.

As for the LLVM/Clang. We have test build the Urho3D library with it in each CI build. The last 4 build jobs on Linux CI build environment are using Clang, see [travis-ci.org/urho3d/Urho3D/builds/55791878](https://travis-ci.org/urho3d/Urho3D/builds/55791878).

-------------------------

globus | 2017-01-02 01:04:25 UTC | #86

Thanks [b]weitjong[/b] for reply.

I complete solved my problem with Unofficial Urho3D Wiki
[url]http://urho3d.wikia.com/wiki/Unofficial_Urho3D_Wiki[/url] 
with small changes.

In this time i can do compile engine with CodeBlocks and also in command line.

Why I do not use VS2008 ?
VS2008 works fine in windows but i want to have a one IDE and compiler for different platforms.

Also, CodeBlocks + GCC is more lightweight and portable working environment.

-------------------------

globus | 2017-01-02 01:04:44 UTC | #87

Dubl libs includes in linklibs.rsp

For example:
In 01_HelloWorld.dir\[b]linklibs.rsp[/b]

[spoiler]../../../lib/libUrho3D.a [u]-luser32[/u] -lgdi32 -lwinmm -limm32 -lole32 [b]-loleaut32[/b] -lversion -luuid -lws2_32 -lwinmm -lopengl32 -limm32 -lole32 [b]-loleaut32[/b] -lversion -luuid -lws2_32 -lopengl32 -lkernel32 [u]-luser32[/u] -lgdi32 -lwinspool -lshell32 -lole32 [b]-loleaut32[/b] -luuid -lcomdlg32 -ladvapi32[/spoiler]

-------------------------

weitjong | 2017-01-02 01:04:44 UTC | #88

You didn't say whether it resulted in a link error or not. If it was not then don't bother with it.

The longer answer. The link order is important for GCC compiler (and its derivatives too). It is perfectly valid to have a same library to appear more than one time in the link list, especially when there is circular dependency between the libs. In this particular case, probably there is better way to avoid the repetition by utilizing special linker flags to aid linker to resolve the dependency problem. However, we rely on CMake to generate this (and all the other things too) automatically. We don't have direct control in this matter (at least to me with my current understanding of how CMake works).

-------------------------

globus | 2017-01-02 01:04:45 UTC | #89

Ok, it not produce errors.
I look to it for create my own Makefile as start point.
I am not want use CMake. :slight_smile:

-------------------------

