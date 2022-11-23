gwald | 2017-01-02 01:11:39 UTC | #1

Continuation from : [topic1142.html](http://discourse.urho3d.io/t/deploying-urho3d-to-android-studio-in-windows/1107/1)
But I didn't want to flood the guide's thread with this.

I've got mintlinux 17.1 32bit and winXP (minGW32) running fine.
But I'm really struggling with android.

So, I've installed
     Java JDK
    CMake
    Ant (Apache-Ant)
    Android Studio SDK
    Android NDK

Gradle, I installed it (like ant, set it's bin path on the path) but not sure how it's used?

I've run the CopyData.bat as required by the instructions: [urho3d.github.io/documentation/1 ... lding.html](http://urho3d.github.io/documentation/1.31/_building.html)


env.bat:
[code]
set path=%path%;C:\Android\android-ndk\prebuilt\windows\bin;C:\ant\bin;C:\gradle\bin;C:\Android\android-ndk\build;C:\Android\android-sdk\tools;C:\Android\android-sdk\platform-tools
set  ANDROID_NDK=C:\Android\android-ndk
set  ANDROID_SDK=C:\Android\android-sdk
set JAVA_HOME=C:\JDK
set GRADLE_HOME=C:\gradle
[/code]


[code]
C:\Urho3D-1.5>cmake_android.bat build1
CMake Warning at CMake/Modules/Urho3D-CMake-common.cmake:193 (message):
  Could not use MKLINK to setup symbolic links as this Windows user account
  does not have the privilege to do so.  When MKLINK is not available then
  the build system will fallback to use file/directory copy of the library
  headers from source tree to build tree.  In order to prevent stale headers
  being used in the build, this file/directory copy will be redone also as a
  post-build step for each library targets.  This may slow down the build
  unnecessarily or even cause other unforseen issues due to incomplete or
  stale headers in the build tree.  Request your Windows Administrator to
  grant your user account to have privilege to create symlink via MKLINK
  command.  You are NOT advised to use the Administrator account directly to
  generate build tree in all cases.
Call Stack (most recent call first):
  CMakeLists.txt:47 (include)


-- Looking for include file stdint.h
-- Looking for include file stdint.h - found
-- The ASM compiler identification is GNU
-- Found assembler: C:/Android/android-ndk/toolchains/arm-linux-androideabi-4.9/
prebuilt/windows/bin/arm-linux-androideabi-gcc.exe
-- Performing Test COMPILER_HAS_HIDDEN_VISIBILITY
-- Performing Test COMPILER_HAS_HIDDEN_VISIBILITY - Success
-- Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY
-- Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY - Success
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR - Success
-- Found Urho3D: as CMake target
-- Could NOT find Doxygen (missing:  DOXYGEN_EXECUTABLE)
-- Configuring done
-- Generating done
-- Build files have been written to: C:/Urho3D-1.5/build1

C:\Urho3D-1.5>cd build1

C:\Urho3D-1.5\build1>android update project -p . -t 1
Updated and renamed default.properties to project.properties
Updated local.properties
Added file C:\Urho3D-1.5\build1\proguard-project.txt

C:\Urho3D-1.5\build1>make
Scanning dependencies of target FreeType
[  0%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/
autofit/autofit.c.o
The system cannot find the path specified.
make[2]: *** [Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/autofit/aut
ofit.c.o] Error 1
make[1]: *** [Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/all] Error 2
make: *** [all] Error 2

[/code]



I'm using winXP SP3 32bit admin account.

I also tried using -DUSE_MKLINK=1 but CMake gives the warning:
  Manually-specified variables were not used by the project:
    USE_MKLINK
Any help would be great.

-------------------------

weitjong | 2017-01-02 01:11:39 UTC | #2

Any chance you can fix the MKLINK privilege first so you don't use Admin account for development? I have not seen your build error before on any build environments that I have including on Windows.

-------------------------

gwald | 2017-01-02 01:11:39 UTC | #3

[quote="weitjong"]Any chance you can fix the MKLINK privilege first so you don't use Admin account for development? I have not seen your build error before on any build environments that I have including on Windows.[/quote]

I'll look into it, but the cmake_codeblocks.bat works 100% on winXP (admin acc), wouldn't that use the same MKLINK privilege?
I'm using mintlinux 17.1 32bit on 2009 hardware, so 64bit linux isn't an option for me (no ndk linux 32bit).
And winXP is small and fast on virtual box, so it's perfect for me.
[url=http://superuser.com/questions/484061/how-to-create-an-ntfs-junction]I think winXP requires a extra tool to support the links.[/url]

I'm setting up a winbloat7 setup to see if I can replicate the error.

-------------------------

weitjong | 2017-01-02 01:11:40 UTC | #4

I used to have an Android build environment on my Win7 VM and I think I didn't have any issue then. The MKLINK is not the root cause of your problem. Now to think about it, I am not sure WinXP has that feature. What prompted me  to make my earlier comment is the fact that you use Admin account for non-admin purposes. Of course which account type being used is really none of our business. However, note that our build system is only being tested using normal account (by myself and by our CI jobs as far as I concern). So, who knows what would happen if you use Admin account. Normally, I would not even respond much to such cases.  :wink:

-------------------------

gwald | 2017-01-02 01:11:40 UTC | #5

Thanks for the replies, 
I'll create a user and test it out, I appreciate the help.

-------------------------

