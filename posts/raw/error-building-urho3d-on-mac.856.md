siska | 2017-01-02 01:03:33 UTC | #1

Hi,

I have been trying to build Urho3D on my MacBook Pro, & I got the following error : 

-----------------------------------------------------------------------------
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR - Success
In file included from /Users/scorneillie/DATA/Urho3DSrc/Source/Urho3D/Precompiled.h:25:
In file included from /Users/scorneillie/DATA/Urho3DSrc/Source/Urho3D/Container/HashMap.h:28:
In file included from /Users/scorneillie/DATA/Urho3DSrc/Source/Urho3D/Container/../Container/Vector.h:27:
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/../include/c++/v1/cassert:21:10: fatal error: 'assert.h' file not found
#include <assert.h>
         ^
1 error generated.
CMake Error at CMake/Modules/Urho3D-CMake-common.cmake:554 (message):
  The configured compiler toolchain in the build tree is not able to handle
  all the compiler flags required to build the project.  Please kindly update
  your compiler toolchain to its latest version.  If you are using MinGW then
  make sure it is MinGW-W64 instead of MinGW-W32 or TDM-GCC (Code::Blocks
  default).  However, if you think there is something wrong with the compiler
  flags being used then please file a bug report to the project devs.
Call Stack (most recent call first):
  CMake/Modules/Urho3D-CMake-common.cmake:610 (enable_pch)
  CMake/Modules/Urho3D-CMake-common.cmake:655 (setup_target)
  Source/Urho3D/CMakeLists.txt:163 (setup_library)

-- Configuring incomplete, errors occurred!
-----------------------------------------------------------------------------

I have some prior experience with Java, & made some small games in Unity3D (C#) & FlashPunk (Actionscript3), but I would like to try out Urho3D. As you can probably guess, I have no experience with C++ or Uhro3D.

Some details : MacBook Pro with freshly installed Yosemite OS, up to date XCode app (I plan on using this as my editor), successfully installed CMake, cloned master branch from git repository. 
I was using the cmake_macosx.sh file as follows : 

sh cmake_macosx.sh ../Urho3DBuild -DURHO3D_ANGELSCRIPT=1 -DURHO3D_SAMPLES=1 

This created some folders and files inside my build dir (=Urho3DBuild), but left me with an empty 'build' subdir.
I'm clueless as to what I should do next. So, any help is very much appreciated !

-------------------------

Softwave | 2017-01-02 01:03:34 UTC | #2

Did you install the command line tools when you installed XCode? If not, do that and then try it again. 

You can install them by typing the following into the terminal. 

[code]xcode-select --install[/code]

-------------------------

