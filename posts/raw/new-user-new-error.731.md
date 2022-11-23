Dimon | 2017-01-02 01:02:31 UTC | #1

Hi folks,

I'm new here and thanks for the great engine. I'm trying to compile it for MinGW via:

[code]mkdir build
cd build
cmake -G"MinGW Makefiles" ..
make -j4[/code]

And getting this error:

[code]
                 from C:\data\src\libs\Urho3D\repo\Source\Urho3D\Audio\Audio.cpp
:23:
C:/data/src/libs/Urho3D/repo/Source/Urho3D/Container/../Container/HashBase.h:25:
23: fatal error: ../Urho3D.h: No such file or directory
 #include "../Urho3D.h"                       ^
compilation terminated.[/code]

I'm sure i'm missing something trivial, but after 4 hours looking and trying things I can't make it on my own.
Compiling as suggested in documentation doesn't work for me either, producing the same error:

[code]cmake_mingw.bat build
cd build
mingw32-make -j4[/code]

Cmake generation goes without errors.

Thanks,
Dimon.


[b]An update:
[/b]
This is produces build without errors:
cmake_mingw.bat build -DURHO3D_SAMPLES=1 -DURHO3D_LUA=1

This is produces build with errors:
cmake_mingw.bat build -DURHO3D_SAMPLES=1

-------------------------

weitjong | 2017-01-02 01:02:31 UTC | #2

Welcome to our forum.

Thanks for reporting the problem. It has been fixed in the master branch.

-------------------------

