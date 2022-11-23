sabotage3d | 2017-01-02 01:06:48 UTC | #1

Hi I have build Urho3d for android succesfully I tested the apk and everything works. If I want to make a seperate C++ based project using Urho3d and to build it for Android what would be the steps ? 

I have added this for my CMake project.
[code]# Include Urho3D Cmake common module
include (Urho3D-CMake-common)

# Find Urho3D library
find_package (Urho3D REQUIRED)
include_directories (${URHO3D_INCLUDE_DIRS})[/code]

After that I am doing cmake -DANDROID=1 .. . But I am getting this:
[code]CMake Error at CMake/Modules/Urho3D-CMake-common.cmake:722 (message):
  Could not find SDL_android_main.c source file in the Urho3D build tree or
  SDK installation.  Please reconfigure and rebuild your Urho3D build tree;
  or reinstall the SDK.
Call Stack (most recent call first):
  CMakeLists.txt:58 (setup_main_executable)[/code]

Thanks in advance,

Alex

-------------------------

jmiller | 2017-01-02 01:06:49 UTC | #2

Hi Alex,

CMake cache error, perhaps? [topic729-20.html#p4037](http://discourse.urho3d.io/t/new-build-system/715/22)

For building Android/C++ in general...

[b]zakk[/b]'s tutorial and this discussion was helpful, and could be touched up for the wiki.
[topic378.html#p2126](http://discourse.urho3d.io/t/solved-using-scripting-with-android/386/8)

I do the scaffolding without rake. In brief: copying Urho3D/Android/* to build-android tree, editing .properties and XML files ( [developer.android.com/tools/projects/index.html](http://developer.android.com/tools/projects/index.html) ), and also in the build tree, have assets/ with symlinks or dirs CoreData and Data.

-------------------------

sabotage3d | 2017-01-02 01:06:50 UTC | #3

Thanks carnalis I got it working via the CMake tool-chain .

-------------------------

