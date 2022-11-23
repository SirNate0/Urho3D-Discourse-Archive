Devy | 2017-06-06 22:23:31 UTC | #1

Hello, I receive an error when using cmake.

Here is the process I went through to get to this point.

git clone https://github.com/urho3d/Urho3D

cd Urho3D

cmake .

I then receive this error:
    -- *** WARNING: You must have SDL_LoadObject() support for dynamic ALSA loading
-- *** WARNING: You must have SDL_LoadObject() support for dynamic PulseAudio loading
-- *** WARNING: You must have SDL_LoadObject() support for dynamic ESD loading
-- Could NOT find aRts development library (missing:  ARTS_LIBRARIES ARTS_INCLUDE_DIRS) 
-- *** WARNING: You must have SDL_LoadObject() support for dynamic NAS loading
-- Could NOT find RoarAudio development library (missing:  SNDIO_LIBRARIES SNDIO_INCLUDE_DIRS) 
CMake Error at Source/ThirdParty/SDL/cmake/macros.cmake:73 (message):
  *** ERROR: Missing Xext.h, maybe you need to install the libxext-dev
  package?
Call Stack (most recent call first):
  Source/ThirdParty/SDL/cmake/sdlchecks.cmake:383 (message_error)
  Source/ThirdParty/SDL/CMakeLists.txt:929 (CheckX11)

I have libxext-dev installed.

Any help would be nice! Thanks.

-------------------------

Modanung | 2017-06-07 09:02:41 UTC | #2

Did you install all required dependencies?
https://urho3d.github.io/documentation/HEAD/_building.html

And welcome to the forums! :)

-------------------------

artgolf1000 | 2017-06-08 00:16:47 UTC | #3

I never run 'cmake' directly, I always use these scripts such as cmake_android.sh, cmake_ios.sh, cmake_xcode.sh, cmake_vs2010.bat etc.

-------------------------

Devy | 2017-06-09 02:12:41 UTC | #4

I went through the documentation and installed all of the required dependences. I even updated gcc to 7.1.0 and updated Ubuntu from 14.04 to 16.04. No dice.

Using the build scripts gives the same error.

-------------------------

Devy | 2017-06-09 02:14:19 UTC | #5

Using the build script "./cmake_generic.sh" gives the same error. Although, I can use the build scripts for codeblocks. There are no errors when using that one.

-------------------------

weitjong | 2017-06-09 14:45:46 UTC | #6

Note that CMake caches previous detection result in the build tree. So, if you install new software deps to resolve the previously reported errors then you must either clear the cache first or nuke the old build tree first.

-------------------------

