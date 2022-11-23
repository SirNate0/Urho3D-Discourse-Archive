Bananaft | 2017-01-02 01:06:26 UTC | #1

Here is the list of things I did there:

-Real world terrain, using SRTM elevation data and Landsat 8 satellite imagery. Great thanks to Sinoid for awesome [url=http://discourse.urho3d.io/t/urho3-geomapping/994/12]16bit heightmap packer.[/url]
-Custom terrain shader. For now it uses one diffuse texture(40mb DXT5 5632x5632) and two normal maps packed into one RGBA texture.
-Hemisphere skylight instead of plain ambient color.
-Day-Night cycle.
-Screen-space exponential fog. I decided to use deferred shading, so I can render sky and fog in post-process. I was wondering if I can make a decent(not super realistic) atmospheric scattering with simple math, instead of logarithms. Not completly pleased with result, yet.
-Linear space lighting and gamma-correction.

[b]Download link[/b]:  [dropbox.com/s/6ufgsnrthkzb6 ... 082015.zip](https://www.dropbox.com/s/6ufgsnrthkzb6c0/zrv_13082015.zip)
Windows exe provided, but it's script(and shaders) only, so you can replace binary and run on any platform.
OpenGL only.

Controls:
WASD and mouse - fly aroud
Shift - fly faster
Mouse Wheel - change time of day
F - toggle fog
E - toggle auto-exposure
B - toggle bloom and gamma-correction

Work in progress. C&C are welcome.

[url=http://i.imgur.com/Qm9LaBX.jpg][img]http://i.imgur.com/Qm9LaBXm.jpg[/img][/url][url=http://i.imgur.com/mFRu2Il.jpg][img]http://i.imgur.com/mFRu2Ilm.jpg[/img][/url][url=http://i.imgur.com/4Ao0g5j.jpg][img]http://i.imgur.com/4Ao0g5jm.jpg[/img][/url][url=http://i.imgur.com/FebLDt2.jpg][img]http://i.imgur.com/FebLDt2m.jpg[/img][/url][url=http://i.imgur.com/6nhi3I5.jpg][img]http://i.imgur.com/6nhi3I5m.jpg[/img][/url][url=http://i.imgur.com/iDsRXS0.jpg][img]http://i.imgur.com/iDsRXS0m.jpg[/img][/url][url=http://i.imgur.com/NW80s4q.jpg][img]http://i.imgur.com/NW80s4qm.jpg[/img][/url][url=http://i.imgur.com/6eY7foR.jpg][img]http://i.imgur.com/6eY7foRm.jpg[/img][/url][url=http://i.imgur.com/ZNzVkGJ.png][img]http://i.imgur.com/ZNzVkGJm.jpg[/img][/url]

-------------------------

1vanK | 2017-01-02 01:06:26 UTC | #2

Amazing!

-------------------------

friesencr | 2017-01-02 01:06:26 UTC | #3

It has been nice seeing the play by play on twitter.  Very beautiful!  Did you have to do any terrain paging?

-------------------------

rasteron | 2017-01-02 01:06:26 UTC | #4

Looks great! will definitely try this out.

-------------------------

codingmonkey | 2017-01-02 01:06:27 UTC | #5

Nice Zarevo ! :slight_smile:

-------------------------

Bananaft | 2017-01-02 01:06:27 UTC | #6

Thank you all for feedback.

[quote="Sinoid"]Very cool.

On an Intel HD4000 there's something up with your light volumes (turned off bloom and gamma so it's more visually apparent): 
[/quote]
Oh, it actually runs on integrated video card, nice. How is FPS?
Looks like some GPUs have different solution to " pow(1-lightDist,2.6) " in Lighting.glsl. I should clamp this thing.

Edit: this should do it:
   [code]return max(dot(normal, lightDir) * pow(max(1-lightDist,0),2.6), 0.0);[/code]

[quote="friesencr"]It has been nice seeing the play by play on twitter.  Very beautiful!  Did you have to do any terrain paging?[/quote]
Let's we all use [url=https://twitter.com/search?q=Urho3d&src=typd]#Urho3d[/url] more often. No paging. Just one standard urho-terrain 3072x3072 with 128 patch size. Not going to do paging before I run out of memory :slight_smile:

-------------------------

cadaver | 2017-01-02 01:06:27 UTC | #7

When Present takes long, it's nothing unusual, it's just the gfx driver doing the actual rendering work there. Sometimes the driver buffer may also fill up earlier, during submitting draw calls, and in that case you could see the majority of time spent inside the frame rendering (actually inside the draw call which causes the buffer to fill and the work be actually performed)

-------------------------

theak472009 | 2017-01-02 01:06:27 UTC | #8

I am trying to port the Sky shader code to hlsl.
It works for the models but the sky does not show up (Black background even in day)
Also no lights show up.

Here is the hlsl shader code
[code]
#include "Uniforms.hlsl"
#include "Samplers.hlsl"
#include "Transform.hlsl"
#include "ScreenPos.hlsl"
#include "Lighting.hlsl"

#ifdef COMPILEPS
cbuffer CustomPS : register (b6)
{
  float3 cSkyColor;
  float3 cSunColor;
  float3 cSunDir;
  float cFogDist;
  float cCamHeight;
}
#endif

void VS(
        float4 iPos : POSITION,
        out float2 oScreenPos : TEXCOORD0,
        out float3 oFarRay : TEXCOORD1,
        out float4 oPos : OUTPOSITION)
{
    float4x3 modelMatrix = iModelMatrix;
    float3 worldPos = GetWorldPos(modelMatrix);
    oPos = GetClipPos(worldPos);

    oScreenPos = GetScreenPosPreDiv(oPos);
    oFarRay = GetFarRay(oPos);
}


void PS(
        float2 iScreenPos : TEXCOORD0,
        float3 iFarRay : TeXCOORD1,
        out float4 oColor : OUTCOLOR0)
{
// oColor = float4 (1.0, 1.0, 1.0, 1.0);
    // If rendering a directional light quad, optimize out the w divide

    #ifdef HWDEPTH
        float depth = ReconstructDepth(Sample2D (DepthBuffer, iScreenPos).r);
    #else
        float depth = DecodeDepth(Sample2D (DepthBuffer, iScreenPos).rgb);
    #endif

    float3 worldPos = iFarRay * depth;

    float4 diffuseInput = Sample2D (DiffMap, iScreenPos);


    float4 projWorldPos = float4 (worldPos, 1.0);

    float depth2 = 1 - clamp (length(worldPos) / cFogDist, 0.0, 1.0);
    float height = (worldPos.y + cCamHeight) * 0.01;

    float fogFactor =  clamp (exp (-height * depth2 + 0.7) * (1 - exp (depth2 * 2 - 2)), 0, 1);
    float diffFactor = 1 - fogFactor;//(1-exp(-height*depth2)) * (exp(depth2*3-3));
    //float skyfactor = (exp((1-depth2)*10-10));

    //float skydiff = 0.5 * (normal.y + 1.0);
    float3 DirRay = normalize (iFarRay);
  //  float layer = min(pow((1-abs(DirRay.y)),3.5),1);//*2*(1-diffFactor)-2*(1-diffFactor)
    //float layer = pow(1-DirRay.y, 1-cCamHeight);
    float layer = clamp (exp (((1 - DirRay.y) - 1) * (0.5 + cCamHeight * 0.001)), 0, 1);
    float sunDot = max (dot (DirRay, -1 * cSunDir), 0);
    float sunAmount = pow (exp ((sunDot - 1) * 5), 1 + (1 - layer) * 60); //exp(sunDot*20*(1-layer)-20*(1-layer)); //pow (sunDot, 1 + (1-layer) * 6);// * (1-diffFactor);//max (dot(DirRay ,-1 * cSunDir ),0);

    //sunAmount *= 1+layer*2;
    //

    float3 fogColor = 1.0 * cSkyColor * layer + cSunColor * sunAmount; //mix( cSkyColor,cSunColor, sunAmount );// pow(sunAmount,8.0)

    float3 result = diffuseInput.rgb * diffFactor + fogColor * fogFactor; //diffuseInput.rgb * (1-0.95*diffFactor) + fogcolor * fogFactor;

    //result = pow( result ,float3( 1/2.2 ) );

    oColor = float4 (result, 0.0);
    // float camHeight = (500.0 - cCamHeight) / 500.0; // For testing if the cbuffer input is working
    // oColor = float4 (camHeight, camHeight, camHeight, 1.0);
    // oColor = float4 (fogcolor, 0.0); // FogColor is computed correctly
    // oColor = float4 (depth2, depth2, depth2, 1.0);
}
[/code]

Here is a screenshot for reference:
[drive.google.com/file/d/0Bxa7g0 ... sp=sharing](https://drive.google.com/file/d/0Bxa7g0oZu4tEaGRKempONTJfX3c/view?usp=sharing)

Note: The terrain in the image is using default terrain shader provided by Urho3D.
It might be a silly mistake somewhere due to my limited knowledge in hlsl (maybe depth in range [0,1] instead of [-1,1]?). Please help.

-------------------------

Bananaft | 2017-01-02 01:06:27 UTC | #9

[quote="cadaver"]When Present takes long, it's nothing unusual, it's just the gfx driver doing the actual rendering work there. [/quote]
[img]http://i.imgur.com/626KZAe.gif[/img][img]http://i.imgur.com/RNiaSX3.gif[/img] [b]CONGRATULATIONS!! THIS IS YOUR 1000th POST!!![/b] [img]http://i.imgur.com/RNiaSX3.gif[/img][img]http://i.imgur.com/626KZAe.gif[/img]

[quote="theak472009"]I am trying to port the Sky shader code to hlsl.
It works for the models but the sky does not show up (Black background even in day)
Also no lights show up.
[/quote]

Hello and welcome to the forum!

I'm really glad you got interested in my shaders, but taking them into your project probably not the best idea because:

1) My code is ugly hacky uncommented mess.
2) I work only in DeferredHWDepth mode and never tested it in any other.
3) Sky-pass requires several parameters to be set by script or code in each frame: sky and sun colors and camera height(because I don't know a better way to get pixel's global world height).

Anyway, here is a couple links, that could help you:
Differences between Direct3D and OpenGL in Urho documentation:
[urho3d.github.io/documentation/1 ... ences.html](http://urho3d.github.io/documentation/1.4/_a_p_i_differences.html)

Tutorial, I've started with:
[iquilezles.org/www/articles/fog/fog.htm](http://www.iquilezles.org/www/articles/fog/fog.htm)

[quote="Sinoid"]None of the post processing has any meaningful impact on that.[/quote]

Whoa, really? I would expect at least Bloom to affect fps, on my machine it eats more than rest of the render.

Does looking upwards, affects fps?

-------------------------

