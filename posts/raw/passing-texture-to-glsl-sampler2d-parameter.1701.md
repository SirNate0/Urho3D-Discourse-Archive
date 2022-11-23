atai | 2017-01-02 01:09:34 UTC | #1

Hi, I am using a custom GLSL shader with Urho3D (1.5).  I have managed to get the shader to properly compile (taking some work to get around resource path handling for shaders...).

I have two "uniform sampler2D" parameters y_tex and uv_tex  (in GLSL file sy_tex and suv_tex, per the convention of Urho3D).

I need to pass in image data I acquired elsewhere in to the shader as the value of these two parameters.  What is the proper way to do so?  I know it should be done via SetShaderParameter("y_tex", Variant(...));

but how do I create the Variant?

There are examples to pass in simple values like a Vector2 or Vector3.  But
I see no example code to bind a two dimensional image, or just as a blob (a C char buffer), to such a GLSL shader parameter of type "uniform samplr2D".  Thanks for any information.

-------------------------

rasteron | 2017-01-02 01:09:34 UTC | #2

Hey atai,

In regard to Sampler2D example, you can checkout my [url=http://discourse.urho3d.io/t/pixelate-effect-glsl/1292/1]Pixelate effect[/url] for reference.

Hope that helps.

-------------------------

atai | 2017-01-02 01:09:35 UTC | #3

[quote="rasteron"]Hey atai,

In regard to Sampler2D example, you can checkout my [url=http://discourse.urho3d.io/t/pixelate-effect-glsl/1292/1]Pixelate effect[/url] for reference.

Hope that helps.[/quote]


Thanks.  From the example I don't see data being passed in from C++ code to the uniform sampler2D shader variable.  Did I miss that part, if that is done in this project somewhere?  Or I shall look for other projects to see how I can bind data in C++ code to a sampler2d shader variable...

-------------------------

rasteron | 2017-01-02 01:09:35 UTC | #4

[quote="atai"][quote="rasteron"]Hey atai,

In regard to Sampler2D example, you can checkout my [url=http://discourse.urho3d.io/t/pixelate-effect-glsl/1292/1]Pixelate effect[/url] for reference.

Hope that helps.[/quote]


Thanks.  From the example I don't see data being passed in from C++ code to the uniform sampler2D shader variable.  Did I miss that part, if that is done in this project somewhere?  Or I shall look for other projects to see how I can bind data in C++ code to a sampler2d shader variable...[/quote]

No problem, I think you are looking for something else and that example is just a simple one. Yes, try and look for other example projects or just wait for other answers/tips. Good luck :slight_smile:

-------------------------

cadaver | 2017-01-02 01:09:37 UTC | #5

Ultimately there needs to be a texture bound to the correct unit (Graphics::SetTexture() getting called), and Urho needs to know the association between sampler names and texture unit numbers. You can't bind texture data with SetShaderParameter().

When GLSL sampler names aren't the predefined ones like sDiffMap, there is a convention that the sampler name ends in a number which is the texture unit. Take a look at the TerrainBlend.glsl shader for example, which defines the following custom samplers:

[code]
uniform sampler2D sWeightMap0;
uniform sampler2D sDetailMap1;
uniform sampler2D sDetailMap2;
uniform sampler2D sDetailMap3;
[/code]

Then, in the Terrain.xml material these would be assigned as following:

[code]
<texture unit="0" name="Textures/TerrainWeights.dds" />
<texture unit="1" name="Textures/TerrainDetail1.dds" />
<texture unit="2" name="Textures/TerrainDetail2.dds" />
<texture unit="3" name="Textures/TerrainDetail3.dds" />
[/code]

If you're making a postprocess effect (quad renderpath command), the texture assignments would naturally happen in the postprocess definition instead.

-------------------------

atai | 2017-01-02 01:09:38 UTC | #6

Great.  Thanks for the reply.  This would make a good wiki page topic...

-------------------------

