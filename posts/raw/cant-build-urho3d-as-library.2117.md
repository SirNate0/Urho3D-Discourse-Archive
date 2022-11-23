Eugene | 2017-01-02 01:13:13 UTC | #1

I am trying to follow this tutorial.
[urho3d.github.io/documentation/H ... brary.html](http://urho3d.github.io/documentation/HEAD/_using_library.html)

and I am getting the following error:
[code]CMake Error at CMake/Modules/FindUrho3D.cmake:356 (message):
  Could NOT find compatible Urho3D library in Urho3D SDK installation or
  build tree.  Use URHO3D_HOME environment variable or build option to
  specify the location of the non-default SDK installation or build tree.
  Ensure the specified location contains the Urho3D library of the requested
  library type.  Change Dir:
  C:/Projects/tools/FlexEngine/build/CMakeFiles/CMakeTmp[/code]

I store source code of Urho in [b]C:/Projects/tools/Urho3D_source[/b] and CMake build dir is [b]C:/Projects/tools/Urho3D[/b]

I tried to set URHO3D_HOME CMake variable to second one and some other variants but it didn't help me.

Some time ago I successfully built Urho, but I can't reproduce my actions now.

Full log:
[spoiler][quote]The C compiler identification is MSVC 18.0.31101.0
The CXX compiler identification is MSVC 18.0.31101.0
Check for working C compiler using: Visual Studio 12 2013
Check for working C compiler using: Visual Studio 12 2013 -- works
Detecting C compiler ABI info
Detecting C compiler ABI info - done
Check for working CXX compiler using: Visual Studio 12 2013
Check for working CXX compiler using: Visual Studio 12 2013 -- works
Detecting CXX compiler ABI info
Detecting CXX compiler ABI info - done
Detecting CXX compile features
Detecting CXX compile features - done
CMake Warning at CMake/Modules/Urho3D-CMake-common.cmake:110 (message):
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
  CMakeLists.txt:27 (include)


Found Urho3D: C:/Projects/tools/Urho3D/lib/Urho3D_d.lib (found version "1.5-1031-gfd9db88")
Looking for C++ include d3dcompiler.h
Looking for C++ include d3dcompiler.h - found
Looking for C++ include d3d9.h
Looking for C++ include d3d9.h - found
Looking for C++ include d3d11.h
Looking for C++ include d3d11.h - found
Looking for C++ include ddraw.h
Looking for C++ include ddraw.h - found
Looking for C++ include dsound.h
Looking for C++ include dsound.h - found
Looking for C++ include dinput.h
Looking for C++ include dinput.h - found
Looking for C++ include dxgi.h
Looking for C++ include dxgi.h - found
Looking for C++ include xaudio2.h
Looking for C++ include xaudio2.h - found
Looking for include files windows.h, xinput.h
Looking for include files windows.h, xinput.h - found
Found DirectX: TRUE  found components:  D3D11 DInput DSound XAudio2 XInput 
Error copying file (if different) from "
C:/Projects/tools/FlexEngine/bin/Autoload" to "C:/Projects/tools/FlexEngine/build/bin/Autoload".

Error copying file (if different) from "
C:/Projects/tools/FlexEngine/bin/CoreData" to "C:/Projects/tools/FlexEngine/build/bin/CoreData".

Error copying file (if different) from "
C:/Projects/tools/FlexEngine/bin/Data" to "C:/Projects/tools/FlexEngine/build/bin/Data".

CMake Error at CMake/Modules/FindUrho3D.cmake:356 (message):
  Could NOT find compatible Urho3D library in Urho3D SDK installation or
  build tree.  Use URHO3D_HOME environment variable or build option to
  specify the location of the non-default SDK installation or build tree.
  Ensure the specified location contains the Urho3D library of the requested
  library type.  Change Dir:
  C:/Projects/tools/FlexEngine/build/CMakeFiles/CMakeTmp

  

  Run Build Command:"C:/Program Files (x86)/MSBuild/12.0/bin/MSBuild.exe"
  "cmTC_2bc1c.vcxproj" "/p:Configuration=Release"
  "/p:VisualStudioVersion=12.0"

  Microsoft (R) Build Engine version 12.0.31101.0


  [Microsoft .NET Framework, version 4.0.30319.42000]


  Copyright (C) Microsoft Corporation.  All rights reserved.


  


  Build started 13.07.2016 14:10:41.


  Project
  "C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj"
  on node 1 (default targets).


  PrepareForBuild:


    Creating directory "cmTC_2bc1c.dir\Release\".

    Creating directory "C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\Release\".

    Creating directory "cmTC_2bc1c.dir\Release\cmTC_2bc1c.tlog\".


  InitializeBuildStatus:


    Creating "cmTC_2bc1c.dir\Release\cmTC_2bc1c.tlog\unsuccessfulbuild" because "AlwaysCreate" was specified.


  ClCompile:


    C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\CL.exe /c /IC:\Projects\tools\Urho3D\include /W3 /WX- /O2 /Ob2 /Oy- /D WIN32 /D _WINDOWS /D NDEBUG /D "CMAKE_INTDIR=\"Release\"" /D _MBCS /Gm- /EHsc /MT /GS /fp:precise /Zc:wchar_t /Zc:forScope /GR /Fo"cmTC_2bc1c.dir\Release\\" /Fd"cmTC_2bc1c.dir\Release\vc120.pdb" /Gd /TP /analyze- /errorReport:queue C:\Projects\tools\FlexEngine\CMake\Modules\CheckUrho3DLibrary.cpp

    Microsoft (R) C/C++ Optimizing Compiler Version 18.00.31101 for x86

    Copyright (C) Microsoft Corporation.  All rights reserved.

    

    cl /c /IC:\Projects\tools\Urho3D\include /W3 /WX- /O2 /Ob2 /Oy- /D WIN32 /D _WINDOWS /D NDEBUG /D "CMAKE_INTDIR=\"Release\"" /D _MBCS /Gm- /EHsc /MT /GS /fp:precise /Zc:wchar_t /Zc:forScope /GR /Fo"cmTC_2bc1c.dir\Release\\" /Fd"cmTC_2bc1c.dir\Release\vc120.pdb" /Gd /TP /analyze- /errorReport:queue C:\Projects\tools\FlexEngine\CMake\Modules\CheckUrho3DLibrary.cpp

    

    CheckUrho3DLibrary.cpp


  Link:


    C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\link.exe /ERRORREPORT:QUEUE /OUT:"C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\Release\cmTC_2bc1c.exe" /INCREMENTAL:NO /NOLOGO kernel32.lib user32.lib gdi32.lib winspool.lib shell32.lib ole32.lib oleaut32.lib uuid.lib comdlg32.lib advapi32.lib C:\Projects\tools\Urho3D\lib\Urho3D_d.lib /MANIFEST /MANIFESTUAC:"level='asInvoker' uiAccess='false'" /manifest:embed /PDB:"C:/Projects/tools/FlexEngine/build/CMakeFiles/CMakeTmp/Release/cmTC_2bc1c.pdb" /SUBSYSTEM:CONSOLE /TLBID:1 /DYNAMICBASE /NXCOMPAT /IMPLIB:"C:/Projects/tools/FlexEngine/build/CMakeFiles/CMakeTmp/Release/cmTC_2bc1c.lib" /MACHINE:X86 /SAFESEH  /machine:X86 cmTC_2bc1c.dir\Release\CheckUrho3DLibrary.obj


  Urho3D_d.lib(DataDeserializer.obj) : error LNK2038: mismatch detected for
  '_ITERATOR_DEBUG_LEVEL': value '2' doesn't match value '0' in
  CheckUrho3DLibrary.obj
  [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]



  Urho3D_d.lib(DataDeserializer.obj) : error LNK2038: mismatch detected for
  'RuntimeLibrary': value 'MDd_DynamicDebug' doesn't match value
  'MT_StaticRelease' in CheckUrho3DLibrary.obj
  [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]



  Urho3D_d.lib(LibraryInfo.obj) : error LNK2038: mismatch detected for
  '_ITERATOR_DEBUG_LEVEL': value '2' doesn't match value '0' in
  CheckUrho3DLibrary.obj
  [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]



  Urho3D_d.lib(LibraryInfo.obj) : error LNK2038: mismatch detected for
  'RuntimeLibrary': value 'MDd_DynamicDebug' doesn't match value
  'MT_StaticRelease' in CheckUrho3DLibrary.obj
  [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]



  Urho3D_d.lib(SerializedDataIterator.obj) : error LNK2038: mismatch detected
  for '_ITERATOR_DEBUG_LEVEL': value '2' doesn't match value '0' in
  CheckUrho3DLibrary.obj
  [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]



  Urho3D_d.lib(SerializedDataIterator.obj) : error LNK2038: mismatch detected
  for 'RuntimeLibrary': value 'MDd_DynamicDebug' doesn't match value
  'MT_StaticRelease' in CheckUrho3DLibrary.obj
  [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]



  Urho3D_d.lib(Precompiled.obj) : error LNK2038: mismatch detected for
  '_ITERATOR_DEBUG_LEVEL': value '2' doesn't match value '0' in
  CheckUrho3DLibrary.obj
  [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]



  Urho3D_d.lib(Precompiled.obj) : error LNK2038: mismatch detected for
  'RuntimeLibrary': value 'MDd_DynamicDebug' doesn't match value
  'MT_StaticRelease' in CheckUrho3DLibrary.obj
  [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]



  msvcprtd.lib(MSVCP120D.dll) : error LNK2005: "void __cdecl
  std::_Xbad_alloc(void)" (?_Xbad_alloc@std@@YAXXZ) already defined in
  libcpmt.lib(xthrow.obj)
  [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]



  msvcprtd.lib(MSVCP120D.dll) : error LNK2005: "void __cdecl
  std::_Xlength_error(char const *)" (?_Xlength_error@std@@YAXPBD@Z) already
  defined in libcpmt.lib(xthrow.obj)
  [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]



  msvcprtd.lib(MSVCP120D.dll) : error LNK2005: "void __cdecl
  std::_Xout_of_range(char const *)" (?_Xout_of_range@std@@YAXPBD@Z) already
  defined in libcpmt.lib(xthrow.obj)
  [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]



  msvcprtd.lib(MSVCP120D.dll) : error LNK2005: "public: __thiscall
  std::locale::id::id(unsigned int)" (??0id@locale@std@@QAE@I@Z) already
  defined in libcpmt.lib(xthrow.obj)
  [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]



  msvcprtd.lib(MSVCP120D.dll) : error LNK2005: "char const * __cdecl
  std::_Syserror_map(int)" (?_Syserror_map@std@@YAPBDH@Z) already defined in
  libcpmt.lib(syserror.obj)
  [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]



  msvcprtd.lib(MSVCP120D.dll) : error LNK2005: "char const * __cdecl
  std::_Winerror_map(int)" (?_Winerror_map@std@@YAPBDH@Z) already defined in
  libcpmt.lib(syserror.obj)
  [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]



  msvcprtd.lib(MSVCP120D.dll) : error LNK2005: "public: __thiscall
  std::_Lockit::_Lockit(int)" (??0_Lockit@std@@QAE@H@Z) already defined in
  libcpmt.lib(xlock.obj)
  [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]



  msvcprtd.lib(MSVCP120D.dll) : error LNK2005: "public: __thiscall
  std::_Lockit::~_Lockit(void)" (??1_Lockit@std@@QAE@XZ) already defined in
  libcpmt.lib(xlock.obj)
  [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]



  MSVCRTD.lib(MSVCR120D.dll) : error LNK2005: __invalid_parameter already
  defined in LIBCMT.lib(invarg.obj)
  [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]



  MSVCRTD.lib(MSVCR120D.dll) : error LNK2005: _memmove already defined in
  LIBCMT.lib(memmove.obj)
  [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]



  MSVCRTD.lib(MSVCR120D.dll) : error LNK2005: __hypot already defined in
  LIBCMT.lib(hypot.obj)
  [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]



  MSVCRTD.lib(MSVCR120D.dll) : error LNK2005: "public: __thiscall
  std::exception::exception(void)" (??0exception@std@@QAE@XZ) already defined
  in LIBCMT.lib(stdexcpt.obj)
  [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]



  MSVCRTD.lib(MSVCR120D.dll) : error LNK2005: "public: __thiscall
  std::exception::exception(class std::exception const &)"
  (??0exception@std@@QAE@ABV01@@Z) already defined in
  LIBCMT.lib(stdexcpt.obj)
  [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]



  MSVCRTD.lib(MSVCR120D.dll) : error LNK2005: "public: virtual __thiscall
  std::exception::~exception(void)" (??1exception@std@@UAE@XZ) already
  defined in LIBCMT.lib(stdexcpt.obj)
  [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]



  MSVCRTD.lib(ti_inst.obj) : error LNK2005: "private: __thiscall
  type_info::type_info(class type_info const &)" (??0type_info@@AAE@ABV0@@Z)
  already defined in LIBCMT.lib(typinfo.obj)
  [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]



  MSVCRTD.lib(ti_inst.obj) : error LNK2005: "private: class type_info &
  __thiscall type_info::operator=(class type_info const &)"
  (??4type_info@@AAEAAV0@ABV0@@Z) already defined in LIBCMT.lib(typinfo.obj)
  [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]



  LINK : warning LNK4098: defaultlib 'MSVCRTD' conflicts with use of other
  libs; use /NODEFAULTLIB:library
  [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]



  
  C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\Release\cmTC_2bc1c.exe
  : fatal error LNK1169: one or more multiply defined symbols found
  [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]



  Done Building Project
  "C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj"
  (default targets) -- FAILED.


  


  Build FAILED.


  


  
  "C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj"
  (default target) (1) ->


  (Link target) -> 


    LINK : warning LNK4098: defaultlib 'MSVCRTD' conflicts with use of other libs; use /NODEFAULTLIB:library [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]


  


  


  
  "C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj"
  (default target) (1) ->


  (Link target) -> 


    Urho3D_d.lib(DataDeserializer.obj) : error LNK2038: mismatch detected for '_ITERATOR_DEBUG_LEVEL': value '2' doesn't match value '0' in CheckUrho3DLibrary.obj [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]

    Urho3D_d.lib(DataDeserializer.obj) : error LNK2038: mismatch detected for 'RuntimeLibrary': value 'MDd_DynamicDebug' doesn't match value 'MT_StaticRelease' in CheckUrho3DLibrary.obj [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]

    Urho3D_d.lib(LibraryInfo.obj) : error LNK2038: mismatch detected for '_ITERATOR_DEBUG_LEVEL': value '2' doesn't match value '0' in CheckUrho3DLibrary.obj [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]

    Urho3D_d.lib(LibraryInfo.obj) : error LNK2038: mismatch detected for 'RuntimeLibrary': value 'MDd_DynamicDebug' doesn't match value 'MT_StaticRelease' in CheckUrho3DLibrary.obj [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]

    Urho3D_d.lib(SerializedDataIterator.obj) : error LNK2038: mismatch detected for '_ITERATOR_DEBUG_LEVEL': value '2' doesn't match value '0' in CheckUrho3DLibrary.obj [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]

    Urho3D_d.lib(SerializedDataIterator.obj) : error LNK2038: mismatch detected for 'RuntimeLibrary': value 'MDd_DynamicDebug' doesn't match value 'MT_StaticRelease' in CheckUrho3DLibrary.obj [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]

    Urho3D_d.lib(Precompiled.obj) : error LNK2038: mismatch detected for '_ITERATOR_DEBUG_LEVEL': value '2' doesn't match value '0' in CheckUrho3DLibrary.obj [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]

    Urho3D_d.lib(Precompiled.obj) : error LNK2038: mismatch detected for 'RuntimeLibrary': value 'MDd_DynamicDebug' doesn't match value 'MT_StaticRelease' in CheckUrho3DLibrary.obj [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]

    msvcprtd.lib(MSVCP120D.dll) : error LNK2005: "void __cdecl std::_Xbad_alloc(void)" (?_Xbad_alloc@std@@YAXXZ) already defined in libcpmt.lib(xthrow.obj) [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]

    msvcprtd.lib(MSVCP120D.dll) : error LNK2005: "void __cdecl std::_Xlength_error(char const *)" (?_Xlength_error@std@@YAXPBD@Z) already defined in libcpmt.lib(xthrow.obj) [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]

    msvcprtd.lib(MSVCP120D.dll) : error LNK2005: "void __cdecl std::_Xout_of_range(char const *)" (?_Xout_of_range@std@@YAXPBD@Z) already defined in libcpmt.lib(xthrow.obj) [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]

    msvcprtd.lib(MSVCP120D.dll) : error LNK2005: "public: __thiscall std::locale::id::id(unsigned int)" (??0id@locale@std@@QAE@I@Z) already defined in libcpmt.lib(xthrow.obj) [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]

    msvcprtd.lib(MSVCP120D.dll) : error LNK2005: "char const * __cdecl std::_Syserror_map(int)" (?_Syserror_map@std@@YAPBDH@Z) already defined in libcpmt.lib(syserror.obj) [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]

    msvcprtd.lib(MSVCP120D.dll) : error LNK2005: "char const * __cdecl std::_Winerror_map(int)" (?_Winerror_map@std@@YAPBDH@Z) already defined in libcpmt.lib(syserror.obj) [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]

    msvcprtd.lib(MSVCP120D.dll) : error LNK2005: "public: __thiscall std::_Lockit::_Lockit(int)" (??0_Lockit@std@@QAE@H@Z) already defined in libcpmt.lib(xlock.obj) [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]

    msvcprtd.lib(MSVCP120D.dll) : error LNK2005: "public: __thiscall std::_Lockit::~_Lockit(void)" (??1_Lockit@std@@QAE@XZ) already defined in libcpmt.lib(xlock.obj) [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]

    MSVCRTD.lib(MSVCR120D.dll) : error LNK2005: __invalid_parameter already defined in LIBCMT.lib(invarg.obj) [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]

    MSVCRTD.lib(MSVCR120D.dll) : error LNK2005: _memmove already defined in LIBCMT.lib(memmove.obj) [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]

    MSVCRTD.lib(MSVCR120D.dll) : error LNK2005: __hypot already defined in LIBCMT.lib(hypot.obj) [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]

    MSVCRTD.lib(MSVCR120D.dll) : error LNK2005: "public: __thiscall std::exception::exception(void)" (??0exception@std@@QAE@XZ) already defined in LIBCMT.lib(stdexcpt.obj) [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]

    MSVCRTD.lib(MSVCR120D.dll) : error LNK2005: "public: __thiscall std::exception::exception(class std::exception const &)" (??0exception@std@@QAE@ABV01@@Z) already defined in LIBCMT.lib(stdexcpt.obj) [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]

    MSVCRTD.lib(MSVCR120D.dll) : error LNK2005: "public: virtual __thiscall std::exception::~exception(void)" (??1exception@std@@UAE@XZ) already defined in LIBCMT.lib(stdexcpt.obj) [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]

    MSVCRTD.lib(ti_inst.obj) : error LNK2005: "private: __thiscall type_info::type_info(class type_info const &)" (??0type_info@@AAE@ABV0@@Z) already defined in LIBCMT.lib(typinfo.obj) [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]

    MSVCRTD.lib(ti_inst.obj) : error LNK2005: "private: class type_info & __thiscall type_info::operator=(class type_info const &)" (??4type_info@@AAEAAV0@ABV0@@Z) already defined in LIBCMT.lib(typinfo.obj) [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]

    C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\Release\cmTC_2bc1c.exe : fatal error LNK1169: one or more multiply defined symbols found [C:\Projects\tools\FlexEngine\build\CMakeFiles\CMakeTmp\cmTC_2bc1c.vcxproj]


  


      1 Warning(s)

      25 Error(s)


  


  Time Elapsed 00:00:00.74


Call Stack (most recent call first):
  CMakeLists.txt:30 (find_package)


Configuring incomplete, errors occurred!
See also "C:/Projects/tools/FlexEngine/build/CMakeFiles/CMakeOutput.log".[/quote][/spoiler]

-------------------------

weitjong | 2017-01-02 01:13:13 UTC | #2

You should not used document link for release 1.31 with the codebase from latest master branch (assuming that is what you were using). The URHO3D_HOME should point to a build tree. So, in your case it is the second path, if that path is what you claimed it is. Make sure a compatible library has been built in the build tree in question. If you have done this and still could not pass this check, read the error messages carefully. It usually provide enough information why it failed the test. Good luck.

-------------------------

Eugene | 2017-01-02 01:13:13 UTC | #3

I posted wrong link.
It looks like usage of Urho as library has changed after I wrote my CMakeLists.txt - e.g. [b]find_package[/b] disappeared.
So my CMakeLists.txt got out-of-dated and when I tried to re-configure it on clean PC I got these strange errors.

-------------------------

weitjong | 2017-01-02 01:13:13 UTC | #4

Well, a lot have changed in our build system for the good or the bad, depends on your point of view. The find_package(URHO3D) is gone now as it is performed automatically inside the Urho3D common module. That is what you can see on the surface. Behind the scene, the modules now auto-discovers all the critical CMake variables in your project based on how the Urho3D library was being built. Of course, it needs to find a compatible Urho3D library in the first place. It is considered compatible when the module could actually build a simple test program linking to the candidate library that it found. If it failed in doing so then it means something is terribly wrong and it gives the error message as you see now. In the past, the module just blindly returned library that it found without checking. And if the found library is indeed not compatible then you will got the compilation error anyway later when you try to build your project. That is, the basic idea of the changes is to give the error up front.

-------------------------

