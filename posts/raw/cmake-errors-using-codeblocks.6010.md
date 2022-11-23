MZoltan32 | 2020-03-21 14:00:05 UTC | #1

I have errors while cmake used with codeblocks settings.

[details=CMake Log]
[quote]
CMake Warning (dev) in CMakeLists.txt:
  No project() command is present.  The top-level CMakeLists.txt file must
  contain a literal, direct call to the project() command.  Add a line of
  code such as

    project(ProjectName)

  near the top of the file, but after cmake_minimum_required().

  CMake is pretending there is a "project(Project)" command on the first
  line.
This warning is for project developers.  Use -Wno-dev to suppress it.

The C compiler identification is GNU 5.1.0
The CXX compiler identification is GNU 5.1.0
Check for working C compiler: C:/Program Files (x86)/CodeBlocks/MinGW/bin/gcc.exe
Check for working C compiler: C:/Program Files (x86)/CodeBlocks/MinGW/bin/gcc.exe -- works
Detecting C compiler ABI info
Detecting C compiler ABI info - done
Detecting C compile features
Detecting C compile features - done
Check for working CXX compiler: C:/Program Files (x86)/CodeBlocks/MinGW/bin/g++.exe
Check for working CXX compiler: C:/Program Files (x86)/CodeBlocks/MinGW/bin/g++.exe -- works
Detecting CXX compiler ABI info
Detecting CXX compiler ABI info - done
Detecting CXX compile features
Detecting CXX compile features - done
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
Looking for sincosf in m - not found
Performing Test HAVE_RTL_OSVERSIONINFOW
Performing Test HAVE_RTL_OSVERSIONINFOW - Failed
CMake Error at ThirdParty/FreeType/CMakeLists.txt:81 (setup_library):
  Unknown CMake command "setup_library".


CMake Warning (dev) in CMakeLists.txt:
  No cmake_minimum_required command is present.  A line of code such as

    cmake_minimum_required(VERSION 3.16)

  should be added at the top of the file.  The version specified may be lower
  if you wish to support older CMake versions for this project.  For more
  information run "cmake --help-policy CMP0000".
This warning is for project developers.  Use -Wno-dev to suppress it.

Configuring incomplete, errors occurred!
See also "E:/tar/games/developedgames/Urho3D-1.7.1/build/CMakeFiles/CMakeOutput.log".
See also "E:/tar/games/developedgames/Urho3D-1.7.1/build/CMakeFiles/CMakeError.log".
[/quote]
[/details]

-------------------------

SirNate0 | 2020-03-21 12:53:26 UTC | #2

Did you perhaps use Source/ as the cmake source directory, rather than the top-level Urho directory?

-------------------------

MZoltan32 | 2020-03-21 13:26:43 UTC | #3

if i use the top level it gives this error code: 

"CMake Error: The source "E:/tar/games/developedgames/Urho3D-1.7.1/CMakeLists.txt" does not match the source "E:/tar/games/developedgames/Urho3D-1.7.1/Source/CMakeLists.txt" used to generate cache.  Re-run cmake with a different source directory."

-------------------------

Modanung | 2020-03-21 13:56:04 UTC | #4

Have you tried running `cmake_clean.sh` in between?

-------------------------

MZoltan32 | 2020-03-21 19:08:17 UTC | #5

i use windows no i havent tryed it

-------------------------

Modanung | 2020-03-21 19:15:14 UTC | #6

Ah, you're in `bat` country. :wink:
CMake tries to be lazy. Usually this only saves time, but sometimes this means it will leave things unchanged that should be modified.

-------------------------

SirNate0 | 2020-03-21 21:06:31 UTC | #7

Just delete your build directory and redo the build process using the correct (top level) directory as the source. The .bat file would also accomplish it, but it's usually simpler this way unless you have stuff you want to keep in it, possibly.

-------------------------

bvanevery | 2020-03-22 01:13:57 UTC | #8

I would say, don't use .bat files at all.  What's with this .bat file stuff that keeps coming up?  I've never used a .bat file to build Urho3D on Windows in my life.  Use cmake-gui.

-------------------------

weitjong | 2020-03-22 06:51:36 UTC | #9

It really does not matter guys. Our build system supports both cmake GUI and CLI mode, and also both out-of-source or non out-of-source build. Out of source build is preferred whether your “build” tree is relative to the “source” tree or really outside of it. We support most of the generators supported by CMake, although officially we only named a few in our docs as well as in our batch files and shell files. So, choose your own poison and stick to one (or more but just don’t mix them).

-------------------------

MZoltan32 | 2020-03-22 08:37:10 UTC | #10

i tryed deleting the build directory content and restarting after installing directx sdk

but i have a lot of error messages about not found things (are there things needed to be added to environment variables?):

[details=Log]
Looking for C++ include d3dcompiler.h

Looking for C++ include d3dcompiler.h - not found

Looking for C++ include d3d9.h

Looking for C++ include d3d9.h - found

Looking for C++ include d3d11.h

Looking for C++ include d3d11.h - not found

Looking for C++ include ddraw.h

Looking for C++ include ddraw.h - not found

Looking for C++ include dsound.h

Looking for C++ include dsound.h - not found

Looking for C++ include dinput.h

Looking for C++ include dinput.h - not found

Looking for C++ include dxgi.h

Looking for C++ include dxgi.h - not found

Looking for C++ include xaudio2.h

Looking for C++ include xaudio2.h - not found

Looking for include files windows.h, xinput.h

Looking for include files windows.h, xinput.h - not found

Found DirectX: TRUE missing components: DInput DSound XAudio2 XInput

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

Looking for sincosf in m - not found

Performing Test HAVE_RTL_OSVERSIONINFOW

Performing Test HAVE_RTL_OSVERSIONINFOW - Failed

Performing Test HAVE_GCC_WALL

Performing Test HAVE_GCC_WALL - Success

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

Looking for strings.h

Looking for strings.h - found

Looking for ctype.h

Looking for ctype.h - found

Looking for math.h

Looking for math.h - found

Looking for iconv.h

Looking for iconv.h - not found

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

Looking for strdup

Looking for strdup - found

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

Looking for fseeko

Looking for fseeko - not found

Looking for fseeko64

Looking for fseeko64 - found

Looking for sigaction

Looking for sigaction - not found

Looking for setjmp

Looking for setjmp - not found

Looking for nanosleep

Looking for nanosleep - found

Looking for sysconf

Looking for sysconf - not found

Looking for sysctlbyname

Looking for sysctlbyname - not found

Looking for pow in m

Looking for pow in m - found
[/details]

-------------------------

weitjong | 2020-03-22 08:42:22 UTC | #11

You must be new to auto-configure tools such as CMake. Those “not found” messages are not error in general. So you don’t have to worry about each and every one of them. Just need to check those you want it to be found but showed up as otherwise as it means you have something wrong in your build environment.

-------------------------

MZoltan32 | 2020-03-22 13:57:45 UTC | #12

but a headerfile is not found isnt it a problem? how to check those i need

you have the same messages?

-------------------------

JTippetts | 2020-03-22 14:24:12 UTC | #13

CMake performs a large number of checks or tests to determine things such as the presence of certain libraries, certain functions, compiler capabilities, and so on. If something critical to the project is missing, it will terminate the entire configure process. In some cases, a missing feature might trigger an alternate build configuration, rather than triggering a critical failure. The success/failure of your configure can be determined by noting whether the build files were written to the build directory. If invoking cmake from the command line you should see some lines at the end of your configure output to the effect of "Configuring done", "Generating done", "Build files have been written to {build path}". If you see errors there instead, then something is broken.

-------------------------

