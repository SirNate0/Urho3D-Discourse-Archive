OvermindDL1 | 2017-01-02 01:01:17 UTC | #1

Since the project is not a full CMake project and requires running a script to start the build (cmake_gcc in my case), it seems the cmake generator is hardcoded to "Unix Makefiles" when I prefer to use "Ninja" as it is a great deal faster at compiling projects (not so much for urho3d since it is not so recursive, but it works fine for uhro3d and fits my build system better).  Any chance of making it so we can pass a -G option to the cmake_gcc.sh script to override it (see: man getopt), or better yet, fix the cmake scripts so the have the functionailty of the scripts so the scripts do not need to exist so it can fit in to normal build systems?  :slight_smile:

EDIT:  For note, a Ninja build on my system results (this was while my system was heavily loaded with another program eating about 15 gigs of ram...):
[spoiler][code]
overminddl1@overmind:~/projects/Urho3D$ ./cmake_gcc.sh -DURHO3D_64BIT=1 -DURHO3D_LUA=1 -DURHO3D_LUAJIT=1 -DURHO3D_LUAJIT_AMALG=1 -DURHO3D_SAMPLES=1 -DURHO3D_EXTRAS=1 -DURHO3D_DOCS=1 -DURHO3D_OPENGL=1 -DURHO3D_STATIC_RUNTIME=1 -DURHO3D_LIB_TYPE=STATIC -DCMAKE_BUILD_TYPE=Release

Native build
================================================================================
-- The C compiler identification is GNU 4.8.2
-- The CXX compiler identification is GNU 4.8.2
-- Check for working C compiler using: Ninja
-- Check for working C compiler using: Ninja -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler using: Ninja
-- Check for working CXX compiler using: Ninja -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Looking for include file stdint.h
-- Looking for include file stdint.h - found
-- Looking for XOpenDisplay in /usr/lib/x86_64-linux-gnu/libX11.so;/usr/lib/x86_64-linux-gnu/libXext.so
-- Looking for XOpenDisplay in /usr/lib/x86_64-linux-gnu/libX11.so;/usr/lib/x86_64-linux-gnu/libXext.so - found
-- Looking for gethostbyname
-- Looking for gethostbyname - found
-- Looking for connect
-- Looking for connect - found
-- Looking for remove
-- Looking for remove - found
-- Looking for shmat
-- Looking for shmat - found
-- Looking for IceConnectionNumber in ICE
-- Looking for IceConnectionNumber in ICE - found
-- Found X11: /usr/lib/x86_64-linux-gnu/libX11.so
-- Found OpenGL: /usr/lib/x86_64-linux-gnu/libGL.so  
-- Following tests check whether X11 library installed in this system uses _Xconst in below functions
-- A failed test result simply means the installed X11 library does not use _Xconst
-- It is OK to proceed to build Urho3D regardless of the test result
-- Performing Test HAVE_CONST_XEXT_ADDDISPLAY
-- Performing Test HAVE_CONST_XEXT_ADDDISPLAY - Success
-- Performing Test HAVE_CONST_XDATA32
-- Performing Test HAVE_CONST_XDATA32 - Success
-- Found ALSA: /usr/lib/x86_64-linux-gnu/libasound.so (found version "1.0.27.2") 
-- Finding value for LuaJIT:TARGET_LJARCH
-- Finding value for LuaJIT:TARGET_LJARCH - found (X64)
-- Finding value for LuaJIT:PS3
-- Finding value for LuaJIT:NO_UNWIND
-- Finding value for LuaJIT:ARCH_BITS
-- Finding value for LuaJIT:ARCH_BITS - found (64)
-- Finding value for LuaJIT:HASJIT
-- Finding value for LuaJIT:HASJIT - found (1)
-- Finding value for LuaJIT:HASFFI
-- Finding value for LuaJIT:HASFFI - found (1)
-- Finding value for LuaJIT:DUALNUM
-- Finding value for LuaJIT:ARCH_HASFPU
-- Finding value for LuaJIT:ARCH_HASFPU - found (1)
-- Finding value for LuaJIT:ABI_SOFTFP
-- Finding value for LuaJIT:ARCH_VERSION
-- The ASM compiler identification is GNU
-- Found assembler: /usr/bin/cc
-- Performing Test COMPILER_HAS_HIDDEN_VISIBILITY
-- Performing Test COMPILER_HAS_HIDDEN_VISIBILITY - Success
-- Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY
-- Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY - Success
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR - Success
-- Found Urho3D: as CMake target
-- Configuring done
-- Generating done
-- Build files have been written to: /home/overminddl1/projects/Urho3D/Build
overminddl1@overmind:~/projects/Urho3D$ cd Build
overminddl1@overmind:~/projects/Urho3D/Build$ time ninja
[199/991] Building C object ThirdParty/toluapp/src/lib/CMakeFiles/toluapp.dir/tolua_map.c.o
/home/overminddl1/projects/Urho3D/Source/ThirdParty/toluapp/src/lib/tolua_map.c: In function ?tolua_usertype?:
/home/overminddl1/projects/Urho3D/Source/ThirdParty/toluapp/src/lib/tolua_map.c:398:2: warning: passing argument 2 of ?tolua_newmetatable? discards ?const? qualifier from pointer target type [enabled by default]
  if (tolua_newmetatable(L,ctype) && tolua_newmetatable(L,type))
  ^
/home/overminddl1/projects/Urho3D/Source/ThirdParty/toluapp/src/lib/tolua_map.c:28:12: note: expected ?char *? but argument is of type ?const char *?
 static int tolua_newmetatable (lua_State* L, char* name)
            ^
[224/991] Building CXX object ThirdParty/StanHull/CMakeFiles/StanHull.dir/hull.cpp.o
/home/overminddl1/projects/Urho3D/Source/ThirdParty/StanHull/hull.cpp: In function ?int StanHull::overhull(StanHull::Plane*, int, StanHull::float3*, int, int, StanHull::float3*&, int&, int*&, int&, float)?:
/home/overminddl1/projects/Urho3D/Source/ThirdParty/StanHull/hull.cpp:2590:28: warning: converting to non-pointer type ?int? from NULL [-Wconversion-null]
  if(verts_count <4) return NULL;
                            ^
[273/991] Building CXX object ThirdParty/kNet/CMakeFiles/kNet.dir/src/unix/UnixEvent.cpp.o
/home/overminddl1/projects/Urho3D/Source/ThirdParty/kNet/src/unix/UnixEvent.cpp: In member function ?void kNet::Event::Set()?:
/home/overminddl1/projects/Urho3D/Source/ThirdParty/kNet/src/unix/UnixEvent.cpp:157:32: warning: ignoring return value of ?ssize_t read(int, void*, size_t)?, declared with attribute warn_unused_result [-Wunused-result]
  read(fd[0], &val, sizeof(val));
                                ^
[384/991] Building CXX object ThirdParty/Bullet/CMakeFiles/Bullet.dir/src/BulletCollision/CollisionShapes/btCompoundShape.cpp.o
/home/overminddl1/projects/Urho3D/Source/ThirdParty/Bullet/src/BulletCollision/CollisionShapes/btCompoundShape.cpp: In member function ?void btCompoundShape::addChildShape(const btTransform&, btCollisionShape*)?:
/home/overminddl1/projects/Urho3D/Source/ThirdParty/Bullet/src/BulletCollision/CollisionShapes/btCompoundShape.cpp:81:58: warning: cast to pointer from integer of different size [-Wint-to-pointer-cast]
   child.m_node = m_dynamicAabbTree->insert(bounds,(void*)index);
                                                          ^
/home/overminddl1/projects/Urho3D/Source/ThirdParty/Bullet/src/BulletCollision/CollisionShapes/btCompoundShape.cpp: In member function ?void btCompoundShape::createAabbTreeFromChildren()?:
/home/overminddl1/projects/Urho3D/Source/ThirdParty/Bullet/src/BulletCollision/CollisionShapes/btCompoundShape.cpp:315:68: warning: cast to pointer from integer of different size [-Wint-to-pointer-cast]
             child.m_node = m_dynamicAabbTree->insert(bounds,(void*)index);
                                                                    ^
[460/991] Building C object ThirdParty/LibCpuId/CMakeFiles/LibCpuId.dir/src/rdtsc.c.o
/home/overminddl1/projects/Urho3D/Source/ThirdParty/LibCpuId/src/rdtsc.c: In function ?cpu_clock_by_ic?:
/home/overminddl1/projects/Urho3D/Source/ThirdParty/LibCpuId/src/rdtsc.c:268:3: warning: format ?%llu? expects argument of type ?long long unsigned int?, but argument 4 has type ?uint64_t? [-Wformat=]
   debugf(2, "c = %d, td = %llu\n", c, t1 - t0);
   ^
[527/991] Generating tolua++ API binding on the fly for IO

** tolua warning: Mapping variable to global may degrade performance.

[528/991] Generating tolua++ API binding on the fly for Network

** tolua warning: Mapping variable to global may degrade performance.

[530/991] Generating tolua++ API binding on the fly for Audio

** tolua warning: Mapping variable to global may degrade performance.

[532/991] Generating tolua++ API binding on the fly for Urho2D

** tolua warning: Mapping variable to global may degrade performance.

[533/991] Generating tolua++ API binding on the fly for Resource

** tolua warning: Mapping variable to global may degrade performance.

[534/991] Generating tolua++ API binding on the fly for Engine

** tolua warning: Mapping variable to global may degrade performance.

[535/991] Generating tolua++ API binding on the fly for Input

** tolua warning: Mapping variable to global may degrade performance.

[536/991] Generating tolua++ API binding on the fly for Scene

** tolua warning: Mapping variable to global may degrade performance.

[537/991] Generating tolua++ API binding on the fly for Core

** tolua warning: No support for operator =, ignoring.


** tolua warning: Mapping variable to global may degrade performance.

[538/991] Generating tolua++ API binding on the fly for UI

** tolua warning: Mapping variable to global may degrade performance.

[540/991] Generating tolua++ API binding on the fly for Math

** tolua warning: Mapping variable to global may degrade performance.

[541/991] Generating tolua++ API binding on the fly for Graphics

** tolua warning: Mapping variable to global may degrade performance.

[681/991] Building CXX object Engine/CMakeFiles/Urho3D.dir/IO/File.cpp.o
/home/overminddl1/projects/Urho3D/Source/Engine/IO/File.cpp: In member function ?virtual unsigned int Urho3D::File::Read(void*, unsigned int)?:
/home/overminddl1/projects/Urho3D/Source/Engine/IO/File.cpp:300:84: warning: ignoring return value of ?size_t fread(void*, size_t, size_t, FILE*)?, declared with attribute warn_unused_result [-Wunused-result]
                 fread(blockHeaderBytes, sizeof blockHeaderBytes, 1, (FILE*)handle_);
                                                                                    ^
/home/overminddl1/projects/Urho3D/Source/Engine/IO/File.cpp:313:73: warning: ignoring return value of ?size_t fread(void*, size_t, size_t, FILE*)?, declared with attribute warn_unused_result [-Wunused-result]
                 fread(inputBuffer_.Get(), packedSize, 1, (FILE*)handle_);
                                                                         ^
[705/991] Building CXX object Engine/CMakeFiles/Urho3D.dir/IO/FileSystem.cpp.o
/home/overminddl1/projects/Urho3D/Source/Engine/IO/FileSystem.cpp: In member function ?Urho3D::String Urho3D::FileSystem::GetCurrentDir() const?:
/home/overminddl1/projects/Urho3D/Source/Engine/IO/FileSystem.cpp:506:27: warning: ignoring return value of ?char* getcwd(char*, size_t)?, declared with attribute warn_unused_result [-Wunused-result]
     getcwd(path, MAX_PATH);
                           ^
/home/overminddl1/projects/Urho3D/Source/Engine/IO/FileSystem.cpp: In member function ?Urho3D::String Urho3D::FileSystem::GetProgramDir() const?:
/home/overminddl1/projects/Urho3D/Source/Engine/IO/FileSystem.cpp:661:48: warning: ignoring return value of ?ssize_t readlink(const char*, char*, size_t)?, declared with attribute warn_unused_result [-Wunused-result]
     readlink(link.CString(), exeName, MAX_PATH);
                                                ^
[887/991] Building C object ThirdParty/Assimp/CMakeFiles/Assimp.dir/contrib/unzip/unzip.c.o
/home/overminddl1/projects/Urho3D/Source/ThirdParty/Assimp/contrib/unzip/unzip.c: In function ?unzOpenCurrentFile3?:
/home/overminddl1/projects/Urho3D/Source/ThirdParty/Assimp/contrib/unzip/unzip.c:1177:24: warning: assignment from incompatible pointer type [enabled by default]
         s->pcrc_32_tab = get_crc_table();
                        ^
[991/991] Linking CXX executable /home/overminddl1/projects/Urho3D/Bin/37_UIDrag

real    3m23.799s
user    17m34.462s
sys     0m52.352s
[/code][/spoiler]

And a makefile build (system not loaded, ran with -j 9, which seems to be the fastest on my system, hence why there is a little overlap in logs due to the concurrent building):
[spoiler][code]
overminddl1@overmind:~/projects/Urho3D$ ./cmake_gcc.sh -DURHO3D_64BIT=1 -DURHO3D_LUA=1 -DURHO3D_LUAJIT=1 -DURHO3D_LUAJIT_AMALG=1 -DURHO3D_SAMPLES=1 -DURHO3D_EXTRAS=1 -DURHO3D_DOCS=1 -DURHO3D_OPENGL=1 -DURHO3D_STATIC_RUNTIME=1 -DURHO3D_LIB_TYPE=STATIC -DCMAKE_BUILD_TYPE=Release

Native build
================================================================================
-- The C compiler identification is GNU 4.8.2
-- The CXX compiler identification is GNU 4.8.2
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Looking for include file stdint.h
-- Looking for include file stdint.h - found
-- Looking for XOpenDisplay in /usr/lib/x86_64-linux-gnu/libX11.so;/usr/lib/x86_64-linux-gnu/libXext.so
-- Looking for XOpenDisplay in /usr/lib/x86_64-linux-gnu/libX11.so;/usr/lib/x86_64-linux-gnu/libXext.so - found
-- Looking for gethostbyname
-- Looking for gethostbyname - found
-- Looking for connect
-- Looking for connect - found
-- Looking for remove
-- Looking for remove - found
-- Looking for shmat
-- Looking for shmat - found
-- Looking for IceConnectionNumber in ICE
-- Looking for IceConnectionNumber in ICE - found
-- Found X11: /usr/lib/x86_64-linux-gnu/libX11.so
-- Found OpenGL: /usr/lib/x86_64-linux-gnu/libGL.so  
-- Following tests check whether X11 library installed in this system uses _Xconst in below functions
-- A failed test result simply means the installed X11 library does not use _Xconst
-- It is OK to proceed to build Urho3D regardless of the test result
-- Performing Test HAVE_CONST_XEXT_ADDDISPLAY
-- Performing Test HAVE_CONST_XEXT_ADDDISPLAY - Success
-- Performing Test HAVE_CONST_XDATA32
-- Performing Test HAVE_CONST_XDATA32 - Success
-- Found ALSA: /usr/lib/x86_64-linux-gnu/libasound.so (found version "1.0.27.2") 
-- Finding value for LuaJIT:TARGET_LJARCH
-- Finding value for LuaJIT:TARGET_LJARCH - found (X64)
-- Finding value for LuaJIT:PS3
-- Finding value for LuaJIT:NO_UNWIND
-- Finding value for LuaJIT:ARCH_BITS
-- Finding value for LuaJIT:ARCH_BITS - found (64)
-- Finding value for LuaJIT:HASJIT
-- Finding value for LuaJIT:HASJIT - found (1)
-- Finding value for LuaJIT:HASFFI
-- Finding value for LuaJIT:HASFFI - found (1)
-- Finding value for LuaJIT:DUALNUM
-- Finding value for LuaJIT:ARCH_HASFPU
-- Finding value for LuaJIT:ARCH_HASFPU - found (1)
-- Finding value for LuaJIT:ABI_SOFTFP
-- Finding value for LuaJIT:ARCH_VERSION
-- The ASM compiler identification is GNU
-- Found assembler: /usr/bin/cc
-- Performing Test COMPILER_HAS_HIDDEN_VISIBILITY
-- Performing Test COMPILER_HAS_HIDDEN_VISIBILITY - Success
-- Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY
-- Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY - Success
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR - Success
-- Found Urho3D: as CMake target
-- Configuring done
-- Generating done
-- Build files have been written to: /home/overminddl1/projects/Urho3D/Build
overminddl1@overmind:~/projects/Urho3D$ cd Build   
overminddl1@overmind:~/projects/Urho3D/Build$ time make -j 9  
Scanning dependencies of target Civetweb
Scanning dependencies of target JO
Scanning dependencies of target PugiXml
Scanning dependencies of target Box2D
Scanning dependencies of target StanHull
Scanning dependencies of target LZ4
[  0%] Scanning dependencies of target FreeType
Scanning dependencies of target STB
[  0%] Scanning dependencies of target SDL
Building CXX object ThirdParty/JO/CMakeFiles/JO.dir/jo_jpeg.cpp.o
[  0%] Building C object ThirdParty/Civetweb/CMakeFiles/Civetweb.dir/src/civetweb.c.o                                                                                                                         
[  1%] [  1%] [  2%] Building CXX object ThirdParty/StanHull/CMakeFiles/StanHull.dir/hull.cpp.o                                                                                                               
Building C object ThirdParty/LZ4/CMakeFiles/LZ4.dir/lz4hc.c.o                                                                                                                                                 
Building CXX object ThirdParty/PugiXml/CMakeFiles/PugiXml.dir/src/pugixml.cpp.o                                                                                                                               
Building C object ThirdParty/STB/CMakeFiles/STB.dir/stb_image_write.c.o                                                                                                                                       
/*
  snip
*/
Linking CXX executable /home/overminddl1/projects/Urho3D/Bin/37_UIDrag
[100%] Built target 37_UIDrag

real    3m52.844s
user    17m48.033s
sys     0m59.983s
[/code][/spoiler]

Also, any chance of cleaning up the warning spam or marking those warnings so they will not appear during compilation?

-------------------------

