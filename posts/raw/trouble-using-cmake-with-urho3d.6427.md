8Xt835nbsWscUMc | 2020-10-11 14:24:18 UTC | #1

I'm a beginner to CMAKE. I'm trying to compile a dummy `main.cpp` while using Urho3D library. Below are the location of files:

D:\cppLibs\Urho3D-1.7.1 (extracted zip file, untouched dir)
D:\projectName\client\cpp\CMakeLists.txt
D:\projectName\client\cpp\src\main.cpp

Currently I wanna keep this kind of tree, rather than placing engine's files inside project folder. Below is the CMakeLists.txt file:

cmake_minimum_required(VERSION 3.2.3)
if(COMMAND cmake_policy)
    cmake_policy (SET CMP0003 NEW)
    cmake_policy (SET CMP0022 NEW)
    cmake_policy (SET CMP0026 OLD)
    cmake_policy (SET CMP0042 NEW)
    cmake_policy (SET CMP0063 OLD)
endif()
project("projectName")
set(ENV{URHO3D_HOME} D:/cppLibs/Urho3D-1.7.1)
set(CMAKE_MODULE_PATH D:/cppLibs/Urho3D-1.7.1/CMake/Modules)
include(UrhoCommon)
include_directories(D:/cppLibs)
add_executable("projectName" src/main.cpp)

As you can see I don't want yet to build for all platforms, I want just to compile `main.cpp`. I get the following error at `D:/cppLibs/Urho3D-1.7.1/CMake/Modules/UrhoCommon.cmake:231`:

Could NOT find compatible Urho3D library in Urho3D SDK installation or build tree

-------------------------

weitjong | 2020-10-11 18:28:33 UTC | #2

If you just starting a new project then please use the master branch. You can setup your new project similarly than the above. Your issue is mainly caused by the wrong URHO3D_HOME value. It needs to be pointing to a build tree containing Urho3D include/headers and Urho3D lib.

So below is definitely wrong. Change it to a path where you HAVE build the Urho3D library, aka the build tree. Alternatively, just do a INSTALL after you built the library. Then you can remove this line.
[quote="8Xt835nbsWscUMc, post:1, topic:6427"]
set(ENV{URHO3D_HOME} D:/cppLibs/Urho3D-1.7.1)
[/quote]

So does this one. Remove this.
[quote="8Xt835nbsWscUMc, post:1, topic:6427"]
include_directories(D:/cppLibs)
[/quote]

Although this line is not wrong, it is not enough to completely setup the target. You are better of using the provided macro to setup a main target. See one of our example.
[quote="8Xt835nbsWscUMc, post:1, topic:6427"]
add_executable(“projectName” src/main.cpp)
[/quote]

-------------------------

8Xt835nbsWscUMc | 2020-10-11 18:30:58 UTC | #3

Thanks for answer. I fixed it. The problem was that I did not built the engine

As a side note, maybe it's a good idea to put on the official site a small code demo to copy-paste in order to make sure everything works right. Something like a blank window

-------------------------

George1 | 2020-10-12 01:58:21 UTC | #4

You should use the latest version in Github!

-------------------------

8Xt835nbsWscUMc | 2020-10-12 07:07:21 UTC | #5

I don't understand what's with the latest version. On Github, 1.8 is showed as alpha, while 1.7.1 is the latest stable. Why should I work with 1.8? Also, if there's important reasons to switch, why the .zip download button on the official site provide 1.7.1 rather than 1.8?

-------------------------

JTippetts1 | 2020-10-12 14:33:06 UTC | #7

"Official" releases have always kind of been in a weird place with Urho3D. 1.7 is especially buggy, with several major issues that continually crop up, so you are highly encouraged to pull the latest master from github and use that instead. It tends to be pretty stable, and is certainly less buggy than 1.7.

-------------------------

8Xt835nbsWscUMc | 2020-10-12 16:51:00 UTC | #8

I understand. Thanks for insisting on fetching from master branch. I will do it

-------------------------

Modanung | 2020-10-13 09:30:42 UTC | #9

Indeed 1.7 is Uralic. :wink:

-------------------------

