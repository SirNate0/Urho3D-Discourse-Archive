arrowhart | 2017-01-02 01:09:55 UTC | #1

Hello, I am just getting into Urho3D and am tring to set up the engine. I am building Urho3D on a Linux OS (Debian 32-bit). I have been following along with the documentation and the tutorial on the Urho3D wiki regarding what I need to have installed in terms of dependencies. I am encountering an issue when I try to build using cmake_generic.sh with -DURHO3D_SAMPLES=1. I am able to successfully run the following:
[code]$ cd $URHO3D_REPOSITORY
$ ./cmake_generic.sh $URHO3D_HOME [variable list][/code]
But the next step is where it falls apart. After changing to $URHO3D_HOME and running make, the build compilation continues until about 50%. This result appears as follows:
[code]
Scanning dependencies of target Urho3D
[ 52%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/Addons.cpp.o
In file included from /media/sf_lwshare/Urho3D-1.5/Source/Urho3D/AngelScript/Addons.cpp:25:0:
/media/sf_lwshare/Urho3D-1.5/Source/Urho3D/AngelScript/../AngelScript/Addons.h:34:37: fatal error: AngelScript/angelscript.h: No such file or directory
 #include <AngelScript/angelscript.h>
                                     ^
compilation terminated.
Source/Urho3D/CMakeFiles/Urho3D.dir/build.make:373: recipe for target 'Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/Addons.cpp.o' failed
make[2]: *** [Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/Addons.cpp.o] Error 1
CMakeFiles/Makefile2:1306: recipe for target 'Source/Urho3D/CMakeFiles/Urho3D.dir/all' failed
make[1]: *** [Source/Urho3D/CMakeFiles/Urho3D.dir/all] Error 2
Makefile:137: recipe for target 'all' failed
make: *** [all] Error 2[/code]

After navigating through the source code, it appears there is no "angelscript.h" in the AngelScript directory. I tried once more, building with URHO3D_ANGELSCRIPT set to 1, but the documentation says this should be so by default.

To clarify, I made sure to install all the dependencies I did not have that were described at the beginning of the tutorial. I have also tried the information provided in the[b] Urho3D Install Tips and Tricks[/b], although to no avail. My best guess is that I am not installing the proper dependencies for 32-bit?

-------------------------

rasteron | 2017-01-02 01:09:55 UTC | #2

Hey arrowhart,

Welcome to the forums :slight_smile: Yes, pretty much the same in all platforms with CMake scripts and Angelscript is indeed enabled by default.

Just invoke this: [b]./cmake_generic.sh ./build[/b] where 'build' is your makefile and binaries directory.

[b]Edit:[/b] As for the Samples build option, I think this is also enabled by default for some reason, which is weird and some sort of a small issue going on, at least with my recent builds.

[img]http://i.imgur.com/7EF1secl.png[/img]

Just did this one earlier in my ubuntu 14.04 32bit using vbox.

-------------------------

