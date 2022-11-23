vivienneanthony | 2017-01-02 01:00:00 UTC | #1

Hello

I find this link interesting. Maybe something like it can be used for texturing terrain in Urho3D in a generated imaged that can be also saved if need be.

[dice.se/wp-content/uploads/Chapt ... stbite.pdf](http://dice.se/wp-content/uploads/Chapter5-Andersson-Terrain_Rendering_in_Frostbite.pdf)

I'm just seeing if someone can take a look. I don't know Urho3D good enougth to build a shader to class function to implement something like this.

Ideas...

Vivienne

-------------------------

vivienneanthony | 2017-01-02 01:00:05 UTC | #2

[quote="Sinoid"]As I understand it the FrostBite technique is more about tools than anything else. From what I could gather (I've read it multiple times - over the past few years) it appears to use "mini-shaders" that they composite together for the chunks/patches of terrain (they do similar in clumping their masks as being more like a "Texture Region" of a texture-atlas).

....

That sort of thing (the shader, not the chunking) is probably a pretty decent place to get dirty with learning shaders in just about any environment. Terrain is 'regular' so there's a fair bit less to have to deal with.

[horde3d.org/wiki/index.php5? ... _Texturing](http://www.horde3d.org/wiki/index.php5?title=Shading_Technique_-_Dot_Product_Detail_Texturing) - here's an example of a shader doing that in Horde (wrote that wiki article a long long time ago)

Because terrain is regular, you could also take it a bit further and do some Von Neuman (to find XY slopes) sampling to perturb the normal for lighting. With a decent colormap even that old technique can still get some pretty good results.[/quote]


I almost got procedural working fully in Urho3D with a lot of help. The link is at [b]http://discourse.urho3d.io/t/procedural-generated-worlds/335/1[/b]

The quicker that [libnoise.sourceforge.net/tutoria ... rial5.html](http://libnoise.sourceforge.net/tutorials/tutorial5.html) can be implemented or some type.  Maybe texturing would be the nice project.

-------------------------

namic | 2017-01-02 01:08:35 UTC | #3

It seems that they use a very similar workflow that the one used here: [unigine.com/en/articles/procedur ... eneration2](http://unigine.com/en/articles/procedural-content-generation2)

-------------------------

