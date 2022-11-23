gawag | 2017-01-02 01:03:48 UTC | #1

I'm trying to modify the terrain material to support six textures (+the weight texture, so seven textures in total), but there seems to be an Urho limit of five textures and I can't find a way around it.
I found this thread [topic663.html](http://discourse.urho3d.io/t/solved-shaders-and-uniforms/656/1) with some hints, but haven't found a solution.

Material:
[code]
<material>
    <technique name="Techniques/TerrainBlend.xml" />
    <texture unit="0" name="Textures/TerrainWeights2.png" />
    <texture unit="1" name="Textures/r.png" />
    <texture unit="2" name="Textures/y.png" />
    <texture unit="3" name="Textures/g.png" />
    <texture unit="4" name="Textures/c.png" />
    <texture unit="5" name="Textures/b.png" />
    <texture unit="6" name="Textures/m.png" />
    <parameter name="MatSpecColor" value="0.5 0.5 0.5 16" />
    <parameter name="DetailTiling" value="16 16" />
</material>
[/code]
GLSL:
[code]
...
uniform sampler2D sWeightMap0;
uniform sampler2D sDetailMap1;
uniform sampler2D sDetailMap2;
uniform sampler2D sDetailMap3;
uniform sampler2D sDetailMap4;
uniform sampler2D sDetailMap5;
uniform sampler2D sDetailMap6;
//sampler2D sDetailMap5 : register(S5);  // found this syntax in that thread, but it doesn't work at all
//sampler2D sDetailMap6 : register(S6);
...
[/code]
I tried modifying the numbers of the texture units (in shader and material), but that gave weird viewport effects, distance based white-black twitching and numbers >=10 seem to be interpreted as 1.
I also tried changing the TextureUnit::MAX_MATERIAL_TEXTURE_UNITS and MAX_TEXTURE_UNITS inside GraphicsDefs.h, but that had no effect at all (even with rebuilding Urho).

I'm using Urho 1.32 with OpenGL on Windows 7.
Do I need to use special numbers or a different syntax somewhere?

-------------------------

cadaver | 2017-01-02 01:03:48 UTC | #2

For a proper solution you will need to wait for the render-refactor branch to be merged. This will allow 8 material texture units on desktops.

If you want, you can go re-ordering the texture units to make room for your textures. This needs you to change both the texture unit enum and the shaders.

-------------------------

gawag | 2017-01-02 01:03:49 UTC | #3

Yay I figured it out!
I had to change more numbers in the enum in GraphicsDefs.h:
[code]
enum TextureUnit
{
    TU_DIFFUSE = 0,
    TU_ALBEDOBUFFER = 0,
    TU_NORMAL = 1,
    TU_NORMALBUFFER = 1,
    TU_SPECULAR = 2,
    TU_EMISSIVE = 3,
    TU_ENVIRONMENT = 4,
    MAX_MATERIAL_TEXTURE_UNITS = 8,  // this number and all of the following ones have been each increased by 3
    TU_LIGHTRAMP = 8,
    TU_LIGHTSHAPE = 9,
    TU_SHADOWMAP = 10,
    TU_FACESELECT = 11,
    TU_INDIRECTION = 12,
    TU_DEPTHBUFFER = 13,
    TU_LIGHTBUFFER = 14,
    TU_VOLUMEMAP = 15,
    TU_ZONE = 16,
    MAX_TEXTURE_UNITS = 17
};
[/code]
[img]http://i.imgur.com/6omdIfS.jpg[/img]
Now with six splatting textures!

I'm going to add this to the wiki after adding a seventh texture for black (if I get that to work and look good). And maybe after also making better/real textures.

Is the number of textures limited by something? Could it (theoretically) be increased to 20 or 100?
Is there a difference for OpenGL/DirectX and their versions?

-------------------------

boberfly | 2017-01-02 01:03:49 UTC | #4

Hi gawag,

I believe on GL 3.0 or DX10 hardware it's safe to say 16 units minimum, but for GL ES 2.0 the spec mandates minimum 8 units and often the hardware only allows 8. So it's up to you what hardware you want to target. To keep supporting max 8 texture units on terrain patches, you could make different materials which have one texture shared between them and always have that texture there at the blend point between the two materials. I'm not sure if patches can have their own materials though.

GL 3.0 and DX10 also supply texture array support, which means if all your textures are the same dimensions and format, they can occupy 1 texture unit and you can index into them in your shader when sampling. I think I did add support in my old GL3.x branch of Urho3D, but it might make sense to just add support to the refactor branch that Cadaver is working on.

-------------------------

gawag | 2017-01-02 01:03:49 UTC | #5

[quote]To keep supporting max 8 texture units on terrain patches, you could make different materials which have one texture shared between them and always have that texture there at the blend point between the two materials. I'm not sure if patches can have their own materials though.[/quote]
Yes, I could also use multiple materials if I wanted more textures.
One could also use multiple terrains instead of patches with different materials (if the later one is possible with Urho default terrain engine).

[quote]GL 3.0 and DX10 also supply texture array support, which means if all your textures are the same dimensions and format, they can occupy 1 texture unit and you can index into them in your shader when sampling. I think I did add support in my old GL3.x branch of Urho3D, but it might make sense to just add support to the refactor branch that Cadaver is working on.[/quote]

That sound interesting. Has that more advantages, like regarding performance?

Up to 8 or 16 textures is good enough (for my current use cases). But just three textures for the terrain was not good enough and would have been quite bad.

-------------------------

TikariSakari | 2017-01-02 01:03:49 UTC | #6

Did you try to combine the texture maps? Like baking the texture from top view of the map? I think that is the common way how people put textures on height maps.

-------------------------

gawag | 2017-01-02 01:03:50 UTC | #7

Do you mean always (partly) blending textures together? Or mixing the splatting (detail) textures with one texture that goes over the whole terrain (without repeating)?

-------------------------

TikariSakari | 2017-01-02 01:03:50 UTC | #8

[quote="gawag"]Do you mean always (partly) blending textures together? Or mixing the splatting (detail) textures with one texture that goes over the whole terrain (without repeating)?[/quote]

Like building one texture by blending the textures together with correct UV-mapping to one texture, then splatting it on top of whole terrain (without repeating). Something like this but just progmatically. [url]https://www.youtube.com/watch?v=g2EMquDN7qQ[/url] . I have really no idea how much work doing such thing would be or how to even one would decide what kind of texture to use on what kind of situation. I guess altitude and normals would be one way to determine which texture to use for sampling the texture data from.

-------------------------

gawag | 2017-01-02 01:03:50 UTC | #9

Ah I see. I remember that being used in the Ogre terrain. One texture (without repeating) for the whole terrain and detail textures (with repeating) for being close by.
The guy in the video had the issue of the texture having different grades of detail / sizes depending on how far away he was while painting. Another issue is the required texture size for big terrains. My terrain should cover multiple kilometers (or maybe I'll use multiple terrains) and the camera being quite close to the ground like first/third person or strategy game-ish.
I think I'll keep using the weight texture to paint the terrain with the splatting textures. There should be many possibilities by mixing textures and using different intensities, this may be enough for my use cases. Also I want the terrain heightmap to be generated by random seeds and make the weight texture according to stuff like height, slope and type of area like forest, desert, stone desert,...
This one texture solutions could be useful though for being very far away like in a flight simulator or coming from space to ground level. But it could also add more variation to the ground color by mixing with detail textures... I'll see how far I can get with my weight texture and if that mixing can make enough variations and stop the texture to being to repetitive.

-------------------------

