alexrass | 2017-01-02 00:57:44 UTC | #1

1) GCC and MinGW has options "-msse"/"-msse2". This options enable sse, but not generate sse instructions. For sse instruction generation need add option "-mfpmath=sse" with "-msse"/"-msse2".
2) For static linking c-runtime on mingw may be need option "-static" instead of "-static-libgcc" and "-static-libstdc++". Option "-static" link staticly c-runtime and libpthread.

Edit: If build 64-bit code, "-mfpmath=sse" enabled by default.

-------------------------

cadaver | 2017-01-02 00:57:47 UTC | #2

Thanks. Both of these are now in use. The dependency on an external libpthread dll does not happen on older MinGW distributions, but on a recent MinGW-w64 it does, so that was a good thing to notice.

-------------------------

alexrass | 2017-01-02 00:58:05 UTC | #3

When building shared lib with mingw, static run-time options not apply. 
[code]
set (CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} -static")
[/code]?

-------------------------

weitjong | 2017-01-02 00:58:06 UTC | #4

I will set this as well. Thanks again.

-------------------------

alexrass | 2017-01-02 00:58:54 UTC | #5

if compile with cross-target gcc (i686 - x86_64) and URHO3D_LIB_TYPE=SHARED link fail

patch for Urho3D-CMake-common.cmake:

[code]@@ -259,13 +259,15 @@ else ()
             set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -ffast-math")
             set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -ffast-math")
             if (URHO3D_64BIT)
                 set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -m64")
                 set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -m64")
+                set (CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} -m64")
             else ()
                 set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -m32")
                 set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -m32")
+                set (CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} -m32")
                 if (URHO3D_SSE)
                     if (NOT WIN32)
                         set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -msse")
                         set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -msse")
                     else ()

[/code]

-------------------------

weitjong | 2017-01-02 00:58:55 UTC | #6

I almost forget to apply the change. I read your last post initially in the morning before I started to work, so I could not apply it immediately. Once read, the post is not highlighted by the forum anymore when I come back later. So it would be great if you can raise it as an Issue in GitHub when you find more issues with the build scripts in the future. Thanks.

-------------------------

weitjong | 2017-01-02 01:07:36 UTC | #7

@alexrass, sorry to resurrect this old post. I am not sure whether you are still tracking Urho3D project development but since the last changes that you proposed, we have made a few changes on how the URHO3D_64BIT build option is being initialized which in turn affects how the '-m32' or '-m64' compiler flag is being set. Most notably is the changes since this commit e06762db76ec1d60ac38d84d351f7535985d6166 made in Sept 2014. I have a strong feeling that after that commit we do not need the workaround command to set the CMAKE_SHARED_LINKER_FLAGS anymore. However, I do not have i686-to-x86_64 cross-compiling toolchain installed on any of my build host systems, so I cannot verify this. It would be great if you can help me to verify and confirm this. Thank you.

-------------------------

alexrass | 2017-01-02 01:07:37 UTC | #8

[b]weitjong[/b]
Don't have access to my computer now, but  i'll check it tonight.

-------------------------

alexrass | 2017-01-02 01:07:38 UTC | #9

I comment line:
[quote]# Required only when cross-compling from i686 to x86_64, in other cases the flag is redundantly duplicated during linking phase for shared lib
                #set (CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} ${DASH_MBIT}")[/quote]
Builds normal.

-------------------------

weitjong | 2017-01-02 01:07:38 UTC | #10

Thanks for your time to check this. I will remove the line in a next commit.

-------------------------

