btschumy | 2020-08-14 15:09:19 UTC | #1

I'm finding that my Text3D labels often become invisible as I pan around, viewing the scene from different angles.  I think this happens when they end up behind other (translucent) materials.

I think I need better control over the rendering order and possibly whether it writes to the depth buffer.  Is this possible?

It seems that the only place you can specify this is on the Material.  However, if you set a Material for the Text3D (even a transparent one), the actual text disappears.

Is there any way to gain more control over this?

-------------------------

btschumy | 2020-08-19 19:25:26 UTC | #2

Any thoughts on this?  I'm really stuck.

-------------------------

Eugene | 2020-08-19 19:51:08 UTC | #3

You can use Material for Text3D, you only have to ensure you setup in exactly the same way as default material used by Text3D (shaders, defines, properties).

Why text disappears -- may be anything, I cannot guess the reason from this description.

-------------------------

btschumy | 2020-08-20 14:32:12 UTC | #4

Eugene,

Thanks for the suggestion.  How do I set up a material the same way as needed by Text3D?  Looking through the list of built in materials & shaders, I don't see anything  that references Text3D.  Given that I will been to modify something about them to solve my problem, I can't have it be "exactly the same way as default material".

This video shows what I'm seeing with the labels.  I have moved the Sun label well off the plane of the Galaxy to make sure it never dips below the Galaxy while panning around.  You will see that the label becomes almost invisible at times even though it is in front of the galaxy image.

http://otherwise.com/movies/Urho3D_Label_Problem.mp4

Any thoughts on why this would be happening?

-------------------------

JTippetts1 | 2020-08-20 14:57:01 UTC | #5

You can see how the default material is constructed at https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/UI/Text3D.cpp#L650 which indicates that it is drawn during the alpha pass, and depth-write is disabled. Your galaxy, being translucent, is likely also being drawn in the alpha pass. Geometries drawn during alpha pass are sorted back-to-front, which is a potential source for your issue if your galaxy has depth-write enabled. If the galaxy is drawn first, but the text label lies 'behind' it according to the Z buffer, then the Text won't draw. Back-to-front, painter's algorithm style rendering is rife with potential problems with sorting order like this. You could try using [Material::SetRenderOrder](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/Material.h#L171) on your galaxy and text materials, to ensure a consistent render order despite any depth sorting weirdness, and see if that resolves your issue.

-------------------------

btschumy | 2020-08-20 15:20:59 UTC | #6

[Edited to escape the xml so it actually shows in the post]

JTippetts1,

I will look at that code and try to duplicate the material.  Once I have an actual material, I can change the rendering order on it and se if that helps.

Not sure if it matters but the galaxy image is a one element billboard system.  I do this because you can change the color (including transparency) of the material on the fly, which you can't easily do with a normal node.

This is the galaxy material:

```
<?xml version="1.0" encoding="UTF-8"?>
<material>
    <technique name="Techniques/GalaxyTechnique.xml" />
    <texture unit="diffuse" name="Textures/Galaxy-North.dds" />
    <shader psdefines="ALPHAMASK" />
    <cull value="none" />
</material>
```
Here is the technique:

```
<technique vs="UnlitParticle" ps="UnlitParticle" vsdefines="VERTEXCOLOR" psdefines="DIFFMAP VERTEXCOLOR">
    <pass name="alpha" depthwrite="true" blend="alpha" />
</technique>
```
Thanks for helping.

-------------------------

btschumy | 2020-08-20 16:08:22 UTC | #7

Okay, I've made progress.  I created a Material using the code of Text3D as a guide.  It looks like the secret is that the rendering order needs to be after that of the galaxy material.  Here is what I have:

			var material = Material.FromColor(color);
			var tech = new Technique();
			var pass = tech.CreatePass("alpha");
			pass.VertexShader = "Text";
			pass.PixelShader = "Text";
			pass.BlendMode = BlendMode.Alpha;
			pass.DepthWrite = false;
			material.SetTechnique(0, tech);
			material.CullMode = CullMode.None;
			material.RenderOrder = RENDER_ORDER_LABEL_MAT;
			text3D.Material = material;

This eliminates the disappearing text as I pan around.

This only issue I have now is that the text color is not getting set.  I see black text.  It may be that a texture is not set.  I see the following in the C++ code.

        Material* material = batches_[i].material_;
        Texture* texture = uiBatches_[i].texture_;
        material->SetTexture(TU_DIFFUSE, texture);

I'm not sure how to translate this into the C# case.  I tried just creating a generic texture using "new Texture()" and setting it to the diffuse texture of the material, but that didn't help.

Any thoughts on how to make the font color be used?

Bill

-------------------------

JTippetts1 | 2020-08-20 22:38:40 UTC | #8

The texture is your font glyph texture, so if you you see letters (even if they're only black) then you have the right texture.

Font colors are set as vertex colors when building the batches. When you call Text3D::SetColor, it calls SetColor on it's internal Text member that is used to provide the geometry data.

I'm suspicious of your call to Material.FromColor(color). C++ doesn't have any such thing, so I'm not really sure what it's doing or what kind of material state it's setting behind the scenes, but it's probably not what you want to start from. Just start from a fresh, clean new material. No need for a color parameter, since as I said the font color is set using vertex colors when the geometry is built. The MatDiffColor shader parameter isn't even used in the Text shader,

-------------------------

btschumy | 2020-08-21 02:42:38 UTC | #9

I've tried it both ways, using a fresh "new Material()" and the "Material.FromColor()" and both give the same result: I see the text but it is black.

I've poked around a bit and have tried various ways of initializing things, but with no success.

I will comment again that I get the colored text if I just create the Text3D and use the material it creates.    However, that one has the "disappearing" issue.  I only need to create a Material so I can set the rendering order.  If there was some way I could access the auto-created material, that would be great.  However the material returned by GetMaterial() (or the Material property in C#) is always null.


I'm open to other ideas.

-------------------------

btschumy | 2020-08-23 16:01:06 UTC | #10

I've played with this quite a bit and have been unsuccessful in getting the SetColor to work.  I always have black text when I create my own material.  Once again, here is what I'm doing:

				var material = new Material();
				var tech = new Technique();
				var pass = tech.CreatePass("alpha");
				pass.VertexShader = "Text";
				pass.PixelShader = "Text";
				pass.BlendMode = BlendMode.Alpha;
				pass.DepthWrite = false;
				material.SetTechnique(0, tech);
				material.CullMode = CullMode.None;
				material.RenderOrder = RENDER_ORDER_LABEL;
				text3D.Material = material;
				text3D.SetColor(color);

Would someone be willing to try this in C++ to see if it works there (this is tested on iOS, if that matters).  Either I'm missing some subtle step or there is a bug and this doesn't currently work.

Thanks,
Bill

-------------------------

Pencheff | 2020-08-24 00:15:22 UTC | #11

I'm using the same code in my rich text and it works:
[code]
RichWidgetText::RichWidgetText(Context* context)
 : RichWidgetBatch(context)
{
    Material* material = new Material(context_);
    Technique* tech = new Technique(context_);
    Pass* pass = tech->CreatePass("alpha");
    pass->SetVertexShader("Text");
    pass->SetPixelShader("Text");
    pass->SetBlendMode(BLEND_ALPHA);
    pass->SetDepthWrite(false);
    material->SetTechnique(0, tech);
    material->SetCullMode(CULL_NONE);
    material_ = material;
    material_->SetName("RichWidgetText");
}
[/code]

-------------------------

btschumy | 2020-08-24 14:35:27 UTC | #12

Pencheff,

Thanks for confirming this does work.  One difference between yours and mine is that you explicitly pass a context into the constructors for Material and Technique.  I have modified my code to do:

				var material = new Material(textNode.Context);
				var tech = new Technique(textNode.Context);

But I still get black text.

How are you setting the text color?  Are you calling SetColor() or if it done in some other fashion?

-------------------------

Pencheff | 2020-08-24 18:31:20 UTC | #13

I'm creating text vertexes manually but it works almost the same way as in Text3D::SetColor(). I would check if you have lighting turned on or something related to shaders.

-------------------------

btschumy | 2020-08-24 19:43:53 UTC | #14

Ah, that is a good hint.  I am not using any lighting.  Everything has a diffuse texture and I'm using "Unlit" techniques .  This does work when the default material is used with Text3D.

In the Urho3D  C++ code I see this after the material is created and set:

```
    Material* material = batches_[i].material_;
    Texture* texture = uiBatches_[i].texture_;
    material->SetTexture(TU_DIFFUSE, texture);
```

Do I need to do something to make it diffusive?

I did a GetTexture() on the material for all to the 18 texture units and all are null after creating and setting the material.  I assume the texture created for Text3D is behind the scenes somewhere?  How do I ensure it will display without lights?

-------------------------

btschumy | 2020-08-24 19:58:28 UTC | #15

OK, after playing around a bit more I found that if I do

				pass.PixelShaderDefines = "ALPHAMAP";

Then the colors are visible.  I really know almost nothing about shaders (or 3D graphics in general), but this does seem to work.  I discovered this looking through the Text.glsl shader and seeing that define and the code when defined seemed to be setting the FragColor.

Is this really the solution or am I just getting lucky?

Programming by trial and error.  What a concept.

-------------------------

btschumy | 2020-08-24 20:57:34 UTC | #16

I know you guys are ready to give up with me an my questions.  However, after discovering the ALPHAMAP trick above, everything *almost* works.  But if I draw the text *before* the galaxy (which I need to do for other reasons), I get the transparent color of the letters drawn in black.

I used to have this problem with the objet symbols themselves until SirNate clued me into setting the ALPHAMASK psdefine.  However, this doesn't appear to work for "Text".

Any ideas on what is happening here.

![image|690x495](upload://s2UHCoqvuPHqfYlUA13QUA0yBtT.jpeg)

-------------------------

George1 | 2020-08-25 03:27:17 UTC | #17

The best way to get answer is to have some code or to create a minimal example.

-------------------------

btschumy | 2020-08-25 14:27:13 UTC | #18

This thread shows my code, although it is admittedly scattered through several posts in this thread.  As far as making an example, the problem is I'm using UrhoSharp and C#.  I assume most of you are not set up to run a small example like that.

I was hoping someone would recognize what would cause the transparent regions of the font to be drawn black.  It only happens when the galaxy material is drawn behind them (the text is rendered first).

I think I will try modifying the "Text" shader and try to add the code that other shaders use when the ALPHAMASK define is set.


LATER.....


I cloned the Text.glsl shader and created my own Text_AlphaMask.glsl shader.  I add the following code to the non - SIGNED_DISTABCE_FIELD case:

        vec4 diffInput = texture2D(sDiffMap, vTexCoord);
        #ifdef ALPHAMASK
            if (diffInput.a < 0.5)
                discard;
        #endif

Amazingly, this does seem to solve my problem.  

Of course, I will need to make a similar change to the Text.hlsl file.

Not sure if this is a good or bad solution.  How often to the shaders get updated?  I may need to re-patch this shader if a future version of UrhoSharp (assuming there ever is one) uses a more recent version of Urho3D with a new Text.glsl file.

-------------------------

