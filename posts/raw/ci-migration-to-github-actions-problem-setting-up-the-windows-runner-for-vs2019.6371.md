weitjong | 2020-09-06 15:59:45 UTC | #1

Anyone knows how to configure Github Actions workflow with the Windows runner to build Urho3D library with CMake and VS as generator? Basically I am looking for the equivalent of below from Appveyor.
```
  - if "%PLATFORM%" == "x64" (
      call "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvars64.bat" &&
      set "URHO3D_64BIT=1"
    ) else (
      call "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvars32.bat"
    )
```

I have tried setting up the PATH with this action before the build, but to no avail.
```
name: Setup msvc
uses: microsoft/setup-msbuild@v1.0.1
```

The CMake produced this error, which indicates to me the PATH is still not correct. I believe on Appveyor I would get the same error if one of the above *.bat file is not called first.

```
CMake suite maintained and supported by Kitware (kitware.com/cmake).
-- The C compiler identification is MSVC 19.27.29111.0
-- The CXX compiler identification is MSVC 19.27.29111.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - failed
-- Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio/2019/Enterprise/VC/Tools/MSVC/14.27.29110/bin/Hostx64/x64/cl.exe
-- Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio/2019/Enterprise/VC/Tools/MSVC/14.27.29110/bin/Hostx64/x64/cl.exe - broken
CMake Error at C:/Program Files/CMake/share/cmake-3.18/Modules/CMakeTestCCompiler.cmake:66 (message):
  The C compiler

    "C:/Program Files (x86)/Microsoft Visual Studio/2019/Enterprise/VC/Tools/MSVC/14.27.29110/bin/Hostx64/x64/cl.exe"

  is not able to compile a simple test program.

  It fails with the following output:

    Change Dir: D:/a/Urho3D/Urho3D/'build/ci'/CMakeFiles/CMakeTmp
    
    Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Enterprise/MSBuild/Current/Bin/MSBuild.exe cmTC_4c31c.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m && Microsoft (R) Build Engine version 16.7.0+b89cb5fde for .NET Framework
```

-------------------------

1vanK | 2020-09-07 00:18:37 UTC | #2

Path `D:/a/Urho3D/Urho3D/'build/ci'/CMakeFiles/CMakeTmp` very strange. Maybe this is the problem?

-------------------------

weitjong | 2020-09-07 00:23:03 UTC | #3

Indeed. Well spotted.

It was late last night and my eyes were blurry. And, I also hope I could get it done faster by collaborating.

I will check if changing the slash to backward one will solve the issue. Thanks.

-------------------------

1vanK | 2020-09-07 01:17:21 UTC | #4

I mean ' inside path. Windows should work correctly with /

-------------------------

weitjong | 2020-09-07 00:33:03 UTC | #5

I know what you meant. But I jump the conclusion a bit that why it ended up like that is due to wrong slash direction. Anyway, even this is not the root cause of my CMake configuration problem, the build tree path needs to be fixed.

-------------------------

weitjong | 2020-09-07 01:21:44 UTC | #6

The slash direction is fine. Both Ruby and CMake handle the forward slash correctly for all the platforms. The problem was caused by the single quote during parameter passing when invoking the *.bat file. What it needs is double quoting the path.
```
-  system "#{script} '#{build_tree}' #{build_options}" or abort
+  system %Q{#{script} "#{build_tree}" #{build_options}} or abort
```
The good news is, it also the root cause of my CMake configuration problem.

-------------------------

