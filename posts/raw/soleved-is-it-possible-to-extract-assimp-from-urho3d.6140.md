8Observer8 | 2020-05-05 20:36:20 UTC | #1

I cannot build Assimp using CMake-GUI and MinGW (32 bit)

<details>
<summary>Errors</summary>

[ 71%] Building CXX object tools/assimp_cmd/CMakeFiles/assimp_cmd.dir/ImageExtractor.cpp.obj
[ 72%] Building CXX object tools/assimp_cmd/CMakeFiles/assimp_cmd.dir/Main.cpp.obj
[ 72%] Building CXX object tools/assimp_cmd/CMakeFiles/assimp_cmd.dir/WriteDumb.cpp.obj
[ 72%] Building CXX object tools/assimp_cmd/CMakeFiles/assimp_cmd.dir/Info.cpp.obj
[ 73%] Building CXX object tools/assimp_cmd/CMakeFiles/assimp_cmd.dir/Export.cpp.obj
[ 73%] Linking CXX executable assimp.exe
CMakeFiles\assimp_cmd.dir/objects.a(Main.cpp.obj):Main.cpp:(.text+0x42): undefined reference to `Assimp::DefaultLogger::create(char const*, Assimp::Logger::LogSeverity, unsigned int, Assimp::IOSystem*)'
CMakeFiles\assimp_cmd.dir/objects.a(Main.cpp.obj):Main.cpp:(.text+0xac): undefined reference to `Assimp::Importer::ValidateFlags(unsigned int) const'
CMakeFiles\assimp_cmd.dir/objects.a(Main.cpp.obj):Main.cpp:(.text+0xee): undefined reference to `Assimp::Importer::ReadFile(char const*, unsigned int)'
CMakeFiles\assimp_cmd.dir/objects.a(Main.cpp.obj):Main.cpp:(.text+0x17a): undefined reference to `Assimp::DefaultLogger::create(char const*, Assimp::Logger::LogSeverity, unsigned int, Assimp::IOSystem*)'
CMakeFiles\assimp_cmd.dir/objects.a(Main.cpp.obj):Main.cpp:(.text+0x1a6): undefined reference to `Assimp::DefaultLogger::kill()'
</details>

And I cannot choose in CMake-GUI what Importers to disable. But I built successfully Urho3D from source using CMake-GUI and MinGW (32 bit). I could disable a lot of importers. I want to try to use Assimp with OpenGL3 and GLSL. I want to understand how to use skeletal animation from scratch.

-------------------------

8Observer8 | 2020-05-05 11:50:26 UTC | #2

I found the same problem here: https://github.com/assimp/assimp/issues/2431

But I cannot find `add_library(IrrXML ${IrrXML_SRCS})` in CMakeList.txt and I do not understand where to place this code:

```
IF(CMAKE_SYSTEM_NAME MATCHES "(Darwin|FreeBSD)")
  add_library(IrrXML ${IrrXML_SRCS})
ELSE()
  add_library(IrrXML STATIC ${IrrXML_SRCS})
 ENDIF()
```

-------------------------

SirNate0 | 2020-05-05 14:08:31 UTC | #3

It looks to me like the upstream project may have broken the mingw builds:

https://stackoverflow.com/a/59453072

-------------------------

johnnycable | 2020-05-05 14:43:44 UTC | #4

[quote="8Observer8, post:2, topic:6140"]
IF(CMAKE_SYSTEM_NAME MATCHES "(Darwin|FreeBSD)")
[/quote]

mind that Darwin|FreeBSD is Apple

-------------------------

8Observer8 | 2020-05-05 15:40:43 UTC | #5

> As far as I know the tools are currently not working with this compiler.

But why was it possible to build Urho3D + Assimp with MinGW 32 bit? Maybe do not I need to include "tools" in build? I will try uncheck "tools".

-------------------------

8Observer8 | 2020-05-05 15:47:45 UTC | #6

CMake-GUI shows what importers to include when I build Urho3D. What did you make with Assimp? How can I uncheck some importers when I build Assimp from source?

-------------------------

8Observer8 | 2020-05-05 15:51:39 UTC | #7

Maybe did I install wrong MinGW? I installed from this link: http://mingw-w64.org/doku.php/download/mingw-builds What is better or it is good?

-------------------------

SirNate0 | 2020-05-05 17:51:42 UTC | #8

Just to clarify, is this a separate Assimp based project you are working on? Are you using the version packaged with Urho? Are you using Urho's build system?

-------------------------

8Observer8 | 2020-05-05 19:43:19 UTC | #9

I wanted to understand why building of Assimp with Urho3D is different. And why I can build Assimp with Urho3D but I cannot build Assimp 5.1.0 from official Assimp Repo. I now understand it. It is because Urho3D uses Assimp 4.1.0. But when I tried to build Assimp 4.1.0 I see the message errors below. All importers was disabled in CMake-GUI excepted OBJ - just for testing. `libassimp.dll.a` was created but I cannot find .dll

`
[ 98%] Building CXX object code/CMakeFiles/assimp.dir/__/contrib/openddlparser/code/OpenDDLStream.cpp.obj
[ 99%] Building C object code/CMakeFiles/assimp.dir/__/contrib/zip/src/zip.c.obj
[100%] Linking CXX shared library libassimp.dll
CMakeFiles\assimp.dir/objects.a(Exporter.cpp.obj):Exporter.cpp:(.text+0x12d1): undefined reference to `Assimp::ExportScene3MF(char const*, Assimp::IOSystem*, aiScene const*, Assimp::ExportProperties const*)'
collect2.exe: error: ld returned 1 exit status
mingw32-make[2]: *** [code\CMakeFiles\assimp.dir\build.make:1276: code/libassimp.dll] Error 1
mingw32-make[1]: *** [CMakeFiles\Makefile2:285: code/CMakeFiles/assimp.dir/all] Error 2
mingw32-make: *** [Makefile:149: all] Error 2
`

-------------------------

8Observer8 | 2020-05-05 19:46:16 UTC | #10

The 3MF importer was unchecked by me.

-------------------------

8Observer8 | 2020-05-05 20:35:24 UTC | #11

I solved the problem! The ASSIMP_BUILD_3MF_IMPORTER option must be enabled. MinGW32 works with [Assimp 4.1.0](https://github.com/assimp/assimp/releases/tag/v4.1.0). You can disable all Importers excepted ASSIMP_BUILD_3MF_IMPORTER. But I cannot build Assimp 5.1.0 with MinGW32 and I do not know how to disable importers in 5.1.0. It does not matter for me now. I glad that 4.1.0 works!

-------------------------

