felipeac | 2017-01-02 01:12:36 UTC | #1

Hi, I've just started using Urho3D a few days ago and I'm also a newbie at C++. I use arch linux. I'm trying to compile my game for windows using the cmake_mingw.sh script, but it keeps giving me errors. It says it couldn't find a compatible URHO3D_HOME directory, while it works when I use the standard cmake_generic.sh script. Do I have to recompile Urho3D specifically for windows, put it in another directory and set the URHO3D_HOME environment variable to that directory? I have mingw already setup with the MINGW_PREFIX and MINGW_SYSROOT environment variables.

-------------------------

weitjong | 2017-01-02 01:12:37 UTC | #2

Welcome to our forum. I think you have already answered your question yourself. The Urho3D library for Windows and for (native) Linux must be built separately and keep in their own build tree. The URHO3D_HOME for your own game project must be configured to point to one of these two build tree locations depending on whether you are targeting Windows or Linux. Naturally you can also target both platforms at the same time and if so, just have your own project's build tree separated, one for Windows and one for Linux as well. Your source tree should be just in one location, same as Urho3D project source tree is. Our build system does not care how many build trees you have.

-------------------------

felipeac | 2017-01-02 01:12:39 UTC | #3

Ok, I cloned the Urho3D repository to another location, executed "./cmake_mingw.sh Build && cd Build" and then I tried to compile it with "make", but that ended up giving me this error:

[code]In file included from /storage/Urho3DWin/Source/ThirdParty/Bullet/src/LinearMath/btAlignedObjectArray.h:20:0,
                 from /storage/Urho3DWin/Source/ThirdParty/Bullet/src/LinearMath/btHashMap.h:20,
                 from /storage/Urho3DWin/Source/ThirdParty/Bullet/src/BulletCollision/CollisionDispatch/btInternalEdgeUtility.h:5,
                 from /storage/Urho3DWin/Source/ThirdParty/Bullet/src/BulletCollision/CollisionDispatch/btInternalEdgeUtility.cpp:1:
/storage/Urho3DWin/Source/ThirdParty/Bullet/src/LinearMath/btScalar.h: In member function ?virtual void btConnectivityProcessor::processTriangle(btVector3*, int, int)?:
/storage/Urho3DWin/Source/ThirdParty/Bullet/src/LinearMath/btScalar.h:448:16: internal compiler error: Segmentation fault
  return sqrtf(y);
                ^
Please submit a full bug report,
with preprocessed source if appropriate.
See <http://gcc.gnu.org/bugs.html> for instructions.
Source/ThirdParty/Bullet/CMakeFiles/Bullet.dir/build.make:326: recipe for target 'Source/ThirdParty/Bullet/CMakeFiles/Bullet.dir/src/BulletCollision/CollisionDispatch/btInternalEdgeUtility.cpp.obj' failed
make[2]: *** [Source/ThirdParty/Bullet/CMakeFiles/Bullet.dir/src/BulletCollision/CollisionDispatch/btInternalEdgeUtility.cpp.obj] Error 1
CMakeFiles/Makefile2:1240: recipe for target 'Source/ThirdParty/Bullet/CMakeFiles/Bullet.dir/all' failed
make[1]: *** [Source/ThirdParty/Bullet/CMakeFiles/Bullet.dir/all] Error 2
Makefile:149: recipe for target 'all' failed
make: *** [all] Error 2[/code]

-------------------------

weitjong | 2017-01-02 01:12:39 UTC | #4

I am sorry to hear that. It seems something is still wrongly setup at your side, but we could not tell exactly what from what you have posted so far. Perhaps you should try to isolate your problem first, say, by building other more simple project or a simple HelloWorld first to verify you have a working MinGW build environment. BTW, you don't need to do a separate clone for each target platform. Rather in any build/host system, just perform  a clone once and that will be your one and only Urho3D source tree. From that single source tree, use CMake to generate as many build trees you like. You only need to maintain the source code in one place, regardless of how many build tress you have. Naturally it is easier to manage if your build trees are uniquely named, such as: native-Build (for Linux build), mingw-Build (for MingW build), android-Build (for Android build), for example.

-------------------------

felipeac | 2017-01-02 01:12:43 UTC | #5

Hey, I just tried to compile it with mingw on my ubuntu 14.04 VM and it worked this time. I guess it's something to do with the version of mingw in the arch linux repositories.

-------------------------

jmiller | 2017-01-02 01:12:44 UTC | #6

[quote="felipeac"]Hey, I just tried to compile it with mingw on my ubuntu 14.04 VM and it worked this time. I guess it's something to do with the version of mingw in the arch linux repositories.[/quote]

Indeed, there are several bugs (some obscure) affecting different versions and I have encountered your bug recently on x86-64 host.

I was happy to see mingw-w64 with a current gcc 6, but the builds I have tried would not debug shared objects or had other issues.. but tomorrow could be success. Official mingw-w64 gcc 5.3 seems to be working for now...

For Urho, I cmake with [b]-D MINGW_SYSROOT="C:/mingw/x86_64-w64-mingw32"[/b]

In other notes: under C++11, Bullet currently needs [b]-Wno-error=narrowing[/b] to successfully compile.

-------------------------

