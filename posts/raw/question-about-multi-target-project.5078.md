Azaratur | 2019-04-05 08:04:42 UTC | #1

The target i would like to achieve is to create a multi platform project, but i would like to work with Visual Studio for the development phase.
I build the engine for Vs2015 and for emscripten, and i am now trying to compile my simple project to visual studio.
The engine complain that my Urho home is indeed the emscripten one, so i did change the home and build the project.
Everything works good.

Did i have to change Uhro home everytime i need to create a project?
Is this the correct approach? Or did i miss some steps?

Thank you.

-------------------------

Leith | 2019-04-05 08:53:39 UTC | #2

multi platform target? this means multiple build environments, yes generally this means more projects, at worst, one for each build target. But your source code does not change, well never a lot, just the requirements and settings for the various targets.
I've built across multiple targets and it's always been somewhat of a pain - but it can be done, some game engines actively support this concept more than others... mostly because they are commercial, and well-funded.

-------------------------

Azaratur | 2019-04-05 08:53:22 UTC | #3

I am not worried about that, i was just asking if this is the correct way to handle this.

-------------------------

Leith | 2019-04-05 08:54:28 UTC | #4

Generally, and without specific knowledge of your preferred IDE or build platform, yes this is the right way for targetting multiple platforms.

-------------------------

Leith | 2019-04-05 08:55:19 UTC | #5

this is usually where things like cmake come in - cmake can wrap your project code for a given target platform, sometimes.

-------------------------

johnnycable | 2019-04-05 15:15:55 UTC | #6

my base app tree:

    (3.5.3_Default) max:myApp tree -L 5
    .
    ├── CMake -> /usr/local/Urho/Urho3D/CMake
    ├── CMakeLists.txt -> /Users/max/Developer/Setup/urho/playground/my1.7/CMakeLists.txt
    ├── bin
    │   ├── CoreData -> /usr/local/Urho/Urho3D/bin/CoreData
    │   ├── Data -> /usr/local/Urho/Urho3D/bin/Data
    │   └── GameData
    │       ├── Scenes
    │       │   └── BaseThreeLights.xml
    │       ├── UI
    │       │   └── UIWindowAndButton.xml
    │       └── dummy.txt
    ├── build
    │   ├── android
    │   │   ├── app
    │   │   │   ├── CMakeLists.txt
    │   │   │   ├── LIBRARIES.txt
    │   │   │   ├── SOURCES.txt
    │   │   │   ├── VARS.txt
    │   │   │   ├── build
    │   │   │   │   ├── generated
    │   │   │   │   ├── intermediates
    │   │   │   │   ├── outputs
    │   │   │   │   └── tmp
    │   │   │   ├── build.gradle
    │   │   │   └── src
    │   │   │       └── main
    │   │   ├── bin
    │   │   │   ├── CoreData -> /Users/max/Developer/Stage/Workspace/Urho/myApp/bin/CoreData
    │   │   │   ├── Data -> /Users/max/Developer/Stage/Workspace/Urho/myApp/bin/Data
    │   │   │   └── GameData -> /Users/max/Developer/Stage/Workspace/Urho/myApp/bin/GameData
    │   │   ├── build
    │   │   │   └── android-profile
    │   │   │       ├── profile-2018-12-17-19-15-13-678.json
    │   │   │       └── profile-2018-12-17-19-15-13-678.rawproto
    │   │   ├── build.gradle
    │   │   ├── gradle
    │   │   │   └── wrapper
    │   │   │       ├── gradle-wrapper.jar
    │   │   │       └── gradle-wrapper.properties
    │   │   ├── gradle.properties
    │   │   ├── gradlew
    │   │   ├── gradlew.bat
    │   │   ├── local.properties
    │   │   └── settings.gradle
    │   └── emscripten
    │       └── Debug
    │           ├── CMakeCache.txt
    │           ├── CMakeFiles
    │           │   ├── 3.14.0
    │           │   ├── CMakeDirectoryInformation.cmake
    │           │   ├── CMakeOutput.log
    │           │   ├── CMakeRelink.dir
    │           │   ├── CMakeRuleHashes.txt
    │           │   ├── CMakeTmp
    │           │   ├── Makefile.cmake
    │           │   ├── Makefile2
    │           │   ├── RESOURCE_CHECK.dir
    │           │   ├── TargetDirectories.txt
    │           │   ├── cmake.check_cache
    │           │   ├── myApp.dir
    │           │   └── progress.marks
    │           ├── CTestTestfile.cmake
    │           ├── Makefile
    │           ├── Source
    │           │   └── shell.html
    │           ├── bin
    │           │   ├── CoreData -> /Users/max/Developer/Stage/Workspace/Urho/myApp/bin/CoreData
    │           │   ├── CoreData.pak
    │           │   ├── Data -> /Users/max/Developer/Stage/Workspace/Urho/myApp/bin/Data
    │           │   ├── Data.pak
    │           │   ├── GameData -> /Users/max/Developer/Stage/Workspace/Urho/myApp/bin/GameData
    │           │   ├── GameData.pak
    │           │   ├── myApp.data
    │           │   ├── myApp.html
    │           │   ├── myApp.html.map
    │           │   └── myApp.js
    │           ├── cmake_install.cmake
    │           └── compile_commands.json
    ├── cmake_clean.sh -> /usr/local/Urho/Urho3D/cmake_clean.sh
    ├── cmake_emscripten.sh -> /usr/local/Urho/Urho3D/cmake_emscripten.sh
    ├── cmake_generic.sh -> /usr/local/Urho/Urho3D/cmake_generic.sh
    ├── setup
    └── src
        ├── MyApp.cpp
        ├── MyApp.h
        ├── Sample.h
        └── Sample.inl

    40 directories, 47 files
    (3.5.3_Default) max:myApp 

one source, mutiple builds per system

I use an ad-hoc bash scripting system, but you can use the default [scaffolding system](https://urho3d.github.io/documentation/HEAD/_using_library.html) with rake for generating quick project setup...

-------------------------

