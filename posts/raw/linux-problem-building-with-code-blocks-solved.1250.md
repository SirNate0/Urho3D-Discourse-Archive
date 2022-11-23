christianclavet | 2017-01-02 01:06:23 UTC | #1

Hi, I had no problems building Urho on Windows with MSVC. But I am now trying to build it on Linux Mint.

I installed Code:Block and it used CGC (GNU compiler) 4.8. I also installed CMAKE with a graphical front end.

When I'm trying to do the configuration, I got this message coming from CMAKE:
[quote]CMake Error at CMake/Modules/Urho3D-CMake-common.cmake:662 (message):
  The configured compiler toolchain in the build tree is not able to handle
  all the compiler flags required to build the project.  Please kindly update
  your compiler toolchain to its latest version.  If you are using MinGW then
  make sure it is MinGW-W64 instead of MinGW-W32 or TDM-GCC (Code::Blocks
  default).  However, if you think there is something wrong with the compiler
  flags being used then please file a bug report to the project devs.
Call Stack (most recent call first):
  CMake/Modules/Urho3D-CMake-common.cmake:718 (enable_pch)
  CMake/Modules/Urho3D-CMake-common.cmake:774 (setup_target)
  Source/Urho3D/CMakeLists.txt:174 (setup_library)[/quote]

Seem something wrong with some compiler flags that are not working and can't build it.

Here are the first messages that passed the test:
[quote]The C compiler identification is GNU 4.8.4
The CXX compiler identification is GNU 4.8.4
Check for working C compiler: /usr/bin/cc
Check for working C compiler: /usr/bin/cc -- works
Detecting C compiler ABI info
Detecting C compiler ABI info - done
Check for working CXX compiler: /usr/bin/c++
Check for working CXX compiler: /usr/bin/c++ -- works
Detecting CXX compiler ABI info
Detecting CXX compiler ABI info - done
Looking for include file stdint.h
Looking for include file stdint.h - found
Looking for XOpenDisplay in /usr/lib/x86_64-linux-gnu/libX11.so;/usr/lib/x86_64-linux-gnu/libXext.so
Looking for XOpenDisplay in /usr/lib/x86_64-linux-gnu/libX11.so;/usr/lib/x86_64-linux-gnu/libXext.so - found
Looking for gethostbyname
Looking for gethostbyname - found
Looking for connect
Looking for connect - found
Looking for remove
Looking for remove - found
Looking for shmat
Looking for shmat - found
Found X11: /usr/lib/x86_64-linux-gnu/libX11.so
Found OpenGL: /usr/lib/x86_64-linux-gnu/libGL.so  
Performing Test HAVE_CONST_XEXT_ADDDISPLAY
Performing Test HAVE_CONST_XEXT_ADDDISPLAY - Success
Performing Test HAVE_CONST_XDATA32
Performing Test HAVE_CONST_XDATA32 - Success
Found ALSA: /usr/lib/x86_64-linux-gnu/libasound.so (found version "1.0.27.2") 
Performing Test COMPILER_HAS_HIDDEN_VISIBILITY
Performing Test COMPILER_HAS_HIDDEN_VISIBILITY - Success
Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY
Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY - Success
Performing Test COMPILER_HAS_DEPRECATED_ATTR
Performing Test COMPILER_HAS_DEPRECATED_ATTR - Success[/quote]

Does that mean that I must install MinGW-W64?

-------------------------

weitjong | 2017-01-02 01:06:23 UTC | #2

[quote="christianclavet"]Does that mean that I must install MinGW-W64?[/quote]
No, unless you intend to target Windows platform. You should use plain vanilla GCC when you intend to target native Linux platform. Last time I tried C::B on my Linux host system (Fedora 64bit), I have not encountered any problem. I was using GCC 4.9.x then but my GCC has been upgraded to 5.1 since. I have also changed my IDE from Eclipse to Clion but they all use the GCC native toolchain with ccache support enabled. No issue so far. So, I reckon if I change the frontend IDE to C::B now with the same GCC backend, it should just work.

I suspect your problem has something to do with the version of GCC and somehow it has tripped over due to the way we setup PCH (precompiled header). Try to upgrade your GCC compiler toolchain to 4.9 or later. This is always the problem when using Debian-based distros where stability is more important over having the latest and greatest version available. Alternatively, instead of using 1.4, try to download the latest Urho3D from master and then passing this build option when generating the Urho3D project file: -DURHO3D_PCH=0. This new build option will instruct the build system not to use PCH at all. Thus, if indeed your GCC version tripped over due to PCH then this build option should side step the problem. Good luck.

-------------------------

christianclavet | 2017-01-02 01:06:25 UTC | #3

Hi, Tried to update to 4.9.2 and still fail.

[quote]The CXX compiler identification is GNU 4.9.2
Check for working CXX compiler: /usr/bin/c++
Check for working CXX compiler: /usr/bin/c++ -- works
Detecting CXX compiler ABI info
Detecting CXX compiler ABI info - done
CMake Error at CMake/Modules/Urho3D-CMake-common.cmake:662 (message):
  The configured compiler toolchain in the build tree is not able to handle
  all the compiler flags required to build the project.  Please kindly update
  your compiler toolchain to its latest version.  If you are using MinGW then
  make sure it is MinGW-W64 instead of MinGW-W32 or TDM-GCC (Code::Blocks
  default).  However, if you think there is something wrong with the compiler
  flags being used then please file a bug report to the project devs.
Call Stack (most recent call first):
  CMake/Modules/Urho3D-CMake-common.cmake:718 (enable_pch)
  CMake/Modules/Urho3D-CMake-common.cmake:774 (setup_target)
  Source/Urho3D/CMakeLists.txt:174 (setup_library)[/quote]

I will see if I can replace this with the lastest and see... Fail at PCH again.

I will have to put it asside. The last version I have access is this 4.9.2 version and there are newer version but from what I've read, I need to recompile all the libs including the OS kernel to make it work. Won't do that for sure. In the next attempt. I'll check to download the last version from GITHUB and try your flag.

I'm trying to build Urho3D on Linux Mint 64 bit (17.2).

-------------------------

weitjong | 2017-01-02 01:06:25 UTC | #4

I have time to test running a build on one of my old Ubuntu VM image. It is Ubuntu 14.04.1 LTS with GCC version 4.8.4, i.e. same as yours. I got no problem there with PCH enabled. I generated the project file directly using cmake_codeblocks.sh via CLI and then just use 'make' command to build it directly. Building it via C::B should not be of any difference but I don't have it installed on my VM. Conclusion: there is something else causing your project file generation failure.

-------------------------

christianclavet | 2017-01-02 01:06:26 UTC | #5

I think I've made a "stupid" error LOL!  :smiley:  

Done the CLI command and it worked. Then checked why it was failing with the FRONTEND GUI: I was creating the build in a directory [u]that has spaces in the name[/u]: "URHO 3D BUILD".
I just changed the folder name to "URHO_3D_BUILD" then the configure command worked perfectly!

I think it could have worked with the 4.8 compiler, it's just that my build folder name had spaces in it! Thanks weitjong! You helped me a lot figure this out!

-------------------------

weitjong | 2017-01-02 01:06:26 UTC | #6

Good to hear that. The setup for PCH need to invoke the compiler at the time CMake is configuring and generating the Urho3D project file. So, most of the time it was the first error one would encounter when there were some problems with the compiler toolchain or build tree. Those problems may or may not be related to PCH. In the past before we have this PCH thingy, CMake would generate the project file silently despite those problems and user would only know about them much later after trying to build the project. By invoking the compiler early on, we get an early sign.

-------------------------

