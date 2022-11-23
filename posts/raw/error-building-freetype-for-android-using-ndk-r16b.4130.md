mizahnyx | 2018-03-28 06:46:35 UTC | #1

I tried to compile latest source on Linux for Android using NDK r16b.

Got this error:

```
-- The C compiler identification is Clang 5.0.300080
-- The CXX compiler identification is Clang 5.0.300080
-- Check for working C compiler: /home/sjenkinsc/Software/android-ndk-r16b/toolchains/llvm/prebuilt/linux-x86_64/bin/clang
-- Check for working C compiler: /home/sjenkinsc/Software/android-ndk-r16b/toolchains/llvm/prebuilt/linux-x86_64/bin/clang -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /home/sjenkinsc/Software/android-ndk-r16b/toolchains/llvm/prebuilt/linux-x86_64/bin/clang++
-- Check for working CXX compiler: /home/sjenkinsc/Software/android-ndk-r16b/toolchains/llvm/prebuilt/linux-x86_64/bin/clang++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
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
-- Performing Test HAVE_NO_UNDEFINED - Success
-- Looking for clock_gettime in rt
-- Looking for clock_gettime in rt - not found
-- Looking for clock_gettime in c
-- Looking for clock_gettime in c - found
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
-- Looking for libunwind.h
-- Looking for libunwind.h - not found
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
-- Looking for bcopy - not found
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
-- Looking for atof - not found
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
-- Looking for fopen64 - not found
-- Looking for fseeko
-- Looking for fseeko - found
-- Looking for fseeko64
-- Looking for fseeko64 - not found
-- Looking for sigaction
-- Looking for sigaction - found
-- Looking for setjmp
-- Looking for setjmp - found
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
-- Looking for dlopen
-- Looking for dlopen - found
-- Performing Test HAVE_DLOPEN
-- Performing Test HAVE_DLOPEN - Failed
-- Performing Test HAVE_PTHREADS
-- Performing Test HAVE_PTHREADS - Failed
-- Performing Test HAVE_ARM_MODE
-- Performing Test HAVE_ARM_MODE - Success
-- Performing Test HAVE_VIDEO_OPENGL_EGL
-- Performing Test HAVE_VIDEO_OPENGL_EGL - Failed
-- Performing Test HAVE_VIDEO_OPENGLES_V1
-- Performing Test HAVE_VIDEO_OPENGLES_V1 - Failed
-- Performing Test HAVE_VIDEO_OPENGLES_V2
-- Performing Test HAVE_VIDEO_OPENGLES_V2 - Failed
-- Performing Test VULKAN_PASSED_ANDROID_CHECKS
-- Performing Test VULKAN_PASSED_ANDROID_CHECKS - Success
-- 
-- SDL2 was configured with the following options:
-- 
-- Platform: Android-1
-- 64-bit:   FALSE
-- Compiler: /home/sjenkinsc/Software/android-ndk-r16b/toolchains/llvm/prebuilt/linux-x86_64/bin/clang
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
--   Threads:    ON
--   Timers:     ON
--   File:       ON
--   Loadso:     ON
--   CPUinfo:    ON
--   Filesystem: ON
--   Dlopen:     ON
-- 
-- Options:
--   ALSA                   (Wanted: OFF): OFF
--   ALSA_SHARED            (Wanted: OFF): OFF
--   ARTS                   (Wanted: OFF): OFF
--   ARTS_SHARED            (Wanted: OFF): OFF
--   ASSEMBLY               (Wanted: ON): ON
--   ASSERTIONS             (Wanted: auto): auto
--   CLOCK_GETTIME          (Wanted: ON): ON
--   DIRECTFB_SHARED        (Wanted: OFF): OFF
--   DISKAUDIO              (Wanted: ON): ON
--   DUMMYAUDIO             (Wanted: ON): ON
--   ESD                    (Wanted: OFF): OFF
--   ESD_SHARED             (Wanted: OFF): OFF
--   FUSIONSOUND            (Wanted: OFF): OFF
--   FUSIONSOUND_SHARED     (Wanted: OFF): OFF
--   GCC_ATOMICS            (Wanted: ON): ON
--   INPUT_TSLIB            (Wanted: OFF): OFF
--   JACK                   (Wanted: OFF): OFF
--   JACK_SHARED            (Wanted: OFF): OFF
--   KMSDRM_SHARED          (Wanted: OFF): OFF
--   LIBC                   (Wanted: ON): ON
--   LIBSAMPLERATE          (Wanted: OFF): OFF
--   LIBSAMPLERATE_SHARED   (Wanted: OFF): OFF
--   MIR_SHARED             (Wanted: OFF): OFF
--   NAS                    (Wanted: OFF): OFF
--   NAS_SHARED             (Wanted: OFF): OFF
--   OSS                    (Wanted: OFF): OFF
--   PTHREADS               (Wanted: ON): OFF
--   PTHREADS_SEM           (Wanted: ON): OFF
--   PULSEAUDIO             (Wanted: OFF): OFF
--   PULSEAUDIO_SHARED      (Wanted: OFF): OFF
--   SDL_DLOPEN             (Wanted: ON): OFF
--   SDL_HAPTIC             (Wanted: ON): ON
--   SDL_STATIC_PIC         (Wanted: OFF): OFF
--   SNDIO                  (Wanted: OFF): OFF
--   VIDEO_COCOA            (Wanted: OFF): OFF
--   VIDEO_DIRECTFB         (Wanted: OFF): OFF
--   VIDEO_DUMMY            (Wanted: ON): ON
--   VIDEO_KMSDRM           (Wanted: OFF): OFF
--   VIDEO_MIR              (Wanted: OFF): OFF
--   VIDEO_OPENGL           (Wanted: ON): OFF
--   VIDEO_OPENGLES         (Wanted: ON): OFF
--   VIDEO_RPI              (Wanted: OFF): OFF
--   VIDEO_VIVANTE          (Wanted: OFF): OFF
--   VIDEO_VULKAN           (Wanted: ON): OFF
--   VIDEO_WAYLAND          (Wanted: OFF): OFF
--   VIDEO_WAYLAND_QT_TOUCH (Wanted: OFF): OFF
--   VIDEO_X11              (Wanted: OFF): OFF
--   VIDEO_X11_XCURSOR      (Wanted: OFF): OFF
--   VIDEO_X11_XINERAMA     (Wanted: OFF): OFF
--   VIDEO_X11_XINPUT       (Wanted: OFF): OFF
--   VIDEO_X11_XRANDR       (Wanted: OFF): OFF
--   VIDEO_X11_XSCRNSAVER   (Wanted: OFF): OFF
--   VIDEO_X11_XSHAPE       (Wanted: OFF): OFF
--   VIDEO_X11_XVM          (Wanted: OFF): OFF
--   WAYLAND_SHARED         (Wanted: OFF): OFF
--   X11_SHARED             (Wanted: OFF): OFF
-- 
--  CFLAGS:        -fsigned-char -funwind-tables -no-canonical-prefixes -gcc-toolchain /home/sjenkinsc/Software/android-ndk-r16b/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64 -target armv7-none-linux-androideabi -Wno-invalid-command-line-argument -Wno-unused-command-line-argument -fno-integrated-as -march=armv7-a -mfloat-abi=softfp -mfpu=vfpv3-d16 -mthumb -Wa,--noexecstack -Wformat -Werror=format-security -fdata-sections -ffunction-sections -Qunused-arguments
--  EXTRA_CFLAGS:  -Wshadow -Wdeclaration-after-statement -Wall 
--  EXTRA_LDFLAGS: -Wl,--no-undefined
--  EXTRA_LIBS:    m;/home/sjenkinsc/Software/android-ndk-r16b/platforms/android-19/arch-arm/usr/lib/libdl.so;/home/sjenkinsc/Software/android-ndk-r16b/platforms/android-19/arch-arm/usr/lib/liblog.so;/home/sjenkinsc/Software/android-ndk-r16b/platforms/android-19/arch-arm/usr/lib/libandroid.so;/home/sjenkinsc/Software/android-ndk-r16b/platforms/android-19/arch-arm/usr/lib/libGLESv1_CM.so;/home/sjenkinsc/Software/android-ndk-r16b/platforms/android-19/arch-arm/usr/lib/libGLESv2.so
-- 
-- The ASM compiler identification is GNU
-- Found assembler: /home/sjenkinsc/Software/android-ndk-r16b/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/bin/arm-linux-androideabi-gcc
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
-- Found Urho3D: as CMake target
-- Could NOT find Doxygen (missing:  DOXYGEN_EXECUTABLE) 
-- Configuring done
-- Generating done
CMake Warning:
  Manually-specified variables were not used by the project:

    ANDROID_TOOLCHAIN
    URHO3D_C++11


-- Build files have been written to: /home/sjenkinsc/Fuentes/Urho3D/build.android
Scanning dependencies of target FreeType
[  0%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/autofit/autofit.c.o
In file included from /home/sjenkinsc/Fuentes/Urho3D/Source/ThirdParty/FreeType/src/autofit/autofit.c:22:
In file included from /home/sjenkinsc/Fuentes/Urho3D/Source/ThirdParty/FreeType/src/autofit/afangles.c:20:
In file included from /home/sjenkinsc/Fuentes/Urho3D/Source/ThirdParty/FreeType/src/autofit/aftypes.h:37:
In file included from /home/sjenkinsc/Fuentes/Urho3D/Source/ThirdParty/FreeType/include/freetype/freetype.h:33:
In file included from /home/sjenkinsc/Fuentes/Urho3D/Source/ThirdParty/FreeType/include/freetype/config/ftconfig.h:43:
In file included from /home/sjenkinsc/Fuentes/Urho3D/Source/ThirdParty/FreeType/include/freetype/config/ftstdlib.h:78:
/home/sjenkinsc/Software/android-ndk-r16b/sources/cxx-stl/llvm-libc++/include/string.h:61:15: fatal error: 
      'string.h' file not found
#include_next <string.h>
              ^~~~~~~~~~
1 error generated.
Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/build.make:62: recipe for target 'Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/autofit/autofit.c.o' failed
make[2]: *** [Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/autofit/autofit.c.o] Error 1
CMakeFiles/Makefile2:169: recipe for target 'Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/all' failed
make[1]: *** [Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/all] Error 2
Makefile:149: recipe for target 'all' failed
make: *** [all] Error 2
```

Any suggestion?

Thanks in advance.

-------------------------

simonsch | 2018-03-28 13:16:41 UTC | #2

Okay i can only talk about my own experience, i used r14 to build urho3d in a docker container based on a debian base image. I would not choose clang to build it, try to use another toolchain like -DANDROID_TOOLCHAIN=gcc

-------------------------

yushli1 | 2018-03-28 16:51:14 UTC | #3

r16b is using unified header only. That needs changes to the build system. Maybe @weitjong can do something about it.

-------------------------

weitjong | 2018-03-28 17:33:52 UTC | #4

That one is on top of my todo list. I am about to wrap up my work with Clang-Tidy. However, I may take some break from Urho project to pursue other interests, like ML. So, no promise.

-------------------------

