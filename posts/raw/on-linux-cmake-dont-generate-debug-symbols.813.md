alexrass | 2017-01-02 01:03:04 UTC | #1

On linux cmake don't generate debug symbols in debug config -DCMAKE_BUILD_TYPE=Debug
fix:
[code]@@ -385,12 +385,12 @@ else ()
             set (CMAKE_CXX_FLAGS_RELWITHDEBINFO "-O2 -g -DNDEBUG")
             # Reduce GCC optimization level from -O3 to -O2 for stability in RELEASE build configuration
             set (CMAKE_C_FLAGS_RELEASE "-O2 -DNDEBUG")
             set (CMAKE_CXX_FLAGS_RELEASE "-O2 -DNDEBUG")
         endif ()
-        set (CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -DDEBUG -D_DEBUG")
-        set (CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -DDEBUG -D_DEBUG")
+        set (CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -g -DDEBUG -D_DEBUG")
+        set (CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -g -DDEBUG -D_DEBUG")
     endif ()
     if (CMAKE_CXX_COMPILER_ID STREQUAL Clang)
         if (CMAKE_GENERATOR STREQUAL Ninja)
             set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fcolor-diagnostics")
             set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fcolor-diagnostics")

[/code]

-------------------------

weitjong | 2017-01-02 01:03:04 UTC | #2

The "-g" compiler flag is added by CMake automatically in my Linux system when CMAKE_BUILD_TYPE=Debug is set, so our CMake build rules just supplies the other flags and not the "-g" itself. So far, I have no problem in debugging Urho3D library and Urho3D application using Eclipse on Linux platform.

-------------------------

alexrass | 2017-01-02 01:03:05 UTC | #3

Hm.. I build with -DCMAKE_BUILD_TYPE=Debug and cmake don't generate debug symbols. In my distro CMake 3.0.1. May be try update to new version?

-------------------------

weitjong | 2017-01-02 01:03:05 UTC | #4

CMake 3.0.1 is not good a version to use, I think. The stable versions are: 2.8.12.2 or 3.0.2. On Mac OS X though, you need to use the bleeding edge 3.1.1.

-------------------------

alexrass | 2017-01-02 01:03:05 UTC | #5

I found problem. It is cmake in my distro.I build CMake 3.1.1 and it works perfect. Thanks.

-------------------------

