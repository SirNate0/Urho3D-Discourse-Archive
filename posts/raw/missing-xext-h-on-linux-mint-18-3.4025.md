galileolajara | 2018-02-17 09:55:58 UTC | #1

Hi!

I'm running cmake_generic.sh to make a build tree on my Linux Mint 18.3 but I keep on receiving this error.
```
-- Could NOT find RoarAudio development library (missing:  SNDIO_LIBRARIES SNDIO_INCLUDE_DIRS) 
CMake Error at Source/ThirdParty/SDL/cmake/macros.cmake:73 (message):
  *** ERROR: Missing Xext.h, maybe you need to install the libxext-dev
  package?
Call Stack (most recent call first):
  Source/ThirdParty/SDL/cmake/sdlchecks.cmake:383 (message_error)
  Source/ThirdParty/SDL/CMakeLists.txt:929 (CheckX11)


-- Configuring incomplete, errors occurred!
See also "/opt/Urho3D/build-linux64/CMakeFiles/CMakeOutput.log".
See also "/opt/Urho3D/build-linux64/CMakeFiles/CMakeError.log".
```
I've installed libdirectfb-dev libegl1-mesa-dev mir-client-platform-mesa-devlibegl1-mesa-dev
libwayland-dev, wayland-protocols libx11-dev, libxcursor-dev, libxext-dev, libxi-dev, libxinerama-dev, libxrandr-dev, libxrender-dev, libxss-dev, libxxf86vm-dev
xorg-devel

I can see that there's Xext.h present on my /usr/include/X11/extensions but I keep on receiving such message.

Thanks in advance!

-------------------------

Modanung | 2018-02-18 10:06:25 UTC | #2

Welcome to the forums @galileolajara! :confetti_ball:

Maybe try: `./cmake_clean.sh` before `./cmake_generic.sh .`

-------------------------

galileolajara | 2018-02-18 10:04:25 UTC | #3

That did it! Thanks a lot! :smiley:

-------------------------

weitjong | 2018-02-18 14:45:03 UTC | #4

I have been bitten by this in the past as well. Some of the CMake checks for SDL are only performed once and exactly once during the initial build tree generation and the result of the checks are "erroneously" cached by the build system regardless of the check result. So even after installing the missing dev packages based on the initial CMake output and rerunning the CMake on the already generated build tree would not produce the desired result. Ideally the build system should not have cached failed check result and/or should recheck on the failed cases when the CMake rerun, however, in order to fix this we need to alter the build scripts in the 3rd-party SDL fork in our git subtree, which will increase our future effort to sync with SDL upstream if our fork differs from the origin by too much. Arguably, the SDL build scripts in our fork are already deviated from upstream, so we may as well don't care about the deviation and just fix everything to suit our need, and perhaps submit our improved version to upstream as PR.

-------------------------

xf200512 | 2022-01-19 01:49:41 UTC | #5

I also meet this issue in xubuntu20.04, but it can not be fixed with this solution `./cmake_clean.sh` before `./cmake_generic.sh .`

-------------------------

SirNate0 | 2022-01-19 01:55:42 UTC | #6

Hello, welcome to the community!

Did you install the required dependencies beforehand?

-------------------------

xf200512 | 2022-01-19 01:57:16 UTC | #7

Yes, I installed libx11-dev libgl1-mesa-dev libasound2-dev libpulse-dev libsdl2-dev

-------------------------

SirNate0 | 2022-01-19 02:18:39 UTC | #8

Maybe install libxext-dev? And I'm not sure, but I don't recall libsdl2-dev being a dependency, I think it's included and built with Urho as one of the Third Party libs.

-------------------------

xf200512 | 2022-01-19 03:25:07 UTC | #9

libxext-dev also installed

**sorry, as a new user, I am limited to 3 reply, see error on below:**

CMake Error at Source/ThirdParty/SDL/cmake/macros.cmake:73 (message):
  *** ERROR: Missing Xext.h, maybe you need to install the libxext-dev
  package?
Call Stack (most recent call first):
  Source/ThirdParty/SDL/cmake/sdlchecks.cmake:441 (message_error)
  Source/ThirdParty/SDL/CMakeLists.txt:1080 (CheckX11)
-- Configuring incomplete, errors occurred!
See also "/home/demo/github/Urho3D/script/CMakeFiles/CMakeOutput.log".
See also "/home/demo/github/Urho3D/script/CMakeFiles/CMakeError.log".

-------------------------

SirNate0 | 2022-01-19 03:02:51 UTC | #10

If you delete the build tree and start again, what exactly is the error message you get?

-------------------------

