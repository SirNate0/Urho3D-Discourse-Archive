Bart | 2017-01-02 01:06:47 UTC | #1

Hi all!
I am complete newbie to Urho (and 3D engines in general). I don't know the internals very well, and I am curious about running the engine "headless" and streaming the resulting video to an external HW device. I am aware that there is Headless mode in Urho, which however does not run the rendering steps and no GPU-related stuff (is this correct?). 
Could I, theoretically, render to some memory location, get the image form there and process it as I want without displaying the window? Or is there some blocking issue why this cannot be done? I need to render roughly 2000x2000px image and stream it out the computer, only option I have now is render in window, take Camera screenshot and stream it. However having to display 2000x2000px windows is quite impractical.

Thanks for your thoughts on this


P.S. Thanks everybody for working on this excellent engine. Everything is so intuitive, well-modeled and easy to use. GREAT JOB!!!

-------------------------

cadaver | 2017-01-02 01:06:47 UTC | #2

Welcome to the forums!

Headless mode, as it is understood by Urho, is meant for non-graphical applications like dedicated servers - a rendering window and graphics context is not created at all. This means that none of the graphics / rendering functionality is usable.

In this case, to get a working graphics context, you should open a window, but its size doesn't matter, it can be very small like 100 x 100, and you don't need to render into it at all. Instead you should render into a Texture2D, which can be sized as large as your GPU allows, and use the Texture2D::GetData() function to get the pixel data every frame. See the RenderToTexture example.

However, I'll make no promises whether the performance will be fast enough for realtime video streaming; your usecase is outside of what I'd strictly consider "supported" by the engine.

-------------------------

Bart | 2017-01-02 01:06:47 UTC | #3

Looks like a useful way to accomplish what I need. I don't mind having a small preview window with downscaled large texture - it's actually something I wanted anyway. I don't think that performance should be an issue at this point (I made some tests), and I am exceeding my requirements already on my laptop.

Thanks for pointing me in the right direction!

-------------------------

