XGundam05 | 2017-01-02 01:11:29 UTC | #1

Is there any interest in adding TFT display support for the RPi builds [i](e.g. the [url=https://www.adafruit.com/products/2298]PiTFT 2.8" from Adafruit[/url])[/i]? I'm currently working on it, but didn't know if there'd be enough interest to attempt to add it to Urho itself.

If there is, I'll make sure it conforms to the Urho code conventions.

-------------------------

weitjong | 2017-01-02 01:11:29 UTC | #2

It certainly looks interesting. Adding a few hard buttons on the side and you have yourself a handheld game console. Having said that, I don't think the hardware interfacing layer needs to be in the Urho3D library, unless I totally misunderstood you.

-------------------------

XGundam05 | 2017-01-02 01:11:29 UTC | #3

I'm taking a look to see if I can pop it out from the engine code.

Right now I let the engine render, and then I copy the framebuffer from the HDMI over to the framebuffer for the TFT (standard /dev/fb1, but I have it so you can change it if that's not the case). The framebuffer copy code is currently called in Engine->RunFrame.

However, as I think about it as I type this, I could potentially just extend Application and stuff the call in there...that sounds like a much better option actually.

Thanks for the thinking point :smiley:

EDIT: I should clarify a bit, the TFT display communicates over SPI, and so it doesn't actually have access to the GPU (so no OpenGL). Hence the render has to take place on the GPU and then get manually copied over to the TFT framebuffer. By handling it in the application doing the render, I can make sure that the framebuffer I'm copying from isn't being currently written to.

-------------------------

weitjong | 2017-01-02 01:11:29 UTC | #4

I have not done this before, so take my words with a grain of salt. If the TFT is immediately recognized by the Linux kernel as /dev/fb1 then you already have a good start. If I were you I would probably look at SDL library to see how to utilize that piece of equipment as Urho3D actually relies on SDL to provide the context for audio, video, input, etc. I believe when done correctly, the Urho3D application (with a few exceptions) does not actually need to "know" where it being run.

-------------------------

XGundam05 | 2017-01-02 01:11:29 UTC | #5

Since the pixel data is pumped out over [url=https://www.raspberrypi.org/documentation/hardware/raspberrypi/spi/README.md]SPI[/url] on the GPIO, SDL won't actually respect use of the TFT framebuffer if you have an OpenGL context. It works for any context which doesn't use hardware acceleration, but the GPU doesn't actually have a way to communicate with the TFT framebuffer (just the HDMI and RCA display circuits).

I've propped up a TFTApplication class, that's essentially a copy of the Application class (needed to override the non-virtual Run() method). Ive got a supporting TFTDisplay class that uses Dispmanx and mmap to copy the accelerated framebuffer over to the TFT. Won't have a chance to test it tonight, but should have a chance sometime this weekend :slight_smile:

-------------------------

weitjong | 2017-01-02 01:11:30 UTC | #6

Normally for fast prototyping I would probably go the same route as yours. However, in this case I believe the interfacing has to be done at the correct layer for better chance of success. If your interfacing code is only at the application level then it might not able to do much beside copying the pixels to /dev/fb*. Without any modifications, of course SDL library won't actually aware of the TFT display. But the same is true with Urho3D library, isn't it?

-------------------------

XGundam05 | 2017-01-02 01:11:30 UTC | #7

Right now I'm going for the "get it working" part. Next is the "get it right" part :wink:

So far, my research isn't showing any way around copying from one framebuffer to the other. The SPI interface is what has been the bane of OpenGL on SPI displays since, well, the first Pi. Because there is no hardware connection to the SPI pins/interface from the GPU, the process goes: CPU->GPU Render->CPU->Bit-Bang over SPI.

I'll take a look in the FBTFT driver code and Device Tree Overlay tho, and see how they get the kernel to treat it as a framebuffer. That may yield some better information/a better way to directly integrate it.

-------------------------

XGundam05 | 2017-01-02 01:11:36 UTC | #8

[b]Question:[/b] is there a way to force the fullscreen resolution to a lower resolution that isn't in the same aspect ratio? (Linux)

In dealing with the HDMI framebuffer, it's optimal to have it set to the same size...which can be done in the boot config.txt, but I was hoping to not make users mess with that (so that other applications would run normally over HDMI).

-------------------------

weitjong | 2017-01-02 01:11:36 UTC | #9

You probably can do that when you write a "custom" video driver in the SDL library. Currently SDL defines one video driver for RPI which calls Broadcom graphics_get_display_size() function to get the display size during its initialization (see RPI_VideoInit). I suppose it always get the fullscreen size for the HDMI (or as per defined in the boot config). I would probably have a look there.

-------------------------

XGundam05 | 2017-01-02 01:11:36 UTC | #10

Well, for now I have it working with setting up the HDMI settings in the boot config :slight_smile:

Now that it's working, time to refactor and redesign to make it right :slight_smile:

[url=https://twitter.com/XGundam05/status/715003331530207234?s=09][img]https://pbs.twimg.com/media/Cewzud1WQAAK4CR.jpg[/img][/url]

-------------------------

XGundam05 | 2017-01-02 01:11:46 UTC | #11

I've added support (using the framebuffer copy method) into the Engine. For right now I plan on maintaining it as a separate fork.

Github repo: [url=https://github.com/xgundam05/Urho3D/tree/PiTFTDisplay]xgundam05/Urho3D[/url]

The additional engine parameters are as follows:
[b]EnableTFT[/b] : Boolean, default=false. Enables TFT Display in engine initialization
[b]TFTSourceBuffer[/b] : Integer, default=0. Source display to copy from. Raspbian Jessie sets TV (HDMI/RCA) out as 0
[b]TFTFramebuffer[/b] : String, default="/dev/fb1". Framebuffer location of the TFT display. FBTFT DT Overlays in Rasbian Jessie default to "/dev/fb1"

TODO List:
* Add detection, reassignment and restoring of console framebuffer (currently this is handled via bash script)
* Add detection, initialization and restoring of TV Out settings (available via VideoCore libraries, currently handled via boot/config.txt settings)

Urho3D Samples:
[video]https://youtu.be/O9kJeXT-VtY[/video]

-------------------------

weitjong | 2017-01-02 01:11:46 UTC | #12

Thanks for sharing it.

-------------------------

