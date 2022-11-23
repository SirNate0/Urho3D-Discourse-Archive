esak | 2017-01-02 01:04:43 UTC | #1

Maybe this is a dumb question, but I'll ask it anyway:
When I run the samples on my Pi 2, the debug info says it's starting in windowed mode 1920x1080.
Can I somehow change the resolution, for example to 1024x768?
I tried setting the WindowWidth/WindowHeight (in the engine-parameters) to 1024x768, but this doesn't have any effect on Pi 2.
It works though fine when running on Windows.
Is there something I have overlooked, or maybe this is something I can't affect on the Pi?

-------------------------

weitjong | 2017-01-02 01:04:43 UTC | #2

I believe you have to change this on the Pi side. There is hdmi_mode in the Pi's config.txt.

-------------------------

