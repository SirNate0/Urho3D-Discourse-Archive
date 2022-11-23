bmcorser | 2017-03-09 10:58:15 UTC | #1

Hello all,

Having a go at building on a newer Ubuntu. I'm getting a pretty interesting error, but no idea how to interpret it. I also tried building with static libs option enabled, but result was the same.

Make output below:

```
[ 70%] Linking CXX executable ../../../bin/Urho3DPlayer
../../../lib/libUrho3D.a(loslib.c.o): In function `os_tmpname':
loslib.c:(.text+0x21d): warning: the use of `tmpnam' is dangerous, better use `mkstemp'
/usr/bin/ld: ../../../lib/libUrho3D.a(jo_jpeg.cpp.o): relocation R_X86_64_32S against `.rodata' can not be used when making a shared object; recompile with -fPIC
/usr/bin/ld: ../../../lib/libUrho3D.a(hull.cpp.o): relocation R_X86_64_32 against `.rodata.str1.1' can not be used when making a shared object; recompile with -fPIC
/usr/bin/ld: ../../../lib/libUrho3D.a(pugixml.cpp.o): relocation R_X86_64_32 against `.rodata.str1.1' can not be used when making a shared object; recompile with -fPIC
/usr/bin/ld: ../../../lib/libUrho3D.a(lz4.c.o): relocation R_X86_64_PC32 against symbol `memset@@GLIBC_2.2.5' can not be used when making a shared object; recompile with -fPIC
/usr/bin/ld: final link failed: Bad value
collect2: error: ld returned 1 exit status
Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/build.make:95: recipe for target 'bin/Urho3DPlayer' failed
make[2]: *** [bin/Urho3DPlayer] Error 1
CMakeFiles/Makefile2:1547: recipe for target 'Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/all' failed
make[1]: *** [Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/all] Error 2
Makefile:138: recipe for target 'all' failed
make: *** [all] Error 2
```

Cheers,

Ben

-------------------------

slapin | 2017-03-09 16:52:11 UTC | #2

Have you did make clean or removed build directory before building with different configuration?

-------------------------

bmcorser | 2017-03-09 10:58:21 UTC | #3

I ran `make clean && ./cmake_clean.sh` as suggested and the build completed successfully ... thanks @slapin!

-------------------------

