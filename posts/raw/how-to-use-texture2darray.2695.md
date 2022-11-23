Enhex | 2017-01-11 18:38:27 UTC | #1

I couldn't find any example of how to use Texture2DArray, and even after looking at the source code I didn't find out how to use it.

Can someone please explain how it's used and give an example?

-------------------------

JTippetts1 | 2017-01-11 20:03:29 UTC | #2

I use it in my custom terrain shader to provide 8 (or more) different terrain detail textures.

In GLSL:

uniform sampler2DArray sDetailMap2;

Then, in the pixel shader, to sample it use:
texture(sDetailMap2, vec3(vDetailTexCoord.xz, 1)); // To index texture at array location 1

In HLSL:

Texture2DArray tDetailMap : register(t2);;
SamplerState sDetailMap : register(s2);

In pixel shader:
tDetailMap.Sample(sDetailMap, float3(iDetailTexCoord.xz, 0)); // To index texture at array location 0

The gist of it is that a texture array object is an array of textures. In order to sample one, you have to provide the UV coordinates as well as the index of the texture to use. As in above examples, in GLSL you use a vec3(uv, index) to sample, and in HLSL use a float3(uv, index) to sample.

For the textures, you specify an XML file listing the textures to use in the array

    <texturearray>
    	<layer name="Textures/pebbles.png" />
    	<layer name="Textures/sand.png" />
    	<layer name="Textures/grass.png" />
    	<layer name="Textures/pebbles2_diff.png" />
    	<layer name="Textures/bigrocks1_diffdisp.png" />
    	<layer name="Textures/cliff.png" />
    	<layer name="Textures/rockface1.png" />
    	<layer name="Textures/cliff2.png" />
    </texturearray>

And you specify it in the material:

    <material>
        <technique name="Techniques/TerrainEdit8TriPlanar.xml" />
 
    	<texture unit="2" name="Textures/diff.xml" />
        <texture unit="3" name="Textures/normal.xml" />
       
    </material>

You can see the full text of my 8-detail texture tri-planar terrain shader at http://pastebin.com/hZy1Gf0E

-------------------------

Enhex | 2017-01-11 21:15:31 UTC | #3

Would it make sense for Urho3D to provide support for texture arrays in built-in shaders for general use?

-------------------------

jmiller | 2017-01-12 04:09:15 UTC | #4

If I may, a reference to a related thread:
http://discourse.urho3d.io/t/terrain-editor/765

-------------------------

feresmu | 2017-10-24 20:41:23 UTC | #5

Hi

When I try to run on Android I've go a error in terrain.glsl

uniform sampler2DArray sDetailMap1;

it seems that sampler2DArray doesn't work on ANdroid.

Is there a way to avoid that error?

-------------------------

jmiller | 2017-10-24 21:02:01 UTC | #6

Hi feresmu,

I assume the shader code you used is intended for desktop targets.
Unfortunately, only later versions of OpenGL ES (not 2.0) support texture arrays (though it is still possible to pass indices as uniforms and switch units on that).

-------------------------

feresmu | 2017-10-29 18:04:19 UTC | #7

Hi carnalis.

I tried to change
uniform sampler2DArray sDetailMap1;
to
uniform sampler2D sDiff1;
uniform sampler2D sDiff2;
uniform sampler2D sDiff3;

uniform sampler2D sNorm4;
uniform sampler2D sNorm5;
uniform sampler2D sNorm6;

uniform sampler2D sSpec7;
uniform sampler2D sSpec8;
uniform sampler2D sSpec9;

uniform sampler2D sHeight10;
uniform sampler2D sHeight11;
uniform sampler2D sHeight12;

and all texture to texture2D
(
weights.r*=texture(sDetailMap1, vec3(vDetailTexCoord,9)).r;
to
weights.r*=texture2D(sHeight10, vDetailTexCoord).r;
)

but it doesn't work:

![screen|281x500](upload://u6MEUlz5IzEQzPC6yiLAwNhXFRx.jpg)

any ideas?

-------------------------

