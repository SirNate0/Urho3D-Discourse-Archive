ganibc | 2017-05-02 09:18:06 UTC | #1

I'm building application that render 3D scene offscreen.
I've implemented the code by render to texture and it's working fine on my local machine.
The application will open a window but it will be just a black screen while it's generating the images in the background.
Now I'm trying to put the application to AWS cloud and run it.
But I'm getting this error:
> Could not create window, root cause: 'No available video device'


Is there any way I can run urho3D application on cloud without GPU and still render to texture?
It seems the headless mode will disable all the rendering.

-------------------------

TheSHEEEP | 2017-05-02 10:10:02 UTC | #2

[quote="ganibc, post:1, topic:3090, full:true"]
Is there any way I can run urho3D application on cloud without GPU and still render to texture?
It seems the headless mode will disable all the rendering.
[/quote]
Isn't the whole point of any headless mode to enable rendering without the need of a window to display to?

Anyway, without a GPU, I think you will be pretty much out of luck.
However, Amazon (and others) offer cloud servers that have GPUs.

-------------------------

weitjong | 2017-05-02 13:33:15 UTC | #3

You didn't say which OS you are using in your setup. We had encountered exactly this error when we first test running our sample apps on Travis (Linux VM) and later on AppVeyor (Windows Server VM). To keep SDL happy, the VM needs a "virtual display" (we do not run the app in headless mode). As it turns out this is such a common requirement for CI servers that both Travis and AppVeyor provide a handy script to call to enable the "X virtual framebuffer" while on Linux and "desktop" while on Windows. It will be slow for sure without a real GPU but they do run successfully nevertheless after that. Probably if you search using a right keyword, you can find the equivalent script for AWS. HTH.

-------------------------

ganibc | 2017-05-03 01:52:16 UTC | #4

It seems the headless is there for non-graphics stuffs, probably like game servers.
AWS with GPU is quite expensive, so I want to avoid it if it's possible.

-------------------------

ganibc | 2017-05-03 01:52:56 UTC | #5

I'm using Ubuntu VM.
Thanks for your suggestion, I'll try to find out about virtual display.

-------------------------

ganibc | 2017-05-03 02:33:17 UTC | #6

[quote="weitjong, post:3, topic:3090"]
X virtual framebuffer
[/quote]

Hi again,

Thanks for your suggestion. Now my application works.
I followed the instructions in this link:
https://github.com/processing/processing/wiki/Running-without-a-Display

First I tried the easiest solution (Option 1):
> xvfb-run /home/<username>/processing/processing-java --sketch=/path/to/sketch/folder --run

This remove the original error, but I got different error message
> libGL error: No matching fbConfigs or visuals found
> libGL error: failed to load driver: swrast
> [Wed May  3 02:08:02 2017] ERROR: Could not create window, root cause: 'Couldn't find matching GLX visual'

Option 2 fix the second error:
> sudo Xvfb :1 -screen 0 1024x768x24 </dev/null &
> export DISPLAY=":1"

Then, run a sketch as usual from the command line:
> /home/<username>/processing/processing-java --sketch=/path/to/sketch/folder --run

-------------------------

TheSHEEEP | 2017-05-03 05:00:16 UTC | #7

Very interesting.
What is doing the rendering, then, if there is no GPU? The drivers must be present for sure for OpenGL/DX to work.
As @weitjong said, it must be very slow if just simulated.

-------------------------

TheComet | 2017-05-03 05:14:20 UTC | #8

Maybe they are offloading gpu rendering to a different cloud

-------------------------

ganibc | 2017-05-04 05:06:51 UTC | #9

I'm guessing without GPU means software rendering. It is slow, but it's okay for my case, since I'm generating images. Not running real time rendering.

-------------------------

TheSHEEEP | 2017-05-05 06:10:10 UTC | #10

You are doing real time rendering if you are rendering a 3D scene. To render it to an image instead of a screen/window doesn't AFAIK make it much faster or slower. Of course, if you just do it rarely and not at 30fps, it probably really doesn't matter.

-------------------------

