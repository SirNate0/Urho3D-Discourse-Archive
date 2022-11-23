teren4m | 2018-02-25 02:37:41 UTC | #1

Cannot compile for linux https://github.com/urho3d/Urho3D/wiki/First-Project

/usr/local/include/Urho3D/Input/InputEvents.h:28:36: fatal error: SDL/SDL_gamecontroller.h: No such file or directory
 #include <SDL/SDL_gamecontroller.h>

-------------------------

weitjong | 2018-02-25 02:32:34 UTC | #2

Welcome to our forums. The problem should be on the way you have generated your build tree. Did you use our common build system?

-------------------------

teren4m | 2018-02-25 07:43:55 UTC | #3

Is there some sample for it?

-------------------------

weitjong | 2018-02-25 09:55:57 UTC | #4

Read the online doc if you haven’t done so. 

https://urho3d.github.io/documentation/HEAD/_using_library.html

-------------------------

teren4m | 2018-02-25 11:42:58 UTC | #5

This is tutorial is not friendly. Is there some sample on github?

-------------------------

weitjong | 2018-02-25 13:23:05 UTC | #6

Yes, the link I provided is not a tutorial per se. Other is probably able to help you with what you are looking for.

-------------------------

Eugene | 2018-02-25 17:03:29 UTC | #7

[quote="teren4m, post:5, topic:4046, full:true"]
This is tutorial is not friendly. Is there some sample on github?
[/quote]

Do you mean sample of using Urho as library?
I always copy-pasted CMake project from the page above, set Urho home and generated new project.
I am win user tho.

-------------------------

Sean221 | 2018-02-27 01:33:31 UTC | #8

what method do you use to set URHO3D_HOME? 

I cant figure out how to set it using cmake with the command line?

-------------------------

Eugene | 2018-02-27 09:37:24 UTC | #9

Well, usually I put my project near the Urho things and do something like this:
`set (URHO3D_HOME ${CMAKE_SOURCE_DIR}/../Urho3D)`
Linux may have different paths.

-------------------------

weitjong | 2018-02-27 10:31:11 UTC | #10

You can set it externally as build option like the rest or set it as host environment variable. Once the value is cached in the build tree then you don’t need to set it again when doing CMake rerun or when building.

-------------------------

teren4m | 2018-03-04 20:13:15 UTC | #11

This is my CMakeList:

# Define target name
cmake_minimum_required(VERSION 3.5)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set (TARGET_NAME TestProject)
set (URHO3D_HOME ${CMAKE_SOURCE_DIR}/../Urho3D)

add_executable(TestProject main.cpp)

target_link_libraries(TestProject ${URHO3D_HOME}/lib/libUrho3D.a )
target_include_directories(TestProject PRIVATE ${URHO3D_HOME}/include/ ${URHO3D_HOME}/include/Urho3D/ThirdParty/ )

Now I have problem with:
../Urho3D/lib/libUrho3D.a(OGLTextureCube.cpp.o): In function `Urho3D::TextureCube::Release()':
OGLTextureCube.cpp:(.text+0x1ed): undefined reference to `glDeleteTextures'

-------------------------

