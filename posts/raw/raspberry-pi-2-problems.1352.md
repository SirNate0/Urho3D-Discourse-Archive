toliaferrode | 2017-01-02 01:07:03 UTC | #1

Greetings. 

Just got a new Raspberry Pi 2 and a small TV to test it with. Tried compiling Urho3D from the source on the github.io site and from the master, got this:

[code]
./cmake_generic.sh $URHO3D_HOME
-- The C compiler identification is GNU 4.6.3
-- The CXX compiler identification is GNU 4.6.3
-- Check for working C compiler: /usr/bin/gcc
-- Check for working C compiler: /usr/bin/gcc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Found Broadcom VideoCore firmware: /opt/vc/lib/libbcm_host.so;/opt/vc/lib/libEGL.so;/opt/vc/lib/libGLESv2.so /opt/vc/include;/opt/vc/include/interface/vcos/pthreads
-- Looking for include file stdint.h
-- Looking for include file stdint.h - not found.
-- Found ALSA: /usr/lib/arm-linux-gnueabihf/libasound.so (found version "1.0.25") 
-- The ASM compiler identification is GNU
-- Found assembler: /usr/bin/gcc
-- Performing Test COMPILER_HAS_HIDDEN_VISIBILITY
-- Performing Test COMPILER_HAS_HIDDEN_VISIBILITY - Failed
-- Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY
-- Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY - Failed
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR - Failed
-- Performing Test COMPILER_HAS_DEPRECATED
-- Performing Test COMPILER_HAS_DEPRECATED - Failed
cc1plus: error: bad value (cortex-a7) for -mcpu switch
CMake Error at CMake/Modules/Urho3D-CMake-common.cmake:756 (message):
  The configured compiler toolchain in the build tree is not able to handle
  all the compiler flags required to build the project with PCH enabled.
  Please kindly update your compiler toolchain to its latest version.  If you
  are using MinGW then make sure it is MinGW-W64 instead of MinGW-W32 or
  TDM-GCC (Code::Blocks default).  Or disable the PCH build support by
  passing the '-DURHO3D_PCH=0' when retrying to configure/generate the build
  tree.  However, if you think there is something wrong with our build system
  then kindly file a bug report to the project devs.
Call Stack (most recent call first):
  CMake/Modules/Urho3D-CMake-common.cmake:817 (enable_pch)
  CMake/Modules/Urho3D-CMake-common.cmake:882 (setup_target)
  Source/Urho3D/CMakeLists.txt:200 (setup_library)


-- Configuring incomplete, errors occurred!

[/code]

Tried building it without sound as mentioned above and I got another error. Then tried the cross-compiling option and I get the same errors as above.

Additionally I checked out the arm7 package for the Pi 2 on the github.io page and it had some glitches including not being able to move the mouse cursor and the character model rendering strangely.

Thanks in advance for your help.

-------------------------

weitjong | 2017-01-02 01:07:04 UTC | #2

Welcome to our forum.

First of all, the term PCH here does not have anything to do with audio. In our build system the PCH refers to "precompiled header". When the PCH is on, we instructs CMake to execute a compilation process early on using all the gathered compiler flags and compiler defines that would have been used in your build later. If you have a problem in this early test then you probably would get the same problem too later in your build (even when you bypass the problem by setting URHO3D_PCH=0. The use case of this option is very specific when you really want to turn off the precompiled header support. It is not to be used to bypass problem not related to precompiled-header, as you have found out.

Anyway, back to your problem. If you are building natively on the RPI device itself then upgrade your GCC installation to the latest version you can find in your distro's repository. The root cause of your error is this line:

[code]cc1plus: error: bad value (cortex-a7) for -mcpu switch[/code]
You need to find a GCC version that understands this compiler flag: -mcpu=cortex-a7. If you can't upgrade for some reasons then you can fallback by using this build option when calling cmake_rpi.sh: -DRPI_ABI=armeabi-v6. This will force the build system to fallback to use -mcpu=arm1176jzf-s (i.e. RPI 1).

The same applies when you are cross-compiling. If you use the download sources recommended by our documentation page here ([urho3d.github.io/documentation/H ... aspberryPi](http://urho3d.github.io/documentation/HEAD/_building.html#Building_RaspberryPi)) then you should be fine. This combination of cross-compiling toolchain and RPI sysroot has been tested continuously in our CI build. Those RPI software packages that you downloaded from sf.net are in fact just build artifacts from those CI builds.

As for those glitches. I have no idea on the mouse cursor glitch. I have not seen it yet but I only have RPI 1 to play with. The glitch with the character model skinning is a known issue. The GPUs on RPI 1 and 2 are the same and they are only capable to handle half the amount of "bones" that otherwise Urho3D engine supports on mobile platforms. And our sample apps are not specifically written for RPI.

-------------------------

toliaferrode | 2017-01-02 01:07:05 UTC | #3

Thanks for the welcome.

Ah ok I just assumed, sorry about that. Precompiled header, not a sound codec as I thought. I was thinking PCM.

As far as I can tell the latest and only GCC in Raspbian is 4.6. I noticed that Wikipedia has the latest as 5.x. So I suppose I'd have to compile it myself? In that case I'd rather just use the nice packages on the github.io. I don't necessarily need to compile stuff just yet and maybe not for a long while.

Ah ok, I thought the mesh problems might have to do with bones as I've read that on the forums a few times.

Yes, the mouse cursor problem happens with all samples as far as I know now. Except curiously the editor works with minimal problems. The only visible problem is that a second black mouse cursor seems to freeze and stay in the same place in the editor, but an active white mouse cursor can move. Very interesting. But I gotta say that running the editor (and indeed the samples) have blown me away. 

This engine really is some nice technology and I want to thank you and the community for it.

Thanks again!

-------------------------

weitjong | 2017-01-02 01:07:05 UTC | #4

I have actually not played with my RPI for quite some time now. For the mouse cursor glitch, it could be caused by more recent change, i.e if I were to test it on my RPI 1 now it would probably show the problem also. There is no "OS cursor" support on RPI platform,  so the OS cursor (black one) should remain hidden all the time on RPI. The white cursor is a software rendered cursor and it is only rendered when requested by the app, such as editor. 

I suggest you learn how to build Urho3D from its source. It would allow you to learn the library quicker by allowing you to study its source code directly, fix the bug by your own, and even contribute your bug fixes or other improvement back to community.

-------------------------

toliaferrode | 2017-01-02 01:07:05 UTC | #5

Is Urho3D fully software rendered on the Pi? Just wondering as I'm not up to snuff on this stuff.

Thank you for the suggestion. I actually finally got Urho3D compiled on my laptop about a month ago. Though I am quite a bit rusty with my C++.

-------------------------

weitjong | 2017-01-02 01:07:05 UTC | #6

The 3D and 2D graphics are rendered using OpenGL ES taking advantage of Pi's GPU, if that's what you asking. I was referring to soft rendered cursor in my earlier post just to contrast it with "hard" OS cursor which does not exists on Pi, at least in our RPI port implementation because the port does not use X11.

-------------------------

toliaferrode | 2017-01-02 01:07:06 UTC | #7

Ah I see, thanks. And thanks again for all your help.

-------------------------

