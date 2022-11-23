Serge | 2017-01-02 00:59:14 UTC | #1

Hello, just downloaded Urho3D via git and trying to compile. My OS is Ubuntu 14.04 64bit. All dev packages installed. The problem is:
[code]
...
Scanning dependencies of target LibCpuId
[ 53%] Building C object ThirdParty/LibCpuId/CMakeFiles/LibCpuId.dir/src/asm-bits.c.o
[ 53%] Building C object ThirdParty/LibCpuId/CMakeFiles/LibCpuId.dir/src/libcpuid_util.c.o
In file included from /home/serge/tmp/Urho3D/Source/ThirdParty/LibCpuId/src/libcpuid.h:68:0,
                 from /home/serge/tmp/Urho3D/Source/ThirdParty/LibCpuId/src/libcpuid_util.c:32:
/home/serge/tmp/Urho3D/Source/ThirdParty/LibCpuId/src/libcpuid_types.h:55:26: error: conflicting types for ?int64_t?
 typedef signed long long int64_t;
                          ^
In file included from /usr/include/stdlib.h:314:0,
                 from /home/serge/tmp/Urho3D/Source/ThirdParty/LibCpuId/src/libcpuid_util.c:28:
/usr/include/x86_64-linux-gnu/sys/types.h:197:1: note: previous declaration of ?int64_t? was here
 __intN_t (64, __DI__);
 ^
make[2]: *** [ThirdParty/LibCpuId/CMakeFiles/LibCpuId.dir/src/libcpuid_util.c.o] Error 1
make[1]: *** [ThirdParty/LibCpuId/CMakeFiles/LibCpuId.dir/all] Error 2
make: *** [all] Error 2

[/code]

-------------------------

friesencr | 2017-01-02 00:59:14 UTC | #2

Are you using the -DURHO3D_64BIT=1 cmake flag?  If you don't you have to setup ubuntu for multiarch which i don't know much about.

-------------------------

Serge | 2017-01-02 00:59:14 UTC | #3

[quote="friesencr"]Are you using the -DURHO3D_64BIT=1 cmake flag?  If you don't you have to setup ubuntu for multiarch which i don't know much about.[/quote]
Yes, I use this flag and have this error with it. Temporary I commented out that line in third party library and compile engine. But I 'm not sure is this correct?

-------------------------

friesencr | 2017-01-02 00:59:14 UTC | #4

Someone did have this problem already:

[github.com/urho3d/Urho3D/issues/297](https://github.com/urho3d/Urho3D/issues/297)

-------------------------

cadaver | 2017-01-02 00:59:14 UTC | #5

I couldn't reproduce the error myself by installing a 64bit Ubuntu 14.04 into VirtualBox. It's an OK workaround to comment the offending line, as int64_t is already defined.

-------------------------

Serge | 2017-01-02 00:59:15 UTC | #6

[quote="cadaver"]I couldn't reproduce the error myself by installing a 64bit Ubuntu 14.04 into VirtualBox. It's an OK workaround to comment the offending line, as int64_t is already defined.[/quote]
Ok, thank you

-------------------------

AGreatFish | 2017-01-02 00:59:15 UTC | #7

I can add that I am on Ubuntu 14.04 64bit, as well, and I have no issues when compiling directly from git master.

Weird.

-------------------------

