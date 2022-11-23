mldevs | 2018-04-07 15:35:21 UTC | #1

I've been having this error for the past few hours, and I cannot figure out why. I have linked everything correctly, I found a pre-made project for CodeBlocks to do the linking, still I get the following errors.

> ||=== Build: Debug in testing (compiler: MinGW-w64) ===|
> obj\Debug\testing.o||In function `_tcf_2': |
> F:\URHO3D\include\Urho3D\Engine\Application.h|37|undefined reference to `Urho3D::TypeInfo::~TypeInfo()'|
> obj\Debug\testing.o||In function `_tcf_3': |
> C:\Users\Matthew\Desktop\BASEFILEHORDE\testing\testing.h|7|undefined reference to `Urho3D::TypeInfo::~TypeInfo()'|
> obj\Debug\testing.o||In function `ZN7testingC2EPN6Urho3D7ContextE': |
> C:\Users\Matthew\Desktop\BASEFILEHORDE\testing\testing.cpp|9|undefined reference to `Urho3D::Application::Application(Urho3D::Context*)'|
> obj\Debug\testing.o||In function `ZN7testing5SetupEv': |
> C:\Users\Matthew\Desktop\BASEFILEHORDE\testing\testing.cpp|15|undefined reference to `Urho3D::StringHash::StringHash(char const*)'|
> C:\Users\Matthew\Desktop\BASEFILEHORDE\testing\testing.cpp|16|undefined reference to `Urho3D::StringHash::StringHash(char const*)'|
> obj\Debug\testing.o||In function `ZN7testing5StartEv': |
> C:\Users\Matthew\Desktop\BASEFILEHORDE\testing\testing.cpp|21|undefined reference to `Urho3D::Object::SubscribeToEvent(Urho3D::StringHash, Urho3D::EventHandler*)'|
> obj\Debug\testing.o||In function `ZN7testing13HandleKeyDownEN6Urho3D10StringHashERNS0_7HashMapIS1_NS0_7VariantEEE': |
> C:\Users\Matthew\Desktop\BASEFILEHORDE\testing\testing.cpp|34|undefined reference to `Urho3D::Engine::Exit()'|
> obj\Debug\testing.o||In function `Z14RunApplicationv': |
> C:\Users\Matthew\Desktop\BASEFILEHORDE\testing\testing.cpp|38|undefined reference to `Urho3D::Context::Context()'|
> C:\Users\Matthew\Desktop\BASEFILEHORDE\testing\testing.cpp|38|undefined reference to `Urho3D::Application::Run()'|
> obj\Debug\testing.o||In function `WinMain@16': |
> C:\Users\Matthew\Desktop\BASEFILEHORDE\testing\testing.cpp|38|undefined reference to `Urho3D::ParseArguments(wchar_t const*)'|
> obj\Debug\testing.o||In function `_static_initialization_and_destruction_0': |
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|36|undefined reference to `Urho3D::EventNameRegistrar::RegisterEventName(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|38|undefined reference to `Urho3D::StringHash::StringHash(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|39|undefined reference to `Urho3D::StringHash::StringHash(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|40|undefined reference to `Urho3D::StringHash::StringHash(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|44|undefined reference to `Urho3D::EventNameRegistrar::RegisterEventName(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|46|undefined reference to `Urho3D::StringHash::StringHash(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|47|undefined reference to `Urho3D::StringHash::StringHash(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|48|undefined reference to `Urho3D::StringHash::StringHash(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|52|undefined reference to `Urho3D::EventNameRegistrar::RegisterEventName(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|54|undefined reference to `Urho3D::StringHash::StringHash(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|55|undefined reference to `Urho3D::StringHash::StringHash(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|56|undefined reference to `Urho3D::StringHash::StringHash(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|57|undefined reference to `Urho3D::StringHash::StringHash(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|58|undefined reference to `Urho3D::StringHash::StringHash(char const*)'|
> obj\Debug\testing.o:F:\URHO3D\include\Urho3D\Input\InputEvents.h|59|more undefined references to `Urho3D::StringHash::StringHash(char const*)' follow|
> obj\Debug\testing.o||In function `_static_initialization_and_destruction_0': |
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|63|undefined reference to `Urho3D::EventNameRegistrar::RegisterEventName(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|65|undefined reference to `Urho3D::StringHash::StringHash(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|66|undefined reference to `Urho3D::StringHash::StringHash(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|67|undefined reference to `Urho3D::StringHash::StringHash(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|71|undefined reference to `Urho3D::EventNameRegistrar::RegisterEventName(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|73|undefined reference to `Urho3D::StringHash::StringHash(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|74|undefined reference to `Urho3D::StringHash::StringHash(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|75|undefined reference to `Urho3D::StringHash::StringHash(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|76|undefined reference to `Urho3D::StringHash::StringHash(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|77|undefined reference to `Urho3D::StringHash::StringHash(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|81|undefined reference to `Urho3D::EventNameRegistrar::RegisterEventName(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|83|undefined reference to `Urho3D::StringHash::StringHash(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|84|undefined reference to `Urho3D::StringHash::StringHash(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|85|undefined reference to `Urho3D::StringHash::StringHash(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|86|undefined reference to `Urho3D::StringHash::StringHash(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|90|undefined reference to `Urho3D::EventNameRegistrar::RegisterEventName(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|92|undefined reference to `Urho3D::StringHash::StringHash(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|96|undefined reference to `Urho3D::EventNameRegistrar::RegisterEventName(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|98|undefined reference to `Urho3D::StringHash::StringHash(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|99|undefined reference to `Urho3D::StringHash::StringHash(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|100|undefined reference to `Urho3D::StringHash::StringHash(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|104|undefined reference to `Urho3D::EventNameRegistrar::RegisterEventName(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|106|undefined reference to `Urho3D::StringHash::StringHash(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|110|undefined reference to `Urho3D::EventNameRegistrar::RegisterEventName(char const*)'|
> F:\URHO3D\include\Urho3D\Input\InputEvents.h|112|undefined reference to `Urho3D::StringHash::StringHash(char const*)'|
> ||More errors follow but not being shown.|
> ||Edit the max errors limit in compiler options...|
> ||=== Build failed: 50 error(s), 0 warning(s) (0 minute(s), 0 second(s)) ===|

I compiled from CMake without errors, and i used the precompiled download as well. The errors especially do not make sense because when I hand type in one of the functions, such as `Urho3D::TypeInfo::~TypeInfo()` the recommended objects appear, as the list format that CodeBlocks does.
Any help would be greatly appreciated
Thank you and have a nice day.

-------------------------

Eugene | 2018-03-28 18:28:33 UTC | #2

Do you generate project via CMake from scratch?
Is it an error when you link Urho or when you link your project with Urho?
Do you use shared library version (Urho3D.dll)?

-------------------------

S.L.C | 2018-03-28 18:29:49 UTC | #3

If you're building a static library then you should probably include `URHO3D_STATIC_DEFINE` somewhere in your defines.

-------------------------

mldevs | 2018-03-28 18:31:25 UTC | #4

I compiled from source, I got the same error the error here is from the pre-compiled static download,
Its an error when I build  the project
This specific error is from static

-------------------------

mldevs | 2018-03-28 18:32:16 UTC | #5

It is in the project defines,
    WIN32
    _WINDOWS
    URHO3D_SSE
    URHO3D_FILEWATCHER
    URHO3D_PROFILING
    URHO3D_LOGGING
    URHO3D_ANGELSCRIPT
    URHO3D_STATIC_DEFINE

-------------------------

Eugene | 2018-03-28 18:35:11 UTC | #6

What's your CMake file?

-------------------------

mldevs | 2018-03-28 18:38:45 UTC | #7

CMake has nothing to do with this, I'm not building my project with CMake, I'm using the standard CodeBlocks build system, mingw32-make.exe. The error persists from linking my project file to the directory of the pre-compiled files, and linking it to my built from source files. CMake is irrelevant in this regard.

-------------------------

mldevs | 2018-03-28 18:41:41 UTC | #8

Downloaded from here:
[https://sourceforge.net/projects/urho3d/files/Urho3D/](https://discourse.urho3d.io/t/urho3d-codeblocks-wizard/1379)

(Also built them from source earlier, but still with the same error)

Project File from:
[https://discourse.urho3d.io/t/urho3d-codeblocks-wizard/1379](https://discourse.urho3d.io/t/urho3d-codeblocks-wizard/1379)

(Also done earlier by linking my own project in the same fashion as the setup wizard)

-------------------------

Eugene | 2018-03-28 18:46:20 UTC | #9

[quote="mldevs, post:7, topic:4132"]
CMake has nothing to do with this, I’m not building my project with CMake, I’m using the standard CodeBlocks build system, mingw32-make.exe
[/quote]

There's guideline how to use Urho as library in your own project, and it's written for CMake project.
This way is maintained by Urho developers and recommended for general usage.

If you use some 3rd-party plugin to make the project file for some specific IDE...
it seems that Urho isn't linked at all, and only author of the plugin may answer your question.

-------------------------

mldevs | 2018-03-28 18:56:48 UTC | #10

Except it is linked the exact same way I linked it myself. Once again it is not a linking error.
I haven't used CMake because it has a 98% fail rate for me, always an issue with the  compilers, even then there always errors with files, so I tend not to use it

-------------------------

mldevs | 2018-03-28 19:33:32 UTC | #11

I've been trying for the past half hour, following the steps on the website, and I continue to get the following error:
> CMake Deprecation Warning at CMakeLists.txt:22 (cmake_policy):
>   The OLD behavior for policy CMP0026 will be removed from a future version
>   of CMake.
> 
>   The cmake-policies(7) manual explains that the OLD behaviors of all
>   policies are deprecated and that a policy should be set to OLD only under
>   specific short-term circumstances.  Projects should be ported to the NEW
>   behavior and not rely on setting a policy to OLD.
> 
> 
> CMake Error at CMake/Modules/FindUrho3D.cmake:346 (message):
>   Could NOT find compatible Urho3D library in Urho3D SDK installation or
>   build tree.  Use URHO3D_HOME environment variable or build option to
>   specify the location of the non-default SDK installation or build tree.
> Call Stack (most recent call first):
>   CMake/Modules/UrhoCommon.cmake:231 (find_package)
>   CMakeLists.txt:30 (include)
> 
> 
> Configuring incomplete, errors occurred!
> See also "F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeOutput.log".

-------------------------

mldevs | 2018-03-28 19:37:01 UTC | #12

In CMakeOutput.log:

> The system is: Windows - 6.1.7601 - AMD64
> Compiling the C compiler identification source file "CMakeCCompilerId.c" succeeded.
> Compiler: C:/MinGW/bin/mingw32-gcc.exe 
> Build flags: 
> Id flags:  
> 
> The output was:
> 0
> 
> 
> Compilation of the C compiler identification source "CMakeCCompilerId.c" produced "a.exe"
> 
> The C compiler identification is GNU, found in "F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/3.11.0-rc3/CompilerIdC/a.exe"
> 
> Compiling the CXX compiler identification source file "CMakeCXXCompilerId.cpp" succeeded.
> Compiler: C:/MinGW/bin/mingw32-g++.exe 
> Build flags: 
> Id flags:  
> 
> The output was:
> 0
> 
> 
> Compilation of the CXX compiler identification source "CMakeCXXCompilerId.cpp" produced "a.exe"
> 
> The CXX compiler identification is GNU, found in "F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/3.11.0-rc3/CompilerIdCXX/a.exe"
> 
> Determining if the C compiler works passed with the following output:
> Change Dir: F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp
> 
> Run Build Command:"C:/MinGW/bin/mingw32-make.exe" "cmTC_a7e1a/fast"
> C:/MinGW/bin/mingw32-make.exe -f CMakeFiles\cmTC_a7e1a.dir\build.make CMakeFiles/cmTC_a7e1a.dir/build
> 
> mingw32-make.exe[1]: Entering directory 'F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp'
> 
> Building C object CMakeFiles/cmTC_a7e1a.dir/testCCompiler.c.obj
> 
> C:\MinGW\bin\mingw32-gcc.exe    -o CMakeFiles\cmTC_a7e1a.dir\testCCompiler.c.obj   -c F:\URHOTEMPLATEPROJECTMAYBEv2\CMakeFiles\CMakeTmp\testCCompiler.c
> 
> Linking C executable cmTC_a7e1a.exe
> 
> "C:\Program Files\CMake\bin\cmake.exe" -E cmake_link_script CMakeFiles\cmTC_a7e1a.dir\link.txt --verbose=1
> 
> "C:\Program Files\CMake\bin\cmake.exe" -E remove -f CMakeFiles\cmTC_a7e1a.dir/objects.a
> C:\MinGW\bin\ar.exe cr CMakeFiles\cmTC_a7e1a.dir/objects.a @CMakeFiles\cmTC_a7e1a.dir\objects1.rsp
> C:\MinGW\bin\mingw32-gcc.exe      -Wl,--whole-archive CMakeFiles\cmTC_a7e1a.dir/objects.a -Wl,--no-whole-archive  -o cmTC_a7e1a.exe -Wl,--out-implib,libcmTC_a7e1a.dll.a -Wl,--major-image-version,0,--minor-image-version,0 @CMakeFiles\cmTC_a7e1a.dir\linklibs.rsp
> mingw32-make.exe[1]: Leaving directory 'F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp'
> 
> 
> 
> Detecting C compiler ABI info compiled with the following output:
> Change Dir: F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp
> 
> Run Build Command:"C:/MinGW/bin/mingw32-make.exe" "cmTC_ea432/fast"
> C:/MinGW/bin/mingw32-make.exe -f CMakeFiles\cmTC_ea432.dir\build.make CMakeFiles/cmTC_ea432.dir/build
> 
> mingw32-make.exe[1]: Entering directory 'F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp'
> 
> Building C object CMakeFiles/cmTC_ea432.dir/CMakeCCompilerABI.c.obj
> 
> C:\MinGW\bin\mingw32-gcc.exe    -o CMakeFiles\cmTC_ea432.dir\CMakeCCompilerABI.c.obj   -c "C:\Program Files\CMake\share\cmake-3.11\Modules\CMakeCCompilerABI.c"
> 
> Linking C executable cmTC_ea432.exe
> 
> "C:\Program Files\CMake\bin\cmake.exe" -E cmake_link_script CMakeFiles\cmTC_ea432.dir\link.txt --verbose=1
> 
> "C:\Program Files\CMake\bin\cmake.exe" -E remove -f CMakeFiles\cmTC_ea432.dir/objects.a
> C:\MinGW\bin\ar.exe cr CMakeFiles\cmTC_ea432.dir/objects.a @CMakeFiles\cmTC_ea432.dir\objects1.rsp
> C:\MinGW\bin\mingw32-gcc.exe     -v -Wl,--whole-archive CMakeFiles\cmTC_ea432.dir/objects.a -Wl,--no-whole-archive  -o cmTC_ea432.exe -Wl,--out-implib,libcmTC_ea432.dll.a -Wl,--major-image-version,0,--minor-image-version,0 
> Using built-in specs.
> 
> COLLECT_GCC=C:\MinGW\bin\mingw32-gcc.exe
> 
> COLLECT_LTO_WRAPPER=c:/mingw/bin/../libexec/gcc/mingw32/6.3.0/lto-wrapper.exe
> 
> Target: mingw32
> 
> Configured with: ../src/gcc-6.3.0/configure --build=x86_64-pc-linux-gnu --host=mingw32 --target=mingw32 --with-gmp=/mingw --with-mpfr --with-mpc=/mingw --with-isl=/mingw --prefix=/mingw --disable-win32-registry --with-arch=i586 --with-tune=generic --enable-languages=c,c++,objc,obj-c++,fortran,ada --with-pkgversion='MinGW.org GCC-6.3.0-1' --enable-static --enable-shared --enable-threads --with-dwarf2 --disable-sjlj-exceptions --enable-version-specific-runtime-libs --with-libiconv-prefix=/mingw --with-libintl-prefix=/mingw --enable-libstdcxx-debug --enable-libgomp --disable-libvtv --enable-nls
> 
> Thread model: win32
> 
> gcc version 6.3.0 (MinGW.org GCC-6.3.0-1) 
> 
> COMPILER_PATH=c:/mingw/bin/../libexec/gcc/mingw32/6.3.0/;c:/mingw/bin/../libexec/gcc/;c:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../../../mingw32/bin/
> 
> LIBRARY_PATH=c:/mingw/bin/../lib/gcc/mingw32/6.3.0/;c:/mingw/bin/../lib/gcc/;c:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../../../mingw32/lib/;c:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../../
> 
> COLLECT_GCC_OPTIONS='-v' '-o' 'cmTC_ea432.exe' '-mtune=generic' '-march=i586'
> 
>  c:/mingw/bin/../libexec/gcc/mingw32/6.3.0/collect2.exe -plugin c:/mingw/bin/../libexec/gcc/mingw32/6.3.0/liblto_plugin-0.dll -plugin-opt=c:/mingw/bin/../libexec/gcc/mingw32/6.3.0/lto-wrapper.exe -plugin-opt=-fresolution=C:\Users\Matthew\AppData\Local\Temp\ccZcMt4f.res -plugin-opt=-pass-through=-lmingw32 -plugin-opt=-pass-through=-lgcc -plugin-opt=-pass-through=-lgcc_eh -plugin-opt=-pass-through=-lmoldname -plugin-opt=-pass-through=-lmingwex -plugin-opt=-pass-through=-lmsvcrt -plugin-opt=-pass-through=-ladvapi32 -plugin-opt=-pass-through=-lshell32 -plugin-opt=-pass-through=-luser32 -plugin-opt=-pass-through=-lkernel32 -plugin-opt=-pass-through=-lmingw32 -plugin-opt=-pass-through=-lgcc -plugin-opt=-pass-through=-lgcc_eh -plugin-opt=-pass-through=-lmoldname -plugin-opt=-pass-through=-lmingwex -plugin-opt=-pass-through=-lmsvcrt -Bdynamic -o cmTC_ea432.exe c:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../../crt2.o c:/mingw/bin/../lib/gcc/mingw32/6.3.0/crtbegin.o -Lc:/mingw/bin/../lib/gcc/mingw32/6.3.0 -Lc:/mingw/bin/../lib/gcc -Lc:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../../../mingw32/lib -Lc:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../.. --whole-archive CMakeFiles\cmTC_ea432.dir/objects.a --no-whole-archive --out-implib libcmTC_ea432.dll.a --major-image-version 0 --minor-image-version 0 -lmingw32 -lgcc -lgcc_eh -lmoldname -lmingwex -lmsvcrt -ladvapi32 -lshell32 -luser32 -lkernel32 -lmingw32 -lgcc -lgcc_eh -lmoldname -lmingwex -lmsvcrt c:/mingw/bin/../lib/gcc/mingw32/6.3.0/crtend.o
> 
> COLLECT_GCC_OPTIONS='-v' '-o' 'cmTC_ea432.exe' '-mtune=generic' '-march=i586'
> 
> mingw32-make.exe[1]: Leaving directory 'F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp'
> 
> 
> 
> Parsed C implicit link information from above output:
>   link line regex: [^( *|.*[/\])(ld\.exe|CMAKE_LINK_STARTFILE-NOTFOUND|([^/\]+-)?ld|collect2)[^/\]*( |$)]
>   ignore line: [Change Dir: F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp]
>   ignore line: []
>   ignore line: [Run Build Command:"C:/MinGW/bin/mingw32-make.exe" "cmTC_ea432/fast"]
>   ignore line: [C:/MinGW/bin/mingw32-make.exe -f CMakeFiles\cmTC_ea432.dir\build.make CMakeFiles/cmTC_ea432.dir/build]
>   ignore line: [mingw32-make.exe[1]: Entering directory 'F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp']
>   ignore line: [Building C object CMakeFiles/cmTC_ea432.dir/CMakeCCompilerABI.c.obj]
>   ignore line: [C:\MinGW\bin\mingw32-gcc.exe    -o CMakeFiles\cmTC_ea432.dir\CMakeCCompilerABI.c.obj   -c "C:\Program Files\CMake\share\cmake-3.11\Modules\CMakeCCompilerABI.c"]
>   ignore line: [Linking C executable cmTC_ea432.exe]
>   ignore line: ["C:\Program Files\CMake\bin\cmake.exe" -E cmake_link_script CMakeFiles\cmTC_ea432.dir\link.txt --verbose=1]
>   ignore line: ["C:\Program Files\CMake\bin\cmake.exe" -E remove -f CMakeFiles\cmTC_ea432.dir/objects.a]
>   ignore line: [C:\MinGW\bin\ar.exe cr CMakeFiles\cmTC_ea432.dir/objects.a @CMakeFiles\cmTC_ea432.dir\objects1.rsp]
>   ignore line: [C:\MinGW\bin\mingw32-gcc.exe     -v -Wl,--whole-archive CMakeFiles\cmTC_ea432.dir/objects.a -Wl,--no-whole-archive  -o cmTC_ea432.exe -Wl,--out-implib,libcmTC_ea432.dll.a -Wl,--major-image-version,0,--minor-image-version,0 ]
>   ignore line: [Using built-in specs.]
>   ignore line: [COLLECT_GCC=C:\MinGW\bin\mingw32-gcc.exe]
>   ignore line: [COLLECT_LTO_WRAPPER=c:/mingw/bin/../libexec/gcc/mingw32/6.3.0/lto-wrapper.exe]
>   ignore line: [Target: mingw32]
>   ignore line: [Configured with: ../src/gcc-6.3.0/configure --build=x86_64-pc-linux-gnu --host=mingw32 --target=mingw32 --with-gmp=/mingw --with-mpfr --with-mpc=/mingw --with-isl=/mingw --prefix=/mingw --disable-win32-registry --with-arch=i586 --with-tune=generic --enable-languages=c,c++,objc,obj-c++,fortran,ada --with-pkgversion='MinGW.org GCC-6.3.0-1' --enable-static --enable-shared --enable-threads --with-dwarf2 --disable-sjlj-exceptions --enable-version-specific-runtime-libs --with-libiconv-prefix=/mingw --with-libintl-prefix=/mingw --enable-libstdcxx-debug --enable-libgomp --disable-libvtv --enable-nls]
>   ignore line: [Thread model: win32]
>   ignore line: [gcc version 6.3.0 (MinGW.org GCC-6.3.0-1) ]
>   ignore line: [COMPILER_PATH=c:/mingw/bin/../libexec/gcc/mingw32/6.3.0/]
>   ignore line: [c:/mingw/bin/../libexec/gcc/]
>   ignore line: [c:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../../../mingw32/bin/]
>   ignore line: [LIBRARY_PATH=c:/mingw/bin/../lib/gcc/mingw32/6.3.0/]
>   ignore line: [c:/mingw/bin/../lib/gcc/]
>   ignore line: [c:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../../../mingw32/lib/]
>   ignore line: [c:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../../]
>   ignore line: [COLLECT_GCC_OPTIONS='-v' '-o' 'cmTC_ea432.exe' '-mtune=generic' '-march=i586']
>   link line: [ c:/mingw/bin/../libexec/gcc/mingw32/6.3.0/collect2.exe -plugin c:/mingw/bin/../libexec/gcc/mingw32/6.3.0/liblto_plugin-0.dll -plugin-opt=c:/mingw/bin/../libexec/gcc/mingw32/6.3.0/lto-wrapper.exe -plugin-opt=-fresolution=C:\Users\Matthew\AppData\Local\Temp\ccZcMt4f.res -plugin-opt=-pass-through=-lmingw32 -plugin-opt=-pass-through=-lgcc -plugin-opt=-pass-through=-lgcc_eh -plugin-opt=-pass-through=-lmoldname -plugin-opt=-pass-through=-lmingwex -plugin-opt=-pass-through=-lmsvcrt -plugin-opt=-pass-through=-ladvapi32 -plugin-opt=-pass-through=-lshell32 -plugin-opt=-pass-through=-luser32 -plugin-opt=-pass-through=-lkernel32 -plugin-opt=-pass-through=-lmingw32 -plugin-opt=-pass-through=-lgcc -plugin-opt=-pass-through=-lgcc_eh -plugin-opt=-pass-through=-lmoldname -plugin-opt=-pass-through=-lmingwex -plugin-opt=-pass-through=-lmsvcrt -Bdynamic -o cmTC_ea432.exe c:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../../crt2.o c:/mingw/bin/../lib/gcc/mingw32/6.3.0/crtbegin.o -Lc:/mingw/bin/../lib/gcc/mingw32/6.3.0 -Lc:/mingw/bin/../lib/gcc -Lc:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../../../mingw32/lib -Lc:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../.. --whole-archive CMakeFiles\cmTC_ea432.dir/objects.a --no-whole-archive --out-implib libcmTC_ea432.dll.a --major-image-version 0 --minor-image-version 0 -lmingw32 -lgcc -lgcc_eh -lmoldname -lmingwex -lmsvcrt -ladvapi32 -lshell32 -luser32 -lkernel32 -lmingw32 -lgcc -lgcc_eh -lmoldname -lmingwex -lmsvcrt c:/mingw/bin/../lib/gcc/mingw32/6.3.0/crtend.o]
>     arg [c:/mingw/bin/../libexec/gcc/mingw32/6.3.0/collect2.exe] ==> ignore
>     arg [-plugin] ==> ignore
>     arg [c:/mingw/bin/../libexec/gcc/mingw32/6.3.0/liblto_plugin-0.dll] ==> ignore
>     arg [-plugin-opt=c:/mingw/bin/../libexec/gcc/mingw32/6.3.0/lto-wrapper.exe] ==> ignore
>     arg [-plugin-opt=-fresolution=C:\Users\Matthew\AppData\Local\Temp\ccZcMt4f.res] ==> ignore
>     arg [-plugin-opt=-pass-through=-lmingw32] ==> ignore
>     arg [-plugin-opt=-pass-through=-lgcc] ==> ignore
>     arg [-plugin-opt=-pass-through=-lgcc_eh] ==> ignore
>     arg [-plugin-opt=-pass-through=-lmoldname] ==> ignore
>     arg [-plugin-opt=-pass-through=-lmingwex] ==> ignore
>     arg [-plugin-opt=-pass-through=-lmsvcrt] ==> ignore
>     arg [-plugin-opt=-pass-through=-ladvapi32] ==> ignore
>     arg [-plugin-opt=-pass-through=-lshell32] ==> ignore
>     arg [-plugin-opt=-pass-through=-luser32] ==> ignore
>     arg [-plugin-opt=-pass-through=-lkernel32] ==> ignore
>     arg [-plugin-opt=-pass-through=-lmingw32] ==> ignore
>     arg [-plugin-opt=-pass-through=-lgcc] ==> ignore
>     arg [-plugin-opt=-pass-through=-lgcc_eh] ==> ignore
>     arg [-plugin-opt=-pass-through=-lmoldname] ==> ignore
>     arg [-plugin-opt=-pass-through=-lmingwex] ==> ignore
>     arg [-plugin-opt=-pass-through=-lmsvcrt] ==> ignore
>     arg [-Bdynamic] ==> ignore
>     arg [-o] ==> ignore
>     arg [cmTC_ea432.exe] ==> ignore
>     arg [c:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../../crt2.o] ==> ignore
>     arg [c:/mingw/bin/../lib/gcc/mingw32/6.3.0/crtbegin.o] ==> ignore
>     arg [-Lc:/mingw/bin/../lib/gcc/mingw32/6.3.0] ==> dir [c:/mingw/bin/../lib/gcc/mingw32/6.3.0]
>     arg [-Lc:/mingw/bin/../lib/gcc] ==> dir [c:/mingw/bin/../lib/gcc]
>     arg [-Lc:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../../../mingw32/lib] ==> dir [c:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../../../mingw32/lib]
>     arg [-Lc:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../..] ==> dir [c:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../..]
>     arg [--whole-archive] ==> ignore
>     arg [CMakeFiles\cmTC_ea432.dir/objects.a] ==> ignore
>     arg [--no-whole-archive] ==> ignore
>     arg [--out-implib] ==> ignore
>     arg [libcmTC_ea432.dll.a] ==> ignore
>     arg [--major-image-version] ==> ignore
>     arg [0] ==> ignore
>     arg [--minor-image-version] ==> ignore
>     arg [0] ==> ignore
>     arg [-lmingw32] ==> lib [mingw32]
>     arg [-lgcc] ==> lib [gcc]
>     arg [-lgcc_eh] ==> lib [gcc_eh]
>     arg [-lmoldname] ==> lib [moldname]
>     arg [-lmingwex] ==> lib [mingwex]
>     arg [-lmsvcrt] ==> lib [msvcrt]
>     arg [-ladvapi32] ==> lib [advapi32]
>     arg [-lshell32] ==> lib [shell32]
>     arg [-luser32] ==> lib [user32]
>     arg [-lkernel32] ==> lib [kernel32]
>     arg [-lmingw32] ==> lib [mingw32]
>     arg [-lgcc] ==> lib [gcc]
>     arg [-lgcc_eh] ==> lib [gcc_eh]
>     arg [-lmoldname] ==> lib [moldname]
>     arg [-lmingwex] ==> lib [mingwex]
>     arg [-lmsvcrt] ==> lib [msvcrt]
>     arg [c:/mingw/bin/../lib/gcc/mingw32/6.3.0/crtend.o] ==> ignore
>   remove lib [gcc_eh]
>   remove lib [msvcrt]
>   remove lib [gcc_eh]
>   remove lib [msvcrt]
>   collapse library dir [c:/mingw/bin/../lib/gcc/mingw32/6.3.0] ==> [C:/MinGW/lib/gcc/mingw32/6.3.0]
>   collapse library dir [c:/mingw/bin/../lib/gcc] ==> [C:/MinGW/lib/gcc]
>   collapse library dir [c:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../../../mingw32/lib] ==> [C:/MinGW/mingw32/lib]
>   collapse library dir [c:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../..] ==> [C:/MinGW/lib]
>   implicit libs: [mingw32;gcc;moldname;mingwex;advapi32;shell32;user32;kernel32;mingw32;gcc;moldname;mingwex]
>   implicit dirs: [C:/MinGW/lib/gcc/mingw32/6.3.0;C:/MinGW/lib/gcc;C:/MinGW/mingw32/lib;C:/MinGW/lib]
>   implicit fwks: []
> 
> 
> 
> 
> Detecting C [-std=c11] compiler features compiled with the following output:
> Change Dir: F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp
> 
> Run Build Command:"C:/MinGW/bin/mingw32-make.exe" "cmTC_a7aec/fast"
> C:/MinGW/bin/mingw32-make.exe -f CMakeFiles\cmTC_a7aec.dir\build.make CMakeFiles/cmTC_a7aec.dir/build
> 
> mingw32-make.exe[1]: Entering directory 'F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp'
> 
> Building C object CMakeFiles/cmTC_a7aec.dir/feature_tests.c.obj
> 
> C:\MinGW\bin\mingw32-gcc.exe   -std=c11 -o CMakeFiles\cmTC_a7aec.dir\feature_tests.c.obj   -c F:\URHOTEMPLATEPROJECTMAYBEv2\CMakeFiles\feature_tests.c
> 
> Linking C executable cmTC_a7aec.exe
> 
> "C:\Program Files\CMake\bin\cmake.exe" -E cmake_link_script CMakeFiles\cmTC_a7aec.dir\link.txt --verbose=1
> 
> "C:\Program Files\CMake\bin\cmake.exe" -E remove -f CMakeFiles\cmTC_a7aec.dir/objects.a
> C:\MinGW\bin\ar.exe cr CMakeFiles\cmTC_a7aec.dir/objects.a @CMakeFiles\cmTC_a7aec.dir\objects1.rsp
> C:\MinGW\bin\mingw32-gcc.exe      -Wl,--whole-archive CMakeFiles\cmTC_a7aec.dir/objects.a -Wl,--no-whole-archive  -o cmTC_a7aec.exe -Wl,--out-implib,libcmTC_a7aec.dll.a -Wl,--major-image-version,0,--minor-image-version,0 @CMakeFiles\cmTC_a7aec.dir\linklibs.rsp
> mingw32-make.exe[1]: Leaving directory 'F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp'
> 
> 
> 
>     Feature record: C_FEATURE:1c_function_prototypes
>     Feature record: C_FEATURE:1c_restrict
>     Feature record: C_FEATURE:1c_static_assert
>     Feature record: C_FEATURE:1c_variadic_macros
> 
> 
> Detecting C [-std=c99] compiler features compiled with the following output:
> Change Dir: F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp
> 
> Run Build Command:"C:/MinGW/bin/mingw32-make.exe" "cmTC_04fc3/fast"
> C:/MinGW/bin/mingw32-make.exe -f CMakeFiles\cmTC_04fc3.dir\build.make CMakeFiles/cmTC_04fc3.dir/build
> 
> mingw32-make.exe[1]: Entering directory 'F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp'
> 
> Building C object CMakeFiles/cmTC_04fc3.dir/feature_tests.c.obj
> 
> C:\MinGW\bin\mingw32-gcc.exe   -std=c99 -o CMakeFiles\cmTC_04fc3.dir\feature_tests.c.obj   -c F:\URHOTEMPLATEPROJECTMAYBEv2\CMakeFiles\feature_tests.c
> 
> Linking C executable cmTC_04fc3.exe
> 
> "C:\Program Files\CMake\bin\cmake.exe" -E cmake_link_script CMakeFiles\cmTC_04fc3.dir\link.txt --verbose=1
> 
> "C:\Program Files\CMake\bin\cmake.exe" -E remove -f CMakeFiles\cmTC_04fc3.dir/objects.a
> C:\MinGW\bin\ar.exe cr CMakeFiles\cmTC_04fc3.dir/objects.a @CMakeFiles\cmTC_04fc3.dir\objects1.rsp
> C:\MinGW\bin\mingw32-gcc.exe      -Wl,--whole-archive CMakeFiles\cmTC_04fc3.dir/objects.a -Wl,--no-whole-archive  -o cmTC_04fc3.exe -Wl,--out-implib,libcmTC_04fc3.dll.a -Wl,--major-image-version,0,--minor-image-version,0 @CMakeFiles\cmTC_04fc3.dir\linklibs.rsp
> mingw32-make.exe[1]: Leaving directory 'F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp'
> 
> 
> 
>     Feature record: C_FEATURE:1c_function_prototypes
>     Feature record: C_FEATURE:1c_restrict
>     Feature record: C_FEATURE:0c_static_assert
>     Feature record: C_FEATURE:1c_variadic_macros
> 
> 
> Detecting C [-std=c90] compiler features compiled with the following output:
> Change Dir: F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp
> 
> Run Build Command:"C:/MinGW/bin/mingw32-make.exe" "cmTC_3d1c6/fast"
> C:/MinGW/bin/mingw32-make.exe -f CMakeFiles\cmTC_3d1c6.dir\build.make CMakeFiles/cmTC_3d1c6.dir/build
> 
> mingw32-make.exe[1]: Entering directory 'F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp'
> 
> Building C object CMakeFiles/cmTC_3d1c6.dir/feature_tests.c.obj
> 
> C:\MinGW\bin\mingw32-gcc.exe   -std=c90 -o CMakeFiles\cmTC_3d1c6.dir\feature_tests.c.obj   -c F:\URHOTEMPLATEPROJECTMAYBEv2\CMakeFiles\feature_tests.c
> 
> Linking C executable cmTC_3d1c6.exe
> 
> "C:\Program Files\CMake\bin\cmake.exe" -E cmake_link_script CMakeFiles\cmTC_3d1c6.dir\link.txt --verbose=1
> 
> "C:\Program Files\CMake\bin\cmake.exe" -E remove -f CMakeFiles\cmTC_3d1c6.dir/objects.a
> C:\MinGW\bin\ar.exe cr CMakeFiles\cmTC_3d1c6.dir/objects.a @CMakeFiles\cmTC_3d1c6.dir\objects1.rsp
> C:\MinGW\bin\mingw32-gcc.exe      -Wl,--whole-archive CMakeFiles\cmTC_3d1c6.dir/objects.a -Wl,--no-whole-archive  -o cmTC_3d1c6.exe -Wl,--out-implib,libcmTC_3d1c6.dll.a -Wl,--major-image-version,0,--minor-image-version,0 @CMakeFiles\cmTC_3d1c6.dir\linklibs.rsp
> mingw32-make.exe[1]: Leaving directory 'F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp'
> 
> 
> 
>     Feature record: C_FEATURE:1c_function_prototypes
>     Feature record: C_FEATURE:0c_restrict
>     Feature record: C_FEATURE:0c_static_assert
>     Feature record: C_FEATURE:0c_variadic_macros
> Determining if the CXX compiler works passed with the following output:
> Change Dir: F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp
> 
> Run Build Command:"C:/MinGW/bin/mingw32-make.exe" "cmTC_9346f/fast"
> C:/MinGW/bin/mingw32-make.exe -f CMakeFiles\cmTC_9346f.dir\build.make CMakeFiles/cmTC_9346f.dir/build
> 
> mingw32-make.exe[1]: Entering directory 'F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp'
> 
> Building CXX object CMakeFiles/cmTC_9346f.dir/testCXXCompiler.cxx.obj
> 
> C:\MinGW\bin\mingw32-g++.exe     -o CMakeFiles\cmTC_9346f.dir\testCXXCompiler.cxx.obj -c F:\URHOTEMPLATEPROJECTMAYBEv2\CMakeFiles\CMakeTmp\testCXXCompiler.cxx
> 
> Linking CXX executable cmTC_9346f.exe
> 
> "C:\Program Files\CMake\bin\cmake.exe" -E cmake_link_script CMakeFiles\cmTC_9346f.dir\link.txt --verbose=1
> 
> "C:\Program Files\CMake\bin\cmake.exe" -E remove -f CMakeFiles\cmTC_9346f.dir/objects.a
> C:\MinGW\bin\ar.exe cr CMakeFiles\cmTC_9346f.dir/objects.a @CMakeFiles\cmTC_9346f.dir\objects1.rsp
> C:\MinGW\bin\mingw32-g++.exe      -Wl,--whole-archive CMakeFiles\cmTC_9346f.dir/objects.a -Wl,--no-whole-archive  -o cmTC_9346f.exe -Wl,--out-implib,libcmTC_9346f.dll.a -Wl,--major-image-version,0,--minor-image-version,0 @CMakeFiles\cmTC_9346f.dir\linklibs.rsp
> mingw32-make.exe[1]: Leaving directory 'F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp'
> 
> 
> 
> Detecting CXX compiler ABI info compiled with the following output:
> Change Dir: F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp
> 
> Run Build Command:"C:/MinGW/bin/mingw32-make.exe" "cmTC_50066/fast"
> C:/MinGW/bin/mingw32-make.exe -f CMakeFiles\cmTC_50066.dir\build.make CMakeFiles/cmTC_50066.dir/build
> 
> mingw32-make.exe[1]: Entering directory 'F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp'
> 
> Building CXX object CMakeFiles/cmTC_50066.dir/CMakeCXXCompilerABI.cpp.obj
> 
> C:\MinGW\bin\mingw32-g++.exe     -o CMakeFiles\cmTC_50066.dir\CMakeCXXCompilerABI.cpp.obj -c "C:\Program Files\CMake\share\cmake-3.11\Modules\CMakeCXXCompilerABI.cpp"
> 
> Linking CXX executable cmTC_50066.exe
> 
> "C:\Program Files\CMake\bin\cmake.exe" -E cmake_link_script CMakeFiles\cmTC_50066.dir\link.txt --verbose=1
> 
> "C:\Program Files\CMake\bin\cmake.exe" -E remove -f CMakeFiles\cmTC_50066.dir/objects.a
> C:\MinGW\bin\ar.exe cr CMakeFiles\cmTC_50066.dir/objects.a @CMakeFiles\cmTC_50066.dir\objects1.rsp
> C:\MinGW\bin\mingw32-g++.exe     -v -Wl,--whole-archive CMakeFiles\cmTC_50066.dir/objects.a -Wl,--no-whole-archive  -o cmTC_50066.exe -Wl,--out-implib,libcmTC_50066.dll.a -Wl,--major-image-version,0,--minor-image-version,0 
> Using built-in specs.
> 
> COLLECT_GCC=C:\MinGW\bin\mingw32-g++.exe
> 
> COLLECT_LTO_WRAPPER=c:/mingw/bin/../libexec/gcc/mingw32/6.3.0/lto-wrapper.exe
> 
> Target: mingw32
> 
> Configured with: ../src/gcc-6.3.0/configure --build=x86_64-pc-linux-gnu --host=mingw32 --with-gmp=/mingw --with-mpfr=/mingw --with-mpc=/mingw --with-isl=/mingw --prefix=/mingw --disable-win32-registry --target=mingw32 --with-arch=i586 --enable-languages=c,c++,objc,obj-c++,fortran,ada --with-pkgversion='MinGW.org GCC-6.3.0-1' --enable-static --enable-shared --enable-threads --with-dwarf2 --disable-sjlj-exceptions --enable-version-specific-runtime-libs --with-libiconv-prefix=/mingw --with-libintl-prefix=/mingw --enable-libstdcxx-debug --with-tune=generic --enable-libgomp --disable-libvtv --enable-nls
> 
> Thread model: win32
> 
> gcc version 6.3.0 (MinGW.org GCC-6.3.0-1) 
> 
> COMPILER_PATH=c:/mingw/bin/../libexec/gcc/mingw32/6.3.0/;c:/mingw/bin/../libexec/gcc/;c:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../../../mingw32/bin/
> 
...

-------------------------

mldevs | 2018-03-28 19:37:41 UTC | #13

> LIBRARY_PATH=c:/mingw/bin/../lib/gcc/mingw32/6.3.0/;c:/mingw/bin/../lib/gcc/;c:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../../../mingw32/lib/;c:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../../
> 
> COLLECT_GCC_OPTIONS='-v' '-o' 'cmTC_50066.exe' '-shared-libgcc' '-mtune=generic' '-march=i586'
> 
>  c:/mingw/bin/../libexec/gcc/mingw32/6.3.0/collect2.exe -plugin c:/mingw/bin/../libexec/gcc/mingw32/6.3.0/liblto_plugin-0.dll -plugin-opt=c:/mingw/bin/../libexec/gcc/mingw32/6.3.0/lto-wrapper.exe -plugin-opt=-fresolution=C:\Users\Matthew\AppData\Local\Temp\cciia8Tt.res -plugin-opt=-pass-through=-lmingw32 -plugin-opt=-pass-through=-lgcc_s -plugin-opt=-pass-through=-lgcc -plugin-opt=-pass-through=-lmoldname -plugin-opt=-pass-through=-lmingwex -plugin-opt=-pass-through=-lmsvcrt -plugin-opt=-pass-through=-ladvapi32 -plugin-opt=-pass-through=-lshell32 -plugin-opt=-pass-through=-luser32 -plugin-opt=-pass-through=-lkernel32 -plugin-opt=-pass-through=-lmingw32 -plugin-opt=-pass-through=-lgcc_s -plugin-opt=-pass-through=-lgcc -plugin-opt=-pass-through=-lmoldname -plugin-opt=-pass-through=-lmingwex -plugin-opt=-pass-through=-lmsvcrt -Bdynamic -u ___register_frame_info -u ___deregister_frame_info -o cmTC_50066.exe c:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../../crt2.o c:/mingw/bin/../lib/gcc/mingw32/6.3.0/crtbegin.o -Lc:/mingw/bin/../lib/gcc/mingw32/6.3.0 -Lc:/mingw/bin/../lib/gcc -Lc:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../../../mingw32/lib -Lc:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../.. --whole-archive CMakeFiles\cmTC_50066.dir/objects.a --no-whole-archive --out-implib libcmTC_50066.dll.a --major-image-version 0 --minor-image-version 0 -lstdc++ -lmingw32 -lgcc_s -lgcc -lmoldname -lmingwex -lmsvcrt -ladvapi32 -lshell32 -luser32 -lkernel32 -lmingw32 -lgcc_s -lgcc -lmoldname -lmingwex -lmsvcrt c:/mingw/bin/../lib/gcc/mingw32/6.3.0/crtend.o
> 
> COLLECT_GCC_OPTIONS='-v' '-o' 'cmTC_50066.exe' '-shared-libgcc' '-mtune=generic' '-march=i586'
> 
> mingw32-make.exe[1]: Leaving directory 'F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp'
> 
> 
> 
> Parsed CXX implicit link information from above output:
>   link line regex: [^( *|.*[/\])(ld\.exe|CMAKE_LINK_STARTFILE-NOTFOUND|([^/\]+-)?ld|collect2)[^/\]*( |$)]
>   ignore line: [Change Dir: F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp]
>   ignore line: []
>   ignore line: [Run Build Command:"C:/MinGW/bin/mingw32-make.exe" "cmTC_50066/fast"]
>   ignore line: [C:/MinGW/bin/mingw32-make.exe -f CMakeFiles\cmTC_50066.dir\build.make CMakeFiles/cmTC_50066.dir/build]
>   ignore line: [mingw32-make.exe[1]: Entering directory 'F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp']
>   ignore line: [Building CXX object CMakeFiles/cmTC_50066.dir/CMakeCXXCompilerABI.cpp.obj]
>   ignore line: [C:\MinGW\bin\mingw32-g++.exe     -o CMakeFiles\cmTC_50066.dir\CMakeCXXCompilerABI.cpp.obj -c "C:\Program Files\CMake\share\cmake-3.11\Modules\CMakeCXXCompilerABI.cpp"]
>   ignore line: [Linking CXX executable cmTC_50066.exe]
>   ignore line: ["C:\Program Files\CMake\bin\cmake.exe" -E cmake_link_script CMakeFiles\cmTC_50066.dir\link.txt --verbose=1]
>   ignore line: ["C:\Program Files\CMake\bin\cmake.exe" -E remove -f CMakeFiles\cmTC_50066.dir/objects.a]
>   ignore line: [C:\MinGW\bin\ar.exe cr CMakeFiles\cmTC_50066.dir/objects.a @CMakeFiles\cmTC_50066.dir\objects1.rsp]
>   ignore line: [C:\MinGW\bin\mingw32-g++.exe     -v -Wl,--whole-archive CMakeFiles\cmTC_50066.dir/objects.a -Wl,--no-whole-archive  -o cmTC_50066.exe -Wl,--out-implib,libcmTC_50066.dll.a -Wl,--major-image-version,0,--minor-image-version,0 ]
>   ignore line: [Using built-in specs.]
>   ignore line: [COLLECT_GCC=C:\MinGW\bin\mingw32-g++.exe]
>   ignore line: [COLLECT_LTO_WRAPPER=c:/mingw/bin/../libexec/gcc/mingw32/6.3.0/lto-wrapper.exe]
>   ignore line: [Target: mingw32]
>   ignore line: [Configured with: ../src/gcc-6.3.0/configure --build=x86_64-pc-linux-gnu --host=mingw32 --with-gmp=/mingw --with-mpfr=/mingw --with-mpc=/mingw --with-isl=/mingw --prefix=/mingw --disable-win32-registry --target=mingw32 --with-arch=i586 --enable-languages=c,c++,objc,obj-c++,fortran,ada --with-pkgversion='MinGW.org GCC-6.3.0-1' --enable-static --enable-shared --enable-threads --with-dwarf2 --disable-sjlj-exceptions --enable-version-specific-runtime-libs --with-libiconv-prefix=/mingw --with-libintl-prefix=/mingw --enable-libstdcxx-debug --with-tune=generic --enable-libgomp --disable-libvtv --enable-nls]
>   ignore line: [Thread model: win32]
>   ignore line: [gcc version 6.3.0 (MinGW.org GCC-6.3.0-1) ]
>   ignore line: [COMPILER_PATH=c:/mingw/bin/../libexec/gcc/mingw32/6.3.0/]
>   ignore line: [c:/mingw/bin/../libexec/gcc/]
>   ignore line: [c:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../../../mingw32/bin/]
>   ignore line: [LIBRARY_PATH=c:/mingw/bin/../lib/gcc/mingw32/6.3.0/]
>   ignore line: [c:/mingw/bin/../lib/gcc/]
>   ignore line: [c:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../../../mingw32/lib/]
>   ignore line: [c:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../../]
>   ignore line: [COLLECT_GCC_OPTIONS='-v' '-o' 'cmTC_50066.exe' '-shared-libgcc' '-mtune=generic' '-march=i586']
>   link line: [ c:/mingw/bin/../libexec/gcc/mingw32/6.3.0/collect2.exe -plugin c:/mingw/bin/../libexec/gcc/mingw32/6.3.0/liblto_plugin-0.dll -plugin-opt=c:/mingw/bin/../libexec/gcc/mingw32/6.3.0/lto-wrapper.exe -plugin-opt=-fresolution=C:\Users\Matthew\AppData\Local\Temp\cciia8Tt.res -plugin-opt=-pass-through=-lmingw32 -plugin-opt=-pass-through=-lgcc_s -plugin-opt=-pass-through=-lgcc -plugin-opt=-pass-through=-lmoldname -plugin-opt=-pass-through=-lmingwex -plugin-opt=-pass-through=-lmsvcrt -plugin-opt=-pass-through=-ladvapi32 -plugin-opt=-pass-through=-lshell32 -plugin-opt=-pass-through=-luser32 -plugin-opt=-pass-through=-lkernel32 -plugin-opt=-pass-through=-lmingw32 -plugin-opt=-pass-through=-lgcc_s -plugin-opt=-pass-through=-lgcc -plugin-opt=-pass-through=-lmoldname -plugin-opt=-pass-through=-lmingwex -plugin-opt=-pass-through=-lmsvcrt -Bdynamic -u ___register_frame_info -u ___deregister_frame_info -o cmTC_50066.exe c:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../../crt2.o c:/mingw/bin/../lib/gcc/mingw32/6.3.0/crtbegin.o -Lc:/mingw/bin/../lib/gcc/mingw32/6.3.0 -Lc:/mingw/bin/../lib/gcc -Lc:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../../../mingw32/lib -Lc:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../.. --whole-archive CMakeFiles\cmTC_50066.dir/objects.a --no-whole-archive --out-implib libcmTC_50066.dll.a --major-image-version 0 --minor-image-version 0 -lstdc++ -lmingw32 -lgcc_s -lgcc -lmoldname -lmingwex -lmsvcrt -ladvapi32 -lshell32 -luser32 -lkernel32 -lmingw32 -lgcc_s -lgcc -lmoldname -lmingwex -lmsvcrt c:/mingw/bin/../lib/gcc/mingw32/6.3.0/crtend.o]
>     arg [c:/mingw/bin/../libexec/gcc/mingw32/6.3.0/collect2.exe] ==> ignore
>     arg [-plugin] ==> ignore
>     arg [c:/mingw/bin/../libexec/gcc/mingw32/6.3.0/liblto_plugin-0.dll] ==> ignore
>     arg [-plugin-opt=c:/mingw/bin/../libexec/gcc/mingw32/6.3.0/lto-wrapper.exe] ==> ignore
>     arg [-plugin-opt=-fresolution=C:\Users\Matthew\AppData\Local\Temp\cciia8Tt.res] ==> ignore
>     arg [-plugin-opt=-pass-through=-lmingw32] ==> ignore
>     arg [-plugin-opt=-pass-through=-lgcc_s] ==> ignore
>     arg [-plugin-opt=-pass-through=-lgcc] ==> ignore
>     arg [-plugin-opt=-pass-through=-lmoldname] ==> ignore
>     arg [-plugin-opt=-pass-through=-lmingwex] ==> ignore
>     arg [-plugin-opt=-pass-through=-lmsvcrt] ==> ignore
>     arg [-plugin-opt=-pass-through=-ladvapi32] ==> ignore
>     arg [-plugin-opt=-pass-through=-lshell32] ==> ignore
>     arg [-plugin-opt=-pass-through=-luser32] ==> ignore
>     arg [-plugin-opt=-pass-through=-lkernel32] ==> ignore
>     arg [-plugin-opt=-pass-through=-lmingw32] ==> ignore
>     arg [-plugin-opt=-pass-through=-lgcc_s] ==> ignore
>     arg [-plugin-opt=-pass-through=-lgcc] ==> ignore
>     arg [-plugin-opt=-pass-through=-lmoldname] ==> ignore
>     arg [-plugin-opt=-pass-through=-lmingwex] ==> ignore
>     arg [-plugin-opt=-pass-through=-lmsvcrt] ==> ignore
>     arg [-Bdynamic] ==> ignore
>     arg [-u] ==> ignore
>     arg [___register_frame_info] ==> ignore
>     arg [-u] ==> ignore
>     arg [___deregister_frame_info] ==> ignore
>     arg [-o] ==> ignore
>     arg [cmTC_50066.exe] ==> ignore
>     arg [c:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../../crt2.o] ==> ignore
>     arg [c:/mingw/bin/../lib/gcc/mingw32/6.3.0/crtbegin.o] ==> ignore
>     arg [-Lc:/mingw/bin/../lib/gcc/mingw32/6.3.0] ==> dir [c:/mingw/bin/../lib/gcc/mingw32/6.3.0]
>     arg [-Lc:/mingw/bin/../lib/gcc] ==> dir [c:/mingw/bin/../lib/gcc]
>     arg [-Lc:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../../../mingw32/lib] ==> dir [c:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../../../mingw32/lib]
>     arg [-Lc:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../..] ==> dir [c:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../..]
>     arg [--whole-archive] ==> ignore
>     arg [CMakeFiles\cmTC_50066.dir/objects.a] ==> ignore
>     arg [--no-whole-archive] ==> ignore
>     arg [--out-implib] ==> ignore
>     arg [libcmTC_50066.dll.a] ==> ignore
>     arg [--major-image-version] ==> ignore
>     arg [0] ==> ignore
>     arg [--minor-image-version] ==> ignore
>     arg [0] ==> ignore
>     arg [-lstdc++] ==> lib [stdc++]
>     arg [-lmingw32] ==> lib [mingw32]
>     arg [-lgcc_s] ==> lib [gcc_s]
>     arg [-lgcc] ==> lib [gcc]
>     arg [-lmoldname] ==> lib [moldname]
>     arg [-lmingwex] ==> lib [mingwex]
>     arg [-lmsvcrt] ==> lib [msvcrt]
>     arg [-ladvapi32] ==> lib [advapi32]
>     arg [-lshell32] ==> lib [shell32]
>     arg [-luser32] ==> lib [user32]
>     arg [-lkernel32] ==> lib [kernel32]
>     arg [-lmingw32] ==> lib [mingw32]
>     arg [-lgcc_s] ==> lib [gcc_s]
>     arg [-lgcc] ==> lib [gcc]
>     arg [-lmoldname] ==> lib [moldname]
>     arg [-lmingwex] ==> lib [mingwex]
>     arg [-lmsvcrt] ==> lib [msvcrt]
>     arg [c:/mingw/bin/../lib/gcc/mingw32/6.3.0/crtend.o] ==> ignore
>   remove lib [msvcrt]
>   remove lib [msvcrt]
>   collapse library dir [c:/mingw/bin/../lib/gcc/mingw32/6.3.0] ==> [C:/MinGW/lib/gcc/mingw32/6.3.0]
>   collapse library dir [c:/mingw/bin/../lib/gcc] ==> [C:/MinGW/lib/gcc]
>   collapse library dir [c:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../../../mingw32/lib] ==> [C:/MinGW/mingw32/lib]
>   collapse library dir [c:/mingw/bin/../lib/gcc/mingw32/6.3.0/../../..] ==> [C:/MinGW/lib]
>   implicit libs: [stdc++;mingw32;gcc_s;gcc;moldname;mingwex;advapi32;shell32;user32;kernel32;mingw32;gcc_s;gcc;moldname;mingwex]
>   implicit dirs: [C:/MinGW/lib/gcc/mingw32/6.3.0;C:/MinGW/lib/gcc;C:/MinGW/mingw32/lib;C:/MinGW/lib]
>   implicit fwks: []
> 
> 
> 
> 
> Detecting CXX [-std=c++1z] compiler features compiled with the following output:
> Change Dir: F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp
> 
> Run Build Command:"C:/MinGW/bin/mingw32-make.exe" "cmTC_b5d89/fast"
> C:/MinGW/bin/mingw32-make.exe -f CMakeFiles\cmTC_b5d89.dir\build.make CMakeFiles/cmTC_b5d89.dir/build
> 
> mingw32-make.exe[1]: Entering directory 'F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp'
> 
> Building CXX object CMakeFiles/cmTC_b5d89.dir/feature_tests.cxx.obj
> 
> C:\MinGW\bin\mingw32-g++.exe    -std=c++1z -o CMakeFiles\cmTC_b5d89.dir\feature_tests.cxx.obj -c F:\URHOTEMPLATEPROJECTMAYBEv2\CMakeFiles\feature_tests.cxx
> 
> Linking CXX executable cmTC_b5d89.exe
> 
> "C:\Program Files\CMake\bin\cmake.exe" -E cmake_link_script CMakeFiles\cmTC_b5d89.dir\link.txt --verbose=1
> 
> "C:\Program Files\CMake\bin\cmake.exe" -E remove -f CMakeFiles\cmTC_b5d89.dir/objects.a
> C:\MinGW\bin\ar.exe cr CMakeFiles\cmTC_b5d89.dir/objects.a @CMakeFiles\cmTC_b5d89.dir\objects1.rsp
> C:\MinGW\bin\mingw32-g++.exe      -Wl,--whole-archive CMakeFiles\cmTC_b5d89.dir/objects.a -Wl,--no-whole-archive  -o cmTC_b5d89.exe -Wl,--out-implib,libcmTC_b5d89.dll.a -Wl,--major-image-version,0,--minor-image-version,0 @CMakeFiles\cmTC_b5d89.dir\linklibs.rsp
> mingw32-make.exe[1]: Leaving directory 'F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp'
> 
> 
> 
>     Feature record: CXX_FEATURE:1cxx_aggregate_default_initializers
>     Feature record: CXX_FEATURE:1cxx_alias_templates
>     Feature record: CXX_FEATURE:1cxx_alignas
>     Feature record: CXX_FEATURE:1cxx_alignof
>     Feature record: CXX_FEATURE:1cxx_attributes
>     Feature record: CXX_FEATURE:1cxx_attribute_deprecated
>     Feature record: CXX_FEATURE:1cxx_auto_type
>     Feature record: CXX_FEATURE:1cxx_binary_literals
>     Feature record: CXX_FEATURE:1cxx_constexpr
>     Feature record: CXX_FEATURE:1cxx_contextual_conversions
>     Feature record: CXX_FEATURE:1cxx_decltype
>     Feature record: CXX_FEATURE:1cxx_decltype_auto
>     Feature record: CXX_FEATURE:1cxx_decltype_incomplete_return_types
>     Feature record: CXX_FEATURE:1cxx_default_function_template_args
>     Feature record: CXX_FEATURE:1cxx_defaulted_functions
>     Feature record: CXX_FEATURE:1cxx_defaulted_move_initializers
>     Feature record: CXX_FEATURE:1cxx_delegating_constructors
>     Feature record: CXX_FEATURE:1cxx_deleted_functions
>     Feature record: CXX_FEATURE:1cxx_digit_separators
>     Feature record: CXX_FEATURE:1cxx_enum_forward_declarations
>     Feature record: CXX_FEATURE:1cxx_explicit_conversions
>     Feature record: CXX_FEATURE:1cxx_extended_friend_declarations
>     Feature record: CXX_FEATURE:1cxx_extern_templates
>     Feature record: CXX_FEATURE:1cxx_final
>     Feature record: CXX_FEATURE:1cxx_func_identifier
>     Feature record: CXX_FEATURE:1cxx_generalized_initializers
>     Feature record: CXX_FEATURE:1cxx_generic_lambdas
>     Feature record: CXX_FEATURE:1cxx_inheriting_constructors
>     Feature record: CXX_FEATURE:1cxx_inline_namespaces
>     Feature record: CXX_FEATURE:1cxx_lambdas
>     Feature record: CXX_FEATURE:1cxx_lambda_init_captures
>     Feature record: CXX_FEATURE:1cxx_local_type_template_args
>     Feature record: CXX_FEATURE:1cxx_long_long_type
>     Feature record: CXX_FEATURE:1cxx_noexcept
>     Feature record: CXX_FEATURE:1cxx_nonstatic_member_init
>     Feature record: CXX_FEATURE:1cxx_nullptr
>     Feature record: CXX_FEATURE:1cxx_override
>     Feature record: CXX_FEATURE:1cxx_range_for
>     Feature record: CXX_FEATURE:1cxx_raw_string_literals
>     Feature record: CXX_FEATURE:1cxx_reference_qualified_functions
>     Feature record: CXX_FEATURE:1cxx_relaxed_constexpr
>     Feature record: CXX_FEATURE:1cxx_return_type_deduction
>     Feature record: CXX_FEATURE:1cxx_right_angle_brackets
>     Feature record: CXX_FEATURE:1cxx_rvalue_references
>     Feature record: CXX_FEATURE:1cxx_sizeof_member
>     Feature record: CXX_FEATURE:1cxx_static_assert
>     Feature record: CXX_FEATURE:1cxx_strong_enums
>     Feature record: CXX_FEATURE:1cxx_template_template_parameters
>     Feature record: CXX_FEATURE:1cxx_thread_local
>     Feature record: CXX_FEATURE:1cxx_trailing_return_types
>     Feature record: CXX_FEATURE:1cxx_unicode_literals
>     Feature record: CXX_FEATURE:1cxx_uniform_initialization
>     Feature record: CXX_FEATURE:1cxx_unrestricted_unions
>     Feature record: CXX_FEATURE:1cxx_user_literals
>     Feature record: CXX_FEATURE:1cxx_variable_templates
>     Feature record: CXX_FEATURE:1cxx_variadic_macros
>     Feature record: CXX_FEATURE:1cxx_variadic_templates
> 
> 
> Detecting CXX [-std=c++14] compiler features compiled with the following output:
> Change Dir: F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp
> 
> Run Build Command:"C:/MinGW/bin/mingw32-make.exe" "cmTC_7007e/fast"
> C:/MinGW/bin/mingw32-make.exe -f CMakeFiles\cmTC_7007e.dir\build.make CMakeFiles/cmTC_7007e.dir/build
> 
> mingw32-make.exe[1]: Entering directory 'F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp'
> 
> Building CXX object CMakeFiles/cmTC_7007e.dir/feature_tests.cxx.obj
> 
> C:\MinGW\bin\mingw32-g++.exe    -std=c++14 -o CMakeFiles\cmTC_7007e.dir\feature_tests.cxx.obj -c F:\URHOTEMPLATEPROJECTMAYBEv2\CMakeFiles\feature_tests.cxx
> 
> Linking CXX executable cmTC_7007e.exe
> 
> "C:\Program Files\CMake\bin\cmake.exe" -E cmake_link_script CMakeFiles\cmTC_7007e.dir\link.txt --verbose=1
> 
> "C:\Program Files\CMake\bin\cmake.exe" -E remove -f CMakeFiles\cmTC_7007e.dir/objects.a
> C:\MinGW\bin\ar.exe cr CMakeFiles\cmTC_7007e.dir/objects.a @CMakeFiles\cmTC_7007e.dir\objects1.rsp
> C:\MinGW\bin\mingw32-g++.exe      -Wl,--whole-archive CMakeFiles\cmTC_7007e.dir/objects.a -Wl,--no-whole-archive  -o cmTC_7007e.exe -Wl,--out-implib,libcmTC_7007e.dll.a -Wl,--major-image-version,0,--minor-image-version,0 @CMakeFiles\cmTC_7007e.dir\linklibs.rsp
> mingw32-make.exe[1]: Leaving directory 'F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp'
> 
> 
> 
>     Feature record: CXX_FEATURE:1cxx_aggregate_default_initializers
>     Feature record: CXX_FEATURE:1cxx_alias_templates
>     Feature record: CXX_FEATURE:1cxx_alignas
>     Feature record: CXX_FEATURE:1cxx_alignof
>     Feature record: CXX_FEATURE:1cxx_attributes
>     Feature record: CXX_FEATURE:1cxx_attribute_deprecated
>     Feature record: CXX_FEATURE:1cxx_auto_type
>     Feature record: CXX_FEATURE:1cxx_binary_literals
>     Feature record: CXX_FEATURE:1cxx_constexpr
>     Feature record: CXX_FEATURE:1cxx_contextual_conversions
>     Feature record: CXX_FEATURE:1cxx_decltype
>     Feature record: CXX_FEATURE:1cxx_decltype_auto
>     Feature record: CXX_FEATURE:1cxx_decltype_incomplete_return_types
>     Feature record: CXX_FEATURE:1cxx_default_function_template_args
>     Feature record: CXX_FEATURE:1cxx_defaulted_functions
>     Feature record: CXX_FEATURE:1cxx_defaulted_move_initializers
>     Feature record: CXX_FEATURE:1cxx_delegating_constructors
>     Feature record: CXX_FEATURE:1cxx_deleted_functions
>     Feature record: CXX_FEATURE:1cxx_digit_separators
>     Feature record: CXX_FEATURE:1cxx_enum_forward_declarations
>     Feature record: CXX_FEATURE:1cxx_explicit_conversions
>     Feature record: CXX_FEATURE:1cxx_extended_friend_declarations
>     Feature record: CXX_FEATURE:1cxx_extern_templates
>     Feature record: CXX_FEATURE:1cxx_final
>     Feature record: CXX_FEATURE:1cxx_func_identifier
>     Feature record: CXX_FEATURE:1cxx_generalized_initializers
>     Feature record: CXX_FEATURE:1cxx_generic_lambdas
>     Feature record: CXX_FEATURE:1cxx_inheriting_constructors
>     Feature record: CXX_FEATURE:1cxx_inline_namespaces
>     Feature record: CXX_FEATURE:1cxx_lambdas
>     Feature record: CXX_FEATURE:1cxx_lambda_init_captures
>     Feature record: CXX_FEATURE:1cxx_local_type_template_args
>     Feature record: CXX_FEATURE:1cxx_long_long_type
>     Feature record: CXX_FEATURE:1cxx_noexcept
>     Feature record: CXX_FEATURE:1cxx_nonstatic_member_init
>     Feature record: CXX_FEATURE:1cxx_nullptr
>     Feature record: CXX_FEATURE:1cxx_override
>     Feature record: CXX_FEATURE:1cxx_range_for
>     Feature record: CXX_FEATURE:1cxx_raw_string_literals
>     Feature record: CXX_FEATURE:1cxx_reference_qualified_functions
>     Feature record: CXX_FEATURE:1cxx_relaxed_constexpr
>     Feature record: CXX_FEATURE:1cxx_return_type_deduction
>     Feature record: CXX_FEATURE:1cxx_right_angle_brackets
>     Feature record: CXX_FEATURE:1cxx_rvalue_references
>     Feature record: CXX_FEATURE:1cxx_sizeof_member
>     Feature record: CXX_FEATURE:1cxx_static_assert
>     Feature record: CXX_FEATURE:1cxx_strong_enums
>     Feature record: CXX_FEATURE:1cxx_template_template_parameters
>     Feature record: CXX_FEATURE:1cxx_thread_local
>     Feature record: CXX_FEATURE:1cxx_trailing_return_types
>     Feature record: CXX_FEATURE:1cxx_unicode_literals
>     Feature record: CXX_FEATURE:1cxx_uniform_initialization
>     Feature record: CXX_FEATURE:1cxx_unrestricted_unions
>     Feature record: CXX_FEATURE:1cxx_user_literals
>     Feature record: CXX_FEATURE:1cxx_variable_templates
>     Feature record: CXX_FEATURE:1cxx_variadic_macros
>     Feature record: CXX_FEATURE:1cxx_variadic_templates
> 
> 
> Detecting CXX [-std=c++11] compiler features compiled with the following output:
> Change Dir: F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp
> 
> Run Build Command:"C:/MinGW/bin/mingw32-make.exe" "cmTC_96a00/fast"
> C:/MinGW/bin/mingw32-make.exe -f CMakeFiles\cmTC_96a00.dir\build.make CMakeFiles/cmTC_96a00.dir/build
> 
> mingw32-make.exe[1]: Entering directory 'F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp'
> 
> Building CXX object CMakeFiles/cmTC_96a00.dir/feature_tests.cxx.obj
> 
> C:\MinGW\bin\mingw32-g++.exe    -std=c++11 -o CMakeFiles\cmTC_96a00.dir\feature_tests.cxx.obj -c F:\URHOTEMPLATEPROJECTMAYBEv2\CMakeFiles\feature_tests.cxx
> 
> Linking CXX executable cmTC_96a00.exe
> 
> "C:\Program Files\CMake\bin\cmake.exe" -E cmake_link_script CMakeFiles\cmTC_96a00.dir\link.txt --verbose=1
> 
> "C:\Program Files\CMake\bin\cmake.exe" -E remove -f CMakeFiles\cmTC_96a00.dir/objects.a
> C:\MinGW\bin\ar.exe cr CMakeFiles\cmTC_96a00.dir/objects.a @CMakeFiles\cmTC_96a00.dir\objects1.rsp
> C:\MinGW\bin\mingw32-g++.exe      -Wl,--whole-archive CMakeFiles\cmTC_96a00.dir/objects.a -Wl,--no-whole-archive  -o cmTC_96a00.exe -Wl,--out-implib,libcmTC_96a00.dll.a -Wl,--major-image-version,0,--minor-image-version,0 @CMakeFiles\cmTC_96a00.dir\linklibs.rsp
> mingw32-make.exe[1]: Leaving directory 'F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp'
> 
> 
> 
>     Feature record: CXX_FEATURE:0cxx_aggregate_default_initializers
>     Feature record: CXX_FEATURE:1cxx_alias_templates
>     Feature record: CXX_FEATURE:1cxx_alignas
>     Feature record: CXX_FEATURE:1cxx_alignof
>     Feature record: CXX_FEATURE:1cxx_attributes
>     Feature record: CXX_FEATURE:0cxx_attribute_deprecated
>     Feature record: CXX_FEATURE:1cxx_auto_type
>     Feature record: CXX_FEATURE:0cxx_binary_literals
>     Feature record: CXX_FEATURE:1cxx_constexpr
>     Feature record: CXX_FEATURE:0cxx_contextual_conversions
>     Feature record: CXX_FEATURE:1cxx_decltype
>     Feature record: CXX_FEATURE:0cxx_decltype_auto
>     Feature record: CXX_FEATURE:1cxx_decltype_incomplete_return_types
>     Feature record: CXX_FEATURE:1cxx_default_function_template_args
>     Feature record: CXX_FEATURE:1cxx_defaulted_functions
>     Feature record: CXX_FEATURE:1cxx_defaulted_move_initializers
>     Feature record: CXX_FEATURE:1cxx_delegating_constructors
>     Feature record: CXX_FEATURE:1cxx_deleted_functions
>     Feature record: CXX_FEATURE:0cxx_digit_separators
>     Feature record: CXX_FEATURE:1cxx_enum_forward_declarations
>     Feature record: CXX_FEATURE:1cxx_explicit_conversions
>     Feature record: CXX_FEATURE:1cxx_extended_friend_declarations
>     Feature record: CXX_FEATURE:1cxx_extern_templates
>     Feature record: CXX_FEATURE:1cxx_final
>     Feature record: CXX_FEATURE:1cxx_func_identifier
>     Feature record: CXX_FEATURE:1cxx_generalized_initializers
>     Feature record: CXX_FEATURE:0cxx_generic_lambdas
>     Feature record: CXX_FEATURE:1cxx_inheriting_constructors
>     Feature record: CXX_FEATURE:1cxx_inline_namespaces
>     Feature record: CXX_FEATURE:1cxx_lambdas
>     Feature record: CXX_FEATURE:0cxx_lambda_init_captures
>     Feature record: CXX_FEATURE:1cxx_local_type_template_args
>     Feature record: CXX_FEATURE:1cxx_long_long_type
>     Feature record: CXX_FEATURE:1cxx_noexcept
>     Feature record: CXX_FEATURE:1cxx_nonstatic_member_init
>     Feature record: CXX_FEATURE:1cxx_nullptr
>     Feature record: CXX_FEATURE:1cxx_override
>     Feature record: CXX_FEATURE:1cxx_range_for
>     Feature record: CXX_FEATURE:1cxx_raw_string_literals
>     Feature record: CXX_FEATURE:1cxx_reference_qualified_functions
>     Feature record: CXX_FEATURE:0cxx_relaxed_constexpr
>     Feature record: CXX_FEATURE:0cxx_return_type_deduction
>     Feature record: CXX_FEATURE:1cxx_right_angle_brackets
>     Feature record: CXX_FEATURE:1cxx_rvalue_references
>     Feature record: CXX_FEATURE:1cxx_sizeof_member
>     Feature record: CXX_FEATURE:1cxx_static_assert
>     Feature record: CXX_FEATURE:1cxx_strong_enums
>     Feature record: CXX_FEATURE:1cxx_template_template_parameters
>     Feature record: CXX_FEATURE:1cxx_thread_local
>     Feature record: CXX_FEATURE:1cxx_trailing_return_types
>     Feature record: CXX_FEATURE:1cxx_unicode_literals
>     Feature record: CXX_FEATURE:1cxx_uniform_initialization
>     Feature record: CXX_FEATURE:1cxx_unrestricted_unions
>     Feature record: CXX_FEATURE:1cxx_user_literals
>     Feature record: CXX_FEATURE:0cxx_variable_templates
>     Feature record: CXX_FEATURE:1cxx_variadic_macros
>     Feature record: CXX_FEATURE:1cxx_variadic_templates
> 
> 
> Detecting CXX [-std=c++98] compiler features compiled with the following output:
> Change Dir: F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp
> 
> Run Build Command:"C:/MinGW/bin/mingw32-make.exe" "cmTC_931f5/fast"
> C:/MinGW/bin/mingw32-make.exe -f CMakeFiles\cmTC_931f5.dir\build.make CMakeFiles/cmTC_931f5.dir/build
> 
> mingw32-make.exe[1]: Entering directory 'F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp'
> 
> Building CXX object CMakeFiles/cmTC_931f5.dir/feature_tests.cxx.obj
> 
> C:\MinGW\bin\mingw32-g++.exe    -std=c++98 -o CMakeFiles\cmTC_931f5.dir\feature_tests.cxx.obj -c F:\URHOTEMPLATEPROJECTMAYBEv2\CMakeFiles\feature_tests.cxx
> 
> Linking CXX executable cmTC_931f5.exe
> 
> "C:\Program Files\CMake\bin\cmake.exe" -E cmake_link_script CMakeFiles\cmTC_931f5.dir\link.txt --verbose=1
> 
> "C:\Program Files\CMake\bin\cmake.exe" -E remove -f CMakeFiles\cmTC_931f5.dir/objects.a
> C:\MinGW\bin\ar.exe cr CMakeFiles\cmTC_931f5.dir/objects.a @CMakeFiles\cmTC_931f5.dir\objects1.rsp
> C:\MinGW\bin\mingw32-g++.exe      -Wl,--whole-archive CMakeFiles\cmTC_931f5.dir/objects.a -Wl,--no-whole-archive  -o cmTC_931f5.exe -Wl,--out-implib,libcmTC_931f5.dll.a -Wl,--major-image-version,0,--minor-image-version,0 @CMakeFiles\cmTC_931f5.dir\linklibs.rsp
> mingw32-make.exe[1]: Leaving directory 'F:/URHOTEMPLATEPROJECTMAYBEv2/CMakeFiles/CMakeTmp'
> 
> 
> 
>     Feature record: CXX_FEATURE:0cxx_aggregate_default_initializers
>     Feature record: CXX_FEATURE:0cxx_alias_templates
>     Feature record: CXX_FEATURE:0cxx_alignas
>     Feature record: CXX_FEATURE:0cxx_alignof
>     Feature record: CXX_FEATURE:0cxx_attributes
>     Feature record: CXX_FEATURE:0cxx_attribute_deprecated
>     Feature record: CXX_FEATURE:0cxx_auto_type
>     Feature record: CXX_FEATURE:0cxx_binary_literals
>     Feature record: CXX_FEATURE:0cxx_constexpr
>     Feature record: CXX_FEATURE:0cxx_contextual_conversions
>     Feature record: CXX_FEATURE:0cxx_decltype
>     Feature record: CXX_FEATURE:0cxx_decltype_auto
>     Feature record: CXX_FEATURE:0cxx_decltype_incomplete_return_types
>     Feature record: CXX_FEATURE:0cxx_default_function_template_args
>     Feature record: CXX_FEATURE:0cxx_defaulted_functions
>     Feature record: CXX_FEATURE:0cxx_defaulted_move_initializers
>     Feature record: CXX_FEATURE:0cxx_delegating_constructors
>     Feature record: CXX_FEATURE:0cxx_deleted_functions
>     Feature record: CXX_FEATURE:0cxx_digit_separators
>     Feature record: CXX_FEATURE:0cxx_enum_forward_declarations
>     Feature record: CXX_FEATURE:0cxx_explicit_conversions
>     Feature record: CXX_FEATURE:0cxx_extended_friend_declarations
>     Feature record: CXX_FEATURE:0cxx_extern_templates
>     Feature record: CXX_FEATURE:0cxx_final
>     Feature record: CXX_FEATURE:0cxx_func_identifier
>     Feature record: CXX_FEATURE:0cxx_generalized_initializers
>     Feature record: CXX_FEATURE:0cxx_generic_lambdas
>     Feature record: CXX_FEATURE:0cxx_inheriting_constructors
>     Feature record: CXX_FEATURE:0cxx_inline_namespaces
>     Feature record: CXX_FEATURE:0cxx_lambdas
>     Feature record: CXX_FEATURE:0cxx_lambda_init_captures
>     Feature record: CXX_FEATURE:0cxx_local_type_template_args
>     Feature record: CXX_FEATURE:0cxx_long_long_type
>     Feature record: CXX_FEATURE:0cxx_noexcept
>     Feature record: CXX_FEATURE:0cxx_nonstatic_member_init
>     Feature record: CXX_FEATURE:0cxx_nullptr
>     Feature record: CXX_FEATURE:0cxx_override
>     Feature record: CXX_FEATURE:0cxx_range_for
>     Feature record: CXX_FEATURE:0cxx_raw_string_literals
>     Feature record: CXX_FEATURE:0cxx_reference_qualified_functions
>     Feature record: CXX_FEATURE:0cxx_relaxed_constexpr
>     Feature record: CXX_FEATURE:0cxx_return_type_deduction
>     Feature record: CXX_FEATURE:0cxx_right_angle_brackets
>     Feature record: CXX_FEATURE:0cxx_rvalue_references
>     Feature record: CXX_FEATURE:0cxx_sizeof_member
>     Feature record: CXX_FEATURE:0cxx_static_assert
>     Feature record: CXX_FEATURE:0cxx_strong_enums
>     Feature record: CXX_FEATURE:1cxx_template_template_parameters
>     Feature record: CXX_FEATURE:0cxx_thread_local
>     Feature record: CXX_FEATURE:0cxx_trailing_return_types
>     Feature record: CXX_FEATURE:0cxx_unicode_literals
>     Feature record: CXX_FEATURE:0cxx_uniform_initialization
>     Feature record: CXX_FEATURE:0cxx_unrestricted_unions
>     Feature record: CXX_FEATURE:0cxx_user_literals
>     Feature record: CXX_FEATURE:0cxx_variable_templates
>     Feature record: CXX_FEATURE:0cxx_variadic_macros
>     Feature record: CXX_FEATURE:0cxx_variadic_templates

-------------------------

Eugene | 2018-03-28 19:38:32 UTC | #14

Have you set this variable (Urho home) to the appropriate directory?
Should be folder with binaries where you generated and built Urho.

-------------------------

Bluemoon | 2018-03-28 19:46:04 UTC | #15

Can you specify your Code::Blocks version for me to try it out on my end?

-------------------------

mldevs | 2018-03-28 20:00:15 UTC | #16

URHO_HOME has been set to F:/URHO3D

-------------------------

mldevs | 2018-03-28 20:00:47 UTC | #17

I'm using both 16.01 and 17.12

-------------------------

Eugene | 2018-03-28 20:35:03 UTC | #18

[quote="mldevs, post:16, topic:4132, full:true"]
URHO_HOME has been set to F:/URHO3D
[/quote]

It doesn't answer my question. I have no idea what do you store in this folder. Is it source or binary (in terms of CMake)? Well... Do you have urho headers in F:/URHO3D/include?

-------------------------

Bluemoon | 2018-03-29 00:14:57 UTC | #19

@mldevs sorry you are encountering this problem. However I've tried to do same over my end with code blocks 16.01 (which is what I have on my system) and everything went well. From what I get from your issue it seems code::blocks can't access your Urho3D "lib" folder. Below is an image from the directory selection page of the Urho3D Project template for code::blocks
![urho_code_blocks|565x473](upload://ivpL1EzSb4LdOpDpZmOeM0Dj8zO.JPG)
According to the helper message, the Urho3D directory selected is that which contains "include" and "lib" directories.

Verify that this is how your setup is.

-------------------------

mldevs | 2018-03-30 06:29:15 UTC | #20

Sorry this is to continue from messages, but I was trying to use .lib files and that probably helped cause an issue there. I am currently rebuilding the entire system

-------------------------

mldevs | 2018-03-30 06:31:51 UTC | #21

Again, to continue from messages, I am running Windows 7, Mingw-w64, and I am building from source again.
Currently as of writing this, I have reinstalled Mingw-64 as 64-bit, to C:/mingw-w64, insead of on F:/mingw-w64, and I have also changed my codeblocks compiler settings, along with change the system PATH and Path variables. Then I restarted my computer. No errors in the config/generate process, and so far at 78% built no errors in the build process, yet.

-------------------------

mldevs | 2018-03-30 20:51:39 UTC | #22

No errors in setting building from source. Examples build without issue. 
And now...
[details=error output]
> ||=== Build: Debug in URHOTESTINGv454545454545454545454 (compiler: MinGW-w64) ===|
> F:\Urho3D-1.7\BUILDIR3\include\Urho3D\Urho3D.h|27|warning: "URHO3D_OPENGL" redefined|
> :0|0|note: this is the location of the previous definition|
> F:\Urho3D-1.7\BUILDIR3\include\Urho3D\Urho3D.h|29|warning: "URHO3D_SSE" redefined|
> :0|0|note: this is the location of the previous definition|
> F:\mingw-w64\i686-7.3.0-posix-dwarf-rt_v5-rev0\mingw32\lib\gcc\i686-w64-mingw32\7.3.0\include\c++\bits\basic_string.h||In function 'long long int std::__cxx11::stoll(const string&, std::size_t*, int)': |
> F:\mingw-w64\i686-7.3.0-posix-dwarf-rt_v5-rev0\mingw32\lib\gcc\i686-w64-mingw32\7.3.0\include\c++\bits\basic_string.h|6375|error: 'strtoll' is not a member of 'std'|
> F:\mingw-w64\i686-7.3.0-posix-dwarf-rt_v5-rev0\mingw32\lib\gcc\i686-w64-mingw32\7.3.0\include\c++\bits\basic_string.h|6375|note: suggested alternative:|
> F:\mingw-w64\i686-7.3.0-posix-dwarf-rt_v5-rev0\mingw32\i686-w64-mingw32\include\stdlib.h|708|note:   'strtoll'|
> F:\mingw-w64\i686-7.3.0-posix-dwarf-rt_v5-rev0\mingw32\lib\gcc\i686-w64-mingw32\7.3.0\include\c++\bits\basic_string.h||In function 'long long unsigned int std::__cxx11::stoull(const string&, std::size_t*, int)': |
> F:\mingw-w64\i686-7.3.0-posix-dwarf-rt_v5-rev0\mingw32\lib\gcc\i686-w64-mingw32\7.3.0\include\c++\bits\basic_string.h|6380|error: 'stroull' is not a member of 'std'|
> F:\mingw-w64\i686-7.3.0-posix-dwarf-rt_v5-rev0\mingw32\lib\gcc\i686-w64-mingw32\7.3.0\include\c++\bits\basic_string.h||In function 'long double std::__cxx11::stold(const string&, std::size_t*)': |
> F:\mingw-w64\i686-7.3.0-posix-dwarf-rt_v5-rev0\mingw32\lib\gcc\i686-w64-mingw32\7.3.0\include\c++\bits\basic_string.h|6394|error: 'strtold' is not a member of 'std'|
> F:\mingw-w64\i686-7.3.0-posix-dwarf-rt_v5-rev0\mingw32\lib\gcc\i686-w64-mingw32\7.3.0\include\c++\bits\basic_string.h|6394|note: suggested alternatives:|
> F:\mingw-w64\i686-7.3.0-posix-dwarf-rt_v5-rev0\mingw32\i686-w64-mingw32\include\stdlib.h|468|note:   'strtold'|
> F:\mingw-w64\i686-7.3.0-posix-dwarf-rt_v5-rev0\mingw32\i686-w64-mingw32\include\stdlib.h|468|note:   'strtold'|
> F:\Urho3D-1.7\BUILDIR3\include\Urho3D\Core\Variant.h||In member function 'bool Urho3D::Variant::operator==(long long unsigned int) const': |
> F:\Urho3D-1.7\BUILDIR3\include\Urho3D\Core\Variant.h|734|warning: comparison between signed and unsigned integer expressions [-Wsign-compare]|
> ||=== Build failed: 3 error(s), 3 warning(s) (0 minute(s), 9 second(s)) ===|
[/details]

This is after building from source without errors, linking to the proper .a file, using the right compiler, and using the "FirsProject" code,

[details="Code"]
>  #include <string>
> #include <sstream>
> 
> #include <Urho3D/Core/CoreEvents.h>
> #include <Urho3D/Engine/Application.h>
> #include <Urho3D/Engine/Engine.h>
> #include <Urho3D/Input/Input.h>
> #include <Urho3D/Input/InputEvents.h>
> #include <Urho3D/Resource/ResourceCache.h>
> #include <Urho3D/Resource/XMLFile.h>
> #include <Urho3D/IO/Log.h>
> #include <Urho3D/UI/UI.h>
> #include <Urho3D/UI/Text.h>
> #include <Urho3D/UI/Font.h>
> #include <Urho3D/UI/Button.h>
> #include <Urho3D/UI/UIEvents.h>
> #include <Urho3D/Scene/Scene.h>
> #include <Urho3D/Scene/SceneEvents.h>
> #include <Urho3D/Graphics/Graphics.h>
> #include <Urho3D/Graphics/Camera.h>
> #include <Urho3D/Graphics/Geometry.h>
> #include <Urho3D/Graphics/Renderer.h>
> #include <Urho3D/Graphics/DebugRenderer.h>
> #include <Urho3D/Graphics/Octree.h>
> #include <Urho3D/Graphics/Light.h>
> #include <Urho3D/Graphics/Model.h>
> #include <Urho3D/Graphics/StaticModel.h>
> #include <Urho3D/Graphics/Material.h>
> #include <Urho3D/Graphics/Skybox.h>
> 
> using namespace Urho3D;
> /**
> * Using the convenient Application API we don't have
> * to worry about initializing the engine or writing a main.
> * You can probably mess around with initializing the engine
> * and running a main manually, but this is convenient and portable.
> */
> class MyApp : public Application
> {
> public:
>     int framecount_;
>     float time_;
>     SharedPtr<Text> text_;
>     SharedPtr<Scene> scene_;
>     SharedPtr<Node> boxNode_;
>     SharedPtr<Node> cameraNode_;
> 
>     /**
>     * This happens before the engine has been initialized
>     * so it's usually minimal code setting defaults for
>     * whatever instance variables you have.
>     * You can also do this in the Setup method.
>     */
>     MyApp(Context * context) : Application(context),framecount_(0),time_(0)
>     {
>     }
> 
>     /**
>     * This method is called before the engine has been initialized.
>     * Thusly, we can setup the engine parameters before anything else
>     * of engine importance happens (such as windows, search paths,
>     * resolution and other things that might be user configurable).
>     */
>     virtual void Setup()
>     {
>         // These parameters should be self-explanatory.
>         // See http://urho3d.github.io/documentation/1.5/_main_loop.html
>         // for a more complete list.
>         engineParameters_["FullScreen"]=false;
>         engineParameters_["WindowWidth"]=1280;
>         engineParameters_["WindowHeight"]=720;
>         engineParameters_["WindowResizable"]=true;
>     }
> 
>     /**
>     * This method is called after the engine has been initialized.
>     * This is where you set up your actual content, such as scenes,
>     * models, controls and what not. Basically, anything that needs
>     * the engine initialized and ready goes in here.
>     */
>     virtual void Start()
>     {
>         // We will be needing to load resources.
>         // All the resources used in this example comes with Urho3D.
>         // If the engine can't find them, check the ResourcePrefixPath (see http://urho3d.github.io/documentation/1.5/_main_loop.html).
>         ResourceCache* cache=GetSubsystem<ResourceCache>();
> 
>         // Let's use the default style that comes with Urho3D.
>         GetSubsystem<UI>()->GetRoot()->SetDefaultStyle(cache->GetResource<XMLFile>("UI/DefaultStyle.xml"));
>         // Let's create some text to display.
>         text_=new Text(context_);
>         // Text will be updated later in the E_UPDATE handler. Keep readin'.
>         text_->SetText("Keys: tab = toggle mouse, AWSD = move camera, Shift = fast mode, Esc = quit.\nWait a bit to see FPS.");
>         // If the engine cannot find the font, it comes with Urho3D.
>         // Set the environment variables URHO3D_HOME, URHO3D_PREFIX_PATH or
>         // change the engine parameter "ResourcePrefixPath" in the Setup method.
>         text_->SetFont(cache->GetResource<Font>("Fonts/Anonymous Pro.ttf"),20);
>         text_->SetColor(Color(.3,0,.3));
>         text_->SetHorizontalAlignment(HA_CENTER);
>         text_->SetVerticalAlignment(VA_TOP);
>         GetSubsystem<UI>()->GetRoot()->AddChild(text_);
>         // Add a button, just as an interactive UI sample.
>         Button* button=new Button(context_);
>         // Note, must be part of the UI system before SetSize calls!
>         GetSubsystem<UI>()->GetRoot()->AddChild(button);
>         button->SetName("Button Quit");
>         button->SetStyle("Button");
>         button->SetSize(32,32);
>         button->SetPosition(16,116);
>         // Subscribe to button release (following a 'press') events
>         SubscribeToEvent(button,E_RELEASED,URHO3D_HANDLER(MyApp,HandleClosePressed));
> 
>         // Let's setup a scene to render.
>         scene_=new Scene(context_);
>         // Let the scene have an Octree component!
>         scene_->CreateComponent<Octree>();
>         // Let's add an additional scene component for fun.
>         scene_->CreateComponent<DebugRenderer>();
> 
>         // Let's put some sky in there.
>         // Again, if the engine can't find these resources you need to check
>         // the "ResourcePrefixPath". These files come with Urho3D.
>         Node* skyNode=scene_->CreateChild("Sky");
>         skyNode->SetScale(500.0f); // The scale actually does not matter
>         Skybox* skybox=skyNode->CreateComponent<Skybox>();
>         skybox->SetModel(cache->GetResource<Model>("Models/Box.mdl"));
>         skybox->SetMaterial(cache->GetResource<Material>("Materials/Skybox.xml"));
> 
>         // Let's put a box in there.
>         boxNode_=scene_->CreateChild("Box");
>         boxNode_->SetPosition(Vector3(0,2,15));
>         boxNode_->SetScale(Vector3(3,3,3));
>         StaticModel* boxObject=boxNode_->CreateComponent<StaticModel>();
>         boxObject->SetModel(cache->GetResource<Model>("Models/Box.mdl"));
>         boxObject->SetMaterial(cache->GetResource<Material>("Materials/Stone.xml"));
>         boxObject->SetCastShadows(true);
> 
>         // Create 400 boxes in a grid.
>         for(int x=-30;x<30;x+=3)
>             for(int z=0;z<60;z+=3)
>             {
>                 Node* boxNode_=scene_->CreateChild("Box");
>                 boxNode_->SetPosition(Vector3(x,-3,z));
>                 boxNode_->SetScale(Vector3(2,2,2));
>                 StaticModel* boxObject=boxNode_->CreateComponent<StaticModel>();
>                 boxObject->SetModel(cache->GetResource<Model>("Models/Box.mdl"));
>                 boxObject->SetMaterial(cache->GetResource<Material>("Materials/Stone.xml"));
>                 boxObject->SetCastShadows(true);
>             }
> 
>         // We need a camera from which the viewport can render.
>         cameraNode_=scene_->CreateChild("Camera");
>         Camera* camera=cameraNode_->CreateComponent<Camera>();
>         camera->SetFarClip(2000);
> 
>         // Create a red directional light (sun)
>         {
>             Node* lightNode=scene_->CreateChild();
>             lightNode->SetDirection(Vector3::FORWARD);
>             lightNode->Yaw(50);     // horizontal
>             lightNode->Pitch(10);   // vertical
>             Light* light=lightNode->CreateComponent<Light>();
>             light->SetLightType(LIGHT_DIRECTIONAL);
>             light->SetBrightness(1.6);
>             light->SetColor(Color(1.0,.6,0.3,1));
>             light->SetCastShadows(true);
>         }
>         // Create a blue point light
>         {
>             Node* lightNode=scene_->CreateChild("Light");
>             lightNode->SetPosition(Vector3(-10,2,5));
>             Light* light=lightNode->CreateComponent<Light>();
>             light->SetLightType(LIGHT_POINT);
>             light->SetRange(25);
>             light->SetBrightness(1.7);
>             light->SetColor(Color(0.5,.5,1.0,1));
>             light->SetCastShadows(true);
>         }
>         // add a green spot light to the camera node
>         {
>             Node* node_light=cameraNode_->CreateChild();
>             Light* light=node_light->CreateComponent<Light>();
>             node_light->Pitch(15);  // point slightly downwards
>             light->SetLightType(LIGHT_SPOT);
>             light->SetRange(20);
>             light->SetColor(Color(.6,1,.6,1.0));
>             light->SetBrightness(2.8);
>             light->SetFov(25);
>         }
> 
>         // Now we setup the viewport. Of course, you can have more than one!
>         Renderer* renderer=GetSubsystem<Renderer>();
>         SharedPtr<Viewport> viewport(new Viewport(context_,scene_,cameraNode_->GetComponent<Camera>()));
>         renderer->SetViewport(0,viewport);
> 
>         // We subscribe to the events we'd like to handle.
>         // In this example we will be showing what most of them do,
>         // but in reality you would only subscribe to the events
>         // you really need to handle.
>         // These are sort of subscribed in the order in which the engine
>         // would send the events. Read each handler method's comment for
>         // details.
>         SubscribeToEvent(E_BEGINFRAME,URHO3D_HANDLER(MyApp,HandleBeginFrame));
>         SubscribeToEvent(E_KEYDOWN,URHO3D_HANDLER(MyApp,HandleKeyDown));
>         SubscribeToEvent(E_UPDATE,URHO3D_HANDLER(MyApp,HandleUpdate));
>         SubscribeToEvent(E_POSTUPDATE,URHO3D_HANDLER(MyApp,HandlePostUpdate));
>         SubscribeToEvent(E_RENDERUPDATE,URHO3D_HANDLER(MyApp,HandleRenderUpdate));
>         SubscribeToEvent(E_POSTRENDERUPDATE,URHO3D_HANDLER(MyApp,HandlePostRenderUpdate));
>         SubscribeToEvent(E_ENDFRAME,URHO3D_HANDLER(MyApp,HandleEndFrame));
>     }
> 
>     /**
>     * Good place to get rid of any system resources that requires the
>     * engine still initialized. You could do the rest in the destructor,
>     * but there's no need, this method will get called when the engine stops,
>     * for whatever reason (short of a segfault).
>     */
>     virtual void Stop()
>     {
>     }
> 
>     /**
>     * Every frame's life must begin somewhere. Here it is.
>     */
>     void HandleBeginFrame(StringHash eventType,VariantMap& eventData)
>     {
>         // We really don't have anything useful to do here for this example.
>         // Probably shouldn't be subscribing to events we don't care about.
>     }
> 
>     /**
>     * Input from keyboard is handled here. I'm assuming that Input, if
>     * available, will be handled before E_UPDATE.
>     */
>     void HandleKeyDown(StringHash eventType,VariantMap& eventData)
>     {
>         using namespace KeyDown;
>         int key=eventData[P_KEY].GetInt();
>         if(key==KEY_ESCAPE)
>             engine_->Exit();
> 
>         if(key==KEY_TAB)    // toggle mouse cursor when pressing tab
>         {
>             GetSubsystem<Input>()->SetMouseVisible(!GetSubsystem<Input>()->IsMouseVisible());
>             GetSubsystem<Input>()->SetMouseGrabbed(!GetSubsystem<Input>()->IsMouseGrabbed());
>         }
>     }
> 
>     /**
>     * You can get these events from when ever the user interacts with the UI.
>     */
>     void HandleClosePressed(StringHash eventType,VariantMap& eventData)
>     {
>         engine_->Exit();
>     }
>     /**
>     * Your non-rendering logic should be handled here.
>     * This could be moving objects, checking collisions and reaction, etc.
>     */
>     void HandleUpdate(StringHash eventType,VariantMap& eventData)
>     {
>         float timeStep=eventData[Update::P_TIMESTEP].GetFloat();
>         framecount_++;
>         time_+=timeStep;
>         // Movement speed as world units per second
>         float MOVE_SPEED=10.0f;
>         // Mouse sensitivity as degrees per pixel
>         const float MOUSE_SENSITIVITY=0.1f;
> 
>         if(time_ >=1)
>         {
>             std::string str;
>             str.append("Keys: tab = toggle mouse, AWSD = move camera, Shift = fast mode, Esc = quit.\n");
>             {
>                 std::ostringstream ss;
>                 ss<<framecount_;
>                 std::string s(ss.str());
>                 str.append(s.substr(0,6));
>             }
>             str.append(" frames in ");
>             {
>                 std::ostringstream ss;
>                 ss<<time_;
>                 std::string s(ss.str());
>                 str.append(s.substr(0,6));
>             }
>             str.append(" seconds = ");
>             {
>                 std::ostringstream ss;
>                 ss<<(float)framecount_/time_;
>                 std::string s(ss.str());
>                 str.append(s.substr(0,6));
>             }
>             str.append(" fps");
>             String s(str.c_str(),str.size());
>             text_->SetText(s);
>             URHO3D_LOGINFO(s);     // this show how to put stuff into the log
>             framecount_=0;
>             time_=0;
>         }
> 
>         // Rotate the box thingy.
>         // A much nicer way of doing this would be with a LogicComponent.
>         // With LogicComponents it is easy to control things like movement
>         // and animation from some IDE, console or just in game.
>         // Alas, it is out of the scope for our simple example.
>         boxNode_->Rotate(Quaternion(8*timeStep,16*timeStep,0));
> 
>         Input* input=GetSubsystem<Input>();
>         if(input->GetQualifierDown(1))  // 1 is shift, 2 is ctrl, 4 is alt
>             MOVE_SPEED*=10;
>         if(input->GetKeyDown('W'))
>             cameraNode_->Translate(Vector3(0,0, 1)*MOVE_SPEED*timeStep);
>         if(input->GetKeyDown('S'))
>             cameraNode_->Translate(Vector3(0,0,-1)*MOVE_SPEED*timeStep);
>         if(input->GetKeyDown('A'))
>             cameraNode_->Translate(Vector3(-1,0,0)*MOVE_SPEED*timeStep);
>         if(input->GetKeyDown('D'))
>             cameraNode_->Translate(Vector3( 1,0,0)*MOVE_SPEED*timeStep);
> 
>         if(!GetSubsystem<Input>()->IsMouseVisible())
>         {
>             // Use this frame's mouse motion to adjust camera node yaw and pitch. Clamp the pitch between -90 and 90 degrees
>             IntVector2 mouseMove=input->GetMouseMove();
>             static float yaw_=0;
>             static float pitch_=0;
>             yaw_+=MOUSE_SENSITIVITY*mouseMove.x_;
>             pitch_+=MOUSE_SENSITIVITY*mouseMove.y_;
>             pitch_=Clamp(pitch_,-90.0f,90.0f);
>             // Reset rotation and set yaw and pitch again
>             cameraNode_->SetDirection(Vector3::FORWARD);
>             cameraNode_->Yaw(yaw_);
>             cameraNode_->Pitch(pitch_);
>         }
>     }
>     /**
>     * Anything in the non-rendering logic that requires a second pass,
>     * it might be well suited to be handled here.
>     */
>     void HandlePostUpdate(StringHash eventType,VariantMap& eventData)
>     {
>         // We really don't have anything useful to do here for this example.
>         // Probably shouldn't be subscribing to events we don't care about.
>     }
>     /**
>     * If you have any details you want to change before the viewport is
>     * rendered, try putting it here.
>     * See http://urho3d.github.io/documentation/1.32/_rendering.html
>     * for details on how the rendering pipeline is setup.
>     */
>     void HandleRenderUpdate(StringHash eventType, VariantMap & eventData)
>     {
>         // We really don't have anything useful to do here for this example.
>         // Probably shouldn't be subscribing to events we don't care about.
>     }
>     /**
>     * After everything is rendered, there might still be things you wish
>     * to add to the rendering. At this point you cannot modify the scene,
>     * only post rendering is allowed. Good for adding things like debug
>     * artifacts on screen or brush up lighting, etc.
>     */
>     void HandlePostRenderUpdate(StringHash eventType, VariantMap & eventData)
>     {
>         // We could draw some debuggy looking thing for the octree.
>         // scene_->GetComponent<Octree>()->DrawDebugGeometry(true);
>     }
>     /**
>     * All good things must come to an end.
>     */
>     void HandleEndFrame(StringHash eventType,VariantMap& eventData)
>     {
>         // We really don't have anything useful to do here for this example.
>         // Probably shouldn't be subscribing to events we don't care about.
>     }
> };
> 
> /**
> * This macro is expanded to (roughly, depending on OS) this:
> *
> * > int RunApplication()
> * > {
> * > Urho3D::SharedPtr<Urho3D::Context> context(new Urho3D::Context());
> * > Urho3D::SharedPtr<className> application(new className(context));
> * > return application->Run();
> * > }
> * >
> * > int main(int argc, char** argv)
> * > {
> * > Urho3D::ParseArguments(argc, argv);
> * > return function;
> * > }
> */
> URHO3D_DEFINE_APPLICATION_MAIN(MyApp)
[/details]

-------------------------

Eugene | 2018-03-30 09:16:23 UTC | #23

Do you use C::B project generator?
If so, are you sure this project has appopriate C++11 settings?
I know, there are some flags that turn C++11 on.

And please, don't post chunks of text here as plain text, it's impossible to navigate. There are pastebin and "hide details", use them.

-------------------------

Bluemoon | 2018-03-30 20:25:21 UTC | #24

@mldevs can you download the current master of [Urho3D Code::Blocks Wizard](https://github.com/BlueMagnificent/Urho3D_CodeBlocks_Wizard) . I made fixes for C++11 to it yesterday

-------------------------

mldevs | 2018-03-30 20:52:33 UTC | #25

That might be an issue as well, I will try again when I get home, though I'm  90% sure I did turn on C++11 flags

-------------------------

mldevs | 2018-03-30 20:52:55 UTC | #26

Hm, okay, thank you, I will try that again.

-------------------------

mldevs | 2018-03-31 06:04:16 UTC | #27

@Bluemoon @Eugene Nothing has helped. I have rebuilt from source yet again today, with C++11 flags for Urho3D on, built and ran the Project Template code, same error with the "TypeInfo" stuff, then I deleted that all and put in the example code, got the same errors again, at least relative to the example code. I genuinely have no idea whats going on. I even turned on C++11 flags in the build options window.

-------------------------

Eugene | 2018-03-31 06:36:34 UTC | #28

I wonder if you have same problem when you generate cb project via cmake. If no, can diff them and check the difference.

-------------------------

Bluemoon | 2018-03-31 08:28:28 UTC | #29

How many versions of Mingw do you have on your system, check if the version pointed to by codeblocks is the same a the one you used in building Urho3D. Equally try out what @Eugene advised about generating codeblocks project via cmake

-------------------------

mldevs | 2018-04-01 05:37:22 UTC | #30

Probably around 5. But I made sure that the build project is set to the Mingw-w64 that I used with CMake

-------------------------

mldevs | 2018-04-01 05:39:10 UTC | #31

What do you mean generate a CB project? Such as making a blank project with a CMakeLists.txt + empty main.cpp or building a CB project with CMake?

-------------------------

mldevs | 2018-04-01 06:14:24 UTC | #32

I have actually discovered a flaw because I did not recheck this. I configured and generated with my Mingw-w64 on my C:/ drive, then built with the one on my F:/ drive, and then continued with that. That will cause issues and such a dumb mistake. Will update after I rebuild it with the Mingw-w64 on the C:/ drive

-------------------------

mldevs | 2018-04-01 07:53:32 UTC | #33

Okay so i have once again rebuilt from source, using the same directory throughout, triple checked it, then I made sure I was using the same directory for the compiler in CB, and I still get undefined reference errors. These I had read would occur from the use of different compilers, but I'm using the exact same compiler for both, so I still have no clue as to whats going on still.

-------------------------

weitjong | 2018-04-01 09:27:14 UTC | #34

IMHO, it does not matter how many times you retries, if you just keep repeating the same steps/mistakes. Besides showing the output of your steps, you have to let us know what exactly are the steps you take so others could reproduce it or could see where you went wrong.

-------------------------

mldevs | 2018-04-01 17:42:25 UTC | #35

I do change things each time. 
Here's a complete list of what I do.
[details="Step List"]

1) Run CMake
2) Open to Urho3D Source Directory, V1.7
3) Change to a new build dir, usually the same but incremented by one, (i.e. dir1, dir2, dir3, etc...)
4) Configure, specifying the native compilers
    -Using the compiler that was setup using the options displayed in the setup tutorial
5) Project configures, I specify path to the CB .exe, and turn on C++11 flag
6)Generate
7)Open CB, open build options of Urho3D project
8) Change the compiler to Mingw-w64
    -Note: Each time I do this I have had to change some aspect of the compiler used, or build options that                didn't match the compiler, or the compiler path in CB. On my last try, everything matched up for a change
9)Project builds without any issue except for about 40 warnings, who cares about those anyway
10) Run the template wizard, choose URHO3D Project, build&run, I get errors that are supposed to relate to mismatched compilers, even though I have made sure they all match up this time around
11) Remove project files, add main.cpp, populate with "First Project" code
12) Build&Run, still fails with same error. Error output below.
[/details]

[details="Error from latest build"]
> ||=== Build: Debug in TestingV565657 (compiler: MinGW-w64) ===|
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Urho3D.h|27|warning: "URHO3D_OPENGL" redefined|
> :0|0|note: this is the location of the previous definition|
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Urho3D.h|29|warning: "URHO3D_SSE" redefined|
> :0|0|note: this is the location of the previous definition|
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Core\Variant.h||In member function 'bool Urho3D::Variant::operator==(long long unsigned int) const': |
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Core\Variant.h|734|warning: comparison between signed and unsigned integer expressions [-Wsign-compare]|
> obj\Debug\main.o||In function `__tcf_2': |
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Engine\Application.h|37|undefined reference to `__ZN6Urho3D8TypeInfoD1Ev'|
> obj\Debug\main.o||In function `__tcf_3': |
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Resource\Resource.h|54|undefined reference to `__ZN6Urho3D8TypeInfoD1Ev'|
> obj\Debug\main.o||In function `__tcf_4': |
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Resource\Resource.h|114|undefined reference to `__ZN6Urho3D8TypeInfoD1Ev'|
> obj\Debug\main.o||In function `__tcf_6': |
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Resource\XMLFile.h|43|undefined reference to `__ZN6Urho3D8TypeInfoD1Ev'|
> obj\Debug\main.o||In function `__tcf_7': |
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Scene\Serializable.h|46|undefined reference to `__ZN6Urho3D8TypeInfoD1Ev'|
> obj\Debug\main.o:F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Scene\Animatable.h|65|more undefined references to `__ZN6Urho3D8TypeInfoD1Ev' follow|
> obj\Debug\main.o||In function `RunApplication()': |
> C:\Users\Matthew\Desktop\BASEFILEHORDE\TestingV565657\main.cpp|393|undefined reference to `___gxx_personality_sj0'|
> C:\Users\Matthew\Desktop\BASEFILEHORDE\TestingV565657\main.cpp|393|undefined reference to `__Unwind_SjLj_Register'|
> C:\Users\Matthew\Desktop\BASEFILEHORDE\TestingV565657\main.cpp|393|undefined reference to `__Znwj'|
> C:\Users\Matthew\Desktop\BASEFILEHORDE\TestingV565657\main.cpp|393|undefined reference to `__ZN6Urho3D7ContextC1Ev'|
> C:\Users\Matthew\Desktop\BASEFILEHORDE\TestingV565657\main.cpp|393|undefined reference to `__Znwj'|
> C:\Users\Matthew\Desktop\BASEFILEHORDE\TestingV565657\main.cpp|393|undefined reference to `__ZN6Urho3D11Application3RunEv'|
> C:\Users\Matthew\Desktop\BASEFILEHORDE\TestingV565657\main.cpp|393|undefined reference to `__ZdlPv'|
> C:\Users\Matthew\Desktop\BASEFILEHORDE\TestingV565657\main.cpp|393|undefined reference to `__Unwind_SjLj_Resume'|
> C:\Users\Matthew\Desktop\BASEFILEHORDE\TestingV565657\main.cpp|393|undefined reference to `__ZdlPv'|
> C:\Users\Matthew\Desktop\BASEFILEHORDE\TestingV565657\main.cpp|393|undefined reference to `__Unwind_SjLj_Resume'|
> C:\Users\Matthew\Desktop\BASEFILEHORDE\TestingV565657\main.cpp|393|undefined reference to `__Unwind_SjLj_Unregister'|
> obj\Debug\main.o||In function `WinMain@16': |
> C:\Users\Matthew\Desktop\BASEFILEHORDE\TestingV565657\main.cpp|393|undefined reference to `__imp__GetCommandLineW@0'|
> C:\Users\Matthew\Desktop\BASEFILEHORDE\TestingV565657\main.cpp|393|undefined reference to `__ZN6Urho3D14ParseArgumentsEPKw'|
> obj\Debug\main.o||In function `__static_initialization_and_destruction_0': |
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Core\CoreEvents.h|31|undefined reference to `__ZN6Urho3D18EventNameRegistrar17RegisterEventNameEPKc'|
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Core\CoreEvents.h|33|undefined reference to `__ZN6Urho3D10StringHashC1EPKc'|
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Core\CoreEvents.h|34|undefined reference to `__ZN6Urho3D10StringHashC1EPKc'|
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Core\CoreEvents.h|38|undefined reference to `__ZN6Urho3D18EventNameRegistrar17RegisterEventNameEPKc'|
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Core\CoreEvents.h|40|undefined reference to `__ZN6Urho3D10StringHashC1EPKc'|
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Core\CoreEvents.h|44|undefined reference to `__ZN6Urho3D18EventNameRegistrar17RegisterEventNameEPKc'|
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Core\CoreEvents.h|46|undefined reference to `__ZN6Urho3D10StringHashC1EPKc'|
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Core\CoreEvents.h|50|undefined reference to `__ZN6Urho3D18EventNameRegistrar17RegisterEventNameEPKc'|
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Core\CoreEvents.h|52|undefined reference to `__ZN6Urho3D10StringHashC1EPKc'|
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Core\CoreEvents.h|56|undefined reference to `__ZN6Urho3D18EventNameRegistrar17RegisterEventNameEPKc'|
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Core\CoreEvents.h|58|undefined reference to `__ZN6Urho3D10StringHashC1EPKc'|
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Core\CoreEvents.h|62|undefined reference to `__ZN6Urho3D18EventNameRegistrar17RegisterEventNameEPKc'|
> obj\Debug\main.o||In function `__static_initialization_and_destruction_0': |
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Input\InputEvents.h|36|undefined reference to `__ZN6Urho3D18EventNameRegistrar17RegisterEventNameEPKc'|
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Input\InputEvents.h|38|undefined reference to `__ZN6Urho3D10StringHashC1EPKc'|
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Input\InputEvents.h|39|undefined reference to `__ZN6Urho3D10StringHashC1EPKc'|
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Input\InputEvents.h|40|undefined reference to `__ZN6Urho3D10StringHashC1EPKc'|
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Input\InputEvents.h|44|undefined reference to `__ZN6Urho3D18EventNameRegistrar17RegisterEventNameEPKc'|
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Input\InputEvents.h|46|undefined reference to `__ZN6Urho3D10StringHashC1EPKc'|
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Input\InputEvents.h|47|undefined reference to `__ZN6Urho3D10StringHashC1EPKc'|
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Input\InputEvents.h|48|undefined reference to `__ZN6Urho3D10StringHashC1EPKc'|
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Input\InputEvents.h|52|undefined reference to `__ZN6Urho3D18EventNameRegistrar17RegisterEventNameEPKc'|
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Input\InputEvents.h|54|undefined reference to `__ZN6Urho3D10StringHashC1EPKc'|
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Input\InputEvents.h|55|undefined reference to `__ZN6Urho3D10StringHashC1EPKc'|
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Input\InputEvents.h|56|undefined reference to `__ZN6Urho3D10StringHashC1EPKc'|
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Input\InputEvents.h|57|undefined reference to `__ZN6Urho3D10StringHashC1EPKc'|
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Input\InputEvents.h|58|undefined reference to `__ZN6Urho3D10StringHashC1EPKc'|
> obj\Debug\main.o:F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Input\InputEvents.h|59|more undefined references to `__ZN6Urho3D10StringHashC1EPKc' follow|
> obj\Debug\main.o||In function `__static_initialization_and_destruction_0': |
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Input\InputEvents.h|63|undefined reference to `__ZN6Urho3D18EventNameRegistrar17RegisterEventNameEPKc'|
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Input\InputEvents.h|65|undefined reference to `__ZN6Urho3D10StringHashC1EPKc'|
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Input\InputEvents.h|66|undefined reference to `__ZN6Urho3D10StringHashC1EPKc'|
> F:\Urho3D-1.7\BUILDIR5\include\Urho3D\Input\InputEvents.h|67|undefined reference to `__ZN6Urho3D10StringHashC1EPKc'|
> ||More errors follow but not being shown.|
> ||Edit the max errors limit in compiler options...|
> ||=== Build failed: 50 error(s), 3 warning(s) (0 minute(s), 12 second(s)) ===|
[/details]

I don't know what more I can tell you, but I have been explaining what I've been doing the whole time, just cutting out the step-by-step and only explaining the changes I have tried.

-------------------------

mldevs | 2018-04-01 17:44:54 UTC | #36

Well, this is an issue on my part. I thought I had changed this compiler on the new project, apparently not. Rebuilding again with the right compiler. I'm pretty mad at myself for goofing that up now. :joy:

-------------------------

Bluemoon | 2018-04-02 17:14:14 UTC | #37

It's good to know its now working for you :+1:

-------------------------

mldevs | 2018-04-02 20:27:17 UTC | #38

Whoops forgot to update, it still isn't working. I have been very thorough this time around. I'm at the point of inviting someone to team viewer in to me and take a look to see if I'm missing anything.

-------------------------

Eugene | 2018-04-02 20:37:25 UTC | #39

Just one more question. Do you have same error when doing this?

[quote="Eugene, post:28, topic:4132"]
I wonder if you have same problem when you generate cb project via cmake
[/quote]

-------------------------

mldevs | 2018-04-03 01:21:43 UTC | #40

Nope, I ran CMake with the same compiler settings, and I was able to configure, generate, build, then run the .exe file without an issue.

[details="CMakeLists.txt"]
cmake_minimum_required (VERSION 2.6)
project (Tutorial)
add_executable(Tutorial main.cpp)
[/details]

[details="main.cpp"]
#include <iostream>

int main()
{
	std::cout<<"Hello world!"<<std::endl;
	std::cout<<"Help..."<<std::endl;
	return 0;
}
[/details]

Then the "Tutorial.exe" appeared after I built, and it has no issue, all witht eh same compilers that I use to build Urho3D

-------------------------

Eugene | 2018-04-03 08:26:43 UTC | #41

[quote="mldevs, post:40, topic:4132"]
Nope, I ran CMake with the same compiler settings, and I was able to configure, generate, build, then run the .exe file without an issue
[/quote]
I mean, project that uses Urho.
I know, you had some issues there. They didn't look serious tho.

-------------------------

mldevs | 2018-04-03 20:53:32 UTC | #42


[details="Error Message From CMake"]
    CMake Deprecation Warning at CMakeLists.txt:22 (cmake_policy):
      The OLD behavior for policy CMP0026 will be removed from a future version
      of CMake.

      The cmake-policies(7) manual explains that the OLD behaviors of all
      policies are deprecated and that a policy should be set to OLD only under
      specific short-term circumstances.  Projects should be ported to the NEW
      behavior and not rely on setting a policy to OLD.


    CMake Error at CMake/Modules/FindUrho3D.cmake:346 (message):
      Could NOT find compatible Urho3D library in Urho3D SDK installation or
      build tree.  Use URHO3D_HOME environment variable or build option to
      specify the location of the non-default SDK installation or build tree.
      Change Dir: F:/TestingV2/BUILD2/CMakeFiles/CMakeTmp

      

      Run Build
      Command:"C:/mingw-w64/x86_64-6.2.0-posix-seh-rt_v5-rev1/mingw64/bin/mingw32-make.exe"
      "cmTC_94f91/fast"

      
      C:/mingw-w64/x86_64-6.2.0-posix-seh-rt_v5-rev1/mingw64/bin/mingw32-make.exe
      -f CMakeFiles\cmTC_94f91.dir\build.make CMakeFiles/cmTC_94f91.dir/build


      mingw32-make.exe[1]: Entering directory
      'F:/TestingV2/BUILD2/CMakeFiles/CMakeTmp'


      Building CXX object CMakeFiles/cmTC_94f91.dir/CheckUrhoLibrary.cpp.obj


      C:\mingw-w64\x86_64-6.2.0-posix-seh-rt_v5-rev1\mingw64\bin\g++.exe
      @CMakeFiles/cmTC_94f91.dir/includes_CXX.rsp -m32 -O3 -DNDEBUG -o
      CMakeFiles\cmTC_94f91.dir\CheckUrhoLibrary.cpp.obj -c
      F:\TestingV2\CMake\Modules\CheckUrhoLibrary.cpp


      In file included from
      C:/mingw-w64/x86_64-6.2.0-posix-seh-rt_v5-rev1/mingw64/lib/gcc/x86_64-w64-mingw32/6.2.0/include/c++/ext/string_conversions.h:41:0,



                       from C:/mingw-w64/x86_64-6.2.0-posix-seh-rt_v5-rev1/mingw64/lib/gcc/x86_64-w64-mingw32/6.2.0/include/c++/bits/basic_string.h:5402,

                       from C:/mingw-w64/x86_64-6.2.0-posix-seh-rt_v5-rev1/mingw64/lib/gcc/x86_64-w64-mingw32/6.2.0/include/c++/string:52,

                       from C:/mingw-w64/x86_64-6.2.0-posix-seh-rt_v5-rev1/mingw64/lib/gcc/x86_64-w64-mingw32/6.2.0/include/c++/bits/locale_classes.h:40,

                       from C:/mingw-w64/x86_64-6.2.0-posix-seh-rt_v5-rev1/mingw64/lib/gcc/x86_64-w64-mingw32/6.2.0/include/c++/bits/ios_base.h:41,

                       from C:/mingw-w64/x86_64-6.2.0-posix-seh-rt_v5-rev1/mingw64/lib/gcc/x86_64-w64-mingw32/6.2.0/include/c++/ios:42,

                       from C:/mingw-w64/x86_64-6.2.0-posix-seh-rt_v5-rev1/mingw64/lib/gcc/x86_64-w64-mingw32/6.2.0/include/c++/ostream:38,

                       from C:/mingw-w64/x86_64-6.2.0-posix-seh-rt_v5-rev1/mingw64/lib/gcc/x86_64-w64-mingw32/6.2.0/include/c++/iostream:39,

                       from F:\TestingV2\CMake\Modules\CheckUrhoLibrary.cpp:24:


      
      C:/mingw-w64/x86_64-6.2.0-posix-seh-rt_v5-rev1/mingw64/lib/gcc/x86_64-w64-mingw32/6.2.0/include/c++/cstdlib:248:11:
      error: '::strtoll' has not been declared


         using ::strtoll;

                 ^~~~~~~


      
      C:/mingw-w64/x86_64-6.2.0-posix-seh-rt_v5-rev1/mingw64/lib/gcc/x86_64-w64-mingw32/6.2.0/include/c++/cstdlib:249:11:
      error: '::strtoull' has not been declared


         using ::strtoull;

                 ^~~~~~~~


      
      C:/mingw-w64/x86_64-6.2.0-posix-seh-rt_v5-rev1/mingw64/lib/gcc/x86_64-w64-mingw32/6.2.0/include/c++/cstdlib:270:22:
      error: '__gnu_cxx::strtoll' has not been declared


         using ::__gnu_cxx::strtoll;

                            ^~~~~~~


      
      C:/mingw-w64/x86_64-6.2.0-posix-seh-rt_v5-rev1/mingw64/lib/gcc/x86_64-w64-mingw32/6.2.0/include/c++/cstdlib:271:22:
      error: '__gnu_cxx::strtoull' has not been declared


         using ::__gnu_cxx::strtoull;

                            ^~~~~~~~


      In file included from
      C:/mingw-w64/x86_64-6.2.0-posix-seh-rt_v5-rev1/mingw64/lib/gcc/x86_64-w64-mingw32/6.2.0/include/c++/string:52:0,



                       from C:/mingw-w64/x86_64-6.2.0-posix-seh-rt_v5-rev1/mingw64/lib/gcc/x86_64-w64-mingw32/6.2.0/include/c++/bits/locale_classes.h:40,

                       from C:/mingw-w64/x86_64-6.2.0-posix-seh-rt_v5-rev1/mingw64/lib/gcc/x86_64-w64-mingw32/6.2.0/include/c++/bits/ios_base.h:41,

                       from C:/mingw-w64/x86_64-6.2.0-posix-seh-rt_v5-rev1/mingw64/lib/gcc/x86_64-w64-mingw32/6.2.0/include/c++/ios:42,

                       from C:/mingw-w64/x86_64-6.2.0-posix-seh-rt_v5-rev1/mingw64/lib/gcc/x86_64-w64-mingw32/6.2.0/include/c++/ostream:38,

                       from C:/mingw-w64/x86_64-6.2.0-posix-seh-rt_v5-rev1/mingw64/lib/gcc/x86_64-w64-mingw32/6.2.0/include/c++/iostream:39,

                       from F:\TestingV2\CMake\Modules\CheckUrhoLibrary.cpp:24:


      
      C:/mingw-w64/x86_64-6.2.0-posix-seh-rt_v5-rev1/mingw64/lib/gcc/x86_64-w64-mingw32/6.2.0/include/c++/bits/basic_string.h:
      In function 'long long int std::__cxx11::stoll(const string&, std::size_t*,
      int)':


      
      C:/mingw-w64/x86_64-6.2.0-posix-seh-rt_v5-rev1/mingw64/lib/gcc/x86_64-w64-mingw32/6.2.0/include/c++/bits/basic_string.h:5428:31:
      error: 'strtoll' is not a member of 'std'


         { return __gnu_cxx::__stoa(&std::strtoll, "stoll", __str.c_str(),

                                     ^~~


      
      C:/mingw-w64/x86_64-6.2.0-posix-seh-rt_v5-rev1/mingw64/lib/gcc/x86_64-w64-mingw32/6.2.0/include/c++/bits/basic_string.h:
      In function 'long long unsigned int std::__cxx11::stoull(const string&,
      std::size_t*, int)':


      
      C:/mingw-w64/x86_64-6.2.0-posix-seh-rt_v5-rev1/mingw64/lib/gcc/x86_64-w64-mingw32/6.2.0/include/c++/bits/basic_string.h:5433:31:
      error: 'strtoull' is not a member of 'std'


         { return __gnu_cxx::__stoa(&std::strtoull, "stoull", __str.c_str(),

                                     ^~~


      CMakeFiles\cmTC_94f91.dir\build.make:65: recipe for target
      'CMakeFiles/cmTC_94f91.dir/CheckUrhoLibrary.cpp.obj' failed


      mingw32-make.exe[1]: ***
      [CMakeFiles/cmTC_94f91.dir/CheckUrhoLibrary.cpp.obj] Error 1


      mingw32-make.exe[1]: Leaving directory
      'F:/TestingV2/BUILD2/CMakeFiles/CMakeTmp'


      Makefile:125: recipe for target 'cmTC_94f91/fast' failed


      mingw32-make.exe: *** [cmTC_94f91/fast] Error 2


    Call Stack (most recent call first):
      CMake/Modules/UrhoCommon.cmake:231 (find_package)
      CMakeLists.txt:30 (include)


    Configuring incomplete, errors occurred!
    See also "F:/TestingV2/BUILD2/CMakeFiles/CMakeOutput.log".
[/details]
This was a similar message I was getting before

-------------------------

mldevs | 2018-04-07 15:35:01 UTC | #43

Update: Solved
All it was, was a compiler flag set to x86 when I had built for x64. Solved by @Bluemoon after going through their project wizard. So if anyone else finds they keep getting odd errors, make sure your flags match up with the Urho3D architecture :joy:
Thank you to everyone that took time to look into the issue

-------------------------

