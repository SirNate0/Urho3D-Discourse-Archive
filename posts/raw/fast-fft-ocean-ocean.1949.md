Lumak | 2017-08-07 17:33:39 UTC | #1

I came across this site - [url]http://www.keithlantz.net/2011/11/ocean-simulation-part-two-using-the-fast-fourier-transform/[/url], and wanted to observe the frame rate in Urho.  His code is written very well.  I literally just copied and pasted his code and changed a couple of vector classes to Urho's and had it running in few minutes.

https://youtu.be/-V3LHbQgL84

Runs at around 40 fps running in the main thread.  Shader stuff next.

-------------------------

rasteron | 2017-01-02 01:11:45 UTC | #2

Looks good! :slight_smile:

-------------------------

Lumak | 2017-01-02 01:11:45 UTC | #3

Yes, Mr. Lantz did an awesome job optimizing his FFT. It's the best that I found showcasing Ocean Simulation.

-------------------------

Lumak | 2017-01-02 01:12:44 UTC | #4

frame rate running in urho 1.5, wave process running in a separate thread, using water.xml material

[img]http://i.imgur.com/ntzrsvb.jpg?1[/img]

-------------------------

Victor | 2017-01-02 01:12:45 UTC | #5

I'm really excited about this! Nice work!

-------------------------

krstefan42 | 2017-01-02 01:13:42 UTC | #6

Wow, looks great! That's running CPU-side? Pretty impressive stuff. I imagine it would benefit from a multi-resolution grid (with higher res closer to the camera). When you are done, could you share the modified source and an example? I'm feeling lazy and would rather not try to get it running myself. :wink:

-------------------------

Lumak | 2017-01-02 01:14:21 UTC | #7

@ krstefan42

Not sure how I missed your post, but sure, I'll create a repository for this (not anytime soon though).

-------------------------

Lumak | 2017-01-02 01:14:26 UTC | #8

Now that Cadaver made some performance improvements, I should work on this soon(TM).

-------------------------

Lumak | 2017-01-02 01:14:29 UTC | #9

Repository: [url]https://github.com/Lumak/Urho3D-Ocean-Simulation[/url]

I'm still not satisfied with the shading of the ocean and the reason why I was reluctant to create a repository for it.  But I decided to create it and perhaps, one of the graphics programmers can tweak it.

-------------------------

Lumak | 2017-01-02 01:14:34 UTC | #10

Added glsl ocean shader in the repo.

[img]http://i.imgur.com/ZNYGj1x.jpg[/img]

-------------------------

Lumak | 2017-01-02 01:14:36 UTC | #11

Added hlsl ocean shader. I think that will be the extent of my graphics/shader enhancement.  There are a lot of other really cool ocean shaders out there, but most are too complicated and beyond my skill set to duplicate :slight_smile:

-------------------------

Miegamicis | 2017-01-02 01:14:36 UTC | #12

Looks good, thank you  :slight_smile:

-------------------------

larsonmattr | 2017-01-02 01:14:38 UTC | #13

Why do you need to use an FFT for the ocean shading?  Is this more complex than a shader that uses sin functions to move up and down vertices?

[Found that there is a blog post describing this further]
Looks like a far more complex simulation of waves and choppiness, so that is probably why it is doing some more complex wave math.

-------------------------

Lumak | 2017-01-02 01:14:40 UTC | #14

[quote="larsonmattr"]
[Found that there is a blog post describing this further]
Looks like a far more complex simulation of waves and choppiness, so that is probably why it is doing some more complex wave math.[/quote]

That's correct. FFT is used for wave simulation, not shader.

-------------------------

