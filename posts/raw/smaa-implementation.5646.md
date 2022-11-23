Athos | 2019-10-04 21:50:30 UTC | #1

I'm trying to implement the SMAA post-process in Urho3D (D3D11); but it's not working (at least not fully).
The shader itself is from here
[https://github.com/iryoku/smaa/blob/master/SMAA.hlsl](https://github.com/iryoku/smaa/blob/master/SMAA.hlsl)

So I created a PostProcess xml file:
(PostProcess/SMAA.xml)
>     <renderpath>
>     	<rendertarget name="EdgesTex" sizedivisor="1 1" format="rgba" filter="true" />
>     	<rendertarget name="BlendTex" sizedivisor="1 1" format="rgba" filter="true" />
>     	<command type="clear" color="0 0 0 0" output="EdgesTex" />
>     	<command type="clear" color="0 0 0 0" output="BlendTex" />
>     	<command type="quad" vs="SMAA" ps="SMAA" vsdefines="_EDGE_DETECTION" psdefines="_EDGE_DETECTION" output="EdgesTex">
>     		<parameter name="SMAAMetricSize" value="1280.0 720.0" />
>     		<texture unit="diffuse" name="viewport" />
>     	</command>
>     	<command type="quad" vs="SMAA" ps="SMAA" vsdefines="_BLEND_WEIGHT" psdefines="_BLEND_WEIGHT" output="BlendTex">
>     		<parameter name="SMAAMetricSize" value="1280.0 720.0" />
>     		<texture unit="diffuse" name="EdgesTex" />
>     		<texture unit="normal" name="Textures/SMAA_Area.bmp" />
>     		<texture unit="specular" name="Textures/SMAA_Search.bmp" />
>     	</command>
>     	<command type="quad" vs="SMAA" ps="SMAA" vsdefines="_NEIGHBORHOOD_BLEND" psdefines="_NEIGHBORHOOD_BLEND" output="viewport">
>     		<parameter name="SMAAMetricSize" value="1280.0 720.0" />
>     		<texture unit="diffuse" name="viewport" />
>     		<texture unit="normal" name="BlendTex" />
>     	</command>
>     	<command type="quad" vs="CopyFramebuffer" ps="CopyFramebuffer" output="viewport" >
>     		<texture unit="diffuse" name="BlendTex" />
>     	</command>
>     </renderpath>

Then the shader used by the Post Process:
(Shaders/SMAA.hlsl)
>     #include "Uniforms.hlsl"
>     #include "Transform.hlsl"
>     #include "Samplers.hlsl"
>     #include "ScreenPos.hlsl"
>     #include "PostProcess.hlsl"
> 
> 
>     // ====================================================
>     // SMAA DEFINITIONS
>     // ====================================================
>     #ifdef COMPILEVS
> 
>     cbuffer CustomVS : register(b6)
>     {
>     	float2 cSMAAMetricSize;
>     }
> 
>     #endif
> 
>     #ifdef COMPILEPS
> 
>     cbuffer CustomPS : register(b6)
>     {
>     	float2 cSMAAMetricSize;
>     }
> 
>     #endif
> 
> 
>     #define SMAA_RT_METRICS float4(1.0 / cSMAAMetricSize.x, 1.0 / cSMAAMetricSize.y, cSMAAMetricSize.x, cSMAAMetricSize.y)
>     #define SMAA_HLSL_4 1
>     #define SMAA_PRESET_HIGH
> 
>     // iryoku's SMAA implementation
>     #include "SMAA.inc.hlsl"
> 
> 
>     // ====================================================
>     // VERTEX SHADER
>     // ====================================================
>     void VS(float4 iPos : POSITION,
>     	out float2 oScreenPos : TEXCOORD0,
>     #if _EDGE_DETECTION
>     	out float4 oOffset[3] : TEXCOORD1,
>     #endif
>     #if _BLEND_WEIGHT
>     	out float2 oPixCoord : TEXCOORD1,
>     	out float4 oOffset[3] : TEXCOORD2,
>     #endif
>     #if _NEIGHBORHOOD_BLEND
>     	out float4 oOffset : TEXCOORD1,
>     #endif
>     	out float4 oPos : OUTPOSITION)
>     {
>     	float4x3 modelMatrix = iModelMatrix;
>     	float3 worldPos = GetWorldPos(modelMatrix);
>     	oPos = GetClipPos(worldPos);
>     	oScreenPos = GetScreenPosPreDiv(oPos);
> 
>     #if _EDGE_DETECTION
>     	SMAAEdgeDetectionVS(oScreenPos, oOffset);
>     #endif
> 
>     #if _BLEND_WEIGHT
>     	SMAABlendingWeightCalculationVS(oScreenPos, oPixCoord, oOffset);
>     #endif
> 
>     #if _NEIGHBORHOOD_BLEND
>     	SMAANeighborhoodBlendingVS(oScreenPos, oOffset);
>     #endif
>     }
> 
> 
>     // ====================================================
>     // PIXEL SHADER
>     // ====================================================
>     void PS(float4 iPos : SV_POSITION,
>     	float2 iScreenPos : TEXCOORD0,
>     #if _EDGE_DETECTION
>     	float4 iOffset[3] : TEXCOORD1,
>     #endif
>     #if _BLEND_WEIGHT
>     	float2 iPixCoord : TEXCOORD1,
>     	float4 iOffset[3] : TEXCOORD2,
>     #endif
>     #if _NEIGHBORHOOD_BLEND
>     	float4 iOffset : TEXCOORD1,
>     #endif
>     	out float4 oColor : OUTCOLOR0)
>     {
>     #if _EDGE_DETECTION
>     	float2 luma;
> 
>     	// Generate the SMAA edgesTex
>     	//
>     	// tDiffMap = viewport
> 
>     	luma = SMAALumaEdgeDetectionPS(iScreenPos, iOffset, tDiffMap);
> 
>     	oColor = float4(luma, float2(0.0, 0.0));
>     #endif
> 
>     #if _BLEND_WEIGHT
>     	// Generate SMAA blendTex
>     	//
>     	// tDiffMap = edgesTex
>     	// tNormapMap = area texture
>     	// tSpecMap = search texture
> 
>     	oColor = SMAABlendingWeightCalculationPS(iScreenPos, iPixCoord, iOffset, tDiffMap, tNormalMap, tSpecMap, 0);
>     #endif
> 
>     #if _NEIGHBORHOOD_BLEND
>     	// Generate final result
>     	//
>     	// tDiffMap = viewport
>     	// tEmissiveMap = BlendTex
> 
>     	oColor = SMAANeighborhoodBlendingPS(iScreenPos, iOffset, tDiffMap, tEmissiveMap);
>     #endif
>     }

The edge detection is working:
![edges_tex|666x500](upload://yzbTfj6FbeyHEhp3hv7NAL0Lrl1.png) 

but the blending weight calculation and final blending is not.
I'm not experienced with shaders so any help is greatly appreciated.

-------------------------

PsychoCircuitry | 2019-10-03 20:29:32 UTC | #2

So just at a glance, i noticed that your AreaTex and SearchTex are being loaded as xml files. They will not load properly this way, no errors are generated either. But if you change those to your actual textures .dds or .png or whatever, that might fix your issue. I believe the accompanying xml file for the texture will be parsed when loading the texture thru the renderpath this way as well, hope this helps.

-------------------------

Athos | 2019-10-04 01:50:53 UTC | #3

Specifying the texture with it's image extension helped (The weight blend pass outputs something), but still not working.

I've run this image in the SMAA demo application and the result is a properly anti-aliased image.
[https://imgsli.com/NzI3Ng](https://imgsli.com/NzI3Ng)

-------------------------

PsychoCircuitry | 2019-10-04 14:22:41 UTC | #4

Ok, I read through the shader. It relies on bilinear filtering for the weight calculation, so change the filter mode of your two render targets to true. That should get you closer to what you expect. Hope that helps.

-------------------------

Athos | 2019-10-04 21:56:23 UTC | #5

Even after changing the filter mode of the render targets, the result of weight calculation is wrong;
I tried using .dds, .bmp and .png textures, to no avail.

I've edited the first post to reflect the current PostProcess/Shader code I'm using.

-------------------------

PsychoCircuitry | 2019-10-04 22:54:52 UTC | #6

Can you post another comparison? I did a really quick implementation like yours this morning and the results looked ok on one of the examples. I didn't compare with the smaa demo tho. Also I was on directx9 as that's what I have compiled currently.

Edit: Also, what do your xml files look like for the area and search textures?
This is what I used for both
`<texture>`
`    <address coord="u" mode="clamp" />`
`    <address coord="v" mode="clamp" />`
`    <address coord="w" mode="clamp" />`
`    <mipmap enable="false" />`
`    <quality low="0" />`
`</texture>`

Edit again: also make sure you're using the right channels for the area texture. I converted the dx10 images to pngs and had to manually define use of the rg channels as the dx9(sm3) version defaults to ra channels, but if I remember correctly the sm4+ defaults to rg channels anyway, just a thought tho if you were maybe instead using the dx9 texture

-------------------------

Athos | 2019-10-05 03:59:52 UTC | #7

The texture xmls are exactly like that (I also tried adding a filter="nearest"). Setting the render targets as sRGB made no difference.

These are the results from the DX10 demo:
[https://imgur.com/a/IvqMo7y](https://imgur.com/a/IvqMo7y)

These are the results I'm getting:
[https://imgur.com/a/FYfsFHc](https://imgur.com/a/FYfsFHc)

There's a huge difference between them, although the settings are the same: SMAA_PRESET_ULTRA with LUMA edge detection.

-------------------------

PsychoCircuitry | 2019-10-05 09:52:52 UTC | #8

What does the result of your AA look like? Is it missing edges?

Here's what it looks like on my setup

SMAA
![aa|580x500](upload://dpObVEExr2btMxNxGnJe240vhYt.jpeg) 

No AA
![noaa|580x500](upload://yHB3NziFGoF6nP20zqUt1sS5gM.jpeg)

Edit: Alright, so I compiled the dx10 demo to test my results. And it seems identical to me. Note the output from urho is in linear space, while the rendered images from the demo are sRGB. Here's the comparisons:

Urho Edge Detect:
![edge|580x500](upload://yTvaTueip8rUIttsAEiYGD604aD.jpeg) 

Demo Edge Detect:
![dx10demoedges|580x500](upload://papTklj3QJncamFHpTF6lMtPea4.jpeg) 

Urho Weights (Gamma corrected):
![weightGammacorrected|580x500](upload://2miVKiJdhYDZVUZEWuqve1JebgH.jpeg) 

Demo Weights:
![dx10weight|580x500](upload://5wJlwf1VGtNizoxPd3LhnWcGMGj.jpeg)

-------------------------

Athos | 2019-10-05 13:24:19 UTC | #9

Yeah it's missing edges; it's like I'm not using any kind of AA.

-------------------------

PsychoCircuitry | 2019-10-06 14:30:14 UTC | #10

Strange, I guess I will build urho with dx11 then and see if I can pinpoint the issue. Guess I should have asked earlier but are you getting any errors on the shader compilation?

Edit: alright, I compiled a dx11 version and I can confirm that something is indeed off with that. The exact same setup I had working under dx9, looks very strange indeed. I'll look into it more and see what's going on.

Edit again: so I spent part of the afternoon rewriting the shader with some of urho's legacy defined functions for directx11 to try and match the way the sm3 implementation behaves, but this was unsuccessful. The results exhibited the same issues as running the actual shader. The edge detection has a lot more overlapping red and green segments, and doesn't detect some edges that the dx9 finds. So I'm not entirely sure what the issue is at this point. I'm not that familiar with dx11, most of my experience is with glsl and I just recently started experimenting with directx9. But it seems to me that urho isn't handling the texture.SampleLevel command the same way it handles tex2Dlod on dx9

Update 10/06/19
So I've done some testing with texture.Sample and texture.SampleLevel and those seem to be behaving correctly. So I guess that's not the culprit. I tried rewriting the shaders sampling macros to add an argument for SamplerState, bypassing the defined point and linear SamplerState. I was hoping that giving it the SamplerState for the texture being used would get closer to the DirectX9 results, but this was not the case. I'm really baffled because the sm3 version works right out of the box on dx9, and it appears that there's really not much difference between the sm3 and sm4 implementations other than updating the functions, but they are just api differences, the way it works should be exactly the same. I also tried adjusting the offsets in the vertex shader, but this didn't help the edge detection either.

10/06 part 2: I adapted the shader to use the opengl 3 implementation in an opengl build of urho. This works as expected. So either I'm not understanding something correctly in the dx11 side, or this is a bug of some kind with the dx11 renderer. So I guess to use this shader, you'll need to use either dx9 or opengl3, I can provide you with the shaders I adapted from your original post with either implementation if you'd like. Sorry I couldn't get it to work in dx11.

-------------------------

Athos | 2019-10-06 14:54:20 UTC | #11

No need to apologize, graphics is complicated. Thanks anyways.

-------------------------

PsychoCircuitry | 2019-10-07 13:10:51 UTC | #12

I'm still gonna see if I can get to the root of the issue. No guarantees, but I'll spend some time working on it.

Edit: started breaking it down step by step, starting with the edge detection. The first thing I've come across is that performing the dot product on 2 vectors yields different results between dx9 and dx11. I've simplified it to just reading the viewport texture and performing a dot product on the rgb channels at the screen position and a vector (0.5, 0.5, 0.5). The result is not a huge difference but noticeable, and the full edge detection algorithm has 7 dot product calculations I think, and I think all those inconsistencies stacking up results in an image that's quite a bit different than what's intended. And thats just the edge algorithm! Lol. The opengl version is identical to the dx9 version, so something is off with dx11. I updated the graphics drivers just to see, but that didn't improve anything.

Update 10/07/19: getting closer to understanding the issue. Dot product is working correctly, the reason for the discrepancies is due to the sampling position. If I flip all the offsets and reduce the first offset to a quarter pixel the results are much closer to the dx9/opengl results. Not quite right yet, but much, much closer. Not sure why all the offsets need to be flipped, but I'm assuming part of the issue is with the sampler state again. I'll keep digging into it and see what I come up with.

-------------------------

PsychoCircuitry | 2019-10-07 16:09:59 UTC | #13

My last couple posts were getting lengthy. So I hope it's ok that I'm making a new post.

I moved the offset calculation to the pixel shader and that fixed it! The coordinates still need flipped tho. I'll start debugging the weight blend next. If you're still interested in this, I'll post an updated shader when I'm done.

Edit: scratch what I said about flipping the cords. The provided coords work correctly when the calculation is done in the pixel shader. Running into a few problems still, but I think I will be able to get it working at some point. Tho I do believe there is some kind of bug with dx11 renderer that is the root of the problem. Still looking into it.

-------------------------

PsychoCircuitry | 2019-10-07 17:25:46 UTC | #14

Alright after all this craziness, turns out it was something very simple lol. Again, I'm not that familiar with dx11 so that could be why it wasn't obvious. But as I was running into issues with rendering during my tests of the adapted shader, there was a line from the original shader that started preventing me from rendering the scene. Anyway in the start of your pixel shader setup remove the line:
`float4 iPos : SV_POSITION`
Then it works properly.

-------------------------

Athos | 2019-10-07 17:27:57 UTC | #15

That was it, it's working now!
Thank you very much!

-------------------------

