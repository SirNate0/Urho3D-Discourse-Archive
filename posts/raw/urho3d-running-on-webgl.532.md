jenge | 2017-01-02 01:01:10 UTC | #1

I spent some time this weekend getting Urho3D running on WebGL with Emscripten.  

It seems to run really well with Firefox on OSX.  It isn't quite as good on Chrome. On Windows there are some issues (maybe the GL -> Direct3D stuff under the hood?).  I was able to get shadows working in Firefox, though not Chrome.  There are some artifacts with cascading shadowmaps so only the first shadowmap is used.  F2, etc work to see metrics.  

Here's a link to some samples, please note that I did not optimize for size on the .js or the data, so they take a bit to download.

[size=150][url]https://dl.dropboxusercontent.com/u/90864981/Demos/Urho3D_WebGL_Demo/index.html[/url][/size]

- Josh Engebretson

-------------------------

weitjong | 2017-01-02 01:01:10 UTC | #2

This is so wickedly cool. On Linux Firefox seems to beat Chrome as well. One thing I notice is, the cursor seems to be off centered so it is difficult to aim on Ragdolls demo. Perhaps it is because when Urho wraps the mouse to center of the viewport, the actual mouse on Emscripten side still isn't. On the Ragdolls demo, the viewport jumps when the mouse first enters the canvas.

-------------------------

cadaver | 2017-01-02 01:01:10 UTC | #3

This is very nice, thanks for sharing!

I assumed that because of using SDL Urho would not be insanely hard to port, but it's awesome to see the possibility confirmed.

-------------------------

hdunderscore | 2017-01-02 01:01:11 UTC | #4

Nice ! It works surprisingly well, did you have to make many changes to the samples/shaders to get them to work ?

-------------------------

jenge | 2017-01-02 01:01:12 UTC | #5

The shaders are unchanged, however I had to hack the shadow support detection in OGLGraphics.cpp and force only the first cascade of the shadow map to be used in the light settings.  This only works on Firefox. On Chrome, I had to disable shadowmaps as they would render incorrectly.  I am sure this can be fixed.

I think Firefox has much better ASM.js support, which makes sense.

Urho is such a great engine, cheers guys!

- Josh

-------------------------

scorvi | 2017-01-02 01:01:12 UTC | #6

wow thats just great ^^ 
will you share your implementation of that ? that would be a nice addition to urho ^^

-------------------------

antont | 2017-01-02 01:01:15 UTC | #7

Now that was great to see! Also thought it was in a bit more distant future still..

@cadaver: IIRC SDL was one of the first targets of Emscripten as kripken himself used it in his syntensity engine (cube2 / sauerbraten) and later we've seen builds of quake or something that also use it, right? So that was actually known to work. SDL is a nice quite simple api for getting a gfx context and input so apparently has worked fine to map it the the browser APIs for those, luckily :slight_smile:

EDIT: bleh I misread earlier what you said, ofc you knew that already, was reading the opposite first :p

-------------------------

lexx | 2017-01-02 01:01:15 UTC | #8

Wow I checked animation demo under firefox, and I was quite surprised that it works great :slight_smile:

Do you share your modifications / knowledge how you did these some day? Maybe in git-fork?

-------------------------

jenge | 2017-01-02 01:01:15 UTC | #9

Hello,

WebGL is an emerging platform and it still a bit rough around the edges.  WebGL is an additional platform to support, with specific requirements, and not a "feature".  This was also a proof of concept and really just comes down to some hacks to the build system and source tweaks.  

There is a SDL2 port for Emscripten which greatly simplifies the process of getting Urho running on the web.    Urho's modular build really helps as it allows you to turn stuff off as you get things bootstrapped, like the networking and physics.  One issue is that web audio only supports floats while Urho uses 16 bit audio 

- Josh

-------------------------

