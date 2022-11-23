ToolmakerSteve | 2021-12-03 02:01:41 UTC | #1

I am following instructions at https://github.com/urho3d/Urho3D/wiki/Setting-up-Urho3D-on-Windows-with-Visual-Studio.

downloaded current cmake.org.  
run cmake-gui.exe  
Where is source code: selected root folder of local repo, "C:\gh\Urho3D".  
Where to build binaries: selected a new folder I made, "C:\gh\Urho3D\_build"  
"Configure"  
Specify generator: Visual Studio 16 2019
everything else default (use default native compilers)
Finish  

result is

> "Error in configuration process, project files may be invalid"

Also adds an entry (in red):

> CMAKE_CONFIGURATION_TYPES   Debug;Release;MinSizeRel;RelWithDebInfo

--------------------------

Configuring incomplete, errors occurred!

See also "C:/gh/Urho3D/_build/CMakeFiles/CMakeOutput.log".

CMakeOutput.log:

> The system is: Windows - 10.0.19043 - AMD64

----------------------------------------------

I don't know how to proceed.

* For source, should I instead select some subfolder?
* What else could be wrong?

-------------------------

SirNate0 | 2021-12-03 02:16:49 UTC | #2

Are there any other errors shown? It's pretty unusual for it to only say that there was an error without saying more about what caused it.

You may want to try deleting the build tree, and using one of the cmake_*.bat files to create it.

-------------------------

ToolmakerSteve | 2021-12-03 02:59:20 UTC | #3

I had never previously done any build - not even the "rake" one - because I have been accessing in C# via Urho.Net.

Just tried "rake build install". It promptly told me that the version of Windows SDK this is configured for could not be found. Sure enough, I never installed the latest SDK (or at least never told VS 2019 how to find it).

I'll go through the tutorial on building first project using rake. Then come back to this.

-------------------------

ToolmakerSteve | 2021-12-03 03:23:35 UTC | #4

Fixed. Uninstalled cmake. Reinstalled. Noticed that default install options DON'T add cmake to path!

Chose the option that does. Rebooted. All good.

-------------------------

ToolmakerSteve | 2021-12-03 03:26:23 UTC | #5

Though at the end it does say

> Could NOT find Doxygen (missing: DOXYGEN_EXECUTABLE) 

When is that needed?

------------------

Didn't seem to cause problem. After that it shows:

> Configuring done
> Generating done

-------------------------

ToolmakerSteve | 2021-12-03 03:31:21 UTC | #6

Just discovered there is also an error log. Don't know if anything here is significant:

Performing C SOURCE FILE Test HAVE_XINPUT_GAMEPAD_EX failed with the following output:
Change Dir: C:/gh/Urho3D/_build/CMakeFiles/CMakeTmp

Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Enterprise/MSBuild/Current/Bin/MSBuild.exe cmTC_47fe5.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m && Microsoft (R) Build Engine version 16.11.1+3e40a09f8 for .NET Framework

Copyright (C) Microsoft Corporation. All rights reserved.



  Microsoft (R) C/C++ Optimizing Compiler Version 19.29.30136 for x64

  Copyright (C) Microsoft Corporation.  All rights reserved.

  src.c

  cl /c /Zi /W3 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D HAVE_XINPUT_GAMEPAD_EX /D "CMAKE_INTDIR=\"Debug\"" /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_47fe5.dir\Debug\\" /Fd"cmTC_47fe5.dir\Debug\vc142.pdb" /external:W3 /Gd /TC /errorReport:queue C:\gh\Urho3D\_build\CMakeFiles\CMakeTmp\src.c

C:\Program Files (x86)\Windows Kits\10\Include\10.0.22000.0\um\winnt.h(169,1): fatal error C1189: #error:  "No Target Architecture" [C:\gh\Urho3D\_build\CMakeFiles\CMakeTmp\cmTC_47fe5.vcxproj]



Source file was:

#include <xinput.h>

int main()
{
  (void)sizeof(((XINPUT_GAMEPAD_EX *)0)->wButtons);
  return 0;
}

Performing C SOURCE FILE Test HAVE_XINPUT_STATE_EX failed with the following output:
Change Dir: C:/gh/Urho3D/_build/CMakeFiles/CMakeTmp

Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Enterprise/MSBuild/Current/Bin/MSBuild.exe cmTC_2d217.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m && Microsoft (R) Build Engine version 16.11.1+3e40a09f8 for .NET Framework

Copyright (C) Microsoft Corporation. All rights reserved.



  Microsoft (R) C/C++ Optimizing Compiler Version 19.29.30136 for x64

  Copyright (C) Microsoft Corporation.  All rights reserved.

  src.c

  cl /c /Zi /W3 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D HAVE_XINPUT_STATE_EX /D "CMAKE_INTDIR=\"Debug\"" /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_2d217.dir\Debug\\" /Fd"cmTC_2d217.dir\Debug\vc142.pdb" /external:W3 /Gd /TC /errorReport:queue C:\gh\Urho3D\_build\CMakeFiles\CMakeTmp\src.c

C:\Program Files (x86)\Windows Kits\10\Include\10.0.22000.0\um\winnt.h(169,1): fatal error C1189: #error:  "No Target Architecture" [C:\gh\Urho3D\_build\CMakeFiles\CMakeTmp\cmTC_2d217.vcxproj]



Source file was:

#include <xinput.h>

int main()
{
  (void)sizeof(((XINPUT_STATE_EX *)0)->dwPacketNumber);
  return 0;
}

Determining if the function __sincosf exists failed with the following output:
Change Dir: C:/gh/Urho3D/_build/CMakeFiles/CMakeTmp

Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Enterprise/MSBuild/Current/Bin/MSBuild.exe cmTC_07f7f.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m && Microsoft (R) Build Engine version 16.11.1+3e40a09f8 for .NET Framework

Copyright (C) Microsoft Corporation. All rights reserved.



  Microsoft (R) C/C++ Optimizing Compiler Version 19.29.30136 for x64

  Copyright (C) Microsoft Corporation.  All rights reserved.

  CheckFunctionExists.c

  cl /c /Zi /W3 /WX- /diagnostics:column /MP /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D CHECK_FUNCTION_EXISTS=__sincosf /D "CMAKE_INTDIR=\"Debug\"" /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_07f7f.dir\Debug\\" /Fd"cmTC_07f7f.dir\Debug\vc142.pdb" /external:W3 /Gd /TC /errorReport:queue "C:\Program Files\CMake\share\cmake-3.22\Modules\CheckFunctionExists.c"

CheckFunctionExists.obj : error LNK2019: unresolved external symbol __sincosf referenced in function main [C:\gh\Urho3D\_build\CMakeFiles\CMakeTmp\cmTC_07f7f.vcxproj]

C:\gh\Urho3D\_build\CMakeFiles\CMakeTmp\Debug\cmTC_07f7f.exe : fatal error LNK1120: 1 unresolved externals [C:\gh\Urho3D\_build\CMakeFiles\CMakeTmp\cmTC_07f7f.vcxproj]




Determining if the function malloc_usable_size exists failed with the following output:
Change Dir: C:/gh/Urho3D/_build/CMakeFiles/CMakeTmp

Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Enterprise/MSBuild/Current/Bin/MSBuild.exe cmTC_6b07f.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m && Microsoft (R) Build Engine version 16.11.1+3e40a09f8 for .NET Framework

Copyright (C) Microsoft Corporation. All rights reserved.



  Microsoft (R) C/C++ Optimizing Compiler Version 19.29.30136 for x64

  Copyright (C) Microsoft Corporation.  All rights reserved.

  CheckFunctionExists.c

  cl /c /Zi /W3 /WX- /diagnostics:column /MP /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D CHECK_FUNCTION_EXISTS=malloc_usable_size /D "CMAKE_INTDIR=\"Debug\"" /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_6b07f.dir\Debug\\" /Fd"cmTC_6b07f.dir\Debug\vc142.pdb" /external:W3 /Gd /TC /errorReport:queue "C:\Program Files\CMake\share\cmake-3.22\Modules\CheckFunctionExists.c"

CheckFunctionExists.obj : error LNK2019: unresolved external symbol malloc_usable_size referenced in function main [C:\gh\Urho3D\_build\CMakeFiles\CMakeTmp\cmTC_6b07f.vcxproj]

C:\gh\Urho3D\_build\CMakeFiles\CMakeTmp\Debug\cmTC_6b07f.exe : fatal error LNK1120: 1 unresolved externals [C:\gh\Urho3D\_build\CMakeFiles\CMakeTmp\cmTC_6b07f.vcxproj]




Determining if the function sincosf exists in the m failed with the following output:
Change Dir: C:/gh/Urho3D/_build/CMakeFiles/CMakeTmp

Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Enterprise/MSBuild/Current/Bin/MSBuild.exe cmTC_5c861.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m && Microsoft (R) Build Engine version 16.11.1+3e40a09f8 for .NET Framework

Copyright (C) Microsoft Corporation. All rights reserved.



  Microsoft (R) C/C++ Optimizing Compiler Version 19.29.30136 for x64

  Copyright (C) Microsoft Corporation.  All rights reserved.

  CheckFunctionExists.c

  cl /c /Zi /W3 /WX- /diagnostics:column /MP /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D CHECK_FUNCTION_EXISTS=sincosf /D "CMAKE_INTDIR=\"Debug\"" /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_5c861.dir\Debug\\" /Fd"cmTC_5c861.dir\Debug\vc142.pdb" /external:W3 /Gd /TC /errorReport:queue "C:\Program Files\CMake\share\cmake-3.22\Modules\CheckFunctionExists.c"

LINK : fatal error LNK1104: cannot open file 'm.lib' [C:\gh\Urho3D\_build\CMakeFiles\CMakeTmp\cmTC_5c861.vcxproj]




Checking whether the ASM_MASM compiler is GNU using "--version" did not match "(GNU assembler)|(GCC)|(Free Software Foundation)":
Microsoft (R) Macro Assembler (x64) Version 14.29.30136.0
Copyright (C) Microsoft Corporation.  All rights reserved.

MASM : warning A4018:invalid command-line option : --version
MASM : fatal error A1017:missing source filename
Checking whether the ASM_MASM compiler is Clang using "--version" did not match "(clang version)":
Microsoft (R) Macro Assembler (x64) Version 14.29.30136.0
Copyright (C) Microsoft Corporation.  All rights reserved.

MASM : warning A4018:invalid command-line option : --version
MASM : fatal error A1017:missing source filename
Checking whether the ASM_MASM compiler is AppleClang using "--version" did not match "(Apple LLVM version)":
Microsoft (R) Macro Assembler (x64) Version 14.29.30136.0
Copyright (C) Microsoft Corporation.  All rights reserved.

MASM : warning A4018:invalid command-line option : --version
MASM : fatal error A1017:missing source filename
Checking whether the ASM_MASM compiler is ARMClang using "--version" did not match "armclang":
Microsoft (R) Macro Assembler (x64) Version 14.29.30136.0
Copyright (C) Microsoft Corporation.  All rights reserved.

MASM : warning A4018:invalid command-line option : --version
MASM : fatal error A1017:missing source filename
Checking whether the ASM_MASM compiler is HP using "-V" did not match "HP C":
Microsoft (R) Macro Assembler (x64) Version 14.29.30136.0
Copyright (C) Microsoft Corporation.  All rights reserved.

MASM : warning A4018:invalid command-line option : -V
MASM : fatal error A1017:missing source filename
Checking whether the ASM_MASM compiler is Intel using "--version" did not match "(ICC)":
Microsoft (R) Macro Assembler (x64) Version 14.29.30136.0
Copyright (C) Microsoft Corporation.  All rights reserved.

MASM : warning A4018:invalid command-line option : --version
MASM : fatal error A1017:missing source filename
Checking whether the ASM_MASM compiler is IntelLLVM using "--version" did not match "(Intel[^
]+oneAPI)":
Microsoft (R) Macro Assembler (x64) Version 14.29.30136.0
Copyright (C) Microsoft Corporation.  All rights reserved.

MASM : warning A4018:invalid command-line option : --version
MASM : fatal error A1017:missing source filename
Checking whether the ASM_MASM compiler is SunPro using "-V" did not match "Sun C":
Microsoft (R) Macro Assembler (x64) Version 14.29.30136.0
Copyright (C) Microsoft Corporation.  All rights reserved.

MASM : warning A4018:invalid command-line option : -V
MASM : fatal error A1017:missing source filename
Checking whether the ASM_MASM compiler is XL using "-qversion" did not match "XL C":
Microsoft (R) Macro Assembler (x64) Version 14.29.30136.0
Copyright (C) Microsoft Corporation.  All rights reserved.

MASM : warning A4018:invalid command-line option : -qversion
MASM : fatal error A1017:missing source filename
Determining if the _TIMESPEC_DEFINED exist failed with the following output:
Change Dir: C:/gh/Urho3D/_build/CMakeFiles/CMakeTmp

Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Enterprise/MSBuild/Current/Bin/MSBuild.exe cmTC_199c4.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m && Microsoft (R) Build Engine version 16.11.1+3e40a09f8 for .NET Framework

Copyright (C) Microsoft Corporation. All rights reserved.



  Microsoft (R) C/C++ Optimizing Compiler Version 19.29.30136 for x64

  Copyright (C) Microsoft Corporation.  All rights reserved.

  CheckSymbolExists.c

  cl /c /Zi /W3 /WX- /diagnostics:column /MP /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D "CMAKE_INTDIR=\"Debug\"" /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_199c4.dir\Debug\\" /Fd"cmTC_199c4.dir\Debug\vc142.pdb" /external:W3 /Gd /TC /errorReport:queue C:\gh\Urho3D\_build\CMakeFiles\CMakeTmp\CheckSymbolExists.c

C:\gh\Urho3D\_build\CMakeFiles\CMakeTmp\CheckSymbolExists.c(8,36): error C2065: '_TIMESPEC_DEFINED': undeclared identifier [C:\gh\Urho3D\_build\CMakeFiles\CMakeTmp\cmTC_199c4.vcxproj]



File C:/gh/Urho3D/_build/CMakeFiles/CMakeTmp/CheckSymbolExists.c:
/* */
#include <time.h>

int main(int argc, char** argv)
{
  (void)argv;
#ifndef _TIMESPEC_DEFINED
  return ((int*)(&_TIMESPEC_DEFINED))[argc];
#else
  (void)argc;
  return 0;
#endif
}
Performing C++ SOURCE FILE Test INET_FUNCTIONS_EXISTS_1 failed with the following output:
Change Dir: C:/gh/Urho3D/_build/CMakeFiles/CMakeTmp

Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Enterprise/MSBuild/Current/Bin/MSBuild.exe cmTC_5bb0f.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m && Microsoft (R) Build Engine version 16.11.1+3e40a09f8 for .NET Framework

Copyright (C) Microsoft Corporation. All rights reserved.



  Microsoft (R) C/C++ Optimizing Compiler Version 19.29.30136 for x64

  Copyright (C) Microsoft Corporation.  All rights reserved.

  src.cxx

  cl /c /Zi /W3 /WX- /diagnostics:column /MP /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D INET_FUNCTIONS_EXISTS_1 /D "CMAKE_INTDIR=\"Debug\"" /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_5bb0f.dir\Debug\\" /Fd"cmTC_5bb0f.dir\Debug\vc142.pdb" /external:W3 /Gd /TP /errorReport:queue C:\gh\Urho3D\_build\CMakeFiles\CMakeTmp\src.cxx

C:\gh\Urho3D\_build\CMakeFiles\CMakeTmp\src.cxx(2,10): fatal error C1083: Cannot open include file: 'sys/socket.h': No such file or directory [C:\gh\Urho3D\_build\CMakeFiles\CMakeTmp\cmTC_5bb0f.vcxproj]



Source file was:
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
int main() {
    struct sockaddr_in sa;
    char str[INET_ADDRSTRLEN];
    inet_pton(AF_INET, "192.0.2.33", &(sa.sin_addr));
    inet_ntop(AF_INET, &(sa.sin_addr), str, INET_ADDRSTRLEN);
}
Performing C++ SOURCE FILE Test COMPILER_HAS_DEPRECATED_ATTR failed with the following output:
Change Dir: C:/gh/Urho3D/_build/CMakeFiles/CMakeTmp

Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Enterprise/MSBuild/Current/Bin/MSBuild.exe cmTC_64fa9.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m && Microsoft (R) Build Engine version 16.11.1+3e40a09f8 for .NET Framework

Copyright (C) Microsoft Corporation. All rights reserved.



  Microsoft (R) C/C++ Optimizing Compiler Version 19.29.30136 for x64

  Copyright (C) Microsoft Corporation.  All rights reserved.

  src.cxx

  cl /c /Zi /W3 /WX- /diagnostics:column /MP /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D COMPILER_HAS_DEPRECATED_ATTR /D "CMAKE_INTDIR=\"Debug\"" /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_64fa9.dir\Debug\\" /Fd"cmTC_64fa9.dir\Debug\vc142.pdb" /external:W3 /Gd /TP /errorReport:queue  /bigobj C:\gh\Urho3D\_build\CMakeFiles\CMakeTmp\src.cxx

C:\gh\Urho3D\_build\CMakeFiles\CMakeTmp\src.cxx(1,16): error C2065: '__deprecated__': undeclared identifier [C:\gh\Urho3D\_build\CMakeFiles\CMakeTmp\cmTC_64fa9.vcxproj]

C:\gh\Urho3D\_build\CMakeFiles\CMakeTmp\src.cxx(1,31): error C4430: missing type specifier - int assumed. Note: C++ does not support default-int [C:\gh\Urho3D\_build\CMakeFiles\CMakeTmp\cmTC_64fa9.vcxproj]

C:\gh\Urho3D\_build\CMakeFiles\CMakeTmp\src.cxx(1,33): error C2062: type 'int' unexpected [C:\gh\Urho3D\_build\CMakeFiles\CMakeTmp\cmTC_64fa9.vcxproj]

C:\gh\Urho3D\_build\CMakeFiles\CMakeTmp\src.cxx(1,48): error C2143: syntax error: missing ';' before '{' [C:\gh\Urho3D\_build\CMakeFiles\CMakeTmp\cmTC_64fa9.vcxproj]

C:\gh\Urho3D\_build\CMakeFiles\CMakeTmp\src.cxx(1,48): error C2447: '{': missing function header (old-style formal list?) [C:\gh\Urho3D\_build\CMakeFiles\CMakeTmp\cmTC_64fa9.vcxproj]

C:\gh\Urho3D\_build\CMakeFiles\CMakeTmp\src.cxx(2,25): error C3861: 'somefunc': identifier not found [C:\gh\Urho3D\_build\CMakeFiles\CMakeTmp\cmTC_64fa9.vcxproj]



Source file was:
__attribute__((__deprecated__)) int somefunc() { return 0; }
    int main() { return somefunc();}

-------------------------

SirNate0 | 2021-12-04 14:14:53 UTC | #7

[quote="ToolmakerSteve, post:5, topic:7080"]
> Could NOT find Doxygen (missing: DOXYGEN_EXECUTABLE)

When is that needed?
[/quote]

Doxygen is used to build the documentation. If you don't need a local copy of it then you can ignore that.

I'm not sure about the other errors, but if it generated and built successfully I wouldn't worry about them.

-------------------------

JTippetts1 | 2021-12-06 22:46:59 UTC | #8

When CMake performs its configure step, it checks for the presence/absence of a large number of various capabilities. For many of the checks, it does this by attempting to compile/build a tiny program that uses that capability, and a failure of the test to build means that feature is not present or not supported. This is not a failure of your build process, it is just a failed check for that capability. Depending on your build platform and the presence or absence of various modules and installed tools, your project might generate many such failures. They are not meaningful to you, and do not mean that your project failed to build. All of those errors are logged to the error log, but you could pretty much live out your entire allotted span of days on this earth without caring even the slightest bit about what is actually in that error log, as long as the project itself tells you "Configuring done. Generating done."

Doxygen is an optional tool that is used to generate the automatic API docs. If you have no need of generating those you have no need of Doxygen, and it is not an error if it can't find it. The API docs are online and readily available, but if for some reason you can't or won't be online but still want access to the API documentation, you can install Doxygen and it will build a local copy of the docs for you.

-------------------------

