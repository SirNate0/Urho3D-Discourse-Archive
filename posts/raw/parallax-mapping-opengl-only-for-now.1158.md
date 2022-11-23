krstefan42 | 2017-01-02 01:05:47 UTC | #1

I modified the LitSolid shader to support parallax mapping, which simulates bumpy surface geometry using a heightmap. If Parallax mapping isn't enabled, the unnecessary code is #ifdef-ed out, so there's no cost.

It comes with a demo, so you can play around with different parameters and quality settings. Press control to load the highest-quality preset, and use space to toggle the effect on or off. It's OpenGL only for now, but I'm working on DirectX support, too.

Here is the download link:
[url]http://www.mediafire.com/download/7ez729j2yiu7moh/Urho3D_Parallax.zip[/url]

Some screenshots (click to view full size):
Parallax on:
 [url=http://s10.postimg.org/rhep93bzt/Parallax1.jpg][img]http://s10.postimg.org/4fy43ccc5/Parallax1.jpg[/img][/url]
Parallax off:
[url=http://s7.postimg.org/tp1yrws63/Parallax1_Off.jpg][img]http://s7.postimg.org/q5g123pg7/Parallax1_Off.jpg[/img][/url]
Parallax mapping on curved surfaces (note that it doesn't effect silhouettes, but still works well):
[url=http://s1.postimg.org/53zcfcni7/Parallax2.jpg][img]http://s1.postimg.org/i84ws1fjv/Parallax2.jpg[/img][/url] 

[b]Instructions to install/run the demo: [/b]
1.Unzip the folder. 
2.Copy the contents of the subfolders "Materials" "Models" and "Textures" into the corresponding folder in Urho3d/bin/Data. 
3.Copy the contents of "techniques" into the corresponding folder in Urho3D/bin/CoreData. 
4.Make a backup copy of the original "LitSolid.glsl" from Urho3D/bin/CoreData/Shaders/GLSL, in case my new shader doesn't work for you, or you want to keep the old one for some reason. 
5.Copy LitSolid.glsl out of "Shaders-GLSL" to Urho3D/bin/CoreData/Shaders/GLSL, overwriting the old version.
6.Run "ParallaxTest.lua" with Urho3DPlayer from the command line.

Alternately, if you don't want to replace LitSolid, you can change the filename of my shader to something else and then go into the technique files and change the file name there to match.

[b]Controls for the demo are:[/b]
Mouselook/WASD
i - increase iterations by 1
o - decrease iterations by 1
k - increase displacement factor
l - decrease displacement factor
n- increase offset limiting factor
m - decrease offset limiting factor
Shift- load a medium-quality preset (only applicable for mat quality 2 / Shader Model 3) (this is the default setting)
Control- load a high-quality preset (only applicable for mat quality 2 / Shader Model 3)
Space- toggle parallax on and off

Note that if your GPU doesn't support Shader Model 3.0 it will default to material quality 1, where the number of iterations is fixed at 2. Only material quality 2 lets you change the iteration count. If it's slow on your machine, the dynamic iteration count could be slowing it down, so try toggling the material quality with the 2 key.


[b]Parameter explanations + Tips for using in a game[/b]
The material parameters are:
ParallaxDisplacement- displacement factor- should be pretty low, I used .045
ParallaxIters - number of iterations (controls overall quality)
OffsetLimit - Value between 0 and 1. Higher values flatten the details at grazing angles, to reduce texture swimming artifacts. There's never any reason to go below .15 or so.

If you're having texture swimming artifacts, you can do one of 3 things: decrease the displacement factor, increase the iterations, or increase the offset limiting factor. Actually, one other thing to do is filter the displacement map to reduce high-frequency features. Maps with a lot of strong, small detail are more prone to artifacts, and usually tend to not make such great displacement maps in general.

[i][b]Important:
If you're using one of the techniques with a fixed iteration count, the ParallaxIters parameter still needs to be set correctly to get consistent results.[/b][/i] This sounds like a strange requirement, but there's a reason for it. If you're using different fixed iteration counts for different material quality and LOD levels, then ParallaxIters should be set to the iteration count of the highest quality technique used. The shader will use this information to scale the displacement along with the iteration count to avoid texture swimming. For instance, if your highest setting uses 4 iterations (and thus ParallaxIters) is set to 4, but the current mat quality/lod level uses only 2 iterations, then the displacement factor will be scaled by 50% (2/4) to compensate for the reduced iteration count. If you don't want displacement scaling (i.e. you want the displacement factor to be be consistent across all quality/lod levels, at the cost of swimming artifacts), then you should set ParallaxIters equal to number of iterations of the current quality/lod level, not the maximum.

[b]Summary of techniques[/b]
The ParallaxStonesDemoVer.xml material (used in the demo) and the  DiffNormalSpecParallaxDemoVer.xml technique that it uses aren't intended to be used in a real game. The dynamic iteration count, while good for testing different settings, adds unnecessary overhead. So use one of the fixed Iteration techniques instead (DiffNormalSpecParallax1Iters, as well as the 2Iters, 4Iters, and 6Iters versions) (ParallaxStones.xml is an example material that uses these techniques).

The shader expects the displacement map to be in the emissive texture channel (so do this in the material xml file: <texture unit="emissive" name ="Textures/StoneFloorDisplacement.jpg" />). So you normally can't use parallax mapping and an emissive map at the same time. But if you do need an emissive map, use one of the techniques ending in "AlphaPackedDisp", where the displacement is instead taken from the alpha channel of the diffuse map, and the diffuse alpha is set to 1 (although per-material alpha settings work fine). Packing the displacement into the diffuse alpha channel also has the added benefit of saving a lot of VRAM if compressed with the DXT5 format.

[b]Shader Defines[/b]
These are shader defines you can set from within a technique xml file to control shader behavior.
-The vertex and pixel shader define "PARALLAX" enables parallax mapping.
-The pixel shader defines ITERS_1 through ITERS_8 will set the number of iterations to be fixed at that value. If you don't use an ITERS_(N) define, then the shader parameter "ParallaxIters" will be used 
instead (dynamic, but slower)
-The pixel shader define DISPFROMALPHA will make the shader take the displacement value from the alpha channel of the diffuse map (by default it's taken from the emit map, specifically the green channel).

Holy crap, that was a lot of text. Let me know if you thought my explanations and different pre-made techniques were useful. Otherwise next time I make a shader I'll just post the shader and one example technique/material, and let you figure it out.

Also, I got the texture from here:[url]http://photosculpt.net/download-free-textures-pack[/url]

-------------------------

krstefan42 | 2017-01-02 01:05:47 UTC | #2

Err, I forgot to upload the .zip file the first time. :blush:  Well, it's fixed now.

-------------------------

Bananaft | 2017-01-02 01:05:47 UTC | #3

You can put displacement map into normal map's alpha channel. Pros: one texture less, free emissive channel, Cons: can't use PACKEDNORMAL.

-------------------------

jmiller | 2017-01-02 01:07:00 UTC | #4

This is great! Thanks for your contribution. :slight_smile:

-------------------------

rasteron | 2017-01-02 01:07:02 UTC | #5

Yes, I remembering trying this a couple of weeks back but forgot to comment. This is really an awesome shader and I hope this works on mobile as I have not tested this yet. 

Seems like parallax mapping is now in every material list/demo on most engine and platforms, so definitely a must have on next release!  :smiley:

-------------------------

krstefan42 | 2017-01-02 01:09:22 UTC | #6

I'm going to resume working on this. A while back I had nearly finished the DX9 implementation as well as Parallax Occlusion Mapping (a more advanced technique) for GL, but then I put this project on the backburner. So you'll see those soon.

In the other thread rasteron reported that it doesn't work on mobile: [topic1189.html](http://discourse.urho3d.io/t/iterative-parallax-mapping-shader/1151/1)

Can anyone confirm this, and maybe get an error message for me? Without an error message, I probably can't pinpoint the problem. The only thing that jumps out at me was using a float for the for loop control variable (what was I thinking with that one, lol), but I think even GL ES 2.0 supports dynamic loop conditions, so that shouldn't be a problem.

Edit: I was wrong, apparently GLES 2 doesn't require support for dynamic loop conditions (it's hard to find a straight answer on Google). So that might be the problem.

-------------------------

rasteron | 2017-01-02 01:09:23 UTC | #7

Hey thanks for the update! Looking forward to the GLES version :slight_smile:

-------------------------

