ghidra | 2017-01-02 01:02:18 UTC | #1

old question:
[quote]i've tried:
[code]
<rendertarget name="viewport" sizedivisor="2 2" filter="false" format="rgba"/>     <!--or-->
<rendertarget name="gbuffer" sizedivisor="2 2" filter="false" format="rgba"/>       <!--or-->
<rendertarget name="viewport" sizemultiplier="0.5 0.5" filter="false" format="rgba"/>     <!--or-->
<rendertarget name="gbuffer" sizemultiplier="0.5 0.5" filter="false" format="rgba"/>
[/code]

but nothing causes the default renderpath viewport to render at half size.
I have successfully, rendered to a half size quad and sampled the texture, but I get antialiasing, even with the filter set to false. Filter set to true i get super aliasing. My desire is to get not aliases, and very crisp colors with no interpolated values.

I guess something that uses GL_TEXTURE_MIN_FILTER and GL_TEXTURE_MAX_FILTER set to GL_NEAREST. (at least that is what this link said [url]http://stackoverflow.com/questions/17560335/glsl-render-solid-pixels-without-interpolation-or-antialiasing[/url] without getting into the c++ side of things...

Is there a simple way to view fullscreen but still render a very crisp no aliased render.

I've also tried to change the graphics settings to half my screen resolution then set fullscreen to true. That actually is decent, but what should look like a single pixel looks like a small plus sign.

The best looking results i've gotten are from the size divisor, but then I'm getting some color interpolation that i'd rather not have.[/quote]

-------------------------

ghidra | 2017-01-02 01:02:20 UTC | #2

So it looks like I just want to set the filter node to "GL_NEAREST"

I can see in c++ there is a way to set the default filter mode in graphics, however. I dont think I can with angelscript. Also, setting it in C++ to FILTER_NEAREST and setting the renderpath to filter="true" didnt seem to actually use nearest mode.

If there a way to do this?
I dont want the rendering to do any filtering. It would be super cool to just be able to set that on a shader level, or even in the render path for the rendertarget.

Thanks for any help.

-------------------------

reattiva | 2017-01-02 01:02:20 UTC | #3

Actually when you set "filter=true" you ask for the bilinear filter, instead if you don't want any filtering on your buffer then you can have the nearest mode by setting "filter=false".
Look at the function: Renderer::GetScreenBuffer

-------------------------

ghidra | 2017-01-02 01:02:20 UTC | #4

I see, it does in fact.
When I render to a sizedivisor 2 2 buffer, i'm getting half values or what look like interpolated values. Which is not desireable for what I am doing. I'll have to look into another way. Thanks for point that out.

So then it might be applyig a filter when I sample a half sized rendertarget.
Where should I look for that? thanks

-------------------------

reattiva | 2017-01-02 01:02:21 UTC | #5

From what I read in the code, FILTER_NEAREST works on both magnification and minification.
Try stepping through the code and see what happens in Texture::UpdateParameters when you are creating your buffer.

-------------------------

ghidra | 2017-01-02 01:02:22 UTC | #6

Yeah im not sure what the deal is really. I would take your advice, but that is over my head already. Im just a script pesant.
However, this code from this answer on stackoverflow seemed to do the trick with some silly modifications:
[url]http://stackoverflow.com/questions/5879403/opengl-texture-coordinates-in-pixel-space/5879551#5879551[/url]

[code]
vec2 s = (1.0/(cGBufferInvSize.xy))*2.0;
vec2 new_uv = (2.0*((vScreenPos.xy / vScreenPos.w)*s) + 0.5)/(2.0*s);
[/code]

Using this when sampeling a fullsize buffer to a half sized quad, and it gives me crisp edges again.

-------------------------

