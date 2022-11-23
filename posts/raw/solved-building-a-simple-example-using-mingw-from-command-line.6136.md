8Observer8 | 2021-02-18 14:03:37 UTC | #1

I have MinGW on Windows. I downloaded Urho3D-1.7.1-MinGW-STATIC and I placed the "include" and "lib" folders here:
- E:\Libs\Urho3D-1.7.1-MinGW-STATIC\include
- E:\Libs\Urho3D-1.7.1-MinGW-STATIC\lib\Urho3D

The "lib\Urho3D" folder contains the "libUrho3D.a" file.

I wrote a very simple example with minimal code to show that it compiles and works:

```
#include <iostream>
#include <Urho3D/Engine/Application.h>

class MyApp : public Urho3D::Application
{
public:
    MyApp(Urho3D::Context * context) : Urho3D::Application(context)
    {
    }

    virtual void Setup()
    {
        std::cout << "Setup" << std::endl;
    }
};

URHO3D_DEFINE_APPLICATION_MAIN(MyApp)
```

I try to compile it using this command:

> g++ main.cpp -I"E:\Libs\Urho3D-1.7.1-MinGW-STATIC\include" -L"E:\Libs\Urho3D-1.7.1-MinGW-STATIC\lib\Urho3D" -lUrho3D -o app.exe

I see a lot of errors like:
> E:\Libs\Urho3D-1.7.1-MinGW-STATIC\lib\Urho3D/libUrho3D.a(SDL_winmm.c.obj):SDL_winmm.c:(.text+0x942): undefined reference to `_imp__waveOutGetNumDevs@0'                                                                                                                                                   

> E:\Libs\Urho3D-1.7.1-MinGW-STATIC\lib\Urho3D/libUrho3D.a(SDL_winmm.c.obj):SDL_winmm.c:(.text+0x97b): undefined reference to `_imp__waveOutGetDevCapsW@12'                                                                                                                                                 

> E:\Libs\Urho3D-1.7.1-MinGW-STATIC\lib\Urho3D/libUrho3D.a(SDL_winmm.c.obj):SDL_winmm.c:(.text+0xa32): undefined reference to `_imp__waveInAddBuffer@12'

-------------------------

8Observer8 | 2020-05-02 13:46:37 UTC | #2

I added this key `-lwinmm` and I do not see the error message related to `SDL_winmm.c` above.

What key do I need to solve this error:

> E:\Libs\Urho3D-1.7.1-MinGW-STATIC\lib\Urho3D/libUrho3D.a(SDL_windowsframebuffer.c.obj):SDL_windowsframebuffer.c:(.text+0x38a): undefined reference to `_imp__DeleteObject@4'

-------------------------

SirNate0 | 2020-05-02 15:07:45 UTC | #3

I would strongly suggest using CMake to get all the build flags correct. If you wish to switch over to just the command line after that you can just run make with VERBOSE=1 and see what the actual commands to compile the project were.

Also, welcome to the community!

-------------------------

jmiller | 2021-07-23 15:43:35 UTC | #4

Welcome to the community!

I can offer some minor notes..
Building from the [master](https://github.com/urho3d/Urho3D) branch on github is frequently recommended as it maintains good stability, and there have been a number of fixes since last release.

Possibly helpful to MingW users,
[details="Here is a bit of code I was using in my app header to target MSW under MinGW and limit global namespace pollution and conflicts with Urho methods."]

```
#pragma once
// Somewhat limit windows header namespace pollution.

#ifdef _WIN32
#define WIN32_LEAN_AND_MEAN
#define NOSERVICE
#define NOMCX
#define NOIME
#define NONLS
#include <windows.h>
#undef CreateDirectory
#undef GetClassName
#undef GetProp
#undef RemoveProp
#undef SetProp
#endif
```
[/details]

S.L.C offers a more sophisticated method:
https://discourse.urho3d.io/t/solved-building-a-simple-example-using-mingw-from-command-line/6136/21

-------------------------

8Observer8 | 2020-05-02 19:21:34 UTC | #5

Thank you, guys!

My steps:

1. I downloaded a source from the [master](https://github.com/urho3d/Urho3D) branch.
2. I run CMake GUI.
3. I selected "MinGW Makefiles" and "Use default native compilers"
4. I choose the "source" and "dist" folders.
5. I pressed the "Configure" button. There are some warnings at the beginning that I do not understand:
<details> 
  <summary>Output</summary>
Urho3D-master

CMake Deprecation Warning at CMakeLists.txt:31 (cmake_policy):
  The OLD behavior for policy CMP0026 will be removed from a future version
  of CMake.

  The cmake-policies(7) manual explains that the OLD behaviors of all
  policies are deprecated and that a policy should be set to OLD only under
  specific short-term circumstances.  Projects should be ported to the NEW
  behavior and not rely on setting a policy to OLD.


CMake Deprecation Warning at CMakeLists.txt:35 (cmake_policy):
  The OLD behavior for policy CMP0063 will be removed from a future version
  of CMake.

  The cmake-policies(7) manual explains that the OLD behaviors of all
  policies are deprecated and that a policy should be set to OLD only under
  specific short-term circumstances.  Projects should be ported to the NEW
  behavior and not rely on setting a policy to OLD.


The C compiler identification is GNU 8.1.0
The CXX compiler identification is GNU 8.1.0
Check for working C compiler: C:/Program Files (x86)/mingw-w64/i686-8.1.0-win32-dwarf-rt_v6-rev0/mingw32/bin/gcc.exe
Check for working C compiler: C:/Program Files (x86)/mingw-w64/i686-8.1.0-win32-dwarf-rt_v6-rev0/mingw32/bin/gcc.exe - works
Detecting C compiler ABI info
Detecting C compiler ABI info - done
Detecting C compile features
Detecting C compile features - done
Check for working CXX compiler: C:/Program Files (x86)/mingw-w64/i686-8.1.0-win32-dwarf-rt_v6-rev0/mingw32/bin/g++.exe
Check for working CXX compiler: C:/Program Files (x86)/mingw-w64/i686-8.1.0-win32-dwarf-rt_v6-rev0/mingw32/bin/g++.exe - works
Detecting CXX compiler ABI info
Detecting CXX compiler ABI info - done
Detecting CXX compile features
Detecting CXX compile features - done
Performing Test IS_TRIVIALLY_DEFAULT_CONSTRUCTIBLE
Performing Test IS_TRIVIALLY_DEFAULT_CONSTRUCTIBLE - Success
Performing Test IS_TRIVIALLY_DESTRUCTIBLE
Performing Test IS_TRIVIALLY_DESTRUCTIBLE - Success
Performing Test IS_TRIVIALLY_COPY_ASSIGNABLE
Performing Test IS_TRIVIALLY_COPY_ASSIGNABLE - Success
Performing Test IS_TRIVIALLY_COPY_CONSTRUCTIBLE
Performing Test IS_TRIVIALLY_COPY_CONSTRUCTIBLE - Success
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
Looking for include files windows.h, xinput.h
Looking for include files windows.h, xinput.h - found
Performing Test HAVE_XINPUT_GAMEPAD_EX
Performing Test HAVE_XINPUT_GAMEPAD_EX - Failed
Performing Test HAVE_XINPUT_STATE_EX
Performing Test HAVE_XINPUT_STATE_EX - Failed
Found DirectX: TRUE  found components: DInput DSound XInput 
Looking for stdint.h
Looking for stdint.h - found
Looking for inttypes.h
Looking for inttypes.h - found
Looking for malloc.h
Looking for malloc.h - found
Looking for __sincosf
Looking for __sincosf - not found
Looking for malloc_usable_size
Looking for malloc_usable_size - not found
Looking for sincosf in m
Looking for sincosf in m - found
Performing Test HAVE_RTL_OSVERSIONINFOW
Performing Test HAVE_RTL_OSVERSIONINFOW - Success
Performing Test HAVE_GCC_WALL
Performing Test HAVE_GCC_WALL - Success
Performing Test HAVE_GCC_NO_STRICT_ALIASING
Performing Test HAVE_GCC_NO_STRICT_ALIASING - Success
Performing Test HAVE_GCC_WDECLARATION_AFTER_STATEMENT
Performing Test HAVE_GCC_WDECLARATION_AFTER_STATEMENT - Success
Performing Test HAVE_GCC_WERROR_DECLARATION_AFTER_STATEMENT
Performing Test HAVE_GCC_WERROR_DECLARATION_AFTER_STATEMENT - Success
Performing Test HAVE_GCC_ATOMICS
Performing Test HAVE_GCC_ATOMICS - Success
Performing Test HAVE_GCC_PREFERRED_STACK_BOUNDARY
Performing Test HAVE_GCC_PREFERRED_STACK_BOUNDARY - Success
Performing Test HAVE_GCC_WSHADOW
Performing Test HAVE_GCC_WSHADOW - Success
Performing Test HAVE_NO_UNDEFINED
Performing Test HAVE_NO_UNDEFINED - Success
Looking for immintrin.h
Looking for immintrin.h - found
Looking for sys/types.h
Looking for sys/types.h - found
Looking for stdio.h
Looking for stdio.h - found
Looking for stdlib.h
Looking for stdlib.h - found
Looking for stddef.h
Looking for stddef.h - found
Looking for stdarg.h
Looking for stdarg.h - found
Looking for memory.h
Looking for memory.h - found
Looking for string.h
Looking for string.h - found
Looking for limits.h
Looking for limits.h - found
Looking for strings.h
Looking for strings.h - found
Looking for wchar.h
Looking for wchar.h - found
Looking for ctype.h
Looking for ctype.h - found
Looking for math.h
Looking for math.h - found
Looking for iconv.h
Looking for iconv.h - found
Looking for signal.h
Looking for signal.h - found
Looking for 7 include files stdint.h, ..., float.h
Looking for 7 include files stdint.h, ..., float.h - found
Looking for M_PI
Looking for M_PI - found
Looking for sys/mman.h
Looking for sys/mman.h - not found
Looking for strtod
Looking for strtod - found
Looking for malloc
Looking for malloc - found
Looking for calloc
Looking for calloc - found
Looking for realloc
Looking for realloc - found
Looking for free
Looking for free - found
Looking for getenv
Looking for getenv - found
Looking for setenv
Looking for setenv - not found
Looking for putenv
Looking for putenv - found
Looking for unsetenv
Looking for unsetenv - not found
Looking for qsort
Looking for qsort - found
Looking for abs
Looking for abs - found
Looking for bcopy
Looking for bcopy - not found
Looking for memset
Looking for memset - found
Looking for memcpy
Looking for memcpy - found
Looking for memmove
Looking for memmove - found
Looking for memcmp
Looking for memcmp - found
Looking for strlen
Looking for strlen - found
Looking for strlcpy
Looking for strlcpy - not found
Looking for strlcat
Looking for strlcat - not found
Looking for _strrev
Looking for _strrev - found
Looking for _strupr
Looking for _strupr - found
Looking for _strlwr
Looking for _strlwr - found
Looking for strchr
Looking for strchr - found
Looking for strrchr
Looking for strrchr - found
Looking for strstr
Looking for strstr - found
Looking for itoa
Looking for itoa - found
Looking for _ltoa
Looking for _ltoa - found
Looking for _uitoa
Looking for _uitoa - not found
Looking for _ultoa
Looking for _ultoa - found
Looking for strtol
Looking for strtol - found
Looking for strtoul
Looking for strtoul - found
Looking for _i64toa
Looking for _i64toa - found
Looking for _ui64toa
Looking for _ui64toa - found
Looking for strtoll
Looking for strtoll - found
Looking for strtoull
Looking for strtoull - found
Looking for atoi
Looking for atoi - found
Looking for atof
Looking for atof - found
Looking for strcmp
Looking for strcmp - found
Looking for strncmp
Looking for strncmp - found
Looking for _stricmp
Looking for _stricmp - found
Looking for strcasecmp
Looking for strcasecmp - found
Looking for _strnicmp
Looking for _strnicmp - found
Looking for strncasecmp
Looking for strncasecmp - found
Looking for vsscanf
Looking for vsscanf - found
Looking for vsnprintf
Looking for vsnprintf - found
Looking for fopen64
Looking for fopen64 - found
Looking for fseeko
Looking for fseeko - found
Looking for fseeko64
Looking for fseeko64 - found
Looking for sigaction
Looking for sigaction - not found
Looking for setjmp
Looking for setjmp - not found
Looking for nanosleep
Looking for nanosleep - not found
Looking for sysconf
Looking for sysconf - not found
Looking for sysctlbyname
Looking for sysctlbyname - not found
Looking for getauxval
Looking for getauxval - not found
Looking for poll
Looking for poll - not found
Looking for _Exit
Looking for _Exit - found
Looking for pow in m
Looking for pow in m - found
Looking for atan
Looking for atan - found
Looking for atan2
Looking for atan2 - found
Looking for ceil
Looking for ceil - found
Looking for copysign
Looking for copysign - found
Looking for cos
Looking for cos - found
Looking for cosf
Looking for cosf - found
Looking for fabs
Looking for fabs - found
Looking for floor
Looking for floor - found
Looking for log
Looking for log - found
Looking for pow
Looking for pow - found
Looking for scalbn
Looking for scalbn - found
Looking for sin
Looking for sin - found
Looking for sinf
Looking for sinf - found
Looking for sqrt
Looking for sqrt - found
Looking for sqrtf
Looking for sqrtf - found
Looking for tan
Looking for tan - found
Looking for tanf
Looking for tanf - found
Looking for acos
Looking for acos - found
Looking for asin
Looking for asin - found
Looking for iconv_open in iconv
Looking for iconv_open in iconv - not found
Looking for alloca.h
Looking for alloca.h - not found
Performing Test HAVE_SA_SIGACTION
Performing Test HAVE_SA_SIGACTION - Failed
Looking for windows.h
Looking for windows.h - found
Looking for mmdeviceapi.h
Looking for mmdeviceapi.h - found
Looking for audioclient.h
Looking for audioclient.h - found
Looking for endpointvolume.h
Looking for endpointvolume.h - found

SDL2 was configured with the following options:

Platform: Windows-10.0.18362
64-bit:   FALSE
Compiler: C:/Program Files (x86)/mingw-w64/i686-8.1.0-win32-dwarf-rt_v6-rev0/mingw32/bin/gcc.exe

Subsystems:
  Atomic:     ON
  Audio:      ON
  Video:      ON
  Render:     OFF
  Events:     ON
  Joystick:   ON
  Haptic:     ON
  Power:      ON
  Threads:    ON
  Timers:     ON
  File:       ON
  Loadso:     ON
  CPUinfo:    ON
  Filesystem: ON
  Dlopen:     OFF
  Sensor:     ON

Options:
  ALSA                   (Wanted: OFF): OFF
  ALSA_SHARED            (Wanted: OFF): OFF
  ARTS                   (Wanted: OFF): OFF
  ARTS_SHARED            (Wanted: OFF): OFF
  ASSEMBLY               (Wanted: ON): ON
  ASSERTIONS             (Wanted: auto): auto
  BACKGROUNDING_SIGNAL   (Wanted: OFF): OFF
  CLOCK_GETTIME          (Wanted: OFF): OFF
  DIRECTFB_SHARED        (Wanted: OFF): OFF
  DIRECTX                (Wanted: ON): ON
  DISKAUDIO              (Wanted: ON): ON
  DUMMYAUDIO             (Wanted: ON): ON
  ESD                    (Wanted: OFF): OFF
  ESD_SHARED             (Wanted: OFF): OFF
  FOREGROUNDING_SIGNAL   (Wanted: OFF): OFF
  FUSIONSOUND            (Wanted: OFF): OFF
  FUSIONSOUND_SHARED     (Wanted: OFF): OFF
  GCC_ATOMICS            (Wanted: ON): ON
  HIDAPI                 (Wanted: ON): ON
  INPUT_TSLIB            (Wanted: OFF): OFF
  JACK                   (Wanted: OFF): OFF
  JACK_SHARED            (Wanted: OFF): OFF
  KMSDRM_SHARED          (Wanted: OFF): OFF
  LIBC                   (Wanted: ON): ON
  LIBSAMPLERATE          (Wanted: OFF): OFF
  LIBSAMPLERATE_SHARED   (Wanted: OFF): OFF
  NAS                    (Wanted: OFF): OFF
  NAS_SHARED             (Wanted: OFF): OFF
  OSS                    (Wanted: OFF): OFF
  PTHREADS               (Wanted: OFF): OFF
  PTHREADS_SEM           (Wanted: OFF): OFF
  PULSEAUDIO             (Wanted: OFF): OFF
  PULSEAUDIO_SHARED      (Wanted: OFF): OFF
  SDL_DLOPEN             (Wanted: OFF): OFF
  SDL_HAPTIC             (Wanted: ON): ON
  SDL_STATIC_PIC         (Wanted: OFF): OFF
  SNDIO                  (Wanted: OFF): OFF
  VIDEO_COCOA            (Wanted: OFF): OFF
  VIDEO_DIRECTFB         (Wanted: OFF): OFF
  VIDEO_DUMMY            (Wanted: ON): ON
  VIDEO_KMSDRM           (Wanted: OFF): OFF
  VIDEO_OPENGL           (Wanted: ON): ON
  VIDEO_OPENGLES         (Wanted: OFF): OFF
  VIDEO_RPI              (Wanted: OFF): OFF
  VIDEO_VIVANTE          (Wanted: OFF): OFF
  VIDEO_VULKAN           (Wanted: ON): ON
  VIDEO_WAYLAND          (Wanted: OFF): OFF
  VIDEO_WAYLAND_QT_TOUCH (Wanted: OFF): OFF
  VIDEO_X11              (Wanted: OFF): OFF
  VIDEO_X11_XCURSOR      (Wanted: OFF): OFF
  VIDEO_X11_XINERAMA     (Wanted: OFF): OFF
  VIDEO_X11_XINPUT       (Wanted: OFF): OFF
  VIDEO_X11_XRANDR       (Wanted: OFF): OFF
  VIDEO_X11_XSCRNSAVER   (Wanted: OFF): OFF
  VIDEO_X11_XSHAPE       (Wanted: OFF): OFF
  VIDEO_X11_XVM          (Wanted: OFF): OFF
  WASAPI                 (Wanted: ON): OFF
  WAYLAND_SHARED         (Wanted: OFF): OFF
  X11_SHARED             (Wanted: OFF): OFF

 CFLAGS:        -mtune=generic  -march=native -msse3 -static -static-libgcc -fno-keep-inline-dllexport -mstackrealign -fdiagnostics-color=auto  -IC:/Users/8Observer8/Downloads/Urho3D-master/Source/ThirdParty/SDL/src/hidapi/hidapi
 EXTRA_CFLAGS:  -Wshadow -Wdeclaration-after-statement -Werror=declaration-after-statement -fno-strict-aliasing -Wall 
 EXTRA_LDFLAGS: -Wl,--no-undefined
 EXTRA_LIBS:    m;user32;gdi32;winmm;imm32;ole32;oleaut32;version;uuid;advapi32;setupapi;shell32;dinput8;dxerr8

Performing Test HAVE_STRUCT_TIMESPEC_TV_SEC
Performing Test HAVE_STRUCT_TIMESPEC_TV_SEC - Success
Looking for _TIMESPEC_DEFINED
Looking for _TIMESPEC_DEFINED - found
Performing Test INET_FUNCTIONS_EXISTS_1
Performing Test INET_FUNCTIONS_EXISTS_1 - Failed
Performing Test INET_FUNCTIONS_EXISTS_2
Performing Test INET_FUNCTIONS_EXISTS_2 - Failed
Performing Test SPRINTFS_FUNCTION_EXISTS
Performing Test SPRINTFS_FUNCTION_EXISTS - Success
Performing Test VSNPRINTFS_FUNCTION_EXISTS
Performing Test VSNPRINTFS_FUNCTION_EXISTS - Success
Looking for include file stdint.h
Looking for include file stdint.h - found
Performing Test IK_RESTRICT_restrict
Performing Test IK_RESTRICT_restrict - Success
Performing Test COMPILER_HAS_DEPRECATED_ATTR
Performing Test COMPILER_HAS_DEPRECATED_ATTR - Success
Found Urho3D: as CMake target
CMake Warning (dev) at C:/Program Files (x86)/CMake/share/cmake-3.17/Modules/FindPackageHandleStandardArgs.cmake:272 (message):
  The package name passed to `find_package_handle_standard_args` (rt) does
  not match the name of the calling package (RT).  This can lead to problems
  in calling code that expects `find_package` result variables (e.g.,
  `_FOUND`) to follow a certain pattern.
Call Stack (most recent call first):
  Source/ThirdParty/Assimp/cmake-modules/FindRT.cmake:19 (find_package_handle_standard_args)
  Source/ThirdParty/Assimp/code/CMakeLists.txt:854 (FIND_PACKAGE)
This warning is for project developers.  Use -Wno-dev to suppress it.

Could NOT find rt (missing: RT_LIBRARY) 
RT-extension not found. glTF import/export will be built without Open3DGC-compression.
Could NOT find Doxygen (missing: DOXYGEN_EXECUTABLE) 
Configuring done </details>

6. I just unchecked some Assimp Importers. I pressed the "Configure" button again.
7. I pressed the "Generate" button.
8. I went to the "dist" folder and I run the "mingw32-make" command.
9. Even EXE's for examples was created successfully.
10. I have the "include" folder and the "libUrho3d.a" library. I think it must be enough to build a simple program:
<details>
<summary>main.cpp</summary>

```
#include <iostream>
#include <Urho3D/Engine/Application.h>

class MyApp : public Urho3D::Application
{
public:
    MyApp(Urho3D::Context * context) : Urho3D::Application(context)
    {
    }

    virtual void Setup()
    {
        std::cout << "Setup" << std::endl;
    }
};

URHO3D_DEFINE_APPLICATION_MAIN(MyApp)

```
</detals>

-------------------------

8Observer8 | 2020-05-02 19:27:59 UTC | #6

11. I run the command:

> g++ -Wall -g -std=c++11 main.cpp -I"C:\Users\8Observer8\Downloads\Urho3D-master\dist\include" -L"C:\Users\8Observer8\Downloads\Urho3D-master\dist\lib" -lUrho3D -lkernel32 -luser32 -lgdi32 -lwinspool -lshell32 -lole32 -loleaut32 -luuid -lcomdlg32 -lwinmm -limm32 -lversion -lws2_32 -ldbghelp -ld3dcompiler -ld3d11 -ldxgi -ldxguid -o app.exe

12. This is the whole output:

<details>
<summary>Output</summary>
C:\Users\8OBSER~1\AppData\Local\Temp\ccCo3yPo.o: In function `_tcf_2':
C:/Users/8Observer8/Downloads/Urho3D-master/dist/include/Urho3D/Engine/Application.h:37: undefined reference to `_imp___ZN6Urho3D8TypeInfoD1Ev'
C:\Users\8OBSER~1\AppData\Local\Temp\ccCo3yPo.o: In function `Z14RunApplicationv':
E:\_Projects\C++\urho3d\hello-world-urho3d-cpp/main.cpp:17: undefined reference to `_imp___ZN6Urho3D7ContextC1Ev'
E:\_Projects\C++\urho3d\hello-world-urho3d-cpp/main.cpp:17: undefined reference to `_imp___ZN6Urho3D11Application3RunEv'        
C:\Users\8OBSER~1\AppData\Local\Temp\ccCo3yPo.o: In function `WinMain@16':
E:\_Projects\C++\urho3d\hello-world-urho3d-cpp/main.cpp:17: undefined reference to `_imp___ZN6Urho3D14ParseArgumentsEPKw'
C:\Users\8OBSER~1\AppData\Local\Temp\ccCo3yPo.o: In function `ZN6Urho3D7VariantD1Ev':
C:/Users/8Observer8/Downloads/Urho3D-master/dist/include/Urho3D/Core/Variant.h:556: undefined reference to `_imp___ZN6Urho3D7Variant7SetTypeENS_11VariantTypeE'
C:\Users\8OBSER~1\AppData\Local\Temp\ccCo3yPo.o: In function `ZN6Urho3D11Application17GetTypeInfoStaticEv':
C:/Users/8Observer8/Downloads/Urho3D-master/dist/include/Urho3D/Engine/Application.h:37: undefined reference to `_imp___ZN6Urho3D8TypeInfoC1EPKcPKS0_'
C:\Users\8OBSER~1\AppData\Local\Temp\ccCo3yPo.o: In function `ZN6Urho3D11ApplicationD2Ev':
C:/Users/8Observer8/Downloads/Urho3D-master/dist/include/Urho3D/Engine/Application.h:35: undefined reference to `_imp___ZTVN6Urho3D11ApplicationE'
C:/Users/8Observer8/Downloads/Urho3D-master/dist/include/Urho3D/Engine/Application.h:35: undefined reference to `_imp___ZN6Urho3D6ObjectD2Ev'
C:\Users\8OBSER~1\AppData\Local\Temp\ccCo3yPo.o: In function `ZN6Urho3D11ApplicationD1Ev':
C:/Users/8Observer8/Downloads/Urho3D-master/dist/include/Urho3D/Engine/Application.h:35: undefined reference to `_imp___ZTVN6Urho3D11ApplicationE'
C:/Users/8Observer8/Downloads/Urho3D-master/dist/include/Urho3D/Engine/Application.h:35: undefined reference to `_imp___ZN6Urho3D6ObjectD2Ev'
C:\Users\8OBSER~1\AppData\Local\Temp\ccCo3yPo.o: In function `ZN5MyAppC1EPN6Urho3D7ContextE':
E:\_Projects\C++\urho3d\hello-world-urho3d-cpp/main.cpp:7: undefined reference to `_imp___ZN6Urho3D11ApplicationC2EPNS_7ContextE'
C:\Users\8OBSER~1\AppData\Local\Temp\ccCo3yPo.o: In function `ZN6Urho3D7HashMapINS_10StringHashENS_7VariantEED1Ev':
C:/Users/8Observer8/Downloads/Urho3D-master/dist/include/Urho3D/Container/HashMap.h:256: undefined reference to `_imp___ZN6Urho3D21AllocatorUninitializeEPNS_14AllocatorBlockE'
C:\Users\8OBSER~1\AppData\Local\Temp\ccCo3yPo.o: In function `ZN6Urho3D7HashMapINS_10StringHashENS_7VariantEE5ClearEv':
C:/Users/8Observer8/Downloads/Urho3D-master/dist/include/Urho3D/Container/HashMap.h:463: undefined reference to `_imp___ZN6Urho3D8HashBase9ResetPtrsEv'
C:\Users\8OBSER~1\AppData\Local\Temp\ccCo3yPo.o: In function `ZN6Urho3D7HashMapINS_10StringHashENS_7VariantEE8FreeNodeEPNS3_4NodeE':
C:/Users/8Observer8/Downloads/Urho3D-master/dist/include/Urho3D/Container/HashMap.h:762: undefined reference to `_imp___ZN6Urho3D13AllocatorFreeEPNS_14AllocatorBlockEPv'
C:\Users\8OBSER~1\AppData\Local\Temp\ccCo3yPo.o: In function `ZN6Urho3D9SharedPtrINS_6EngineEE10ReleaseRefEv':
C:/Users/8Observer8/Downloads/Urho3D-master/dist/include/Urho3D/Container/Ptr.h:237: undefined reference to `_imp___ZN6Urho3D10RefCounted10ReleaseRefEv'
C:\Users\8OBSER~1\AppData\Local\Temp\ccCo3yPo.o: In function `ZN6Urho3D9SharedPtrINS_7ContextEE6AddRefEv':
C:/Users/8Observer8/Downloads/Urho3D-master/dist/include/Urho3D/Container/Ptr.h:229: undefined reference to `_imp___ZN6Urho3D10RefCounted6AddRefEv'
C:\Users\8OBSER~1\AppData\Local\Temp\ccCo3yPo.o: In function `ZN6Urho3D9SharedPtrINS_7ContextEE10ReleaseRefEv':
C:/Users/8Observer8/Downloads/Urho3D-master/dist/include/Urho3D/Container/Ptr.h:237: undefined reference to `_imp___ZN6Urho3D10RefCounted10ReleaseRefEv'
C:\Users\8OBSER~1\AppData\Local\Temp\ccCo3yPo.o: In function `ZN6Urho3D9SharedPtrI5MyAppE6AddRefEv':
C:/Users/8Observer8/Downloads/Urho3D-master/dist/include/Urho3D/Container/Ptr.h:229: undefined reference to `_imp___ZN6Urho3D10RefCounted6AddRefEv'
C:\Users\8OBSER~1\AppData\Local\Temp\ccCo3yPo.o: In function `ZN6Urho3D9SharedPtrI5MyAppE10ReleaseRefEv':
C:/Users/8Observer8/Downloads/Urho3D-master/dist/include/Urho3D/Container/Ptr.h:237: undefined reference to `_imp___ZN6Urho3D10RefCounted10ReleaseRefEv'
C:\Users\8Observer8\Downloads\Urho3D-master\dist\lib/libUrho3D.a(hid.c.obj):hid.c:(.text+0x3cb): undefined reference to `_imp__SetupDiGetClassDevsA@16'
C:\Users\8Observer8\Downloads\Urho3D-master\dist\lib/libUrho3D.a(hid.c.obj):hid.c:(.text+0x408): undefined reference to `_imp__SetupDiEnumDeviceInterfaces@20'
C:\Users\8Observer8\Downloads\Urho3D-master\dist\lib/libUrho3D.a(hid.c.obj):hid.c:(.text+0x440): undefined reference to `_imp__SetupDiGetDeviceInterfaceDetailA@24'
C:\Users\8Observer8\Downloads\Urho3D-master\dist\lib/libUrho3D.a(hid.c.obj):hid.c:(.text+0x480): undefined reference to `_imp__SetupDiGetDeviceInterfaceDetailA@24'
C:\Users\8Observer8\Downloads\Urho3D-master\dist\lib/libUrho3D.a(hid.c.obj):hid.c:(.text+0x4a0): undefined reference to `_imp__SetupDiEnumDeviceInfo@12'
C:\Users\8Observer8\Downloads\Urho3D-master\dist\lib/libUrho3D.a(hid.c.obj):hid.c:(.text+0x4c7): undefined reference to `_imp__SetupDiGetDeviceRegistryPropertyA@28'
C:\Users\8Observer8\Downloads\Urho3D-master\dist\lib/libUrho3D.a(hid.c.obj):hid.c:(.text+0x525): undefined reference to `_imp__SetupDiDestroyDeviceInfoList@4'
collect2.exe: error: ld returned 1 exit status</details>

-------------------------

8Observer8 | 2020-05-02 19:32:04 UTC | #7

For example, I use a similar command for building apps with the SFML library. This command works correctly:

> g++ main.cpp -I"E:\Libs\SFML\SFML-2.5.1-windows-gcc-7.3.0-mingw-32-bit\SFML-2.5.1\include" -L"E:\Libs\SFML\SFML-2.5.1-windows-gcc-7.3.0-mingw-32-bit\SFML-2.5.1\lib" -lsfml-graphics -lsfml-window -lsfml-system -o hero.exe

-------------------------

8Observer8 | 2020-05-02 19:35:07 UTC | #8

Maybe do I use incorrect keys? Where can I find correct keys?

-------------------------

8Observer8 | 2020-05-02 19:52:20 UTC | #9

[quote="8Observer8, post:6, topic:6136"]
SetupDiGetDeviceInterfaceDetail
[/quote]
This problem was solved using this key: `-lSetupapi`

But what key will solve this problem:

> C:/Users/8Observer8/Downloads/Urho3D-master/dist/include/Urho3D/Engine/Application.h:37: undefined reference to `_imp___ZN6Urho3D8TypeInfoD1Ev'

-------------------------

8Observer8 | 2020-05-02 19:59:29 UTC | #10

This command:

> g++ -Wall -g -std=c++11 main.cpp -I"C:\Users\8Observer8\Downloads\Urho3D-master\dist\include" -L"C:\Users\8Observer8\Downloads\Urho3D-master\dist\lib" -lUrho3D -lkernel32 -luser32 -lgdi32 -lwinspool -lshell32 -lole32 -loleaut32 -luuid -lcomdlg32 -lwinmm -limm32 -lversion -lws2_32 -ldbghelp -ld3dcompiler -ld3d11 -ldxgi -ldxguid -lSetupapi -o app.exe

gives me these errors:

`
C:\Users\8OBSER~1\AppData\Local\Temp\ccirz7RL.o: In function `_tcf_2':
C:/Users/8Observer8/Downloads/Urho3D-master/dist/include/Urho3D/Engine/Application.h:37: undefined reference to `_imp___ZN6Urho3D8TypeInfoD1Ev'
C:\Users\8OBSER~1\AppData\Local\Temp\ccirz7RL.o: In function `Z14RunApplicationv':
E:\_Projects\C++\urho3d\hello-world-urho3d-cpp/main.cpp:18: undefined reference to `_imp___ZN6Urho3D7ContextC1Ev'
E:\_Projects\C++\urho3d\hello-world-urho3d-cpp/main.cpp:18: undefined reference to `_imp___ZN6Urho3D11Application3RunEv'        
C:\Users\8OBSER~1\AppData\Local\Temp\ccirz7RL.o: In function `WinMain@16':
E:\_Projects\C++\urho3d\hello-world-urho3d-cpp/main.cpp:18: undefined reference to `_imp___ZN6Urho3D14ParseArgumentsEPKw'
C:\Users\8OBSER~1\AppData\Local\Temp\ccirz7RL.o: In function `ZN6Urho3D7VariantD1Ev':
C:/Users/8Observer8/Downloads/Urho3D-master/dist/include/Urho3D/Core/Variant.h:556: undefined reference to `_imp___ZN6Urho3D7Variant7SetTypeENS_11VariantTypeE'
C:\Users\8OBSER~1\AppData\Local\Temp\ccirz7RL.o: In function `ZN6Urho3D11Application17GetTypeInfoStaticEv':
C:/Users/8Observer8/Downloads/Urho3D-master/dist/include/Urho3D/Engine/Application.h:37: undefined reference to `_imp___ZN6Urho3D8TypeInfoC1EPKcPKS0_'
C:\Users\8OBSER~1\AppData\Local\Temp\ccirz7RL.o: In function `ZN6Urho3D11ApplicationD2Ev':
C:/Users/8Observer8/Downloads/Urho3D-master/dist/include/Urho3D/Engine/Application.h:35: undefined reference to `_imp___ZTVN6Urho3D11ApplicationE'
C:/Users/8Observer8/Downloads/Urho3D-master/dist/include/Urho3D/Engine/Application.h:35: undefined reference to `_imp___ZN6Urho3D6ObjectD2Ev'
C:\Users\8OBSER~1\AppData\Local\Temp\ccirz7RL.o: In function `ZN6Urho3D11ApplicationD1Ev':
C:/Users/8Observer8/Downloads/Urho3D-master/dist/include/Urho3D/Engine/Application.h:35: undefined reference to `_imp___ZTVN6Urho3D11ApplicationE'
C:/Users/8Observer8/Downloads/Urho3D-master/dist/include/Urho3D/Engine/Application.h:35: undefined reference to `_imp___ZN6Urho3D6ObjectD2Ev'
C:\Users\8OBSER~1\AppData\Local\Temp\ccirz7RL.o: In function `ZN5MyAppC1EPN6Urho3D7ContextE':
E:\_Projects\C++\urho3d\hello-world-urho3d-cpp/main.cpp:8: undefined reference to `_imp___ZN6Urho3D11ApplicationC2EPNS_7ContextE'
C:\Users\8OBSER~1\AppData\Local\Temp\ccirz7RL.o: In function `ZN6Urho3D7HashMapINS_10StringHashENS_7VariantEED1Ev':
C:/Users/8Observer8/Downloads/Urho3D-master/dist/include/Urho3D/Container/HashMap.h:256: undefined reference to `_imp___ZN6Urho3D21AllocatorUninitializeEPNS_14AllocatorBlockE'
C:\Users\8OBSER~1\AppData\Local\Temp\ccirz7RL.o: In function `ZN6Urho3D7HashMapINS_10StringHashENS_7VariantEE5ClearEv':
C:/Users/8Observer8/Downloads/Urho3D-master/dist/include/Urho3D/Container/HashMap.h:463: undefined reference to `_imp___ZN6Urho3D8HashBase9ResetPtrsEv'
C:\Users\8OBSER~1\AppData\Local\Temp\ccirz7RL.o: In function `ZN6Urho3D7HashMapINS_10StringHashENS_7VariantEE8FreeNodeEPNS3_4NodeE':
C:/Users/8Observer8/Downloads/Urho3D-master/dist/include/Urho3D/Container/HashMap.h:762: undefined reference to `_imp___ZN6Urho3D13AllocatorFreeEPNS_14AllocatorBlockEPv'
C:\Users\8OBSER~1\AppData\Local\Temp\ccirz7RL.o: In function `ZN6Urho3D9SharedPtrINS_6EngineEE10ReleaseRefEv':
C:/Users/8Observer8/Downloads/Urho3D-master/dist/include/Urho3D/Container/Ptr.h:237: undefined reference to `_imp___ZN6Urho3D10RefCounted10ReleaseRefEv'
C:\Users\8OBSER~1\AppData\Local\Temp\ccirz7RL.o: In function `ZN6Urho3D9SharedPtrINS_7ContextEE6AddRefEv':
C:/Users/8Observer8/Downloads/Urho3D-master/dist/include/Urho3D/Container/Ptr.h:229: undefined reference to `_imp___ZN6Urho3D10RefCounted6AddRefEv'
C:\Users\8OBSER~1\AppData\Local\Temp\ccirz7RL.o: In function `ZN6Urho3D9SharedPtrINS_7ContextEE10ReleaseRefEv':
C:/Users/8Observer8/Downloads/Urho3D-master/dist/include/Urho3D/Container/Ptr.h:237: undefined reference to `_imp___ZN6Urho3D10RefCounted10ReleaseRefEv'
C:\Users\8OBSER~1\AppData\Local\Temp\ccirz7RL.o: In function `ZN6Urho3D9SharedPtrI5MyAppE6AddRefEv':
C:/Users/8Observer8/Downloads/Urho3D-master/dist/include/Urho3D/Container/Ptr.h:229: undefined reference to `_imp___ZN6Urho3D10RefCounted6AddRefEv'
C:\Users\8OBSER~1\AppData\Local\Temp\ccirz7RL.o: In function `ZN6Urho3D9SharedPtrI5MyAppE10ReleaseRefEv':
C:/Users/8Observer8/Downloads/Urho3D-master/dist/include/Urho3D/Container/Ptr.h:237: undefined reference to `_imp___ZN6Urho3D10RefCounted10ReleaseRefEv'
collect2.exe: error: ld returned 1 exit status
`

-------------------------

Lys0gen | 2020-05-02 20:19:31 UTC | #11

Looks like it can't find the libUrho3D.a, are you sure you're linking to the correct folder?

-------------------------

8Observer8 | 2020-05-02 20:41:14 UTC | #12

When I break the path:

> g++ -Wall -g -std=c++11 main.cpp -I"C:\Users\8Observer8\Downloads\Urho3D-master\dist\include" -L"C:\Users\8Observer8\Downloads\Urho3D-master\dist" -lUrho3D -lkernel32 -luser32 -lgdi32 -lwinspool -lshell32 
-lole32 -loleaut32 -luuid -lcomdlg32 -lSetupapi -ladvapi32 -lwinmm -limm32 -lversion -lws2_32 -ldbghelp -lopengl32 -o app.exe

I get this:

`
C:/Program Files (x86)/mingw-w64/i686-8.1.0-win32-dwarf-rt_v6-rev0/mingw32/bin/../lib/gcc/i686-w64-mingw32/8.1.0/../../../../i686-w64-mingw32/bin/ld.exe: cannot find -lUrho3D
collect2.exe: error: ld returned 1 exit status
`

-------------------------

SirNate0 | 2020-05-02 20:59:45 UTC | #13

As I suggested before, run the make command verbosely and see the actual commands used to compile something, let's say one of the samples. I think you're missing some of the flags, but I can't tell you just from looking at then which will be needed.

From your CMake output:
```
CFLAGS: -mtune=generic -march=native -msse3 -static -static-libgcc -fno-keep-inline-dllexport -mstackrealign -fdiagnostics-color=auto -IC:/Users/8Observer8/Downloads/Urho3D-master/Source/ThirdParty/SDL/src/hidapi/hidapi
EXTRA_CFLAGS: -Wshadow -Wdeclaration-after-statement -Werror=declaration-after-statement -fno-strict-aliasing -Wall
EXTRA_LDFLAGS: -Wl,–no-undefined
EXTRA_LIBS: m;user32;gdi32;winmm;imm32;ole32;oleaut32;version;uuid;advapi32;setupapi;shell32;dinput8;dxerr8
```

-------------------------

8Observer8 | 2020-05-03 02:22:15 UTC | #14

I did not understand you before. Now I understand that I need to run the next command and I will try it later:

> mingw32-make VERBOSE=1

The build command above works with "shared" version of Urho. I downloaded [Urho3D-1.7.1-MinGW-SHARED](https://sourceforge.net/projects/urho3d/files/Urho3D/). When I run the command:

> g++ -Wall -g -std=c++11 main.cpp -I"C:\Users\8Observer8\Downloads\Urho3D-1.7.1-MinGW-SHARED\include" -L"C:\Users\8Observer8\Downloads\Urho3D-1.7.1-MinGW-SHARED\lib\Urho3D" -lUrho3D -lkernel32 -luser32 -lgdi32 -lwinspool -lshell32 -lole32 -loleaut32 -luuid -lcomdlg32 -lSetupapi -ladvapi32 -lwinmm -limm32 -lversion -lws2_32 -ldbghelp -lopengl32 -o app.exe

I get "app.exe". But I get this warning after compilation:

<details>
<summary>Output</summary>
`
In file included from C:/Users/8Observer8/Downloads/Urho3D-1.7.1-MinGW-SHARED/include/Urho3D/Core/Attribute.h:26,
                 from C:/Users/8Observer8/Downloads/Urho3D-1.7.1-MinGW-SHARED/include/Urho3D/Core/Context.h:26,
                 from C:\Users\8Observer8\Downloads\Urho3D-1.7.1-MinGW-SHARED\include/Urho3D/Engine/Application.h:25,
                 from main.cpp:2:
C:/Users/8Observer8/Downloads/Urho3D-1.7.1-MinGW-SHARED/include/Urho3D/Core/Variant.h: In member function 'bool Urho3D::Variant::operator==(long long unsigned int) const':
C:/Users/8Observer8/Downloads/Urho3D-1.7.1-MinGW-SHARED/include/Urho3D/Core/Variant.h:734:141: warning: comparison of integer expressions of different signedness: 'const long long unsigned int' and 'int' [-Wsign-compare]
     bool operator ==(unsigned long long rhs) const { return type_ == VAR_INT64 ? *reinterpret_cast<const unsigned long long*>(&value_.int_) == (int)rhs : false; }
`
</details>

I copied the "Urho3D.dll" from the folder:
- C:\Users\8Observer8\Downloads\Urho3D-1.7.1-MinGW-SHARED\bin

to

- C:\Windows\SysWOW64

I run "app.exe" and It works! I read [here](https://discourse.urho3d.io/t/solved-error-failed-to-add-resource-path-data/579) that I need to add "Data" and "CoreDate".

<details>
<summary>main.cpp</summary>

```
// #include <Urho3D/Urho3D.h>
#include <Urho3D/Engine/Application.h>
#include <iostream>

class MyApp : public Urho3D::Application
{
public:
    MyApp(Urho3D::Context * context) : Urho3D::Application(context)
    {
    }

    virtual void Setup()
    {
        std::cout << "Setup" << std::endl;
    }
};

URHO3D_DEFINE_APPLICATION_MAIN(MyApp)
```
</details>

<details>
<summary>Output</summary>

* Setup                                                                                                                                                
* [Sun May 03 02:10:36 2020] INFO: Opened log file Urho3D.log                                                                                          
* [Sun May 03 02:10:36 2020] INFO: Created 1 worker thread                                                                                             
* [Sun May 03 02:10:36 2020] INFO: Added resource path E:/_Projects/C++/urho3d/hello-world-urho3d-cpp/Data/                                            [Sun May 03 02:10:36 2020] INFO: Added resource path E:/_Projects/C++/urho3d/hello-world-urho3d-cpp/CoreData/                                        
* [Sun May 03 02:10:43 2020] INFO: Set screen mode 1366x768 fullscreen monitor 0                                                                       
* [Sun May 03 02:10:43 2020] INFO: Initialized input                                                                                                   
* [Sun May 03 02:10:43 2020] INFO: Initialized user interface                                                                                          
* [Sun May 03 02:10:43 2020] ERROR: Could not find resource Textures/Ramp.png                                                                          
* [Sun May 03 02:10:43 2020] ERROR: Could not find resource Textures/Spot.png                                                                          
* [Sun May 03 02:10:43 2020] ERROR: Could not find resource Techniques/NoTexture.xml                                                                   
* [Sun May 03 02:10:43 2020] ERROR: Could not find resource RenderPaths/Forward.xml                                                                    
* [Sun May 03 02:10:43 2020] INFO: Initialized renderer                                                                                                
* [Sun May 03 02:10:43 2020] INFO: Set audio mode 44100 Hz stereo interpolated                                                                         
* [Sun May 03 02:10:43 2020] INFO: Initialized engine 
</detals>

-------------------------

8Observer8 | 2020-05-02 22:27:47 UTC | #15

It is time to study and practice with Urho. I will try to compile statically an example later. Thank you, guys!

-------------------------

SirNate0 | 2020-05-03 00:06:17 UTC | #16

Glad you got it working! To fix those errors make sure you have the necessary files in either Data or CoreData (they should be in `bin/*Data/`

Other than that, the only thing I would recommend is that you use Urho's log macros (in IO/Log.h) rather than std::cout in general so that the redirection to a file and such will all be handled uniformly.

-------------------------

8Observer8 | 2020-05-13 21:46:10 UTC | #17

I will save my Makefile for the future. Maybe it will useful for beginners. If you want to use VSCode install the [C/C++ for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools) plugin. Press Ctrl+Shift+P and select `C/C++: Edit Configurations (UI)`. Open the `.vscode/c_cpp_properties.json` file and include path to the Urho3D include folder:

```
            "includePath": [
                "${workspaceFolder}/**",
                "E:/Libs/Urho3D-1.7.1-MinGW-SHARED/include"
            ],
```

Makefile

```

CC = g++

INC = -I"E:\Libs\Urho3D-1.7.1-MinGW-SHARED\include"

LIB = -L"E:\Libs\Urho3D-1.7.1-MinGW-SHARED\lib\Urho3D"

FLAGS = -c

all: main.o
	$(CC) main.o -Wall -g -std=c++11 $(LIB) -lUrho3D -lkernel32 -luser32 -lgdi32 -lwinspool -lshell32 -lole32 -loleaut32 -luuid -lcomdlg32 -lSetupapi -ladvapi32 -lwinmm -limm32 -lversion -lws2_32 -ldbghelp -lopengl32 -o app

main.o: main.cpp
	$(CC) main.cpp $(FLAGS) $(INC)
```
Create a minimal file:

main.cpp

```
#include <Urho3D/Engine/Application.h>
#include <iostream>

class MyApp : public Urho3D::Application
{
public:
    MyApp(Urho3D::Context * context) : Urho3D::Application(context)
    {
    }

    virtual void Setup()
    {
        std::cout << "Setup" << std::endl;
    }
};

URHO3D_DEFINE_APPLICATION_MAIN(MyApp)
```

Build the project: `mingw32-make`

-------------------------

8Observer8 | 2021-02-16 15:09:41 UTC | #18

My step-by-step tutorial for beginners: [[Tutorial] How to set up Urho3D (Shared, MinGW) in Qt Creator IDE](https://discourse.urho3d.io/t/tutorial-how-to-set-up-urho3d-shared-mingw-in-qt-creator-ide/6715)

-------------------------

8Observer8 | 2021-07-21 15:01:23 UTC | #19

[quote="Lys0gen, post:11, topic:6136, full:true"]
Looks like it can’t find the libUrho3D.a, are you sure you’re linking to the correct folder?
[/quote]
I tried to build Urho3D statically from source using CMake and MinGW32 but it is really looks like it cannot find the libUrho3D.a. Because I tried to delete "-lUrho3D" from settings and I get 21 errors like:

![image|444x159](upload://wslFD5L5UYJQMmEIc7TgE43ozwK.png)

My settings:

```
CONFIG += c++11

INCLUDEPATH += "C:\Users\8Observer8\Downloads\Urho3D-1.7.1\dist\include"

LIBS += -L"C:\Users\8Observer8\Downloads\Urho3D-1.7.1\dist\lib"

LIBS += -lUrho3D -lkernel32 -luser32 -lgdi32 -lwinspool -lshell32 -lole32 -loleaut32 -luuid -lcomdlg32 -ladvapi32

LIBS += -ldbghelp -limm32 -lversion -lwinmm -lws2_32

SOURCES += \
    main.cpp

```

-------------------------

8Observer8 | 2021-07-21 15:06:21 UTC | #20

I want to mention that if I delete -lUrho3D I get 21 errors and if I do not delete -lUrho3D from settings above I get the same 21 errors in any case. This path is correct: ```C:\Users\8Observer8\Downloads\Urho3D-1.7.1\dist\lib```:

![image|375x100](upload://9JwHi4q0k3MajRc9HIRowYMdnbG.png)

-------------------------

S.L.C | 2021-07-22 03:12:54 UTC | #21

Since MinGW is just GCC you could `#pragma push` those macros in case you need them later. You probably don't but a mere suggestion.

```
#if defined (__MINGW32__) || defined (__MINGW64__)
#pragma push_macro("CreateDirectory")
#endif
#undef CreateDirectory
//...
```
And later if you need one:
```
#pragma pop_macro("CreateDirectory")
```
Although this probably complicates things more than it should :laughing:
Reason I included this suggestion is in case you do it in a global header.

-------------------------

Bluemoon | 2021-07-22 12:06:04 UTC | #22

By Building from source do you mean using the supplied urho3d build setup?

-------------------------

8Observer8 | 2021-07-22 14:29:31 UTC | #23

I downloaded the Urho3D-1.7.1 archive here: ```https://github.com/urho3d/Urho3D/releases``` I used CMake-GUI to configure and generate a project. And I use the ```mingw32-make``` command to make ```libUrho3D.a```.

These are my settings. I just deleted some importers:

![image|384x500](upload://oQvRMTPYVb29v9ZhDcKYVPn2vPK.png)

![image|384x500](upload://2Lxgq77ZYjP6cAZKiweMKGY5ppQ.png)

![image|384x500](upload://gwNhHs09TNnqEHPBjjDYJxMcV3i.png)

![image|384x500](upload://xQXQFRRNWbaoPljysGFCQ6gY1Sq.png)

![image|384x500](upload://7SGwSjVkn94H1mjvSdsxaMUiYz0.png)

![image|384x500](upload://lBMXeVTzCmzfEFrqd6Q6Q55gL2Y.png)

![image|384x500](upload://gbLYETlNLnLNgGk4RCSuqDyWRmx.png)

-------------------------

Bluemoon | 2021-07-22 14:33:31 UTC | #24

Ok. I assume from this stage you go ahead to click  the "Generate" button.

After it is done generating your build files, you navigate to your build directory and through CMD run

> mingw32-make -f makefile install

Was that your procedure?

-------------------------

8Observer8 | 2021-07-22 14:40:02 UTC | #25

[quote="Bluemoon, post:24, topic:6136"]
you go ahead to click the “Generate” button.
[/quote]
Yes, I clicked the Generate button. I opened the "dist" folder and opened CMD in the "dist" folder. I wrote the "mingw32-make" command. After 10 minutes of successful building I got libUrho3D.a in the folder: ```C:\Users\8Observer8\Downloads\Urho3D-1.7.1\dist\lib```

-------------------------

8Observer8 | 2021-07-22 14:38:38 UTC | #26

[quote="Bluemoon, post:24, topic:6136"]
mingw32-make -f makefile install
[/quote]

I will try this command.

-------------------------

Bluemoon | 2021-07-22 14:42:10 UTC | #27

To use the command

> mingw32-make -f makefile install

ensure that your properly set the value for CMAKE_INSTALL_PREFIX, it should be the directory you want Urho3D to be installed in

-------------------------

8Observer8 | 2021-07-22 14:48:56 UTC | #28

I think I must to run CMD as Admin:

![image|596x320](upload://aQvaO2hnUEFxyfaoUHrbh5s5Q4z.png)

-------------------------

8Observer8 | 2021-07-22 15:09:57 UTC | #29

[quote="Bluemoon, post:24, topic:6136"]
mingw32-make -f makefile install
[/quote]
It does not work again:

![image|601x216](upload://scAk5vl4gVGGWyI6VTz3lf8Ig6V.png)

-------------------------

8Observer8 | 2021-07-22 15:11:25 UTC | #30

My settings in Qt Creator IDE:
```
CONFIG += c++11

INCLUDEPATH += "C:\Program Files (x86)\Urho3D\include"

LIBS += -L"C:\Program Files (x86)\Urho3D\lib"

LIBS += -lUrho3D -lkernel32 -luser32 -lgdi32 -lwinspool -lshell32 -lole32 -loleaut32 -luuid -lcomdlg32 -ladvapi32
LIBS += -ldbghelp -limm32 -lversion -lwinmm -lws2_32

SOURCES += \
    main.cpp
```

-------------------------

Bluemoon | 2021-07-22 15:13:51 UTC | #31

I use QT Creator and below is my *.pro file setting

> TEMPLATE = app
> CONFIG -= console
> CONFIG -= app_bundle
> CONFIG -= qt
> 
> TARGET = HelloUrho
> 
> URHO_HOME = C:\urho3d\home
> 
> 
> DEFINES += O2 NDEBUG
> DEFINES += URHO3D_STATIC_DEFINE URHO3D_ANGELSCRIPT URHO3D_FILEWATCHER URHO3D_IK URHO3D_LOGGING URHO3D_LUA URHO3D_NAVIGATION URHO3D_NETWORK URHO3D_PHYSICS URHO3D_PROFILING URHO3D_THREADING URHO3D_URHO2D URHO3D_WEBP HAVE_STDINT_H
> 
> QMAKE_CXXFLAGS += -mtune=generic  -std=gnu++11 -Wno-invalid-offsetof -march=native -msse3 -static -static-libgcc -static-libstdc++ -fno-keep-inline-dllexport -mstackrealign -fdiagnostics-color=auto
> 
> INCLUDEPATH += $${URHO_HOME}\include $${URHO_HOME}\include\Urho3D\ThirdParty $${URHO_HOME}\include\Urho3D\ThirdParty\Bullet $${URHO_HOME}\include\Urho3D\ThirdParty\Lua
> 
> LIBS += -L$${URHO_HOME}\lib -lUrho3D -luser32 -lgdi32 -lwinmm -limm32 -lole32 -loleaut32 -lsetupapi -lversion -luuid -lws2_32 -liphlpapi -lwinmm -lopengl32
> 
> SOURCES += \
>         HelloUrho.cpp
> 
> HEADERS += \
>     HelloUrho.h


See if it can be of any help

-------------------------

8Observer8 | 2021-07-22 15:15:02 UTC | #32

But a few days ago I made the same steps (CMake and so on) with Allegro5 and it works:

```
INCLUDEPATH += "E:\Libs\allegro-5.2.7.0-mingw-32bit\include"

LIBS += -L"E:\Libs\allegro-5.2.7.0-mingw-32bit\lib"

LIBS += -lallegro_dialog-static -lallegro_main-static -lallegro-static
LIBS += -lopengl32 -lgdi32 -lole32 -lwinmm -lcomdlg32 -lpsapi -lshlwapi

SOURCES += \
    main.cpp
```
main.cpp
```
#include <allegro5/allegro.h>
#include <allegro5/allegro_native_dialog.h>

int main()
{
    ALLEGRO_DISPLAY *display;

    if (!al_init())
    {
        al_show_native_message_box(NULL, NULL, NULL, "Could not initialize Allegro 5", NULL, 0);
    }

    if (!al_install_keyboard())
    {
        al_show_native_message_box(NULL, NULL, NULL, "Could not install keyboard", NULL, 0);
    }

    display = al_create_display(800, 600);

    if (!display)
    {
        al_show_native_message_box(NULL, NULL, NULL, "Could not create Allegro Window", NULL, 0);
    }

    bool done = false;
    bool redraw = true;

    ALLEGRO_EVENT_QUEUE *queue;
    queue = al_create_event_queue();
    al_register_event_source(queue, al_get_keyboard_event_source());
    al_register_event_source(queue, al_get_display_event_source(display));

    while (!done)
    {
        ALLEGRO_EVENT event;

        if (redraw && al_is_event_queue_empty(queue))
        {
            al_clear_to_color(al_map_rgb_f(0, 0, 0));
            al_flip_display();
            redraw = false;
        }

        al_wait_for_event(queue, &event);

        switch (event.type)
        {
            case ALLEGRO_EVENT_KEY_DOWN:
                if (event.keyboard.keycode == ALLEGRO_KEY_ESCAPE)
                {
                    done = true;
                }
                break;
            case ALLEGRO_EVENT_DISPLAY_CLOSE:
                done = true;
                break;
        }
    }

    return 0;
}
```

-------------------------

8Observer8 | 2021-07-22 15:21:43 UTC | #33

[quote="Bluemoon, post:31, topic:6136"]
I use QT Creator and below is my *.pro file setting
[/quote]
It very complicated for me. I am not an expert in .pro files but I will try later. Thank you! But it is very strange that Urho3D does not work in my settings because Allegro5 works fine with the same steps and settings.

-------------------------

Bluemoon | 2021-07-22 18:12:44 UTC | #34

Is it possible to post the content of your `main.cpp` and any companion header file of your urho3d setup.

-------------------------

8Observer8 | 2021-07-22 19:53:25 UTC | #35

main.cpp

```
#include <Urho3D/Engine/Application.h>
#include <iostream>

class MyApp : public Urho3D::Application
{
public:
    MyApp(Urho3D::Context * context) : Urho3D::Application(context)
    {
    }

    virtual void Setup()
    {
        std::cout << "Setup" << std::endl;
    }
};

URHO3D_DEFINE_APPLICATION_MAIN(MyApp)
```

-------------------------

Bluemoon | 2021-07-22 20:51:03 UTC | #36

Using a Urho3D-1.7.1 build I was able to successfully reproduce the error and seems to have identified what was actually causing it. Below is the modified .pro file of QT Creator that should work

```
CONFIG += c++11

INCLUDEPATH += "C:\Program Files (x86)\Urho3D\include"

LIBS += -L"C:\Program Files (x86)\Urho3D\lib"

DEFINES += URHO3D_STATIC_DEFINE

LIBS += -lUrho3D -lkernel32 -luser32 -lgdi32 -lwinspool -lshell32 -lole32 -loleaut32 -luuid -lcomdlg32 -ladvapi32
LIBS += -ldbghelp -limm32 -lversion -lwinmm -lws2_32 -lopengl32

SOURCES += \
    main.cpp
```

The first of the additions to your previous setting is `DEFINES += URHO3D_STATIC_DEFINE`. Personally I usually include all the Urho Defines used in building the lib, however, `URHO3D_STATIC_DEFINE` seems to be the minimum needed for the code in your `main.cpp` to run.

The next addition is `-lopengl32` added after the last `LIBS +=`

With these modification I was able to build and run the `main.cpp` you posted without any error.

-------------------------

8Observer8 | 2021-07-22 21:39:49 UTC | #37

21 errors again:

```
CONFIG += c++11

INCLUDEPATH += "C:\Program Files (x86)\Urho3D\include"

LIBS += -L"C:\Program Files (x86)\Urho3D\lib"

DEFINES += URHO3D_STATIC_DEFINE

#INCLUDEPATH += "E:\Libs\Urho3D-1.7.1-MinGW-32bit\include"

#LIBS += -L"E:\Libs\Urho3D-1.7.1-MinGW-32bit\lib\Urho3D"

#LIBS += -lkernel32 -luser32 -lgdi32 -lwinspool -lshell32 -lole32 -loleaut32 -luuid -lcomdlg32 -lSetupapi -ladvapi32 -lwinmm -limm32 -lversion -lws2_32 -ldbghelp -lopengl32 -lurho3d

#LIBS += -lUrho3D -lkernel32 -luser32 -lgdi32 -lwinspool -lshell32 -lole32 -loleaut32 -luuid -lcomdlg32 -ladvapi32

#LIBS += -ldbghelp -limm32 -lversion -lwinmm -lws2_32 -lopengl32

LIBS += -lUrho3D -lkernel32 -luser32 -lgdi32 -lwinspool -lshell32 -lole32 -loleaut32 -luuid -lcomdlg32 -ladvapi32

LIBS += -ldbghelp -limm32 -lversion -lwinmm -lws2_32 -lopengl32

SOURCES += \
    main.cpp
```

![image|604x215](upload://u9SJHWNNnvBKg8xCx3cn8WeA0FI.png)

-------------------------

8Observer8 | 2021-07-22 21:43:38 UTC | #38

I even tried to build to Static Release:

![image|365x199](upload://ysaozBFQTTdmqE7K8LOKlZ9z2OJ.png)

But in this case I got 51 errors:

![image|603x215](upload://7UP72V4UI1Lus4GYCilL3ayJLnD.png)

![image|599x182](upload://41EYbpqT6QFUqvRKmhdxNYnnhNK.png)

![image|583x181](upload://1aLIrKjRUTILwxDzkLaDyJTu41v.png)

![image|589x180](upload://6BjTCRZ0S2DN7fp4usExkMXbDLQ.png)

![image|589x184](upload://j0IcpdtTrRTMyieX2nwJLem26SQ.png)

![image|585x179](upload://vcbxcO2b2qnTctGhpmu8LwLE3DQ.png)

![image|580x101](upload://le7WdXItVetOHJFjtGLuVdE83eD.png)

-------------------------

S.L.C | 2021-07-23 02:57:51 UTC | #39

Might I ask where did you get the MinGW you're using?

-------------------------

8Observer8 | 2021-07-23 07:02:56 UTC | #40

From Qt: ```C:\Qt5\Tools\mingw810_32\bin```

-------------------------

8Observer8 | 2021-07-23 07:33:57 UTC | #41

@Bluemoon, what MinGW version did you use to build Urho3D? I think it is better to use the same MinGW that I use for my development environment. I use Qt Creator and Qt libraries.

-------------------------

Bluemoon | 2021-07-23 08:31:57 UTC | #42

My MinGW is v8.1.0

One more request.

navigate to the installation directory of your urho3d build. inside the `/lib/pkgconfig` folder look for a `Urho3D.pc` file. Post the content of this file let me take a look, you can also study the content yourself.

-------------------------

8Observer8 | 2021-07-23 08:58:55 UTC | #43

[quote="Bluemoon, post:42, topic:6136"]
Urho3D.pc
[/quote]

```
prefix=C:/Program Files (x86)/Urho3D
exec_prefix=${prefix}
libdir=${exec_prefix}/lib/.
includedir=${prefix}/include

# Additional Cflags for various build configurations, which can be accessed as normal pkg-config variable using '--variable' option
CFLAGS_DEBUG=-g -DDEBUG -D_DEBUG
CFLAGS_RELEASE=-O2 -DNDEBUG
CFLAGS_RELWITHDEBINFO=-O2 -g -DNDEBUG

Name: Urho3D
Description: Urho3D is a free lightweight, cross-platform 2D and 3D game engine implemented in C++ and released under the MIT license. Greatly inspired by OGRE (http://www.ogre3d.org) and Horde3D (http://www.horde3d.org).
Version: 0.0
URL: https://github.com/urho3d/Urho3D
Libs:   -L"${libdir}" -lUrho3D -luser32 -lgdi32 -lwinmm -limm32 -lole32 -loleaut32 -lversion -luuid -lws2_32 -lwinmm -lopengl32
Cflags: -DURHO3D_STATIC_DEFINE -DURHO3D_ANGELSCRIPT -DURHO3D_FILEWATCHER -DURHO3D_IK -DURHO3D_LOGGING -DURHO3D_LUA -DURHO3D_NAVIGATION -DURHO3D_NETWORK -DURHO3D_PHYSICS -DURHO3D_PROFILING -DURHO3D_THREADING -DURHO3D_URHO2D -DURHO3D_WEBP -DURHO3D_CXX11 -std=gnu++11 -Wno-invalid-offsetof -march=native -msse -msse2 -static -static-libgcc -static-libstdc++ -fno-keep-inline-dllexport -mstackrealign -fdiagnostics-color=auto  -I"${includedir}" -I"${includedir}/Urho3D/ThirdParty" -I"${includedir}/Urho3D/ThirdParty/Bullet" -I"${includedir}/Urho3D/ThirdParty/Lua"
```

-------------------------

Bluemoon | 2021-07-23 23:21:21 UTC | #44

So what I have below is QT Creator .pro file generated from the values in your `Urho3D.pc` . You can try using it
```
CONFIG += c++11

INCLUDEPATH += "C:\Program Files (x86)\Urho3D\include"

LIBS += -L"C:\Program Files (x86)\Urho3D\lib"


DEFINES += O2 NDEBUG
DEFINES += URHO3D_STATIC_DEFINE URHO3D_ANGELSCRIPT URHO3D_FILEWATCHER URHO3D_IK URHO3D_LOGGING 
DEFINES += URHO3D_LUA URHO3D_NAVIGATION URHO3D_NETWORK URHO3D_PHYSICS URHO3D_PROFILING 
DEFINES += URHO3D_THREADING URHO3D_URHO2D URHO3D_WEBP URHO3D_CXX11 

QMAKE_CXXFLAGS += -std=gnu++11 -Wno-invalid-offsetof -march=native -msse -msse2 -static 
QMAKE_CXXFLAGS += -static-libgcc -static-libstdc++ -fno-keep-inline-dllexport -mstackrealign -fdiagnostics-color=auto

LIBS += -lUrho3D -lkernel32 -luser32 -lgdi32 -lwinspool -lshell32 -lole32 -loleaut32 -luuid -lcomdlg32 -ladvapi32
LIBS += -ldbghelp -limm32 -lversion -lwinmm -lws2_32 -lopengl32

SOURCES += \
    main.cpp
```

As an addition, can you ensure that the compiler has access permission to `C:\Program Files (x86)\Urho3D`

-------------------------

8Observer8 | 2021-07-24 11:12:01 UTC | #45

Result:

![image|603x212](upload://lP1RU1TdwDzeSKmM0MHkJyAfzUY.png)

-------------------------

8Observer8 | 2021-07-24 11:13:00 UTC | #46

Result for Qt Static:

![image|593x220](upload://t6RCdOLPrUrqvmHNFOzjGoozvNm.png)

-------------------------

8Observer8 | 2021-07-24 11:19:31 UTC | #47

I found the problem for Qt Debug! I made "Clean" here:

![image|483x192](upload://6uXIhWy1mXmcJYfADZ1HQlNTHLd.png)

And now It works for Qt Debug:

![image|617x216](upload://9BotUHdbLf0n6fMgLxnWiNBozdQ.png)

But it does not work for Qt Static Release. What ideas?

![image|600x219](upload://23uUJElvoMyycsEASrXWU9XoFK6.png)

-------------------------

8Observer8 | 2021-07-24 11:21:04 UTC | #48

[quote="8Observer8, post:47, topic:6136"]
But it does not work for Qt Static Release. What ideas?
[/quote]

I made "Clean" for Static Release and now I have another errors:

![image|597x178](upload://pdwa7Peh0mV0QSgcVRD8cZMeIwG.png)

-------------------------

