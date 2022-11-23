hinchyk | 2021-04-10 16:41:28 UTC | #1

I am trying to build Urho3D with one of the provided scripts.
This is command I'm using:
```
.\cmake_mingw.bat Build -DURHO3D_OPENGL=1 -DURHO3D_WIN32_CONSOLE=1
```
 and the response:
```
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


CMake Error at CMake/Modules/FindDirectX.cmake:84 (message):
  Could not find MinGW system root.  Use MINGW_SYSROOT environment variable
  or build option to specify the location of system root.
Call Stack (most recent call first):
  CMake/Modules/UrhoCommon.cmake:470 (find_package)
  CMakeLists.txt:45 (include)


-- Configuring incomplete, errors occurred!
See also "D:/Gamedev/Urho3D/Build/CMakeFiles/CMakeOutput.log".
```
Please help!

-------------------------

SirNate0 | 2021-04-10 15:50:35 UTC | #2

You have a `C` in URHO: DUR**C**HO3D_OPENGL=1

Also, welcome to the forum!

-------------------------

hinchyk | 2021-04-10 16:43:48 UTC | #3

Thank you!
I corrected the spelling, and response is still the same.
I also corrected spelling in post.

-------------------------

SirNate0 | 2021-04-10 17:36:15 UTC | #4

Clear the cache and retry. It seems like it is still trying to find the direct x files, so I suspect it might be a cache issue (hopefully).

-------------------------

Modanung | 2021-04-10 18:21:21 UTC | #5

Might this be a hint?
> Could not find MinGW system root.  Use MINGW_SYSROOT environment variable
  or build option to specify the location of system root.

-------------------------

hinchyk | 2021-04-10 18:54:30 UTC | #6

Ok I used another MinGW distribution (the one given in tutorials), and it worked.

-------------------------

SirNate0 | 2021-04-10 20:27:01 UTC | #7

What version were you originally using and which one worked? We might need to update the documentation if it wasn't clear!

-------------------------

