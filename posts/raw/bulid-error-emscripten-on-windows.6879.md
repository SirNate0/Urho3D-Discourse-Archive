huminzheng | 2021-06-07 10:16:28 UTC | #1

Emscripten on Windows
Hi guys,
I want to build Urho3D with emscripten on windows, but I have some troubles. Pls give me some advise.

The build detals as follows:
1.Install emsdk 2.0.8
2.Install mingw by MinGW Installer
3.run emcmdprompt.bat
4.Build tree  D:\Urho3D>script\cmake_emscripten.bat d:\web01 -D URHO3D_LUA=0 -D URHO3D_PACKAGING=0
5.D:\Urho3D>cd ../web01
  D:\web01>emmake make
  
Error as follows：

D:\Urho3D\Source\Urho3D\Core\ProcessUtils.cpp: In function 'void Urho3D::PrintUnicode(const Urho3D::String&, bool)':
D:\Urho3D\Source\Urho3D\Core\ProcessUtils.cpp:224:29: error: '_fileno' was not declared in this scope
     if (!_isatty(_fileno(out)))
                             ^
CMakeFiles\PackageTool.dir\build.make:225: recipe for target 'CMakeFiles/PackageTool.dir/D_/Urho3D/Source/Urho3D/Core/ProcessUtils.cpp.obj' failed
mingw32-make[5]: *** [CMakeFiles/PackageTool.dir/D_/Urho3D/Source/Urho3D/Core/ProcessUtils.cpp.obj] Error 1
CMakeFiles\Makefile2:117: recipe for target 'CMakeFiles/PackageTool.dir/all' failed
mingw32-make[4]: *** [CMakeFiles/PackageTool.dir/all] Error 2
Makefile:134: recipe for target 'all' failed
mingw32-make[3]: *** [all] Error 2
Source\Tools\CMakeFiles\PackageTool.dir\build.make:84: recipe for target 'Source/Tools/PackageTool-prefix/src/PackageTool-stamp/PackageTool-build' failed
mingw32-make[2]: *** [Source/Tools/PackageTool-prefix/src/PackageTool-stamp/PackageTool-build] Error 2
CMakeFiles\Makefile2:1988: recipe for target 'Source/Tools/CMakeFiles/PackageTool.dir/all' failed
mingw32-make[1]: *** [Source/Tools/CMakeFiles/PackageTool.dir/all] Error 2
Makefile:154: recipe for target 'all' failed
mingw32-make: *** [all] Error 2

-------------------------

huminzheng | 2021-06-07 10:15:46 UTC | #2

-- Build files have been written to: D:/web01/Source/Tools/PackageTool-prefix/src/PackageTool-build
[ 89%] Performing build step for 'PackageTool'
[  2%] Building C object host/LibCpuId/CMakeFiles/LibCpuId.dir/src/asm-bits.c.obj
[  4%] Building C object host/LibCpuId/CMakeFiles/LibCpuId.dir/src/cpuid_main.c.obj
[  6%] Building C object host/LibCpuId/CMakeFiles/LibCpuId.dir/src/libcpuid_util.c.obj
[  8%] Building C object host/LibCpuId/CMakeFiles/LibCpuId.dir/src/msrdriver.c.obj
[ 10%] Building C object host/LibCpuId/CMakeFiles/LibCpuId.dir/src/rdmsr.c.obj
[ 12%] Building C object host/LibCpuId/CMakeFiles/LibCpuId.dir/src/rdtsc.c.obj
[ 14%] Building C object host/LibCpuId/CMakeFiles/LibCpuId.dir/src/recog_amd.c.obj
[ 16%] Building C object host/LibCpuId/CMakeFiles/LibCpuId.dir/src/recog_intel.c.obj
[ 18%] Linking C static library libLibCpuId.a
[ 18%] Built target LibCpuId
[ 20%] Building C object host/LZ4/CMakeFiles/LZ4.dir/lz4.c.obj
[ 22%] Building C object host/LZ4/CMakeFiles/LZ4.dir/lz4hc.c.obj
[ 25%] Linking C static library libLZ4.a
[ 25%] Built target LZ4
[ 27%] Building CXX object CMakeFiles/PackageTool.dir/PackageTool.cpp.obj
[ 29%] Building CXX object CMakeFiles/PackageTool.dir/D_/Urho3D/Source/Urho3D/Container/Allocator.cpp.obj
[ 31%] Building CXX object CMakeFiles/PackageTool.dir/D_/Urho3D/Source/Urho3D/Container/HashBase.cpp.obj
[ 33%] Building CXX object CMakeFiles/PackageTool.dir/D_/Urho3D/Source/Urho3D/Container/RefCounted.cpp.obj
[ 35%] Building CXX object CMakeFiles/PackageTool.dir/D_/Urho3D/Source/Urho3D/Container/Str.cpp.obj
[ 37%] Building CXX object CMakeFiles/PackageTool.dir/D_/Urho3D/Source/Urho3D/Container/VectorBase.cpp.obj
[ 39%] Building CXX object CMakeFiles/PackageTool.dir/D_/Urho3D/Source/Urho3D/Core/Context.cpp.obj
[ 41%] Building CXX object CMakeFiles/PackageTool.dir/D_/Urho3D/Source/Urho3D/Core/EventProfiler.cpp.obj
[ 43%] Building CXX object CMakeFiles/PackageTool.dir/D_/Urho3D/Source/Urho3D/Core/Mutex.cpp.obj
[ 45%] Building CXX object CMakeFiles/PackageTool.dir/D_/Urho3D/Source/Urho3D/Core/Object.cpp.obj
[ 47%] Building CXX object CMakeFiles/PackageTool.dir/D_/Urho3D/Source/Urho3D/Core/ProcessUtils.cpp.obj
D:\Urho3D\Source\Urho3D\Core\ProcessUtils.cpp: In function 'void Urho3D::PrintUnicode(const Urho3D::String&, bool)':
D:\Urho3D\Source\Urho3D\Core\ProcessUtils.cpp:224:29: error: '_fileno' was not declared in this scope
     if (!_isatty(_fileno(out)))
                             ^
CMakeFiles\PackageTool.dir\build.make:225: recipe for target 'CMakeFiles/PackageTool.dir/D_/Urho3D/Source/Urho3D/Core/ProcessUtils.cpp.obj' failed
mingw32-make[5]: *** [CMakeFiles/PackageTool.dir/D_/Urho3D/Source/Urho3D/Core/ProcessUtils.cpp.obj] Error 1
CMakeFiles\Makefile2:117: recipe for target 'CMakeFiles/PackageTool.dir/all' failed
mingw32-make[4]: *** [CMakeFiles/PackageTool.dir/all] Error 2
Makefile:134: recipe for target 'all' failed
mingw32-make[3]: *** [all] Error 2
Source\Tools\CMakeFiles\PackageTool.dir\build.make:84: recipe for target 'Source/Tools/PackageTool-prefix/src/PackageTool-stamp/PackageTool-build' failed
mingw32-make[2]: *** [Source/Tools/PackageTool-prefix/src/PackageTool-stamp/PackageTool-build] Error 2
CMakeFiles\Makefile2:1988: recipe for target 'Source/Tools/CMakeFiles/PackageTool.dir/all' failed
mingw32-make[1]: *** [Source/Tools/CMakeFiles/PackageTool.dir/all] Error 2
Makefile:154: recipe for target 'all' failed
mingw32-make: *** [all] Error 2

-------------------------

SirNate0 | 2021-06-07 10:35:52 UTC | #3

What version of mingw are you using?

-------------------------

huminzheng | 2021-06-07 10:40:44 UTC | #4

C:\Users\pc>gcc -v
 specs
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=c:/mingw/bin/../libexec/gcc/mingw32/6.3.0/lto-wrapper.exe
mingw32
../src/gcc-6.3.0/configure --build=x86_64-pc-linux-gnu --host=mingw32 --target=mingw32 --with-gmp=/mingw --with-mpfr --with-mpc=/mingw --with-isl=/mingw --prefix=/mingw --disable-win32-registry --with-arch=i586 --with-tune=generic --enable-languages=c,c++,objc,obj-c++,fortran,ada --with-pkgversion='MinGW.org GCC-6.3.0-1' --enable-static --enable-shared --enable-threads --with-dwarf2 --disable-sjlj-exceptions --enable-version-specific-runtime-libs --with-libiconv-prefix=/mingw --with-libintl-prefix=/mingw --enable-libstdcxx-debug --enable-libgomp --disable-libvtv --enable-nls
win32
gcc  6.3.0 (MinGW.org GCC-6.3.0-1)

-------------------------

SirNate0 | 2021-06-07 11:12:00 UTC | #5

Try using mingw-w64, I think there are some problems using the other version in building Urho.

-------------------------

huminzheng | 2021-06-09 02:54:09 UTC | #6

Hi,   now I have met  errors as follows, Probably what's the reason？

Install the project...
-- Install configuration: "Release"
-- Installing: D:/w00/bin/tool/PackageTool.exe
[ 87%] Completed 'PackageTool'
[ 87%] Built target PackageTool
[ 87%] Checking and packaging resource directories
Packaging D:/Urho3D-1.7/bin/CoreData...
Packaging D:/Urho3D-1.7/bin/Data...
[ 87%] Built target RESOURCE_CHECK
[ 87%] Generating shared data file -s FORCE_FILESYS
Remember to build the main file with TEM=1  so that it includes support for loading this file package
[ 87%] Building CXX object Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/Urho3DPlayer.cpp.o
[ 87%] Linking CXX executable ..\..\..\bin\Urho3DPlayer.html
parseTools.js preprocessor error in shell.html:1: "#!/usr/bin/env firefox"!

undefined:102
      throw e;
      ^
Unclear preprocessor command on line 0: #!/usr/bin/env firefox
(Use `node --trace-uncaught ...` to show where the exception was thrown)
em++: error: 'D:/emsdk/node/14.15.5_64bit/bin/node.exe D:\emsdk\upstream\emscripten\tools/preprocessor.js C:\Users\pc\AppData\Local\Temp\emscripten_temp_0rieuf5p\settings.js shell.html' failed (1)
Source\Tools\Urho3DPlayer\CMakeFiles\Urho3DPlayer.dir\build.make:107: recipe for target 'bin/Urho3DPlayer.html' failed
mingw32-make[2]: *** [bin/Urho3DPlayer.html] Error 1
CMakeFiles\Makefile2:2008: recipe for target 'Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/all' failed
mingw32-make[1]: *** [Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/all] Error 2
Makefile:164: recipe for target 'all' failed
mingw32-make: *** [all] Error 2

-------------------------

weitjong | 2021-06-09 03:17:35 UTC | #7

It seems you still have the old “shell” html file. Remove the shebang line as the newer Emscripten toolchain has a “#” preprocessor that doesn’t understand age-old shebang concept.

-------------------------

huminzheng | 2021-06-09 03:37:17 UTC | #8

Hi,weitjong! Thanks for you reply!  What EMSDK version is right for Urho3D-1.7?

-------------------------

weitjong | 2021-06-09 03:50:13 UTC | #9

Seriously you are better of with current master branch. I am not sure I could answer that question anymore from the top of my head.

-------------------------

huminzheng | 2021-06-09 04:47:05 UTC | #10

Atfter remove the shebang line in shell.html file，I  bulid the Urho3D successfully. But still have an error as follows.
![image|690x244](upload://wjWWkntALgTIH9fKyrjoRjoUYYd.png)

-------------------------

weitjong | 2021-06-09 06:08:34 UTC | #11

It has been awhile for me to work with Urho3D build system. Just back from a long break. So, I am not able to give you answer for every possible build errors out there. Having said that, I can provide you with one good advise. Use the master branch to build from the source and use the same EMSDK version that currently being used by our CI/CD. See this build log from https://github.com/urho3d/Urho3D/runs/2775102327?check_suite_focus=true, click on the "CMake" step to expand it to see the detail. You can of course use EMSDK with higher version than what shown there, but from the past experience EMSDK developers do not have a very good track record of keeping the backward compatibility.

Ideally, once you get a version that works for you then you can try to bump the EMSDK version up again to break the build and help us to fix the root cause and submit it as PR.

-------------------------

huminzheng | 2021-06-15 03:13:45 UTC | #12

Hi, weitjong
Thanks for your help! I have already bulid the Urho3D successfully with emscripten on windows10.   But I want to use the lib as shared type. How can I change the lib type to shared?

-------------------------

weitjong | 2021-06-15 04:04:34 UTC | #13

Glad to hear that. Normally you would just pass the build option `URHO3D_LIB_TYPE=SHARED` to the build system, however, EMCC with WASM does not really support the notion of shared lib type yet. So that build option is not available for Web platform, I believe.

-------------------------

huminzheng | 2021-06-17 04:52:01 UTC | #14

Hi, weitjong
   Thanks for your help!   I build the urho3d with emsdk -2.0.8. Now I want to use the libUrho3D.a in Qt project, and then I build the Qt project  to  wasm，but the Qt must use emsdk-1.38.9 . Such two emsdk version is different. How could I to handle this problem ?   Thanks !

-------------------------

huminzheng | 2021-06-17 05:05:52 UTC | #15

When I bulid the Urho3D project and the Sample Projetcts,  the Urho3D projet  only use MingW to bulid  to libUrho3D.a and not use emscripten tools . The sample projects use the mingw and the emscripten t build to wasm. Do I understand correctly? Thanks !

-------------------------

weitjong | 2021-06-17 07:25:35 UTC | #16

Different EMDSK with different major numbers is not really a good idea. Like I mentioned before, those guys even breaking the build on minor version changes. I am not fan of Qt so no comments on anything related to Qt.

When cross-compiling on Windows host system, we just use the MinGW to build host-tools on the fly. The rest of the code are still compiled using the cross-compiling toolchain, in this case EMCC.

-------------------------

huminzheng | 2021-06-28 08:31:04 UTC | #17

Hi，weitjong
 When I use the httpRequest,there is some build error. How could I to handle this problem ? Thanks !

error: undefined symbol: _ZN6Urho3D7Network15MakeHttpRequestERKNS_6StringES3_RKNS_6VectorIS1_EES3_ (referenced by top-level compiled C/C++ code)
warning: Link with `-s LLD_REPORT_UNDEFINED` to get more information on undefined symbols
warning: To disable errors for undefined symbols use `-s ERROR_ON_UNDEFINED_SYMBOLS=0`
warning: __ZN6Urho3D7Network15MakeHttpRequestERKNS_6StringES3_RKNS_6VectorIS1_EES3_ may need to be added to EXPORTED_FUNCTIONS if it arrives from a system library
error: undefined symbol: _ZNK6Urho3D11HttpRequest16GetAvailableSizeEv (referenced by top-level compiled C/C++ code)
warning: __ZNK6Urho3D11HttpRequest16GetAvailableSizeEv may need to be added to EXPORTED_FUNCTIONS if it arrives from a system library
error: undefined symbol: _ZNK6Urho3D11HttpRequest8GetStateEv (referenced by top-level compiled C/C++ code)
warning: __ZNK6Urho3D11HttpRequest8GetStateEv may need to be added to EXPORTED_FUNCTIONS if it arrives from a system library
Error: Aborting compilation due to previous errors
em++: error: 'D:/emsdk/node/14.15.5_64bit/bin/node.exe D:\emsdk\upstream\emscripten\src\compiler.js C:\Users\pc\AppData\Local\Temp\tmppgqrv48i.txt' failed (1)
mingw32-make[2]: *** [Source\Samples\00_Aphro3DWeb\CMakeFiles\00_Aphro3DWeb.dir\build.make:1060: bin/00_Aphro3DWeb.html] Error 1
mingw32-make[1]: *** [CMakeFiles\Makefile2:1234: Source/Samples/00_Aphro3DWeb/CMakeFiles/00_Aphro3DWeb.dir/all] Error 2
mingw32-make: *** [makefile:165: all] Error 2

-------------------------

JTippetts1 | 2021-06-28 11:17:58 UTC | #18

URHO3D_NETWORK option is disabled for Web builds, so HttpRequest doesn't get built.

-------------------------

huminzheng | 2021-06-28 11:49:44 UTC | #19

Thank you for you reply. The build command as follows ,but still have error.
D:\Web>script\cmake_emscripten.bat d:\Web\build -D URHO3D_TESTING=1 -D EMSCRIPTEN_SHARE_DATA=1 -D URHO3D_NETWORK=1
error: undefined symbol: _ZN6Urho3D7Network15MakeHttpRequestERKNS_6StringES3_RKNS_6VectorIS1_EES3_ (referenced by top-level compiled C/C++ code)
warning: Link with `-s LLD_REPORT_UNDEFINED` to get more information on undefined symbols
warning: To disable errors for undefined symbols use `-s ERROR_ON_UNDEFINED_SYMBOLS=0`
warning: __ZN6Urho3D7Network15MakeHttpRequestERKNS_6StringES3_RKNS_6VectorIS1_EES3_ may need to be added to EXPORTED_FUNCTIONS if it arrives from a system library
error: undefined symbol: _ZNK6Urho3D11HttpRequest16GetAvailableSizeEv (referenced by top-level compiled C/C++ code)
warning: __ZNK6Urho3D11HttpRequest16GetAvailableSizeEv may need to be added to EXPORTED_FUNCTIONS if it arrives from a system library
error: undefined symbol: _ZNK6Urho3D11HttpRequest8GetStateEv (referenced by top-level compiled C/C++ code)
warning: __ZNK6Urho3D11HttpRequest8GetStateEv may need to be added to EXPORTED_FUNCTIONS if it arrives from a system library
Error: Aborting compilation due to previous errors
em++: error: 'D:/emsdk/node/14.15.5_64bit/bin/node.exe D:\emsdk\upstream\emscripten\src\compiler.js C:\Users\pc\AppData\Local\Temp\tmp8qltnlgy.txt' failed (1)
mingw32-make[2]: *** [Source\Samples\00_Aphro3DWeb\CMakeFiles\00_Aphro3DWeb.dir\build.make:1060: bin/00_Aphro3DWeb.html] Error 1
mingw32-make[1]: *** [CMakeFiles\Makefile2:1234: Source/Samples/00_Aphro3DWeb/CMakeFiles/00_Aphro3DWeb.dir/all] Error 2
mingw32-make: *** [makefile:165: all] Error 2

-------------------------

weitjong | 2021-06-28 16:25:56 UTC | #20

AFAIK, our Web platform does not support networking yet. The `URHO3D_NETWORK` build option is basically NOT an available option at all when targeting Web platform. But I recall there is an unfinished work from @Miegamicis that attempted to bring in the network support for Web platform using Websocket library. He was the maintainer for the networking subsystem before but he has already left the project. I am not sure whether he still actively working on that on his own.

@Miegamicis Do you still have that dev branch locally? Could you help to push it to remote branch again if you still have it.

-------------------------

Miegamicis | 2021-06-28 17:22:39 UTC | #21

No, I haven't worked on it since December. What happened to the WebSockets branch? Did I get accidentally deleted? It contained already working WebSocket implementation + there was full support for the HTTP/HTTPS requests for the WEB. My laptop died with everything in it a while ago so I don't have a copy with it right away but I think I have it on another workstation. :thinking:

-------------------------

weitjong | 2021-06-28 17:36:54 UTC | #22

May be I did. I removed some of the stale branches a few weeks ago. Thinking all the recent but stale branches should have been merged to master branch already, especially those with the CI suffix. Anyway, I also have them in my local workstation too, until my next local prune that is. So, what stopping you from making it as PR back then? Still not ready or just other reason? 😉

-------------------------

Miegamicis | 2021-06-28 17:45:29 UTC | #23

I wasn't quite happy with the code quality back then to issue a PR. Technically everything worked just fine but of course there might be some bugs lurking around, but nothing critical afaik. 
On the top of my head I do remember one thing that I wanted to refactor (but didn't) - the way how the incoming/outgoing packets are stored in memory since the current implementation allowed unlimited memory consumption but maybe I added some limitations there idk, it's been a while since I looked at it.

-------------------------

Eugene | 2021-06-28 18:26:33 UTC | #24

[quote="Miegamicis, post:21, topic:6879"]
What happened to the WebSockets branch?
[/quote]
If I'm not mistaken, I have this branch locally.
Pushed it remotely just it case:
 https://github.com/urho3d/Urho3D/tree/websockets-implementation

I would really like to have networking in Web, it's the last thing needed for true platform parity.

-------------------------

