TikariSakari | 2017-01-02 01:04:28 UTC | #1

Hello, I have been wondering this for a while, and I just cannot figure out what would cause this problem. I think there is a high chance its a driver issue, but I noticed that I had quite terrible performance on windows 10 as well with open gl, which again could be just windows 10 and not every single driver for my computer working correctly. Edit: Looks like this is more an issue I have in linux rather than also a thing in windows 10. On win 10, I simply just have terrible performance with opengl, and that is most likely a driver issue or some sort.

What I do is as following in linux mint:
I fly back so that I see, everything moving. Then I resize the window by hitting alt+enter a couple of times. After a few resizes the fps just drops down a lot. Like it could be 200 fps in the beginning, after resizing couple of times, it drops down to 30 or something.

Originally I was using window-resizable and it seems to make the fps drop quite often, since it resizes once in the beginning.

Maybe this has something to do with context? Like if there is too much stuff to load on size change, and it isnt finished or something, it does some really weird stuff.

Again as said this could be completely my computers own driver problem. I noticed with linux I do have some problems with ALSA from time to time and my gpu has had some issues before with various things (Ati HD 5870), so I wouldn't be surprised if this doesn't affect anyone else.

Initial fps, 1920x1040ish
[url]http://i.imgur.com/iC2EekR.jpg[/url]

After resizing it few times, something x something (smaller resolution)
[url]http://i.imgur.com/xy185QI.png[/url]

Edit: Actually I can simply use alt+enter couple of times, so there is no need to even make the window resizable or any code change to 06_SkeletalAnimation.

Edit2: It doesn't seem to affect windows 10 for me. I simply just have terrible performance on win 10 with opengl, probably due to bad drivers or some sort of driver conflict.

Edit3: Forgot to mention, that if I use windowed mode, and I keep resizing it after the fps drop, it might actually suddenly get higher fps than the initial. Also what happens with the higher fps is that it starts to blink, like in some frames you can see through the window or something.
Also forgot to mention, that this existed before the opengl3 render-change.

-------------------------

GoogleBot42 | 2017-01-02 01:04:28 UTC | #2

That seems really weird.... what happens if you change the screen size and then change it back to the original number?  I remember reading somewhere that older graphics cards do better at some specific resolutions...

Also what graphics card do you have?

And what version of OpenGL is your driver?
[code]glxinfo | grep "OpenGL version"[/code]
For me the output of this command is:
[code]OpenGL version string: 2.1 Mesa 10.5.2[/code]

I don't really think I would be much more help... just trying to think of some possible reasons for this before calling this is possible bug.   :slight_smile:

-------------------------

TikariSakari | 2017-01-02 01:04:28 UTC | #3

The opengl command:
glxinfo | grep "OpenGL version"

gives this as an answer:
OpenGL version string: 4.4.12967 Compatibility Profile Context 14.20

I tried to make a video of showing the problem. Sadly it is less obvious when the fps actually drops because of the obs, the performance isn't that good to begin with, but when it changes to phase 3, where the fps boosts and the blinking starts, I think that should be better visible.
[video]https://www.youtube.com/watch?v=-KR8QfxcBGk[/video]

I do get this error from time to time, but this weird thing happens even without this error appearing:
ALSA lib pcm.c:7843:(snd_pcm_recover) underrun occurred

I tried to google around how to fix this error, and tried 3 different sound cards (sound blaster x-fi fatality pro, asus xonar dx/xd and aureon pci 5.1), but it just appears from time to time. I also tried to disable hdmi sound, since that has caused a lot of issues for me even in windows, same with the gpu I have.

As for the windowed mode, I use that one, because it seems to resize the whole window on every move of the mouse, meaning it actually does some resizing thing every pixel that the window gets resized. At first I thought it is something to do with my resizing function, but since it actually also happens on samples, I guess it is something that has something to do with my gpu (I have had a fair amount of issues with it.)

If I am only one that actually suffers from this, then I don't really mind, since I can live with it, but I was wondering if anyone else happens to have this thing happen to them?

So basically phase 1: Everything is normal... fps ~160 (gpu usage 100%) (app cpu usage: 144%, cinnamon 36%)
Resizing the window couple of times, phase 2: The fps drops a lot, fps ~40 (gpu usage: 100%) (app cpu usage: 120%, cinnamon 18%)
Phase 3: Fps boost, blinking and cannot see windows behind the application. Fps ~200 (gpu usage: 100%) (app cpu usage: 150%, cinnamon: 6%)

I have amd phenom x6 1055T, ati radeon 5870HD, but after taking down the cpu usages, it could be something to do with cinnamon.

Edit: As far as the win10 performance, after I used refresh on win10 and did not install any gpu drivers at all, the performance on windows 10 was normal both opengl and direct3d.

Edit2: Ah I accidentally made it private, meant to set it as unlisted video. Now it is unlisted. I am also trying to install ubuntu, in case it works better. I think the problem lies on either cinnamon or the window managing system that the linux mint has.

-------------------------

GoogleBot42 | 2017-01-02 01:04:28 UTC | #4

I get an error saying the video is private...

[quote="TikariSakari"]ALSA lib pcm.c:7843:(snd_pcm_recover) underrun occurred[/quote]

Ignore that error it happens constantly on my linux box in all programs.  It is an error related to audio.  I am pretty sure that it is harmless.

[quote="TikariSakari"]So basically phase 1: Everything is normal... fps ~160 (gpu usage 100%) (app cpu usage: 144%, cinnamon 36%)
Resizing the window couple of times, phase 2: The fps drops a lot, fps ~40 (gpu usage: 100%) (app cpu usage: 120%, cinnamon 18%)
Phase 3: Fps boost, blinking and cannot see windows behind the application. Fps ~200 (gpu usage: 100%) (app cpu usage: 150%, cinnamon: 6%)[/quote]

What do you do to the window between phase 2 and 3?

[quote="TikariSakari"]Edit: As far as the win10 performance, after I used refresh on win10 and did not install any gpu drivers at all, the performance on windows 10 was normal both opengl and direct3d.[/quote]

This is begining to sound like a driver/Uhro3D issue you do have a fair new graphics card based on the version of OpenGL it supports...  Do other games do this too?

What happens when you force opengl 2.1 when launching urho3d?

Also you could try using the latest drivers.  Here is a link to the beta drivers (you will get best performance with this): [url]http://support.amd.com/en-us/kb-articles/Pages/latest-linux-beta-driver.aspx[/url]

-------------------------

weitjong | 2017-01-02 01:04:28 UTC | #5

I have a different problem with GL3 on my nVidia GTX580 card on Linux. I use proprietary driver (kernel module) from nVidia (packaged by rpmfusion for Fedora). The alt+enter toggle gave me a consistent segfault instead. Forcing to use GL2 does not exhibit this problem. Using Eclipse in debug mode, I can see it crashed around in this line: [github.com/urho3d/Urho3D/blob/m ... .cpp#L2944](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/View.cpp#L2944).

Resizing the window is also problematic now. Any attempt to resize would shrunk the window size into a single pixel or line instead. I don't think that how I remember it but I could be wrong though. Interestingly, resizing on Editor still works as before but still crash on alt+enter. IMHO, we have a regression issue here.

-------------------------

cadaver | 2017-01-02 01:04:28 UTC | #6

Also got a crash on Alt-Enter when testing on an AMD GPU on Windows & OpenGL. It happens with 100% certainty so it should not be hard to pinpoint & fix.

EDIT: Committed what should likely be the fix, on GL3 vertex buffers would restore themselves after context loss without a valid bound VAO.

-------------------------

TikariSakari | 2017-01-02 01:04:29 UTC | #7

After spending one day of trying to figure out what is the reason or cause, I never found out. I did get rid of it though, so I guess this is kind of solved, at least for now. I shall see if it reappears after longer uptime. I managed to "fix it" by reformatting and reinstalling linux mint with cinnamon.

Maybe it could be different sound card or some bios change, but what I did notice is that on the urho3d build instructions for debian based system, there is mention of installing packet libgl1-mesa-dev for debian based systems. This packet at least for me removes most of opengl  drivers. So if I reboot computer after installing this, which removes a lot of stuff, most of the windows are complete transparent + cinnamon cannot even create opengl2 context. I managed to fix this by installing gpu drivers afterwards, but this could be one of the reasons why I originally had the problem to begin with. On the other hand this packet was enough for me to actually be able to build Urho3D without having to install the libgl1-mesa-dev package: 
[code]sudo apt-get install mesa-common-dev[/code].

Anyways thanks everyone for trying to help me with my terrible skills.

-------------------------

GoogleBot42 | 2017-01-02 01:04:29 UTC | #8

Now that is really weird... cadaver and weitjong were able to verify this bug (it actually would crash for them) so I am not sure if it your linux mint installations fault but you say that the error went away on a complete reinstall of linux mint....  :question:   :neutral_face:

-------------------------

weitjong | 2017-01-02 01:04:29 UTC | #9

[quote="cadaver"]Also got a crash on Alt-Enter when testing on an AMD GPU on Windows & OpenGL. It happens with 100% certainty so it should not be hard to pinpoint & fix.

EDIT: Committed what should likely be the fix, on GL3 vertex buffers would restore themselves after context loss without a valid bound VAO.[/quote]
Thanks Lasse. That fixed the Alt+Enter segfault problem on my system. However, the window resizing is still an issue on sample apps (I tried 06_SkeletalAnimation). I have a gut feeling that this has something to do with mouse input handling changes.

[quote="TikariSakari"]Maybe it could be different sound card or some bios change, but what I did notice is that on the urho3d build instructions for debian based system, there is mention of installing packet libgl1-mesa-dev for debian based systems. This packet at least for me removes most of opengl drivers.[/quote]
You read it wrongly. It is trying to say that you should only install mesa driver when you don't have proprietary driver from the graphic card vendor installed. You should be much better of with ATI or nVidia driver instead of lousy mesa driver. The latter is probably only needed to be installed on a virtual machine system where a graphic card is being emulated.

And about the sound buffer underrun issue, I used to get those in the log as well but I choose to ignore them then. It does not seem to happen now after I upgrade my system to Fedora 21. I believe this has something to do with PulseAudio and/or ALSA configuration setting. Do a google search and you should find that this issue is not unique to Urho3D.

-------------------------

TikariSakari | 2017-01-02 01:04:29 UTC | #10

[quote="weitjong"]
You read it wrongly. It is trying to say that you should only install mesa driver when you don't have proprietary driver from the graphic card vendor installed. You should be much better of with ATI or nVidia driver instead of lousy mesa driver. The latter is probably only needed to be installed on a virtual machine system where a graphic card is being emulated.[/quote]

Without the package libgl1-mesa-dev, I wasn't able to compile SDL, since I was missing the opengl-headers <GL/gl.h> even when I had propriety drivers installed. But the headers also seems to be part of package mesa-common-dev, and installing this package did not make my opengl2 completely unusable unlike the libgl1-mesa-dev package did.

Tbh. the way how I first time "solved" this issue was first installing libgl1-mesa-dev and then after it was done, I immediately installed AMD drivers without booting, and then reboot. With this order I didn't come up to the point where my whole windowing system was gone after reboot, and it could be also the reason for the weird flickering issue I had.

[quote="weitjong"]And about the sound buffer underrun issue, I used to get those in the log as well but I choose to ignore them then. It does not seem to happen now after I upgrade my system to Fedora 21. I believe this has something to do with PulseAudio and/or ALSA configuration setting. Do a google search and you should find that this issue is not unique to Urho3D.[/quote]

I tried to google around for solutions for these, and tried to disable hdmi drivers etc. but I didn't manage to get rid of it, except now with reinstall I haven't seen these issues pop yet.

I have yet to see the buffer underruns after the reinstall, but on the other hand they usually started to appear after the computer had been running for couple of hours, which I didn't have luxury for trying yesterday. Before reinstalling, I did have some odd half a minute unresponsiviness sometimes, where it spammed buffer underruns into console after it regained responsiviness, this usually was somehow related to resizing of a window. It could also be the other way around, that the buffer underrun happened because of the computer became unresponsive.

I also noticed that the performance for running the samples has increased a bit after the reinstall. Last time I did have antivirus program installed tho + this was the first time that I actually reformatted my boot-partition instead of just installing over the old installation of linux(I think ive done that close to 10 times now since I installed linux first time about 2 months ago) + I think on first try I tried beta drivers and those completely failed, so it might have left some weird package combination.

-------------------------

cadaver | 2017-01-02 01:04:29 UTC | #11

The resize bug looks like mouse cursor recentering is happening during the resize.

-------------------------

TikariSakari | 2017-01-02 01:04:29 UTC | #12

[quote="cadaver"]The resize bug looks like mouse cursor recentering is happening during the resize.[/quote]

If you set mousevisible to true, then the window stops automatically centering the mouse. I think I saw it on docs, that the mouse behaviour has different ways of handling mouse. When its invisible I believe the point is to mimic fps-types of games. 
On the other hand I noticed that if you use the setcursor, then like in example 38, moving around the mouse while holding right click the mouse stays still, but the mouse cursor is locked into the scene as in I cannot move the cursor out of the window. This is probably pretty good for some fast paced games + dual monitor, where you accidentally might click outside of window, something along a rts-type of a game. 
If I do not use the setcursor, the mouse moves while holding right button, even if its invisible, meaning it might move on top of button, and upon releasing it resets its position. Though with the android I do not really want to see the cursor on the screen, so this is probably the behaviour I do want to have. This on the otherhand doesn't lock the cursor to the screen. The game I am trying to make would be turn based game, where mouse should freely go out of the window, and the window size preferably should be readjustable. I suppose some setting of mouse position on every frame would probably fix the problem of hovering over ui-objects while holding right mouse down would be a simple fix for me in my case.
Although I think there was some way to change the behaviour of the mouse even with the visibility of mouse, but using the cursor also creates cursor on android phone, which I want to avoid doing.
So I guess either changing mouse behaviour during resize or setting mouse visibility to true while resizing, then restoring after resize is done could be one way to solve the automatic shrink?

-------------------------

cadaver | 2017-01-02 01:04:29 UTC | #13

From what I remember, the resize used to work OK on all desktop platforms, but either the new mouse modes or Emscripten support broke it.

-------------------------

TikariSakari | 2017-01-02 01:04:30 UTC | #14

Well looks like its not completely gone. I still haven't been able to make the blinking thing happen, but it happens sometimes, very rare though now after the changes into the context creation code than it did before the reformat and urho code changes. I do have a theory tho. Even on this installation I did use the package that completely wiped my opengl2 drivers because I wanted to be sure that it was that one package that caused me some problems, and installed amds drivers after installing the package. My theory is, that it sometimes doesn't use the propierity drivers when creating context, and uses mesa-drivers or something, this could be pretty far fetched though. Then when I readjust the window, it again randomly chooses one of the drivers.

I noticed that even when its running at 30-35 fps at full screen, it is actually utilizing 100% gpu. Then when it runs at roughly 140fps full screen on open gl 3, my gpu utilization is at 100%, this is the normal speed. With opengl 2, it can runs bit faster (170-200) fps, depending on what viewing angle I am using. If it has to draw into full area, the fps is a bit lower than when it tries to draw everything on a portion of the window. I guess with opengl2 there is some sort of depth buffer test, and it tries to avoid redrawing same pixel.

Edit: I have to point out, that the problem does occur with opengl 2 as well, so it is not completely a problem that only happens with open gl 3 mode.

I am using this to check my gpu utilization:
[code]aticonfig --odgc --odgt[/code]

Another possible reason might be that for some reason my gpu is using 2d-clocks, which I know happens quite a lot at least in windows, and it is more about my gpu problem than anything. It especially happens if I just happen to have flash running in any tabs on a browser.

Anyways I guess this is kind of case solved-ish. Hopefully there won't be a sequel in a near future.

-------------------------

TikariSakari | 2017-01-02 01:04:30 UTC | #15

Part2:

I think I have finally gotten a lot closer to the problem, and it definitely doesn't seem to have anything to do with Urho. If I boot in linux and then spam 10-20 Nemo windows, and start urho-program, or pretty much anything that uses opengl, the performance drops quite dramatically. I guess its some kind of combination with cinnamon and the driver installation I have. On the other hand if I log from Cinnamon to KDE, I can spam a lot of windows without suffering from this problem.

I also think there is some kind of connection with the size of the windows as well, because same amount of windows that are using full screen might cause the bug to happen, where as if I shrink the nemo windows, it might not happen. Also when I resize the window, it changes the fps-count. Like if I have it on full screen then open more windows, make it smaller, then back to full screen it might have the bug occuring.

Anyways seems that my fps drop indeed has nothing to do with Urho, although coinsidentically the other bug was found with the resizing.

-------------------------

cadaver | 2017-01-02 01:04:30 UTC | #16

About the resize issue: it exists on Linux only, and also in Urho3D 1.32. It depends on whether the window manager will draw a box outline when resizing, or live resize the window. In the latter case the bug will happen.

EDIT: hopefully it should be fixed now. The (in retrospect obvious) trick is to not recenter mouse when a window resize happens, which avoids the error and allows the user to stay in control of the cursor.

-------------------------

weitjong | 2017-01-02 01:04:30 UTC | #17

[quote="cadaver"]About the resize issue: it exists on Linux only, and also in Urho3D 1.32. It depends on whether the window manager will draw a box outline when resizing, or live resize the window. In the latter case the bug will happen.

EDIT: hopefully it should be fixed now. The (in retrospect obvious) trick is to not recenter mouse when a window resize happens, which avoids the error and allows the user to stay in control of the cursor.[/quote]
I haven't retested it this morning yet but from the changes in the commit, that should nail it for good. Thanks again.

Not sure about the other lesser known Linux window managers, but most of the full blown Linux desktop environments that I know of use live window resizing these days.

-------------------------

weitjong | 2017-01-02 01:04:30 UTC | #18

It looks like I spoke too soon this time. Just tested it and it does not fully fix the resizing problem on my system (Fedora 21 64-bit using Gnome 3 "DE").

EDIT: I have time to debug it a little bit. After the fix, the windows resize problem only occurs on certain circumstances, i.e. it depends on how I cover and uncover the window. I now suspect the root cause of the problem is at the SDL side. The SDL_GetWindowFlags() function may return a wrong result with respect to SDL_WINDOW_MOUSE_FOCUS flag. SDL may erroneously report true for this flag when clearly my mouse is not hovering on top of the window. Unfortunately, when SDL returns a bogus result then our code reaches here [github.com/urho3d/Urho3D/blob/m ... t.cpp#L371](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Input/Input.cpp#L371). It should not reach there when SDL returns a good result and the check at line 358 stops it. I don't have the stomach to mess with SDL today so I will just leave it for now. To be fair, this could be SDL or Gnome3 fault. The latter has broken too many things in the recent past.

-------------------------

cadaver | 2017-01-02 01:04:30 UTC | #19

We could also reinstate the logic where user needs to click inside window once before the mouse lock kicks in, and make it consistent on all desktop platforms. This just needs a bit of work since code was inserted to flush SDL events when we're not focused. (Before it was on OSX only, but had to be removed due to the flushing, or else you could never regain focus)

-------------------------

weitjong | 2017-01-02 01:04:30 UTC | #20

I think click to gain focus may solve the problem. Currently when Urho3D sample app window is on top, the app "grabs" the mouse when it ventures too far into the window frame. This makes the window resizing requiring a good hand and eye coordination  :wink: .

-------------------------

