TheComet | 2017-01-25 00:43:56 UTC | #1

I've been trying to understand how on earth the following code works:

    #if defined(URHO3D_OPENGL)
    #   include "OpenGL/OGLGraphicsImpl.h"
    #   error GL was selected
    #elif defined(URHO3D_D3D11)
    #   include "Direct3D11/D3D11GraphicsImpl.h"
    #elif defined(URHO3D_D3D9)
    #   include "Direct3D9/D3D9GraphicsImpl.h"
    #else
    #   error No graphics API defined
    #endif

The output, of course, is: `error: GL was selected` as expected.

URHO3D_OPENGL is never defined with add_definitions(). I realise it is defined in the precompiled header, but I'm at a loss as to how it ends up there.

I want to add my own graphics API and want to make that an option.

-------------------------

Eugene | 2017-01-27 14:30:29 UTC | #2

[quote="TheComet, post:1, topic:2745"]
but I'm at a loss as to how it ends up there.
[/quote]
Maybe during CMake generation?

-------------------------

weitjong | 2017-01-25 10:30:27 UTC | #3

It is not clear to me at which context your question is. When building Urho3D library, the compiler define is added by CMake script. While using the library, some of them are already baked in the export header file. See also the discussion [here](http://discourse.urho3d.io/t/auto-discover-var-does-not-find-urho3d-testing/2742). URHO3D_TESTING and URHO3D_OPENGL are baked the same way.

Whether the PCH is used or not, is irrelevant.

-------------------------

TheComet | 2017-01-25 17:21:24 UTC | #4

[quote="weitjong, post:3, topic:2745"]
When building Urho3D library, the compiler define is added by CMake script.
[/quote]

This is what's unclear to me. Where specifically does this happen? Can you perhaps point me to a file/line?

-------------------------

weitjong | 2017-01-26 01:43:45 UTC | #5

Instead of telling you that, I could tell how to search for yourself. I believe something like this below should do it (not in front of a PC at the moment). 
    git grep URHO3D_OPENGL -- CMakeLists.txt

-------------------------

TheComet | 2017-01-26 04:07:32 UTC | #6

I've already done that and I mentioned in the first post that there is not a single occurrence of `add_definitions (-DURHO3D_OPENGL)`. This is the whole reason why I'm making this thread: I don't understand how URHO3D_OPENGL is defined without the use of `add_definitions()`. What other mechanism is there in CMake that can add global defines?

Here's the output of `make VERBOSE=1`:
> [ 47%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/LuaScript/LuaScriptInstance.cpp.o
>     cd /home/thecomet/documents/programming/cpp/Urho3D/build_gl/Source/Urho3D && /usr/bin/c++   -DGLEW_NO_GLU -DGLEW_STATIC -DHAVE_SINCOSF -DHAVE_STDINT_H -DTOLUA_RELEASE -DURHO3D_ANGELSCRIPT -DURHO3D_FILEWATCHER -DURHO3D_IS_BUILDING -DURHO3D_LOGGING -DURHO3D_LUA -DURHO3D_NAVIGATION -DURHO3D_NETWORK -DURHO3D_PHYSICS -DURHO3D_PROFILING -DURHO3D_STATIC_DEFINE -DURHO3D_THREADING -DURHO3D_URHO2D -I/home/thecomet/documents/programming/cpp/Urho3D/build_gl/Source/Urho3D -I/home/thecomet/documents/programming/cpp/Urho3D/Source/Urho3D -I/home/thecomet/documents/programming/cpp/Urho3D/build_gl/include/Urho3D/ThirdParty -I/home/thecomet/documents/programming/cpp/Urho3D/build_gl/include/Urho3D/ThirdParty/Bullet -I/home/thecomet/documents/programming/cpp/Urho3D/build_gl/include/Urho3D/ThirdParty/Detour -I/home/thecomet/documents/programming/cpp/Urho3D/build_gl/include/Urho3D/ThirdParty/Lua  -Wno-invalid-offsetof -march=native -ffast-math -pthread -fdiagnostics-color=auto -include "/home/thecomet/documents/programming/cpp/Urho3D/build_gl/Source/Urho3D/Precompiled.h" -O3 -DNDEBUG   -o CMakeFiles/Urho3D.dir/LuaScript/LuaScriptInstance.cpp.o -c /home/thecomet/documents/programming/cpp/Urho3D/Source/Urho3D/LuaScript/LuaScriptInstance.cpp

I don't see `-DURHO3D_OPENGL` on the command line here. But it's defined anyway. Why?

What I do see is the file `Precompiled.h` being included, and if I search for URHO3D_OPENGL in `build_gl/Source/Urho3D/Precompiled.h.gch/Precompiled.h.gch.Release` then I find matches.

So to repeat my initial question: How does URHO3D_OPENGL end up in Precompiled.h?

Here is my output for searching for URHO3D_OPENGL in all cmake files:
> $ find . \( -name "CMakeLists.txt" -or -name "*.cmake" \) -exec grep -H "URHO3D_OPENGL" {} \;
> ./CMakeLists.txt:if (WIN32 AND NOT URHO3D_OPENGL AND NOT URHO3D_VULKAN)
> ./CMake/Modules/FindUrho3D.cmake:#  URHO3D_OPENGL
> ./CMake/Modules/FindUrho3D.cmake:set (AUTO_DISCOVER_VARS URHO3D_OPENGL URHO3D_VULKAN URHO3D_D3D11 URHO3D_SSE URHO3D_DATABASE_ODBC URHO3D_DATABASE_SQLITE URHO3D_LUAJIT URHO3D_TESTING URHO3D_STATIC_RUNTIME)
> ./CMake/Modules/Urho3D-CMake-common.cmake:        # OpenGL can be manually enabled with -DURHO3D_OPENGL=1, but Windows graphics card drivers are usually better optimized for Direct3D
> ./CMake/Modules/Urho3D-CMake-common.cmake:        # Direct3D can be manually enabled with -DURHO3D_OPENGL=0, but it is likely to fail unless the MinGW-w64 distribution is used due to dependency to Direct3D headers and libs
./CMake/Modules/Urho3D-CMake-common.cmake:    option (URHO3D_OPENGL "Use OpenGL as the rendering backend." ${DEFAULT_OPENGL})
./CMake/Modules/Urho3D-CMake-common.cmake:    set (URHO3D_OPENGL 0)
./CMake/Modules/Urho3D-CMake-common.cmake:    set (URHO3D_OPENGL 0)
./CMake/Modules/Urho3D-CMake-common.cmake:if (URHO3D_OPENGL)
./CMake/Modules/Urho3D-CMake-common.cmake:    set (URHO3D_OPENGL 0)
./CMake/Modules/Urho3D-CMake-common.cmake:if (NOT ANDROID AND NOT ARM AND NOT WEB AND URHO3D_OPENGL)
./CMake/Modules/Urho3D-CMake-common.cmake:        if (URHO3D_OPENGL)
./Docs/CMakeLists.txt:    if (NOT URHO3D_OPENGL EQUAL DOXYFILE_URHO3D_OPENGL OR ${CMAKE_CURRENT_SOURCE_DIR}/Doxyfile.in IS_NEWER_THAN ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile)
./Docs/CMakeLists.txt:        set (DOXYFILE_URHO3D_OPENGL ${URHO3D_OPENGL} CACHE INTERNAL "URHO3D_OPENGL build option when Doxyfile was last generated")
./Docs/CMakeLists.txt:        if (URHO3D_OPENGL)
./Source/CMakeLists.txt:    if (URHO3D_OPENGL)
./Source/ThirdParty/SDL/CMakeLists.txt:# Urho3D - only make DIRECTX option available on Windows platform when URHO3D_OPENGL OR URHO3D_VULKAN
./Source/ThirdParty/SDL/CMakeLists.txt:# is enabled, i.e. DIRECTX variable must always be ON (not an option) when URHO3D_OPENGL and URHO3D_VULKAN
./Source/ThirdParty/SDL/CMakeLists.txt:  if (URHO3D_OPENGL or URHO3D_VULKAN)
./Source/ThirdParty/SDL/CMakeLists.txt:# Urho3D - commented out RENDER_D3D as an option to avoid potential conflict with our URHO3D_OPENGL and URHO3D_D3D11 build options on Windows platform
./Source/ThirdParty/SDL/CMakeLists.txt:  if (URHO3D_OPENGL or URHO3D_VULKAN)
./Source/Urho3D/CMakeLists.txt:if (URHO3D_OPENGL)

As you can see, there is no occurrence of `add_definitions()`, which makes me confused.

-------------------------

weitjong | 2017-01-26 07:31:43 UTC | #7

I am sorry if I didn't make myself clear. I asked you to search "URHO3D_OPENGL" as the keyword.

    git grep URHO3D_OPENGL

Don't use any pathspec so it will search on any files in the repo. If you do that then you will see we just declare "URHO3D_OPENGL" in the common CMake module file "URHO3D-CMake-common.cmake" as CMake variable and then bake that into a compiler define in the export header "Urho3D.h". The template for export header file is called "exportheader.cmake.in". Again, you should find this file if you use the right keyword to search.

-------------------------

TheComet | 2017-01-26 12:20:34 UTC | #8

Aaaah, so _that's_ how it's done. I understand now. Thanks!

-------------------------

