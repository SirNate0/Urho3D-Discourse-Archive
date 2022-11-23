coho | 2017-01-02 01:06:11 UTC | #1

hey guys,
first for all,thank all of you for your amazing work on this great engine 
i build  run smooth on window7 64 bit and android.here the question:
when build with -DURHO3D_LUA = 1 for android 
get this error
Scanning dependencies of target tolua++
[ 62%] Creating directories for 'tolua++'
[ 62%] No download step for 'tolua++'
[ 63%] No patch step for 'tolua++'
[ 63%] No update step for 'tolua++'
[ 63%] Performing configure step for 'tolua++'
-- The C compiler identification is unknown
-- The CXX compiler identification is unknown
CMake Error: your C compiler: "CMAKE_C_COMPILER-NOTFOUND" was not found.   Pleas
e set CMAKE_C_COMPILER to a valid compiler path or name.
CMake Error: your CXX compiler: "CMAKE_CXX_COMPILER-NOTFOUND" was not found.   P
lease set CMAKE_CXX_COMPILER to a valid compiler path or name.
-- DirectX SDK search skipped for MinGW. It is assumed that MinGW itself comes w
ith the necessary headers & libraries
-- Configuring incomplete, errors occurred!
make[2]: *** [Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-configure]
Error 1
make[1]: *** [Source/Urho3D/CMakeFiles/tolua++.dir/all] Error 2
make: *** [all] Error 2

look like the tolua++ wrong with cmake setting and if build with  -DURHO3D_LUAJIT = 1
get same sort of error at libvm(not sure right name?), anybody get this problem,how to fix this
agian, thanks for this awesome  engine for free and opensource.

-------------------------

thebluefish | 2017-01-02 01:06:11 UTC | #2

Hi,

Please see this answer: [topic820.html](http://discourse.urho3d.io/t/i-cant-build-urho3d-with-lua-on-android/801/1)

-------------------------

coho | 2017-01-02 01:06:16 UTC | #3

ho,thank you reply that answe my question,
should find deep in forum

-------------------------

