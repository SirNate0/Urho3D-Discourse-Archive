najak3d | 2020-07-21 14:51:45 UTC | #1

We are using UrhoSharp.

We create a lot of quads (that each render an icon).   Each has a color that should be looked up in a table.  I'd like to have each vertex use the "Y" Position component simply as an Index into this Color Table, as shown in this HLSL mock-up:

uniform float3[] cColorTable;

void VS(float4 iPos : POSITION)
{
     int colorIndex = int(iPos.Y);
     oColor = cColorTable[colorIndex];
     iPos.Y = 0;
     .....
}

How do you fill the cColorTable[] data from Urho?

I saw an API for "Graphics.SetShaderParameter(StringHash Name, float* data, uint count)" - but this appears to be too "global".  We're just wanting to set the cColorTable[] for this one material, similar to what we see with "material.SetShaderParameter(...)" but there are no overloads here for setting an array of values.

This solution is needed for other shaders as well.

If we are forced to use the "Graphics.SetShaderParameter(name, float* data, uint count)" interface, it seems like we would need to follow some special method for inserting this logic at the appropriate time before each Batch render call (as the data may render for each batch of renderables).  When we set it on the "Material", I'm assuming that Urho3D magically handles this timing for us.   So it's a bit frustrating that Urho3D Material.SetShaderParameter doesn't permit us to set Array data.

-------------------------

Modanung | 2020-07-21 19:00:22 UTC | #2

How about using a ramp `Texture` instead?

-------------------------

najak3d | 2020-07-21 19:27:29 UTC | #3

Modanung.  I see.  So I could encode my data into a Texture, and sample it.  For a Color Table, it could just be a Texture that is size  1 x N, and each column of the texture is a different color.  Is that what you are suggesting?  Or something else?

-------------------------

najak3d | 2020-07-21 19:31:52 UTC | #4

I am trying the following code where the colors are hard coded into the shader (because I don't know how to set these values via the Urho API), and this DOES NOT WORK.  It compiles, but all colors turn out to be opaque black.

[quote="najak3d, post:1, topic:6279"]
uniform float4[] cColorTable = { float4(1.0, 0.0, 0.0, 1.0), float4(0.0, 1.0, 0.0, 1.0) };

void VS(float4 iPos : POSITION)
{
int colorIndex = int(iPos.Y);
oColor = cColorTable[colorIndex];
iPos.Y = 0;
…
}
[/quote]

What am I doing wrong?  It would be "OK" to hard-code these values, if there isn't a better way to do it dynamically.

-------------------------

Modanung | 2020-07-21 19:43:02 UTC | #5

[quote="najak3d, post:3, topic:6279"]
Is that what you are suggesting?
[/quote]

Yes, something like that. You could generate the `Texture` during runtime and reap all the benefits of a `Resource` and share it among different materials. You could write the colors to the `Image`, just as you would fill the array. I think it might turn out N x 1.

Shaders like data to be presented as textures beyond a certain level of complexity, and I think this method would fit Urho's API more elegantly.

-------------------------

Eugene | 2020-07-22 10:08:02 UTC | #6

[quote="najak3d, post:4, topic:6279"]
What am I doing wrong?
[/quote]

First, all uniforms must be inside uniform buffers.
Second, all uniforms must be initialized externally from C++/C# code using `Material::SetShaderParameter` or equivalents. Whatever values you hard-code in shaders are outright ignored.

I'd use some unused texture slot of `Material`, I think you have at least one.

-------------------------

najak3d | 2020-07-22 14:13:08 UTC | #7

Eugene, thanks!  I have resigned myself to using a Texture as the means for storing Vector Array data, although I'd surely prefer to use Uniform buffers, if they were supported in the future.

Here's the sample HLSL that I imagine writing for this:

int colorIndex = iPos.y;
float colorIndexNormalized = colorIndex / 256.0;   // assumes the color palette is 256 sized palette.
float4 color = Sample2D(Custom1Map, float2(colorIndexNormalized, 0));
oColor = color;

And from the code, to assign this material texture:

	material.SetTexture(TextureUnit.Custom1, colorPaletteTexture);

Does this look right?
(NOTE: I assume that inside the shader we use the "{TextureUnitValue}Map" to access the texture, yes?)


And is there something special I need to do to ensure that my Custom1Map doesn't employ LOD's?  (i.e. I always want to be sampling the full resolution LOD0)

Thanks in advance!

-------------------------

