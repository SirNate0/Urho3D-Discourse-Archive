johnnycable | 2017-09-07 08:17:46 UTC | #1

There's an error which still persist on android build of IK.

[ 43%] Building C object Source/ThirdParty/ik/CMakeFiles/ik.dir/src/node.c.o
[ 44%] Building C object Source/ThirdParty/ik/CMakeFiles/ik.dir/src/ordered_vector.c.o
[ 44%] Building C object Source/ThirdParty/ik/CMakeFiles/ik.dir/src/quat.c.o
[ 44%] Building C object Source/ThirdParty/ik/CMakeFiles/ik.dir/src/solver.c.o
[ 44%] Building C object Source/ThirdParty/ik/CMakeFiles/ik.dir/src/solver_1bone.c.o
[ 44%] Building C object Source/ThirdParty/ik/CMakeFiles/ik.dir/src/solver_2bone.c.o
[ 44%] Building C object Source/ThirdParty/ik/CMakeFiles/ik.dir/src/solver_FABRIK.c.o
[ 44%] Building C object Source/ThirdParty/ik/CMakeFiles/ik.dir/src/solver_MSD.c.o
[ 44%] Building C object Source/ThirdParty/ik/CMakeFiles/ik.dir/src/util.c.o
[ 45%] Building C object Source/ThirdParty/ik/CMakeFiles/ik.dir/src/vec3.c.o
[ 45%] Building C object Source/ThirdParty/ik/CMakeFiles/ik.dir/src/platform/linux/backtrace_linux.c.o
/usr/local/Urho/Urho3D-1.7/Source/ThirdParty/ik/src/platform/linux/backtrace_linux.c:2:10: fatal error: 
      'execinfo.h' file not found
#include <execinfo.h>
         ^
1 error generated.
make[3]: *** [Source/ThirdParty/ik/CMakeFiles/ik.dir/src/platform/linux/backtrace_linux.c.o] Error 1
make[2]: *** [Source/ThirdParty/ik/CMakeFiles/ik.dir/all] Error 2
make[1]: *** [Source/Urho3D/CMakeFiles/Urho3D.dir/rule] Error 2
make: *** [Urho3D] Error 2
Done building Debug Library for android in /usr/local/Urho/Urho3D-1.7/build/android/Debug/armeabi-v7a

as already noted by @Pencheff [here](https://discourse.urho3d.io/t/android-studio-2-3-build-with-gradle/2995?u=johnnycable)

I think it takes a guard there... gave me no error while building on Os X... maybe the system "incorrectly" mistake android for linux?

-------------------------

weitjong | 2017-09-07 10:48:27 UTC | #2

If you believe this is a bug then you should report it in the Urho Github issue tracker. Thanks.
Will have a look later regardless.  😄

-------------------------

weitjong | 2017-09-08 12:51:10 UTC | #3

Please check out the latest commit in the master branch. It should fix the debug build configuration for Android platform.

-------------------------

Eugene | 2017-09-07 14:48:08 UTC | #4

Sometimes I think that you are more improtant for Urho than all other contributors taken together. BTW, is it hard to maintain build system?

-------------------------

weitjong | 2017-09-07 23:20:46 UTC | #5

No, not at all. When I started to look at this, I was a CMake newbie as well. The only advantage I have is years of Unix experience for scripting.

-------------------------

johnnycable | 2017-09-08 12:51:04 UTC | #6

Goddammit! It works!

-------------------------

