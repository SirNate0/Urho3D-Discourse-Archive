Penny | 2020-03-18 02:06:31 UTC | #1

Hello,
Brand new to Urho3D here.
Already struggling as I am unable to find a hello world to compile my first project.
Please provide a link to the idiots guide to compiling the first "Hello World" project on a windows 10 system.

Many Thanks.

-------------------------

ab4daa | 2020-03-18 02:21:24 UTC | #2

If you want to have your project  inside Urho3D, maybe look into sample folder and create your own folder to mimic.

If you want to build Urho3D as external lib and link to your project, maybe take a look to the project structure of 

https://github.com/ArnisLielturks/Urho3D-Project-Template

-------------------------

jmiller | 2020-03-18 05:17:50 UTC | #3

Hello Penny, and welcome to the forum! :confetti_ball: 

The [docs](https://urho3d.github.io/documentation/HEAD/index.html) are not terribly easy to find in the first place. :slight_smile:
After [building Urho3D](https://urho3d.github.io/documentation/HEAD/_building.html), the section [Using Urho3D Library](https://urho3d.github.io/documentation/HEAD/_using_library.html) is official reference for setting up and building a project. [Note: it is temporarily outdated in that it refers to build scripts (*.bat *.sh) once in the Urho3D root directory that were moved to Urho3D/**script**, so could change your command invocation slightly.]

Indeed, Urho3D Project Template is active and filling with useful features.

Let us know how it goes?

-------------------------

Penny | 2020-03-18 06:51:45 UTC | #4

Thank you for your replies.

I looked at the GitHub thing and yes I could download the files but then I would not have a clue what to do with them and there are no instructions, this is why I am asking for an idiots guide.

I looked at the "docs" link and how to get started. The first line mentions Windows and visual studio with no further links. The second line mentions Linex. Then is raspberyPI and then macOS and then it just goes on and on and I was confused at the second line.

Just a simply idiots guide would be perfect. I see visual studio was mentioned, wheres the visual project to download that would have everything already setup within?

What is cmake? alright, I know, but the instructions say, use cmake, and my question is how? and there is no explaination on how to use cmake.

Just a simply idiots guide step by step from downloading to files from the github to executing the final result would be awesome.

Thank you.

-------------------------

Miegamicis | 2020-03-18 08:14:12 UTC | #5

Download the https://cmake.org/ and https://visualstudio.microsoft.com/ virst

Building the engine
1. Download the source code from https://github.com/urho3d/Urho3D
2. Unzip the source code
3. Go to the unzipped directory
4. Run `script\cmake_vs2019.bat build` from the terminal in the same directory
5. It will create build subdirectory in your current location
6. Open the build directory in the file explorer and open the Urho3D.sln file in Visual Studio and compile the project

For instance let's say that Urho3D project is built in `C:\Urho3D\build` directory

Download the sample project
1. Download the source code from https://github.com/ArnisLielturks/Urho3D-Project-Template
2. Unzip the source code
3. Go to the unzipped directory
4. Run `script\cmake_vs2019.bat build -DURHO3D_HOME=C:\Urho3D\build` from the terminal in the same directory
5. It will create build subdirectory in your current location
6. Open the build directory in the file explorer and open the ProjectTemplate.sln file in Visual Studio and compile the project

-------------------------

Modanung | 2020-03-18 10:16:20 UTC | #6

Let's not forget the [wiki](https://github.com/urho3d/urho3d/wiki), it also contains practical information for beginners.
If you're using QtCreator, [these wizards](https://discourse.urho3d.io/t/qtcreator-class-and-project-wizards/2076) may be useful as well.

And of course, welcome to the forums! :confetti_ball: :smiley:

-------------------------

spwork | 2020-03-18 11:28:29 UTC | #7


The disadvantage of this engine is that the first step is difficult. Cmake is still unfamiliar to many Windows users. If someone write a simple fool tutorial to teach novices to compile examples, it is estimated that there will be more users. The documentation on how to build the engine library is too complicated for users unfamiliar with cmake, which will discourage a group of potential users / contributors.

-------------------------

George1 | 2020-03-20 10:26:09 UTC | #8

I think we can't say that.
I'm an idiot in C++ when I started.

I set up Urho3d using cmake gui on windows without any issue, while using the document.  So I think it need a little bit of trial and error, and determination.

The make build always works, thanks to Wei.

-------------------------

SirNate0 | 2020-03-18 13:40:48 UTC | #9

I agree, there is definitely a steep learning curve for the engine if someone is new to C++ and/or CMake. But I don't think that means we should not have CMake, for example - what would the alternative be? A visual studio file you must manually edit to get the proper build flags and files, which only works on Microsoft's IDE? We certainly can't make the case that C++ has a steep learning curve, so we should use a different language for the engine, and I think it's similar for CMake.

I do agree, though, there could definitely be a better tutorial setup, if not in the Docs then in the Wiki/forum. Fortunately anyone is welcome to add to the former, and this thread provides the latter :slight_smile:

-------------------------

spwork | 2020-03-18 15:16:04 UTC | #10

We don't need to give up cmake, cmake is fine. I think we should give newbies a simple start. For example, the beginning of the document should be:
 1.install visual studio and cmake, 
2.enter "cmake ..." command,
3. Open and compile with visual studio.
 so they can build the engine and examples with simple operations. Then go into the detailed build options. They don't even need to learn C ++ to do the above tasks. They can see the face of the engine. Like the first helloworld example in the c programming language book, this should be the best.

-------------------------

Modanung | 2020-03-18 15:44:21 UTC | #11

The wiki _is_ a wiki.

-------------------------

Penny | 2020-03-18 16:03:28 UTC | #12

Thank you all for your responses.

Miehamicis replied with the closest thing to an idiots guide so I proceeded with the mind for success. Here are the results...

#1 Downloaded from the link. Without this guide what I had actually downloaded was Urho3D-1.7.1 and not the master. What I previously downloaded is what is provided when I used the download link on the main page. It does not hold the script directory.

#4 This is what I tried adjusting for my system...

X:\test1>\urho3d-master\script\cmake_vs2019.bat build -DURHO3D_HOME=X:\Urho3D-master\build
'cmake' is not recognized as an internal or external command,
operable program or batch file.

Whilst urho3d-master has the script directory it does not have the build directory.

I was not successful and now I am stuck.
Please help me more with this idiots guide.
Thank you for your understanding.

-------------------------

SirNate0 | 2020-03-18 18:17:18 UTC | #13

[quote="Penny, post:12, topic:6000"]
‘cmake’ is not recognized as an internal or external command,
operable program or batch file.
[/quote]
You're missing CMake. If you did not install it do so now. If you did, ensure that the directory containing cmake is included in the PATH environment variable (some directions [here](https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/) for adding directories to the path if you're not familiar with it).

The build directory is expected to not exist - the build script creates it.

If you want, you can also use the cmake-gui to run CMake, though you don't get the the scripts automatically picking the right compiler and flags for the build for you. My preference is to use the scripts to initially create the build (which sets the right stuff for web builds and such for me by picking the right script), then I modify build flags like a shared vs static build using the GUI.

-------------------------

bvanevery | 2020-03-19 01:38:36 UTC | #14

We need to review what noob guidance *CMake itself* actually has.  "Learn how to use CMake" is a perfectly valid thing to tell people to do, same as learn C++.  Thing is, people here are giving causal advice to do command line CMake stuff, and that's complete nonsense.  CMake has a GUI tool.  It's pretty straightforward to use, at least as far as build systems go, if you've been briefed on the basic method of operation.  Which is something cmake.org should have as a readily available material.  I *hope* they have it, I'll go check later.  Something that could derail that agenda, is their historical tendency to sell books on how to use CMake, to make money.

Ok *unfortunately* pointing a complete noob at cmake.org is not a kind thing to do.  Kitware is oriented towards convincing business managers to switch to a CMake build system, and earning consulting fees helping businesses make that switch.  The documentation is fine for someone who already knows what a build system is and how to swim through tech stuff in general, but it's not geared towards a noob game developer at all.  Probably Kitware has put all the "digestible" stuff into their Mastering CMake book, which you have to pay for.

I don't know if a third party "CMake noob tutorial" is available somewhere.  I had a major falling out with Kitware a long time ago.  I got kicked off their mailing list back in the day.  Yes I used to be a CMake big deal once upon a time, but not since 2008.  Pretty sure I threatened to write a "free noob book" at one point, before the end.  That's why I can always "hum a few bars" about CMake and feel other people's pain, but I've never committed to becoming someone's CMake buildmaster again.  It was a career dead end for me.  Has tons to do with why I live out of a car and am broke now.

-------------------------

bvanevery | 2020-03-20 03:08:10 UTC | #15

Ok, I found that web searching for "cmake tutorial" was generally *not* helpful.  It's always stuff about how to write a build system in CMake.  Nobody wants to know about that just to build an existing project.

It seems that what you need to web search to get useful info, is "**running CMake**".  Then for instance you might chance upon the proper section of official documentation, which looks reasonably sane.  https://cmake.org/runningcmake/

See if that's enough to get you started.  If it isn't, there are videos on YouTube that you can find, using the same search term.  I'm not going to recommend one, because I haven't gone through them.  I don't know which a noob would consider to be easier or harder to follow.  I just know that they are out there, and YMMV.

-------------------------

SirNate0 | 2020-03-20 03:49:17 UTC | #16

Not a comment on your answer, which seems useful, but on the cmake documentation - they seem to have completely avoided the fact that there are cmake-gui programs available on Linux, as if Windows users are the only ones who would want a GUI. Granted, they did specify the directions for Unix, not Linux, so maybe that's why...
That was just from a quick read, so feel free to correct me if I missed something in the document.

-------------------------

bvanevery | 2020-03-20 04:04:17 UTC | #17

ccmake is a GUI.  It's just ugly.  I don't think the existence of the prettier cmake-gui on Unixes bears *too* much comment, since they are trying to cover every system out there, and also want you to buy their book.  Wouldn't shock me if that documentation hasn't been updated in quite some time, and nobody felt like writing the cmake-gui on Unix section.

-------------------------

Penny | 2020-04-02 04:06:51 UTC | #18

Excellent!!

Ok this is my idiots guide so far...

for Windows 10 x64
#1 goto https://cmake.org/runningcmake/
#2 click on download Windows 10 x64 version msi
#3 install and ensure "add to path" is selected
#4 goto *ArnisLielturks/Urho3D-Project-Template and download
#5 unzip to desird location
#6 goto location in command prompt and run "script\cmake_vs2019.bat build -DURHO3D_HOME=C:\Urho3D\build" adjusting paths

Miegamicis final step is to open "ProjectTemplate.sln" using visual studio but there is no such file
There is however CompilerIdC.vcxproj, CompilerIdCXX.vcxproj which seem the closest to Visual Studio files.

Thanks so much for your help so far but we still not quite there.
What do I need to do to overcome this last hurdle?

-------------------------

Penny | 2020-03-20 05:55:41 UTC | #19

ps, do I have to use visual studio? Am I able to simply use notepad?

-------------------------

Penny | 2020-03-20 05:59:25 UTC | #20

This is what I am talking about!

-------------------------

Penny | 2020-03-20 08:25:28 UTC | #21

There's an error in the logs....

[details=Log]
The C compiler identification is MSVC 19.24.28314.0
The CXX compiler identification is MSVC 19.24.28314.0
Check for working C compiler: Y:/Games/Microsoft Visual Studio/IDE/VC/Tools/MSVC/14.24.28314/bin/Hostx64/x64/cl.exe
Check for working C compiler: Y:/Games/Microsoft Visual Studio/IDE/VC/Tools/MSVC/14.24.28314/bin/Hostx64/x64/cl.exe - works
Detecting C compiler ABI info
Detecting C compiler ABI info - done
Detecting C compile features
Detecting C compile features - done
Check for working CXX compiler: Y:/Games/Microsoft Visual Studio/IDE/VC/Tools/MSVC/14.24.28314/bin/Hostx64/x64/cl.exe
Check for working CXX compiler: Y:/Games/Microsoft Visual Studio/IDE/VC/Tools/MSVC/14.24.28314/bin/Hostx64/x64/cl.exe - works
Detecting CXX compiler ABI info
Detecting CXX compiler ABI info - done
Detecting CXX compile features
Detecting CXX compile features - done
CMake Deprecation Warning at CMakeLists.txt:14 (cmake_policy):
  The OLD behavior for policy CMP0026 will be removed from a future version
  of CMake.

  The cmake-policies(7) manual explains that the OLD behaviors of all
  policies are deprecated and that a policy should be set to OLD only under
  specific short-term circumstances.  Projects should be ported to the NEW
  behavior and not rely on setting a policy to OLD.


CMake Warning at CMake/Modules/CheckHost.cmake:48 (message):
  Could not use MKLINK to setup symbolic links as this Windows user account
  does not have the privilege to do so.  When MKLINK is not available then
  the build system will fallback to use file/directory copy of the library
  headers from source tree to build tree.  In order to prevent stale headers
  being used in the build, this file/directory copy will be redone also as a
  post-build step for each library targets.  This may slow down the build
  unnecessarily or even cause other unforseen issues due to incomplete or
  stale headers in the build tree.  Request your Windows Administrator to
  grant your user account to have privilege to create symlink via MKLINK
  command.  You are NOT advised to use the Administrator account directly to
  generate build tree in all cases.
Call Stack (most recent call first):
  CMake/Modules/UrhoCommon.cmake:122 (include)
  CMakeLists.txt:24 (include)


CMake Error at CMake/Modules/FindUrho3D.cmake:343 (message):
  Could NOT find compatible Urho3D library in Urho3D SDK installation or
  build tree or in Android library.  Use URHO3D_HOME environment variable or
  build option to specify the location of the non-default SDK installation or
  build tree.  Ensure the specified location contains the Urho3D library of
  the requested library type.
Call Stack (most recent call first):
  CMake/Modules/UrhoCommon.cmake:244 (find_package)
  CMakeLists.txt:24 (include)


Configuring incomplete, errors occurred!
See also "X:/Urho3D/build2/CMakeFiles/CMakeOutput.log".

CMakeOutput.log...

The system is: Windows - 10.0.18362 - AMD64
Compiling the C compiler identification source file "CMakeCCompilerId.c" succeeded.
Compiler:  
Build flags: 
Id flags:  

The output was:
0
Microsoft (R) Build Engine version 16.4.0+e901037fe for .NET Framework
Copyright (C) Microsoft Corporation. All rights reserved.

Build started 20/03/2020 06:13:11.
Project "X:\Urho3D\build2\CMakeFiles\3.17.0-rc3\CompilerIdC\CompilerIdC.vcxproj" on node 1 (default targets).
PrepareForBuild:
  Creating directory "Debug\".
  Creating directory "Debug\CompilerIdC.tlog\".
InitializeBuildStatus:
  Creating "Debug\CompilerIdC.tlog\unsuccessfulbuild" because "AlwaysCreate" was specified.
ClCompile:
  Y:\Games\Microsoft Visual Studio\IDE\VC\Tools\MSVC\14.24.28314\bin\HostX64\x64\CL.exe /c /nologo /W0 /WX- /diagnostics:column /Od /D _MBCS /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"Debug\\" /Fd"Debug\vc142.pdb" /Gd /TC /FC /errorReport:queue CMakeCCompilerId.c
  CMakeCCompilerId.c
Link:
  Y:\Games\Microsoft Visual Studio\IDE\VC\Tools\MSVC\14.24.28314\bin\HostX64\x64\link.exe /ERRORREPORT:QUEUE /OUT:".\CompilerIdC.exe" /INCREMENTAL:NO /NOLOGO kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /MANIFEST /MANIFESTUAC:"level='asInvoker' uiAccess='false'" /manifest:embed /PDB:".\CompilerIdC.pdb" /SUBSYSTEM:CONSOLE /TLBID:1 /DYNAMICBASE /NXCOMPAT /IMPLIB:".\CompilerIdC.lib" /MACHINE:X64 Debug\CMakeCCompilerId.obj
  CompilerIdC.vcxproj -> X:\Urho3D\build2\CMakeFiles\3.17.0-rc3\CompilerIdC\.\CompilerIdC.exe
PostBuildEvent:
  for %%i in (cl.exe) do @echo CMAKE_C_COMPILER=%%~$PATH:i
  :VCEnd
  CMAKE_C_COMPILER=Y:\Games\Microsoft Visual Studio\IDE\VC\Tools\MSVC\14.24.28314\bin\Hostx64\x64\cl.exe
FinalizeBuildStatus:
  Deleting file "Debug\CompilerIdC.tlog\unsuccessfulbuild".
  Touching "Debug\CompilerIdC.tlog\CompilerIdC.lastbuildstate".
Done Building Project "X:\Urho3D\build2\CMakeFiles\3.17.0-rc3\CompilerIdC\CompilerIdC.vcxproj" (default targets).

Build succeeded.
    0 Warning(s)
    0 Error(s)

Time Elapsed 00:00:00.99


Compilation of the C compiler identification source "CMakeCCompilerId.c" produced "CompilerIdC.exe"

Compilation of the C compiler identification source "CMakeCCompilerId.c" produced "CompilerIdC.vcxproj"

The C compiler identification is MSVC, found in "X:/Urho3D/build2/CMakeFiles/3.17.0-rc3/CompilerIdC/CompilerIdC.exe"

Compiling the CXX compiler identification source file "CMakeCXXCompilerId.cpp" succeeded.
Compiler:  
Build flags: 
Id flags:  

The output was:
0
Microsoft (R) Build Engine version 16.4.0+e901037fe for .NET Framework
Copyright (C) Microsoft Corporation. All rights reserved.

Build started 20/03/2020 06:13:12.
Project "X:\Urho3D\build2\CMakeFiles\3.17.0-rc3\CompilerIdCXX\CompilerIdCXX.vcxproj" on node 1 (default targets).
PrepareForBuild:
  Creating directory "Debug\".
  Creating directory "Debug\CompilerIdCXX.tlog\".
InitializeBuildStatus:
  Creating "Debug\CompilerIdCXX.tlog\unsuccessfulbuild" because "AlwaysCreate" was specified.
ClCompile:
  Y:\Games\Microsoft Visual Studio\IDE\VC\Tools\MSVC\14.24.28314\bin\HostX64\x64\CL.exe /c /nologo /W0 /WX- /diagnostics:column /Od /D _MBCS /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"Debug\\" /Fd"Debug\vc142.pdb" /Gd /TP /FC /errorReport:queue CMakeCXXCompilerId.cpp
  CMakeCXXCompilerId.cpp
Link:
  Y:\Games\Microsoft Visual Studio\IDE\VC\Tools\MSVC\14.24.28314\bin\HostX64\x64\link.exe /ERRORREPORT:QUEUE /OUT:".\CompilerIdCXX.exe" /INCREMENTAL:NO /NOLOGO kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /MANIFEST /MANIFESTUAC:"level='asInvoker' uiAccess='false'" /manifest:embed /PDB:".\CompilerIdCXX.pdb" /SUBSYSTEM:CONSOLE /TLBID:1 /DYNAMICBASE /NXCOMPAT /IMPLIB:".\CompilerIdCXX.lib" /MACHINE:X64 Debug\CMakeCXXCompilerId.obj
  CompilerIdCXX.vcxproj -> X:\Urho3D\build2\CMakeFiles\3.17.0-rc3\CompilerIdCXX\.\CompilerIdCXX.exe
PostBuildEvent:
  for %%i in (cl.exe) do @echo CMAKE_CXX_COMPILER=%%~$PATH:i
  :VCEnd
  CMAKE_CXX_COMPILER=Y:\Games\Microsoft Visual Studio\IDE\VC\Tools\MSVC\14.24.28314\bin\Hostx64\x64\cl.exe
FinalizeBuildStatus:
  Deleting file "Debug\CompilerIdCXX.tlog\unsuccessfulbuild".
  Touching "Debug\CompilerIdCXX.tlog\CompilerIdCXX.lastbuildstate".
Done Building Project "X:\Urho3D\build2\CMakeFiles\3.17.0-rc3\CompilerIdCXX\CompilerIdCXX.vcxproj" (default targets).

Build succeeded.
    0 Warning(s)
    0 Error(s)

Time Elapsed 00:00:00.62


Compilation of the CXX compiler identification source "CMakeCXXCompilerId.cpp" produced "CompilerIdCXX.exe"

Compilation of the CXX compiler identification source "CMakeCXXCompilerId.cpp" produced "CompilerIdCXX.vcxproj"

The CXX compiler identification is MSVC, found in "X:/Urho3D/build2/CMakeFiles/3.17.0-rc3/CompilerIdCXX/CompilerIdCXX.exe"

Determining if the C compiler works passed with the following output:
Change Dir: X:/Urho3D/build2/CMakeFiles/CMakeTmp

Run Build Command(s):Y:/Games/Microsoft Visual Studio/IDE/MSBuild/Current/Bin/MSBuild.exe cmTC_50226.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m && Microsoft (R) Build Engine version 16.4.0+e901037fe for .NET Framework

Copyright (C) Microsoft Corporation. All rights reserved.



  Microsoft (R) C/C++ Optimizing Compiler Version 19.24.28314 for x64

  testCCompiler.c

  Copyright (C) Microsoft Corporation.  All rights reserved.

  cl /c /Zi /W3 /WX- /diagnostics:column /Od /Ob0 /D WIN32 /D _WINDOWS /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_50226.dir\Debug\\" /Fd"cmTC_50226.dir\Debug\vc142.pdb" /Gd /TC /errorReport:queue X:\Urho3D\build2\CMakeFiles\CMakeTmp\testCCompiler.c

  cmTC_50226.vcxproj -> X:\Urho3D\build2\CMakeFiles\CMakeTmp\Debug\cmTC_50226.exe




Detecting C compiler ABI info compiled with the following output:
Change Dir: X:/Urho3D/build2/CMakeFiles/CMakeTmp

Run Build Command(s):Y:/Games/Microsoft Visual Studio/IDE/MSBuild/Current/Bin/MSBuild.exe cmTC_3b5df.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m && Microsoft (R) Build Engine version 16.4.0+e901037fe for .NET Framework

Copyright (C) Microsoft Corporation. All rights reserved.



  Microsoft (R) C/C++ Optimizing Compiler Version 19.24.28314 for x64

  CMakeCCompilerABI.c

  Copyright (C) Microsoft Corporation.  All rights reserved.

  cl /c /Zi /W3 /WX- /diagnostics:column /Od /Ob0 /D WIN32 /D _WINDOWS /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_3b5df.dir\Debug\\" /Fd"cmTC_3b5df.dir\Debug\vc142.pdb" /Gd /TC /errorReport:queue "Y:\Program Files\CMake\share\cmake-3.17\Modules\CMakeCCompilerABI.c"

  cmTC_3b5df.vcxproj -> X:\Urho3D\build2\CMakeFiles\CMakeTmp\Debug\cmTC_3b5df.exe




Determining if the CXX compiler works passed with the following output:
Change Dir: X:/Urho3D/build2/CMakeFiles/CMakeTmp

Run Build Command(s):Y:/Games/Microsoft Visual Studio/IDE/MSBuild/Current/Bin/MSBuild.exe cmTC_0692d.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m && Microsoft (R) Build Engine version 16.4.0+e901037fe for .NET Framework

Copyright (C) Microsoft Corporation. All rights reserved.



  Microsoft (R) C/C++ Optimizing Compiler Version 19.24.28314 for x64

  testCXXCompiler.cxx

  Copyright (C) Microsoft Corporation.  All rights reserved.

  cl /c /Zi /W3 /WX- /diagnostics:column /Od /Ob0 /D WIN32 /D _WINDOWS /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_0692d.dir\Debug\\" /Fd"cmTC_0692d.dir\Debug\vc142.pdb" /Gd /TP /errorReport:queue X:\Urho3D\build2\CMakeFiles\CMakeTmp\testCXXCompiler.cxx

  cmTC_0692d.vcxproj -> X:\Urho3D\build2\CMakeFiles\CMakeTmp\Debug\cmTC_0692d.exe




Detecting CXX compiler ABI info compiled with the following output:
Change Dir: X:/Urho3D/build2/CMakeFiles/CMakeTmp

Run Build Command(s):Y:/Games/Microsoft Visual Studio/IDE/MSBuild/Current/Bin/MSBuild.exe cmTC_d2d27.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m && Microsoft (R) Build Engine version 16.4.0+e901037fe for .NET Framework

Copyright (C) Microsoft Corporation. All rights reserved.



  Microsoft (R) C/C++ Optimizing Compiler Version 19.24.28314 for x64

  CMakeCXXCompilerABI.cpp

  Copyright (C) Microsoft Corporation.  All rights reserved.

  cl /c /Zi /W3 /WX- /diagnostics:column /Od /Ob0 /D WIN32 /D _WINDOWS /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_d2d27.dir\Debug\\" /Fd"cmTC_d2d27.dir\Debug\vc142.pdb" /Gd /TP /errorReport:queue "Y:\Program Files\CMake\share\cmake-3.17\Modules\CMakeCXXCompilerABI.cpp"

  cmTC_d2d27.vcxproj -> X:\Urho3D\build2\CMakeFiles\CMakeTmp\Debug\cmTC_d2d27.exe
[/details]

-------------------------

bvanevery | 2020-03-20 07:11:42 UTC | #22

[quote="Penny, post:18, topic:6000"]
#6 goto location in command prompt and run “script\cmake_vs2019.bat build -DURHO3D_HOME=C:\Urho3D\build” adjusting paths
[/quote]

I didn't look at that project, but I don't really get this step, ever, in any CMake build.  It's not basically the CMake way of doing things.  The whole point is not to need system specific or compiler specific script files.  You should be running CMake on a CMakeLists.txt, that's it, nothing else.  You don't have to do command line anything, cmake-gui works just fine.  It will produce a .sln file.  Unless the author of the template really doesn't get CMake and really did something odd, so that it doesn't generate the right and expected stuff.

CMake is a build system *generator*.  You could generate files for Visual Studio, or for Code::Blocks, or for Makefiles, or for Eclipse, or for a number of other supported IDEs or non-IDE build tools.  Which of these you want to use for your development, is totally up to you.  But if you're a native Windows developer, you should be using Visual Studio unless you've come up with a very good reason not to.  In which case, you don't need to ask the question.

Been awhile since I messed with the symbolic links on Windows issue.  I believe you enable them somehow.  I probably did it a long time ago.  It's one of those boring development issues that you will need to / should research yourself.  I remember it not being exceptionally hard to get past, someone will have written an article about it somewhere.  It's completely boring.

Actually it turns out I get the same MKLINK warning.  I've been blowing it off / not even noticing.  Obviously doesn't stop my build.

Looks like your template example code doesn't know where to find the Urho3D you already built and put somewhere.  This is why all that .bat and command line stuff is bad advice to follow.  Ordinarily, you'd just use cmake-gui to tell stuff where everything is.  If anything is missing, you download it or install it or build it, then tell cmake-gui where it is.  You do this enough times, and all those "pink you've done something wrong" lines turn white.  Then you're ready to Generate.  Then you get a .sln out of it, or whatever other IDE file if you're not doing VS.

-------------------------

George1 | 2020-03-21 09:46:36 UTC | #23

For visual studio version.  If you already installed it.
-----------------------
1) Download latest master from git hub.  Extract to any location.
2)  Download CMake. Installer or zip.   Open CMake gui set location as image below. 
Click configure button.
![image|690x121](upload://5PayeoZwUpNpY5wrkJI5vvkug9x.png)
 
3) Choose visual studio version from dialog. Click Finish, let it run 
![image|506x381](upload://fU2OruBpZCiAu77lsEevU7uQLOR.png)
 
4). Check the options you want.  Maybe use URHO3D_LIB_TYPE = STATIC, if you know what it is. Otherwise just leave default.  Don't select document, because you will need a library. 
![image|336x224](upload://tLf5PNnJ7i7An7PumcIBDLPu5Af.png) 

5) Click configure again. Until there is no red shown on the gui.
![image|426x163](upload://kNsDMLKN14e8oEtyOjGtzRgVHG0.png) 

6) Click Generate button. Click the open project if you have visual studio installed.  Build solution and right click run a sample.

-------------------------

bvanevery | 2020-03-20 07:04:42 UTC | #24

[quote="George1, post:23, topic:6000"]
Maybe URHO3D_LIB_TYPE = STATIC.
[/quote]

Don't even bother.  If you're a noob, never ever ever bother with some weird, personal, totally unfounded idea about what "should" be built or not.  First you find out if the build *works*.  Default options should work out of the box, no mucking around.  If it doesn't work, either you did something wrong, or the person who wrote all the CMakeLists.txt did something wrong.  If you're not doing anything weird, then it's them.  So don't do weird things.

-------------------------

bvanevery | 2020-03-20 07:06:36 UTC | #26

You aren't the OP.  The advice is for them.  **Idiots guide to Hello World.**

Noobs don't know static vs. dynamic libraries.  Don't confuse them.

-------------------------

bvanevery | 2020-03-20 07:28:09 UTC | #28

I just tested Master on a clean directory.  URHO3D_SAMPLES is a default build item.  Noob doesn't need to do anything to make that happen.

Stick to defaults.  Defaults are supposed to work.  Don't change defaults unless you know why you're doing so.

-------------------------

Penny | 2020-03-20 16:38:29 UTC | #30

Your screenshots were very helpful. I suggest to keep this post.

I am attempting to run cmake gui again.
One parameter which doesnt make sense.
CMAKE_INSTALL_PREFIX = C:\program files (x86)\Urho3D

The location is not where Urho3D is installed and I do not wish to have anything on my system drive. Should I change this to where I have located Urho3D?

-------------------------

Penny | 2020-04-02 04:06:54 UTC | #31

Thank you for your support.
Here is where I am at...

#1 goto https://cmake.org/runningcmake/
#2 click on download Windows 10 x64 version msi
#3 install and ensure “add to path” is selected
#3 goto https://github.com/urho3d/Urho3D download Urho3D-master.zip
#4 extract zip to X:/Urho3D (adjust to suit)
#5 open cmake gui
#6 set source to X:/Urho3D
#7 set build to X:/Urho3D/build
#8 click on "Configure"
#9 set CMAKE_INSTALL_PREFIX to X:/Urho3D/Prefix (I dont want anything on system drive)
#10 click on "Generate"
#11 goto X:/Urho3D/build/Source/Samples
#12 Open "Urho3D-Samples.sln" with Visual Studio 2019
#13 Build Solution
#14 Click on "01_HelloWorld" and "Start without debugging"

I get this....
![Urho3D error|690x480](upload://szCRDod5Gw7sLKXdwWv3CGoG0Tx.jpeg) 

Thank you so much. I have come a long way.
What now?
Thanks.

-------------------------

spwork | 2020-03-20 17:37:07 UTC | #32

set a launch project，for example 01_HelloWorld

-------------------------

bvanevery | 2020-03-20 18:24:24 UTC | #33

[quote="Penny, post:31, topic:6000"]
#7 set build to X:/Urho3D/build
[/quote]

I would suggest, to do CMake "expected hygiene" properly, do not do this.  You are polluting your source tree with new stuff.  You should keep your source tree read only.  You're not as conscious of this because you downloaded a static .ZIP archive from GitHub.  But it would be more typical in ongoing development, to *git clone* from GitHub, and to *git pull* when you want more updates from Master.  Your local Git repository should be for the source code only and not polluted with generated build files.

I know that some people in the CMake universe do have a /build subdirectory personal culture.  I say they are Doing It Wrong, and don't understand / embrace the basic distinction of source vs. build directory in CMake's model of operation.  I don't know what the CMake community pushes nowadays as best practices, if there's any push at all.  Back in the day, some people wanted to do /build subdirectories and I always thought they were Doing It Wrong [TM].

Standard drill for when a build blows up in your face, is to completely delete the build directory and start fresh.  That's why you don't put it under a chunk of your filesystem that's supposed to be read only.

So what I do, for instance, is have a C:\devel directory.  I git clone into that directory, resulting in C:\devel\Urho3D.  I build in C:\devel\build\Urho3D.  All of my various CMake built projects live in C:\devel\build.  I could delete my entire \build directory for every single project I ever built, if I so chose.  Such as to free up space on my crammed hard drive.

These distinctions about "completely separate build directory" become more important when you are *writing* CMakeLists.txt build files for other people's consumption.  Expecting people to use a /build subdirectory in their own source tree is a bad practice, in my book pretty much unforgivable, "deserves an Issue filed" and some hounding for them to learn how to get it right.  YMMV for a small one-off project, but not acceptable for an ongoing project at the scale of something like Urho3D.

Not that Urho3D has / had any such problems.  Weitjong's CMake kung fu is legion.

-------------------------

bvanevery | 2020-03-20 18:38:21 UTC | #34

[quote="spwork, post:32, topic:6000, full:true"]
set a launch project，for example 01_HelloWorld
[/quote]

No.  That's not the missing piece of the puzzle.  Do no such thing.

The missing CMake obscura, is that Penny needed to build the ALL_BUILD target.  Not just "Build the Solution" like one would expect in a sane and perfectly polished universe.  The difference is some kind of historical implementation detail, about what it took to get CMake to work in Visual Studio.  I don't know if it's theoretically possible for Kitware to change CMake to build things "a nicer way", or if there are any Feature Requests for that.  But selecting ALL_BUILD and building that, is the standard operating procedure for how you do CMake in Visual Studio.

Once you've done that, everything is built and it works.  You don't need to change launch projects.  When you want to run a target project, you click on the menu for that project specifically, and "Start Debugging".  It'll run.  Doesn't matter if it's a Release build, you still click on "Start Debugging".  I've seen a "Start Without Debugging" option floating around in VS 2019, you can do that too.  But historically it's just "Start Debugging".  It runs.

-------------------------

SirNate0 | 2020-03-20 20:10:30 UTC | #35

[quote="bvanevery, post:33, topic:6000"]
Not that Urho3D has / had any such problems. Weitjong’s CMake kung fu is legion.
[/quote]

Agreed. Though I'd say that it makes the rest of your post basically giving you're opinion about (sort of) in source vs out of source build trees. Either work with Urho, and in my opinion either should work with all projects (unfortunately this is not the case, but for Urho at least it is).

And while I probably have less experience on the matter than you, I take the opposite approach. All projects should have a Build (or build, if you prefer) subdirectory, not a second folder elsewhere. Then when I'm done with a project being on the drive (after it's backed up elsewhere) I just delete the whole directory for the project, rather than the separate source and build directories. Perhaps this just reflects how I prefer grouping files, though. For the files for my games I prefer grouping by, for example Maps, Characters, etc, rather than Models, Textures, Materials, etc.

That said, I agree that using . as the source and build directories is a bad idea (an actual in source build)

-------------------------

bvanevery | 2020-03-20 21:27:48 UTC | #36

I've done CMake for money, for Mozilla, trying to convert their Firefox build to CMake back in the day.  I think that makes my opinion on out of source builds worth more.  On the other hand, I blew the gig and they didn't make that transition back then.  So one could argue that my opinion is worth less.  :-)  No seriously, I've had CMake kung fu in my time.  Don't be messing with that /build subdirectory stuff.  There are all sorts of reasons when writing production build systems that that's a bad idea.

-------------------------

Penny | 2020-03-20 21:54:17 UTC | #37

I'm so pleased that you all have superb experience.
What is most likely causing the error?
Thanks.

-------------------------

bvanevery | 2020-03-20 23:49:32 UTC | #38

Have you built the ALL_BUILD target, like I said above, buried amidst all that other verbiage?

-------------------------

Penny | 2020-03-21 00:37:42 UTC | #39

Not sure what you mean, is that a setting in the cmake gui?

-------------------------

bvanevery | 2020-03-21 00:42:40 UTC | #40

No, it is in Visual Studio.  Look at all the Projects in your Solution.  One of them is called ALL_BUILD.

You might have noticed that your error message in your screenshot talks about ALL_BUILD.  I suspect it's *part of* your problem.

I also think you're probably doing something without Admin permissions.  Are you Admin equivalent?  Probably has to do with the MKLINK / symbolic links obscura.

Hmm, now that I *really stare* at your screenshot, it says that all your builds succeeded.  Perhaps you just didn't right-click on the Sample you were interested in to "Start Debugging" it.

-------------------------

Penny | 2020-04-02 04:06:56 UTC | #41

Yeah, the first time I built them it said zero errors.
I tried to run the first project but it seemed to want to rebuild again before it ran it and came up with errors.
I attempted to rebuild again and had lots of errors.
Please view the error log...

https://www.dropbox.com/s/wjtn3mdxxvr4r1p/urho3d%20build%20error%20log.txt?dl=0

Thank you very much.
I don't think I am asking a lot to download the samples, build and run. Seems waaaaay too complicated.
I haven't even got to the stage where my poor coding is causing the errors! lol

-------------------------

Lumak | 2020-03-21 03:59:47 UTC | #42

ALL_BUILDS is not an executable project.
Do this:

1.  select 01_HelloWorld
2. right mouse click and choose "Set as StartUp Project" as shown below
3. now, you are able to click on the run button (green arrow with "Local Windows Debugger") to execute it 


[img]https://i.imgur.com/Us4RyOC.png[/img]

-------------------------

bvanevery | 2020-03-21 04:06:48 UTC | #43

CMake does work well for what it does accomplish, which is providing a single cross-platform build for a lot of different development IDEs and toolchains.  But it's not exactly super easy plug and play in that regard.  The learning curve for merely building with it isn't that steep though.

Ok, you've got all these .pdb out of date errors.  Those are Program Databases, Visual Studio's version of a debugging file.  They keep saying delete it and recompile.  I'm not sure why, but your build tree is trashed.  You need to delete it all and start over from scratch.  Totally clean.

This time, do not use X:\Urho3D\build as your build directory.  Use X:\SomethingElse\build.

-------------------------

bvanevery | 2020-03-21 04:10:56 UTC | #44

[quote="Lumak, post:42, topic:6000"]
right mouse click and choose “Set as StartUp Project” as shown below
[/quote]


You really don't have to keep doing this over and over again for every project.  Right click and "Start Debugging" works just fine.

-------------------------

Penny | 2020-03-21 05:27:36 UTC | #45

Ok, I deleted everything to start again.
This time I created X:\Urho3D\repo where I placed the contents of the master.zip
Used CMAKE to build to X:\Urho3D\build success.
Opened project and built solution, zero errors.

I right clicked on Hello World, there was no "Start Debugging" but there was "Debug > start new instance"
this was the result...

1>------ Build started: Project: toluapp, Configuration: Debug x64 ------
2>------ Build started: Project: Detour, Configuration: Debug x64 ------
2>DetourAlloc.cpp
1>tolua_event.c
2>DetourAssert.cpp
2>DetourCommon.cpp
2>DetourNavMesh.cpp
2>DetourNavMeshBuilder.cpp
2>DetourNavMeshQuery.cpp
2>DetourNode.cpp
1>tolua_is.c
1>tolua_map.c
1>tolua_push.c
1>tolua_to.c
1>Y:\Games\Microsoft Visual Studio\IDE\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(502,5): warning MSB8015: All source files are not up-to-date:  forcing a rebuild of all source files due to the contents of 'X:\Urho3D\build\Source\ThirdParty\toluapp\src\lib\toluapp.dir\Debug\toluapp.tlog\CL.command.1.tlog' being invalid.
2>Y:\Games\Microsoft Visual Studio\IDE\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(502,5): warning MSB8015: All source files are not up-to-date:  forcing a rebuild of all source files due to the contents of 'X:\Urho3D\build\Source\ThirdParty\Detour\Detour.dir\Debug\Detour.tlog\CL.command.1.tlog' being invalid.
1>toluapp.vcxproj -> X:\Urho3D\build\Source\ThirdParty\toluapp\src\lib\Debug\toluapp.lib
2>Detour.vcxproj -> X:\Urho3D\build\Source\ThirdParty\Detour\Debug\Detour.lib
1>Done building project "toluapp.vcxproj".
3>------ Build started: Project: tolua++, Configuration: Debug x64 ------
2>Done building project "Detour.vcxproj".
3>toluabind.c
3>tolua.c
3>LINK : fatal error LNK1201: error writing to program database 'X:\Urho3D\build\bin\tool\tolua++.pdb'; check for insufficient disk space, invalid path, or insufficient privilege
3>Done building project "tolua++.vcxproj" -- FAILED.
4>------ Build started: Project: Urho3D, Configuration: Debug x64 ------
4>Generating tolua++ API binding on the fly for Audio
4>'X:\Urho3D\build\bin\tool\tolua++' is not recognized as an internal or external command,
4>operable program or batch file.
4>Y:\Games\Microsoft Visual Studio\IDE\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(231,5): error MSB6006: "cmd.exe" exited with code 9009.
4>Done building project "Urho3D.vcxproj" -- FAILED.
5>------ Build started: Project: 01_HelloWorld, Configuration: Debug x64 ------
5>01_HelloWorld.vcxproj -> X:\Urho3D\build\bin\01_HelloWorld_d.exe
========== Build: 3 succeeded, 2 failed, 22 up-to-date, 0 skipped ==========

-------------------------

Penny | 2020-04-02 04:06:57 UTC | #46

Actually, sellecting a demo and setting it as the startup project runs that demo when I click Local Windows Debugger.

I have enjoyed watching a number of the demos now.

Thank you all for your help. I am now going to spend some time pulling the demos apart with the view to start my own project. I am sure I will have lots of questions :slightly_smiling_face:
Thank you!

ps...
Final Idiot's Guide.

#1 Install latest version of Visual Studio
#2 goto https://cmake.org/runningcmake/
#3 click on download Windows 10 x64 version msi
#4 install and ensure “add to path” is selected
#5 goto https://github.com/urho3d/Urho3D download Urho3D-master.zip
#6 extract zip to X:/Urho3D/repo (adjust to suit)
#7 open cmake gui
#8 set source to X:/Urho3D/repo
#9 set build to X:/Urho3D/build
#10 click on “Configure”
#11 click on “Generate”
#12 click on “Open Project” (Opens Visual Studio with samples solution)
#13 in VS, build solution
#14 right click Hello World project and set as the start up project
#15 click "Local Windows Debugger" and the project you selected as the StartUp project will run.

-------------------------

bvanevery | 2020-03-21 14:01:56 UTC | #47

[quote="Penny, post:45, topic:6000"]
Opened project and built solution, zero errors.
[/quote]

Lack of errors is good, but did you use the ALL_BUILD target?  It may explain why you had errors subsequently with tolua++.

[quote="Penny, post:46, topic:6000"]
Actually, sellecting a demo and setting it as the startup project runs that demo when I click Local Windows Debugger.
[/quote]

It shouldn't have been necessary, but if it resolved something, great.  I never do this.

-------------------------

Penny | 2020-03-24 07:56:32 UTC | #48

Thank you very much for your help.

What is the best way to create my own Urho3D project?

I was thinking of using HelloWorld, I exported a template, and created a new project from that template, but could not build because of some unresolved external links.

What is the best way to create my own Urho3D project?

Thanks

-------------------------

Modanung | 2020-03-24 10:15:52 UTC | #49

I'd say there is no "best way". There _is_ several options to pick from, which are mentioned in the [Getting started](https://github.com/urho3d/urho3d/wiki#getting-started) section of the wiki, but which would be considered _best_ really depends on your personal preference. Reworking a sample is a good first step, as - I think - it helps to understand the structure of a basic Urho3D program more than whipping out a template right away. The [Overall structure](https://urho3d.github.io/documentation/HEAD/_structure.html) section of the documentation also helps with that.

-------------------------

Penny | 2020-03-24 11:38:22 UTC | #50

Thank you. I am not unfamiliar with 3D engines. All of the libraries appear to be pretty much standard expectation.

I am giving Urho3D a go, migrating so to say.

My unfamiliarity lies with cmake, Visual Studio, and of course how to create a Urho3D base project with a running null main loop.

Creating an empty project and linking in the includes didn't work in this case.

The Empty Project Template has instructions for Ubunto but not Windows & Visual Studio.

Not terribly familiar with C++ either so theres a learning curve with that. Spent a life time with MASM, cobol, pascal and a whole bunch of modern languages that have been around in the last 20 years.

So heres to my learning curve :slight_smile: 

Any tips in creating a null main loop, or steps to create the Empty Project template would be fabby thanks.

-------------------------

Modanung | 2020-03-24 11:49:01 UTC | #51

[quote="Penny, post:50, topic:6000"]
Any tips in creating a null main loop, or steps to create the Empty Project template would be fabby thanks.
[/quote]

Since I use QtCreator, I made some [wizards](https://gitlab.com/luckeyproductions/QtCreatorUrho3DWizards) for it to do just that. If you _must_ use Visual Studio, I guess you could take the [MasterControl](https://gitlab.com/luckeyproductions/QtCreatorUrho3DWizards/-/blob/master/templates/wizards/projects/urho3d/mastercontrol.cpp) class and rip out all the conditionals. That should get you pretty close.

-------------------------

Modanung | 2020-03-26 09:20:37 UTC | #52

11 posts were split to a new topic: [Choosing a C++ IDE](/t/choosing-a-c-ide/6016)

-------------------------

Modanung | 2020-03-26 09:21:20 UTC | #53

[quote="Penny, post:1, topic:6016"]
Do you have an idiots guide?
[/quote]
1. Trust in yourself
2. Read the readme
3. Don't be an idiot :stuck_out_tongue:
4. Ask specific questions

-------------------------

Penny | 2020-04-01 21:07:15 UTC | #54

I have followed the guide on "Setting-up-a-Project-(CMake)"
to make my first project.
CMake seems to create the sln ok however when VS is opened there are 4 projects listed, ALL_BUILD, INSTALL, TestProject2, ZERO_CHECK

There is nothing inside any of these.
Is this right? The project builds but doesnt display anything in the window. What do I need to do to fix this? Thanks

-------------------------

bvanevery | 2020-04-02 19:10:01 UTC | #55

https://github.com/urho3d/Urho3D/wiki/Setting-up-a-Project-(CMake) for anyone wiki challenged.

ALL_BUILD should contain an expandable list of References.  For instance, Urho3D itself has a pile of these things, basically all the libraries and Samples as targets.

Urho3D has a folder for External Dependencies, but it doesn't have anything in it.

There should be a CMakeLists.txt.

If you have nothing whatsoever inside of ALL_BUILD, then something is definitely wrong.  

It's been quite some time since I've written a CMakeLists.txt for brand new code, as opposed to debugging an open source project that already had one.  In short, I haven't made a production commitment to Urho3D, becuase I'm still trying to figure out what language I want to hand write 3D art assets in.  Such as inventing my own.  So I'm not much help about *how* your CMakeLists.txt is wrong.  Just that it has to be wrong.

Posting it, would certainly help.

Back in the day, I remember GLOB being a problematic construct that could get one into trouble, due to an unexpected delay as to when it would actually evaluate in the build generation process.  I doubt it belongs as part of noob advice.

I also don't approve of dorking with cmake_policy as noob guidance.  However, I'm also not motivated enough to figure out what The Right Thing To Do [TM] is.  I just want to say, for the record, that including such is absolutely terrible and completely tone deaf as far as writing noob guidance for anything.  I suspect that TRTTD is to move that machinery into the Urho3D-CMake-common module, so that nobody has to think about such an implementation detail.  And/or make any Policy go away in Urho3D, because I do see dire warnings during builds, that CMake is someday just gonna cut all that stuff off.

So it is possible, that the wiki page you are reading is wrong, bugged, and unhelpful.  But I don't actually know.

-------------------------

SirNate0 | 2020-04-02 19:20:39 UTC | #56

Did you create source files? Do you have spaces in the project path? Other than that I personally have no ideas, I don't use VS.

-------------------------

Penny | 2020-04-03 23:36:12 UTC | #57

Hiya, That is the guide I followed exactly. In the SLN, ALL_BUILD, INSTALL, ProjectTest1, ZERO_CHECK were created but they were empty.

I can only follow the instructions. I can asssure you I followed the instructions to the letter. My results are different from what the instructions claim will be the result.

Please help!
Thanks

-------------------------

bvanevery | 2020-04-04 03:05:27 UTC | #58

[quote="Penny, post:57, topic:6000"]
I can only follow the instructions.
[/quote]

Right.  Unfortunately as I alluded, in Open Source the instructions can be 1) wrong or 2) woefully out of date.  One makes up the shortfall by finding "understanding" from somewhere.  If nobody who "actually knows better" shows up, unfortunately the only thing left to do is, solve it oneself.  And then the great contribution of Open Source, is to share that pain and those fixes, so that the *next* person doesn't suffer as much as you did.

Maybe nobody here can help you.  *But*, at a minimum you need to post your CMakeLists.txt.

-------------------------

Penny | 2020-04-04 06:37:48 UTC | #59

Thank you!
Here it is...

# Set project name
project (TestProject2)
# Define target name
set (TARGET_NAME TestProject2)

######################################

set (URHO3D_HOME = "X:/Urho3D/build")


# Set CMake minimum version and CMake policy required by Urho3D-CMake-common module
if (WIN32)
    cmake_minimum_required (VERSION 3.2.3)      # Going forward all platforms will use this as minimum version
else ()
    cmake_minimum_required (VERSION 2.8.6)
endif ()
if (COMMAND cmake_policy)
    cmake_policy (SET CMP0003 NEW)
    if (CMAKE_VERSION VERSION_GREATER 2.8.12 OR CMAKE_VERSION VERSION_EQUAL 2.8.12)
        # INTERFACE_LINK_LIBRARIES defines the link interface
        cmake_policy (SET CMP0022 NEW)
    endif ()
    if (CMAKE_VERSION VERSION_GREATER 3.0.0 OR CMAKE_VERSION VERSION_EQUAL 3.0.0)
        # Disallow use of the LOCATION target property - so we set to OLD as we still need it
        cmake_policy (SET CMP0026 OLD)
        # MACOSX_RPATH is enabled by default
        cmake_policy (SET CMP0042 NEW)
    endif ()
endif ()
# Set CMake modules search path
set (CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/CMake/Modules)
# Include Urho3D Cmake common module
include (UrhoCommon)
# Define source files
file (GLOB SRC_CPP_FILES src/*.cpp)
file (GLOB SRC_H_FILES src/*.h)
define_source_files (GROUP EXTRA_CPP_FILES ${SRC_CPP_FILES} EXTRA_H_FILES ${SRC_H_FILES})
# Setup target with resource copying
setup_main_executable ()

-------------------------

bvanevery | 2020-04-04 15:06:24 UTC | #60

Please edit your CMakeLists.txt post to use "Preformatted text".  It's an icon that looks like this </>.

-------------------------

SirNate0 | 2020-04-04 15:50:48 UTC | #61

Or use a code block. (Three back ticks on either side)
    ```
    Your code here
    `` < Should be three of them, but then it formats it as a code block and you won't see them.

-------------------------

Lumak | 2020-04-04 17:07:19 UTC | #62

Let me add my 2cents. How I go about creating my projects is to use one of the samples that come with Urho3D as the starting point -- all my github examples were created following this method because it does not get any simpler than this. 

1 - Choose a sample which closely resembles what you're trying to accomplish
     For this example, I'll use 18_CharacterDemo as the base:
2 - copy, paste, and rename the folder --> 80_MySample
3 - go into the 80_MySample folder and open CMakeLists.txt
4 - rename
```
set (TARGET_NAME 18_CharacterDemo)
 to
set (TARGET_NAME 80_MySample)
```
4 - extend that sample and add your source/header files or simply modify what's already there
5 - open cmake_gui or use one of the cmakexx.bat files and make your project files -- DONE!

-------------------------

bvanevery | 2020-04-04 19:47:30 UTC | #63

I have modified the wiki page https://github.com/urho3d/Urho3D/wiki/Setting-up-a-Project-(CMake) to be less stupid about cmake_policy decisions.  It's still stupid, but at least there are far fewer commands to express it.  I will look into what it would take to eliminate the remaining policies from Urho3D.  This kind of machinery should either go away completely, for the sake of any noob's sanity, or else the machinery should be buried in an appropriate Urho3D specific CMake module.  It should not be user visible, as how the build works is Urho3D's problem, not the user's.

I suspect that machinery should be moved into UrhoCommon.cmake.

-------------------------

bvanevery | 2020-04-04 21:15:32 UTC | #64

Where do your own source files exist?  Are they in a subdirectory called /src ?  That advice was written with that assumption in mind.  The wiki page said:

> You might want to put your source code in a dedicated folder like `src` for example. In such a case, then you need to tell cmake to look at this folder to find your source files by completing the `CMakeLists.txt` file like this:
>
>*blah blah blah*
>*blah blah*
>*blah blah blah blah*
>*I am the count!*
>*blah blah blah*

It is probably once again extremely bad noob advice, at least from the standpoint of drop-kickability.  It assumes the noob is going to absorb the meaning and importance of a CMake GLOB command, and that for some reason, this is to be preferred over explicitly naming all of one's .cpp and .h files.  It's not going to shock me if this is the cognitive link in the chain that went totally wrong, resulting in no targets whatsoever in your project.

So, where are your source files?

-------------------------

GastaGaming | 2020-04-04 22:36:42 UTC | #65

As a newcomer, I would also like to bring my thoughts to this thread. When I first started using Urho3D I also was new to c++, CMake and how to link libraries, etc, this made reading and understanding documentation hard, not because documentation was bad.

It has way more to do with the fact as a beginner you don't know all those little things that you have to know to follow that documentation, like for example setting up environment variables and how to set start-up solution, should Urho3D documentation cover all this? Probably not. :sweat_smile:
Beter way to show all these things would be a video that assumes that the user knows very little about programming.

I could contribute and produce this video. :blush: :blush:
This video should probably assume the user is a newcomer on the windows platform and has access to visual studio. Even show how to clone source using git bash and how to run CMake GUI. How to tinker with sample projects and how to set up an external project. Separate video could show how to download Android SDK, NDK, etc and how to run Gradle. Sure users still can run into problems since many of these things are machine specific and can conflict with other programs etc, but at least it would give visually a hint on how to do those things and witch button to press in a given program.

-------------------------

bvanevery | 2020-04-05 06:24:39 UTC | #66

I personally can't stand long videos, they put me completely to sleep!  But that's me and not you.  If you like videos, and think there's anyone else out there who wants to absorb programming information that way, by all means make what you want to make.  That's how Open Source works, people work on what they can personally be interested in doing.  Not what someone would like to assign them as a labor project.  *That* costs money.  ;-)

The advice on that wiki page is still *bad*.  I can't stand that kind of bad, and that's why I'm chipping away at its badness.  It's not a matter of whether one only has noob coding skills.  I have plenty of skills and when coming to a new codebase, there's *still* such a thing as bad.  Stuff needs to be dog fed.  People need to visualize how a beginner would use something, not an expert who knows 100 gory implementation details already.

Now granted, true noob needs are subject to noobs coming along, trying things out, and actually reporting how it went for them.  Such as has happened in this thread.  But it has bothered me, for a long time, the lack of "fit and finish" in Open Source.  That's how I became a CMake expert back in the day, doing my best to fix other people's *broken* builds and make the pain go away.  Got a little too good at it, learned some hard lessons that way.  Well, it's not like you can have Open Source be perfectly smooth, that's not how it works.  But the most obvious rough edges, they gotta get sanded down, or it's *not worth anything*.

Everyone just works on what they want to be better.

-------------------------

Penny | 2020-04-05 22:57:21 UTC | #67

You make some interesting points. I have to agree that a video is a great idea but also labour intensive so, if you have the time then sure go for it.

You ask the question, "should Urho3D documentation cover all this?", the answer is definitely a big resounding yes. My response should be considered as from someone with the experience of writing idiots guides for some of the best minds in the world. Documentation and guides should always be written in the same way that you would write a guide that helps Albert Einstein learn how to tie his shoe laces. Saying, he should already know how to do that, well, im sorry, it shows a lack of understanding and perspective.

I hope you find my comments helpful.

bvanevery, I did create the src folder in the master as the instructions suggested but it remains empty and was not created in the build.

I am attempting what Lumak suggested but CMake only errors.

Thanks for all your suggestions. I will persists. For now.
Thanks.

-------------------------

SirNate0 | 2020-04-06 02:31:03 UTC | #68

[quote="Penny, post:67, topic:6000"]
I did create the src folder in the master as the instructions suggested but it remains empty and was not created in the build.
[/quote]

I suspect this is the root of your problem. Assuming I am reading this correctly, you didn't actually put any source files in it, you just have the folder. With no source files, it wouldn't surprise me that the projects are all empty. Try adding a main.cpp file to source, and maybe add a simple main function, such as this (from http://cpp.sh/)
```
// Example program
#include <iostream>
#include <string>

int main()
{
  std::string name;
  std::cout << "What is your name? ";
  getline (std::cin, name);
  std::cout << "Hello, " << name << "!\n";
}
```
Or, for a more Urho specific example, the code at https://github.com/urho3d/Urho3D/wiki/First-Project is probably a better choice.

In regards to Lumak's suggestion and your results, it's typically very hard for anyone to help if you just say there were errors without specifying what they were (typically copying and pasting the error message is the best approach to sharing it, as that avoids any missing details from summarizing/paraphrasing the message).

Good luck with getting it to work!

-------------------------

Penny | 2020-04-06 03:42:17 UTC | #69

Thank you!
I created a main.cpp within src folder and copied the code block from the "First-Project" link that you provided. I presume this is what you intended as your instructions were vague. I apologise. I created this thread asking for an "idiots guide" because the instructions provided from the start to start my first project have been completely vague. I am getting information in dips and when I follow them to the letter, as you would expect from a computer, always result in errors. I do find it odd that programmers who understand how specific you have to be to programme a computer fail to write a guide to the same standard.

Please accept the log from the attempt...
    The system is: Windows - 10.0.18362 - AMD64
Compiling the C compiler identification source file "CMakeCCompilerId.c" succeeded.
Compiler:  
Build flags: 
Id flags:  

The output was:
0
Microsoft (R) Build Engine version 16.4.0+e901037fe for .NET Framework
Copyright (C) Microsoft Corporation. All rights reserved.

Build started 06/04/2020 05:32:26.
Project "X:\Urho3D\Projects\_T3\build\CMakeFiles\3.17.0-rc3\CompilerIdC\CompilerIdC.vcxproj" on node 1 (default targets).
PrepareForBuild:
  Creating directory "Debug\".
  Creating directory "Debug\CompilerIdC.tlog\".
InitializeBuildStatus:
  Creating "Debug\CompilerIdC.tlog\unsuccessfulbuild" because "AlwaysCreate" was specified.
ClCompile:
  Y:\Games\Microsoft Visual Studio\IDE\VC\Tools\MSVC\14.24.28314\bin\HostX64\x64\CL.exe /c /nologo /W0 /WX- /diagnostics:column /Od /D _MBCS /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"Debug\\" /Fd"Debug\vc142.pdb" /Gd /TC /FC /errorReport:queue CMakeCCompilerId.c
  CMakeCCompilerId.c
Link:
  Y:\Games\Microsoft Visual Studio\IDE\VC\Tools\MSVC\14.24.28314\bin\HostX64\x64\link.exe /ERRORREPORT:QUEUE /OUT:".\CompilerIdC.exe" /INCREMENTAL:NO /NOLOGO kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /MANIFEST /MANIFESTUAC:"level='asInvoker' uiAccess='false'" /manifest:embed /PDB:".\CompilerIdC.pdb" /SUBSYSTEM:CONSOLE /TLBID:1 /DYNAMICBASE /NXCOMPAT /IMPLIB:".\CompilerIdC.lib" /MACHINE:X64 Debug\CMakeCCompilerId.obj
  CompilerIdC.vcxproj -> X:\Urho3D\Projects\_T3\build\CMakeFiles\3.17.0-rc3\CompilerIdC\.\CompilerIdC.exe
PostBuildEvent:
  for %%i in (cl.exe) do @echo CMAKE_C_COMPILER=%%~$PATH:i
  :VCEnd
  CMAKE_C_COMPILER=Y:\Games\Microsoft Visual Studio\IDE\VC\Tools\MSVC\14.24.28314\bin\Hostx64\x64\cl.exe
FinalizeBuildStatus:
  Deleting file "Debug\CompilerIdC.tlog\unsuccessfulbuild".
  Touching "Debug\CompilerIdC.tlog\CompilerIdC.lastbuildstate".
Done Building Project "X:\Urho3D\Projects\_T3\build\CMakeFiles\3.17.0-rc3\CompilerIdC\CompilerIdC.vcxproj" (default targets).

Build succeeded.
    0 Warning(s)
    0 Error(s)

Time Elapsed 00:00:01.36


Compilation of the C compiler identification source "CMakeCCompilerId.c" produced "CompilerIdC.exe"

Compilation of the C compiler identification source "CMakeCCompilerId.c" produced "CompilerIdC.vcxproj"

The C compiler identification is MSVC, found in "X:/Urho3D/Projects/_T3/build/CMakeFiles/3.17.0-rc3/CompilerIdC/CompilerIdC.exe"

Compiling the CXX compiler identification source file "CMakeCXXCompilerId.cpp" succeeded.
Compiler:  
Build flags: 
Id flags:  

The output was:
0
Microsoft (R) Build Engine version 16.4.0+e901037fe for .NET Framework
Copyright (C) Microsoft Corporation. All rights reserved.

Build started 06/04/2020 05:32:28.
Project "X:\Urho3D\Projects\_T3\build\CMakeFiles\3.17.0-rc3\CompilerIdCXX\CompilerIdCXX.vcxproj" on node 1 (default targets).
PrepareForBuild:
  Creating directory "Debug\".
  Creating directory "Debug\CompilerIdCXX.tlog\".
InitializeBuildStatus:
  Creating "Debug\CompilerIdCXX.tlog\unsuccessfulbuild" because "AlwaysCreate" was specified.
ClCompile:
  Y:\Games\Microsoft Visual Studio\IDE\VC\Tools\MSVC\14.24.28314\bin\HostX64\x64\CL.exe /c /nologo /W0 /WX- /diagnostics:column /Od /D _MBCS /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"Debug\\" /Fd"Debug\vc142.pdb" /Gd /TP /FC /errorReport:queue CMakeCXXCompilerId.cpp
  CMakeCXXCompilerId.cpp
Link:
  Y:\Games\Microsoft Visual Studio\IDE\VC\Tools\MSVC\14.24.28314\bin\HostX64\x64\link.exe /ERRORREPORT:QUEUE /OUT:".\CompilerIdCXX.exe" /INCREMENTAL:NO /NOLOGO kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /MANIFEST /MANIFESTUAC:"level='asInvoker' uiAccess='false'" /manifest:embed /PDB:".\CompilerIdCXX.pdb" /SUBSYSTEM:CONSOLE /TLBID:1 /DYNAMICBASE /NXCOMPAT /IMPLIB:".\CompilerIdCXX.lib" /MACHINE:X64 Debug\CMakeCXXCompilerId.obj
  CompilerIdCXX.vcxproj -> X:\Urho3D\Projects\_T3\build\CMakeFiles\3.17.0-rc3\CompilerIdCXX\.\CompilerIdCXX.exe
PostBuildEvent:
  for %%i in (cl.exe) do @echo CMAKE_CXX_COMPILER=%%~$PATH:i
  :VCEnd
  CMAKE_CXX_COMPILER=Y:\Games\Microsoft Visual Studio\IDE\VC\Tools\MSVC\14.24.28314\bin\Hostx64\x64\cl.exe
FinalizeBuildStatus:
  Deleting file "Debug\CompilerIdCXX.tlog\unsuccessfulbuild".
  Touching "Debug\CompilerIdCXX.tlog\CompilerIdCXX.lastbuildstate".
Done Building Project "X:\Urho3D\Projects\_T3\build\CMakeFiles\3.17.0-rc3\CompilerIdCXX\CompilerIdCXX.vcxproj" (default targets).

Build succeeded.
    0 Warning(s)
    0 Error(s)

Time Elapsed 00:00:00.69


Compilation of the CXX compiler identification source "CMakeCXXCompilerId.cpp" produced "CompilerIdCXX.exe"

Compilation of the CXX compiler identification source "CMakeCXXCompilerId.cpp" produced "CompilerIdCXX.vcxproj"

The CXX compiler identification is MSVC, found in "X:/Urho3D/Projects/_T3/build/CMakeFiles/3.17.0-rc3/CompilerIdCXX/CompilerIdCXX.exe"

Determining if the C compiler works passed with the following output:
Change Dir: X:/Urho3D/Projects/_T3/build/CMakeFiles/CMakeTmp

Run Build Command(s):Y:/Games/Microsoft Visual Studio/IDE/MSBuild/Current/Bin/MSBuild.exe cmTC_cc479.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m && Microsoft (R) Build Engine version 16.4.0+e901037fe for .NET Framework

Copyright (C) Microsoft Corporation. All rights reserved.



  Microsoft (R) C/C++ Optimizing Compiler Version 19.24.28314 for x64

  testCCompiler.c

  Copyright (C) Microsoft Corporation.  All rights reserved.

  cl /c /Zi /W3 /WX- /diagnostics:column /Od /Ob0 /D WIN32 /D _WINDOWS /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_cc479.dir\Debug\\" /Fd"cmTC_cc479.dir\Debug\vc142.pdb" /Gd /TC /errorReport:queue X:\Urho3D\Projects\_T3\build\CMakeFiles\CMakeTmp\testCCompiler.c

  cmTC_cc479.vcxproj -> X:\Urho3D\Projects\_T3\build\CMakeFiles\CMakeTmp\Debug\cmTC_cc479.exe




Detecting C compiler ABI info compiled with the following output:
Change Dir: X:/Urho3D/Projects/_T3/build/CMakeFiles/CMakeTmp

Run Build Command(s):Y:/Games/Microsoft Visual Studio/IDE/MSBuild/Current/Bin/MSBuild.exe cmTC_671bf.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m && Microsoft (R) Build Engine version 16.4.0+e901037fe for .NET Framework

Copyright (C) Microsoft Corporation. All rights reserved.



  Microsoft (R) C/C++ Optimizing Compiler Version 19.24.28314 for x64

  CMakeCCompilerABI.c

  Copyright (C) Microsoft Corporation.  All rights reserved.

  cl /c /Zi /W3 /WX- /diagnostics:column /Od /Ob0 /D WIN32 /D _WINDOWS /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_671bf.dir\Debug\\" /Fd"cmTC_671bf.dir\Debug\vc142.pdb" /Gd /TC /errorReport:queue "Y:\Program Files\CMake\share\cmake-3.17\Modules\CMakeCCompilerABI.c"

  cmTC_671bf.vcxproj -> X:\Urho3D\Projects\_T3\build\CMakeFiles\CMakeTmp\Debug\cmTC_671bf.exe




Determining if the CXX compiler works passed with the following output:
Change Dir: X:/Urho3D/Projects/_T3/build/CMakeFiles/CMakeTmp

Run Build Command(s):Y:/Games/Microsoft Visual Studio/IDE/MSBuild/Current/Bin/MSBuild.exe cmTC_bb7cd.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m && Microsoft (R) Build Engine version 16.4.0+e901037fe for .NET Framework

Copyright (C) Microsoft Corporation. All rights reserved.



  Microsoft (R) C/C++ Optimizing Compiler Version 19.24.28314 for x64

  testCXXCompiler.cxx

  Copyright (C) Microsoft Corporation.  All rights reserved.

  cl /c /Zi /W3 /WX- /diagnostics:column /Od /Ob0 /D WIN32 /D _WINDOWS /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_bb7cd.dir\Debug\\" /Fd"cmTC_bb7cd.dir\Debug\vc142.pdb" /Gd /TP /errorReport:queue X:\Urho3D\Projects\_T3\build\CMakeFiles\CMakeTmp\testCXXCompiler.cxx

  cmTC_bb7cd.vcxproj -> X:\Urho3D\Projects\_T3\build\CMakeFiles\CMakeTmp\Debug\cmTC_bb7cd.exe




Detecting CXX compiler ABI info compiled with the following output:
Change Dir: X:/Urho3D/Projects/_T3/build/CMakeFiles/CMakeTmp

Run Build Command(s):Y:/Games/Microsoft Visual Studio/IDE/MSBuild/Current/Bin/MSBuild.exe cmTC_55c1b.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m && Microsoft (R) Build Engine version 16.4.0+e901037fe for .NET Framework

Copyright (C) Microsoft Corporation. All rights reserved.



  Microsoft (R) C/C++ Optimizing Compiler Version 19.24.28314 for x64

  CMakeCXXCompilerABI.cpp

  Copyright (C) Microsoft Corporation.  All rights reserved.

  cl /c /Zi /W3 /WX- /diagnostics:column /Od /Ob0 /D WIN32 /D _WINDOWS /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_55c1b.dir\Debug\\" /Fd"cmTC_55c1b.dir\Debug\vc142.pdb" /Gd /TP /errorReport:queue "Y:\Program Files\CMake\share\cmake-3.17\Modules\CMakeCXXCompilerABI.cpp"

  cmTC_55c1b.vcxproj -> X:\Urho3D\Projects\_T3\build\CMakeFiles\CMakeTmp\Debug\cmTC_55c1b.exe

-------------------------

GastaGaming | 2020-04-06 07:05:44 UTC | #70

Hey, Penny, I recorded a video yesterday to test out if it is possible to make an informative video that is a reasonable length. The test was somewhat successful without a manuscript and not much planning.
I tried to use VirtualBox to run Windows 10 VM which caused some rendering issues because of the software GPU. I am going to do a more planned version on physical hardware which I believe can be easily compressed in 10mins. 😊

I keep this video private for now and I will take it down when I will have a more polished version of it.
Here is a link to the video 🙂
https://youtu.be/mbWHHMmkIC0 

Documentation that I made for our school project. Which is almost an "idiots guide"
**https://tinyurl.com/ul4qdhf**

-------------------------

Penny | 2020-04-06 11:05:01 UTC | #71

Hi GastaGaming,
Your video was very interesting. I certainly learned a lot.
I replicated exactly everything you did.
When I went into VS via CMake OpenProject the following were listed but there was nothing inside...
ALL_BUILD, INSTALL, NextBigMMO, RESOURCE_CHECK, ZERO_CHECK

I do not understand why you have entries and I do not.
Thank you.

-------------------------

Modanung | 2020-04-06 12:24:22 UTC | #72

There's a drop-down list for selecting the documentation version, next to the light switch. :slightly_smiling_face:

-------------------------

bvanevery | 2020-04-06 13:56:09 UTC | #73

I notice there is a difference between GLOB statements on [the wiki page](https://github.com/urho3d/Urho3D/wiki/Setting-up-a-Project-(CMake))

```
file (GLOB SRC_CPP_FILES src/*.cpp)
file (GLOB SRC_H_FILES src/*.h)
```
and what you posted in this thread:

[quote="Penny, post:59, topic:6000"]
# Define source files

file (GLOB SRC_CPP_FILES src/ <em>.cpp)
file (GLOB SRC_H_FILES src/</em> .h)
[/quote]

Note the lack of asterisks.  Without asterisks, these would match files literally named .cpp and .h.  Which of course you don't have, so no targets.

Now I think what actually happened when you posted in this thread, is you didn't use any kind of code formatting thingy, like the </> icon or the \``` ``` backticking for code.  So the asterisks got interpreted as you wanting *italics* between them.  Maybe you don't have any error in your CMakeLists.txt, but please check.

-------------------------

bvanevery | 2020-04-06 14:31:50 UTC | #74

When I stared at your long logfile, nothing obvious lept out at me as being wrong.  But then, I haven't stared at that kind of logfile in awhile either.

I keep coming back to "the GLOB statement is written incorrectly" as the answer for why you don't have targets.  The original wiki advice could be plain outright wrong, or insufficient in the case of an out-of-source build, or out of date due to subsequent versions of CMake, or who knows.  My CMake kung fu is not quite what it used to be, and I never used GLOB statements at all back in the day.  I remember they were trouble.

You could try adding a directory macro to the GLOB, per some advice I found on [Stack Overflow](https://stackoverflow.com/questions/34863374/how-to-use-cmake-file-glob-srcs-with-a-build-directory):

```
file (GLOB SRC_CPP_FILES ${PROJECT_SOURCE_DIR}/src/*.cpp)
file (GLOB SRC_H_FILES ${PROJECT_SOURCE_DIR}/src/*.h)
```

You could try explicitly listing every file, and not relying on a GLOB.  That Stack Overflow advice said, **"As Phil reminds, CMake documentation doesn't recommend this use of GLOB."**  Which is how I remember it from back in the day.  To be explicit, you'd do stuff like:

```
set(SRC_CPP_FILES ${PROJECT_SOURCE_DIR}/src/main.cpp
              ${PROJECT_SOURCE_DIR}/src/someother.cpp
              ${PROJECT_SOURCE_DIR}/src/yougettheidea.cpp     
)
set(SRC_H_FILES ${PROJECT_SOURCE_DIR}/src/something.h)
```
Reconsidering the wisdom of /src, for a teeny tiny Hello World project, is left as an exercise to the reader.

-------------------------

SirNate0 | 2020-04-06 14:45:20 UTC | #75

Switching to `file (GLOB_RECURSE SRC_CPP_FILES *.cpp)` or better `file (GLOB_RECURSE SRC_CPP_FILES ${PROJECT_SOURCE_DIR}/src/*.cpp)` would likely also work. (I'm not sure if the `${PROJECT_SOURCE_DIR}` would need to be added to the first or not). Either way, probably the easiest check is to list the files explicitly as suggested at the end of bvanevery's post and see what happens - I assume that would result in an actual error if the file wasn't found.

-------------------------

Penny | 2020-04-06 15:13:21 UTC | #76

I have extra confusion because the only 2 files I created are CMakelists.txt and Main.cpp and neither contain text anything like what you are both posting.

-------------------------

jmiller | 2020-04-06 15:55:55 UTC | #77

Good to see progress and contributions. :slight_smile:

For reference, `CMakeLists.txt` and `GLOB` are also covered to some extent in
  https://urho3d.github.io/documentation/HEAD/_using_library.html
and do let us know where it could be improved in a concise way.

edit: Some find GLOB to be a useful time-saver (I have nearly always used it in Urho projects) and should be wary of the possible pitfall.

-------------------------

bvanevery | 2020-04-06 16:50:23 UTC | #78

Confusion is understandable, but you actually have to solider through the confusion and follow at least *someone's* advice that someone's giving you.  Only way to move the ball forwards.

When you don't know what's going on, the basic skill is *hacking*.  Not waiting to follow directions, or even requiring an understanding of directions, to try out different stuff.  My advice is and has been, you need to hack the list of files differently.  I think GLOB is a bad idea.  I've given you 2 different ways to do it differently.  YMMV.

I don't understand how your CMakeLists.txt can be "vastly" different from what I recently talked about, because you *posted* your own CMakeLists.txt, *I thought*, albeit with really bad forum formatting that's hard to read.  Please use those </> or \``` tricks.  You can edit old posts too.

It may be appropriate for you to .zip up all your project source files and directory structure, and post them as an attachment.  Then someone could try it out on their machine and see how it fails or succeeds for them.  Way easier to look at the log results too.

-------------------------

Penny | 2020-04-06 23:47:50 UTC | #79

Here you are, as requested...

https://www.dropbox.com/s/5qy8agx8v5hy645/NextBigMMO.rar?dl=0

Thank you!

-------------------------

bvanevery | 2020-04-07 00:21:55 UTC | #80

More than I bargained for, but at least it makes CMake forensics easier.  I'm poking through stuff.  Not much to say yet.

Based on the existence of a subdirectory called \NextBigMMO\CMakeFiles\3.17.0-rc3 I believe you are using CMake version 3.17.0-rc3.  Please install version 3.17.0 which has now been released.  In general in the future, *do not* use Release Candidates for your work.  They could be buggy, that's why they're Release Candidates and not official releases.  Please rebuild your project cleanly, getting rid of all the previous built and generated stuff.  This BTW is why you do out-of-source builds, to make that easy to do.  This exercise will probably not fix your problem, but who knows, just in case.  And you should not be using a RC for your work anyways, so nothing lost by doing this.

-------------------------

Penny | 2020-04-07 07:48:54 UTC | #81

Hiya,
I reinstalled CMake as you suggested.
I downloaded a fresh version of Urho3D-master.

I generated using CMake.
Now when I go into VS to look at the samples, none of those projects have anything listed.
I did before. The samples compiled ok and will run. I simply do not understand why the files aren't listed in the resource view.
I did update VS though, has a setting in VS been changed?
Figured it out. It was the resource view not the solution view.


Right! Awesome! I have compiled and run the null main loop.
I have even downloaded the template project and run that.
I feel I am now good to go.
Thank you very much for your support.
Is there anything I can provide to give back to the community?
Thank you.

-------------------------

bvanevery | 2020-04-07 16:30:59 UTC | #82

Wow, so the problem was ultimately which tabbed window in Visual Studio you were looking at?  I would never have guessed.  Good to know.

The moral of the story would be to start with a "known good" CMake build of some kind, to eliminate doubt about CMake itself being bugged, your development libraries being incorrectly installed, Visual Studio not working, etc.  At least I did notice you using a CMake Release Candidate instead of a full release.

I will continue to look into the issues raised by this "dog feeding" exercise.  Some things could definitely be simpler.

The utility function define_source_files() did seem to work, as your main.cpp did exist in the Visual Studio project file.  That had me really scratching my head.

-------------------------

Penny | 2020-04-08 02:20:42 UTC | #83

Yeah, as I am not that familiar with VS was unaware of the difference between the Solution view and the Resource View, not sure how or why it changed.
Another big and fantastic lesson for me :slight_smile:
Thanks!

-------------------------

bvanevery | 2020-04-08 12:41:29 UTC | #84

None of us thought of taking a screenshot as a sanity check.

-------------------------

