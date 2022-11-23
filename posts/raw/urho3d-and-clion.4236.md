MaClay | 2018-05-18 00:22:36 UTC | #1

Hello.

I am newbie of Urho3D and I'm extremely inspired by their features.
And I see that it compatible with CLion (JetBrains IDE for C++).

![image|617x60](upload://A0IhxwYa05OqzHQyuR6ty2GC8VK.png)

So I wonder if there are any examples of how to set up my first project with that? I already compiled engine by VS++ but prefer to use CLion if it's possible.

Or maybe somebody could write a little step-by-step guide...

Thanks a lot.

Best regards,
Mike.

-------------------------

weitjong | 2018-05-18 13:50:59 UTC | #2

I only use CLion on my Linux host machine but I think it is similar there on Windows. Unlike Xcode or Visual Studio, CLion is only an IDE which depends on compiler toolchain(s) to be installed on the  host. It does come with its own CMake, debugger, code inspector, and other tools though. So, I believe the only prerequisite to setup is to install a version of MinGW compiler toolchain alongside. And for that you can follow any setup instruction for MinGW that you can find. However, if you are using CLion 2018 on Windows 10 with WSL then you are in luck. Although I have never tried it myself but this latest version supports the compiler toolchain installed in the WSL. If you have native GCC on WSL then it builds for Linux target. If you have cross-compiler toolchain then it can target other platforms as well, like Windows with MinGW. It is only one apt-get away to install.

According to their blog the latest CLion also supports MSVC compiler now, but why go there since we have so many choices with GCC and Clang (native/cross) compilers already.

As for the project setup, it is the same. The new project scaffolding is IDE-agnostic, with the exception for Android at the moment. Read the existing Urho online doc.

-------------------------

MaClay | 2018-05-18 18:28:07 UTC | #3

Thanks for your reply, its very helpful. 

So I have to compile the engine by IDE anyway, right?

-------------------------

weitjong | 2018-05-19 00:45:43 UTC | #4

Yes, you have to build the engine from source to a same target platform using the chosen compiler toolchain you plan to use for your own project.

-------------------------

VaniaK | 2018-05-22 05:19:50 UTC | #5

# main CMakeFile.txt   
 cmake_minimum_required (VERSION 3.2.3)
    if (COMMAND cmake_policy)
        # Libraries linked via full path no longer produce linker search paths
        cmake_policy (SET CMP0003 NEW)
        # INTERFACE_LINK_LIBRARIES defines the link interface
        cmake_policy (SET CMP0022 NEW)
        # Disallow use of the LOCATION target property - so we set to OLD as we still need it
        cmake_policy (SET CMP0026 OLD)
        # MACOSX_RPATH is enabled by default
        cmake_policy (SET CMP0042 NEW)
        # Honor the visibility properties for SHARED target types only
        cmake_policy (SET CMP0063 OLD)
    endif ()

    project(game)

    set(TARGET_NAME ${PROJECT_NAME})

    set(CMAKE_CXX_STANDARD 11)

    #set(URHO3D_HOME "E:/Urho3D_pro-x64/") # windows
    set(URHO3D_HOME Urho3D-lib) # linux

    # Set CMake modules search path
    set (CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/CMake/Modules/)

    include(UrhoCommon)

    set(SOURCE_FILES ${SOURCE_FILES} main.cpp)


    subdirs(GameCore) # GameCore
    subdirs(EditorCore)

    set(LIBS ${LIBS} EditorCore GameCore)

    setup_main_executable()

-------------------------

VaniaK | 2018-05-22 05:22:27 UTC | #6

# Test subproject CMakeLists.txt
    project(EditorCore)

    set(CMAKE_CXX_STANDARD 11)

    set(HEADERS
            GameObjectBuilder/AssimpModel.h
            GameObjectBuilder/GameObjectBuilder.h
            MapEditor.h
            )

    set(SOURCES

            GameObjectBuilder/AssimpModel.cpp
            GameObjectBuilder/GameObjectBuilder.cpp
            MapEditor.cpp
            )

    subdirs(Assimp)

    set(SOURCE_FILES  ${HEADERS} ${SOURCES})

    add_library(EditorCore STATIC ${SOURCE_FILES}) #SHARED STATIC
    target_link_libraries(EditorCore Assimp)

    target_include_directories(EditorCore PUBLIC ./ ./Terrain ./Assimp/include)

-------------------------

VaniaK | 2018-05-22 05:58:20 UTC | #7

This is compiled on VS and on Linux systems, only problem on windows Path... VS supported CMake Project, you can use without converting, VS do it this automatic
Clion 2017.3.4 most stability compared to latest versions...
MSVC debugging doesn't yet!!!!

-------------------------

LordGolias | 2018-06-24 07:02:44 UTC | #8

I installed CLion (Mac), cloned the project, opened the project in CLion and everything just worked out of the box.

Specifically, CLion automatically created the targets for all the samples and lib, and when pressed to run `01_HelloWorld`, it just compiled and run as expected. Same for all other samples.

Note that by default `URHO3D_DATABASE_SQLITE` is disabled, and thus sample `41_DatabaseDemo` is not shown in the list of targets. This is fixed by going to `cmake-build-debug/CMakeCache.txt` and setting `URHO3D_DATABASE_SQLITE:BOOL=ON`.

-------------------------

nmikros | 2020-11-16 02:49:48 UTC | #9

When you say you just cloned the project, I'm assuming you mean the HelloWorld. Did you build Urho3D library in something else first? Can you build the core in CLion? there's a lot of examples of how to run the .bat file open it in visual studio and build the whole thing but I'm having a hard time wrapping my head around how to build the thing from scratch in CLion, if possible I'd like to do a static build, with all the source in the same project.

-------------------------

