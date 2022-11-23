vmost | 2021-01-18 13:15:49 UTC | #1

Here is some information on getting started with building and using Urho3D for Mac OSX users running 10.11 El Capitan.

1. When trying to build Urho3D I ran into a bug with one of the dependencies. Apply [this patch](https://gist.githubusercontent.com/illume/ac2eb4daa1bd805255d5355806acf822/raw/7e3c83f760fe5bf61a9f6bcc196ed9be6f6e22da/sdl2-mac-10-11.patch) to fix [this issue](https://discourse.libsdl.org/t/sdl-2-0-10-old-mac-os-el-capitan-10-11-and-xcode7-3/26554/11) in file Urho3D/Source/ThirdParty/SDL/src/video/cocoa/SDL_cocoavideo.h. It should look like
```
/* Fix build with the 10.10 SDK */
#if MAC_OS_X_VERSION_MAX_ALLOWED < 101100
#define NSEventSubtypeTouch NSTouchEventSubtype
#endif
/* Fix build with the 10.11 SDK */
#if MAC_OS_X_VERSION_MAX_ALLOWED < 101200
#define NSEventSubtypeMouseEvent NSMouseEventSubtype
#endif
```
2. When building, I found that the precompiled header isn't supported. See [this thread](https://discourse.urho3d.io/t/build-failed-in-mac-osx-no-suitable-precompiled-header/3794) (it's a common problem for Mac users). Go into CMakeCache.txt and set "URHO3D_PCH:BOOL=OFF", or pass `-DURHO3D_PCH=OFF` to cmake when building the library.
3. Move the Urho3D folder to a location where it can live for the rest of its life. I have a folder called 'Libs'.
4. Whenever you make a new project that will pull in the built Urho3D as a library (e.g. by adapting [this](https://github.com/ArnisLielturks/Urho3D-Project-Template) or following [this tutorial](https://www.youtube.com/playlist?list=PL9AoJQ0JIIKpOI4p_W02C9wRGIYB3n1RM)) you have to add the library's location to the 'URHO3D_HOME' environment variable. I went to my sample project's CMakeCache.txt and set 'URHO3D_HOME:PATH=/Users/vmost/Libs/Urho3D'. A more reliable way is to add `export URHO3D_HOME=~/Libs/Urho3D` to your `cmake_etc.sh` script file, or bake it into your CMakeLists.txt file with `set (ENV{URHO3D_HOME} "~/Libs/Urho3D")`.
5. When I built my sample project for a little 'hello world', the console spit out a bunch of garbage, which you can silence with [this patch](https://github.com/Microsoft/vcpkg/issues/4497). Dive into the sample project's CMakeLists.txt file and add these lines:
```
set(other_flags "${other_flags} -frtti -fvisibility-inlines-hidden")
set(other_flags "${other_flags} -fvisibility=hidden")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -stdlib=libc++ ${other_flags}")
```

With those issues out of the way, here is how to actually build the library (you need git and cmake installed, which can be done with homebrew).
1. `git clone https://github.com/urho3d/Urho3D`
2. `cd Urho3D`
3. `cmake .`
4. `make`
5. oh, it's done (after 30mins and assuming nothing else crops up); in Urho3D/bin are a bunch of samples that have been automatically built. You can also use the 'Urho3DPlayer' found in that same folder to run a script. It can run any of the samples
a. `cd Urho3D/bin`
b. `./Urho3DPlayer Scripts/sample_name.as [options]`
c. example option (see [the docs](https://urho3d.github.io/documentation/1.7/_running.html)): `-v` turns on vertical sync, which is [interesting](https://www.digitaltrends.com/computing/what-is-vsync/)

And some hints on setting up a sample project. Keep [this page](https://urho3d.github.io/documentation/1.7.1/index.html) in mind, as it has a lot of information!
1. [This tutorial](https://www.youtube.com/watch?v=B8fhIqGFyEU&list=PL9AoJQ0JIIKpOI4p_W02C9wRGIYB3n1RM&index=2) is a good starting spot. 
2. Rather than try and put together everything from scratch, it's best to just copy several things and run the cmake script to do the rest of the work. Here are the essential parts of an infant project.
a. Folder: bin; contains [CoreData] and [Data] folders (can copy them out of Urho3D/bin)
b. Folder: CMake; contains [Modules] and [Toolchains] folders (can copy Urho3D/CMake folder directly)
c. Folder: script; contains [cmake_generic.sh] (can copy out of Urho3D/script), and [cmake_projectname.sh] which contains the line `$(dirname $0)/cmake_generic.sh`. Use the second one for adding stuff instead of editing the generic script.
d. Folder: Source; put C++ source files in here (code files, header files, etc). Need at least one file e.g. 'app_main.cpp' which creates an Application derived class and calls `URHO3D_DEFINE_APPLICATION_MAIN(MyApp)`
e. File: CMakeLists.txt; paste in the stuff from [this link](https://urho3d.github.io/documentation/1.7.1/_using_library.html). Have to change 'project name' and 'target name', and add these lines since I prefer putting source files in their own folder:
```
# Define source files
file (GLOB SRC_CPP_FILES Source/*.cpp)
file (GLOB SRC_H_FILES Source/*.h)
define_source_files (GROUP EXTRA_CPP_FILES ${SRC_CPP_FILES} EXTRA_H_FILES ${SRC_H_FILES})
```
3. The happy moment is when you hit `script/cmake_projectname.sh ./` and `make`, and then your executable shows up in `project_folder/bin`.

note: There are so many things to learn here, I hope these resources are helpful pointers.

Anyway, that's the first step on this journey.

-------------------------

Modanung | 2020-08-09 04:53:52 UTC | #2

A few months back I managed to compile and run the engine on an (~15 year) old machine - my first laptop - after enabling "stub ARB_occlusion_query support on 915/945" in `driconf` and reducing the minimum required CMake version, which also required the following modification:
``` diff
- source_group (TREE ${CMAKE_CURRENT_SOURCE_DIR} PREFIX "Source Files" FILES ${SOURCE_FILES})
+ source_group ("Source Files" FILES ${CMAKE_CURRENT_SOURCE_DIR}/${SOURCE_FILES})
```

![](https://www.notebookcheck.net/uploads/tx_nbc2/illus_medionakoyae1210.jpg)

Spec | Value
---|---
Manufacturer | Medion
Model name | Akoya Mini
Model id |	E1210
CPU | Intel Atom (Diamondville)
CPU speed | 1600 Mhz
Graphics | Intel 945GME
OS | Linux Mint 
Display Size | 10.2" 1024x600
RAM | 1024 MB
Hard Disk | 160 GB
Weight | 1191 g
Size | 259x180x31.0 mm

Using a bluetooth dongle it even supports wireless PS3 controllers. :slightly_smiling_face:

Obviously there's features it does not like at all; shadows, normal maps and many lights make it hog.

-------------------------

