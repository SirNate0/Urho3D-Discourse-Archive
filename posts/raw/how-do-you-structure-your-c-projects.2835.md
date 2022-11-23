smellymumbler | 2017-03-01 18:47:50 UTC | #1

So far, i've been toying around with Lua scripts and the Urho3D player, in order to understand the engine and learn from the docs and examples. However, i'm now planning to start working on the actual project, but i'm not sure how to start. After asking a similar question on GitHub and getting a not-so-friendly answer, i decided to post here and hear from actual users of the engine:

* Is there a sample CMakeLists.txt file for new Urho3D-based projects?
* Do you link Urho3D statically? 
* Where do you keep your assets? What about shaders?

-------------------------

1vanK | 2017-03-01 18:57:33 UTC | #2

https://github.com/1vanK/PuddleSimulator/tree/master/GameSrc

-------------------------

Eugene | 2017-03-01 19:11:03 UTC | #3

What's wrong with my answer? It was as brief as possible: 1) docs have example CMake project of using Urho, 2) it is by-default linked statically, and 3) I keep my assets in configured resource folders (I am sure that you do know this, so it'd be better to ask something more concrete).

-------------------------

hdunderscore | 2017-03-01 19:59:08 UTC | #4

This page in the docs goes into detail on how to set up your c++ projects:
https://urho3d.github.io/documentation/HEAD/_using_library.html

It goes into good detail and offers some options, try follow this and let us know if you run into a problem.

-------------------------

smellymumbler | 2017-03-02 17:52:20 UTC | #5

I keep getting errors like this: CMake can not determine linker language for target: SampleProject.

    project(SampleProject)
    set(TARGET_NAME SampleProject)
    set(CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/cmake/modules)

    if(MSVC)
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /W4")
    else()
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Wpedantic -std=c++11")
    endif()

    # Set CMake minimum version and CMake policy required by Urho3D-CMake-common module
    if(WIN32)
        cmake_minimum_required (VERSION 3.2.3)
    else()
        cmake_minimum_required (VERSION 2.8.6)
    endif()

    if(COMMAND cmake_policy)
        cmake_policy(SET CMP0003 NEW)

        if(CMAKE_VERSION VERSION_GREATER 2.8.12 OR CMAKE_VERSION VERSION_EQUAL 2.8.12)
            cmake_policy (SET CMP0022 NEW)
        endif()

        if(CMAKE_VERSION VERSION_GREATER 3.0.0 OR CMAKE_VERSION VERSION_EQUAL 3.0.0)
            cmake_policy (SET CMP0026 OLD)
            cmake_policy (SET CMP0042 NEW)
        endif()
    endif()

    include(Urho3D-CMake-common)

    file(GLOB_RECURSE PROJECT_SOURCES src/**/*.cpp)
    file(GLOB_RECURSE PROJECT_HEADERS include/**/*.h)
    set(SOURCE_FILES ${PROJECT_SOURCES} ${PROJECT_HEADERS})

    setup_main_executable()

-------------------------

Eugene | 2017-03-02 18:54:00 UTC | #6

Do you have any source files in `PROJECT_SOURCES`?
Try to print & check it.

-------------------------

smellymumbler | 2017-03-02 20:03:53 UTC | #7

I do. I ended up giving up on GLOB_RECURSE and decided to specify the files manually.

-------------------------

Eugene | 2017-03-02 20:17:16 UTC | #8

That's strange... You got strange CMake problem and getting rid of GLOB was strange solution.

-------------------------

suncaller | 2017-03-16 21:10:43 UTC | #9

It's not really a strange CMake error, just ambiguous as to what the cause might be. To me it suggests a few possibilities, most likely of which are 1) not having CMakeLists.txt in all relevant sub-directories and 2) one or more relative addresses are incorrectly specified. However, manually specifying files in CMake is a valid and in many cases superior approach, and if it's working for you, I would stick with it until a point at which it no longer works for you, and reconsider it then.

If you're looking for examples of good project structure for C++ projects and Urho projects in particular, I would suggest looking at the Urho3D source code itself. At its core it's a viable solution to this problem, even if I don't agree with it entirely myself (for mostly personal/aesthetic reasons).

To answer your original question, I make significant, application specific changes to the engine core, and so have forked the engine and add new demos/project code directly in the Samples folder. I would not recommend this to others for obvious reasons.

-------------------------

