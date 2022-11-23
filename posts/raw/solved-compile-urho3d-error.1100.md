hsl9999 | 2017-01-02 01:05:27 UTC | #1

env:win7 64
urho3d 1.4  emscripten
cmake 3.2.2
mingw: x86_64-5.1.0-posix-seh-rt_v4-rev0 

cmd : mingw32-make

error log:

D:/PROGRA~2/MINGW-~1/X86_64~1.0-P/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/5.1.
0/../../../../x86_64-w64-mingw32/bin/ld.exe: skipping incompatible D:/PROGRA~2/M
INGW-~1/X86_64~1.0-P/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/5.1.0\libgcc.a wh
en searching for -lgcc
D:/PROGRA~2/MINGW-~1/X86_64~1.0-P/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/5.1.
0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lgcc
D:/PROGRA~2/MINGW-~1/X86_64~1.0-P/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/5.1.
0/../../../../x86_64-w64-mingw32/bin/ld.exe: skipping incompatible D:/PROGRA~2/M
INGW-~1/X86_64~1.0-P/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/5.1.0\libgcc_eh.a
 when searching for -lgcc_eh
D:/PROGRA~2/MINGW-~1/X86_64~1.0-P/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/5.1.
0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lgcc_eh
D:/PROGRA~2/MINGW-~1/X86_64~1.0-P/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/5.1.
0/../../../../x86_64-w64-mingw32/bin/ld.exe: skipping incompatible D:/PROGRA~2/M
INGW-~1/X86_64~1.0-P/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/5.1.0/../../../..
/x86_64-w64-mingw32/lib\libmoldname.a when searching for -lmoldname
D:/PROGRA~2/MINGW-~1/X86_64~1.0-P/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/5.1.
0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lmoldname
D:/PROGRA~2/MINGW-~1/X86_64~1.0-P/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/5.1.
0/../../../../x86_64-w64-mingw32/bin/ld.exe: skipping incompatible D:/PROGRA~2/M
INGW-~1/X86_64~1.0-P/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/5.1.0/../../../..
/x86_64-w64-mingw32/lib\libmingwex.a when searching for -lmingwex
D:/PROGRA~2/MINGW-~1/X86_64~1.0-P/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/5.1.
0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lmingwex
D:/PROGRA~2/MINGW-~1/X86_64~1.0-P/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/5.1.
0/../../../../x86_64-w64-mingw32/bin/ld.exe: skipping incompatible D:/PROGRA~2/M
INGW-~1/X86_64~1.0-P/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/5.1.0/../../../..
/x86_64-w64-mingw32/lib\libmsvcrt.a when searching for -lmsvcrt
D:/PROGRA~2/MINGW-~1/X86_64~1.0-P/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/5.1.
0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lmsvcrt
collect2.exe: error: ld returned 1 exit status
CMakeFiles\PackageTool.dir\build.make:896: recipe for target 'bin/PackageTool.ex
e' failed
mingw32-make[5]: *** [bin/PackageTool.exe] Error 1
CMakeFiles\Makefile2:61: recipe for target 'CMakeFiles/PackageTool.dir/all' fail
ed
mingw32-make[4]: *** [CMakeFiles/PackageTool.dir/all] Error 2
makefile:115: recipe for target 'all' failed
mingw32-make[3]: *** [all] Error 2
Source\Tools\CMakeFiles\PackageTool.dir\build.make:107: recipe for target 'Sourc
e/Tools/PackageTool-prefix/src/PackageTool-stamp/PackageTool-build' failed
mingw32-make[2]: *** [Source/Tools/PackageTool-prefix/src/PackageTool-stamp/Pack
ageTool-build] Error 2
CMakeFiles\Makefile2:900: recipe for target 'Source/Tools/CMakeFiles/PackageTool
.dir/all' failed
mingw32-make[1]: *** [Source/Tools/CMakeFiles/PackageTool.dir/all] Error 2
makefile:135: recipe for target 'all' failed
mingw32-make: *** [all] Error 2


anybody help me!thanks.

-------------------------

weitjong | 2017-01-02 01:05:27 UTC | #2

Something wrong with your MnGW-W64 installation but I cannot say for sure what. Try to build Urho3D natively first using MingW-W64 toolchain to verify your MingW-W64 toolchain is OK before proceeding to do cross-compiling with Emscripten. Sorry for not being more helpful.

-------------------------

hsl9999 | 2017-01-02 01:05:28 UTC | #3

My apology,is my mistake lead to the problems.Thank you for your patience reply

-------------------------

