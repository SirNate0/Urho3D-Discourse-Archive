rogerdv | 2017-01-02 01:00:46 UTC | #1

Im trying to compile for Windows using Visual Studio Express 2010. I run the corresponding bat file (cmake_vs2010) but I get a lot of errors:

[code]D:\work\Urho3D>cmake_vs2010.bat

D:\work\Urho3D>cmake -E chdir Build cmake  -G "Visual Studio 10" VERSION=10 -DUR
HO3D_SAMPLES=1 URHO3D_LUAJIT=1 ..\Source
-- The C compiler identification is MSVC 16.0.30319.1
-- The CXX compiler identification is MSVC 16.0.30319.1
-- Check for working C compiler using: Visual Studio 10 2010
-- Check for working C compiler using: Visual Studio 10 2010 -- broken
CMake Error at C:/Program Files (x86)/CMake/share/cmake-3.0/Modules/CMakeTestCCo
mpiler.cmake:61 (message):
  The C compiler "C:/Program Files (x86)/Microsoft Visual Studio
  10.0/VC/bin/cl.exe" is not able to compile a simple test program.

  It fails with the following output:

   Change Dir: D:/work/Urho3D/Build/CMakeFiles/CMakeTmp

Run Build Command:"C:/Windows/Microsoft.NET/Framework/v4.0.30319/MSBuild.exe" "cmTryCompileExec3866937741.vcxproj" "/p:Configuration=Debug" "/p:VisualStudioVersion=10.0"
Microsoft (R) Build Engine version 4.0.30319.17929

[Microsoft .NET Framework, version 4.0.30319.17929]

Copyright (C) Microsoft Corporation. All rights reserved.



Build started 13/10/2014 11:08:23.

Project "D:\work\Urho3D\Build\CMakeFiles\CMakeTmp\cmTryCompileExec3866937741.vcxproj" on node 1 (default targets).

PrepareForBuild:

  Creating directory "cmTryCompileExec3866937741.dir\Debug\".

  Creating directory "D:\work\Urho3D\Build\CMakeFiles\CMakeTmp\Debug\".

InitializeBuildStatus:

  Creating "cmTryCompileExec3866937741.dir\Debug\cmTryCompileExec3866937741.unsuccessfulbuild" because "AlwaysCreate" was specified.

ClCompile:

  C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\bin\CL.exe /c /Zi /W3 /WX- /Od /Ob0 /Oy- /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTryCompileExec3866937741.dir\Debug\\" /Fd"cmTryCompileExec3866937741.dir\Debug\vc100.pdb" /Gd /TC /analyze- /errorReport:queue testCCompiler.c

  Microsoft (R) 32-bit C/C++ Optimizing Compiler Version 16.00.30319.01 for 80x86

  Copyright (C) Microsoft Corporation.  All rights reserved.

  

  cl /c /Zi /W3 /WX- /Od /Ob0 /Oy- /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTryCompileExec3866937741.dir\Debug\\" /Fd"cmTryCompileExec3866937741.dir\Debug\vc100.pdb" /Gd /TC /analyze- /errorReport:queue testCCompiler.c

  

  testCCompiler.c

ManifestResourceCompile:

  C:\Program Files (x86)\Microsoft SDKs\Windows\v7.0A\bin\rc.exe /nologo /fo"cmTryCompileExec3866937741.dir\Debug\cmTryCompileExec3866937741.exe.embed.manifest.res" cmTryCompileExec3866937741.dir\Debug\cmTryCompileExec3866937741_manifest.rc 

Link:

  C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\bin\link.exe /ERRORREPORT:QUEUE /OUT:"D:\work\Urho3D\Build\CMakeFiles\CMakeTmp\Debug\cmTryCompileExec3866937741.exe" /INCREMENTAL /NOLOGO kernel32.lib user32.lib gdi32.lib winspool.lib shell32.lib ole32.lib oleaut32.lib uuid.lib comdlg32.lib advapi32.lib /MANIFEST /ManifestFile:"cmTryCompileExec3866937741.dir\Debug\cmTryCompileExec3866937741.exe.intermediate.manifest" /MANIFESTUAC:"level='asInvoker' uiAccess='false'" /DEBUG /PDB:"D:/work/Urho3D/Build/CMakeFiles/CMakeTmp/Debug/cmTryCompileExec3866937741.pdb" /SUBSYSTEM:CONSOLE /TLBID:1 /DYNAMICBASE /NXCOMPAT /IMPLIB:"D:/work/Urho3D/Build/CMakeFiles/CMakeTmp/Debug/cmTryCompileExec3866937741.lib" /MACHINE:X86 cmTryCompileExec3866937741.dir\Debug\cmTryCompileExec3866937741.exe.embed.manifest.res

  cmTryCompileExec3866937741.dir\Debug\testCCompiler.obj  /machine:X86 /debug 

LINK : fatal error LNK1123: failure during conversion to COFF: file invalid or corrupt [D:\work\Urho3D\Build\CMakeFiles\CMakeTmp\cmTryCompileExec3866937741.vcxproj]

Done Building Project "D:\work\Urho3D\Build\CMakeFiles\CMakeTmp\cmTryCompileExec3866937741.vcxproj" (default targets) -- FAILED.



Build FAILED.



"D:\work\Urho3D\Build\CMakeFiles\CMakeTmp\cmTryCompileExec3866937741.vcxproj" (default target) (1) ->

(Link target) -> 

  LINK : fatal error LNK1123: failure during conversion to COFF: file invalid or corrupt [D:\work\Urho3D\Build\CMakeFiles\CMakeTmp\cmTryCompileExec3866937741.vcxproj]



    0 Warning(s)

    1 Error(s)



Time Elapsed 00:00:01.09
[/code]

What Im doing wrong here?

-------------------------

cin | 2017-01-02 01:00:46 UTC | #2

Another version of Visual Studio installed?

-------------------------

rogerdv | 2017-01-02 01:00:47 UTC | #3

Nop, only 2010, with VC++ and VC# installed.

-------------------------

Bluemoon | 2017-01-02 01:00:47 UTC | #4

Just tried it on my system and got the same error with windows reporting that "Microsoft Resource File To COFF Object Conversion Utility has stopped working" more like a crash. I used both the cmake batch file supplied with Urho3D and the cmake-gui, the Urho3D source used was downloaded three days ago.
My System is Windows Vista, 4GB Ram, with visual c++ 2010 ( and also visual c# 2010 just like rogerdv)
Below is the output of cmake
[code]
Check for working C compiler using: Visual Studio 10
Check for working C compiler using: Visual Studio 10 -- broken
CMake Error at C:/CMAKE/share/cmake-2.8/Modules/CMakeTestCCompiler.cmake:52 (MESSAGE):
  The C compiler "cl" is not able to compile a simple test program.

  It fails with the following output:

   Change Dir: C:/Build_Folder/Urho3D-master/Build/CMakeFiles/CMakeTmp

  

  Run Build Command:C:\Windows\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe
  cmTryCompileExec231998991.vcxproj /p:Configuration=Debug

  Microsoft (R) Build Engine version 4.0.30319.17929

  [Microsoft .NET Framework, version 4.0.30319.17929]

  Copyright (C) Microsoft Corporation.  All rights reserved.

  Build started 13/10/2014 23:03:04.

  Project
  "C:\Build_Folder\Urho3D-master\Build\CMakeFiles\CMakeTmp\cmTryCompileExec231998991.vcxproj"
  on node 1 (default targets).

  PrepareForBuild:

    Creating directory "cmTryCompileExec231998991.dir\Debug\".

  InitializeBuildStatus:

    Creating "cmTryCompileExec231998991.dir\Debug\cmTryCompileExec231998991.unsuccessfulbuild" because "AlwaysCreate" was specified.

  ClCompile:

    C:\Program Files\Microsoft Visual Studio 10.0\VC\bin\CL.exe /c /Zi /W3 /WX- /Od /Ob0 /Oy- /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTryCompileExec231998991.dir\Debug\\" /Fd"C:/Build_Folder/Urho3D-master/Build/CMakeFiles/CMakeTmp/Debug/cmTryCompileExec231998991.pdb" /Gd /TC /analyze- /errorReport:queue "C:\Build_Folder\Urho3D-master\Build\CMakeFiles\CMakeTmp\testCCompiler.c"  /Zm1000 
    Microsoft (R) 32-bit C/C++ Optimizing Compiler Version 16.00.30319.01 for 80x86
    Copyright (C) Microsoft Corporation.  All rights reserved.
    
    cl /c /Zi /W3 /WX- /Od /Ob0 /Oy- /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTryCompileExec231998991.dir\Debug\\" /Fd"C:/Build_Folder/Urho3D-master/Build/CMakeFiles/CMakeTmp/Debug/cmTryCompileExec231998991.pdb" /Gd /TC /analyze- /errorReport:queue "C:\Build_Folder\Urho3D-master\Build\CMakeFiles\CMakeTmp\testCCompiler.c"  /Zm1000 
    testCCompiler.c
    

  ManifestResourceCompile:

    C:\Program Files\Microsoft SDKs\Windows\v7.0A\bin\rc.exe /nologo /fo"cmTryCompileExec231998991.dir\Debug\cmTryCompileExec231998991.exe.embed.manifest.res" cmTryCompileExec231998991.dir\Debug\cmTryCompileExec231998991_manifest.rc 

  Link:

    C:\Program Files\Microsoft Visual Studio 10.0\VC\bin\link.exe /ERRORREPORT:QUEUE /OUT:"C:\Build_Folder\Urho3D-master\Build\CMakeFiles\CMakeTmp\Debug\cmTryCompileExec231998991.exe" /INCREMENTAL /NOLOGO kernel32.lib user32.lib gdi32.lib winspool.lib shell32.lib ole32.lib oleaut32.lib uuid.lib comdlg32.lib advapi32.lib /MANIFEST /ManifestFile:"cmTryCompileExec231998991.dir\Debug\cmTryCompileExec231998991.exe.intermediate.manifest" /MANIFESTUAC:"level='asInvoker' uiAccess='false'" /DEBUG /PDB:"C:/Build_Folder/Urho3D-master/Build/CMakeFiles/CMakeTmp/Debug/cmTryCompileExec231998991.pdb" /SUBSYSTEM:CONSOLE /STACK:"10000000" /TLBID:1 /DYNAMICBASE /NXCOMPAT /IMPLIB:"C:/Build_Folder/Urho3D-master/Build/CMakeFiles/CMakeTmp/Debug/cmTryCompileExec231998991.lib" /MACHINE:X86 cmTryCompileExec231998991.dir\Debug\cmTryCompileExec231998991.exe.embed.manifest.res
    cmTryCompileExec231998991.dir\Debug\testCCompiler.obj  /machine:X86 /debug 

  LINK : fatal error LNK1123: failure during conversion to COFF: file invalid
  or corrupt
  [C:\Build_Folder\Urho3D-master\Build\CMakeFiles\CMakeTmp\cmTryCompileExec231998991.vcxproj]


  Done Building Project
  "C:\Build_Folder\Urho3D-master\Build\CMakeFiles\CMakeTmp\cmTryCompileExec231998991.vcxproj"
  (default targets) -- FAILED.

  Build FAILED.
  
  "C:\Build_Folder\Urho3D-master\Build\CMakeFiles\CMakeTmp\cmTryCompileExec231998991.vcxproj"
  (default target) (1) ->

  (Link target) -> 

    LINK : fatal error LNK1123: failure during conversion to COFF: file invalid or corrupt [C:\Build_Folder\Urho3D-master\Build\CMakeFiles\CMakeTmp\cmTryCompileExec231998991.vcxproj]

      0 Warning(s)
      1 Error(s)

  Time Elapsed 00:00:06.48

  CMake will not be able to correctly generate this project.
Call Stack (most recent call first):
  CMakeLists.txt:24 (project)


Configuring incomplete, errors occurred!
[/code]

I feel the issue might be from the cmake build script  :frowning:

-------------------------

weitjong | 2017-01-02 01:00:47 UTC | #5

I doubt that this issue is caused by the CMake build script itself, although I could be wrong.

I have quickly done a google search on the reported problem and immediately reveal the problem is not unique to our project. If you have to stay with an outdated VS 2010 then you probably should ensure your other components (e.g. .NET framework) in your host system stays slightly outdated as well so they are compatible with VS 2010. And also ensure that your PATH environment variable is correctly set so that CMake is able to invoke "cmd.exe". These are the two reasons I find to be the most plausible for your problem. Google is your best friend.

[delta3d.org/forum/viewtopic.php?showtopic=22426](http://delta3d.org/forum/viewtopic.php?showtopic=22426)

-------------------------

rogerdv | 2017-01-02 01:00:47 UTC | #6

Tried at home yesterday and it built the engine successfully (except for the samples, but thats not essential). Same setup: VC++/VC# 2010.

-------------------------

