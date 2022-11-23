walabulu4 | 2018-10-31 05:04:57 UTC | #1

Hi, I am fairly new to Linux and the pi. I followed all the instructions on the [https://github.com/urho3d/Urho3D/wiki/Getting-started-in-Linux](https://github.com/urho3d/Urho3D/wiki/Getting-started-in-Linux) page. however i get this error. 

    [ 75%] Linking CXX static library ../../lib/libUrho3D.a
    Merging all archives into a single static library using ar
    [ 75%] Built target Urho3D
    [ 75%] Linking CXX executable ../../../bin/Urho3DPlayer
    /usr/bin/ld: cannot find -lGLESv1_CM
    /usr/bin/ld: cannot find -lGLESv1_CM
    collect2: error: ld returned 1 exit status
    Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/build.make:95: recipe for target 'bin/Urho3DPlayer' failed
    make[2]: *** [bin/Urho3DPlayer] Error 1
    CMakeFiles/Makefile2:1516: recipe for target 'Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/all' failed
    make[1]: *** [Source/Tools/Urho3DPlayer/C[ 75%] Linking CXX static library ../../lib/libUrho3D.a
    Merging all archives into a single static library using ar
    [ 75%] Built target Urho3D
    [ 75%] Linking CXX executable ../../../bin/Urho3DPlayer
    /usr/bin/ld: cannot find -lGLESv1_CM
    /usr/bin/ld: cannot find -lGLESv1_CM
    collect2: error: ld returned 1 exit status
    Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/build.make:95: recipe for target 'bin/Urho3DPlayer' failed
    make[2]: *** [bin/Urho3DPlayer] Error 1
    CMakeFiles/Makefile2:1516: recipe for target 'Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/all' failed
    make[1]: *** [Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/all] Error 2
    Makefile:149: recipe for target 'all' failed
    make: *** [all] Error 2
    MakeFiles/Urho3DPlayer.dir/all] Error 2
    Makefile:149: recipe for target 'all' failed
    make: *** [all] Error 2


any help would be appreciated. Thanks in advance!

-------------------------

Miegamicis | 2018-10-31 06:47:05 UTC | #2

Looks like you don't have the OpenGL installed on your machine.

-------------------------

weitjong | 2018-10-31 11:00:28 UTC | #3

RPI build is slightly different than native Linux build. You may want to follow the steps outlined in https://urho3d.github.io/documentation/HEAD/_building.html#Building_RaspberryPi instead.

-------------------------

walabulu4 | 2018-10-31 13:26:26 UTC | #4

I'm a little confused. I was trying to build directly on my raspberry pi. Do i need a second Linux machine to build on?

-------------------------

walabulu4 | 2018-10-31 13:31:38 UTC | #5

I have openGL installed. I can run the glxgears demo

-------------------------

weitjong | 2018-10-31 14:24:14 UTC | #6

You did not say earlier and I assumed you were cross-building, which is by the way much easier and faster to get thing done. I have not done the direct build on RPI for a long while but our build system should be able to generate the Makefile project for building directly on the Raspberry Pi itself. Provided, you have all the prerequisite dev software packages properly installed, something like: libx11-dev, libasound2-dev, libpulse-dev, libdbus-1-dev, libreadline6-dev, libudev-dev, and libevdev2. This is on top of the usual build-essential package. Also, ensure you use the right build options for CMake for the Makefile project generation. We have provided "script/cmake_rpi.sh" for such occasion, which basically passes a crucial flag to inform the build system to target RPI platform.

Good luck.

-------------------------

walabulu4 | 2018-11-01 00:22:10 UTC | #7

Thank you so much! I managed to get it working with running the cmake_rpi.sh file. When I try opening a sample file in the bin folder using
    `./Urho3DPlayer 01_HelloWorld`
I get the error
        [Wed Oct 31 20:13:34 2018] ERROR: Failed to initialise SDL subsystem: 
        [Wed Oct 31 20:13:34 2018] INFO: Opened log file /home/pi/.local/share/urho3d/logs/01_HelloWorld.log
        [Wed Oct 31 20:13:34 2018] INFO: Created 3 worker threads
        [Wed Oct 31 20:13:34 2018] INFO: Added resource path /home/pi/Urho3D-master/bin/Data/
        [Wed Oct 31 20:13:34 2018] INFO: Added resource path /home/pi/Urho3D-master/bin/CoreData/
        [Wed Oct 31 20:13:34 2018] INFO: Added resource path /home/pi/Urho3D-master/bin/Autoload/LargeData/
        [Wed Oct 31 20:13:34 2018] ERROR: Could not create window, root cause: ''

-------------------------

weitjong | 2018-11-01 01:55:24 UTC | #8

Have you dropped to text mode? Kill the Gnome/KDE desktop to conserve CPU power and memory just for Urho3D. Also do this as stated in our online doc. 

* Raspberry Pi: Model B revision 2.0 with at least 128 MB of 512 MB SDRAM allocated for GPU.

-------------------------

walabulu4 | 2018-11-01 05:04:58 UTC | #9

Yep i did both! it still throws the same errors.

-------------------------

weitjong | 2018-11-01 05:57:09 UTC | #10

FWIW, have you tried the prebuilt binary on your device? If it works then probably you need to rebuild from a new build tree. Sometimes after try and error, CMake still caches the wrong bits and interferes with the build tree generation and therefore the build result becomes wrong also.

-------------------------

weitjong | 2018-11-02 01:01:22 UTC | #11

One more thing. You have to use latest master from GitHub if you are using Raspbian Stretch or newer version.

-------------------------

walabulu4 | 2018-11-02 01:47:53 UTC | #12

How do I make sure its the newest version? i just use
    git clone https://github.com/urho3d/Urho3D

-------------------------

weitjong | 2018-11-02 06:14:33 UTC | #13

The commits related to Raspbian Stretch build support were added to master branch around December last year. We have not made any release since then. But if you just cloned the repo recently then you should be ok. So it is something else that caused your runtime issue.

-------------------------

walabulu4 | 2018-11-02 04:23:31 UTC | #14

I re-downloaded and remade it. I now get this error at runtime. I am using just the command line and running at 680x420.
    pi@DuckPi:~/Urho3D/bin $ ./Urho3DPlayer 01_HelloWorld
    [Fri Nov  2 00:20:02 2018] INFO: Opened log file /home/pi/.local/share/urho3d/logs/01_HelloWorld.log
    [Fri Nov  2 00:20:02 2018] INFO: Created 3 worker threads
    [Fri Nov  2 00:20:02 2018] INFO: Added resource path /home/pi/Urho3D/bin/Data/
    [Fri Nov  2 00:20:02 2018] INFO: Added resource path /home/pi/Urho3D/bin/CoreData/
    [Fri Nov  2 00:20:02 2018] INFO: Added resource path /home/pi/Urho3D/bin/Autoload/LargeData/
    [Fri Nov  2 00:20:02 2018] INFO: Adapter used Broadcom VideoCore IV HW
    [Fri Nov  2 00:20:02 2018] INFO: Set screen mode 640x480 fullscreen monitor 0
    [Fri Nov  2 00:20:02 2018] INFO: Initialized input
    [Fri Nov  2 00:20:02 2018] INFO: Initialized user interface
    [Fri Nov  2 00:20:02 2018] INFO: Initialized renderer
    ALSA lib pcm_hw.c:1794:(_snd_pcm_hw_open) card is not defined
    [Fri Nov  2 00:20:02 2018] ERROR: Could not initialize audio output
    [Fri Nov  2 00:20:02 2018] INFO: Initialized engine
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:1,1 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:26,174 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:371,380 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:372,212 Unexpected token '!'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:386,64 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:386,103 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:389,25 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:391,258 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:407,19 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:407,190 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:412,262 Unexpected token '&'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:413,226 Expected identifier
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:413,226 Instead found '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147057,1250 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147064,143 Expected identifier
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147064,143 Instead found '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147109,523 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147118,879 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147142,371 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147143,428 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147143,434 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147173,280 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147173,286 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147173,310 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147173,316 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147173,322 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147173,330 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147173,336 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147173,339 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147173,342 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147206,319 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147206,1567 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147206,1572 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147225,825 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147225,831 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147226,156 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147226,168 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147272,36 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147280,676 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147300,1521 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147300,1529 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147300,1537 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147300,1545 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147309,377 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147309,5089 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147310,201 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: 01_HelloWorld:147326,2609 Unexpected token '<unrecognized token>'
    [Fri Nov  2 00:20:03 2018] ERROR: Failed to compile script module 01_HelloWorld

-------------------------

walabulu4 | 2018-11-02 06:07:00 UTC | #15

Oh, I just needed it to use 

    ./01_HelloWorld
and not
`    ./Urho3DPlayer 01_HelloWorld`

Thanks for all the help!

-------------------------

weitjong | 2018-11-02 06:13:14 UTC | #16

If using the player then you need to specify the script name with the extension as well.

-------------------------

walabulu4 | 2018-11-02 16:50:02 UTC | #17

Once I open an example I cant figure out how to quit?

-------------------------

weitjong | 2018-11-03 02:13:24 UTC | #18

Read this section of the online doc. HTH

https://urho3d.github.io/documentation/HEAD/_examples.html

-------------------------

walabulu4 | 2018-11-03 03:09:11 UTC | #19

OH then it definitely just got stuck. Ill try it out later today again

-------------------------

walabulu4 | 2018-11-03 04:00:20 UTC | #20

I tried a couple of the pre-compiled examples and tried some through the player. They started but I could not input anything. Im pretty sure it was frozen.

EDIT: 
Wait now i just keep getting this error 
    [Fri Nov  2 23:59:21 2018] INFO: Opened log file /home/pi/.local/share/urho3d/logs/Editor.as.log
    [Fri Nov  2 23:59:21 2018] INFO: Created 3 worker threads
    [Fri Nov  2 23:59:21 2018] INFO: Added resource path /home/pi/Urho3D/bin/Data/
    [Fri Nov  2 23:59:21 2018] INFO: Added resource path /home/pi/Urho3D/bin/CoreData/
    [Fri Nov  2 23:59:21 2018] INFO: Added resource path /home/pi/Urho3D/bin/Autoload/LargeData/
    * failed to add service - already in use?

-------------------------

weitjong | 2018-11-03 04:25:16 UTC | #21

Just to point out the obvious and make sure we are on the same page, when you using the prebuilt binary on Raspbian Stretch then you have to use "snapshot" versions instead of "1.7" release version.

As for your last error, I have never seen it before. In the past I remember one of the RPI user reported that the sample ran but he got no input. However, eventually he managed to solve that problem after installing missing dev packages (I think) and rebuild. Ensure you have the libdbus-1-dev, libudev-dev, and libevdev2 installed.

-------------------------

