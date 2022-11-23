arcadeperfect | 2021-06-09 02:04:24 UTC | #1

Hi

Build finished on Raspberry Pi 4 but when I got to run a demo, get the following error:

[Tue Jun  8 22:01:09 2021] ERROR: Could not create window, root cause: 'OpenGL support is either not configured in SDL or not available in current SDL video driver (x11) or platform'

Any help appreciated

Thanks

-------------------------

SirNate0 | 2021-06-09 02:12:00 UTC | #2

Try running it from a terminal and not a desktop? Though it's been quite I few years since I've worked with Urho on a Pi...

Also, make sure the right libraries are installed. That's one issue people on the Pi 4 ran into.

https://github.com/libsdl-org/SDL/issues/3678

And welcome to the forum!

-------------------------

arcadeperfect | 2021-06-09 21:10:35 UTC | #3

I did run it from a terminal, albeit one loaded through the desktop. Do you mean running it from a terminal without X loaded at all?

-------------------------

SirNate0 | 2021-06-09 22:46:02 UTC | #4

Yes, without X loaded at all. But again, this may not be the cause of the problem at all. It's just my recollection of how it worked several years ago.

-------------------------

weitjong | 2021-06-10 03:48:23 UTC | #5

Yes. Like what Sirnate0 said, Urho3D Pi port doesn’t required X at all. Last time I had my Pi configured to use text mode on boot, but I think just for testing you can just boot with single-user-mode or kill X before executing the binary. Having said that, even when X still runs in the background, it should not stop the app from initializing. It will just suck the computing juice from the Pi for nothing. What I think that can fail the initialization is the newer Raspbian switched from VC graphic driver to a standard driver. I cannot recall the exact specific now, so take it with some salt. I also recall I/we have done something about it in the master branch to deal with it. The new code in the master may not be well tested yet. I was waiting for my new Pi 4 at the time and when the thing finally arrived, it just collecting dust in my study as I have moved on to other thing. Are you using master branch BTW?

-------------------------

arcadeperfect | 2021-06-10 14:21:59 UTC | #6

Yes, master branch

If I boot into CLI I get a different error: 

ERROR: Failed to initialize SDL subsystem: No available video device

And before you ask, yes I have a monitor connected via HDMI :wink:

Apologies if I'm missing basic things here. Is it an SDL config issue? I hadn't even heard of SDL until yesterday but if that's the issue happy to research it myself. But it would be good to know if I'm even on the right track.

-------------------------

weitjong | 2021-06-10 14:47:21 UTC | #7

How did you build your engine from source? Show us your exact build config that you pass to CMake during the initial configuration phase.

-------------------------

arcadeperfect | 2021-06-10 16:32:22 UTC | #8

I used the cmake_generic shell script with -DURHO3D_SAMPLES=1

After you asked that, I went back to the script folder and realized there's also a cmakr_rpi script. I just ran a build with that script and now I get a new error ...

Can't find a way to dump the error to a file so here's a photo. 

![IMG_0537|690x145](upload://yfDf2VxK7V8Lv8IJOsHKPnvXkPr.jpeg)

-------------------------

weitjong | 2021-06-10 17:11:05 UTC | #9

Did you pass anything else when you invoke the `cmake_rpi.sh`? Any build options or build config that you use? It is also not clear to me whether you were building on the Pi itself or you use a cross-compiling toolchain. The options to pass may be slightly different between these two approaches. You may try to pass "-D RPI_ABI=RPI4" and/or "-D URHO3D_64BIT=1" if you have 64 bit Raspbian on your Pi4, for example.

-------------------------

arcadeperfect | 2021-06-10 18:09:32 UTC | #10

No, didn't pass anything else. I'm building directly on the pi, with a fresh install of 32 bit Raspberry Pi OS. For libs I used:

libxrandr-dev
libasound2-dev
libgles2-mesa-dev

The command is just

./cmake_rpi.sh ~/urho -DURHO3D_SAMPLES=1


I'll try “-D RPI_ABI=RPI4” see if it helps

thanks for the responses

-------------------------

arcadeperfect | 2021-06-10 19:58:47 UTC | #11

Aha! That flag fixed it. 

Thanks for the help!

-------------------------

arcadeperfect | 2021-06-10 20:15:42 UTC | #12

Ok, so it works from X. But when I run from cli, I still get 
"Could not create window, root cause: 'No available video device'"

So close :woozy_face:

This time my make command was simply:
./cmake_generic.sh ~/urho1-D RPI_ABI=RPI4

-------------------------

weitjong | 2021-06-11 04:47:49 UTC | #13

Glad to hear that. Without X then the game engine supposes to use the SDL support for KMS/DRM. Unfortunately, that’s the part where I said earlier it may not be well tested yet. There are also many improvements made in the upstream SDL regarding KMS/DRM that haven’t got merged yet in our subtree. Anyway, if I were you I would check the CMake cache to see if KMS/DRM support is enabled in your build. If it did then try to export an env-var to tell SDL subsystem to use it as the video driver instead of the default X11 video driver from SDL. I cannot remember the specific variable name at the moment. It should starts with “SDL_”. You are ahead of me now in this regards. So take what I have just said with a grain of salt.

-------------------------

arcadeperfect | 2021-06-11 14:32:11 UTC | #14

Gotcha

Thanks for the tips, I'll see what I can figure out.

-------------------------

tvault | 2021-06-13 13:16:07 UTC | #15

I run Urho3D on the Pi 4, I used the master branch, created a build folder and ran cmake, within
the build folder and that's all I did, I didn't use the build scripts.

-------------------------

tvault | 2021-06-13 13:14:36 UTC | #16

This is what I get:
![Screenshot from 2021-06-13 14-13-10|690x430](upload://7ZsSDobHWM6lroR3GQAM6e0K5C1.png)

-------------------------

Pencheff | 2021-06-13 13:59:21 UTC | #17

This looks completely fine.

-------------------------

arcadeperfect | 2021-06-15 02:45:16 UTC | #18

And the engine runs fine for you?

-------------------------

tvault | 2021-06-15 11:36:59 UTC | #19

I can run the examples from both desktop and the terminal. I seem to have an issue running the UrhoPlayer with the ninja demo, i get a segmentation fault although it works fine on the pi 3.

-------------------------

weitjong | 2021-06-15 14:49:22 UTC | #20

If you don’t pass any option and build from the Pi itself then it is likely (although I am not 100% sure anymore without double checking the script) that it will just target RPI3. Only when the build system finds a 64bit system then it will be sure to set the target to RPI4. Replying using my iPhone and just based on my recollection. But you can always use the CMakeCache to find out what is being set by default.

-------------------------

arcadeperfect | 2021-06-15 14:26:25 UTC | #21

Interesting that it works for you, I tried building with your method and still get the SDL errors. I can only assume it's some kind of dependency issue in that case. Can I ask if you're using Raspian / Rapsian lite / something else? Did you build SDL from source?

-------------------------

tvault | 2021-06-15 15:17:23 UTC | #22

I'm using Raspbian Buster.

I only use the dependencies provided by Urho.

-------------------------

arcadeperfect | 2021-06-15 15:24:05 UTC | #23

Then I am flummoxed  :woozy_face:

-------------------------

tvault | 2021-06-15 19:28:35 UTC | #24

I'm not sure if it will work but have you tried installing libsdl2-dev , I remember installing SDL this way for something else.

-------------------------

weitjong | 2021-06-16 01:09:33 UTC | #25

Urho3D project contains all the 3rd party libraries that it uses, including SDL. By installing SDL-dev what it may help to solve is by doing so then the system package manager  also installs all the other dependencies package into the system. At the time you built Urho3D from source then it has most, if not all, of its build requirements already fulfilled. The legacy online documentation actually has a section for describing this build prerequisite. Have a look on the docs.

-------------------------

arcadeperfect | 2021-06-16 02:42:19 UTC | #26

I did read through the docs and was going off this page:

https://urho3d.io/documentation/1.7/_building.html

Going by that it will build, although I do have to install one extra thing. I think it's libgles2-mesa-dev

I was curious about building SDL from source after looking into your suggestion with the SDL_VIDEODRIVER env var, bc after googling the correct syntax to set that to KMS/DRM I found an example where someone set a flag during build of SDL to enable it and override X. (simply setting the var as is just leads to Urho saying that KMSDRM is not available, assuming I got the var right)

But no matter how I install SDL, be it from source, Urho, through apt-get or a tar ball of a pre-built bin, I always get the same error about "No available video device".

I must confess I'm at the limits of my skill here, but my next step is to compile some example C code for SDL and see if that works at all.

-------------------------

