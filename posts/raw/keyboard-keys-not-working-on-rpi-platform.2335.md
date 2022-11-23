OMID-313 | 2017-01-02 01:14:48 UTC | #1

Hi all,

I just recently installed Urho3D on Raspberry Pi 3.
But the problem is that when I run each of the example games (./05_AnimatingScene for example), the games opens and I see the scene, but the keyboard keys don't work, and I'm not able to move or do anything.
All I can do is Ctrl+C to quit, which sometimes doesn't work either!!

How can I solve this !!?

-------------------------

OMID-313 | 2017-01-02 01:14:49 UTC | #2

Any suggestions !!?

-------------------------

rku | 2017-01-02 01:14:49 UTC | #3

Ctrl+C is a terminal command. If it sometimes does not work then likely something is wrong with your system. You should test on a fresh install and provide us information on build you are using. What flags you used to build it or if it was build from website, and what distribution is installed on PI. Maybe then someone with right combination can test this and verify if it is broken or not.

-------------------------

weitjong | 2017-01-02 01:14:49 UTC | #4

I have seen a few users reporting input problem in Urho3D 1.6. I am partly to blame for this. Ever since the SDL 2.0.4 update, I have not actually tested the build on an actual RPI board. My old RPI is now being used as a mini server and I didn't want to mess with it at the time. Bought myself a brand new RPI 3 last month but I haven't spent quality time with it yet.  :laughing: 

I think this is what happened. In the past before SDL 2.0.4 our RPI port still relied on the X11 for the input. After SDL 2.0.4 update, our RPI port does not use xinput anymore, if I recall correctly. It is a side effect from using SDL's own CMakeLists.txt which auto-configures its configuration file. At that time I thought it is as intended and didn't investigate it further.

-------------------------

Victor | 2017-01-02 01:14:50 UTC | #5

Not sure if this is related, however I've been experiencing some issues with the EventSystem on Mac specifically where the events do not work... sometimes. UI elements, and everything else will load up at the start of the program, however no events will fire. This is currently a hard issue for me to duplicate since I've only seen it happen on OSX, and it doesn't happen all of the time, just sometimes. Almost like a thread is running in the background and hasn't fully completed.

Edit: Most of my development is done on a Windows machine which doesn't seem to have the issue.

-------------------------

OMID-313 | 2017-01-02 01:14:51 UTC | #6

So, after all these, what can I do !?
Somebody suggested to check the /dev/input in the logs.
How can I see the logs of Urho3D !?

Any other suggestions !?

-------------------------

weitjong | 2017-01-02 01:14:51 UTC | #7

I think I have already given enough pointer on how to troubleshoot the problem. If you still do not understand how to do it then may be you can try the older 1.5 release instead while waiting the devs to fix this issue.

-------------------------

OMID-313 | 2017-01-02 01:14:51 UTC | #8

[quote="weitjong"]I think I have already given enough pointer on how to troubleshoot the problem. If you still do not understand how to do it then may be you can try the older 1.5 release instead while waiting the devs to fix this issue.[/quote]

Ok. I'll try version 1.5.

Just a question:
Which command must be executed instead of the following in the installation?
[code]git clone https://github.com/urho3d/Urho3D[/code]

-------------------------

OMID-313 | 2017-01-02 01:14:52 UTC | #9

Ok.
I installed the version 1.5.
But now it gives another error :

[code]ERROR: Could not create window, root cause: 'Could not create GLES windows surface'[/code]

Now what should I do !!?

-------------------------

weitjong | 2017-01-02 01:14:54 UTC | #10

I just want to add what I have read from SDL readme file for RPI platform.
[quote]================================================================================
Features
================================================================================

 * Works without X11
 * Hardware accelerated OpenGL ES 2.x
 * Sound via ALSA
 * Input (mouse/keyboard/joystick) via EVDEV
 * Hotplugging of input devices via UDEV

[/quote]
It seems the EVDEV does not pipe those input events correctly into our engine yet. Anyway, SDL 2.0.5 is just out now. Whoever does the SDL version upgrade later can double check this.

-------------------------

Victor | 2017-01-02 01:15:01 UTC | #11

Ok, so for Mac I discovered something interesting. When the keys aren't immediately working I noticed that if I wait 10-30 sec the UI and keys will start being responsive. Not sure if this helps, and again, I've only seen this so far on Mac, not Windows.

-------------------------

weitjong | 2017-01-02 01:15:03 UTC | #12

[quote="Victor"]Ok, so for Mac I discovered something interesting. When the keys aren't immediately working I noticed that if I wait 10-30 sec the UI and keys will start being responsive. Not sure if this helps, and again, I've only seen this so far on Mac, not Windows.[/quote]
Whatever it is that causing your issue on Mac is off-topic in this thread. I have updated the thread's subject to make this point clear.

-------------------------

miz | 2017-02-08 15:55:07 UTC | #13

Did this issue ever get resolved? I'm having trouble - the SDL text input event doesn't seem to be triggering. (at least OnTextInput isn't being called in UIElement subclasses)

-------------------------

weitjong | 2017-02-08 16:38:55 UTC | #14

Nothing has changed since then. I can confirm the issue exists though at the very least, however, I have limited free time now to investigate further and fix it. You are all welcome to give it a try.

-------------------------

miz | 2017-02-08 17:27:11 UTC | #15

Any suggestions for where/how to start fixing this/ narrowing down the problem?

-------------------------

weitjong | 2017-02-08 17:37:48 UTC | #16

I have mentioned this before.

[quote="weitjong, post:10, topic:2335"]
It seems the EVDEV does not pipe those input events correctly into our engine yet.
[/quote]

The uglier solution is to add back X11 stack just in order to get the keyboard input. Note that this was what we have done in the past version. But I consider that to be a mistake. We should not depend on X11 if I understood the Release Notes from SDL correctly. Perhaps I have a wrong understanding though. The latter can be done by simply flipping a switch in the generated SDL_config.h (I think).

-------------------------

miz | 2017-02-08 20:42:21 UTC | #17

OK, so I solved the problem! Did some digging around, found this - https://bugzilla.libsdl.org/show_bug.cgi?id=3469 so I swapped the SDL/src/core/linux folder with the one mercurial are using and rebuilt everything.

-------------------------

weitjong | 2017-02-09 03:12:11 UTC | #18

Good to know that. Thanks.

-------------------------

miz | 2017-02-14 14:47:01 UTC | #19

I am having a strange problem with this now. The text input works until either CTRL or ALT are pressed. Once either of these keys has been pressed text input no longer works and the game needs to be closed and opened again to regain text input. Any ideas what could be causing this? Not sure where to look

-------------------------

weitjong | 2017-02-17 17:32:56 UTC | #20

This issue is now fixed in the master branch.

-------------------------

miz | 2017-02-20 17:10:08 UTC | #21

[quote="weitjong, post:20, topic:2335, full:true"]
This issue is now fixed in the master branch.
[/quote]

I just built from master branch and not sure if keyboard is working (doesn't seem to be) but mouse definitely isn't...

Did you test it on a Pi?

-------------------------

weitjong | 2017-02-20 18:22:35 UTC | #22

Yes, I did test on a RPI 3 this time. Only the keyboard though.

-------------------------

weitjong | 2017-02-20 18:33:56 UTC | #23

Just tested with the mouse attached. It is not only working on my side but it is hot-pluggable too.

-------------------------

miz | 2017-02-20 18:39:07 UTC | #24

Do I maybe need to install some evdev or udev libraries on the pi for it to work? I'm still getting neither working

-------------------------

miz | 2017-02-20 18:44:34 UTC | #25

Also, what operating system are you running on your Pi?

-------------------------

weitjong | 2017-02-21 00:16:13 UTC | #26

I am using Raspbian Jessie Lite. The prerequisite software packages are listed in https://urho3d.github.io/documentation/1.6/_building.html#Building_Prerequisites.

-------------------------

miz | 2017-08-31 13:56:13 UTC | #27

I never managed to get it working on 1.6 (tried doing everything 'by the book' following all instructions on build page), gave up and went back to 1.5 as still the input didn't work. Since 1.7 came out with a bit in the changelog saying rpi stuff was fixed I thought I would give it a go again. With Raspbian Jesse I had the same problem - input didn't work in the samples. With Raspbian Stretch (new) there is a more worrying problem. The GLES so on the pi files have been renamed (and changed i presume) to have 'brcm' in the name, i.e libbrcmGLES.so so I get '/usr/bin/ld: cannot find -lGLESv2' type errors when trying to build urho. So optimistically I tried changing #define DEFAULT_EGL and following lines in Source/ThirdParty/SDL/src/video/SDL_egl.c to look for the brcm named files - it had no effect. Not really sure what to try next, would love to get 1.7 going!

-------------------------

weitjong | 2017-08-31 14:08:25 UTC | #28

Sorry to hear that. Maybe you could try to build a simple SDL app from elsewhere to see or to learn how to get it to work. Urho relies on SDL for its input subsystem.

I haven't heard of the new Raspbian before. Wonder why they do that.

-------------------------

miz | 2017-09-01 09:41:07 UTC | #29

I found this as to why it might be:

 "As the mesa arm side GL driver is going to become the standard in the future, we’d like to avoid confusion when linking with either the arm side driver (/usr/lib/arm-linux-gnueabihf) or the gpu driver (/opt/vc/lib).

As such applications built to use the gpu driver should now link with libbrcmEGL.so/libbrcmGLESv2.so rather than the ambiguous libEGL.so/libGLESv2.so libs." - https://www.raspberrypi.org/blog/raspbian-stretch/

Also, finally got it building (running rpi-update on Stretch pulled in old name GLES libs which fixed GL build/linking errors) and input working - it turns out all I needed was to add libibus-1.0-dev (labelled as optional in build instructions but I found it not to be optional for RPi with versions of urho3d 1.6+)

While most samples worked fine, 19_VehicleDemo caused a flashing screen (and nothing else) and the ragdoll sample had strangely all the left legs of the dummies stretching out to a point in the sky.

-------------------------

weitjong | 2017-09-01 10:03:29 UTC | #30

Thanks for the info. Will have a closer look on the Raspbian Stretch when I have extra time. I could be wrong but don't think ibus package solved your keyboard issue. Probably it is what got installed together as part of the ibus package.

The GPU on the RPI is not as powerful as we want. The artifact you observed is a known limitation.

-------------------------

weitjong | 2017-12-09 15:53:22 UTC | #31

We have a new dev branch “upgrade-sdl-2.0.7” which has the attempted fix to get Urho3D/RPI port working for Raspbian Stretch. Can you give the branch a try and report back any issue. Thanks.

-------------------------

miz | 2018-02-20 10:37:07 UTC | #32

I have just come back to this. I can't see that dev branch but I assume it was merged into master? I have found that with Urho3D 1.7 and Raspbian Jessie, key down works as it should but the text input stops working after modifiers are pressed (CTRL ALT SHIFT) and only way to get text input after that is to close and open the game. Any ideas where this issue might be coming from? Have you come across this?

-------------------------

weitjong | 2018-02-20 11:16:11 UTC | #33

Yes, it is in the master branch now. No, I haven’t noticed it on Jessie.

-------------------------

miz | 2018-02-20 12:06:59 UTC | #34

I've just built Urho3D from the master branch on a clean Stretch image and the input (mouse and keyboard) is not working

-------------------------

weitjong | 2018-02-20 14:24:45 UTC | #35

The last SDL upgrade for Raspbian Stretch is more about fixing the video support. I have not experienced any keyboard and mouse input problem whatsoever in my last test. I wish there is more I can help but in this case I have running out of idea. For what it's worth, I usually use the lite version, boot in text mode and without any DE.

-------------------------

miz | 2018-02-20 14:40:40 UTC | #36

I'll try a few things and report back

-------------------------

miz | 2018-02-21 10:36:12 UTC | #37

Let me tell you everything I ran on a clean, latest image of stretch lite, if you could reply with all your steps that get it working then hopefully we can get somewhere. 
I did this:
sudo apt-get update
sudo apt-get install git
sudo apt-get install cmake
sudo apt-get install libibus-1.0-dev
sudo apt-get install libasound2-dev
git clone https://github.com/urho3d/Urho3D.git
cd Urho3D
./cmake_rpi.sh ../build
cd ../build
make -j4

I then launch samples and the input does not work

-------------------------

weitjong | 2018-02-21 14:42:05 UTC | #38

Immediately I can tell you one big difference. I cross-compiled to target RPI instead of building it natively on the device itself. I installed all the prerequisite packages as listed in the online documentation. You can get a hint of the list using this line.

https://github.com/urho3d/rpi-sysroot/blob/sysroot-update-trigger/Rakefile#L35

Having said that, building natively on a device should work too provided all the prerequisite packages are installed. And probably I don't have the time to repeat again all the steps that I have taken. Perhaps it is just me but I don't think there is anything special about those steps. It is almost like how I set up another Linux VM from scratch.

-------------------------

miz | 2018-02-21 16:34:30 UTC | #39

Once I install those additional libs things work! It's a case of some 'optional' libraries (as listed on the building urho3d page) aren't so optional I suppose.

-------------------------

weitjong | 2018-02-21 17:09:27 UTC | #40

Glad to hear that. If you can pinpoint exactly what is/are the non optional then we can update the doc accordingly.

-------------------------

