godan | 2017-06-16 16:13:20 UTC | #1

I'm pretty excited about this: IOGRAM now supports creating, editing, and compiling script files directly inside the Editor. You can create custom IOGRAM components, or standard Urho scripts. I think you can even combine them!

This is a really basic demo - more advanced features coming up:

https://www.youtube.com/watch?v=cDmnkwCStR4

-------------------------

godan | 2017-06-16 19:22:01 UTC | #2

Works really well for shaders:

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/3e2969b2d8db019174ef2889c2c56eb02d085e7b.jpg" width="690" height="377">

-------------------------

Victor | 2017-06-19 14:36:44 UTC | #3

This is a feature I'm really excited about!

Another feature that, in my opinion, could be useful, is a 16-bit PNG Terrain node or option. Currently (and perhaps I just handled this incorrectly), terrain I've created in World Machine does not load correctly in either Urho's editor or IOGram. I haven't yet pulled down the code to see if I could create my own node for terrain.

For my own terrain, I'm using a small library called LodePNG (http://lodev.org/lodepng/) to load in a 16-bit PNG heightmap, and then I use the following method in my Terrain class to generate an Urho3D Image object.

https://gist.github.com/victorholt/497642bdc2eb5a0a372e73244805fac3

Maybe this could be useful for a future feature for the terrain node? I could also try to get IOGram to compile in CLion and see if I could generate a pull request as well. I just need to stop being so lazy haha.

Anyways, thank you for this feature, and I look forward to the new version of IOGram!

-------------------------

godan | 2017-06-20 11:28:54 UTC | #4

@Victor Sure! I will put in. Definitely seems useful. I was also thinking about trying to support TIFF (since it is a common format for terrain data).

-------------------------

Victor | 2017-06-20 13:54:24 UTC | #5

Wow thanks man! You rock!

I had also thought about tiff as well, although I couldn't find a library that didn't cause a headache to compile with mingw64.

Can't wait for the next release!

-------------------------

