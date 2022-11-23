mcra3005 | 2017-01-02 01:10:17 UTC | #1

Help Please,
I am trying to cross compile for windows I am using a Linux Ubuntu Host system, I installed mingw 32 bit headers and librarys are under
/usr/i686-w64-mingw32 and 64 bit headers and librarys are under /usr/x86_64-w64-mingw32 the binarys were automatically installed
under /usr/bin, but I copied all i686 Mingw binarys under the /usr/i686-w64-mingw32/bin , and all  x86_64 Mingw binarys under /usr/x86_64-w64-mingw32/bin
also copied the direct headers downloaded into both include directories and librarys into lib directories so. Basically I have bin, lib  and include structure
under each directory  i686-w64-mingw32 for 32 bit windows  and x86_64-w64-mingw32 for 64 bit windows. I installed Urho3D-1.5 Source,
now I succesuffly compiled and make 64 bit and 32 bit linux excuteables already, so I wanted to compile for Windows.

So I use the command Below But never works, any one  got this working cross compiling please help
./cmake_mingw.sh $URHO3D_HOME -DWIN32=1 -DURHO3D_64BIT=0 -DURHO3D_ANGELSCRIPT=0 -DURHO3D_SAMPLES=1 -DURHO3D_TOOLS=0 -DURHO3D_PACKAGING=1 -DURHO3D_LOGGING=0 -DCMAKE_BUILD_TYPE=Release -DMINGW_PREFIX=i686-w64-mingw32 -DMINGW_SYSROOT=/usr/i686-w64-mingw32

But I get error below 
CMake Error at CMake/Toolchains/mingw.toolchain.cmake:40 (message):
  Could not find MinGW cross compilation tool.  Use MINGW_PREFIX environment
  variable or build option to specify the location of the toolchain.
Call Stack (most recent call first):
  /UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/cmake-3.5.0-rc1-Linux-x86_64/share/cmake-3.5/Modules/CMakeDetermineSystem.cmake:98 (include)
  CMakeLists.txt:24 (project)


CMake Error: CMAKE_C_COMPILER not set, after EnableLanguage
CMake Error: CMAKE_CXX_COMPILER not set, after EnableLanguage
-- Configuring incomplete, errors occurred!

-------------------------

rasteron | 2017-01-02 01:10:17 UTC | #2

Hey mcra3005,

Welcome to the forums! :slight_smile: First off, you could try setting up using CMake GUI, as it would be so much easier getting rid of those path and environment errors and check again.

-------------------------

mcra3005 | 2017-01-02 01:10:17 UTC | #3

Hi Raston

I tried CMAKE  GUI it always gave errors and complain about paths and similar errors also. 
Have you done this in CMAKE GUI what steps did you do just in case I am doing it wrong .

Thanks

-------------------------

1vanK | 2017-01-02 01:10:17 UTC | #4

May be problem is here?

[quote="mcra3005"]-DMINGW_PREFIX=i686-w64-mingw32

Use MINGW_PREFIX environment variable or build option to specify the [b]location[/b] of the toolchain.
[/quote]

-------------------------

rasteron | 2017-01-02 01:10:17 UTC | #5

[quote="mcra3005"]Hi Raston

I tried CMAKE  GUI it always gave errors and complain about paths and similar errors also. 
Have you done this in CMAKE GUI what steps did you do just in case I am doing it wrong .

Thanks[/quote]

I'm also taking a crack at it.. used to build mingw for windows only with urho. btw, have you also tried the [b]cmake_mingw.sh[/b] script? You can also check with 1vanK's suggestion.

-------------------------

mcra3005 | 2017-01-02 01:10:17 UTC | #6

Hi Ivan,

From [urho3d.github.io/documentation/1 ... lding.html](http://urho3d.github.io/documentation/1.5/_building.html) it said Prefix path to MinGW cross-compiler tools (MinGW cross-compiling build only)
i.e A prefix instaed of gcc it will run i686-w64-mingw32-gcc  and attach the  i686-w64-mingw32 as a prefix ??
but that waht I thought.

I also thought /usr/i686-w64-mingw32 is MINGW_SYSROOT since that is where the bin, lib, include for the MInGW was?? 

But anyway I tried Now and did -DMINGW_PREFIX=/usr/i686-w64-mingw32 and -DMINGW_PREFIX=/usr/i686-w64-mingw32/bin and still got the same
error or Their another value I should set it to. 

Any IDeas how to get this to work??

-------------------------

weitjong | 2017-01-02 01:10:18 UTC | #7

Do not doubt the error message given by the CMake error. The message is quite clear to me that the MINGW_PREFIX build option is not being set correctly. MINGW_PREFIX is not a path. It contains a prefix string for the GCC compiler toolchain. In my Linux box, I do not have to make any manual correction to the binary installation location. Basically I just did a yum/dnf install of the MinGW64 packages and all set to go. So, another possibility is you have a borked installation. Here is what I have, just for your comparison.

[code]$ echo $MINGW_PREFIX
/usr/bin/x86_64-w64-mingw32

$ ls /usr/bin/x86_64-w64-mingw32*
/usr/bin/x86_64-w64-mingw32-addr2line  /usr/bin/x86_64-w64-mingw32-gcc         /usr/bin/x86_64-w64-mingw32-nm
/usr/bin/x86_64-w64-mingw32-ar         /usr/bin/x86_64-w64-mingw32-gcc-5.2.0   /usr/bin/x86_64-w64-mingw32-objcopy
/usr/bin/x86_64-w64-mingw32-as         /usr/bin/x86_64-w64-mingw32-gcc-ar      /usr/bin/x86_64-w64-mingw32-objdump
/usr/bin/x86_64-w64-mingw32-c++        /usr/bin/x86_64-w64-mingw32-gcc-nm      /usr/bin/x86_64-w64-mingw32-ranlib
/usr/bin/x86_64-w64-mingw32-c++filt    /usr/bin/x86_64-w64-mingw32-gcc-ranlib  /usr/bin/x86_64-w64-mingw32-readelf
/usr/bin/x86_64-w64-mingw32-cpp        /usr/bin/x86_64-w64-mingw32-gcov        /usr/bin/x86_64-w64-mingw32-size
/usr/bin/x86_64-w64-mingw32-dlltool    /usr/bin/x86_64-w64-mingw32-gcov-tool   /usr/bin/x86_64-w64-mingw32-strings
/usr/bin/x86_64-w64-mingw32-dllwrap    /usr/bin/x86_64-w64-mingw32-gprof       /usr/bin/x86_64-w64-mingw32-strip
/usr/bin/x86_64-w64-mingw32-elfedit    /usr/bin/x86_64-w64-mingw32-ld          /usr/bin/x86_64-w64-mingw32-windmc
/usr/bin/x86_64-w64-mingw32-g++        /usr/bin/x86_64-w64-mingw32-ld.bfd      /usr/bin/x86_64-w64-mingw32-windres[/code]
You can set MINGW_PREFIX as build option or as environment variable. I like the latter approach because I don't have to retype the prefix again and again.  I nuke and recreate my MinGW build tree quite frequently when modifying and testing Urho3D build system.

-------------------------

mcra3005 | 2017-01-02 01:10:18 UTC | #8

Thanks

I Tried the new MINGW_PREFIX my output did change I also have the binarys in /usr/bin also but I made a copy to the same directorys  under /usr
where mingw installed the /include and /lib.

I also noticed it was refering to comiplers in /usr/lib/ccache so I removed the links their.

I also set my environment variable but when that did not work I tried the option also

Anyway what is your MINGW_SYSROOT set to ?

When I rerun with the new MINGW_PREFIX I get the following errors below any ideas?
Thanks.

-- The C compiler identification is unknown
-- The CXX compiler identification is unknown
-- Check for working C compiler: /UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/BUrho3D/i686-w64-mingw32-gcc
-- Check for working C compiler: /UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/BUrho3D/i686-w64-mingw32-gcc -- broken
CMake Error at /UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/cmake-3.5.0-rc1-Linux-x86_64/share/cmake-3.5/Modules/CMakeTestCCompiler.cmake:61 (message):
  The C compiler
  "/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/BUrho3D/i686-w64-mingw32-gcc"
  is not able to compile a simple test program.

  It fails with the following output:

   Change Dir: /UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/BUrho3D/CMakeFiles/CMakeTmp

  

  Run Build Command:"/usr/bin/make" "cmTC_4f2bc/fast"

  /usr/bin/make -f CMakeFiles/cmTC_4f2bc.dir/build.make
  CMakeFiles/cmTC_4f2bc.dir/build

  make[1]: Entering directory
  `/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/BUrho3D/CMakeFiles/CMakeTmp'

  Building C object CMakeFiles/cmTC_4f2bc.dir/testCCompiler.c.obj

  /UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/BUrho3D/i686-w64-mingw32-gcc -o
  CMakeFiles/cmTC_4f2bc.dir/testCCompiler.c.obj -c
  /UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/BUrho3D/CMakeFiles/CMakeTmp/testCCompiler.c


  i686-w64-mingw32-gcc: error trying to exec 'cc1': execvp: No such file or
  directory

  make[1]: *** [CMakeFiles/cmTC_4f2bc.dir/testCCompiler.c.obj] Error 1

  make[1]: Leaving directory
  `/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/BUrho3D/CMakeFiles/CMakeTmp'

  make: *** [cmTC_4f2bc/fast] Error 2

  

  

  CMake will not be able to correctly generate this project.
Call Stack (most recent call first):
  CMakeLists.txt:24 (project)


-- Configuring incomplete, errors occurred!
See also "/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/BUrho3D/CMakeFiles/CMakeOutput.log".
See also "/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/BUrho3D/CMakeFiles/CMakeError.log".

-------------------------

rasteron | 2017-01-02 01:10:18 UTC | #9

Ok, I got it configured and build with win32 on my ubuntu 32bit vbox, copied and ran some tools/examples to windows 7 and works ok.

[img]http://i.imgur.com/uwGp2ar.png[/img]

[quote]Anyway what is your MINGW_SYSROOT set to ?[/quote]

I use [b]/usr/x86_64-w64-mingw32[/b]

-------------------------

mcra3005 | 2017-01-02 01:10:18 UTC | #10

Thats Great you got it compiled your SYSROOT variable looks the same but I have the /usr/i686-w64-mingw32
what steps did you do I guess if you used the CMAKE GUI what option did you pick and what did you put in your boxes.

But I am trying to compile 32 bit windows on 64 bit Linux Ubuntu real system.
Hopefully your settings and CMAKEGUI Directions can help me.

Thanks.

-------------------------

rasteron | 2017-01-02 01:10:18 UTC | #11

[quote="mcra3005"]Thats Great you got it compiled your SYSROOT variable looks the same but I have the /usr/i686-w64-mingw32
what steps did you do I guess if you used the CMAKE GUI what option did you pick and what did you put in your boxes.

But I am trying to compile 32 bit windows on 64 bit Linux Ubuntu real system.
Hopefully your settings and CMAKEGUI Directions can help me.

Thanks.[/quote]

Sure thing. I did not use CMake GUI at this time as the console stuff looks fairly straightforward following the docs. OS emulation is as good as the real system, even in this case with default or dummy graphic setup/acceleration for 3D apps. I only used OPENGL for quick testing. Some key stuff that I did:

[code]
export MINGW_SYSROOT=/usr/x86_64-w64-mingw32
./cmake_mingw.sh ./mingw -DMINGW_PREFIX=/usr/bin/x86_64-w64-mingw32 -DURHO3D_OPENGL=1
[/code]

I think your setup just got messed up somewhere or try the above with the 64bit equivalent.

Hope that helps and good luck :slight_smile:

[b]EDIT:[/b] I did a 64bit exe build with this test when I recalled using the URHO3D_64BIT=1 if it is of any help

[img]http://i.imgur.com/QAvEMNf.jpg[/img]

-------------------------

mcra3005 | 2017-01-02 01:10:18 UTC | #12

Well I got Urho to crosscompile and generate the files now but I have a issue when I try to make shown below any Ideas??

I found that after setting the fully qualified path for the prefix it almost worked but complain about cc1, it appears that ccache does not like cross compiling
I disabled it and it almost worked due to 32 bit version I had to disable PCH option and due to gcc version I had to disable SSE.
Then it configured the make files.
But when I tried to make I get below error which is why I disabled the PCH option?

Any Ideas

make
Scanning dependencies of target FreeType
[  1%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/autofit/autofit.c.obj
i686-w64-mingw32-gcc: error: unrecognized command line option ?-fno-tree-loop-vectorize?
make[2]: *** [Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/autofit/autofit.c.obj] Error 1
make[1]: *** [Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/all] Error 2
make: *** [all] Error 2

-------------------------

rasteron | 2017-01-02 01:10:18 UTC | #13

[quote="mcra3005"]Well I got Urho to crosscompile and generate the files now but I have a issue when I try to make shown below any Ideas??

I found that after setting the fully qualified path for the prefix it almost worked but complain about cc1, it appears that ccache does not like cross compiling
I disabled it and it almost worked due to 32 bit version I had to disable PCH option and due to gcc version I had to disable SSE.
Then it configured the make files.
But when I tried to make I get below error which is why I disabled the PCH option?

Any Ideas

make
Scanning dependencies of target FreeType
[  1%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/autofit/autofit.c.obj
i686-w64-mingw32-gcc: error: unrecognized command line option ?-fno-tree-loop-vectorize?
make[2]: *** [Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/autofit/autofit.c.obj] Error 1
make[1]: *** [Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/all] Error 2
make: *** [all] Error 2[/quote]

Hey, great to hear you got some progress! As for that [i]?-fno-tree-loop-vectorize?[/i] specific error, I ran into the same but with mingw windows, see here: [github.com/urho3d/Urho3D/issues/1124](https://github.com/urho3d/Urho3D/issues/1124)

Upgrade your mingw gcc and it should get rid of that issue :wink:

-------------------------

mcra3005 | 2017-01-02 01:10:18 UTC | #14

PostPosted by rasteron ? 23 Feb 2016, 20:10

mcra3005 wrote:
Thats Great you got it compiled your SYSROOT variable looks the same but I have the /usr/i686-w64-mingw32
what steps did you do I guess if you used the CMAKE GUI what option did you pick and what did you put in your boxes.

But I am trying to compile 32 bit windows on 64 bit Linux Ubuntu real system.
Hopefully your settings and CMAKEGUI Directions can help me.

Thanks.


Sure thing. I did not use CMake GUI at this time as the console stuff looks fairly straightforward following the docs. OS emulation is as good as the real system, even in this case with default or dummy graphic setup/acceleration for 3D apps. I only used OPENGL for quick testing. Some key stuff that I did are:

CODE: SELECT ALL
export MINGW_SYSROOT=/usr/x86_64-w64-mingw32
./cmake_mingw.sh ./mingw -DMINGW_PREFIX=/usr/bin/x86_64-w64-mingw32 -DURHO3D_OPENGL=1


I think your setup just got messed up somewhere or try the above with the 64bit equivalent.

Hope that helps and good luck :slight_smile:

EDIT: I did a 64bit exe build with this test when I recalled using the URHO3D_64BIT=1 if it is of any help

Image
Raster Games | G+ github.com/rasteron | StrikeForce
User avatar
rasteron
Most active user
Most active user
 
Posts: 311
Joined: 07 Mar 2014, 17:46
Location: web
Top
Re: Cross Compile LInux Host for Windows Help Please
PostPosted by mcra3005 ? 23 Feb 2016, 22:01

Well I got Urho to crosscompile and generate the files now but I have a issue when I try to make shown below any Ideas??

I found that after setting the fully qualified path for the prefix it almost worked but complain about cc1, it appears that ccache does not like cross compiling
I disabled it and it almost worked due to 32 bit version I had to disable PCH option and due to gcc version I had to disable SSE.
Then it configured the make files.
But when I tried to make I get below error which is why I disabled the PCH option?

Any Ideas

make
Scanning dependencies of target FreeType
[ 1%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/autofit/autofit.c.obj
i686-w64-mingw32-gcc: error: unrecognized command line option ?-fno-tree-loop-vectorize?
make[2]: *** [Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/autofit/autofit.c.obj] Error 1
make[1]: *** [Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/all] Error 2
make: *** [all] Error 2

-------------------------

weitjong | 2017-01-02 01:10:18 UTC | #15

[quote="mcra3005"]Thanks

I Tried the new MINGW_PREFIX my output did change I also have the binarys in /usr/bin also but I made a copy to the same directorys  under /usr
where mingw installed the /include and /lib.

I also noticed it was refering to comiplers in /usr/lib/ccache so I removed the links their.[/quote]
But why? Believe me, using your compiler toolchains via ccache is a very good thing. If ccache is not good then your distro would not have set it up to work with the installed compiler toolchains by default.

[quote="mcra3005"]I found that after setting the fully qualified path for the prefix it almost worked but complain about cc1, it appears that ccache does not like cross compiling[/quote]
This is not true. ccache works with any GCC and Clang compiler toolchains, native or cross-compile one. All our CI build jobs on Travis CI linux boxes are in fact using ccache to shorten the build time. Our typical build time for MinGW CI build jobs are 2 to 3 minutes. We have about 1 minute overhead to prepare the VM at the start of CI job to install MinGW on the fly, git clone the repository, setting up the cache, etc. So, in essence, our MinGW CI jobs only take about 1 to 2 minutes to build from scratch! Thanks to ccache.

We have a section in our online documentation describing the usage of ccache, if you are interested. Also use 'man ccache' to learn more.

[quote="rasteron"]Hey, great to hear you got some progress! As for that ?-fno-tree-loop-vectorize? specific error, I ran into the same but with mingw windows, see here: [github.com/urho3d/Urho3D/issues/1124](https://github.com/urho3d/Urho3D/issues/1124)[/quote]
rasteron has nailed it down correctly on this one.

-------------------------

mcra3005 | 2017-01-02 01:10:19 UTC | #16

Thanks everyone, I can generate the files now but weather I do a 64 bit windows build or 32 windows build using cross compiling
I have the following errors below.

I was advised that a version of gcc i.e. i686-w64-mingw32-gcc or x86_64-w64-mingw32-gcc  at 4.9.1 should fix this ?
I am on ubuntu 14.04 any idea where I could get updated versions of these or do I need to look for sources and compile ???

Or do I need a new OS??

Thanks

64 bit 
SDL_dxjoystick_c.h:133:5: error: unknown type name ?LPDIRECTINPUTDEVICE8?
make[2]: *** [Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/haptic/windows/SDL_syshaptic.c.obj] Error 1
32 bit
Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/autofit/autofit.c.obj
i686-w64-mingw32-gcc: error: unrecognized command line option ?-fno-tree-loop-vectorize?

-------------------------

weitjong | 2017-01-02 01:10:19 UTC | #17

For compiler toolchain, later version is always the better one, generally speaking. So I would always go for the latest provided by my distro package manager. GCC 4.9.1 is ancient when measured in computer time. Try to upgrade and come back here if you still encountering error despite of that. Good luck.

EDIT: My Linux distro is 64-bit Fedora. Currently the latest Fedora release is 23. In this release, the GCC compiler toolchain version is 5.3.1 and MinGW version is 5.2.0. The Clang version is 4.2.1 which is quite recent also. This is why I like about Fedora. Cutting edge software. Besides, "blue" is my favorite color  :wink: . If you use Ubuntu then try to upgrade to the latest Ubuntu you can find and if even after that still it does not work then try to enable the ubuntu-toolchain-r-test PPA to your Ubuntu system in order to upgrade to the latest compiler version available for your distro. See how this is done in our .travis.yml file.

-------------------------

mcra3005 | 2017-01-02 01:10:27 UTC | #18

Hi all,

It took a while but.

I rebuilt my Linux envirnoment to Ubuntu 15.10, and have a more upgraded version of mingw gcc and I have all my
Prefix and Sysroot variables correct I can Cmake the files for windows 32 bit or windows 64 bit using cross compiling
but when I do make. I get the current error weather I try to compile for 64 bit windows or 32 bit Below. 

Of course i am doing this on a Linux 64 bit OS i.e. Ubuntu

Any Ideas ??

[ 16%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/haptic/windows/SDL_syshaptic.c.obj
In file included from /UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c:34:0:
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/../../joystick/windows/SDL_dxjoystick_c.h:133:5: error: unknown type name ?LPDIRECTINPUTDEVICE8?
     LPDIRECTINPUTDEVICE8 InputDevice;
     ^
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c:58:5: error: unknown type name ?LPDIRECTINPUTDEVICE8?
     LPDIRECTINPUTDEVICE8 device;
     ^
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c:85:8: error: unknown type name ?LPDIRECTINPUT8?
 static LPDIRECTINPUT8 dinput = NULL;
        ^
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c:105:42: error: unknown type name ?LPDIRECTINPUTDEVICE8?
                                          LPDIRECTINPUTDEVICE8 device8,

-------------------------

rasteron | 2017-01-02 01:10:27 UTC | #19

That looks like a [url=https://www.google.com/search?q=LPDIRECTINPUTDEVICE8&oq=LPDIRECTINPUTDEVICE8]Direct X[/url] related error. I'm not sure, but since that you're still using MinGW + DirectX, did you include the directx headers?

[quote]
If using MinGW to compile, DirectX headers may need to be acquired separately. They can be copied to the MinGW installation eg. from the following package: [libsdl.org/extras/win32/comm ... vel.tar.gz](http://www.libsdl.org/extras/win32/common/directx-devel.tar.gz) These will be missing some of the headers related to shader compilation, so a MinGW build will use OpenGL by default.[/quote]

[libsdl.org/extras/win32/comm ... vel.tar.gz](http://www.libsdl.org/extras/win32/common/directx-devel.tar.gz)

Try with the OpenGL enabled build and see if you're still having those issues or include those headers for DirectX.

-------------------------

mcra3005 | 2017-01-02 01:10:27 UTC | #20

I did use the CMake with -DURHO3D_OPENGL=1 I still got the same error I did download previously the same DirectX headers and I copied the include and lib folder
contents into the /usr/i686-w64-mingw32  and also in the /usr/x86_64-w64-mingw32. But still I have the same error I am using Urho3D-1.5 source from main web site.
It looks like a SDL error possible a  definition error but only complains when it looks at the windows source.

Not sure what to do I even did the option like you did minumum ./cmake_mingw.sh $URHO3D_HOME -DURHO3D_OPENGL=1 to do a 64bit windows but when I run the
make command in the Build directory I get the errors I mention weather it is 32 bit or 64 bit.

How does anyone else cross compile ???

Any Ideas ??

Is their a Variable I meant to point to the DirectX ???
Thanks

-------------------------

weitjong | 2017-01-02 01:10:29 UTC | #21

[quote="mcra3005"]Hi all,

It took a while but.

I rebuilt my Linux envirnoment to Ubuntu 15.10, and have a more upgraded version of mingw gcc and I have all my
Prefix and Sysroot variables correct I can Cmake the files for windows 32 bit or windows 64 bit using cross compiling
but when I do make. I get the current error weather I try to compile for 64 bit windows or 32 bit Below. 

Of course i am doing this on a Linux 64 bit OS i.e. Ubuntu

Any Ideas ??

[ 16%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/haptic/windows/SDL_syshaptic.c.obj
In file included from /UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c:34:0:
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/../../joystick/windows/SDL_dxjoystick_c.h:133:5: error: unknown type name ?LPDIRECTINPUTDEVICE8?
     LPDIRECTINPUTDEVICE8 InputDevice;
     ^
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c:58:5: error: unknown type name ?LPDIRECTINPUTDEVICE8?
     LPDIRECTINPUTDEVICE8 device;
     ^
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c:85:8: error: unknown type name ?LPDIRECTINPUT8?
 static LPDIRECTINPUT8 dinput = NULL;
        ^
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c:105:42: error: unknown type name ?LPDIRECTINPUTDEVICE8?
                                          LPDIRECTINPUTDEVICE8 device8,[/quote]
How did you install your MinGW-W64? It seems you have not installed the "mingw-w64-dev" package. Also when troubleshooting compiler error, pasting the first few lines of the error messages do not actually help. Those that you pasted was not the root cause of the error. The error should be further down. I think the compiler should be complaining about not able to find the "dinput.h". The header file is available in the development package that I just mentioned. Install that and you should be good.

-------------------------

mcra3005 | 2017-01-02 01:10:34 UTC | #22

My full error from trying to cross compile i.e. use make in the build directory is below, when I tried to apt-get install dev for mingw it stted it was already the newest,
Any way my error I get is below the full out put any ideas. ??

Thanks.

[ 17%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/haptic/windows/SDL_syshaptic.c.obj
In file included from /UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c:34:0:
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/../../joystick/windows/SDL_dxjoystick_c.h:133:5: error: unknown type name ?LPDIRECTINPUTDEVICE8?
     LPDIRECTINPUTDEVICE8 InputDevice;
     ^
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c:58:5: error: unknown type name ?LPDIRECTINPUTDEVICE8?
     LPDIRECTINPUTDEVICE8 device;
     ^
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c:85:8: error: unknown type name ?LPDIRECTINPUT8?
 static LPDIRECTINPUT8 dinput = NULL;
        ^
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c:105:42: error: unknown type name ?LPDIRECTINPUTDEVICE8?
                                          LPDIRECTINPUTDEVICE8 device8,
                                          ^
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c: In function ?SDL_SYS_HapticInit?:
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c:157:16: warning: comparison between pointer and integer
     if (dinput != NULL) {       /* Already open. */
                ^
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c:168:29: error: ?CLSID_DirectInput8? undeclared (first use in this function)
     ret = CoCreateInstance(&CLSID_DirectInput8, NULL, CLSCTX_INPROC_SERVER,
                             ^
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c:168:29: note: each undeclared identifier is reported only once for each function it appears in
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c:169:29: error: ?IID_IDirectInput8? undeclared (first use in this function)
                            &IID_IDirectInput8, (LPVOID) & dinput);
                             ^
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c: In function ?DirectInputHaptic_MaybeAddDevice?:
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c:219:5: error: unknown type name ?LPDIRECTINPUTDEVICE8?
     LPDIRECTINPUTDEVICE8 device;
     ^
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c:224:16: warning: comparison between pointer and integer
     if (dinput == NULL) {
                ^
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c: In function ?DirectInputHaptic_MaybeRemoveDevice?:
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c:291:16: warning: comparison between pointer and integer
     if (dinput == NULL) {
                ^
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c: In function ?SDL_SYS_HapticOpenFromInstance?:
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c:538:5: error: unknown type name ?LPDIRECTINPUTDEVICE8?
     LPDIRECTINPUTDEVICE8 device;
     ^
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c:539:5: error: unknown type name ?LPDIRECTINPUTDEVICE8?
     LPDIRECTINPUTDEVICE8 device8;
     ^
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c:551:46: error: ?IID_IDirectInputDevice8? undeclared (first use in this function)
                                             &IID_IDirectInputDevice8,
                                              ^
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c: At top level:
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c:645:31: error: unknown type name ?LPDIRECTINPUTDEVICE8?
                               LPDIRECTINPUTDEVICE8 device8, SDL_bool is_joystick)
                               ^
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c: In function ?SDL_SYS_HapticMouse?:
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c:798:45: error: ?DI8DEVCLASS_POINTER? undeclared (first use in this function)
         if (item->capabilities.dwDevType == DI8DEVCLASS_POINTER ) {
                                             ^
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c: In function ?SDL_SYS_HapticQuit?:
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c:968:16: warning: comparison between pointer and integer
     if (dinput != NULL) {
                ^
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c:970:16: warning: assignment makes integer from pointer without a cast
         dinput = NULL;
                ^
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c: In function ?SDL_SYS_ToDIEFFECT?:
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c:1123:13: error: ?DIEFFECT? has no member named ?dwStartDelay?
         dest->dwStartDelay = hap_constant->delay * 1000;        /* In microseconds. */
             ^
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c:1170:13: error: ?DIEFFECT? has no member named ?dwStartDelay?
         dest->dwStartDelay = hap_periodic->delay * 1000;        /* In microseconds. */
             ^
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c:1223:13: error: ?DIEFFECT? has no member named ?dwStartDelay?
         dest->dwStartDelay = hap_condition->delay * 1000;       /* In microseconds. */
             ^
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c:1255:13: error: ?DIEFFECT? has no member named ?dwStartDelay?
         dest->dwStartDelay = hap_ramp->delay * 1000;    /* In microseconds. */
             ^
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c:1299:13: error: ?DIEFFECT? has no member named ?dwStartDelay?
         dest->dwStartDelay = hap_custom->delay * 1000;  /* In microseconds. */
             ^
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c: In function ?SDL_SYS_HapticUpdateEffect?:
/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/Urho3D-1.5/Source/ThirdParty/SDL/src/haptic/windows/SDL_syshaptic.c:1497:9: error: ?DIEP_STARTDELAY? undeclared (first use in this function)
         DIEP_STARTDELAY |
         ^
Source/ThirdParty/SDL/CMakeFiles/SDL.dir/build.make:1886: recipe for target 'Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/haptic/windows/SDL_syshaptic.c.obj' failed
make[2]: *** [Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/haptic/windows/SDL_syshaptic.c.obj] Error 1
CMakeFiles/Makefile2:444: recipe for target 'Source/ThirdParty/SDL/CMakeFiles/SDL.dir/all' failed
make[1]: *** [Source/ThirdParty/SDL/CMakeFiles/SDL.dir/all] Error 2
Makefile:149: recipe for target 'all' failed
make: *** [all] Error 2

-------------------------

weitjong | 2017-01-02 01:10:35 UTC | #23

[quote="mcra3005"]I did use the CMake with -DURHO3D_OPENGL=1 I still got the same error I did download previously the same DirectX headers and I copied the include and lib folder
contents into the /usr/i686-w64-mingw32  and also in the /usr/x86_64-w64-mingw32.[/quote]
I think I have said this before. Just use your package manager to install the bits. When you have any missing headers and libraries, hunt down the correct package(s) that provides those missing headers and libraries. Never attempt to become root and try to mess with the installed files manually. Although at this point I am really just guessing what have happened, but if what you claimed is true that your system already has the DirectX development headers installed then the culprit may be your earlier action to download and override them with incompatible version from other sources. Anyway, I am kind of lost myself at what state your MinGW installation status. It might be worth to try to uninstall and reinstall the MinGW again. And ensure this time you get this development package installed when you are done: 'mingw-w64-dev' for 64-bit or 'mingw-w64-i686-dev' for 32-bit.

-------------------------

weitjong | 2017-01-02 01:10:36 UTC | #24

Alternatively, you can try to asses your MinGW installation status by doing below simple test. The test output below is from my 64-bit Fedora 23, so YMMV a little bit on Ubuntu. Note: the trailing '-' in the first command is important, so don't miss it.
[code][weitjong@igloo Urho3D]$ echo '#include <dinput.h>' |/usr/bin/x86_64-w64-mingw32-gcc -E -MTdeps -M -
deps:  /usr/x86_64-w64-mingw32/sys-root/mingw/include/dinput.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/objbase.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/winapifamily.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/rpc.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/_mingw.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/_mingw_mac.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/_mingw_secapi.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/vadefs.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/sdks/_mingw_directx.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/sdks/_mingw_ddk.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/windows.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/sdkddkver.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/excpt.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/crtdefs.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/stdarg.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/stdarg.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/_mingw_stdarg.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/windef.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/minwindef.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/specstrings.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/sal.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/winnt.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/_mingw_unicode.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/ctype.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/apiset.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/psdk_inc/intrin-impl.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/basetsd.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/guiddef.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/string.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/sec_api/string_s.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/x86intrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/ia32intrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/mmintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/xmmintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/mm_malloc.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/stdlib.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include-fixed/limits.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include-fixed/syslimits.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/limits.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/sec_api/stdlib_s.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/malloc.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/errno.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/emmintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/pmmintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/tmmintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/ammintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/smmintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/popcntintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/wmmintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/immintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/avxintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/avx2intrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/avx512fintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/avx512erintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/avx512pfintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/avx512cdintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/avx512vlintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/avx512bwintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/avx512dqintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/avx512vlbwintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/avx512vldqintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/avx512ifmaintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/avx512ifmavlintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/avx512vbmiintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/avx512vbmivlintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/shaintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/lzcntintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/bmiintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/bmi2intrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/fmaintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/f16cintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/rtmintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/xtestintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/mm3dnow.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/prfchwintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/fma4intrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/xopintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/lwpintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/tbmintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/rdseedintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/fxsrintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/xsaveintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/xsaveoptintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/adxintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/clwbintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/pcommitintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/clflushoptintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/xsavesintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/xsavecintrin.h \
 /usr/lib/gcc/x86_64-w64-mingw32/5.2.0/include/mwaitxintrin.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/pshpack4.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/poppack.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/pshpack4.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/pshpack2.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/poppack.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/pshpack2.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/pshpack8.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/pshpack8.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/ktmtypes.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/winbase.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/apisetcconv.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/minwinbase.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/bemapiset.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/debugapi.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/errhandlingapi.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/fibersapi.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/fileapi.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/handleapi.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/heapapi.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/ioapiset.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/interlockedapi.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/jobapi.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/libloaderapi.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/memoryapi.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/namedpipeapi.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/namespaceapi.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/processenv.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/processthreadsapi.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/processtopologyapi.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/profileapi.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/realtimeapiset.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/securityappcontainer.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/securitybaseapi.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/synchapi.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/sysinfoapi.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/systemtopologyapi.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/threadpoolapiset.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/threadpoollegacyapiset.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/utilapiset.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/wow64apiset.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/winerror.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/fltwinerror.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/timezoneapi.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/wingdi.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/pshpack1.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/winuser.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/tvout.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/winnls.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/datetimeapi.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/stringapiset.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/wincon.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/winver.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/winreg.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/reason.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/winnetwk.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/wnnc.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/virtdisk.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/cderr.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/dde.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/ddeml.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/dlgs.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/lzexpand.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/mmsystem.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/nb30.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/rpcdce.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/rpcdcep.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/rpcnsi.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/rpcnterr.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/rpcasync.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/shellapi.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/winperf.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/winsock.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/_timeval.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/_bsd_types.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/inaddr.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/psdk_inc/_socket_types.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/psdk_inc/_fd_types.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/psdk_inc/_ip_types.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/psdk_inc/_ip_mreq1.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/psdk_inc/_wsadata.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/psdk_inc/_xmitfile.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/psdk_inc/_wsa_errnos.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/wincrypt.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/bcrypt.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/ncrypt.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/dpapi.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/winefs.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/winscard.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/wtypes.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/rpcndr.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/rpcnsip.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/rpcsal.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/wtypesbase.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/winioctl.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/winsmcrd.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/winspool.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/prsht.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/ole2.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/combaseapi.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/unknwnbase.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/objidlbase.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/cguid.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/objidl.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/unknwn.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/urlmon.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/oleidl.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/servprov.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/msxml.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/oaidl.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/propidl.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/oleauto.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/commdlg.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/stralign.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/sec_api/stralign_s.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/winsvc.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/mcx.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/imm.h \
 /usr/x86_64-w64-mingw32/sys-root/mingw/include/_mingw_dxhelper.h
[weitjong@igloo Urho3D]$ echo $?
0[/code]

-------------------------

mcra3005 | 2017-01-02 01:11:24 UTC | #25

I Finally got Windows Cross compiling working it appears the error message was due to Direct X headers files
I downloaded ones from a source Downloaded DirectX9.0C from [dim-i.net/2004/06/26/directx-devpak-for-dev-cpp/](http://dim-i.net/2004/06/26/directx-devpak-for-dev-cpp/)
and copied as per below directorys as below, includes to include  and libs to lib Now i did the same with the Urho3D link for DirectX
headers but it did not work, once I used this source it worked.  Once again Thankyou everyone on this Forum you have been very
helpful and tried, a great forum and support.

cp -v * /usr/i686-w64-mingw32/lib
cp -v * /usr/lib
cp -v *.h /usr/i686-w64-mingw32/include
cp -v *.h /usr/include

-------------------------

weitjong | 2017-01-02 01:11:24 UTC | #26

Glad to hear that. However,  forgive me if I sounds like a broken record but you should not become root and copy files around like that  :wink: .

-------------------------

