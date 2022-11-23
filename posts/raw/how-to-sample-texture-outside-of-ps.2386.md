godan | 2017-01-02 01:15:07 UTC | #1

I'm having a lot of fun porting some Shadertoy shaders to Urho. However, one thing that I run in to quite a bit is that a shader from Shadertoy might have some code like this:

[code]
float pn(in vec3 x) {
    vec3 p = floor(x), f = fract(x);
	f *= f*(3.-f-f);
	vec2 uv = (p.xy+vec2(37.,17.)*p.z) + f.xy,
	     rg = texture2D( iChannel0, (uv+.5)/256., -100.).yx;
	return 2.4*mix(rg.x, rg.y, f.z)-1.;
}[/code]

This is a helper function that computes some kind of noise. It sits outside of either VS() or PS(), to put it into Urho terms. The issue is here:

[code]
rg = texture2D( iChannel0,....)
[/code]

Where the code samples the texture called "iChannel0". Now, my understanding is that in Urho, we only have access to certain Uniforms (i.e. vTexCoord, cElapsedTimePS,etc). In particular, we can only access textures that are held in the sampler uniforms, i.e. cDiffMap, cNormalMap, etc.

So, sampling cDiffMap from insider PS() certainly works. However, my question is: how can I sample the texture from outside PS() or VS() like in the code above?

-------------------------

Eugene | 2017-01-02 01:15:07 UTC | #2

What error do you have if you place the same code outside PS(), but in the COMPILEPS define scope?

-------------------------

godan | 2017-01-02 01:15:07 UTC | #3

So, here is a simplified version of the shader with the COMPILEPS def:
[code]
// Created by inigo quilez - iq/2013
// License Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.

// Volumetric clouds. It performs level of detail (LOD) for faster rendering

#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"
#include "ScreenPos.glsl"
#include "PostProcess.glsl"

varying vec2 vTexCoord;
varying vec2 vScreenPos;

float time = 10.0;

#ifdef COMPILEPS

float noise( in vec3 x )
{
    vec3 p = floor(x);
    vec3 f = fract(x);
    f = f*f*(3.0-2.0*f);
    vec2 uv = (p.xy+vec2(37.0,17.0)*p.z) + f.xy;
    vec2 rg = texture2D( cDiffMap, (uv+ 0.5)/256.0, -100.0 ).yx;
    return -1.0+2.0*mix( rg.x, rg.y, f.z );
}

#endif

void VS()
{

}

void PS()
{
    float n = noise(vec3(0.5, 0.5, 0.5));
    gl_FragColor = vec4(n,n,n,n);
}
[/code]

and here is the RenderPath:

[code]
<renderpath>
    <command type="quad" tag="Clouds" vs="CloudsTest" ps="CloudsTest" psdefines="COMPILEPS" output="viewport">
        <texture unit="diffuse" name="Textures/noise.bmp" />
    </command>
</renderpath>
[/code]

In this configuration, I get an error that says: "Undefined variable cDiffMap". Am I'm putting the #define COMPILEPS in the right spot?

-------------------------

1vanK | 2017-01-02 01:15:07 UTC | #4

sDiffMap - sampler (not cDiffMap - constant)

-------------------------

godan | 2017-01-02 01:15:07 UTC | #5

Oh man...feeling sheeeepish. Totally works though:

[img]http://iogram.ca/wp-content/uploads/2016/11/demo_nebula.gif[/img]

-------------------------

