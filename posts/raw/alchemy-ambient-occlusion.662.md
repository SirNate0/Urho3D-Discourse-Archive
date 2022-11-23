reattiva | 2017-01-02 01:01:57 UTC | #1

Hello, I've adapted the Alchemy/SAO ambient occlusion algorithm by Morgan McGuire:
[graphics.cs.williams.edu/papers/AlchemyHPG11/](http://graphics.cs.williams.edu/papers/AlchemyHPG11/)
[graphics.cs.williams.edu/papers/SAOHPG12/](http://graphics.cs.williams.edu/papers/SAOHPG12/)
It has some faults, especially the blur shaders, but it could be a starting point.

You can find it here:
[bitbucket.org/reattiva/sao-as/downloads](https://bitbucket.org/reattiva/sao-as/downloads)

There is a simple AS script (Alchemy.as) to test it. It uses deferred render path, the occlusion shader needs the depth and normal buffers, but normals can also be calculated realtime on the shader.
It is based on McGuire's demo code (BSD licensed) for SAO, but many of the SAO improvements are not implemented so it is closer to the Alchemy algorithm than the SAO one. I've written some Gaussian blur filters: BlurGaussian and BlurGaussianDepth. They tend to make occlusion too big in the distance so I've added a fade-out effect.
The parameters are very coupled and difficult to adjust, this is exactly the opposite of the original author results, probably there are some bugs around. These parameters are: radius, intensity, projscale and bias. Projscale is used to adjust the radius scaling with the depth, this was not present in the paper so I think this is the bugged part. Bias is used to prevent self occlusion due to depth precision (e.g. a flat surface should be white).
The parameters are changeable with the keyboard (R,F,T,G,Y,H,U,J), you can disable the occlusion effect (V), enable a Gaussian blur (B), enable a depth aware Gaussian blur (N), and display the occlusion buffer (M).
In the script set "bool OpenGL" to false if you use DirectX (I couldn't find a good flag for this).

Notes:

1) In this example the intensity is too high, it should be a very subtle effect, but more important the occlusion buffer is blended with the final viewport (SAO_copy shader). This is not correct, AO should only affect the ambient light. A simple way to do this is to move the "quad SAO_copy" command before the "lightvolumes" command (and enable shadows to appreciate the difference). The "lightvolumes" command is not a good point to do the blend because it uses the add/subtract blend mode.

2) When you use a big radius, the occlusion is not correct around the screen borders because these is no depth buffer to sample outside the screen. To reduce this flaw you can use a G-buffer bigger than the viewport (for example "<rendertarget sizemultiplier="1.05 1.05" />"), you compute the occlusion and then you can use a shader to offset and center it on the screen. This guard band is used only for reading the depth buffer, to avoid calculating the occlusion on it you can use Graphics::SetScissorTest in View::RenderQuad. This could also be done on the "lightvolumes" command in View::SetupLightVolumeBatch. You have to modify the engine but it should not be hard.

3) An improvement of SAO is the use of a depth buffer with mipmaps. To do this you create a texture for the depth buffer with N mipmaps, then you create N framebuffers and attach a different depth mipmap to each of them on COLOR0. Using the first framebuffer you compute the depth buffer, this will be written on the level 0 of the depth texture, then using the other framebuffers and a special shader you can build a mipmap level N by reading the level N-1.
I've still haven't how to do this in Urho (RenderTargets don't have mipmaps), and using mipmaps in HLSL is tricky/impossible with DirectX9 (on GLSL it is possible by enabling "extension GL_EXT_gpu_shader4").

Any comment is really welcomed.

[url=http://postimg.org/image/4tqdy5v77/][img]http://s29.postimg.org/4tqdy5v77/image.jpg[/img][/url]

-------------------------

codingmonkey | 2017-01-02 01:01:58 UTC | #2

Wow, cool! 
I tried to rewrite your script in C ++ and use in my test scene, but the scene did not look like the examples from the video (frog kinght). Maybe I missed something in code.

-------------------------

alexrass | 2017-01-02 01:01:58 UTC | #3

GL_EXT_gpu_shader4 from OpenGL 3.0?

-------------------------

reattiva | 2017-01-02 01:01:58 UTC | #4

[quote="codingmonkey"]the scene did not look like the examples from the video (frog kinght)[/quote]
Any screenshot? If the test scene of the script looks the same then the problem are the shaders or their parameters. Actually, I was never able to make the original demo from McGuire work, so I don't really know if it is supposed to look like that.

[quote="alexrass"]GL_EXT_gpu_shader4 from OpenGL 3.0?[/quote]
This one [url]https://www.opengl.org/registry/specs/EXT/gpu_shader4.txt[/url], so the minimum is OpenGL 2.0, GLSL 1.10 and a card that supports it. Anyway you don't need this for the example, you need it only to work with mipmaps. I've also removed the bitwise operations from the random function (not sure if it was wise), so you really don't need this extension.

-------------------------

alexrass | 2017-01-02 01:01:59 UTC | #5

cool

-------------------------

sabotage3d | 2017-01-02 01:02:07 UTC | #6

Awesome !  I just tried it works like a charm on OSX I did it with C++ instead of AngelScript .
Can someone help me to get this working on mobile for OpenGL ES 2.0 ?

-------------------------

reattiva | 2017-01-02 01:02:09 UTC | #7

[quote="sabotage3d"]Can someone help me to get this working on mobile for OpenGL ES 2.0 ?
[/quote]
I have no experience with OpenGL ES, but if you have a particular problem, post it here, there shouldn't be big differences. However keep in mind that the occlusion and blur shaders are very, very heavy especially on textures reading.

-------------------------

sabotage3d | 2017-01-02 01:02:12 UTC | #8

Thanks reattiva,

I am trying to port it to Opengl ES 2.0, but I am having some problems. 
I am getting these errors. If I try to fix any of these I am getting even deeper errors which are very weird. Any ideas ?

[code]2014-12-26 22:39:36.222 34_DynamicGeometry[26595:60b] Loading resource Shaders/GLSL/SAO_main.glsl
2014-12-26 22:39:36.235 34_DynamicGeometry[26595:60b] Compiled vertex shader SAO_main()
2014-12-26 22:39:36.238 34_DynamicGeometry[26595:60b] Failed to compile pixel shader SAO_main():
ERROR: 0:97: Use of undeclared identifier 'sDepthBuffer'
ERROR: 0:98: Use of undeclared identifier 'edC'
ERROR: 0:99: Use of undeclared identifier 'depthC'
ERROR: 0:116: Use of undeclared identifier 'vsC'
ERROR: 0:121: Use of undeclared identifier 'vsC'
ERROR: 0:145: Use of undeclared identifier 'vsC'
ERROR: 0:157: Use of undeclared identifier 'ssDiskRadius'
ERROR: 0:160: Use of undeclared identifier 'ssOffset'
ERROR: 0:163: Use of undeclared identifier 'sDepthBuffer'
ERROR: 0:163: Use of undeclared identifier 'ssP'
ERROR: 0:164: Use of undeclared identifier 'ssP'
ERROR: 0:164: Use of undeclared identifier 'depthP'
ERROR: 0:167: Use of undeclared identifier 'vsP'
ERROR: 0:167: Use of undeclared identifier 'vsC'
ERROR: 0:169: Use of undeclared identifier 'v'
ERROR: 0:169: Use of undeclared identifier 'v'
ERROR: 0:170: Use of undeclared identifier 'v'
ERROR: 0:177: Use of undeclared identifier 'vv'
ERROR: 0:178: Use of undeclared identifier 'f'
ERROR: 0:178: Use of undeclared identifier 'f'
ERROR: 0:178: Use of undeclared identifier 'f'
ERROR: 0:178: Use of undeclared identifier 'vn'
ERROR: 0:178: Use of undeclared identifier 'vv'
ERROR: 0:189: Use of undeclared identifier 'intensity'
ERROR: 0:204: Use of undeclared identifier 'occlusion'
ERROR: 0:204: Use of undeclared identifier 'edC'
2014-12-26 22:39:36.239 34_DynamicGeometry[26595:60b] Loading resource Shaders/GLSL/BlurGaussianDepth.glsl
2014-12-26 22:39:36.251 34_DynamicGeometry[26595:60b] Compiled vertex shader BlurGaussianDepth()
2014-12-26 22:39:36.255 34_DynamicGeometry[26595:60b] Compiled pixel shader BlurGaussianDepth(SAMPLES=8)
2014-12-26 22:39:36.258 34_DynamicGeometry[26595:60b] Linked vertex shader BlurGaussianDepth() and pixel shader BlurGaussianDepth(SAMPLES=8)
2014-12-26 22:39:37.185 34_DynamicGeometry[26595:60b] Compiled pixel shader BlurGaussianDepth(SAMPLES=8 VERTICAL)
2014-12-26 22:39:37.187 34_DynamicGeometry[26595:60b] Linked vertex shader BlurGaussianDepth() and pixel shader BlurGaussianDepth(SAMPLES=8 VERTICAL)
2014-12-26 22:39:38.135 34_DynamicGeometry[26595:60b] Compiled vertex shader DeferredLight(DIRLIGHT)
2014-12-26 22:39:38.136 34_DynamicGeometry[26595:60b] Shader DeferredLight(DIRLIGHT PERPIXEL SPECULAR) does not use the define PERPIXEL
2014-12-26 22:39:38.139 34_DynamicGeometry[26595:60b] Failed to compile pixel shader DeferredLight(DIRLIGHT PERPIXEL SPECULAR):
ERROR: 0:599: Use of undeclared identifier 'sDepthBuffer'
ERROR: 0:603: Use of undeclared identifier 'depth'
ERROR: 0:605: Use of undeclared identifier 'sAlbedoBuffer'
ERROR: 0:606: Use of undeclared identifier 'sNormalBuffer'
ERROR: 0:618: Use of undeclared identifier 'normalInput'
ERROR: 0:619: Use of undeclared identifier 'worldPos'
ERROR: 0:623: Use of undeclared identifier 'normal'
ERROR: 0:623: Use of undeclared identifier 'worldPos'
ERROR: 0:640: Use of undeclared identifier 'normal'
ERROR: 0:640: Use of undeclared identifier 'worldPos'
ERROR: 0:640: Use of undeclared identifier 'normalInput'
ERROR: 0:641: Use of undeclared identifier 'diff'
ERROR: 0:641: Use of undeclared identifier 'albedoInput'
ERROR: 0:641: Use of undeclared identifier 'spec'
ERROR: 0:641: Use of undeclared identifier 'albedoInput'
2014-12-26 22:39:38.424 34_DynamicGeometry[26595:60b] Loading resource Shaders/GLSL/SAO_copy.glsl
2014-12-26 22:39:38.434 34_DynamicGeometry[26595:60b] Compiled vertex shader SAO_copy()
2014-12-26 22:39:38.436 34_DynamicGeometry[26595:60b] Compiled pixel shader SAO_copy()
2014-12-26 22:39:38.438 34_DynamicGeometry[26595:60b] Linked vertex shader SAO_copy() and pixel shader SAO_copy()[/code]

-------------------------

reattiva | 2017-01-02 01:02:13 UTC | #9

Sorry Sabotage, there are big differences. In ES the depth buffer, sDepthBuffer, is not defined, all your other errors are consequences. This is intended, you can clearly see it in the file \Bin\CoreData\Shaders\GLSL\Samplers.glsl, the other g-buffers are not defined as well, so the deferred render path is not an option in ES.
You can try to build the depth buffer yourself with the Depth.glsl shader and move to the forward render path, but I think a lightmap texture is a better and much cheaper way to have occlusion on mobile.

-------------------------

sabotage3d | 2017-01-02 01:02:13 UTC | #10

I think the OES_depth_texture extension would work. 
Is it enough if I move the code from SAO main into single material assign it to all surfaces and swap sDepthBuffer for OES_depth_texture .
As a first step is it possible to discard the Gaussian blur or any other deffered shaders ?
I already have lightmaps but for moving objects I need some interactive shadows and your solution is looking awesome.

-------------------------

reattiva | 2017-01-02 01:02:13 UTC | #11

I don't think the SAO will work if you move it in a technique. The SAO is like a post-process effect, it needs to work on a quad fullscreen, but if you are trying to limit the AO effect to only some objects then you have a point, but I don't know a good way to do it, maybe using the stencil?
Yes, you can skip the blur and for sure you'd better skip the deferred render path.

For starters, use a simple scene (e.g. 04_StaticScene.as) and try switch it to the ForwardDepth.xml render path. See if you can get a good depth buffer written, you can view it by adding these lines at the end of the render path:
[code]    <command type="quad" tag="depth_copy" vs="CopyFramebuffer" ps="CopyFramebuffer" output="viewport">
        <texture unit="diffuse" name="depth" />
    </command>[/code]
In OpenGL you '''should''' be able to see it as a wonderful sawtooth of colors.

In the forward path you don't have the normal buffer, but in the shader there is a "#if 1" you can use to calculate the normal real-time, it is the part with the "dxdf", unfortunately I think this instruction could be a problem for ES.

-------------------------

sabotage3d | 2017-01-02 01:02:14 UTC | #12

Thanks again for helping me out.

With the ForwardDepth.xml with your additions I am getting this:

On OSX

[img]http://i.imgur.com/YhtKHIb.png[/img]

On IOS

[img]http://i.imgur.com/D5F6eMR.png[/img]

Is the result correct ?
If am getting the same if I attach the Depth.glsl to my objects. 
So we can't bake the normals buffer to texture as well ?

I am trying to add new uniforms for the depth to textures but it is very convoluted.
I have used that before for shadowmaps but I am not sure how to fit it with Urho3d or if it is already provided.
The original code is taken from a book for OpenGL ES.

[code]unsigned int depth_texture,
			 shadowmap_buffer,
			 shadowmap_width  = 128,
			 shadowmap_height = 256;

...

glGenFramebuffers( 1, &shadowmap_buffer );
glBindFramebuffer( GL_FRAMEBUFFER, shadowmap_buffer );

glGenTextures( 1, &depth_texture );
glBindTexture( GL_TEXTURE_2D, depth_texture );

glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST );
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST );

glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE );
glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE );


glTexImage2D( GL_TEXTURE_2D,
			  0,
			  GL_DEPTH_COMPONENT,
			  shadowmap_width,
			  shadowmap_height,
			  0,
			  GL_DEPTH_COMPONENT,
			  GL_UNSIGNED_SHORT,
			  NULL );

glBindTexture( GL_TEXTURE_2D, 0 );

glFramebufferTexture2D( GL_FRAMEBUFFER,
						GL_DEPTH_ATTACHMENT,
						GL_TEXTURE_2D,
						depth_texture,
						0 );

...

glBindFramebuffer( GL_FRAMEBUFFER, shadowmap_buffer );
	
glViewport( 0, 0, shadowmap_width, shadowmap_height );

glClear( GL_DEPTH_BUFFER_BIT );

glCullFace( GL_FRONT )

...

glActiveTexture( GL_TEXTURE0 );
glBindTexture( GL_TEXTURE_2D, depth_texture );[/code]

-------------------------

sabotage3d | 2017-01-02 01:02:14 UTC | #13

I am having some difficulties applying your shader based on the ForwardDepth if I remove the code below from your DeferredSAO.xml it doesn''t render at all.

[code]    <command type="lightvolumes" vs="DeferredLight" ps="DeferredLight">
        <texture unit="albedo" name="albedo" />
        <texture unit="normal" name="normal" />
        <texture unit="depth" name="depth" />
    </command>[/code]

It is possible just to isolate this one for now without the need for any other shaders ?

[code]    <command type="quad" tag="SAO_main" vs="SAO_main" ps="SAO_main" output="occlusion">
        <texture unit="diffuse" name="viewport" />
        <texture unit="normal" name="normal" />
        <texture unit="depth" name="depth" />
        <parameter name="ProjInfo" />
        <parameter name="ProjScale" />
        <parameter name="View" />
        <parameter name="Radius" value="1.0" />
        <parameter name="Bias" value="0.01" />
        <parameter name="ProjScale2" value="1.0" />
        <parameter name="IntensityDivR6" value="1.0" />
    </command>[/code]

-------------------------

reattiva | 2017-01-02 01:02:15 UTC | #14

Download the repository now, I've added a forward path example. In the angelscript example you have to change it from DeferredSAO.xml to ForwardDepthSAO.xml.
Your depth buffer looks good.

-------------------------

sabotage3d | 2017-01-02 01:02:16 UTC | #15

Thanks a lot :slight_smile:
It works perfectly, you saved me hours .
Earlier I tried all the combinations to get it the forward rendering working with your shader, but I couldn't figure it out.

-------------------------

sabotage3d | 2017-01-02 01:02:16 UTC | #16

It seems that projecting on a quad doesn't work great under IOS or there is osmething that is not supported properly.
I am getting this result on IOS after fixing all the errors and warnings. Even setting float occlusion = 0.5;
I cannot get the 50% gray layer. Everything works perfectly under OSX. 

It seems that it displays the depth buffer rather than the diffuse + occlusion on top .

[img]http://i.imgur.com/CgoWIBt.png[/img]

-------------------------

reattiva | 2017-01-02 01:02:17 UTC | #17

No, that doesn't look good.
One thing I forgot and you probably have already fixed it, on IOS you have to add "uniform sampler2D sDepthBuffer;" at the start of SAO_main.glsl, because the one in Samplers.glsl is skipped.
About dFdx and dFdy on ES, I've found this [khronos.org/opengles/sdk/do ... dFdx.xhtml](https://www.khronos.org/opengles/sdk/docs/man31/html/dFdx.xhtml), so it is supported from ES GLSL v3.00. Maybe try adding (as first line) the directive "#version 300 es" to be sure.

-------------------------

sabotage3d | 2017-01-02 01:02:17 UTC | #18

I think the main problem at the moment is in the xml rather than the shader. Because I tried doing simple Gray color overlay using your ForwardDepthSAO.xml  
In SAO_main.glsl I am setting [b]float occlusion = 0.5;[/b]  When I try this under OSX I can see Gray overlay, but it doesn't work under IOS. On IOS it shows only the depth buffer so it means there is something weird that Urho3d does on the ES side.
Also I tried this for the SAO_main.glsl : For the sDepthBuffer I am declaring it as: uniform sampler2D sDepthBuffer;  And for [b]dFdx[/b] and [b]dFdy[/b] I did this[b] #extension GL_OES_standard_derivatives : enable[/b] as mentioned from this link: [stackoverflow.com/questions/9671 ... ve-texture](http://stackoverflow.com/questions/9671705/opengl-es-2-0-derivative-texture)
I also set the precision to : [b]precision highp float; [/b]
Because it was complaining about the precision of the [b]cFrustumSize[/b]

Is there a native way just to render SAO_main on a quad  ?
Is it going to work in a single shader like surface shader ?

Any ideas how to debug this are welcomed :slight_smile:

-------------------------

reattiva | 2017-01-02 01:02:17 UTC | #19

This is where I can't help you further in ES. 
Anyway, I didn't catch your question. SAO is rendered on a quad and it only needs the depth buffer. The only way to make it simpler is to save a depth buffer (the colors rainbow) to an image (png, tga ...) once, then you load it in the depth texture unit of the SAO.
Debugging a shader is a pain in the arse, you print everything on the screen step by step, buffer by buffer... maybe you should try to find a working AO shader for IOS and start from there.

-------------------------

sabotage3d | 2017-01-02 01:02:17 UTC | #20

Thanks a lot I will start from the basics again.

-------------------------

rasteron | 2017-01-02 01:06:26 UTC | #21

Hey guys, I'm trying to add this to a sample game like NSW to test it out. I just need to load the default values without the controls and it doesn't seem to work.

I loaded this values on top:

[code]
// Number of steps in each controller (high = precise+slow)
const float var_steps = 200.0f;

// Enable ambient occlusion effect
bool ao_enable = true;
// Enable a simple Gaussian blur
bool ao_blur = false;
// Enable a depth aware Gaussian blur
bool ao_blurdepth = true;
// Show ambient occlusion raw values
bool ao_only = false;

// uniforms format: Vector3[val, min, max]

// AO radius in scene units
Vector3 ao_radius = Vector3(1.0f, 0.0f, 4.0f);
// AO intensity (in the paper/demo is divided by radius^6, this is commented out)
Vector3 ao_intensity = Vector3(0.15f, 0.0f, 2.0f);
// Radius scale adjust (not present in the paper/demo, TODO to be fixed)
Vector3 ao_projscale = Vector3(0.3f, 0.0f, 1.0f);
// Self occlusion margin
Vector3 ao_bias = Vector3(0.01f, 0.0f, 0.1f);
// Aux vars
Vector3 ao_var1 = Vector3(0.0f, -1.0f, 1.0f);
Vector3 ao_var2 = Vector3(1.0f, 0.0f, 1.0f);[/code]

Then in the setup viewport, I added this:

[code]
effectRenderPath.Append( cache.GetResource("XMLFile", "RenderPaths/DeferredSAO.xml") );
effectRenderPath.SetEnabled("SAO_copy", ao_enable);
effectRenderPath.SetEnabled("BlurGaussian", ao_blur);
effectRenderPath.SetEnabled("BlurGaussianDepth", ao_blurdepth);
effectRenderPath.shaderParameters["Radius"] = Variant(ao_radius.x);
effectRenderPath.shaderParameters["ProjScale2"] = Variant(ao_projscale.x);
effectRenderPath.shaderParameters["IntensityDivR6"] = Variant( ao_intensity.x );
effectRenderPath.shaderParameters["Bias"] = Variant(ao_bias.x);        
effectRenderPath.shaderParameters["Var1"] = Variant(ao_var1.x);
effectRenderPath.shaderParameters["Var2"] = Variant(ao_var2.x);
[/code] 

I'm using other effects such as Bloom, etc. Any ideas on how to get this to work? Thanks! :slight_smile:

-------------------------

hvince95 | 2018-03-17 06:16:35 UTC | #22

If you're still around lol, I had issues when using this with bloom, to solve the problem you need to append the deferredSAO BEFORE you append bloom fxaa2 etc.
Problem is then that multisampling doesnt seem to work anymore. I solved this issue by using the ForwardDepthSAO.xml renderpath. except now I seem to get random crashes every now and then :frowning: Beyone the fact that ForwardDepthSAO is causing  the issue, I have no idea what is wrong!
If anyone has any thoughts it would be appreciated!

-------------------------

