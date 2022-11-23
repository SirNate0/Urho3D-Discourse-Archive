Avagrande | 2019-08-18 18:01:43 UTC | #1

Hello

I am trying to make a new render target in the render path with an alpha pass.
It doesn't work ONLY in the new render target and not in the default. 

I am not sure why but it looks like when I am drawing on top its clearing the objects beneath it.

I am using the same materials and techniques for both images. The only difference is the render path. 

I copied the forward render path and moved its alpha pass out into my own render path extension where I render alpha in its own render target and then draw the render target on top of the screen last.

Here is my extension for drawing the render target to the screen:
```
<renderpath>

    <rendertarget name="tile_lights" tag="TileLighting" sizedivisor="1 1" format="rgba" filter="true" />
    <command type="clear" tag="TileLighting" color="0 0 0 0" output="tile_lights" />

    <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" output="tile_lights"/>
    <command type="quad" tag="TileLighting" vs="ApplyTexture" ps="ApplyTexture" psdefines="DIFFMAP"  blend="alpha">
        <texture unit="diffuse" name="tile_lights" />
    </command>

</renderpath>
```


here is the screenshot:

![render_target|516x500](upload://7Lh0XpW19mjGYWIY0AQRHc7Yx4g.png) 

However it should look like this, as rendered without the additional render path and with the default alpha pass.

![default|643x500](upload://hFxUwXzXxkW7KbifSOgiclIsSaI.png) 


The only difference between these two images is where I put my alpha pass, either in the default render target or my own. 

Why does the alpha pass blend improperly when using a render target?

One thing to note aswell, if I have two alpha passes then I get a hard crash, is there any magic done in the alpha pass that I am not aware of?

Some more information:
- I am using opengl 
- I use Forward render path as my base ( although this occurs still if I erase all commands from it excluding clear pass
- This happens to ANY render target that renders alpha even if there is a single pass, so if I push everything from the forward render path to render target I still get the same blending issue.
- this only happens when I use any alpha blending inside a render target that isn't the default

-------------------------

Sinoid | 2019-08-18 20:34:53 UTC | #2

> One thing to note aswell, if I have two alpha passes then I get a hard crash, is there any magic done in the alpha pass that I am not aware of?

forward-lights, deferred-lights, gbuffer, `base`, `alpha`, `light`, `'litbase`, and `litalpha` passes are special and you can only have one of each in a render-path or things will break. Renderpath isn't anywhere near as generic as it appears because of all of the queue construction/maintenance.

-------------------------

Avagrande | 2019-08-18 20:49:27 UTC | #3

thanks. 
I did notice a mention of a "customalpha" pass in the docs related to render path so I think its not unexpected to have two passes one with default alpha and another for different objects and it wont crash unless the passes are identical which I have no problem with. What I am more concerned about is the differences between the default render targets blending and other render targets. 
It shouldn't make a difference if I do a alpha pass on the default target or if I do it on a different target and then render it on default afterwards, unless I am misunderstanding something.

Sadly this effect happens regardless of how many passes you do, just as long as the pass is put into a render target it will produce the improper blending, I tried to isolate it with just a clear pass and it still kept happening.

-------------------------

Bananaft | 2019-08-19 07:44:42 UTC | #4

You probably need to use premultiplied alpha in this case.

-------------------------

Avagrande | 2019-08-19 08:30:10 UTC | #5

although at first it looks like setting premulalpha works, it doesn't when I set the mat diff color to anything other than white eg ( 1 1 1 1 ) so if I set the mat diff color to ( 0.9 0.9 0.9 1 ) I get the same effect again.

I am not sure whats interfering with it, but I need the alpha to be rendered to a flat 2d texture as I want to use it later with a custom blending shader.

-------------------------

Avagrande | 2019-08-19 13:56:30 UTC | #6

Not sure why but whenever I set the alpha to premultiplied it always goes more and more white until it dissolves, even though I am clearing all the frame buffers and everything else... not sure where that information is kept which creates the whiteness effect but its probably linked to the alpha as it seems like rgb values in alpha blend mode somehow affect alpha itself

-------------------------

Bananaft | 2019-08-22 11:48:20 UTC | #7

Are you setting permultiplied alpha for scenepass or for ApplyTexture command?
I'm not sure how it should be, but you probably need to set is for both and multiply color by alha in pixel shader.

See last section of this article:
https://developer.nvidia.com/content/alpha-blending-pre-or-not-pre


>I am clearing all the frame buffers and everything else

I recomend using RenderDoc to make sure everything is cleared and see how your render targets look on every stage of the process.

Also, if you can share a project with me, I can check it.

-------------------------

Avagrande | 2019-08-22 20:39:08 UTC | #8

I am setting it for the quad command yeah, that works... somewhat. pre-multiplied alpha for the pass as placed in technique isn't what I want as it renders black squares and not the alpha that I want.

I just want an alpha pass like you would normally do it without a render target. currently I have found a work around and moved on form this particular problem. 

I would still like it to be solved since I might need to do this at a later point so I will make a sample for you to play around with it since I think this might be a bug, currently a bit busy so I will post it later.

-------------------------

Sinoid | 2019-08-22 21:41:58 UTC | #9

You'd have to tweak things to use premultiplied if your textures aren't designed for multiplied alpha - (`float4 newRGBA = float4(oColor.rgb * diffColor.a, 1.0)`, just passing a regular alpha image off as premultiplied isn't going to work as intended (outside of coincidence or mistakenly believing that's how premul works).

That really shouldn't be the problem though. 

You need to fire-up render-doc and see what the differences are. 

Garbage depth configuration or differences in the alpha blend func (of the separable state Urho doesn't use) on the backbuffer vs the render-target could do it. Alpha func seems more suspect since depth trash should be really really obvious. Either-way you need to break out render-doc.

-------------------------

Avagrande | 2019-10-25 11:50:11 UTC | #10

I encountered this issue again later on and I traced it down to blending mode.
Urho3d currently uses glBlendFunc for its blending: 

At OGLGraphics.cpp at line 1779:
    glBlendFunc(glSrcBlend[mode], glDestBlend[mode]);
I changed it to 
    glBlendFuncSeparate(glSrcBlend[mode], glDestBlend[mode], GL_ONE, GL_ONE);

As this correctly blends with RGBA. I discovered that with some of the other transparent images I was rendering they would not take into the account transparency of the images beneath them. 
If a pixel on the image beneath is at alpha 1 and I draw another image with a pixel at 0.5 the final render would have alpha 0.5 instead of 1. In some cases this even created gaps. The above changes fixes that blending issue. This also fixes the annoying white lines around transparent images.

To see a demo of this you can try: 
https://www.andersriggelsen.dk/glblendfunc.php 
with:
Display: Final RGBA and glBlendFunc at GL_SRC_ALPHA and GL_ONE_MINUS_SRC_ALPHA this should give you white outlines next change it to glBLendFuncSeperate and set GL_ONE for alpha for both dest and src. 

you can clearly visualize the effect if you swap the image to a gradient.

-------------------------

