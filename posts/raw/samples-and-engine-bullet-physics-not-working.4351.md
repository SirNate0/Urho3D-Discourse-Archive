fnadalt | 2018-06-26 01:10:36 UTC | #1

Hi! Yesterday I upgraded my Arch linux and the engine (including samples) stopped working as they should, regarding physics I guess. I get the "Overflow in AABB, object removed from simulation" message, and my own project, which was working until yesterday, is messed up. I git cloned, compiled and installed Urho3D today. I don't know where to start looking! In my notebook, with a not upgraded archlinux, everything works fine. 

4.17.2-1-ARCH 64bit

-------------------------

Numerator | 2018-06-26 01:28:24 UTC | #2

Check the data for your meshes.  It may be bad.  One way to get that output, the distances between AABB is > 1e12.

You can put a breakpoint at 

	if ( colObj->isStaticObject() || ((maxAabb-minAabb).length2() < btScalar(1e12)))

in btCollisionWorld.cpp
void	btCollisionWorld::updateSingleAabb(btCollisionObject* colObj)
about line 172
and look the values in minAabb and maxAabb

-------------------------

weitjong | 2018-06-26 01:43:18 UTC | #3

Does your new ArchLinux come with GCC 8.x? If yes then you may be hitting this. If you are not using master branch, that is. 

https://github.com/urho3d/Urho3D/issues/2326

-------------------------

fnadalt | 2018-06-26 01:45:43 UTC | #4

The issue takes places with samples too

-------------------------

fnadalt | 2018-06-26 02:33:26 UTC | #5

Thanks... I'll try that

Compiled from master.  Vehicle sample physics crazy. Throws "Overflow in AABB"

-------------------------

weitjong | 2018-06-26 04:25:17 UTC | #6

FWIW, have you tried from a clean build tree?  Have you tried the debug build config? Any debug stacktrace? Also please indicate your GCC version.

-------------------------

fnadalt | 2018-06-26 16:03:47 UTC | #7

Github master branch compiled today with ./cmake_generic.sh -DCMAKE_BUILD_TYPE=Debug.
Last night I tried with stable 1.7... no Debug compilation... SAME.

Read, there's a "warning btCollisionDispatcher::needsCollision: static-static collision!" at the end...

Watch: https://drive.google.com/open?id=1Lt7XAxCxjMwhN-Zf6QQHDeBq2MDaERmm

[flaco@epubre bin]$ gcc -v
Usando especificaciones internas.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/lib/gcc/x86_64-pc-linux-gnu/8.1.1/lto-wrapper
Objetivo: x86_64-pc-linux-gnu
Configurado con: /build/gcc/src/gcc/configure --prefix=/usr --libdir=/usr/lib --libexecdir=/usr/lib --mandir=/usr/share/man --infodir=/usr/share/info --with-bugurl=https://bugs.archlinux.org/ --enable-languages=c,c++,ada,fortran,go,lto,objc,obj-c++ --enable-shared --enable-threads=posix --enable-libmpx --with-system-zlib --with-isl --enable-__cxa_atexit --disable-libunwind-exceptions --enable-clocale=gnu --disable-libstdcxx-pch --disable-libssp --enable-gnu-unique-object --enable-linker-build-id --enable-lto --enable-plugin --enable-install-libiberty --with-linker-hash-style=gnu --enable-gnu-indirect-function --enable-multilib --disable-werror --enable-checking=release --enable-default-pie --enable-default-ssp
Modelo de hilos: posix
gcc versión 8.1.1 20180531 (GCC) 

[flaco@epubre bin]$ ./Urho3DPlayer Data/Scripts/19_VehicleDemo.as 
[Tue Jun 26 12:53:16 2018] DEBUG: Initialising SDL
[Tue Jun 26 12:53:17 2018] INFO: Opened log file /home/flaco/.local/share/urho3d/logs/19_VehicleDemo.as.log
[Tue Jun 26 12:53:17 2018] INFO: Created 1 worker thread
[Tue Jun 26 12:53:17 2018] INFO: Added resource path /home/flaco/build/Urho3D/build/genericd/bin/Data/
[Tue Jun 26 12:53:17 2018] INFO: Added resource path /home/flaco/build/Urho3D/build/genericd/bin/CoreData/
[Tue Jun 26 12:53:17 2018] INFO: Added resource path /home/flaco/build/Urho3D/build/genericd/bin/Autoload/LargeData/
[Tue Jun 26 12:53:18 2018] INFO: Set screen mode 1680x1050 fullscreen monitor 0
[Tue Jun 26 12:53:18 2018] INFO: Initialized input
[Tue Jun 26 12:53:18 2018] INFO: Initialized user interface
[Tue Jun 26 12:53:18 2018] DEBUG: Loading resource Textures/Ramp.png
[Tue Jun 26 12:53:18 2018] DEBUG: Loading temporary resource Textures/Ramp.xml
[Tue Jun 26 12:53:18 2018] DEBUG: Loading resource Textures/Spot.png
[Tue Jun 26 12:53:18 2018] DEBUG: Loading temporary resource Textures/Spot.xml
[Tue Jun 26 12:53:18 2018] DEBUG: Loading resource Techniques/NoTexture.xml
[Tue Jun 26 12:53:18 2018] DEBUG: Loading resource RenderPaths/Forward.xml
[Tue Jun 26 12:53:18 2018] INFO: Initialized renderer
[Tue Jun 26 12:53:19 2018] INFO: Set audio mode 44100 Hz stereo interpolated
[Tue Jun 26 12:53:19 2018] INFO: Initialized engine
[Tue Jun 26 12:53:19 2018] DEBUG: Loading resource Scripts/19_VehicleDemo.as
[Tue Jun 26 12:53:19 2018] INFO: Scripts/19_VehicleDemo.as:43,1 Compiling void CreateScene()
[Tue Jun 26 12:53:19 2018] WARNING: Scripts/19_VehicleDemo.as:110,20 Variable 'body' hides another variable of same name in outer scope
[Tue Jun 26 12:53:19 2018] WARNING: Scripts/19_VehicleDemo.as:112,25 Variable 'shape' hides another variable of same name in outer scope
[Tue Jun 26 12:53:19 2018] INFO: Compiled script module Scripts/19_VehicleDemo.as
[Tue Jun 26 12:53:19 2018] DEBUG: Loading resource Textures/FishBoneLogo.png
[Tue Jun 26 12:53:19 2018] DEBUG: Loading temporary resource Textures/FishBoneLogo.xml
[Tue Jun 26 12:53:20 2018] DEBUG: Loading resource Textures/UrhoIcon.png
[Tue Jun 26 12:53:20 2018] DEBUG: Loading resource UI/DefaultStyle.xml
[Tue Jun 26 12:53:20 2018] DEBUG: Loading resource Textures/UI.png
[Tue Jun 26 12:53:20 2018] DEBUG: Loading temporary resource Textures/UI.xml
[Tue Jun 26 12:53:20 2018] DEBUG: Loading resource Fonts/Anonymous Pro.ttf
[Tue Jun 26 12:53:20 2018] DEBUG: Font face Anonymous Pro (11pt) has 624 glyphs
[Tue Jun 26 12:53:20 2018] DEBUG: Loading resource Textures/HeightMap.png
[Tue Jun 26 12:53:23 2018] DEBUG: Loading resource Materials/Terrain.xml
[Tue Jun 26 12:53:23 2018] DEBUG: Loading resource Techniques/TerrainBlend.xml
[Tue Jun 26 12:53:23 2018] DEBUG: Loading resource Textures/TerrainWeights.dds
[Tue Jun 26 12:53:23 2018] DEBUG: Loading resource Textures/TerrainDetail1.dds
[Tue Jun 26 12:53:23 2018] DEBUG: Loading resource Textures/TerrainDetail2.dds
[Tue Jun 26 12:53:23 2018] DEBUG: Loading resource Textures/TerrainDetail3.dds
[Tue Jun 26 12:53:23 2018] DEBUG: Loading resource Models/Mushroom.mdl
[Tue Jun 26 12:53:23 2018] DEBUG: Loading resource Materials/Mushroom.xml
[Tue Jun 26 12:53:23 2018] DEBUG: Loading resource Techniques/Diff.xml
[Tue Jun 26 12:53:23 2018] DEBUG: Loading resource Textures/Mushroom.dds
[Tue Jun 26 12:53:23 2018] DEBUG: Loading resource Models/Box.mdl
[Tue Jun 26 12:53:23 2018] DEBUG: Loading resource Materials/Stone.xml
[Tue Jun 26 12:53:23 2018] DEBUG: Loading resource Techniques/DiffNormal.xml
[Tue Jun 26 12:53:23 2018] DEBUG: Loading resource Textures/StoneDiffuse.dds
[Tue Jun 26 12:53:23 2018] DEBUG: Loading resource Textures/StoneNormal.dds
[Tue Jun 26 12:53:23 2018] DEBUG: Loading resource Models/Cylinder.mdl
[Tue Jun 26 12:53:23 2018] DEBUG: Font face Anonymous Pro (15pt) has 624 glyphs
[Tue Jun 26 12:53:23 2018] DEBUG: Reloading shaders
[Tue Jun 26 12:53:23 2018] DEBUG: Set occlusion buffer size 256x160 with 5 mip levels and 1 thread buffers
[Tue Jun 26 12:53:23 2018] DEBUG: Loading resource Shaders/GLSL/Shadow.glsl
[Tue Jun 26 12:53:23 2018] DEBUG: Loading resource Shaders/GLSL/TerrainBlend.glsl
[Tue Jun 26 12:53:23 2018] DEBUG: Loading resource Shaders/GLSL/LitSolid.glsl
[Tue Jun 26 12:53:23 2018] DEBUG: Compiled vertex shader Shadow(INSTANCED)
[Tue Jun 26 12:53:23 2018] DEBUG: Compiled pixel shader Shadow()
[Tue Jun 26 12:53:24 2018] DEBUG: Linked vertex shader Shadow(INSTANCED) and pixel shader Shadow()
[Tue Jun 26 12:53:24 2018] DEBUG: Compiled vertex shader Shadow()
[Tue Jun 26 12:53:24 2018] DEBUG: Linked vertex shader Shadow() and pixel shader Shadow()
[Tue Jun 26 12:53:24 2018] DEBUG: Compiled vertex shader LitSolid(DIRLIGHT INSTANCED NORMALMAP PERPIXEL SHADOW)
[Tue Jun 26 12:53:24 2018] DEBUG: Compiled pixel shader LitSolid(AMBIENT DIFFMAP DIRLIGHT NORMALMAP PACKEDNORMAL PCF_SHADOW PERPIXEL SHADOW SPECULAR)
[Tue Jun 26 12:53:24 2018] DEBUG: Linked vertex shader LitSolid(DIRLIGHT INSTANCED NORMALMAP PERPIXEL SHADOW) and pixel shader LitSolid(AMBIENT DIFFMAP DIRLIGHT NORMALMAP PACKEDNORMAL PCF_SHADOW PERPIXEL SHADOW SPECULAR)
[Tue Jun 26 12:53:24 2018] DEBUG: Compiled vertex shader LitSolid(DIRLIGHT NORMALMAP PERPIXEL SHADOW)
[Tue Jun 26 12:53:24 2018] DEBUG: Linked vertex shader LitSolid(DIRLIGHT NORMALMAP PERPIXEL SHADOW) and pixel shader LitSolid(AMBIENT DIFFMAP DIRLIGHT NORMALMAP PACKEDNORMAL PCF_SHADOW PERPIXEL SHADOW SPECULAR)
[Tue Jun 26 12:53:24 2018] DEBUG: Compiled vertex shader LitSolid(DIRLIGHT PERPIXEL SHADOW)
[Tue Jun 26 12:53:24 2018] DEBUG: Compiled pixel shader LitSolid(AMBIENT DIFFMAP DIRLIGHT PCF_SHADOW PERPIXEL SHADOW SPECULAR)
[Tue Jun 26 12:53:24 2018] DEBUG: Linked vertex shader LitSolid(DIRLIGHT PERPIXEL SHADOW) and pixel shader LitSolid(AMBIENT DIFFMAP DIRLIGHT PCF_SHADOW PERPIXEL SHADOW SPECULAR)
[Tue Jun 26 12:53:24 2018] DEBUG: Compiled vertex shader LitSolid(DIRLIGHT INSTANCED PERPIXEL SHADOW)
[Tue Jun 26 12:53:24 2018] DEBUG: Linked vertex shader LitSolid(DIRLIGHT INSTANCED PERPIXEL SHADOW) and pixel shader LitSolid(AMBIENT DIFFMAP DIRLIGHT PCF_SHADOW PERPIXEL SHADOW SPECULAR)
[Tue Jun 26 12:53:24 2018] DEBUG: Compiled vertex shader TerrainBlend(DIRLIGHT PERPIXEL SHADOW)
[Tue Jun 26 12:53:24 2018] DEBUG: Compiled pixel shader TerrainBlend(AMBIENT DIRLIGHT PCF_SHADOW PERPIXEL SHADOW SPECULAR)
[Tue Jun 26 12:53:24 2018] DEBUG: Linked vertex shader TerrainBlend(DIRLIGHT PERPIXEL SHADOW) and pixel shader TerrainBlend(AMBIENT DIRLIGHT PCF_SHADOW PERPIXEL SHADOW SPECULAR)
[Tue Jun 26 12:53:24 2018] DEBUG: Loading resource Shaders/GLSL/Basic.glsl
[Tue Jun 26 12:53:24 2018] DEBUG: Compiled vertex shader Basic(DIFFMAP VERTEXCOLOR)
[Tue Jun 26 12:53:24 2018] DEBUG: Compiled pixel shader Basic(DIFFMAP VERTEXCOLOR)
[Tue Jun 26 12:53:24 2018] DEBUG: Linked vertex shader Basic(DIFFMAP VERTEXCOLOR) and pixel shader Basic(DIFFMAP VERTEXCOLOR)
[Tue Jun 26 12:53:24 2018] DEBUG: Compiled pixel shader Basic(ALPHAMAP VERTEXCOLOR)
[Tue Jun 26 12:53:24 2018] DEBUG: Linked vertex shader Basic(DIFFMAP VERTEXCOLOR) and pixel shader Basic(ALPHAMAP VERTEXCOLOR)
warning btCollisionDispatcher::needsCollision: static-static collision!
[Tue Jun 26 12:53:25 2018] DEBUG: Quitting SDL

-------------------------

weitjong | 2018-06-26 23:59:14 UTC | #8

Thanks for the information. I am able to reproduce the issue in Fedora 28  with GCC 8.1.1 as well. I have reopened the issue in our issue tracker. In the meantime switch to Clang 6.0 (latest) compiler toolchain, the grass is greener there at the moment.

-------------------------

fnadalt | 2018-06-28 01:38:00 UTC | #9

hey, I did the following:
./cmake_generic.sh ./cmake_generic.sh build/generic-clang/ -DURHO3D_LUA=0 -DURHO3D_SAMPLES=0 -DCMAKE_CXX_COMPILER=/usr/bin/clang-6.0 -DCMAKE_C_COMPILER=/usr/bin/clang-6.0

...and at the time it's compiling Urho3DPlayer Error comes to the scene and stops compilation...
Moreover, I downloaded Urho3D-1.7-Linux-64bit-STATIC... guess what... c++ samples work... but Urho3DPlayer doesn't even initialize... freezes with black screen and mouse pointer... no error messages

-------------------------

weitjong | 2018-06-28 02:52:10 UTC | #10

That is not how I usually setup to use Clang. Usually I just `export CC=clang CXX=clang++` and have the compiler toolchain available in my PATH. That's basically an old convention and CMake honors it. I build my own Clang 6.0, but I don't think it should make any differences. In my build environment, it does not only build cleanly but also does not exhibit the runtime error you faced. Just tested a few days ago and the master branch did not move yet.

As for the prebuilt binary download, it does not prove anything. Those build artifacts were built using prior version of GCC (where the problem does not exist yet), and in fact they were using version 4.8.4 that our CI VM provides (this is an ancient GCC version using ancient C libraries provided by Ubuntu 14.04 that I actually a little surprise the binary could run at all in your box).

-------------------------

weitjong | 2018-07-06 02:03:45 UTC | #11

Alex has fixed this issue in the master branch. Give it a try.

-------------------------

fnadalt | 2018-07-06 02:42:57 UTC | #12

Yes sorry for not replying. Even before the PR I removed the cflag and worked... Thank you all

-------------------------

