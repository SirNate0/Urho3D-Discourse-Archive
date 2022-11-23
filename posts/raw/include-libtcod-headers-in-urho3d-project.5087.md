Lunarovich | 2019-04-13 14:52:06 UTC | #1

Hello! I would like to be able to use a roguelike library https://github.com/libtcod/libtcod with my project. I've installed the lib via **apt-get** on Ubuntu. I've included all the necessary headers in my *Main.cpp* file (in fact, there's only one). I can't get a project compiled. 

I suppose that I need to do something with CMake, which I don't know well. Any suggestions?

-------------------------

Leith | 2019-04-07 04:31:49 UTC | #2

Generally speaking, using third parties libs in any c++ project is "no-problemo"... but setting up new c++ projects for Urho3D, as a new user of Urho3D, can be a little daunting. Also, for each new project, you may need to set up the project build settings all over again. For CodeBlocks, this is true, even if you completely copy an existing project into a new folder.

Building a c++ project happens mostly as two stages - first we try to compile the project sourcecode, which pulls in header files - if that worked, we move on to the second stage, which pulls in any needed existing code library files. 
Any errors in compiling will prevent us reaching the linker stage. 
Any errors in the linker stage are (strictly?) about us forgetting to add the path to some needed lib.

I'd have to see the compiler / linker errors, but the most common issue is that you have not told your project about all the required libs (there's a handful for linux) and all the search paths for included header files.

For Linux:
Step one is to use cmake-gui to generate an Urho3D Build from the master sourcecode.
Step two is to use make to build your Urho3D Build.
Step three is to point your project at the Urho3D lib file (in the Urho3D Build folder), plus a fistful of other needed libs such as pthread.
Step four is to point your project at the Urho3D headers (I use the Urho3D Master folder, I am adverse to symlinks).
Now your project can find all the headers and binaries required.
Happy to help more, but need to see the errors. I use CodeBlocks as my preferred IDE, and gcc as my compiler.

-------------------------

Leith | 2019-04-07 04:24:59 UTC | #3

For CodeBlocks, for my current project, in C++, on Linux.

Using the menu in the title bar, we go to "project/build options/linker settings".
Under "Link Libraries", we add the paths to these core libs.
../URHO_BUILD/lib/libUrho3D.a  <-- edit these paths as required
/lib/x86_64-linux-gnu/libdl-2.27.so
/usr/lib/x86_64-linux-gnu/libGL.so

Over on the right hand side, under "Other linker options", we add these guys:
-pthread
-ldl
-lGL
-lGLU
-lGLEW

Now we click on the Search Directories tab, and add these guys:
../URHO_BUILD/include
../URHO_BUILD/include/Urho3D/ThirdParty
../URHO_MASTER/Urho3D/Source/ThirdParty/Bullet/src
source <-- project folder for included Header (.h) files

Anywhere I wrote <-- is a comment, so strip that stuff out.

The above is not perfect, I've spent zero time on the build stuff, and little time using Urho (in the scheme of things) but it's enough to make everything work for me.

Setting up a new project on a new codebase? Let's call it "teething issues" :) Yeah, it's a pain. But once done, is done for life.
For the record, it took me about two or three days to work out all the dependencies and what I needed to add to my compiler and linker settings, and I may have needed to install something third-party as well.

-------------------------

Leith | 2019-04-07 04:32:57 UTC | #4

We have one guy that works a lot on our build system, but not enough eyes.

-------------------------

Lunarovich | 2019-04-07 07:01:51 UTC | #5

@Leith Thank you for your long and informative answer. To be precise, I don't want to compile Libtcod as a built in third party lib (I mean, like Bullet or FreeType, etc.). I just want to use it with an already set up project. So, I've found a solution in making FindLibtcod.cmake and FindLibtcodxx.cmake modules and by including the following lines in my CMakeLists.txt:

    find_package(Libtcod REQUIRED)
    include_directories(${LIBTCOD_INCLUDE_DIRS})
    set(LIBS ${LIBS} ${LIBTCOD_LIBRARIES})

    find_package(Libtcodxx REQUIRED)
    include_directories(${LIBTCODXX_INCLUDE_DIRS})
    set(LIBS ${LIBS} ${LIBTCODXX_LIBRARIES})

I've kind of copy pasted Cmake module finders from the internet and follow the instructions here https://gitlab.kitware.com/cmake/community/wikis/doc/tutorials/How-To-Find-Libraries

In general, I find *Building Urho3D library* and *Using Urho3D library* especially daunting for the newcomers. What is more, I have an impression that topics are not well separated in the sense that already the first mentioned page (*Building Urho3D library*) is actually talking about build scripts, which are, actually, used not to build Urho3D library, but to create a project based on Urho3D, and that means that the heading **Build scripts** belongs rather to the second page of the documentation (*Using Urho3D library*). Also, I've needed quite few trial and error and search on the internet just to figure out that **Build options** is related to the personal project build options and not to the building of the Urho3D library. 

Anyway, I've got through the initial pain, mostly by looking around on the internet how to set up an initial and barebones project. IMHO, we need to have some official tutorials for the major systems, like Windows 10, Ubuntu and OS X. I know quite well that it's easier said than done and that people are working hard and contributing a lot. Nevertheless, it seems to like a priority. I've found this page https://github.com/urho3d/Urho3D/wiki/Getting-started-in-Linux particularly helpful. Also, this guy provided really nice basic explanations: http://darkdove.proboards.com/thread/30/urho-flow-1

-------------------------

weitjong | 2019-04-07 08:55:30 UTC | #6

The "Building Urho3D library" page describes how to build the library itself. All those build options belongs to Urho3D project. While the "Using Urho3D library" page is only one way to use the library. As the first paragraph says, you can ignore this whole section if you already have your own build system. Just integrate Urho3D library as you would in your app like any other libraries you have tried in the past. However, if you want to **reuse** the build system of the Urho3D project in your own downstream project, only then you need to read that section. Some of the existing build options are then suddenly becomes available for your build, but some are not relevant for downstream project still because  remember those build options really belong to Urho3D project in the first place.

We do not force you to use CMake in your own project. But of course, I personally only provide support for those that use CMake and reuse our Urho3D build system.

-------------------------

Leith | 2019-04-09 09:17:27 UTC | #7

I tend to agree that documentation could improve - this does not mean that existing documentation is bad, but it could be broader, so that corner cases could be talked about in a proper context. I've offered to help with documentation, but I'm still asking "stupid questions" and still "making stuff work" before I feel I can turn my hand to documenting stuff.

-------------------------

