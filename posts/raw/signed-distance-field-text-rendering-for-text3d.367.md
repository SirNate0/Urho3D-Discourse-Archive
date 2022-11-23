aster2013 | 2017-01-02 00:59:54 UTC | #1

[youtube.com/watch?v=CGZRHJvJYIg](http://www.youtube.com/watch?v=CGZRHJvJYIg)

Normal text rendering
[img]https://raw.githubusercontent.com/aster2013/Readme/master/images/Font01.jpg[/img]

Signed distance field text rendering, it look better!
[img]https://raw.githubusercontent.com/aster2013/Readme/master/images/Font02.jpg[/img]

-------------------------

friesencr | 2017-01-02 00:59:54 UTC | #2

I was trying to figure out how to draw smooth curves a while ago (and failed like everything i try).  However I did find this library written by the nanovg guy. [github.com/memononen/sdf](https://github.com/memononen/sdf)

Update:
The pictures weren't working before.  You got it to work and it does look really nice! and its all on 1 texure!

-------------------------

weitjong | 2017-01-02 00:59:55 UTC | #3

This certainly will be a nice addition to the Urho3D repo. The shader is so simple. "Why didn't I think of that?", as said in this article [forum.libcinder.org/topic/signe ... -rendering](https://forum.libcinder.org/topic/signed-distance-field-font-rendering).

-------------------------

Mike | 2017-01-02 00:59:55 UTC | #4

The improvement is stunning!

-------------------------

cadaver | 2017-01-02 00:59:55 UTC | #5

Yes, looks very nice and sharp!

-------------------------

aster2013 | 2017-01-02 00:59:55 UTC | #6

[valvesoftware.com/publicatio ... cation.pdf](http://www.valvesoftware.com/publications/2007/SIGGRAPH2007_AlphaTestedMagnification.pdf)

-------------------------

aster2013 | 2017-01-02 00:59:55 UTC | #7

With SDF, we can do more text effects in shader, it is so easy.
[img]https://raw.githubusercontent.com/aster2013/Readme/master/images/Font03.jpg[/img]

-------------------------

aster2013 | 2017-01-02 00:59:56 UTC | #8

Build SDF on run time is very slow, so I don't want to add for FreeType font face. Anybody has good idea?

-------------------------

cadaver | 2017-01-02 00:59:56 UTC | #9

Maybe create a tool that preprocesses TrueType fonts and saves the SDF image data.

-------------------------

aster2013 | 2017-01-02 00:59:56 UTC | #10

Current I use UBFG to generate SDF font file, and save as BMFont XML format, then change it's extension to .sdf. Font class will use it as SDF font automaticlly. You can get UBFG from [github.com/aster2013/UBFG](https://github.com/aster2013/UBFG).

-------------------------

boberfly | 2017-01-02 00:59:57 UTC | #11

I remember long ago when Quake 3 was the best moddable game out and I was adding character models with Milkshape 3D. I used an alpha channel with a very heavy anti-aliased edge for a bird feather and discovered that it had an almost-vector clean edge to it on magnification in the game engine with alpha test/discard (fortunately fixed-function GL/hardware did the alpha test at 0.5 alpha, no GLSL/HLSL back then!) and wondered if anyone else stumbled upon this technique. Many moons later Valve bring out the paper for Team Fortress 2 for fonts. Definitely a "Why didn't I think of that?" type of technique... :slight_smile:

-------------------------

