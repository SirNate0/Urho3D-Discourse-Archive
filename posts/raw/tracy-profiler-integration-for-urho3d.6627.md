WangKai | 2020-12-24 01:50:09 UTC | #1

Hi,

I'm integrating **Tracy** profiler (https://github.com/wolfpld/tracy/) into Urho3D. If it's only the client side integration, things should be neat. Tracy profiler should be a good plus to the engine.

It's working great on Windows -

![image|690x253](upload://xwZGUKpyNywSqcUJKtL53n0DHvI.jpeg) 

but, I find a compiling issue for Android:

````log
D:\AndroidDev\AndroidSDK\ndk\22.0.7026061\toolchains\llvm\prebuilt\windows-x86_64\bin\clang++.exe --target=armv7-none-linux-androideabi18 --gcc-toolchain=D:/AndroidDev/AndroidSDK/ndk/22.0.7026061/toolchains/llvm/prebuilt/windows-x86_64 --sysroot=D:/AndroidDev/AndroidSDK/ndk/22.0.7026061/toolchains/llvm/prebuilt/windows-x86_64/sysroot  -DNOMINMAX=1 -DTRACY_ENABLE=1 -DURHO3D_ANGELSCRIPT -DURHO3D_FILEWATCHER -DURHO3D_IK -DURHO3D_LOGGING -DURHO3D_LUA -DURHO3D_NAVIGATION -DURHO3D_NETWORK -DURHO3D_PHYSICS -DURHO3D_PROFILING -DURHO3D_STATIC_DEFINE -DURHO3D_THREADING -DURHO3D_URHO2D -DURHO3D_WEBP -DWIN32_LEAN_AND_MEAN -D_CRT_NONSTDC_NO_DEPRECATE -D_CRT_SECURE_NO_DEPRECATE -D_USE_MATH_DEFINES  -g -DANDROID -fdata-sections -ffunction-sections -funwind-tables -fstack-protector-strong -no-canonical-prefixes -D_FORTIFY_SOURCE=2 -march=armv7-a -mthumb -Wformat -Werror=format-security   -std=c++11 -Wno-invalid-offsetof -Qunused-arguments -fcolor-diagnostics -Wno-argument-outside-range -O0 -fno-limit-debug-info  -fPIC -fvisibility=hidden -fvisibility-inlines-hidden -MD -MT Source/ThirdParty/Tracy/CMakeFiles/Tracy.dir/client/TracySysTrace.cpp.o -MF Source\ThirdParty\Tracy\CMakeFiles\Tracy.dir\client\TracySysTrace.cpp.o.d -o Source/ThirdParty/Tracy/CMakeFiles/Tracy.dir/client/TracySysTrace.cpp.o -c ../../../../../../Source/ThirdParty/Tracy/client/TracySysTrace.cpp
../../../../../../Source/ThirdParty/Tracy/client/TracySysTrace.cpp:638:21: error: use of undeclared identifier '__NR_perf_event_open'
    return syscall( __NR_perf_event_open, hw_event, pid, cpu, group_fd, flags );
                    ^
1 error generated.
[18/945] Building CXX object Source/ThirdParty/Tracy/CMakeFiles/Tracy.dir/client/TracyProfiler.cpp.o
ninja: build stopped: subcommand failed.
````

NDK **21.0.6113669** and **22.0.7026061** have been tried.

Any ideas?

Thanks!

-------------------------

Eugene | 2020-12-24 10:00:37 UTC | #2

Fortunatelly, we have an expert in integrating Tracy into Urho. @rku?

-------------------------

rku | 2020-12-24 10:14:41 UTC | #3

Disable context switch profiling on android i think

-------------------------

WangKai | 2020-12-24 12:35:05 UTC | #4

According to Tracy's document -
![image|671x444](upload://zq3k8sdkC0nr9sm4hsEreuIdlOr.png) 

Context switch should be supported on Android and if there is no direct fixing, I have to disable `TRACY_HAS_SYSTEM_TRACING` completely to make it work on Android.

I have submitted an issue on Tracy -
https://github.com/wolfpld/tracy/issues/153

-------------------------

WangKai | 2020-12-26 04:55:31 UTC | #5

The compiling issue has been solved by adding `#include <sys/syscall.h>` to the source, but now there is a linking issue -
```log
  clang++: error: linker command failed with exit code 1 (use -v to see invocation)
  [13/104] Linking CXX shared library ..\..\..\..\build\intermediates\cmake\debug\obj\armeabi-v7a\lib01_HelloWorld.so
  FAILED: ../../../../build/intermediates/cmake/debug/obj/armeabi-v7a/lib01_HelloWorld.so
  cmd.exe /C "cd . && D:\AndroidDev\AndroidSDK\ndk\21.0.6113669\toolchains\llvm\prebuilt\windows-x86_64\bin\clang++.exe --target=armv7-none-linux-androideabi18 --gcc-toolchain=D:/AndroidDev/AndroidSDK/ndk/21.0.6113669/toolchains/llvm/prebuilt/windows-x86_64 --sysroot=D:/AndroidDev/AndroidSDK/ndk/21.0.6113669/toolchains/llvm/prebuilt/windows-x86_64/sysroot -fPIC -g -DANDROID -fdata-sections -ffunction-sections -funwind-tables -fstack-protector-strong -no-canonical-prefixes -D_FORTIFY_SOURCE=2 -march=armv7-a -mthumb -Wformat -Werror=format-security   -std=c++11 -Wno-invalid-offsetof -Qunused-arguments -fcolor-diagnostics -Wno-argument-outside-range -O0 -fno-limit-debug-info  -Wl,--exclude-libs,libgcc_real.a -Wl,--exclude-libs,libatomic.a -static-libstdc++ -Wl,--build-id -Wl,--fatal-warnings -Wl,--exclude-libs,libunwind.a -Wl,--no-undefined -Qunused-arguments -shared -Wl,-soname,lib01_HelloWorld.so -o ..\..\..\..\build\intermediates\cmake\debug\obj\armeabi-v7a\lib01_HelloWorld.so Samples/01_HelloWorld/CMakeFiles/01_HelloWorld.dir/HelloWorld.cpp.o  D:/code/man/Urho3D/android/urho3d-lib/build/tree/Debug/armeabi-v7a/lib/libUrho3D.a -ldl -llog -landroid -lGLESv1_CM -lGLESv2 -latomic -lm && cd ."
  ../../../../../../Source/ThirdParty/Tracy/client/TracyProfiler.cpp:123: error: undefined reference to 'tracy::rpmalloc_initialize()'
```
function `tracy::rpmalloc_initialize()` in source code -
![image|598x500](upload://mQOL5PjEGODzl676XBgfeu9voRa.png) 

object generated -
![image|690x65](upload://4N6vhBSOu7StmCMU1P1Yax8UmkI.png) 

Interesting situation...

-------------------------

SirNate0 | 2020-12-26 06:52:12 UTC | #6

Maybe remove the `extern` from the function definition?

-------------------------

WangKai | 2020-12-26 08:08:06 UTC | #7

Thank you! However, the link issue still exists :thinking:

-------------------------

weitjong | 2020-12-26 14:05:47 UTC | #8

Try using STATIC lib type instead of SHARED. If the “Urho3DPlayer” target is successfully built after that then the issue was with your libUrho3D.so shared lib already eliminating unused symbols.

And, if you were already using STATIC lib type then it means the symbol was not in the libUrho3D.a despite what you have setup. You can verify that using “nm”.

HTH.

-------------------------

WangKai | 2020-12-27 03:08:40 UTC | #9

Thank you @weitjong!

I think you are right. 

I'm using the STATIC lib of Urho3D, and lib Tracy is supposed to live inside of lib Urho3D. However, since Tracy is used everywhere in the Samples by including headers and inserting macros but some of the symbols are just elimiated.

It seems we have three choices - 
* **Export** all missed functions of Tracy, just like this commit (https://github.com/wolfpld/tracy/commit/a467ef4c2b2ffe8047a08c802b363d23c473b66b) is doing. But I don't know the full list in which we include all necessary functions.
* Add lib Tracy to applications' dependencis instead of just linking lib Urho3D. It seems not the way we handle third-party libraries in Urho but still practical.
* I wonder if there is way to ask the build toolchain to keep the symbols of Tracy and not optimize them in the Urho3D, instead delay the optimization till the application building phase?

All remides me to do a testing for the release version, which may lead more such potential issues.

-------------------------

weitjong | 2020-12-27 04:44:53 UTC | #10

You misunderstood me a little bit. Only the SHARED lib type needs special consideration (what get exported) in order to avoid undesired symbol elimination while building the shared library itself. On the other hand the STATIC lib type does not suffer from this kind of elimination issue. It is basically just a collection or archive of all the objects there are in the said library target. Assuming you only interested in using the STATIC lib type then you can either:

1. Rely on the existing "librarian" logic that Urho3D library has. If you add a new third-party lib with Urho3D provided macro (i.e not using the vanila CMake command) then it should automatically set thing up for you. The librarian will merge all the objects from the new lib (Tracy) into the libUrho3D.a while the Urho3D target is being built.

1. Set it up as you have mentioned in your second bullet point. Add a new third-party lib with the vanila CMake command to do so. It should then just build libTracy.a or what have you, which should contain all the objects from this new target. Note that I said, "it should" here as I don't know anything about this profiling library. In the app then you have to explicitly tell CMake that the app depends on this new library.

-------------------------

WangKai | 2020-12-27 04:49:28 UTC | #11

Yes, I'm using the approach you explained in your first bullet point. Tracy is added just like other 3rd-party libraries of Urho.

I just don't understand why these symbols got removed. Maybe it's an issue of Tracy.

-------------------------

weitjong | 2020-12-27 05:07:01 UTC | #12

It is easy to debug. Each 3rd-party lib is built and the *.a is generated first before it get merged into the final `libUrho3D.a`. You can quickly verify if your `libTracy.a` has all the objects you need.

-------------------------

WangKai | 2020-12-29 07:36:07 UTC | #13

Thank you @weitjong

Android platform is now working with Tracy. However, there are some issues I need to solve to make the integration more solid.

After some polishing work and testing on maybe Linux, I think I'd make a PR and ask the community to check it.

-------------------------

JTippetts1 | 2020-12-29 13:19:19 UTC | #14

Tracy integration in rbfx broke MinGW support, so if you care about continuing  support for that platform you might need to do a little work.

-------------------------

WangKai | 2020-12-29 14:35:06 UTC | #15

Hi @JTippetts1,

Can you describe the issue with more details?
I'd like to have a try after fixing my Hello World issues on Linux.

Currrent, Android and Windows should be good with some minor changes on the integration and and fixings for Tracy.

I'm not sure if I can make my old MacBook Pro run again. I'd try to have the integration work on MACOS and IOS if I have some spare time for this side work.

-------------------------

WangKai | 2020-12-29 14:51:01 UTC | #16

As for rbfx, I have checked the work there. The Tracy profiler tool has been integrated into the Editor, which is very impressive. However, I think in Urho, we can keep thing simple by just integrating the client, and use standard Tracy tool avoid the introduction of other dependencies. 

AFAIK, the Tracy support for other platforms in rbfx is limited, no Android (yet?) and I must have missed the `Release` configurations in Visual Studio solution cmake generated?

Ideally, people could have brought Tracy integration into Urho3D from rbfx in a non disrupted community, so my work can be just fixing some issues for it. Anyway, I don't really think this is a big issue in this case.

-------------------------

rku | 2021-01-03 08:09:29 UTC | #17

Not exactly correct. MinGW builds work fine as long as you do not enable Tracy. Actually problem is quite minor too. MinGW is :poop: so even latest SDK does not provide all windows APIs, some of which Tracy uses. What we have to do is load those APIs using LoadLibrary+GetProcAddress.

[quote="WangKai, post:16, topic:6627"]
I think in Urho, we can keep thing simple by just integrating the client, and use standard Tracy tool avoid the introduction of other dependencies.
[/quote]

By default Tracy uses glfw for platform window creation. At very least client would have to be reworked to use SDL, or even Urho3D. That is not a big deal, but an annoyance when it comes to updating Tracy.

[quote="WangKai, post:16, topic:6627"]
AFAIK, the Tracy support for other platforms in rbfx is limited, no Android (yet?) and I must have missed the `Release` configurations in Visual Studio solution cmake generated?
[/quote]

My primary reason for integrating Tracy was that Urho3D profiler is unusable on mobiles. Profiling phones over the network works just fine.

-------------------------

WangKai | 2021-02-14 15:08:00 UTC | #18

**Finally have some vacation and can finish this.**

This is the pull request! -
https://github.com/urho3d/Urho3D/pull/2776

-------------------------

WangKai | 2021-02-16 16:54:39 UTC | #19

# Integration Decision
In the current integration, only **client** side code is integrated into Urho3D, so we don't have to introduce a whole family of Tracy dependencies into Urho3D, instead, we use standard Tracy tools. Current version of Tracy in our `ThirdParty` folder is the latest release 0.7.6 (https://github.com/wolfpld/tracy/releases/tag/v0.7.6). An issue on Android virtual device https://github.com/wolfpld/tracy/issues/173 really takes me sometime to figure out and it is one of the reasons why this PR is delayed.

# Build Option
`URHO3D_TRACY_PROFILING` build option toggles this feature, meaning it is optional and can be used when we need the extra profiling ability and the target platform is supported by Tracy. The original profiling related macros and their references are reused and extended.

**Edit: (updated due to changes in recent commit)**
Pseudo code of build control:
```c++
if URHO3D_TRACY_PROFILING:
    // Tracy used
elif URHO3D_PROFILING:
    // Default Urho3D profiling used.
else:
    // Profiling off.
```

# Platforms ([x] means the support is validated)
- [x] Windows
- [x] MinGW
- [x] Linux
- [x] Android (Physical/Virtual)
- [?] macOS
- [?] iOS
- [?] ??

# Testing
**1. Enable Tracy integration**
**Edit: (updated due to changes in recent commit)**
Build Urho3D and its Samples with extra build option `-D URHO3D_TRACY_PROFILING=1`.
`URHO3D_PROFILING` will be automatically turned off when `URHO3D_TRACY_PROFILING` is on. This is achieved in `UrhoCommon.cmake` script.
```cmake
if (URHO3D_TRACY_PROFILING)
    set (URHO3D_PROFILING 0)
endif ()
```

**2. Download or build the Tracy server**
* On Windows you can just download the pre-built server `Tracy.exe` from https://github.com/wolfpld/tracy/releases/download/v0.7.6/Tracy-0.7.6.7z
* On other platforms or you just want to build your own Tracy server, you can follow the `2.3 Building the server` chapter from `tracy.pdf` manual in the `Tracy-0.7.6.7z` archive and build the Tracy server by your own. (On Linux, here is a good reference -https://google.github.io/iree/developing-iree/profiling-with-tracy)

**3. Run a sample** 
* Run a sample you want to test.
* In the Tracy server, press `Connect` button to start profiling
![image|453x319](upload://aLNjAwobYJ0t2cKcx4rKgSWZTNJ.png)  

* You should see this -
![tracy_screenshot|690x266](upload://fEw04RFfSiZv6iUN05skP5QkJF2.jpeg) 

Enjoy Urho3D!

-------------------------

