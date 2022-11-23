codingmonkey | 2017-01-02 01:08:24 UTC | #1

[b]EDIT[/b]: latest version of SP you may found at this link (currently GL and DX11 only): [github.com/1vanK/Urho3DSoftParticles](https://github.com/1vanK/Urho3DSoftParticles)


Hi, today I try to read depth texture. 
In same time it using as depth buffer for testing and reading Z in alpha pass.

file: ForwardHWDepth.xml

<renderpath>
    <rendertarget name="depth" sizedivisor="1 1" format="readabledepth" />
...
    <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" depthstencil="depth" >
        <texture unit="depth" name="depth" />
    </command>
...
</renderpath>

Is it possible use depth in same time for testing samples and reading?

maybe need use additional depth RT (r16) and populate it in all scene passes? and only then put it to TU for reading?

-------------------------

Bananaft | 2017-01-02 01:08:24 UTC | #2

So, is it not working?

Aren't light volumes pass does it, in DefferedHWDepth and PrepassHWDepth?

-------------------------

codingmonkey | 2017-01-02 01:08:24 UTC | #3

Oh, sorry my mistake.
I just do some test with reading from Z and suppose what I got wrong results in readed from Zbuffer.  
I thought it was a mistake usage of depth buffer in same time for read and testing.

and other questions: 
1. did you trying to reproject Z sample from depth buffer from (NDC space) to (ViewProj space before div by w) xyz/w value ?

float hwDepth = texture2D(sDepthBuffer, vTexCoord).r; // Read Depth value
float rDepth = ReconstructDepth(hwDepth); // Reconstruct 0..1
What next step?


2.  The value that will be written to DepthBuffer from VS shader:
gl_Position = GetClipPos(worldPos);
Is it this - gl_Position.z / gl_Position.w ?

3. vWorldPos = vec4(worldPos, GetDepth(gl_Position));
What thing stored into last component (w) ?

-------------------------

codingmonkey | 2017-03-28 16:43:16 UTC | #4

https://youtu.be/CHAKG73Sqcs

Hi  again, I have a some process there, but i stuck in place with comparing sceneZ and particleZ.
As you see on this vedeo if i change a position of camera (rotate around) there is bug, particles are disappears.
I guessing this is because I have some problems with math difference between background sceneZ value and particleZ value.
and I do not actually know what of this reprojecties are wrong in my shader.

I have a this algorithm:

RenderPath
```
    <!-- Render SoftParticles --> 
    <command type="scenepass" pass="softparticles" vertexlights="true" sort="backtofront" metadata="alpha" blend="replace" output="viewport">
        <texture unit="depth" name="depth" />
    </command>
```

Technique for particles
DiffVColUnlitAlphaSP.xml
```
<technique vs="UnlitSP" ps="UnlitSP" vsdefines="VERTEXCOLOR SP" psdefines="DIFFMAP VERTEXCOLOR SP">
    <pass name="softparticles" depthtest="always" depthwrite="false" blend="alpha" />
</technique
```

and shader UnlitSP.glsl
[spoiler]
http://pastebin.com/2MCWLkKq
[/spoiler]

I suppose what I do wrong converting sceneZ into ViewProj space or particleZ into ViewProj space. (mb need get ViewProjInvert matrix from camera to project  with sceneZ * ViewProjInvert)
Is any body have some ideas how to solve rotation bug ?

-------------------------

1vanK | 2017-01-02 01:08:25 UTC | #5

i create material 

[code]<material>
    <technique name="Techniques/DiffVColUnlitAlphaSP.xml" />
    <texture unit="diffuse" name="Urho2D/Ball.png" />
</material>
[/code]

and it is fully transparent

p.s. Where did the variable cProj in shader?

-------------------------

codingmonkey | 2017-01-02 01:08:25 UTC | #6

>and it is fully transparent
I use for testing tweaked smoke.xml

>p.s. Where did the variable cProj in shader?
actually I add this matrixes and pass they in:

[code]void View::SetCameraShaderParameters(Camera* camera, bool setProjection)
{
        graphics_->SetShaderParameter(VSP_VIEWPROJ, projection * camera->GetView());
        graphics_->SetShaderParameter(VSP_VIEW, Matrix4::IDENTITY * camera->GetView());
        graphics_->SetShaderParameter(VSP_PROJ, projection);
}[/code]

also you need after what fix uniforms.glsl to set visible this uniforms for PS shader

[code]
// OpenGL 2 uniforms (no constant buffers)

uniform mat4 cViewProj;
uniform mat4 cProj;

#ifdef COMPILEVS
...
[/code]

-------------------------

1vanK | 2017-01-02 01:08:27 UTC | #7

I found a solution (and modification of the engine is not required)

CoreData\RenderPaths\ForwardHWDepth_SoftParticles.xml (based on ForwardHWDepth)
[code]
<renderpath>
    <rendertarget name="depth" sizedivisor="1 1" format="readabledepth" />
    <command type="clear" depth="1.0" output="depth" />
    <command type="scenepass" pass="shadow" output="depth" />
    <command type="clear" color="fog" depthstencil="depth" />
    <command type="scenepass" pass="base" vertexlights="true" metadata="base" depthstencil="depth" />
    <command type="forwardlights" pass="light" depthstencil="depth" />
    <command type="scenepass" pass="postopaque" depthstencil="depth" />
    <command type="scenepass" pass="refract" depthstencil="depth">
        <texture unit="environment" name="viewport" />
    </command>
    <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" depthstencil="depth"  />
    <command type="scenepass" pass="postalpha" sort="backtofront" depthstencil="depth" />
    <!-- Render SoftParticles -->
    <command type="scenepass" pass="softparticles" vertexlights="true" sort="backtofront" metadata="alpha" blend="replace" output="viewport">
        <texture unit="depth" name="depth" />
    </command>
</renderpath>
[/code]

CoreData\Shaders\GLSL\UnlitSP.glsl (based on unlit)
[code]
#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"
#include "ScreenPos.glsl"
#include "Fog.glsl"

varying vec2 vTexCoord;
varying vec4 vWorldPos;
varying vec4 vScreenPos;
#ifdef VERTEXCOLOR
    varying vec4 vColor;
#endif

void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
    gl_Position = GetClipPos(worldPos);
    vTexCoord = GetTexCoord(iTexCoord);
    vWorldPos = vec4(worldPos, GetDepth(gl_Position));
    vScreenPos = GetScreenPos(gl_Position);

    #ifdef VERTEXCOLOR
        vColor = iColor;
    #endif
}

void PS()
{
    // Get material diffuse albedo
    #ifdef DIFFMAP
        vec4 diffColor = cMatDiffColor * texture2D(sDiffMap, vTexCoord);
        #ifdef ALPHAMASK
            if (diffColor.a < 0.5)
                discard;
        #endif
    #else
        vec4 diffColor = cMatDiffColor;
    #endif

    #ifdef VERTEXCOLOR
        diffColor *= vColor;
    #endif

    // Get fog factor
    #ifdef HEIGHTFOG
        float fogFactor = GetHeightFogFactor(vWorldPos.w, vWorldPos.y);
    #else
        float fogFactor = GetFogFactor(vWorldPos.w);
    #endif

    #if defined(PREPASS)
        // Fill light pre-pass G-Buffer
        gl_FragData[0] = vec4(0.5, 0.5, 0.5, 1.0);
        gl_FragData[1] = vec4(EncodeDepth(vWorldPos.w), 0.0);
    #elif defined(DEFERRED)
        gl_FragData[0] = vec4(GetFog(diffColor.rgb, fogFactor), diffColor.a);
        gl_FragData[1] = vec4(0.0, 0.0, 0.0, 0.0);
        gl_FragData[2] = vec4(0.5, 0.5, 0.5, 1.0);
        gl_FragData[3] = vec4(EncodeDepth(vWorldPos.w), 0.0);
    #else

        float particleDepth = vWorldPos.w;
        float solidGeometrydepth = ReconstructDepth(texture2DProj(sDepthBuffer, vScreenPos).r); // use ReconstructDepth when HWDEPTH
    
        if (solidGeometrydepth <= particleDepth)
        {
            float deltaDepth = (particleDepth - solidGeometrydepth) * 1000;
            diffColor.a -= deltaDepth;
        }
    
        gl_FragColor = vec4(GetFog(diffColor.rgb, fogFactor), diffColor.a);
    
    #endif
}
[/code]

CoreData\Techniques\DiffVColUnlitAlphaSP.xml (based on DiffVColUnlitAlpha)
[code]
<technique vs="UnlitSP" ps="UnlitSP" vsdefines="VERTEXCOLOR SP" psdefines="DIFFMAP VERTEXCOLOR SP">
    <pass name="softparticles" depthtest="always" depthwrite="false" blend="alpha" />
</technique>
[/code]

Data\Materials\SmokeSoftParticle.xml (based on Smoke)
[code]
<material>
    <technique name="Techniques/DiffVColUnlitAlphaSP.xml" />
    <texture unit="diffuse" name="Textures/Smoke.dds" />
</material>
[/code]

Data\Particle\SmokeStackSoftParticle.xml (based on Smoke)
[code]
<?xml version="1.0"?>
<particleeffect>
	<material name="Materials/SmokeSoftParticle.xml" />
	<numparticles value="1000" />
	<updateinvisible enable="true" />
	<relative enable="false" />
	<scaled enable="true" />
	<sorted enable="true" />
	<animlodbias value="0" />
	<emittertype value="Box" />
	<emittersize value="1 1 1" />
	<direction min="-0.15 1 -0.15" max="0.15 1 0.15" />
	<constantforce value="0 2 0" />
	<dampingforce value="2" />
	<activetime value="0" />
	<inactivetime value="0" />
	<emissionrate min="100" max="200" />
	<particlesize min="0.1 0.2" max="0.6 0.7" />
	<timetolive min="4" max="4" />
	<velocity min="0.5" max="3" />
	<rotation min="0" max="0" />
	<rotationspeed min="60" max="60" />
	<sizedelta add="0" mul="1.3" />
	<colorfade color="1 1 1 0" time="0" />
	<colorfade color="0.69 0.33 0.2 0.5" time="0.64" />
	<colorfade color="0 0 0 0" time="1.98" />
	<colorfade color="0 0 0 0" time="4" />
</particleeffect>
[/code]

Old:
[url=http://savepic.su/6730046.htm][img]http://savepic.su/6730046m.png[/img][/url]

New:
[url=http://savepic.su/6718782.htm][img]http://savepic.su/6718782m.png[/img][/url]

-------------------------

1vanK | 2017-01-02 01:08:27 UTC | #8

Here is possible make some improvements:
send to shader a coefficient (replacing 1000) from material in the case of large sprites (Like explosions)

-------------------------

codingmonkey | 2017-01-02 01:08:27 UTC | #9

Wow, great job.
Did you tried to  create some solid blocs around smoke to test overlaying effect?
I also find this different functions:
[code]    
//vec2 vScreenPos = GetScreenPosPreDiv(gl_Position);
    vec4 vScreenPos = GetScreenPos(gl_Position);[/code]

in what case we may use each of them ? I do not understand.

>float sceneZ = texture2DProj(sDepthBuffer, vScreenPos).r;   // read depthstencil texture(readabledepth)
the using texture2DProj is providing from previous operation step because size of  vScreenPos is vec4 and not vec2, or there is another reason? ( why we use texture projection? and no simple texture2D )

there is magic number I guess 1000 ? If we change this block of code to NV's code from whitepaper is still will be working properly?
[code]        if (solidGeometrydepth <= particleDepth)
        {
            float deltaDepth = (particleDepth - solidGeometrydepth) * 1000;
            diffColor.a -= deltaDepth;
        }
[/code]
to
 [code]           float scale = 1.0;
            float diffZ = (particleDepth - solidGeometrydepth) 
            
            float input = clamp(diffZ, 0.0, 1.0);
            float contrastPower = 1.0;
            float output = 0.5 * pow(clamp(2*((input > 0.5) ? 1 - input : input), 0.0, 1.0), contrastPower);
            float weight = (input > 0.5) ? 1 - output : output; 
            
            diffColor.a *= weight;
[/code]

I mean in using NV's tech we got two controls values what very handy: the control of contrast and scale.

-------------------------

1vanK | 2017-01-02 01:08:27 UTC | #10

> in what case we may use each of them ? I do not understand.
> the using texture2DProj is providing from previous operation step because size of vScreenPos is vec4 and not vec2, or there is another reason?

i just copy random code from PrepassLight.glss xD

> there is magic number I guess 1000 ? If we change this block of code to NV's code from whitepaper is still will be working properly?

I did not study the documentation in detail. The higher the number, the greater the depth difference will affect the transparency (most of the hidden part of sprite will be visible).

-------------------------

codingmonkey | 2017-01-02 01:08:27 UTC | #11

I'm tesing you shader and "overlaying" is not presented I guess it work fine for now.

>i just copy random code from PrepassLight.glss xD
i am always wanted to write shaders in this manner, and in same time i wanted to they should work as I expect xD

>I did not study the documentation in detail.
There is no documentation about shaders using ) 
For example what differences between: this -> GetScreenPosPreDiv() and this -> GetScreenPos() and many other things...

Anyway I think you may try to create pull request with your SoftParticles. 
In future we can polish they )

-------------------------

1vanK | 2017-01-02 01:08:27 UTC | #12

[quote="codingmonkey"]
Anyway I think you may try to create pull request with your SoftParticles. 
In future we can polish they )[/quote]

It will not work in all RenderPaths. I do not think it will take to master. Just rename this post to "Soft Particles" and and anyone can take shader here.

-------------------------

codingmonkey | 2017-01-02 01:08:27 UTC | #13

Ok, but may be you create small repo for store all stuff in one place also for fixes and updating ?
- also need add hlsl shader for SoftParticles

-------------------------

1vanK | 2017-01-02 01:08:27 UTC | #14

[quote="codingmonkey"]Ok, but may be you create small repo for store all stuff in one place also for fixes and updating ?
- also need add hlsl shader for SoftParticles[/quote]

no problems :)

EDIT: [github.com/1vanK/Urho3DSoftParticles](https://github.com/1vanK/Urho3DSoftParticles)

-------------------------

codingmonkey | 2017-01-02 01:08:27 UTC | #15

>https://github.com/1vanK/Urho3DSoftParticles

cool, but I found what it no working in ortho projection (when you press key 5 on numpad)

-------------------------

1vanK | 2017-01-02 01:08:27 UTC | #16

[quote="codingmonkey"]
cool, but I found what it no working in ortho projection (when you press key 5 on numpad)[/quote]


[url=http://savepic.su/6700395.htm][img]http://savepic.su/6700395m.png[/img][/url]

-------------------------

codingmonkey | 2017-01-02 01:08:27 UTC | #17

Oh, sorry I understood, I'm use not your original shader )
anyway I found there this 1000 value are lay (Editor settings camera far clip) - this is camera far value. 
In PS shader this is cFarClipPS uniform 
I guessing the scale may be calc with this way:
float scale = cFarClipPS - cNearClipPS;

-------------------------

szamq | 2017-01-02 01:08:27 UTC | #18

Nice, would be that also possible on the deffered render path?

-------------------------

codingmonkey | 2017-01-02 01:08:27 UTC | #19

>would be that also possible on the deffered render path?
Yes it possible, few lines to add in deffered

DeferredHWDepthSP.xml (in simple Deferred.xml we do not have possibility to read depth. That's why this working only with %name%HWDepth )
[code]
<renderpath>
    <rendertarget name="albedo" sizedivisor="1 1" format="rgba" />
    <rendertarget name="normal" sizedivisor="1 1" format="rgba" />
    <rendertarget name="depth" sizedivisor="1 1" format="readabledepth" />
    <command type="clear" color="fog" depth="1.0" stencil="0" depthstencil="depth" />
    <command type="clear" color="0 0 0 0" output="albedo" depthstencil="depth" />
    <command type="scenepass" pass="deferred" marktostencil="true" vertexlights="true" metadata="gbuffer" depthstencil="depth">
        <output index="0" name="viewport" />
        <output index="1" name="albedo" />
        <output index="2" name="normal" />
    </command>
    <command type="lightvolumes" vs="DeferredLight" ps="DeferredLight" psdefines="HWDEPTH" depthstencil="depth">
        <texture unit="albedo" name="albedo" />
        <texture unit="normal" name="normal" />
        <texture unit="depth" name="depth" />
    </command>
    <command type="scenepass" pass="postopaque" depthstencil="depth" />
    <command type="scenepass" pass="refract" depthstencil="depth">
        <texture unit="environment" name="viewport" />
    </command>
    <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" depthstencil="depth" />
    
    <command type="scenepass" pass="softparticles" vertexlights="true" sort="backtofront" metadata="alpha" blend="replace" output="viewport">
        <texture unit="depth" name="depth" />
    </command>
    
    <command type="scenepass" pass="postalpha" sort="backtofront" depthstencil="depth" />
</renderpath>
[/code]

and move soft particle calculations in shader little upper

UnlitSP.glsl
[code]
#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"
#include "ScreenPos.glsl"
#include "Fog.glsl"

varying vec2 vTexCoord;
varying vec4 vWorldPos;
varying vec4 vScreenPos;
#ifdef VERTEXCOLOR
    varying vec4 vColor;
#endif

void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
    gl_Position = GetClipPos(worldPos);
    vTexCoord = GetTexCoord(iTexCoord);
    vWorldPos = vec4(worldPos, GetDepth(gl_Position));
    vScreenPos = GetScreenPos(gl_Position);
    //vScreenPos = GetScreenPosPreDiv(gl_Position);

    #ifdef VERTEXCOLOR
        vColor = iColor;
    #endif
}

void PS()
{
    // Get material diffuse albedo
    #ifdef DIFFMAP
        vec4 diffColor = cMatDiffColor * texture2D(sDiffMap, vTexCoord);
        #ifdef ALPHAMASK
            if (diffColor.a < 0.5)
                discard;
        #endif
    #else
        vec4 diffColor = cMatDiffColor;
    #endif

    #ifdef VERTEXCOLOR
        diffColor *= vColor;
    #endif

    // Get fog factor
    #ifdef HEIGHTFOG
        float fogFactor = GetHeightFogFactor(vWorldPos.w, vWorldPos.y);
    #else
        float fogFactor = GetFogFactor(vWorldPos.w);
    #endif
    
    float particleDepth = vWorldPos.w;
    float solidGeometrydepth = ReconstructDepth(texture2DProj(sDepthBuffer, vScreenPos).r); // use ReconstructDepth when HWDEPTH
        
    if (solidGeometrydepth < particleDepth)
    {
        float scale = cFarClipPS - cNearClipPS;
        float deltaDepth = (particleDepth - solidGeometrydepth) * scale;    
         
        diffColor.a -= deltaDepth;
    }
    
    #if defined(PREPASS)
        // Fill light pre-pass G-Buffer
        gl_FragData[0] = vec4(0.5, 0.5, 0.5, 1.0);
        gl_FragData[1] = vec4(EncodeDepth(vWorldPos.w), 0.0);
    #elif defined(DEFERRED)
        gl_FragData[0] = vec4(GetFog(diffColor.rgb, fogFactor), diffColor.a);
        gl_FragData[1] = vec4(0.0, 0.0, 0.0, 0.0);
        gl_FragData[2] = vec4(0.5, 0.5, 0.5, 1.0);
        gl_FragData[3] = vec4(EncodeDepth(vWorldPos.w), 0.0);
    #else    
        gl_FragColor = vec4(GetFog(diffColor.rgb, fogFactor), diffColor.a);
    #endif
}
[/code]

-------------------------

franck22000 | 2017-01-02 01:08:46 UTC | #20

Anyone is planning to make a pull request in master branch to add this ? I think it's a must have feature for a modern engine :slight_smile:

-------------------------

1vanK | 2017-01-02 01:08:46 UTC | #21

[quote="franck22000"]Anyone is planning to make a pull request in master branch to add this ? I think it's a must have feature for a modern engine :)[/quote]

We had a big discussion with CodingMonkey and came to the conclusion that still need to do much

[github.com/1vanK/Urho3DSoftParticles/pull/3](https://github.com/1vanK/Urho3DSoftParticles/pull/3) (sorry, the Russian language)

-------------------------

codingmonkey | 2017-01-02 01:08:46 UTC | #22

Yes,  [b]1vanK[/b] is right, there is still needed to do some polishing.
But you also can use it now, just copy shaders and technics.

-------------------------

