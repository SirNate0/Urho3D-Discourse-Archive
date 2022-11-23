arcadeperfect | 2021-06-11 20:43:38 UTC | #1

Many thanks to @weitjong for helping me get a build to work on the pi.

Currently still haven't got it to work without x running. However, installing only xorg with no desktop and running via xinit seems to be a decent compromise in the mean time.

The demos run with as much performance as I need / expected from a pi4, with a nice frame rate on the simpler ones. 

Except - they all freeze for a split second roughly every 3 seconds. It's not intermittent, it's quite regular, and happens on every demo I've tried.

I guess this is more a pi issue than Urho but any suggestions on what it might be greatly appreciated.

The pi is running the 32bit Raspberry Pi OS lite (no desktop installed)

The only things I've installed are the libs for Urho, smb, git, and xorg. When I check htop I can't see anything obvious using the resources.

So close...

Thanks in advance

-------------------------

Eugene | 2021-06-11 20:48:39 UTC | #2

I don't remember Urho having any kind of periodic job that may cause this kind of lag.
Try to reduce frame rate in options (what's your FPS btw?), maybe your gpu gets overfed with commands or something.

-------------------------

arcadeperfect | 2021-06-11 22:40:31 UTC | #3

Frame rate is solid 60fps (except the lag obviously) in the 2d physics demo (the one I'm interested in) at 1920x1080

More like 18 in the Character demo one.

Is there a way to limit the framerate without modifying the source of the actual app? Can't see anything like that in the runtime flags. Full disclosure I have never developed anything with Urho (yet). I'm currently speccing it to see if it will will work for my project performance wise (seems like it will!)

Although the lag still happens in the heavier demos so I suspect it isn't related to framerate.

-------------------------

Pencheff | 2021-06-11 22:44:15 UTC | #4

I had the same problem, it comes from SDL. Here's the patch I made to work around it:

[code]
diff --git a/Source/ThirdParty/SDL/src/joystick/linux/SDL_sysjoystick.c b/Source/ThirdParty/SDL/src/joystick/linux/SDL_sysjoystick.c
index ad83091..3b69710 100644
--- a/Source/ThirdParty/SDL/src/joystick/linux/SDL_sysjoystick.c
+++ b/Source/ThirdParty/SDL/src/joystick/linux/SDL_sysjoystick.c
@@ -421,7 +421,7 @@ LINUX_JoystickDetect(void)
     Uint32 now = SDL_GetTicks();
 
     if (!last_joy_detect_time || SDL_TICKS_PASSED(now, last_joy_detect_time + SDL_JOY_DETECT_INTERVAL_MS)) {
-        DIR *folder;
+        /*DIR *folder;
         struct dirent *dent;
 
         folder = opendir("/dev/input");
@@ -436,7 +436,7 @@ LINUX_JoystickDetect(void)
             }
 
             closedir(folder);
-        }
+        }*/
 
         last_joy_detect_time = now;
     }

[/code]

-------------------------

arcadeperfect | 2021-06-11 22:46:46 UTC | #5

amazing thanks, I will try this

-------------------------

arcadeperfect | 2021-06-11 22:47:40 UTC | #6

Out of interest what platform were you running on?

-------------------------

Pencheff | 2021-06-11 22:50:10 UTC | #7

RockPro64 with rk3399. It required lots of other workarounds as well, particularly on ARM devices.
You will lose runtime joystick detection however.

-------------------------

arcadeperfect | 2021-06-11 22:52:27 UTC | #8

Good to know thanks. No need for joysticks here so that's fine.

-------------------------

weitjong | 2021-06-12 02:32:57 UTC | #9

Haven’t tested on new Pi4 yet, but I don’t remember observing freeze on my older Pi for those simple demos. The only artifacts I recall is the skeleton demo caused by not enough uniform and slow frame rate on physics stress test and water demo. It was last tested quite a few years ago using older code version in the repo. It was also without X draining the computing power. The Pi has its memory configuration altered to optimize for 3D application. 

Have you tried to configure your Pi4 to have more ram allocated to the GPU? Newer Raspbian uses non-proprietary graphics driver, but I am not sure yet how much it affects performance on Urho3D.

PS. The newer Pi4 has more uniforms. I believe we could change the bone limit now when targeting Pi4. That should fix the skeleton animation demo artifact. That’s one of the things I wanted to do while waiting for my Pi4 to arrive at the time. Hope I can find time in the near future to finish the experiment.

-------------------------

