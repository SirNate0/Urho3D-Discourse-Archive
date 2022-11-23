NOCAPS | 2017-01-02 01:07:47 UTC | #1

I've been trying to compile and build a project just using g++ and terminal for everything, and I can't seem to find a way to get it to work. If this is possible, could someone please teach me how to do this?

-------------------------

jmiller | 2017-01-02 01:07:48 UTC | #2

Hello NOCAPS, welcome to the forum :slight_smile: 

In general, I'd recommend working with the 'master' development branch of Urho.
In that case, you will probably want Git: [git-scm.com/](https://git-scm.com/)
more tips: [topic1126.html](http://discourse.urho3d.io/t/how-to-start-with-urho3d/1094/1)
(git clone [github.com/urho3d/Urho3D.git](https://github.com/urho3d/Urho3D.git))

The docs should be helpful; in particular, the Getting Started section, Prerequisites and Build Scripts.
[urho3d.github.io/documentation/HEAD/index.html](http://urho3d.github.io/documentation/HEAD/index.html)

In short, one typically one makes a 'build tree' directory, runs a script (probably Urho3D/cmake-generic.sh, for you) with build options for debug/release/samples/etc. which runs cmake, giving you Makefile stuff in your build tree where you can 'make'.

If you can be a bit more specific as you go, you're sure to have some answers here. Let us know how it's working out.

-------------------------

NOCAPS | 2017-01-02 01:07:48 UTC | #3

So far, I've been using terminal to git clone and pull etc, so I understand git somewhat well. 
I have already run the script cmake-generic.sh into my FirstProject directory, but what I don't understand how to do is create a brand new project and allow the build to read the new cpp files that I create. I'm not entirely sure whether or not I have a 'build tree' directory created, however I have already built into my FirstProject directory using ./cmake-generic.sh $FirstProject in my terminal.

-------------------------

jmiller | 2017-01-02 01:07:48 UTC | #4

So you are generally following
[urho3d.github.io/documentation/H ... brary.html](http://urho3d.github.io/documentation/HEAD/_using_library.html)

Using the Urho build scripts, the build tree(s) for your own project are created and used similarly to Urho's.

I think you need to define your source files for cmake, in your project's CMakeLists.txt.

[code]# One "easy" method - but you will likely have to reinvoke cmake when you add/remove source files.
define_source_files(RECURSE GLOB_CPP_PATTERNS "src/*.cpp" "src/*.cc" GLOB_H_PATTERNS "src/*.h")[/code]

a bit more info on that: [topic893.html](http://discourse.urho3d.io/t/how-do-you-include-source-in-subdirectories/871/1)

Tip 'o' the day, -D URHO3D_LIB_TYPE=SHARED can save a lot of linking time, depending on your setup.

-------------------------

NOCAPS | 2017-01-02 01:07:48 UTC | #5

Alright, well I'm still stuck. I think it's more of because I don't know where to proceed after I've done what I have done, so here's the list of my terminal steps for what I have done so far to make it more clear on where I am. 

$FIRSTPROJECT = directory of FirstProject
$URHO3D_REPOSITORY = directory of Urho3D

mkdir FirstProject
cd FirstProject/
mkdir bin
cd bin
ln -s $URHO3D_REPOSITORY/bin/Data
ln -s $URHO3D_REPOSITORY/bin/CoreData
cd ..
Create CMakeLists.txt with the sample one and change ProjectName and executable name
Create main.cpp
cd $URHO3D_REPOSITORY
./cmake_generic.sh $FIRSTPROJECT
cd $FIRSTPROJECT
make

That's what I've done so far, and I can't find any executable with my executable name. However, I feel as though I'm doing something wrong with my steps.

-------------------------

jmiller | 2017-01-02 01:07:51 UTC | #6

With your project as well as with the library, the scripts expect a build tree and a source tree. They seem to take their own location as the source tree.

Some might choose $PROJECT/build as their build tree.

If things go well, usually binaries are generated in your build/bin, but that can be changed if desired in CMakeLists.txt:
[code]
set_output_directories(${CMAKE_BINARY_DIR}/.. RUNTIME PDB)

#define_source_files...
[/code]

HTH?

-------------------------

jmiller | 2017-01-02 01:07:54 UTC | #7

Any luck?
cmake can be one of the confusing things when initially setting up Urho, although much work has been done to make it as painless as possible on so many configurations.
Once you're over the initial bump, it should be much smoother sailing - and maybe even enjoyable!

There are also plenty of helpful folks at our very own [b]#Urho3D[/b] chat channel, so feel free to join the party.
[webchat.freenode.net/](https://webchat.freenode.net/)

-------------------------

