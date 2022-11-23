Bluemoon | 2017-01-02 00:59:56 UTC | #1

I have a MinGW-w64 Urho3D build. All included samples run well without issue, both the C++ executable and the script files. But I encountered a problem while trying to use physics in the Editor.
On opening the Editor, I created a simple plane from the included plane model, scaled it considerably, added a rigid body and a static plane collision shape. Next I added a box with a rigid body with a mass of 1.0 and a box collision shape. This box was raised up so as to fall on the plane when the RunUpdatePlay button is pressed. Now when the RunUpdatePlay button is pressed, the box falls, but when it makes contact with the plane, the Urho3DPlayer crashes, but if the box's rigid body mass is set to 0.0 and the scene played, there is no crash.
I even tried opening the scene I saved from the Sample physics test that comes with urho3D, but as I play the scene Urho3DPlayer equally crashes. Why i believe this is a MinGW-w64 problem is the fact that I already have and use a Visual C++ build of Urho3D, and non of these crashes occur. I even tried loading the scene from the Sample physics test with the same Editor script but run by the two different build of Urho3DPlayer, but that built with MinGW-w64 still crashed.

Below is my MinGW-w64 version info 

[code]
Using built-in specs.
COLLECT_GCC=g++
COLLECT_LTO_WRAPPER=C:/MinGW-w64/mingw32/bin/../libexec/gcc/i686-w64-mingw32/4.9.1/lto-wrapper.exe
Target: i686-w64-mingw32
Configured with: ../../../src/gcc-4.9.1/configure --host=i686-w64-mingw32 --build=i686-w64-mingw32 --target=i686-w64-mingw32 --prefix=/mingw32 --with-sysroot=/c/mingw491/i686-491-posix-dwarf-rt_v3-rev0/mingw32 --with-gxx-include-dir=/mingw32/i686-w64-mingw32/include/c++ --enable-shared --enable-static --disable-multilib --enable-languages=ada,c,c++,fortran,objc,obj-c++,lto --enable-libstdcxx-time=yes --enable-threads=posix --enable-libgomp --enable-libatomic --enable-lto --enable-graphite --enable-checking=release --enable-fully-dynamic-string --enable-version-specific-runtime-libs --disable-sjlj-exceptions --with-dwarf2 --disable-isl-version-check --disable-cloog-version-check --disable-libstdcxx-pch --disable-libstdcxx-debug --enable-bootstrap --disable-rpath --disable-win32-registry --disable-nls --disable-werror --disable-symvers --with-gnu-as --with-gnu-ld --with-arch=i686 --with-tune=generic --with-libiconv --with-system-zlib --with-gmp=/c/mingw491/prerequisites/i686-w64-mingw32-static --with-mpfr=/c/mingw491/prerequisites/i686-w64-mingw32-static --with-mpc=/c/mingw491/prerequisites/i686-w64-mingw32-static --with-isl=/c/mingw491/prerequisites/i686-w64-mingw32-static --with-cloog=/c/mingw491/prerequisites/i686-w64-mingw32-static --enable-cloog-backend=isl --with-pkgversion='i686-posix-dwarf-rev0, Built by MinGW-W64 project' --with-bugurl=http://sourceforge.net/projects/mingw-w64 CFLAGS='-O2 -pipe -I/c/mingw491/i686-491-posix-dwarf-rt_v3-rev0/mingw32/opt/include -I/c/mingw491/prerequisites/i686-zlib-static/include -I/c/mingw491/prerequisites/i686-w64-mingw32-static/include' CXXFLAGS='-O2 -pipe -I/c/mingw491/i686-491-posix-dwarf-rt_v3-rev0/mingw32/opt/include -I/c/mingw491/prerequisites/i686-zlib-static/include -I/c/mingw491/prerequisites/i686-w64-mingw32-static/include' CPPFLAGS= LDFLAGS='-pipe -L/c/mingw491/i686-491-posix-dwarf-rt_v3-rev0/mingw32/opt/lib -L/c/mingw491/prerequisites/i686-zlib-static/lib -L/c/mingw491/prerequisites/i686-w64-mingw32-static/lib'
Thread model: posix
gcc version 4.9.1 (i686-posix-dwarf-rev0, Built by MinGW-W64 project) 

[/code]

I have no idea what might be wrong here

-------------------------

cadaver | 2017-01-02 00:59:56 UTC | #2

Crash reproduced when I load the scene saved from the Physics sample in the editor, and start scene update (Ctrl-P).

EDIT: the crash happens inside Bullet's box-box collision detection routine, where it's using SSE math instructions. You can use the CMake option -DURHO3D_SSE=0 to disable SSE; in that case it shouldn't crash anymore. This requires investigation whether we should perhaps default to SSE off on MinGW, or whether the editor somehow causes physics objects to be allocated in a way that violates SSE memory alignment requirements. Note however that it does not happen on some other MinGW GCC versions even with SSE enabled, for example 4.7.2.

-------------------------

Bluemoon | 2017-01-02 00:59:56 UTC | #3

I rebuilt Urho3D using the same compiler as before, that is MinGW-w64 GCC 4.9.1 but with SSE turned off. When I tried the editor physics procedure it worked well without crashing. I made another build using GCC 4.7.2 with SSE turned on, on running the editor physics procedure it ran well also without crashing. So most likely the SSE issue is with GCC 4.9.1 or perhaps it was inherited from a version after 4.7.2 and passed along

-------------------------

weitjong | 2017-01-02 00:59:56 UTC | #4

When the compiler is MinGW, our build script configures to use -msse2 instead of -msse when URHO3D_SSE=1 (default) and generates this configuration message.

[quote]Using SSE2 instead of SSE because SSE fails on some Windows ports of GCC
Disable SSE with the CMake option -DURHO3D_SSE=0 if this is not desired[/quote]

It implies that either the crashed version built using GCC 4.9.1 or the working version built using GCC 4.7.2 are both compiled with -msse2 option set and never uses the -msse option (unless you use different CMake build scripts than the official repo). Vaguely I remember this change was made based on a report by a MinGW user some time ago. However, I fail to understand its rationale. I thought -msse2 will enable more built-in SSE functions than -msse and so does -msse3 will enable even more (but it will only work on more modern CPUs) and so on. So, why -msse2 would work when -msse would fail on MinGW compiler? Or do I have a wrong understanding? Perhaps, we really need to modify this part of the MinGW configuration in the build script after all.

On your issue, have you tried to set the compiler flag to instruct GCC to perform stack alignment on your program entry points? See [peterstock.co.uk/games/mingw_sse/](http://www.peterstock.co.uk/games/mingw_sse/). This stack alignment problem when MinGW is called from Windows runtime appears to be an old known issue.

-------------------------

cadaver | 2017-01-02 00:59:56 UTC | #5

In fact it's that "fix" that is causing the crash in this case. Using just SSE instructions, Bullet doesn't crash on MinGW / GCC 4.9.1.

EDIT: I've pushed the change to not use "-msse2". If this leads to bug report(s) again, we can either tell to disable SSE, tell to upgrade MinGW, or implement GCC version detection to the build script.

-------------------------

weitjong | 2017-01-02 00:59:56 UTC | #6

I don't think we need to wait for too long to get a new bug report :slight_smile:.  It appears that Urho3D does not build successfully with -msse option for Windows 32-bit platform when the build system has an older version of MinGW, like our CI build system on Travis-CI. The last commit has failed the CI build for Windows 32-bit platform. The build fails due to incorrect include in one of MinGW header file. MinGW developer has corrected the offending header file but has only committed the changes in their trunk and not on their stable branches. In which case, it means only MinGW version released after Feb 2014 will have this fix. See [sourceforge.net/p/mingw-w64/mai ... /31965996/](https://sourceforge.net/p/mingw-w64/mailman/message/31965996/). When SSE2 is used, the compiler already has built-in function declared some how, so the offending header file still work, I guess.

Tough luck. I wonder that this is exactly what the "fix" is trying to fix :slight_smile:.

-------------------------

cadaver | 2017-01-02 00:59:56 UTC | #7

Thanks for the heads-up, and subsequent CMake code cleanup! Ok, now we have the version check, which can be tightened later if there's need, and users should always be able to attempt SSE build even with a low MinGW version by just specifying -DURHO3D_SSE=1.

-------------------------

Bluemoon | 2017-01-02 00:59:57 UTC | #8

I guess I'll have to go with -DURHO3D_SSE=0 on the GCC 4.9.1  :frowning:  I just hope I won't miss much in terms of performance enhancement...

Thanks cadaver and weitjong for the in-depth explanations.

-------------------------

weitjong | 2017-01-02 00:59:57 UTC | #9

No. With the changes Lasse (@cadaver) just made, MinGW/GCC having version 4.9.1 or greater should by default be configured to use SSE. Lasse reported in one of the post above that he has tested before that Bullet doesn't crash on this particular version (hopefully on all subsequent newer versions). The crash only happens with SSE2 which is not used anymore after his changes.

-------------------------

Bluemoon | 2017-01-02 00:59:57 UTC | #10

:smiley: I finally have it working well with the changes Lasse made... Thanks once again.

-------------------------

