lexx | 2017-06-12 12:18:13 UTC | #1

I have a problem while compiling to android (w7, newest android sdk and ndk, newest urho3d from github).

* I setup some paths:
> set path="%PATH%;c:\android-ndk-r15\prebuilt\windows-x86_64\bin;C:\android-ndk-r15\build;C:\Program Files (x86)\Android\android-sdk\tools;C:\Program Files (x86)\Android\android-sdk\tools\bin;C:\Program Files (x86)\Android\android-sdk\platform-tools"
> set path="%PATH%;C:\Program Files\CMake\bin"
> 	
> set ANDROID_NDK=c:\android-ndk-r15

> call cmake_android.bat  Build

I think cmake starts right:
> -- The C compiler identification is Clang 5.0.300080
> -- The CXX compiler identification is Clang 5.0.300080
> -- Check for working C compiler: c:/android-ndk-r15/toolchains/llvm/prebuilt/win
> dows-x86_64/bin/clang.exe
> -- Check for working C compiler: c:/android-ndk-r15/toolchains/llvm/prebuilt/win
> dows-x86_64/bin/clang.exe -- works
> -- Detecting C compiler ABI info
> -- Detecting C compiler ABI info - done
> -- Detecting C compile features
> -- Detecting C compile features - done
> -- Check for working CXX compiler: c:/android-ndk-r15/toolchains/llvm/prebuilt/w
> indows-x86_64/bin/clang++.exe
> -- Check for working CXX compiler: c:/android-ndk-r15/toolchains/llvm/prebuilt/w
> indows-x86_64/bin/clang++.exe -- works
> -- Detecting CXX compiler ABI info
> -- Detecting CXX compiler ABI info - done
> -- Detecting CXX compile features
> -- Detecting CXX compile features - done
> -- Looking for stdint.h
> -- Looking for stdint.h - found
> -- Looking for inttypes.h

etc etc..


But in the end:
> -- The ASM compiler identification is GNU
> -- Found assembler: c:/android-ndk-r15/toolchains/arm-linux-androideabi-4.9/preb
> uilt/windows-x86_64/bin/arm-linux-androideabi-gcc.exe
> -- Performing Test HAVE_NATIVE_COMPILER
> -- Performing Test HAVE_NATIVE_COMPILER - Failed
> CMake Error at CMake/Modules/CheckCompilerToolchain.cmake:134 (message):
>   Could not find native compiler toolchain.  This is usually caused by wrong
>   PATH env-var value.

>   CMake Error in CMakeLists.txt:

>     No CMAKE_C_COMPILER could be found.

>     Tell CMake where to find the compiler by setting either the environment
>     variable "CC" or the CMake cache entry CMAKE_C_COMPILER to the full path to
>     the compiler, or to the compiler name if it is in the PATH.

>   CMake Error in CMakeLists.txt:

>     No CMAKE_CXX_COMPILER could be found.

>     Tell CMake where to find the compiler by setting either the environment
>     variable "CXX" or the CMake cache entry CMAKE_CXX_COMPILER to the full path
>     to the compiler, or to the compiler name if it is in the PATH.

> Call Stack (most recent call first):
>   Source/Urho3D/CMakeLists.txt:195 (check_native_compiler_exist)

-------------------------

weitjong | 2017-06-12 16:57:13 UTC | #2

That error is typically happened in Windows host system. Our build system is designed in such a way that it builds all the targets (either cross-compiling or native one), plus all the build tools that it required for the build itself on the fly in a single "make" process. The tricky part is the building of the build tool, which of course has to be built as native target using a native compiler toolchain. Now back to your problem, when using Windows host system to target Android platform, you actually need two compiler toolchains: Android NDK and MinGW (or something like that) in the PATH so that CMake can find them. Good luck.

-------------------------

lexx | 2017-06-12 16:57:35 UTC | #3

Installed MinGW and got libraries and examples compiled.

Thanks.

-------------------------

