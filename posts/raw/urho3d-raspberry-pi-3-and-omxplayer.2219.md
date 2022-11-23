fpecheux | 2017-01-02 01:14:00 UTC | #1

Hi,

For a project of mine involving a Raspberry PI 3, I'd like to be able to temporarily suspend a Urho3D application, say ./04_StaticScene for instance, run an omxplayer instance showing  a 1920x1080 H264 video, and then resume the Urho3D application. The problem is that they share the same framebuffer and GPU stuff, and when I launch omxplayer, I get the sound but the image remains produced by the Urho3D engine.

My question: how can I suspend the Urho3D app correctly so that omxplayer can take control of the framebuffer momentarily then give it back to the Urho3D app ?

BTW, your environment is really awesome.

Best regards,

Francois

-------------------------

cadaver | 2017-01-02 01:14:01 UTC | #2

Welcome to the forums.
On desktop platforms you can call Graphics::Minimize() which will minimize the app window to the taskbar. Depending on Engine class config the frame updates may still go on, but it doesn't render to the minimized window. You could try if the same works on RPi3; this depends on how SDL actually handles the windowing, ie. does it relinquish the framebuffer when the window shouldn't be visible.

-------------------------

weitjong | 2017-01-02 01:14:01 UTC | #3

SDL "video driver" for RPI is quite simple or broken, depends on how you see it. It mainly only contains stubs without actually implementing those windowing functions. So, minimizing window may not give the same result as in the desktop platform. I think you may have to get your hand dirty to experiment with the dispmanx's element layer or alpha settings directly.

-------------------------

weitjong | 2017-01-02 01:14:54 UTC | #4

It may be too late for you by now but it looks like this commit in SDL 2.0.5 release tag is exactly what you are looking for. [github.com/urho3d/SDL-mirror/co ... 061d76ac8e](https://github.com/urho3d/SDL-mirror/commit/8bc6a7ef95c3d206fad841a420cf81061d76ac8e)

-------------------------

