hdunderscore | 2017-01-02 01:12:01 UTC | #1

I'm trying to get this SSAO shader into urho: [john-chapman-graphics.blogspot.c ... orial.html](http://john-chapman-graphics.blogspot.com.au/2013/01/ssao-tutorial.html)

It seems simple enough, find position in view space, make new points around that point in viewspace, convert to screen space to grab a depth sample for comparison. But I can't seem to convert from viewspace (or world space) to screenspace in the pixel shader. Here is a simple example, although I did try a few other things already:
[code]#include "Uniforms.hlsl"
#include "Samplers.hlsl"
#include "Transform.hlsl"
#include "ScreenPos.hlsl"
#include "Lighting.hlsl"
#line 7

void VS(float4 iPos : POSITION,
    out float4 oScreenPos : TEXCOORD0,
    out float3 oFarRay : TEXCOORD1,
    #ifdef ORTHO
        out float3 oNearRay : TEXCOORD2,
    #endif
    out float4 oGBufferOffsets : TEXCOORD3,
    out float4x4 oViewProj : TEXCOORD4,
    out float4 oPos : OUTPOSITION)
{
    float4x3 modelMatrix = iModelMatrix;
    float3 worldPos = GetWorldPos(modelMatrix);
    oPos = GetClipPos(worldPos);
    oScreenPos = GetScreenPos(oPos);
    oFarRay = GetFarRay(oPos) * oPos.w;
    oViewProj = cViewProj;
    oGBufferOffsets = cGBufferOffsets;
    #ifdef ORTHO
        oNearRay = GetNearRay(oPos) * oPos.w;
    #endif
}

void PS(
    float4 iScreenPos : TEXCOORD0,
    float3 iFarRay : TEXCOORD1,
    #ifdef ORTHO
        float3 iNearRay : TEXCOORD2,
    #endif
    float4 iGBufferOffsets : TEXCOORD3,
    float4x4 iViewProj : TEXCOORD4,
    out float4 oColor : OUTCOLOR0)
{
    float depth = Sample2D(DepthBuffer, iScreenPos).r;
    #ifdef HWDEPTH
        depth = ReconstructDepth(depth);
    #endif
    #ifdef ORTHO
        float3 worldPos = lerp(iNearRay, iFarRay, depth) / iScreenPos.w;
    #else
        float3 worldPos = iFarRay * depth / iScreenPos.w;
    #endif

    float3 somePosition = worldPos.xyz;

    float4 cPos = mul(float4(somePosition, 1.0), iViewProj);

    float4 sPos =  float4(
        cPos.x * iGBufferOffsets.z + iGBufferOffsets.x * cPos.w,
        -cPos.y * iGBufferOffsets.w + iGBufferOffsets.y * cPos.w,
        0.0,
        cPos.w);

    oColor = float4(sPos.xy, 0.0, 1.0);
    // Trying to get:
    //oColor = float4(iScreenPos.xy, 0.0, 1.0);
}
[/code]

Seems like the 'worldPos' in this example is really viewPos ?

Thanks

-------------------------

cadaver | 2017-01-02 01:12:01 UTC | #2

The deferred shaders (or anything else that uses the camera near/far rays calculated in vertex shader) work in a "camera-centered world space" meaning you must add the camera position to get world space. Light world positions are adjusted accordingly in the batch preparation. This is rather confusing to get a negligible performance gain (one addition in PS) and since we don't support pixel shader 2.0 anymore the instruction count shouldn't be an issue, so I'd say it should be changed to true world space.

-------------------------

hdunderscore | 2017-01-02 01:12:01 UTC | #3

Am I mistaken to use the cViewProj matrix to try convert from world space to clip space? Am I maybe passing it along to the pixel shader incorrectly ? I get an error if I try to pass two matrices, or anything after a matrix. I feel like cViewProj is a unit matrix when I try to use it in the pixel shader.

-------------------------

cadaver | 2017-01-02 01:12:01 UTC | #4

I believe I've never passed matrices in interpolators, so can't outright comment what is the right approach for that. cViewProj should be appropriate for world->clip conversion though. If you foresee it's useful elsewhere you could also make it an actual pixel shader uniform (again, we're no longer PS2.0, so it's acceptable)

-------------------------

hdunderscore | 2017-01-02 01:12:01 UTC | #5

Thanks for the help ! I have exposed a cViewProjPS and have made progress on this.

-------------------------

