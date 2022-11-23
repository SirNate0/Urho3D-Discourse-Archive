lesun90 | 2017-01-02 01:15:43 UTC | #1

Hi,
I have an existing project with some libraries,I coding in Ubuntu, and using CMake to build my program. Now I want to add urho3d as an external library to add 3D feature for my project, but I dont know how to config my CMakeLists file to make urho3d work with my project. 
This is what I did:
- complied and installed  Urho3d into my system. (I follow the tutorial  in wiki page "Setting-up-a-Project-(CMake)" and it worked so I am sure Urho3d is working now on my pc)
- Copy CMake folder in Urho3D folder into my project folder.
- Create a bin folder with a CoreData and a Data folder inside in my project directory.
- add the following line into my CMakeLists.txt file
[code]
# Set CMake modules search path
set (CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/CMake/Modules)
# Include Urho3D Cmake common module
include (Urho3D-CMake-common)
[/code]

cmake run with no problem but it had error when I try to "make" a test3D.cpp file
[code]
Test3D.cpp:(.text.startup+0x1f): undefined reference to `Urho3D::EventNameRegistrar::RegisterEventName(char const*)'
Test3D.cpp:(.text.startup+0x2e): undefined reference to `Urho3D::StringHash::StringHash(char const*)'
Test3D.cpp:(.text.startup+0x3d): undefined reference to `Urho3D::StringHash::StringHash(char const*)'
Test3D.cpp:(.text.startup+0x4c): undefined reference to `Urho3D::EventNameRegistrar::RegisterEventName(char const*)'
Test3D.cpp:(.text.startup+0x5b): undefined reference to `Urho3D::StringHash::StringHash(char const*)'
Test3D.cpp:(.text.startup+0x6a): undefined reference to `Urho3D::EventNameRegistrar::RegisterEventName(char const*)'
Test3D.cpp:(.text.startup+0x79): undefined reference to `Urho3D::StringHash::StringHash(char const*)'
Test3D.cpp:(.text.startup+0x88): undefined reference to `Urho3D::EventNameRegistrar::RegisterEventName(char const*)'
Test3D.cpp:(.text.startup+0x97): undefined reference to `Urho3D::StringHash::StringHash(char const*)'
Test3D.cpp:(.text.startup+0xa6): undefined reference to `Urho3D::EventNameRegistrar::RegisterEventName(char const*)'
Test3D.cpp:(.text.startup+0xb5): undefined reference to `Urho3D::StringHash::StringHash(char const*)'
Test3D.cpp:(.text.startup+0xc4): undefined reference to `Urho3D::EventNameRegistrar::RegisterEventName(char const*)'
collect2: error: ld returned 1 exit status
[/code]

my test3d.cpp file
[code]
// my first program in C++
#include <string>
#include <sstream>

#include <Urho3D/Core/CoreEvents.h>

// using namespace Urho3D;

int test(int argc, char **argv)
{
  printf("hehehehehe\n" );
  return 0;
}

[/code]

Sorry if this is a stupid question, I am new both with urho3d and CMake.
Thank you.

-------------------------

Eugene | 2017-01-02 01:15:44 UTC | #2

Have you read an article at urho3d.github.io about using urho3d with an existing project?

-------------------------

lesun90 | 2017-01-02 01:15:44 UTC | #3

yes, I follow the tutorial in wiki page "Setting-up-a-Project-(CMake)" and it worked so I am sure Urho3d is working now on my pc.

-------------------------

Victor | 2017-01-02 01:15:44 UTC | #4

Here's my current setup. I'm using CLion and MinGW64 6.2 (posix) as the compiler. [b]Disclaimer:[/b] I'm no CMake expert so there may be problems...

This setup is useful if you're compiling your game as a DLL and you've created a launcher.exe to launch your game or custom editor, which is what I'm doing. However, I think it's useful to know how to separate out your CMake stuff with Urho's methods.
[code]
# Set the URHO3D_HOME variable manually
set(URHO3DSDK_HOME "C:/Urho3DSDK")
set(URHO3D_HOME "${URHO3DSDK_HOME}" CACHE STRING "Urho3D SDK" FORCE)

# Append my game includes with the URHO3D includes
list(APPEND MYGAME_INCLUDES
        ${URHO3D_INCLUDE_DIRS}
)

# Include whatever files you want to use throughout your project
# ...

# Set the include directories.
include_directories(${MYGAME_INCLUDES})

# Include Urho3D Cmake common module
include (Urho3D-CMake-common)

# Find Urho3D library
find_package (Urho3D REQUIRED)

# Add the Urho3D Library (based on debug/release mode)
add_library(Urho3DLib STATIC IMPORTED)
if (CMAKE_BUILD_TYPE MATCHES Debug)
    set_property(TARGET Urho3DLib PROPERTY IMPORTED_LOCATION ${URHO3DSDK_HOME}/lib/libUrho3D_d.a)
else ()
    set_property(TARGET Urho3DLib PROPERTY IMPORTED_LOCATION ${URHO3DSDK_HOME}/lib/libUrho3D.a)
endif ()
[/code]

In my case, I'm forced to used static linking, because if you're doing a Game.dll file, CMake (or I haven't found out at least), doesn't allow a target dll to import another dll... which is sad/annoying. :frowning:
Now, when building your exe, you can do the following:

[code]
project(MyGame)

# Header and src files.
file (GLOB MYGAME_HEADERS
        "${CMAKE_CURRENT_SOURCE_DIR}/mygame-headers/*.h"
)

file (GLOB MYGAME_SRC
        "${CMAKE_CURRENT_SOURCE_DIR}/mygame-sources/*.cpp"
)

# For Mac support I do the following... (I've had to do this after updating to the latest xcode version)
list (APPEND AppleLibs "")
if (APPLE)
    list (APPEND AppleLibs "-framework AudioToolbox" "-framework CoreAudio" "-framework CoreGraphics" "-framework Foundation" "-framework GameController" "-framework QuartzCore")
endif ()

add_executable(MyGame ${MYGAME_HEADERS} ${MYGAME_SOURCES})

# Now add our dependencies.
define_dependency_libs (Urho3D)
target_link_libraries(
        MyGame
        ${AppleLibs}
        ${ABSOLUTE_PATH_LIBS}
        ${LIBS}
)
[/code]

The [b]ABSOLUTE_PATH_LIBS[/b] and [b]LIBS[/b] come from Urho3D. You'll want to include them so you don't run into any undefined errors when building statically/dynamically.

This is a bit of a drawn out setup the way I have it, but it allows me a bit more flexibility with other libs. I just started working with wxWidgets, which I link as a dll, and it works with Urho perfectly. I hope this helps and good luck!

-------------------------

