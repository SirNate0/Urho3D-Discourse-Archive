ghidra | 2017-01-02 01:00:03 UTC | #1

I normally use linux and dont have these issues. But I am trying to build on windows for whatever reason.
What I've done so far, is run cmake_mingw.bat
then i've installed cingw files with make. And run make in the build directory

I immediatly get this error:

[code]
[  0%] Building CXX object ThirdParty/Box2D/CMakeFiles/Box2D.dir/Box2D/Collision
/b2BroadPhase.cpp.obj
G__~1.EXE: error: unrecognized command line option '-static-libstdc++'
ThirdParty\Box2D\CMakeFiles\Box2D.dir\build.make:54: recipe for target 'ThirdPar
ty/Box2D/CMakeFiles/Box2D.dir/Box2D/Collision/b2BroadPhase.cpp.obj' failed
make[2]: *** [ThirdParty/Box2D/CMakeFiles/Box2D.dir/Box2D/Collision/b2BroadPhase
.cpp.obj] Error 1
CMakeFiles\Makefile2:74: recipe for target 'ThirdParty/Box2D/CMakeFiles/Box2D.di
r/all' failed
make[1]: *** [ThirdParty/Box2D/CMakeFiles/Box2D.dir/all] Error 2
Makefile:136: recipe for target 'all' failed
make: *** [all] Error 2
[/code]

google is telling me to modify the makefile basically. But I wanted to consult the forums first. Maybe I am just missing something in mingw

-------------------------

weitjong | 2017-01-02 01:00:04 UTC | #2

cingw? Is that a typo? Anyway, we only support MinGW-W64. Only this variant of MinGW is being tested everyday on our CI build on a Linux build system. I have not booted into my Windows partition in months now so I have not built Urho3D there for a while but I reckon MinGW-W64 would also work well with Urho3D on a Windows build system.

-------------------------

cadaver | 2017-01-02 01:00:04 UTC | #3

It looks like you have so old MinGW that it doesn't recognize the options that current MinGW's need to avoid depending on GCC runtime dll's.

You will find those options on line 290 of Source/CMake/Modules/Urho3D-CMake-common.cmake and could try removing them, but the recommended course of action is to update to the latest MinGW-W64.

-------------------------

ghidra | 2017-01-02 01:00:04 UTC | #4

Totally a typo. I mean MingW.
I think i downloaded the latest, but still getting that error. I'll investigate further. Thank you.

-------------------------

friesencr | 2017-01-02 01:00:04 UTC | #5

Something that isn't clear is that mingw kind of forked a couple years ago.  The new stuff is the w64.

[mingw-w64.sourceforge.net/](http://mingw-w64.sourceforge.net/)

Both of them have terrible websites.

-------------------------

ghidra | 2017-01-02 01:00:04 UTC | #6

yup, that what I got, and still same error...
the gcc version is 4.9.1 make version 4.0.90
i tried the i686 version and the x86_64, i've tried serveral combinations... maybe i should just opt to find a visual studio download.

-------------------------

Mike | 2017-01-02 01:00:05 UTC | #7

You can also try with the MinGW version shipped with Code::Blocks :
[url]http://tdm-gcc.tdragon.net/[/url]

-------------------------

weitjong | 2017-01-02 01:00:05 UTC | #8

I have just successfully built Urho3D library, its tools and samples on 64-bit Win7 build system. The build system itself is a guest virtual machine but I don't see it would make any difference. Here is how I did it.

1. Uninstall all existing MinGW installation. Making sure PATH environment variable does not point to any old MinGW version.
2. Install MinGW-W64 from [mingw-w64.sourceforge.net/download.php](http://mingw-w64.sourceforge.net/download.php). I chose Mingw-builds project instead of Win-builds project because I don't intend to cross-compile on my virtual Win7 to other target platforms. I chose x86_64, POSIX, and SEH as installation option (default).
3. Open a DOS terminal, ensure the PATH environment variable is set to point to the newly installed MinGW-W64 binaries. For my case, it is: set PATH=C:\Program Files\mingw-w64\x86_64-4.9.1-posix-seh-rt_v3-rev0\mingw64\bin;%PATH%
4. Execute cmake_mingw.bat with -DURHO3D_64BIT=1. I also enable LUAJIT and SAMPLES build options.
5. Then finally, make -j4. I use 'make' command that I got from msysgit (I think), but I believe the 'mingw32-make' provided by Mingw-builds project should also do the job well.

I did not encounter the build issue you reported in the first post. Anyway, thanks for the incentive to get me upgrading my MinGW toolchain on my VM. :slight_smile:

-------------------------

jmiller | 2017-01-02 01:00:05 UTC | #9

I currently build Urho3D lib/samples/tools/docs with [b]dongsheng[/b] daily mingw-w64 builds ([mingw-w64.sourceforge.net](http://mingw-w64.sourceforge.net) at the bottom). I've only yet tried the one targeting win32. Can extract the package, name it mingw, and add c:\mingw\bin to PATH.
Currently gcc-4.9.2 and make 4.0.

I also use Msys (bash/GNU in MS Windows is a godsend as well as GCC). In case anyone else has CMake complain about 'sh.exe' being in your path (even when it's not): I finally hacked CMake/share/modules/CMakeMinGWFindMake.cmake to stop its complaining. I have msys\bin after other mingw in PATH.

-------------------------

ghidra | 2017-01-02 01:00:05 UTC | #10

I thank everyone for being so helpful.
But at the risk of dragging this on, i'm getting no where. Its not a big deal, I have urho built and working on my linux box, I was just trying to get something built on my windows workstation. Just, well to have it and as a learning process. And I've learned that I dont like windows anymore than I did yesterday.
First of all, I am no programmer, so i get lost fairly easily with tracking down what could cause the issues here. I followed your steps exactly weitjong, and same error. (just to add, I had to install cmake too) Maybe I need to start fresh.

It would be cool, to have a bat that made a codeblocks project. the sh file errors on my windows machine. Maybe that would keep some of the tail chasing to a minimum.

-------------------------

rasteron | 2017-01-02 01:00:05 UTC | #11

Hi ghidra,

Building on windows with Mingw32 or CodeBlocks is pretty simple. I guess it is the same steps with Linux. I have a Win7 64 system and I could test this again if you need more confirmation from other users..

-------------------------

ghidra | 2017-01-02 01:00:07 UTC | #12

well, i managed to get it to compile.
I ended up redownloading the source, then running cmake_mingw.bat with the -DURHO3D_64BIT=1.
Honestly I think that i forgot to do that the whole time, the 64 bit flag. Being as I am on Windows7 64 bit. All is well now. Thank you for your help everyone.

-------------------------

jmiller | 2017-01-02 01:00:07 UTC | #13

Glad you got it working.
If there had been a "wtf" with MSWindows, it would not have been the first time :slight_smile:
(and just fyi, I can build 32-bit on 64-bit because this mingw targets it)

-------------------------

