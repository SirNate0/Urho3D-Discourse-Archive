CaptainCN | 2017-01-02 01:03:00 UTC | #1

I'm doing:
cmake_android.bat Android -DURHO3D_LUA=1
cd Android
make -j8


if build without lua, then there is no problem.and successful running.(sorry.I'm not good at english.)



Linking CXX static library libBox2D.a
[ 62%] "Built target Box2D"
Scanning dependencies of target tolua++
[ 62%] Creating directories for 'tolua++'
[ 62%] No download step for 'tolua++'
[ 63%] No patch step for 'tolua++'
[ 63%] No update step for 'tolua++'
[ 63%] Performing configure step for 'tolua++'
-- The C compiler identification is unknown
-- The CXX compiler identification is unknown
CMake Error at CMakeLists.txt:25 (project):
  No CMAKE_C_COMPILER could be found.

  Tell CMake where to find the compiler by setting either the environment
  variable "CC" or the CMake cache entry CMAKE_C_COMPILER to the full path to
  the compiler, or to the compiler name if it is in the PATH.


CMake Error at CMakeLists.txt:25 (project):
  No CMAKE_CXX_COMPILER could be found.

  Tell CMake where to find the compiler by setting either the environment
  variable "CXX" or the CMake cache entry CMAKE_CXX_COMPILER to the full path
  to the compiler, or to the compiler name if it is in the PATH.


-- Configuring incomplete, errors occurred!
See also "E:/work/Urho3D/Android/Source/Urho3D/tolua++-prefix/src/tolua++-build/CMakeFiles/CMakeOutput.log".
See also "E:/work/Urho3D/Android/Source/Urho3D/tolua++-prefix/src/tolua++-build/CMakeFiles/CMakeError.log".
make[2]: *** [Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-configure] Error 1
make[1]: *** [Source/Urho3D/CMakeFiles/tolua++.dir/all] Error 2
make: *** [all] Error 2

-------------------------

weitjong | 2017-01-02 01:03:00 UTC | #2

Welcome to our forum.

This has been discussed in [topic729.html](http://discourse.urho3d.io/t/new-build-system/715/1). Short answer: On Windows host system, you need to install MinGW compiler toolchain besides Android NDK compiler toolchain; and also make sure that CMake is able to find both the compiler toolchains.

-------------------------

CaptainCN | 2017-01-02 01:03:01 UTC | #3

[quote="weitjong"]Welcome to our forum.

This has been discussed in [topic729.html](http://discourse.urho3d.io/t/new-build-system/715/1). Short answer: On Windows host system, you need to install MinGW compiler toolchain besides Android NDK compiler toolchain; and also make sure that CMake is able to find both the compiler toolchains.[/quote]
 :frowning: oh no. I think MinGW not good for new users. hard to configuration, to huge and download it slowly(I'm in china, you know.).

-------------------------

weitjong | 2017-01-02 01:03:01 UTC | #4

I know exactly how it feels with slow download. Long ago I lived in Indonesia where using a dial up modem was a norm and 56k was actually already a luxury  :wink: . But I am a little surprised that you are implying China does not have fast broadband internet today. I use PPTV to stream Holywood movies directly from China servers to my Apple TV almost every night. Buffering free most of the time  :laughing: .

Anyway, should you decide to give it a try. Use this link [mingw-w64.sourceforge.net/download.php](http://mingw-w64.sourceforge.net/download.php).

-------------------------

