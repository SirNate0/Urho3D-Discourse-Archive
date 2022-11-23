zakk | 2017-01-02 01:00:07 UTC | #1

Hello,

Well, maybe another future tutorial. For the moment, i'm stuck.

The Urho3D build with -DURHO3D_LUA works like a charm (except it's slow, relative to C++ or AngelScript samples).

Then I've decided to build Urho3D with LuaJIT support.

I tried with these parameters:

[b]./cmake_gcc.sh -DURHO3D_LUA=0 -DURHO3D_LUAJIT=1[/b]

I get no warnings for x86 (native) build, but for Android:

[code]

Android build
================================================================================
CMake Error at ThirdParty/LuaJIT/CMakeLists.txt:169 (message):
  The configuration cannot be done now because the target-specific
  'buildvm-android' tool has not been built yet.  However, the specific
  target architecture information is now saved.  Reconfigure the desktop
  native build to incorporate the saved information by calling the respective
  batch/shell script for native build (it might be the same script as this
  one).  Then run make or the equivalent command to actually build the
  missing tool natively.  Finally, after the tool is built, come back to call
  this batch/shell script again to complete this configuration.


-- Configuring incomplete, errors occurred!
See also "/home/zakk/sources/Urho3D/android-Build/CMakeFiles/CMakeOutput.log".

[/code]

I've checked the [i]CMakeOutput.log[/i] and didn't find anything odd.


And indeed, when i try to build LuaJIT (~/sources/Urho3D/Build/ThirdParty/LuaJIT), x86 static lib is generated, but troubles rise with [i]buildvm-android[/i]. (i know, i've been warned).

[code]

The LuaJIT static library for x86 succeed.

Scanning dependencies of target buildvm-android
[100%] Building C object ThirdParty/LuaJIT/generated/buildvm-android/CMakeFiles/buildvm-android.dir/home/zakk/sources/Urho3D/Source/Thir
dParty/LuaJIT/src/host/buildvm.c.o
[100%] Building C object ThirdParty/LuaJIT/generated/buildvm-android/CMakeFiles/buildvm-android.dir/home/zakk/sources/Urho3D/Source/Thir
dParty/LuaJIT/src/host/buildvm_asm.c.o
[100%] Building C object ThirdParty/LuaJIT/generated/buildvm-android/CMakeFiles/buildvm-android.dir/home/zakk/sources/Urho3D/Source/Thir
dParty/LuaJIT/src/host/buildvm_peobj.c.o
[100%] Building C object ThirdParty/LuaJIT/generated/buildvm-android/CMakeFiles/buildvm-android.dir/home/zakk/sources/Urho3D/Source/Thir
dParty/LuaJIT/src/host/buildvm_lib.c.o
[100%] Building C object ThirdParty/LuaJIT/generated/buildvm-android/CMakeFiles/buildvm-android.dir/home/zakk/sources/Urho3D/Source/Thir
dParty/LuaJIT/src/host/buildvm_fold.c.o
Linking C executable /home/zakk/sources/Urho3D/Bin/buildvm-android
/usr/bin/ld: skipping incompatible /usr/lib/gcc/x86_64-unknown-linux-gnu/4.9.1/../../../../lib/libdl.so when searching for -ldl
/usr/bin/ld: skipping incompatible /usr/lib/gcc/x86_64-unknown-linux-gnu/4.9.1/../../../../lib/libdl.a when searching for -ldl
/usr/bin/ld: skipping incompatible /lib/../lib/libdl.so when searching for -ldl
/usr/bin/ld: skipping incompatible /lib/../lib/libdl.a when searching for -ldl
/usr/bin/ld: skipping incompatible /usr/lib/../lib/libdl.so when searching for -ldl
/usr/bin/ld: skipping incompatible /usr/lib/../lib/libdl.a when searching for -ldl
/usr/bin/ld: skipping incompatible /usr/lib/gcc/x86_64-unknown-linux-gnu/4.9.1/../../../libdl.so when searching for -ldl
/usr/bin/ld: skipping incompatible /usr/lib/gcc/x86_64-unknown-linux-gnu/4.9.1/../../../libdl.a when searching for -ldl
/usr/bin/ld: skipping incompatible /usr/lib/libdl.so when searching for -ldl
/usr/bin/ld: skipping incompatible /usr/lib/libdl.a when searching for -ldl
/usr/bin/ld: cannot find -ldl
(cut the rest)

[/code]

What can i do or try ?

Thank you.

-------------------------

weitjong | 2017-01-02 01:00:07 UTC | #2

[quote]The configuration cannot be done now because the target-specific
  'buildvm-android' tool has not been built yet.  However, the specific
  target architecture information is now saved.  Reconfigure the desktop
  native build to incorporate the saved information by calling the respective
  batch/shell script for native build (it might be the same script as this
  one).  Then run make or the equivalent command to actually build the
  missing tool natively.  Finally, after the tool is built, come back to call
  this batch/shell script again to complete this configuration.[/quote]

Just which part of the above sentence is not clear to you? I was the one who put those sentences together. Sorry for my bad English. Basically, what you need to do after receiving this message is to build the missing 'buildvm-android' tool before proceeding with Android build. How to build the tool?
1. This tool (as well as all the other tools) should be built natively. By native, I mean your normal build (i.e. when target platform system is equal to build/host system). For your case, you need to run ./cmake_gcc.sh one more time. The script will reconfigure your existing native Urho3D project to build this new tool natively.
2. cd Build && make to actually build it. Note that it is "Build" directory (native). Verify the buildvm-android executable is created in "Bin" directory.
3. Now you have the tool built, call the ./cmake_gcc.sh one more time to reconfigure for your Android project. It should not complain again and should configure your Android project with LuaJIT enabled.
4. cd android-Build && make.

Good luck.

-------------------------

weitjong | 2017-01-02 01:00:07 UTC | #3

BTW, why we did all this is because we have hit CMake technical limitation in cross compiling build. The good old Makefile is able to handle such cross compiling cases much better, as can be seen in the original LuaJIT Makefile. This is as automated as we can come up with using CMake. At least it works to enable LuaJIT for these cross compiling targets: Android and Raspberry-Pi using Linux build system or for Android target only using Windows build system. In theory we could also make it works for iOS target too, but we didn't because of Apple policy.

-------------------------

zakk | 2017-01-02 01:00:08 UTC | #4

Hello,

Thanks for providing help one more time.

Don't worry about your english, it's more a problem with my own understanding.
With your additional explanations, it's easier for me to understand.

Reading the script output i posted, i had understood that i had to build something related to [i]buildvm-android[/i].

After doing a [i]find[/i] on this file, i've found that it was related to LuaJIT. Then i scratched my head, wondering ?so i have to build LuaJIT part for building LuaJIT ??

I searched in the generated Makefile (in [i]ThirdParty/LuaJIT[/i]) if there was an entry dedicated for [i]buildvm-android[/i], but found nothing. Then i posted here.

I had not understand what was the meaning of [i]native build[/i]. Now it's ok, i guess.


So if i understand well:

1) i have to launch [i]./cmake_gcc.sh[/i] with [b]native[/b] parameters (ie those for Linux 64 bits x86).

2) Then i got this warning (?you have to build buildvm-android?): I must launch again [i]./cmake_gcc.sh[/i] with same parameters as above.

3) cd Build / make.
(after checking that [i]buildvm-android[/i] is in Bin)

To be sure, i did a complete clone of the project with git.

[code]

 ~/sources/Urho3D$ git clone https://github.com/urho3d/Urho3D.git

[/code]


Then, i've cleaned cmake cache (not needed, but just to be sure).
And i gave parameters for a [b]native build on Linux 64 bits x86[/b]. I've put URHO3D_EXTRAS and URHO3D_TOOLS to be sure to include needed 3rd parties.

[code]

 ~/sources/Urho3D$ ./cmake_clean.sh 
 ~/sources/Urho3D$ ./cmake_gcc.sh -DURHO3D_64BIT=1 -DURHO3D_LUA=0 -DURHO3D_LUAJIT=1 -DURHO3D_EXTRAS=1 -DURHO3D_TOOLS=1 -DURHO3D_LIB_TYPE=SHARED

[/code]

So i get the same message i've posted above.
I relaunch immediatly the last command:


[code]

 ~/sources/Urho3D$ ./cmake_gcc.sh -DURHO3D_64BIT=1 -DURHO3D_LUA=0 -DURHO3D_LUAJIT=1 -DURHO3D_EXTRAS=1 -DURHO3D_TOOLS=1 -DURHO3D_LIB_TYPE=SHARED

Android build
================================================================================
CMake Warning at Engine/LuaScript/CMakeLists.txt:35 (message):
  For cross-compiling build to be successful, the 'tolua++' tool must be
  built natively first and present in the 'Bin' folder.


CMake Error at ThirdParty/LuaJIT/CMakeLists.txt:169 (message):
  The configuration cannot be done now because the target-specific
  'buildvm-android' tool has not been built yet.  However, the specific
  target architecture information is now saved.  Reconfigure the desktop
  native build to incorporate the saved information by calling the respective
  batch/shell script for native build (it might be the same script as this
  one).  Then run make or the equivalent command to actually build the
  missing tool natively.  Finally, after the tool is built, come back to call
  this batch/shell script again to complete this configuration.


-- Configuring incomplete, errors occurred!
See also "/home/zakk/sources/Urho3D/android-Build/CMakeFiles/CMakeOutput.log".

Native build
================================================================================
-- Configuring done
-- Generating done
-- Build files have been written to: /home/zakk/sources/Urho3D/Build

[/code]

Hmmm still warnings?
Well, let's try a build.

As i got a strange bug with the cpufreq governor on my laptop (sure, it needs a reboot after 42 days of hibernation cycles), my cpu cannot go beyond 0.6 Ghz.
I tell you this for explaining why i jump directly to LuaJIT directory, instead of doing a full build.

So at the beginning, all seems to go smooth.

But is still hangs like the last time.


[code]

 ~/sources/Urho3D/Build/ThirdParty/LuaJIT$ make

(lot of compilation, 5mn later?)
Linking C static library libLuaJIT.a
(...)
Linking C executable /home/zakk/sources/Urho3D/Bin/luajit
Copying dependency files for luajit standalone executable
(...)
Scanning dependencies of target buildvm-android
(...)
Linking C executable /home/zakk/sources/Urho3D/Bin/buildvm-android
/usr/bin/ld: skipping incompatible /usr/lib/gcc/x86_64-unknown-linux-gnu/4.9.0/../../../../lib/libdl.so when se arching for -ldl
/usr/bin/ld: skipping incompatible /usr/lib/gcc/x86_64-unknown-linux-gnu/4.9.0/../../../../lib/libdl.a when sea rching for -ldl
/usr/bin/ld: skipping incompatible /lib/../lib/libdl.so when searching for -ldl
/usr/bin/ld: skipping incompatible /lib/../lib/libdl.a when searching for -ldl
/usr/bin/ld: skipping incompatible /usr/lib/../lib/libdl.so when searching for -ldl
/usr/bin/ld: skipping incompatible /usr/lib/../lib/libdl.a when searching for -ldl
/usr/bin/ld: skipping incompatible /usr/lib/gcc/x86_64-unknown-linux-gnu/4.9.0/../../../libdl.so when searching for -ldl
/usr/bin/ld: skipping incompatible /usr/lib/gcc/x86_64-unknown-linux-gnu/4.9.0/../../../libdl.a when searching for -ldl
/usr/bin/ld: skipping incompatible /usr/lib/libdl.so when searching for -ldl
/usr/bin/ld: skipping incompatible /usr/lib/libdl.a when searching for -ldl
/usr/bin/ld: cannot find -ldl

[/code]

I thought it was a problem related to the cross-compiler, but as it's a native build, i don't understand what happens.

Thank you again for the time you are spending on this. When it's solved, i'll repost my notes with full explanations, for helping the next newb :slight_smile:

-------------------------

zakk | 2017-01-02 01:00:08 UTC | #5

Hello,

I've decided to try to compile LuaJIT for Android, apart from Urho3D.
Just for seeing if i encounter the same problems.

So i've downloadedl last sources from LuaJIT website.

I've followed the instruction given here: [luajit.org/install.html](http://luajit.org/install.html)

I can compile others Android programs (I've compiled Lua without problems).

The interesting thing is [i]i have the same compilation (linking in fact) problems[/i] than when i try to [b]buildvm-android[/b] with Urho3D.

To be accurate, these are not the same libs involved with Urho3D buildvm-android (see my previous post in this thread). But i'm sure the problem is the same.

So i think if i manage to compile LuaJIT on my own, i can sort out the Urho3D buildvm-android problem.

I use this compilation script:

[code]

NDK=/opt/android-ndk-r10
NDKABI=14
NDKVER=$NDK/toolchains/arm-linux-androideabi-4.6
NDKP=$NDKVER/prebuilt/linux-x86_64/bin/arm-linux-androideabi-
NDKF="--sysroot $NDK/platforms/android-$NDKABI/arch-arm"
NDKARCH="-march=armv7-a -mfloat-abi=softfp -Wl,--fix-cortex-a8"

# just to be sure
make clean

make HOST_CC="gcc -m32" CROSS=$NDKP TARGET_FLAGS="$NDKF $NDKARCH" 

[/code]


But i get this:

[code]

Building LuaJIT 2.0.3 ==== make -C src
make[1]: Entering directory '/home/zakk/coding/android/LuaJIT-2.0.3/src'
HOSTCC    host/minilua.o
HOSTLINK  host/minilua
/usr/bin/ld: skipping incompatible /usr/lib/gcc/x86_64-unknown-linux-gnu/4.9.1/../../../../lib/libm.so when searching for -lm
/usr/bin/ld: skipping incompatible /usr/lib/gcc/x86_64-unknown-linux-gnu/4.9.1/../../../../lib/libm.a when searching for -lm
/usr/bin/ld: skipping incompatible /lib/../lib/libm.so when searching for -lm
/usr/bin/ld: skipping incompatible /lib/../lib/libm.a when searching for -lm
/usr/bin/ld: skipping incompatible /usr/lib/../lib/libm.so when searching for -lm
/usr/bin/ld: skipping incompatible /usr/lib/../lib/libm.a when searching for -lm
/usr/bin/ld: skipping incompatible /usr/lib/gcc/x86_64-unknown-linux-gnu/4.9.1/../../../libm.so when searching for -lm
/usr/bin/ld: skipping incompatible /usr/lib/gcc/x86_64-unknown-linux-gnu/4.9.1/../../../libm.a when searching for -lm
/usr/bin/ld: skipping incompatible /usr/lib/libm.so when searching for -lm
/usr/bin/ld: skipping incompatible /usr/lib/libm.a when searching for -lm
/usr/bin/ld: cannot find -lm ARGET_SYS=Linux

(snip the rest of the errors)

[/code]

And after this error on math-lib, same thing for libgcc, libgcc_s and libc, whose search fails the same way.

I tried differents combinations with LDFLAGS (for forcing libs path searching), but with no luck.
With --sysroot, i shouldn't have to give libs path, anyway.

[code]
 
$ ls /opt/android-ndk-r10/platforms/android-14/arch-arm
usr

[/code]

(so it's ok for the sysroot value)


Any idea ?


Thank you.

-------------------------

weitjong | 2017-01-02 01:00:08 UTC | #6

[quote]Any idea ?[/quote]

I am taking a long shot at this. It is caused by your host operating system. Are you using 64-bit Debian or Ubuntu? I guess that the error: "/usr/bin/ld: skipping incompatible /usr/lib/gcc/x86_64-unknown-linux-gnu" means the linker was looking for 32-bit version of the library but found a 64-bit one. Remember that at the moment when you targeting Android platform, your build is always 32-bit. This is also true when you build Urho3D for Android platform regardless of the URHO3D_64BIT build option that you pass.

My recommendation. Get a 32-bit Debian or 32-bit Ubuntu when you want to build for Android. Or, get a 64-bit Fedora but install both 32-bit and 64-bit software development packages. If my guess on why you got this problem in the first place is correct then in theory you should be able to install 32-bit devel packages into your 64-bit Debian/Ubuntu and it should also solve your problem, however, that would or might whack your 64-bit part out for good in your host system (speaking from past experience using Ubuntu 12.04 LTS VM). In my opinion Debian-based distros still do not have good multi-arch support where the same 64-bit host system has both 32-bit arch and 64-bit arch libraries coexist. Not intended to start a flame war here but 64-bit Fedora system does a much better job at this kind of scenario.

-------------------------

friesencr | 2017-01-02 01:00:08 UTC | #7

I had troubles with luajit for the android too.  I deferred solving it until I actually have a game :slight_smile:, which will probably be never.  Build problems make me grumpy.  Depending on how heavy your lua code is you may not suffer as large of a perf penalty as you think.  Urho's c++ is still doing most of the work behind the scenes.

-------------------------

zakk | 2017-01-02 01:00:09 UTC | #8

I'm running 64 bits Arch Linux. There is clearly a problem with finding the correct libs for ARM 32 bits target.

[b]--sysroot[/b] parameter seems totally ignored.

In fact, it seems event that [i]CROSS[/i] parameter is ignored, and that the gcc shipped for x86_64 is used instead.

If i force the compiler to HOST_CC, and provide CFLAGS and LDFLAGS for include and libs path, it will compile farther. But still completly hangs when the time to link has come.

(the -m32 is here for forcing 32 bits code to be generated)

[code]

$ make HOST_CC="arm-linux-androideabi-gcc -m32" TARGET_SYS=Linux TARGET=arm CFLAGS=-I/opt/android-ndk-r10/platforms/android-14/arch-arm/usr/include LDFLAGS=-L/opt/android-ndk-r10/platforms/android-14/arch-arm/usr/lib

make[1]: Entering directory '/home/zakk/coding/android/LuaJIT-2.0.3/src'
HOSTLINK  host/minilua
/opt/android-ndk-r10/toolchains/arm-linux-androideabi-4.6/prebuilt/linux-x86_64/bin/../lib/gcc/arm-linux-androideabi/4.6/../../../../arm-linux-androideabi/bin/ld: error: cannot open crtbegin_dynamic.o: No such file or directory
/opt/android-ndk-r10/toolchains/arm-linux-androideabi-4.6/prebuilt/linux-x86_64/bin/../lib/gcc/arm-linux-androideabi/4.6/../../../../arm-linux-androideabi/bin/ld: error: cannot open crtend_android.o: No such file or directory
/opt/android-ndk-r10/toolchains/arm-linux-androideabi-4.6/prebuilt/linux-x86_64/bin/../lib/gcc/arm-linux-androideabi/4.6/../../../../arm-linux-androideabi/bin/ld: warning: skipping incompatible /opt/android-ndk-r10/platforms/android-14/arch-arm/usr/lib/libm.so while searching for m
/opt/android-ndk-r10/toolchains/arm-linux-androideabi-4.6/prebuilt/linux-x86_64/bin/../lib/gcc/arm-linux-androideabi/4.6/../../../../arm-linux-androideabi/bin/ld: error: cannot find -lm
/opt/android-ndk-r10/toolchains/arm-linux-androideabi-4.6/prebuilt/linux-x86_64/bin/../lib/gcc/arm-linux-androideabi/4.6/../../../../arm-linux-androideabi/bin/ld: warning: skipping incompatible /opt/android-ndk-r10/platforms/android-14/arch-arm/usr/lib/libc.so while searching for c

(snip the rest)

[/code]


Though, my libs are here.

[code]

$ ls /opt/android-ndk-r10/platforms/android-14/arch-arm/usr/lib
crtbegin_dynamic.o  crtend_android.o  libc.a    libEGL.so        libjnigraphics.so  libm_hard.a      libOpenSLES.so  libthread_db.so
crtbegin_so.o       crtend_so.o       libc.so   libGLESv1_CM.so  liblog.so          libm.so          libstdc++.a     libz.so
crtbegin_static.o   libandroid.so     libdl.so  libGLESv2.so     libm.a             libOpenMAXAL.so  libstdc++.so

[/code]


And it's 32 bits.

[code]

$ file /opt/android-ndk-r10/platforms/android-14/arch-arm/usr/lib/libm.so
/opt/android-ndk-r10/platforms/android-14/arch-arm/usr/lib/libm.so: ELF 32-bit LSB shared object, ARM, EABI5 version 1 (SYSV), dynamically linked, not stripped

[/code]


Strange thing is that i had no problem compiling and linking Lua for Android on same computer.
It seems that there are several problems which stack up :frowning:

For the moment, i give up on compiling LuaJIT for Android.

Anyway, as friesencr said, the most important is to have a game to run. That's not the case for me now, so i've to do that before.

It will be time for optimizations after. For the moment, Urho3D seems to package well at least Linux, Windows and Android. With Lua support and that's the most important for me. In the worst case, i guess i can extend Lua with a small C unit, for heavy-duty computations (ahem.)

Thank you for answering, always a pleasure to have support  :smiley:

-------------------------

friesencr | 2017-01-02 01:00:09 UTC | #9

I will probably make a dedicated 32bit box at some point.  Skip all the multi arch crap.  Moar computers!!!

-------------------------

weitjong | 2017-01-02 01:00:09 UTC | #10

I don't want to end this discussion while leading other forum readers to believe that building Urho3D library with LuaJIT enabled is difficult. As I said it before, the process is almost all automated by our CMake scripts that one just have to:
[ol][li] Carry out the configuration in the right order. For cross compiling target such as Android, one have to deal with configuration for not 1 but 2 projects: a) native project to build the necessary tools and b) Android project to build the library itself. [/li]
[li] Have a build/host system with all the compatible prerequisite software installed for the intended target platform.[/li][/ol]
Lastly have a closer look on the Rakefile and .travis.yml. It has all the bits to instruct our CI Server to test build Urho3D library with LuaJIT enabled on most of the supported target platforms. My own 64-bit Fedora build system can do the same feat without any sweat  :smiley:.

-------------------------

