rogerdv | 2017-01-02 00:58:44 UTC | #1

Im trying to compile the engine under Fedora 19. cmake runs detection without reporting critical errors, but when compilation starts I inmediatly get ths error:

[code][  0%] Building CXX object ThirdParty/Box2D/CMakeFiles/Box2D.dir/Box2D/Collision/b2BroadPhase.cpp.o
In file included from /usr/include/features.h:399:0,
                 from /usr/include/assert.h:36,
                 from /home/roger/projects/Urho3D/Source/ThirdParty/Box2D/./Box2D/Common/b2Settings.h:23,
                 from /home/roger/projects/Urho3D/Source/ThirdParty/Box2D/./Box2D/Collision/b2BroadPhase.h:22,
                 from /home/roger/projects/Urho3D/Source/ThirdParty/Box2D/Box2D/Collision/b2BroadPhase.cpp:19:
/usr/include/gnu/stubs.h:7:27: error fatal: gnu/stubs-32.h: No existe el fichero o el directorio
 # include <gnu/stubs-32.h>
                           ^
compilaci?n terminada.
make[2]: *** [ThirdParty/Box2D/CMakeFiles/Box2D.dir/Box2D/Collision/b2BroadPhase.cpp.o] Error 1
make[1]: *** [ThirdParty/Box2D/CMakeFiles/Box2D.dir/all] Error 2
make: *** [all] Error 2
[/code]

gnu/stubs-32.h doesnt exists, so I probably lack some devel files, but cant figure out what is missing. How can I solve this?

-------------------------

cadaver | 2017-01-02 00:58:44 UTC | #2

My guess is that you lack 32-bit development files, so you must trigger a 64-bit build with

./cmake_gcc.sh -DENABLE_64BIT=1

-------------------------

weitjong | 2017-01-02 00:58:44 UTC | #3

If you really want to build 32-bit Urho3D library on a 64-bit Fedora OS then you have to install the corresponding *.i686 variant of the prerequisite packages, including the kernel module (graphic card driver) package for running the app.

-------------------------

rogerdv | 2017-01-02 00:58:44 UTC | #4

Thanks, that solved the problem. But now Im getting this:


[code]In file included from /usr/include/stdlib.h:314:0,
                 from /home/roger/projects/Urho3D/Source/ThirdParty/LibCpuId/src/cpuid_main.c:36:
/usr/include/sys/types.h:197:13: error: tipos en conflicto para ?int64_t?
 __intN_t (64, __DI__);
             ^
In file included from /home/roger/projects/Urho3D/Source/ThirdParty/LibCpuId/src/libcpuid.h:68:0,
                 from /home/roger/projects/Urho3D/Source/ThirdParty/LibCpuId/src/cpuid_main.c:26:
/home/roger/projects/Urho3D/Source/ThirdParty/LibCpuId/src/libcpuid_types.h:55:26: nota: la declaraci?n previa de ?int64_t? estaba aqu?
 typedef signed long long int64_t;
                          ^
make[2]: *** [ThirdParty/LibCpuId/CMakeFiles/LibCpuId.dir/src/cpuid_main.c.o] Error 1
make[1]: *** [ThirdParty/LibCpuId/CMakeFiles/LibCpuId.dir/all] Error 2
make: *** [all] Error 2
[/code]

Seems there are some type conflict, int64_t was already declared.

-------------------------

weitjong | 2017-01-02 00:58:45 UTC | #5

This is strange. Have you cleared the CMake cache when changing the build option? You need to do that if you are changing critical build option. Either that, nuke your existing build directory and invoke the cmake script to recreate it from scratch again. Also make sure "glibc-headers.x86_64" package is installed in your system.

-------------------------

weitjong | 2017-01-02 00:58:45 UTC | #6

After the commit 46285baf975d0ddddbe98423de5a092c6fa6e34c on April 5th, the build option for 64-bit build becomes "URHO3D_64BIT" instead of "ENABLE_64BIT".

-------------------------

