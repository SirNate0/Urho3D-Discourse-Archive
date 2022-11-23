ibatrakov | 2017-02-05 00:17:42 UTC | #1


include < SDL/SDL_rwops.h > from file
/Urho3D/include/Urho3D/IO/RWOpsWrapper.h
does not exist with path /Urho3D/Source/ThirdParty/SDL/include

linux has
/usr/include/SDL2/SDL_rwops.h

needed to setup right path, not  < SDL/SDL_rwops.h >

SDL2 and SDL different packages

should write
include < SDL/include/SDL_rwops.h >

or 
include < SDL2/SDL_rwops.h >

or setting by right include path
include < SDL_rwops.h >

-------------------------

weitjong | 2017-02-04 02:41:53 UTC | #2

Something was wrong with your symlinks in the generated build tree. Probably you should regenerate the build tree again from scratch.

All headers from our third-party libs are being setup to be "SDK-like", i.e. as if the libs have been locally installed so their headers can be included using the same general angle brackets format:

    <3rd-party-lib-name/header-name>

For SDL, we have setup the symlink pointing to SDL headers to be prefixed with "SDL", although we could have named it anything we like. So, ```<SDL/SDL_rwops.h>``` in our code is correct. Also, do not confuse them with the headers that you might have outside of the build tree.

-------------------------

ibatrakov | 2017-02-04 21:41:00 UTC | #3

build tree again from scratch did not help

$ pwd
/Urho3D/Source/ThirdParty/SDL

$ ll
total 1528
-rw-rw-r--.  1 m m     504 Feb  4 09:48 BUGS.txt
drwxrwxr-x.  2 m m    4096 Feb  4 09:48 cmake
drwxrwxr-x.  3 m m    4096 Feb  5 04:19 CMakeFiles
-rw-rw-r--.  1 m m    1560 Feb  4 09:48 cmake_install.cmake
-rw-rw-r--.  1 m m   62385 Feb  4 09:48 CMakeLists.txt
-rw-rw-r--.  1 m m     930 Feb  4 09:48 COPYING.txt
-rw-rw-r--.  1 m m    1920 Feb  4 09:48 CREDITS.txt
drwxrwxr-x.  3 m m    4096 Feb  4 09:48 include
-rw-rw-r--.  1 m m    1147 Feb  4 09:48 INSTALL.txt
-rw-rw-r--.  1 m m 1292798 Feb  5 04:21 libSDL.a
-rw-rw-r--.  1 m m  138713 Feb  4 09:48 Makefile
-rw-rw-r--.  1 m m     432 Feb  4 09:48 README-SDL.txt
-rw-rw-r--.  1 m m     647 Feb  4 09:48 README.txt
drwxrwxr-x. 21 m m    4096 Feb  4 09:48 src
-rw-rw-r--.  1 m m     468 Feb  4 09:48 TODO.txt
-rw-rw-r--.  1 m m   16047 Feb  4 09:48 WhatsNew.txt

it is impossible to link /Urho3D/Source/ThirdParty/SDL/include to /Urho3D/Source/ThirdParty/SDL because directory is used for build SDL

also linux gives msg hardware error with make -j8

something messed up with the same directory SDL

-------------------------

weitjong | 2017-02-05 00:23:27 UTC | #4

You didn't give us what steps you took to generate your build tree. I think it is more important to know that rather than the content of your directory listing. So, help us to help you by providing more useful information.

It appears you have used non out-of-source build tree. Normally we recommend to have the build tree and source tree separated. This way, when the build tree is corrupted then we simply nuke the build tree and regenerate a new one with ease. When the source tree and build tree are not separated then one must nuke both and redo git-clone the source tree and then regenerate the build tree. Having said that, that was not the root cause of your problem as our build system supports both out-of-source and non out-of-source build trees. So none of what you posted above makes any sense to me, including why ```make -j8``` gave you hardware error.

-------------------------

ibatrakov | 2017-02-05 02:38:27 UTC | #5

$ git clone https://github.com/urho3d/Urho3D.git
$ cd Urho3D/
$ cmake CMakeLists.txt 
$ make -j8
$ uname -sr
Linux 4.9.6-200.fc25.x86_64

all samples compiled and working ok
but trying to make own qtcreator c++ project using Urho3D includes failed due to SDL wrong path

-------------------------

weitjong | 2017-02-05 03:09:46 UTC | #6

Read these two sections, in case you haven't: [Building Urho3D library](https://urho3d.github.io/documentation/HEAD/_building.html) and [Using Urho3D library ](https://urho3d.github.io/documentation/HEAD/_using_library.html)

Here are the gist:

* Use the provided build script or cmake-gui to generate an out-of-source build tree to build the Urho3D library
* Scaffold your own project based on Urho3D project so that you can reuse its build system
* Use the provided build script or cmake-gui to generate an out-of-source build tree to build your own app
* DO NOT use QtCreator to create/generate your project. Instead, use our build system to generate a build tree using the CMake/Code::Block generator (we have a build script for that) then open the generated Makefile project in the QtCreator.

HTH.

-------------------------

ibatrakov | 2017-02-05 03:59:15 UTC | #7

cb seems too buggy to me, was unable even create simple console app and double click on file in tree opens the same multiple file 

my failure, have to give up and wait working Orho SDK right from box

this topic can be deleted

-------------------------

weitjong | 2017-02-05 04:19:59 UTC | #8

You misunderstand me. I didn't ask you to change the IDE of your choice. The things is, CMake provides quite a number of generators but for some reason they do not provide generator for Qt. They have one for Eclipse and Code::Block, and even CodeLite. But regardless which one you choose, those generator actually just generate the GNU Makefiles project, plus one or two IDE-specific files. So, if you use C::B generator then you got an extra *.cbp file in the build tree. You can open this build tree using QtCreator IDE to build your project just fine. In fact the last time I checked it, QtCreator also uses CMake/C::B generator internally when you attempt to load a CMakeLists.txt and ask it to generate a project from it.

-------------------------

ibatrakov | 2017-02-06 13:47:50 UTC | #9

solution

$ ln -s /Urho3D/Source/ThirdParty/SDL/include /z/uhro_kludges
$ move /z/uhro_kludges/include /z/uhro_kludges/SDL

qt.pro
INCLUDEPATH += /z/uhro_kludges
INCLUDEPATH += /Urho3D/include/Urho3D
INCLUDEPATH += /Urho3D/Source/Samples
INCLUDEPATH += /Urho3D/include

LIBS += -L/Urho3D/lib
LIBS += -lUrho3D -ldl

now it is working, thanks for help

for future needed to rename /Urho3D/Source/ThirdParty/SDL/include to /Urho3D/Source/ThirdParty/SDL/SDL

-------------------------

weitjong | 2017-02-05 08:04:55 UTC | #10

Sure, but you are on your own with that kind of setup. Glad that you have it working, however.

-------------------------

