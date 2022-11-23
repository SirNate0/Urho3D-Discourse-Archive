hsl9999 | 2017-01-02 01:05:27 UTC | #1

env:win7 64
urho3d 1.4
cmake:3.2.2

ANDORID_NDK   D:\NVPACK\android-ndk-r10d
add Path :  D:\NVPACK\android-ndk-r10d\toolchains\arm-linux-androideabi-4.9\prebuilt\windows-x86_64\bin;

error:
Looking for include file stdint.h
Looking for include file stdint.h - found
The ASM compiler identification is GNU
Found assembler: D:/NVPACK/android-ndk-r10d/toolchains/arm-linux-androideabi-4.9/prebuilt/windows-x86_64/bin/arm-linux-androideabi-gcc.exe
Performing Test COMPILER_HAS_HIDDEN_VISIBILITY
Performing Test COMPILER_HAS_HIDDEN_VISIBILITY - Failed
Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY
Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY - Failed
Performing Test COMPILER_HAS_DEPRECATED_ATTR
Performing Test COMPILER_HAS_DEPRECATED_ATTR - Failed
Performing Test COMPILER_HAS_DEPRECATED
Performing Test COMPILER_HAS_DEPRECATED - Failed
arm-linux-androideabi-g++.exe: error: CreateProcess: No such file or directory

CMake Error at CMake/Modules/Urho3D-CMake-common.cmake:662 (message):
  The configured compiler toolchain in the build tree is not able to handle
  all the compiler flags required to build the project.  Please kindly update
  your compiler toolchain to its latest version.  If you are using MinGW then
  make sure it is MinGW-W64 instead of MinGW-W32 or TDM-GCC (Code::Blocks
  default).  However, if you think there is something wrong with the compiler
  flags being used then please file a bug report to the project devs.
Call Stack (most recent call first):
  CMake/Modules/Urho3D-CMake-common.cmake:718 (enable_pch)
  CMake/Modules/Urho3D-CMake-common.cmake:774 (setup_target)
  Source/Urho3D/CMakeLists.txt:174 (setup_library)

error log:
Performing C++ SOURCE FILE Test COMPILER_HAS_HIDDEN_VISIBILITY failed with the following output:
Change Dir: E:/Urho3D/AndroidBuild/CMakeFiles/CMakeTmp

Run Build Command:"D:/NVPACK/android-ndk-r10d/prebuilt/windows-x86_64/bin/make.exe" "cmTryCompileExec3046427120/fast"
D:/NVPACK/android-ndk-r10d/prebuilt/windows-x86_64/bin/make.exe -f CMakeFiles/cmTryCompileExec3046427120.dir/build.make CMakeFiles/cmTryCompileExec3046427120.dir/build

make.exe[1]: Entering directory `E:/Urho3D/AndroidBuild/CMakeFiles/CMakeTmp'

"D:/Program Files (x86)/CMake/bin/cmake.exe" -E cmake_progress_report E:/Urho3D/AndroidBuild/CMakeFiles/CMakeTmp/CMakeFiles 1

"Building CXX object CMakeFiles/cmTryCompileExec3046427120.dir/src.cxx.o"

D:/NVPACK/android-ndk-r10d/toolchains/arm-linux-androideabi-4.9/prebuilt/windows-x86_64/bin/arm-linux-androideabi-g++.exe   -DANDROID -fexceptions -frtti -fPIC -Wno-psabi --sysroot=D:/NVPACK/android-ndk-r10d/platforms/android-12/arch-arm -funwind-tables -finline-limit=64 -fsigned-char -no-canonical-prefixes -march=armv7-a -mfloat-abi=softfp -mfpu=vfpv3-d16 -fdata-sections -ffunction-sections -Wa,--noexecstack  -Wno-invalid-offsetof -fstack-protector -DCOMPILER_HAS_HIDDEN_VISIBILITY -fPIE -isystem D:/NVPACK/android-ndk-r10d/platforms/android-12/arch-arm/usr/include -isystem D:/NVPACK/android-ndk-r10d/sources/cxx-stl/gnu-libstdc++/4.9/include -isystem D:/NVPACK/android-ndk-r10d/sources/cxx-stl/gnu-libstdc++/4.9/libs/armeabi-v7a/include -isystem D:/NVPACK/android-ndk-r10d/sources/cxx-stl/gnu-libstdc++/4.9/include/backward    -fvisibility=hidden -o CMakeFiles/cmTryCompileExec3046427120.dir/src.cxx.o -c E:/Urho3D/AndroidBuild/CMakeFiles/CMakeTmp/src.cxx

arm-linux-androideabi-g++.exe: error: CreateProcess: No such file or directory

make.exe[1]: *** [CMakeFiles/cmTryCompileExec3046427120.dir/src.cxx.o] Error 1

make.exe[1]: Leaving directory `E:/Urho3D/AndroidBuild/CMakeFiles/CMakeTmp'

make.exe: *** [cmTryCompileExec3046427120/fast] Error 2


Source file was:
int main() { return 0; }
Performing C++ SOURCE FILE Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY failed with the following output:
Change Dir: E:/Urho3D/AndroidBuild/CMakeFiles/CMakeTmp

Run Build Command:"D:/NVPACK/android-ndk-r10d/prebuilt/windows-x86_64/bin/make.exe" "cmTryCompileExec57645084/fast"
D:/NVPACK/android-ndk-r10d/prebuilt/windows-x86_64/bin/make.exe -f CMakeFiles/cmTryCompileExec57645084.dir/build.make CMakeFiles/cmTryCompileExec57645084.dir/build

make.exe[1]: Entering directory `E:/Urho3D/AndroidBuild/CMakeFiles/CMakeTmp'

"D:/Program Files (x86)/CMake/bin/cmake.exe" -E cmake_progress_report E:/Urho3D/AndroidBuild/CMakeFiles/CMakeTmp/CMakeFiles 1

"Building CXX object CMakeFiles/cmTryCompileExec57645084.dir/src.cxx.o"

D:/NVPACK/android-ndk-r10d/toolchains/arm-linux-androideabi-4.9/prebuilt/windows-x86_64/bin/arm-linux-androideabi-g++.exe   -DANDROID -fexceptions -frtti -fPIC -Wno-psabi --sysroot=D:/NVPACK/android-ndk-r10d/platforms/android-12/arch-arm -funwind-tables -finline-limit=64 -fsigned-char -no-canonical-prefixes -march=armv7-a -mfloat-abi=softfp -mfpu=vfpv3-d16 -fdata-sections -ffunction-sections -Wa,--noexecstack  -Wno-invalid-offsetof -fstack-protector -DCOMPILER_HAS_HIDDEN_INLINE_VISIBILITY -fPIE -isystem D:/NVPACK/android-ndk-r10d/platforms/android-12/arch-arm/usr/include -isystem D:/NVPACK/android-ndk-r10d/sources/cxx-stl/gnu-libstdc++/4.9/include -isystem D:/NVPACK/android-ndk-r10d/sources/cxx-stl/gnu-libstdc++/4.9/libs/armeabi-v7a/include -isystem D:/NVPACK/android-ndk-r10d/sources/cxx-stl/gnu-libstdc++/4.9/include/backward    -fvisibility-inlines-hidden -o CMakeFiles/cmTryCompileExec57645084.dir/src.cxx.o -c E:/Urho3D/AndroidBuild/CMakeFiles/CMakeTmp/src.cxx

arm-linux-androideabi-g++.exe: error: CreateProcess: No such file or directory

make.exe[1]: Leaving directory `E:/Urho3D/AndroidBuild/CMakeFiles/CMakeTmp'

make.exe[1]: *** [CMakeFiles/cmTryCompileExec57645084.dir/src.cxx.o] Error 1

make.exe: *** [cmTryCompileExec57645084/fast] Error 2


Source file was:
int main() { return 0; }
Performing C++ SOURCE FILE Test COMPILER_HAS_DEPRECATED_ATTR failed with the following output:
Change Dir: E:/Urho3D/AndroidBuild/CMakeFiles/CMakeTmp

Run Build Command:"D:/NVPACK/android-ndk-r10d/prebuilt/windows-x86_64/bin/make.exe" "cmTryCompileExec772191057/fast"
D:/NVPACK/android-ndk-r10d/prebuilt/windows-x86_64/bin/make.exe -f CMakeFiles/cmTryCompileExec772191057.dir/build.make CMakeFiles/cmTryCompileExec772191057.dir/build

make.exe[1]: Entering directory `E:/Urho3D/AndroidBuild/CMakeFiles/CMakeTmp'

"D:/Program Files (x86)/CMake/bin/cmake.exe" -E cmake_progress_report E:/Urho3D/AndroidBuild/CMakeFiles/CMakeTmp/CMakeFiles 1

"Building CXX object CMakeFiles/cmTryCompileExec772191057.dir/src.cxx.o"

D:/NVPACK/android-ndk-r10d/toolchains/arm-linux-androideabi-4.9/prebuilt/windows-x86_64/bin/arm-linux-androideabi-g++.exe   -DANDROID -fexceptions -frtti -fPIC -Wno-psabi --sysroot=D:/NVPACK/android-ndk-r10d/platforms/android-12/arch-arm -funwind-tables -finline-limit=64 -fsigned-char -no-canonical-prefixes -march=armv7-a -mfloat-abi=softfp -mfpu=vfpv3-d16 -fdata-sections -ffunction-sections -Wa,--noexecstack  -Wno-invalid-offsetof -fstack-protector -DCOMPILER_HAS_DEPRECATED_ATTR -fPIE -isystem D:/NVPACK/android-ndk-r10d/platforms/android-12/arch-arm/usr/include -isystem D:/NVPACK/android-ndk-r10d/sources/cxx-stl/gnu-libstdc++/4.9/include -isystem D:/NVPACK/android-ndk-r10d/sources/cxx-stl/gnu-libstdc++/4.9/libs/armeabi-v7a/include -isystem D:/NVPACK/android-ndk-r10d/sources/cxx-stl/gnu-libstdc++/4.9/include/backward    -o CMakeFiles/cmTryCompileExec772191057.dir/src.cxx.o -c E:/Urho3D/AndroidBuild/CMakeFiles/CMakeTmp/src.cxx

arm-linux-androideabi-g++.exe: error: CreateProcess: No such file or directory

make.exe[1]: *** [CMakeFiles/cmTryCompileExec772191057.dir/src.cxx.o] Error 1

make.exe[1]: Leaving directory `E:/Urho3D/AndroidBuild/CMakeFiles/CMakeTmp'

make.exe: *** [cmTryCompileExec772191057/fast] Error 2


Source file was:
__attribute__((__deprecated__)) int somefunc() { return 0; }
    int main() { return somefunc();}
Performing C++ SOURCE FILE Test COMPILER_HAS_DEPRECATED failed with the following output:
Change Dir: E:/Urho3D/AndroidBuild/CMakeFiles/CMakeTmp

Run Build Command:"D:/NVPACK/android-ndk-r10d/prebuilt/windows-x86_64/bin/make.exe" "cmTryCompileExec72661732/fast"
D:/NVPACK/android-ndk-r10d/prebuilt/windows-x86_64/bin/make.exe -f CMakeFiles/cmTryCompileExec72661732.dir/build.make CMakeFiles/cmTryCompileExec72661732.dir/build

make.exe[1]: Entering directory `E:/Urho3D/AndroidBuild/CMakeFiles/CMakeTmp'

"D:/Program Files (x86)/CMake/bin/cmake.exe" -E cmake_progress_report E:/Urho3D/AndroidBuild/CMakeFiles/CMakeTmp/CMakeFiles 1

"Building CXX object CMakeFiles/cmTryCompileExec72661732.dir/src.cxx.o"

D:/NVPACK/android-ndk-r10d/toolchains/arm-linux-androideabi-4.9/prebuilt/windows-x86_64/bin/arm-linux-androideabi-g++.exe   -DANDROID -fexceptions -frtti -fPIC -Wno-psabi --sysroot=D:/NVPACK/android-ndk-r10d/platforms/android-12/arch-arm -funwind-tables -finline-limit=64 -fsigned-char -no-canonical-prefixes -march=armv7-a -mfloat-abi=softfp -mfpu=vfpv3-d16 -fdata-sections -ffunction-sections -Wa,--noexecstack  -Wno-invalid-offsetof -fstack-protector -DCOMPILER_HAS_DEPRECATED -fPIE -isystem D:/NVPACK/android-ndk-r10d/platforms/android-12/arch-arm/usr/include -isystem D:/NVPACK/android-ndk-r10d/sources/cxx-stl/gnu-libstdc++/4.9/include -isystem D:/NVPACK/android-ndk-r10d/sources/cxx-stl/gnu-libstdc++/4.9/libs/armeabi-v7a/include -isystem D:/NVPACK/android-ndk-r10d/sources/cxx-stl/gnu-libstdc++/4.9/include/backward    -o CMakeFiles/cmTryCompileExec72661732.dir/src.cxx.o -c E:/Urho3D/AndroidBuild/CMakeFiles/CMakeTmp/src.cxx

arm-linux-androideabi-g++.exe: error: CreateProcess: No such file or directory

make.exe[1]: *** [CMakeFiles/cmTryCompileExec72661732.dir/src.cxx.o] Error 1

make.exe[1]: Leaving directory `E:/Urho3D/AndroidBuild/CMakeFiles/CMakeTmp'

make.exe: *** [cmTryCompileExec72661732/fast] Error 2


Source file was:
__declspec(deprecated) int somefunc() { return 0; }
    int main() { return somefunc();}

-------------------------

weitjong | 2017-01-02 01:05:27 UTC | #2

I have not used NVPACK before. Can you verify "arm-linux-androideabi-g++.exe" can be found using your current configured path. Try executing "arm-linux-androideabi-g++.exe --version" in a cmd shell. Rightfully, I think it should be found in the "D:\NVPACK\android-ndk-r10d\toolchains\arm-linux-androideabi-4.9\prebuilt\windows-x86_64\bin" in your case. But I am not sure why it does not work for you as you have that path added to your PATH environment variable already. There are two logical plausible explanations:
1. NVPACK is not installed correctly. Try to reinstall it or try to use Google Android NDK.
2. You have configured your PATH environment variable wrongly. Sometimes it is the obvious that causes the problem.

-------------------------

hsl9999 | 2017-01-02 01:05:28 UTC | #3

to weitjong:
You are right,NVPACK is not installed correctly.thanks.

-------------------------

