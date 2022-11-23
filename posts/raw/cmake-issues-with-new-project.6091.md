lebrewer | 2020-04-15 19:10:20 UTC | #1

Hey guys! I'm getting the following error with my setup:

    CMake Error at vendor/engine/CMakeLists.txt:45 (include):
      include could not find load file:

        UrhoCommon


    CMake Error: Error processing file: /home/foo/MyProject/CMake/Modules/GetUrhoRevision.cmake
    CMake Error at vendor/engine/CMakeLists.txt:86 (string):
      string sub-command REGEX, mode MATCH needs at least 5 arguments total to
      command.


    CMake Error at /usr/share/cmake-3.17/Modules/CPack.cmake:561 (message):
      CPack license resource file: "/home/foo/MyProject/LICENSE" could not be found.
    Call Stack (most recent call first):
      /usr/share/cmake-3.17/Modules/CPack.cmake:566 (cpack_check_file_exists)
      vendor/engine/CMakeLists.txt:167 (include)


    CMake Error at vendor/engine/Source/ThirdParty/ETCPACK/CMakeLists.txt:30 (setup_library):
      Unknown CMake command "setup_library".

Here's how my CMake looks like:

    cmake_minimum_required(VERSION 3.8)
    project(MyProject VERSION 0.1.0)

    set(CMAKE_INCLUDE_CURRENT_DIR ON)
    set(CMAKE_CXX_STANDARD 17)
    list(APPEND CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/cmake")
    set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${PROJECT_SOURCE_DIR}/bin")

    set(SOURCE_DIR ${CMAKE_CURRENT_LIST_DIR}/src)
    set(VENDOR_DIR ${CMAKE_CURRENT_LIST_DIR}/vendor)
    set(PROJECT_INCLUDE_DIRS)
    set(PROJECT_LINK_DIRS)

    set(PROJECT_SOURCES ${SOURCE_DIR}/main.cpp)

    list(APPEND CMAKE_MODULE_PATH "${VENDOR_DIR}/engine/CMake/Modules")
    add_subdirectory(${VENDOR_DIR}/engine)

    add_executable(${PROJECT_NAME} ${PROJECT_SOURCES})
    target_link_libraries(${PROJECT_NAME} Urho3D)

I've added Urho as a git submodule, following the ideas of this repo: https://github.com/Polytonic/Glitter

-------------------------

dertom | 2020-04-15 22:46:58 UTC | #2

I guess the problem is CMakeList.txt:42

If you want to embed urho3d like that (not sure that is the best choice) you need to change 'cmake_source_dir' to 'cmake_current_source_dir'. That should at least set the modules path right....good luck ;)

https://github.com/urho3d/Urho3D/blob/master/CMakeLists.txt#L42

-------------------------

Eugene | 2020-04-15 23:11:24 UTC | #3

Current Urho build system is not designed to be used as submodule.
There was PR that tried to bring this functionality, but it didn't go anywhere.

-------------------------

lebrewer | 2020-04-16 04:16:45 UTC | #4

This one? https://github.com/urho3d/Urho3D/pull/1474

-------------------------

WangKai | 2020-04-16 04:21:06 UTC | #5

I think you just need to copy/symlink CMake folder into your project folder. 

My project structure can work for CMake on Windows. Hope it helps - https://github.com/SuperWangKai/Urho3DCMakeTest

Meanwhile, I have figured out how to handle on Android in a clean way, I will finish it when I have some weekend time.

-------------------------

weitjong | 2020-04-16 09:45:24 UTC | #6

At the moment the test proven way of using Urho3D library is by using it as an external library. That is, the library is built first before your app(s). You are on your own for other kind use cases.

-------------------------

lebrewer | 2020-04-16 16:55:41 UTC | #7

@rku do you still have this somewhere? https://github.com/r-ku/Urho3D/tree/cmake-add-subdirectory

-------------------------

rku | 2020-04-16 17:00:42 UTC | #8

This was saved in https://github.com/urho3d/Urho3D/tree/rokups-add_subdirectory
Or if you feel adventurous and you want a modern build system without hacks you may try ripping out [rbfx](https://github.com/rokups/rbfx) build system and adapting it to urho3d. It should not be that much of work. Definitely less work than rewriting it once again.

-------------------------

