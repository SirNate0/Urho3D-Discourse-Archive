GIMB4L | 2017-01-02 00:58:25 UTC | #1

So I have a fullscreen effect I want to happen on two separate viewports. I've noticed the viewport I've passed in is the entire backbuffer, not the individual viewport itself. How do I get an individual viewport to sample from? Also, how do I change the texture clamp settings on a buffer I'm sampling from if it's the buffer the scene was rendered on?

-------------------------

cadaver | 2017-01-02 00:58:25 UTC | #2

Currently there's no way for either (without modifying the rendering + shader code, of course). The original reason why it works like that is to avoid allocating separate G-buffer textures for multiple viewports, and to have the quad shaders and viewport sampling work similarly in both deferred rendering and post processing.

-------------------------

GIMB4L | 2017-01-02 00:58:25 UTC | #3

Okay, so if I'm rendering in two viewports how can I do a fullscreen effect on the entire screen?

-------------------------

cadaver | 2017-01-02 00:58:25 UTC | #4

You can't do that either with unmodified rendering code.

What you can do is apply the effect to each of the viewports in turn, after rendering, by referencing the effect in both of the viewports' renderpaths. See the existing shaders, such as EdgeFilter or GreyScale for the simplest examples, how they get the UV coordinates for sampling the viewport texture.

Note that I've written an issue for changing this mechanism, as it should improve GPU efficiency to not be blitting the whole screen unnecessarily, but just the viewport part.

-------------------------

GIMB4L | 2017-01-02 00:58:25 UTC | #5

Yeah, that's what I'm doing. I think I can fix it if I only sample from 0-0.5 on the left viewport and 0.5-1 on the right.

-------------------------

cadaver | 2017-01-02 00:58:26 UTC | #6

Code like this should get you the proper UV's automatically: (this is the GreyScale example shader)

[code]
void VS(float4 iPos : POSITION,
    out float4 oPos : POSITION,
    out float2 oScreenPos : TEXCOORD0)
{
    float4x3 modelMatrix = iModelMatrix;
    float3 worldPos = GetWorldPos(modelMatrix);
    oPos = GetClipPos(worldPos);
    oScreenPos = GetScreenPosPreDiv(oPos);
}

void PS(float2 iScreenPos : TEXCOORD0,
    out float4 oColor : COLOR0)
{
    float3 rgb = tex2D(sDiffMap, iScreenPos).rgb;
    float intensity = GetIntensity(rgb);
    oColor = float4(intensity, intensity, intensity, 1.0);
}
[/code]

-------------------------

GIMB4L | 2017-01-02 00:58:26 UTC | #7

I'll give it a try. To be honest I'm trying to get the shaders for the Oculus Rift working, and it depends heavily on viewports and post-processing effects.

-------------------------

