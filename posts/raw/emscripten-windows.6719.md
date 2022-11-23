1vanK | 2021-02-18 18:58:19 UTC | #1

Does anyone have experience building Emscripten version of the engine on Windows? 

```
set "PATH=c:\Programs\CMake\bin;c:\Programs\Doxygen;c:\Programs\Graphviz\bin;c:\Program Files (x86)\HTML Help Workshop;c:\Program Files\Git\bin;c:\Programs\Python3;c:\Programs\MinGW64\i686-8.1.0-posix-dwarf-rt_v6-rev0\mingw32\bin"

call g:\MyGames\Emscripten\emsdk\emsdk_env.bat

set "TOOLCHAINS=%~dp0Urho3D\cmake\Toolchains"

cd Urho3D
call script\cmake_emscripten.bat g:\MyGames\Urho3DFork\BuildEmscripten
```

Error:

```

g:\MyGames\Urho3DFork>set "PATH=c:\Programs\CMake\bin;c:\Programs\Doxygen;c:\Programs\Graphviz\bin;c:\Program Files (x86)\HTML Help Workshop;c:\Program Files\Git\bin;c:\Programs\Python3;c:\Programs\MinGW64\i686-8.1.0-posix-dwarf-rt_v6-rev0\mingw32\bin" 

g:\MyGames\Urho3DFork>call g:\MyGames\Emscripten\emsdk\emsdk_env.bat 
Adding directories to PATH:
PATH += g:\MyGames\Emscripten\emsdk
PATH += g:\MyGames\Emscripten\emsdk\upstream\emscripten
PATH += g:\MyGames\Emscripten\emsdk\node\14.15.5_64bit\bin

Setting environment variables:
PATH = g:\MyGames\Emscripten\emsdk;g:\MyGames\Emscripten\emsdk\upstream\emscripten;g:\MyGames\Emscripten\emsdk\node\14.15.5_64bit\bin;c:\Programs\CMake\bin;c:\Programs\Doxygen;c:\Programs\Graphviz\bin;c:\Program Files (x86)\HTML Help Workshop;c:\Program Files\Git\bin;c:\Programs\Python3;c:\Programs\MinGW64\i686-8.1.0-posix-dwarf-rt_v6-rev0\mingw32\bin
EMSDK = g:/MyGames/Emscripten/emsdk
EM_CONFIG = g:\MyGames\Emscripten\emsdk\.emscripten
EM_CACHE = g:/MyGames/Emscripten/emsdk/upstream/emscripten\cache
EMSDK_NODE = g:\MyGames\Emscripten\emsdk\node\14.15.5_64bit\bin\node.exe
EMSDK_PYTHON = g:\MyGames\Emscripten\emsdk\python\3.7.4-pywin32_64bit\python.exe
JAVA_HOME = g:\MyGames\Emscripten\emsdk\java\8.152_64bit
emcc (Emscripten gcc/clang-like replacement + linker emulating GNU ld) 2.0.14 (8dd277d191daee9adfad03e5f0663df2db4b8bb1)
Copyright (C) 2014 the Emscripten authors (see AUTHORS.txt)
This is free and open source software under the MIT license.
There is NO warranty not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
-- Check for working C compiler: g:/MyGames/Emscripten/emsdk/upstream/emscripten/emcc.bat - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: g:/MyGames/Emscripten/emsdk/upstream/emscripten/em++.bat - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
CMake Warning at cmake/Modules/CheckHost.cmake:48 (message):
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
  cmake/Modules/UrhoCommon.cmake:125 (include)
  CMakeLists.txt:33 (include)


-- Performing Test IS_TRIVIALLY_DEFAULT_CONSTRUCTIBLE
-- Performing Test IS_TRIVIALLY_DEFAULT_CONSTRUCTIBLE - Failed
-- Performing Test IS_TRIVIALLY_DESTRUCTIBLE
-- Performing Test IS_TRIVIALLY_DESTRUCTIBLE - Failed
-- Performing Test IS_TRIVIALLY_COPY_ASSIGNABLE
-- Performing Test IS_TRIVIALLY_COPY_ASSIGNABLE - Failed
-- Performing Test IS_TRIVIALLY_COPY_CONSTRUCTIBLE
-- Performing Test IS_TRIVIALLY_COPY_CONSTRUCTIBLE - Failed
-- Looking for stdint.h
-- Looking for stdint.h - found
-- Looking for inttypes.h
-- Looking for inttypes.h - not found
-- Looking for malloc.h
-- Looking for malloc.h - not found
-- Looking for __sincosf
-- Looking for __sincosf - not found
-- Looking for malloc_usable_size
-- Looking for malloc_usable_size - found
-- Looking for sincosf in m
-- Looking for sincosf in m - found
-- Performing Test HAVE_GCC_WALL
-- Performing Test HAVE_GCC_WALL - Success
-- Performing Test HAVE_GCC_NO_STRICT_ALIASING
-- Performing Test HAVE_GCC_NO_STRICT_ALIASING - Success
-- Performing Test HAVE_GCC_WDECLARATION_AFTER_STATEMENT
-- Performing Test HAVE_GCC_WDECLARATION_AFTER_STATEMENT - Success
-- Performing Test HAVE_GCC_WERROR_DECLARATION_AFTER_STATEMENT
-- Performing Test HAVE_GCC_WERROR_DECLARATION_AFTER_STATEMENT - Success
-- Performing Test HAVE_GCC_ATOMICS
-- Performing Test HAVE_GCC_ATOMICS - Success
-- Performing Test HAVE_GCC_PREFERRED_STACK_BOUNDARY
-- Performing Test HAVE_GCC_PREFERRED_STACK_BOUNDARY - Failed
-- Performing Test HAVE_GCC_WSHADOW
-- Performing Test HAVE_GCC_WSHADOW - Success
-- Performing Test HAVE_NO_UNDEFINED
-- Performing Test HAVE_NO_UNDEFINED - Failed
-- Looking for clock_gettime in rt
-- Looking for clock_gettime in rt - found
-- Looking for sys/types.h
-- Looking for sys/types.h - not found
-- Looking for stdio.h
-- Looking for stdio.h - not found
-- Looking for stdlib.h
-- Looking for stdlib.h - not found
-- Looking for stddef.h
-- Looking for stddef.h - found
-- Looking for stdarg.h
-- Looking for stdarg.h - found
-- Looking for memory.h
-- Looking for memory.h - not found
-- Looking for string.h
-- Looking for string.h - not found
-- Looking for limits.h
-- Looking for limits.h - found
-- Looking for strings.h
-- Looking for strings.h - not found
-- Looking for wchar.h
-- Looking for wchar.h - not found
-- Looking for ctype.h
-- Looking for ctype.h - not found
-- Looking for math.h
-- Looking for math.h - not found
-- Looking for iconv.h
-- Looking for iconv.h - not found
-- Looking for signal.h
-- Looking for signal.h - not found
-- Looking for 8 include files stdint.h, ..., dlfcn.h
-- Looking for 8 include files stdint.h, ..., dlfcn.h - not found
-- Looking for M_PI
-- Looking for M_PI - not found
-- Looking for sys/mman.h
-- Looking for sys/mman.h - not found
-- Looking for strtod
-- Looking for strtod - found
-- Looking for malloc
-- Looking for malloc - found
-- Looking for calloc
-- Looking for calloc - found
-- Looking for realloc
-- Looking for realloc - found
-- Looking for free
-- Looking for free - found
-- Looking for getenv
-- Looking for getenv - found
-- Looking for setenv
-- Looking for setenv - found
-- Looking for putenv
-- Looking for putenv - found
-- Looking for unsetenv
-- Looking for unsetenv - found
-- Looking for qsort
-- Looking for qsort - found
-- Looking for abs
-- Looking for abs - found
-- Looking for bcopy
-- Looking for bcopy - found
-- Looking for memset
-- Looking for memset - found
-- Looking for memcpy
-- Looking for memcpy - found
-- Looking for memmove
-- Looking for memmove - found
-- Looking for memcmp
-- Looking for memcmp - found
-- Looking for strlen
-- Looking for strlen - found
-- Looking for strlcpy
-- Looking for strlcpy - found
-- Looking for strlcat
-- Looking for strlcat - found
-- Looking for _strrev
-- Looking for _strrev - not found
-- Looking for _strupr
-- Looking for _strupr - not found
-- Looking for _strlwr
-- Looking for _strlwr - not found
-- Looking for strchr
-- Looking for strchr - found
-- Looking for strrchr
-- Looking for strrchr - found
-- Looking for strstr
-- Looking for strstr - found
-- Looking for itoa
-- Looking for itoa - not found
-- Looking for _ltoa
-- Looking for _ltoa - not found
-- Looking for _uitoa
-- Looking for _uitoa - not found
-- Looking for _ultoa
-- Looking for _ultoa - not found
-- Looking for strtol
-- Looking for strtol - found
-- Looking for strtoul
-- Looking for strtoul - found
-- Looking for _i64toa
-- Looking for _i64toa - not found
-- Looking for _ui64toa
-- Looking for _ui64toa - not found
-- Looking for strtoll
-- Looking for strtoll - found
-- Looking for strtoull
-- Looking for strtoull - found
-- Looking for atoi
-- Looking for atoi - found
-- Looking for atof
-- Looking for atof - found
-- Looking for strcmp
-- Looking for strcmp - found
-- Looking for strncmp
-- Looking for strncmp - found
-- Looking for _stricmp
-- Looking for _stricmp - not found
-- Looking for strcasecmp
-- Looking for strcasecmp - found
-- Looking for _strnicmp
-- Looking for _strnicmp - not found
-- Looking for strncasecmp
-- Looking for strncasecmp - found
-- Looking for vsscanf
-- Looking for vsscanf - found
-- Looking for vsnprintf
-- Looking for vsnprintf - found
-- Looking for fopen64
-- Looking for fopen64 - found
-- Looking for fseeko
-- Looking for fseeko - found
-- Looking for fseeko64
-- Looking for fseeko64 - found
-- Looking for sigaction
-- Looking for sigaction - found
-- Looking for setjmp
-- Looking for setjmp - not found
-- Looking for nanosleep
-- Looking for nanosleep - found
-- Looking for sysconf
-- Looking for sysconf - found
-- Looking for sysctlbyname
-- Looking for sysctlbyname - not found
-- Looking for getauxval
-- Looking for getauxval - found
-- Looking for poll
-- Looking for poll - found
-- Looking for _Exit
-- Looking for _Exit - found
-- Looking for pow in m
-- Looking for pow in m - found
-- Looking for atan
-- Looking for atan - found
-- Looking for atan2
-- Looking for atan2 - found
-- Looking for ceil
-- Looking for ceil - found
-- Looking for copysign
-- Looking for copysign - found
-- Looking for cos
-- Looking for cos - found
-- Looking for cosf
-- Looking for cosf - found
-- Looking for fabs
-- Looking for fabs - found
-- Looking for floor
-- Looking for floor - found
-- Looking for log
-- Looking for log - found
-- Looking for pow
-- Looking for pow - found
-- Looking for scalbn
-- Looking for scalbn - found
-- Looking for sin
-- Looking for sin - found
-- Looking for sinf
-- Looking for sinf - found
-- Looking for sqrt
-- Looking for sqrt - found
-- Looking for sqrtf
-- Looking for sqrtf - found
-- Looking for tan
-- Looking for tan - found
-- Looking for tanf
-- Looking for tanf - found
-- Looking for acos
-- Looking for acos - found
-- Looking for asin
-- Looking for asin - found
-- Looking for iconv_open in iconv
-- Looking for iconv_open in iconv - not found
-- Looking for alloca.h
-- Looking for alloca.h - not found
-- Performing Test HAVE_SA_SIGACTION
-- Performing Test HAVE_SA_SIGACTION - Failed
-- Performing Test HAVE_VIDEO_OPENGL_EGL
-- Performing Test HAVE_VIDEO_OPENGL_EGL - Success
-- Performing Test HAVE_VIDEO_OPENGLES_V1
-- Performing Test HAVE_VIDEO_OPENGLES_V1 - Success
-- Performing Test HAVE_VIDEO_OPENGLES_V2
-- Performing Test HAVE_VIDEO_OPENGLES_V2 - Success
-- 
-- SDL2 was configured with the following options:
-- 
-- Platform: Linux-1
-- 64-bit:   FALSE
-- Compiler: g:/MyGames/Emscripten/emsdk/upstream/emscripten/emcc.bat
-- 
-- Subsystems:
--   Atomic:     ON
--   Audio:      ON
--   Video:      ON
--   Render:     OFF
--   Events:     ON
--   Joystick:   ON
--   Haptic:     ON
--   Power:      ON
--   Threads:    OFF
--   Timers:     ON
--   File:       ON
--   Loadso:     ON
--   CPUinfo:    ON
--   Filesystem: ON
--   Dlopen:     ON
--   Sensor:     ON
-- 
-- Options:
--   ALSA                   (Wanted: ON): OFF
--   ALSA_SHARED            (Wanted: ON): OFF
--   ARTS                   (Wanted: ON): OFF
--   ARTS_SHARED            (Wanted: ON): OFF
--   ASSEMBLY               (Wanted: OFF): OFF
--   ASSERTIONS             (Wanted: auto): auto
--   BACKGROUNDING_SIGNAL   (Wanted: OFF): OFF
--   CLOCK_GETTIME          (Wanted: ON): ON
--   DIRECTFB_SHARED        (Wanted: OFF): OFF
--   DISKAUDIO              (Wanted: ON): ON
--   DUMMYAUDIO             (Wanted: ON): ON
--   ESD                    (Wanted: ON): OFF
--   ESD_SHARED             (Wanted: ON): OFF
--   FOREGROUNDING_SIGNAL   (Wanted: OFF): OFF
--   FUSIONSOUND            (Wanted: ON): OFF
--   FUSIONSOUND_SHARED     (Wanted: ON): OFF
--   GCC_ATOMICS            (Wanted: ON): ON
--   HIDAPI                 (Wanted: OFF): OFF
--   INPUT_TSLIB            (Wanted: ON): OFF
--   JACK                   (Wanted: ON): OFF
--   JACK_SHARED            (Wanted: ON): OFF
--   KMSDRM_SHARED          (Wanted: ON): OFF
--   LIBC                   (Wanted: ON): ON
--   LIBSAMPLERATE          (Wanted: ON): OFF
--   LIBSAMPLERATE_SHARED   (Wanted: ON): OFF
--   NAS                    (Wanted: ON): OFF
--   NAS_SHARED             (Wanted: ON): OFF
--   OSS                    (Wanted: ON): OFF
--   PTHREADS               (Wanted: ON): OFF
--   PTHREADS_SEM           (Wanted: ON): OFF
--   PULSEAUDIO             (Wanted: ON): OFF
--   PULSEAUDIO_SHARED      (Wanted: ON): OFF
--   SDL_DLOPEN             (Wanted: ON): ON
--   SDL_HAPTIC             (Wanted: ON): OFF
--   SDL_STATIC_PIC         (Wanted: OFF): OFF
--   SNDIO                  (Wanted: ON): OFF
--   VIDEO_COCOA            (Wanted: OFF): OFF
--   VIDEO_DIRECTFB         (Wanted: OFF): OFF
--   VIDEO_DUMMY            (Wanted: ON): ON
--   VIDEO_KMSDRM           (Wanted: ON): OFF
--   VIDEO_OPENGL           (Wanted: OFF): OFF
--   VIDEO_OPENGLES         (Wanted: ON): ON
--   VIDEO_RPI              (Wanted: OFF): OFF
--   VIDEO_VIVANTE          (Wanted: ON): OFF
--   VIDEO_VULKAN           (Wanted: ON): ON
--   VIDEO_WAYLAND          (Wanted: ON): OFF
--   VIDEO_WAYLAND_QT_TOUCH (Wanted: OFF): OFF
--   VIDEO_X11              (Wanted: ON): OFF
--   VIDEO_X11_XCURSOR      (Wanted: ON): OFF
--   VIDEO_X11_XINERAMA     (Wanted: ON): OFF
--   VIDEO_X11_XINPUT       (Wanted: ON): OFF
--   VIDEO_X11_XRANDR       (Wanted: ON): OFF
--   VIDEO_X11_XSCRNSAVER   (Wanted: ON): OFF
--   VIDEO_X11_XSHAPE       (Wanted: ON): OFF
--   VIDEO_X11_XVM          (Wanted: ON): OFF
--   WASAPI                 (Wanted: OFF): OFF
--   WAYLAND_SHARED         (Wanted: ON): OFF
--   X11_SHARED             (Wanted: ON): OFF
-- 
--  CFLAGS:        -mno-sse -Wno-warn-absolute-paths -Wno-unknown-warning-option --bind -Qunused-arguments
--  EXTRA_CFLAGS:  -Wshadow -Wdeclaration-after-statement -Werror=declaration-after-statement -fno-strict-aliasing -Wall 
--  EXTRA_LDFLAGS: 
--  EXTRA_LIBS:    rt;m
-- 
-- Looking for include file stdint.h
-- Looking for include file stdint.h - found
-- Performing Test IK_RESTRICT_restrict
-- Performing Test IK_RESTRICT_restrict - Success
-- Performing Test HAVE_NATIVE_COMPILER
-- Performing Test HAVE_NATIVE_COMPILER - Success
-- Performing Test COMPILER_HAS_HIDDEN_VISIBILITY
-- Performing Test COMPILER_HAS_HIDDEN_VISIBILITY - Success
-- Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY
-- Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY - Success
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR - Success
In file included from G:/MyGames/Urho3DFork/Urho3D/Source/Urho3D/Precompiled.h:28:
In file included from G:/MyGames/Urho3DFork/Urho3D/Source/Urho3D/Container/HashMap.h:25:
In file included from G:/MyGames/Urho3DFork/Urho3D/Source/Urho3D/Container/../Container/HashBase.h:31:
G:/MyGames/Urho3DFork/Urho3D/Source/Urho3D/Container/../Container/Allocator.h:31:10: fatal error: 'cstddef' file not found
#include <cstddef>
         ^~~~~~~~~
1 error generated.
em++: error: 'g:/MyGames/Emscripten/emsdk/upstream/bin\clang++.exe -DEMSCRIPTEN -fignore-exceptions -fno-inline-functions -mllvm -combiner-global-alias-analysis=false -mllvm -enable-emscripten-sjlj -mllvm -disable-lsr -Xclang -iwithsysroot/include/SDL -target wasm32-unknown-emscripten -D__EMSCRIPTEN_major__=2 -D__EMSCRIPTEN_minor__=0 -D__EMSCRIPTEN_tiny__=14 -D_LIBCPP_ABI_VERSION=2 -Dunix -D__unix -D__unix__ -flegacy-pass-manager -Werror=implicit-function-declaration --sysroot=g:\MyGames\Emscripten\emsdk\upstream\emscripten\cache\sysroot -Xclang -iwithsysroot/include\compat -DURHO3D_STATIC_DEFINE -DURHO3D_ANGELSCRIPT -DURHO3D_FILEWATCHER -DURHO3D_IK -DURHO3D_LOGGING -DURHO3D_LUA -DURHO3D_NAVIGATION -DURHO3D_PHYSICS -DURHO3D_PROFILING -DURHO3D_URHO2D -DURHO3D_WEBP -DHAVE_STDINT_H -DURHO3D_IS_BUILDING -DHAVE_SINCOSF -DTOLUA_RELEASE --sysroot=g:/MyGames/Emscripten/emsdk/upstream/emscripten/system -std=c++11 -Wno-invalid-offsetof -mno-sse -Wno-unknown-warning-option -Qunused-arguments -Oz -DNDEBUG -fvisibility=hidden -fvisibility-inlines-hidden -std=c++11 -IG:/MyGames/Urho3DFork/BuildEmscripten/Source/Urho3D -IG:/MyGames/Urho3DFork/Urho3D/Source/Urho3D -IG:/MyGames/Urho3DFork/BuildEmscripten/include/Urho3D/ThirdParty -IG:/MyGames/Urho3DFork/BuildEmscripten/include/Urho3D/ThirdParty/Bullet -IG:/MyGames/Urho3DFork/BuildEmscripten/include/Urho3D/ThirdParty/Detour -IG:/MyGames/Urho3DFork/BuildEmscripten/include/Urho3D/ThirdParty/Lua -c -x c++-header -MTdeps -MM -MF G:/MyGames/Urho3DFork/BuildEmscripten/Source/Urho3D/Precompiled.h.d G:/MyGames/Urho3DFork/Urho3D/Source/Urho3D/Precompiled.h' failed (1)
CMake Error at cmake/Modules/UrhoCommon.cmake:1303 (message):
  Could not generate dependency list for PCH.  There is something wrong with
  your compiler toolchain.  Ensure its bin path is in the PATH environment
  variable or ensure CMake can find CC/CXX in your build environment.
Call Stack (most recent call first):
  Source/Urho3D/CMakeLists.txt:409 (enable_pch)


-- Configuring incomplete, errors occurred!
See also "G:/MyGames/Urho3DFork/BuildEmscripten/CMakeFiles/CMakeOutput.log".
See also "G:/MyGames/Urho3DFork/BuildEmscripten/CMakeFiles/CMakeError.log".
```

With disabled PCH: `call script\cmake_emscripten.bat g:\MyGames\Urho3DFork\BuildEmscripten -D URHO3D_PCH=0` cmake finish successfully with all test programs.

```
...
-- Looking for include file stdint.h
-- Looking for include file stdint.h - found
...
```

But when compiling, it does not find header files

```
set "PATH=c:\Programs\CMake\bin;c:\Programs\Doxygen;c:\Programs\Graphviz\bin;c:\Program Files (x86)\HTML Help Workshop;c:\Program Files\Git\bin;c:\Programs\Python3;c:\Programs\MinGW64\i686-8.1.0-posix-dwarf-rt_v6-rev0\mingw32\bin"

call g:\MyGames\Emscripten\emsdk\emsdk_env.bat

cmake --build BuildEmscripten >log 2>&1
```

```
[  0%] Building CXX object Source/ThirdParty/ETCPACK/CMakeFiles/ETCPACK.dir/source/etcdec.cxx.o
G:\MyGames\Urho3DFork\Urho3D\Source\ThirdParty\ETCPACK\source\etcdec.cxx:168:10: fatal error: 'stdio.h' file not found
#include <stdio.h>
         ^~~~~~~~~
1 error generated.
em++: error: 'g:/MyGames/Emscripten/emsdk/upstream/bin\clang++.exe -DEMSCRIPTEN -fignore-exceptions -fno-inline-functions -mllvm -combiner-global-alias-analysis=false -mllvm -enable-emscripten-sjlj -mllvm -disable-lsr -Xclang -iwithsysroot/include/SDL -target wasm32-unknown-emscripten -D__EMSCRIPTEN_major__=2 -D__EMSCRIPTEN_minor__=0 -D__EMSCRIPTEN_tiny__=14 -D_LIBCPP_ABI_VERSION=2 -Dunix -D__unix -D__unix__ -flegacy-pass-manager -Werror=implicit-function-declaration --sysroot=g:\MyGames\Emscripten\emsdk\upstream\emscripten\cache\sysroot -Xclang -iwithsysroot/include\compat --sysroot=g:/MyGames/Emscripten/emsdk/upstream/emscripten/system -DURHO3D_ANGELSCRIPT -DURHO3D_FILEWATCHER -DURHO3D_IK -DURHO3D_LOGGING -DURHO3D_LUA -DURHO3D_NAVIGATION -DURHO3D_PHYSICS -DURHO3D_PROFILING -DURHO3D_STATIC_DEFINE -DURHO3D_URHO2D -DURHO3D_WEBP -std=c++11 -Wno-invalid-offsetof -mno-sse -Wno-unknown-warning-option -Qunused-arguments -Oz -DNDEBUG -fvisibility=hidden -fvisibility-inlines-hidden -c G:\MyGames\Urho3DFork\Urho3D\Source\ThirdParty\ETCPACK\source\etcdec.cxx -o CMakeFiles\ETCPACK.dir\source\etcdec.cxx.o' failed (1)
mingw32-make.exe[2]: *** [Source\ThirdParty\ETCPACK\CMakeFiles\ETCPACK.dir\build.make:81: Source/ThirdParty/ETCPACK/CMakeFiles/ETCPACK.dir/source/etcdec.cxx.o] Error 1
mingw32-make.exe[1]: *** [CMakeFiles\Makefile2:1768: Source/ThirdParty/ETCPACK/CMakeFiles/ETCPACK.dir/all] Error 2
mingw32-make.exe: *** [Makefile:170: all] Error 2
```

Any ideas?

-------------------------

1vanK | 2021-02-18 23:10:11 UTC | #2

Ok using old version of Emscripten helped me:

```
call emsdk install 2.0.8
call emsdk activate 2.0.8
```

-------------------------

1vanK | 2021-02-20 17:39:01 UTC | #3

If someone is interested, then launching the application locally without installing a web server: 
```
call g:\MyGames\Emscripten\emsdk\emsdk_env.bat
cd BuildEmscripten\bin
emrun --serve_after_exit --serve_after_close 01_HelloWorld.html
```

Running script:
```
call emrun --serve_after_exit --serve_after_close Urho3DPlayer.html Scripts/Editor.as
```

-------------------------

