Enhex | 2017-01-02 01:12:06 UTC | #1

Using HEAD commit
Window 7

I'm trying to build Urho3D Emscripten with MinGW, but I'm getting errors after "Generating tolua++ API binding on the fly for [Audio/Core/Engine/...]".
It dumps code, and each code section ends with:
[code]stack traceback:
	[string "tolua embedded: lua/basic.lua"]:57: in function 'tolua_error'
	[string "tolua: embedded Lua code 23"]:5: in main chunk

** tolua internal error: [string "tolua embedded: lua/container.lua"]:573: #parse error.[/code]


When disabling Lua, I get this:
[code]
[ 25%] Building CXX object CMakeFiles/PackageTool.dir/PackageTool.cpp.obj
In file included from e:\tdm-gcc-64\x86_64-w64-mingw32\include\winnt.h:26:0,
                 from e:\tdm-gcc-64\x86_64-w64-mingw32\include\minwindef.h:146,
                 from e:\tdm-gcc-64\x86_64-w64-mingw32\include\windef.h:8,
                 from e:\tdm-gcc-64\x86_64-w64-mingw32\include\windows.h:69,
                 from E:\Urho3D\Urho3D\Source\Tools\PackageTool\PackageTool.cpp:
30:
e:\tdm-gcc-64\x86_64-w64-mingw32\include\psdk_inc\intrin-impl.h: In function 'void __faststorefence()':
e:\tdm-gcc-64\x86_64-w64-mingw32\include\psdk_inc\intrin-impl.h:490:27: error: '__builtin_ia32_sfence' was not declared in this scope
     __builtin_ia32_sfence();
                           ^
CMakeFiles\PackageTool.dir\build.make:62: recipe for target 'CMakeFiles/PackageTool.dir/PackageTool.cpp.obj' failed
[/code]

-------------------------

hdunderscore | 2017-01-02 01:12:06 UTC | #2

Which commands did you run, from start to that point ?

-------------------------

Enhex | 2017-01-02 01:12:07 UTC | #3

To configure cmake:
E:\Urho3D\Urho3D\cmake_emscripten.bat E:\Urho3D\Urho3D_1.5_web

To build:
mingw32-make

Disabled Lua using CMake GUI afterwards. It did make a libUrho3D.a file, but no samples.


EDIT:
The problem seems to be related to mingw-w64, which was recommended in the [url=http://urho3d.github.io/documentation/HEAD/_building.html#Building_Emscripten]docs[/url].
I think it doesn't include some needed DLLs, and for me they were found from some other mingw build that was in my PATH as a fallback, and those didn't work.

Emscripten's minGW works.
Perhaps the docs should be updated, maybe mingw-w64 doesn't work out of the box.

-------------------------

