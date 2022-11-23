vivienneanthony | 2017-01-02 01:02:19 UTC | #1

Hello

Is it possible to use a HDR image for a skybox like directly?

Or a sphere with a transparent layer and clouds?

[img]http://1.bp.blogspot.com/-BdLgsEStyEg/UpvLjiUB9wI/AAAAAAAABME/exk76XcUYqQ/s1600/sky+18_littile.jpg[/img]

Vivienne

-------------------------

hdunderscore | 2017-01-02 01:02:19 UTC | #2

I don't believe Urho supports any image formats with hdr?

The way that I've gone about it is encoding the hdr information into the texture using an encoding:

Here is a fork of cmft with the ability to export dds with 'bgrd8', 'bgrm8' and 'bgre8' encodings:
[github.com/hdunderscore/cmft/tree/hdr](https://github.com/hdunderscore/cmft/tree/hdr)

Here is the hlsl shader code to decode them:
[code]float4 DecodeBGRM8(in float4 rgbm)
{
    float4 r;
    const float MaxRange = 20.0f;
    const float MaxValue = 255.0f * MaxRange;
    const float scale = 1.0f / log2(MaxValue);
    float M = exp2(rgbm.a / scale);
    float m = M / (255.0f * 255.0f);
    r.rgb = rgbm.rgb * m;
    r.a = M;
    return r;
}

#define DecodeHDR(IN) DecodeBGRM8((IN))
float4 DecodeBGRE8(in float4 rgbe)
{
    float4 r;
    r.a = rgbe.a * 255 - 128;
    r.rgb = rgbe.rgb * exp2(r.a);
    r.a = length(r.rgb);
    return r;
}

float4 DecodeBGRD8(in float4 rgbd)
{
    float4 r;
    const float MaxRange = 20.0f;
    const float MaxValue = 255.0f * MaxRange;
    const float scale = 1.0f / log2(MaxValue);
    float D = MaxValue / exp2(rgbd.a / scale);
    float d = D / (255.0f * 255.0f);
    r.rgb = rgbd.rgb * d;
    r.a = D;
    return r;
}[/code]

This method doesn't support alpha as the alpha channel being used for hdr on encoding.

-------------------------

vivienneanthony | 2017-01-02 01:02:19 UTC | #3

[quote="hd_"]I don't believe Urho supports any image formats with hdr?

The way that I've gone about it is encoding the hdr information into the texture using an encoding:

Here is a fork of cmft with the ability to export dds with 'bgrd8', 'bgrm8' and 'bgre8' encodings:
[github.com/hdunderscore/cmft/tree/hdr](https://github.com/hdunderscore/cmft/tree/hdr)

Here is the hlsl shader code to decode them:
[code]float4 DecodeBGRM8(in float4 rgbm)
{
    float4 r;
    const float MaxRange = 20.0f;
    const float MaxValue = 255.0f * MaxRange;
    const float scale = 1.0f / log2(MaxValue);
    float M = exp2(rgbm.a / scale);
    float m = M / (255.0f * 255.0f);
    r.rgb = rgbm.rgb * m;
    r.a = M;
    return r;
}

#define DecodeHDR(IN) DecodeBGRM8((IN))
float4 DecodeBGRE8(in float4 rgbe)
{
    float4 r;
    r.a = rgbe.a * 255 - 128;
    r.rgb = rgbe.rgb * exp2(r.a);
    r.a = length(r.rgb);
    return r;
}

float4 DecodeBGRD8(in float4 rgbd)
{
    float4 r;
    const float MaxRange = 20.0f;
    const float MaxValue = 255.0f * MaxRange;
    const float scale = 1.0f / log2(MaxValue);
    float D = MaxValue / exp2(rgbd.a / scale);
    float d = D / (255.0f * 255.0f);
    r.rgb = rgbd.rgb * d;
    r.a = D;
    return r;
}[/code]

This method doesn't support alpha as the alpha channel being used for hdr on encoding.[/quote]

I think I understand.  I have not used the hlsl shader so Im not sure how to use it.

-------------------------

hdunderscore | 2017-01-02 01:02:20 UTC | #4

Here is the change you would make for the skybox.hlsl (however you will need to make the adjustments for glsl yourself):

[code]#include "Uniforms.hlsl"
#include "Samplers.hlsl"
#include "Transform.hlsl"

#define DecodeHDR(IN) DecodeBGRM8((IN))

float4 DecodeBGRM8(in float4 rgbm)
{
    float4 r;
    const float MaxRange = 20.0f;
    const float MaxValue = 255.0f * MaxRange;
    const float scale = 1.0f / log2(MaxValue);
    float M = exp2(rgbm.a / scale);
    float m = M / (255.0f * 255.0f);
    r.rgb = rgbm.rgb * m;
    r.a = M;
    return r;
}

float4 DecodeBGRE8(in float4 rgbe)
{
    float4 r;
    r.a = rgbe.a * 255 - 128;
    r.rgb = rgbe.rgb * exp2(r.a);
    r.a = length(r.rgb);
    return r;
}

float4 DecodeBGRD8(in float4 rgbd)
{
    float4 r;
    const float MaxRange = 20.0f;
    const float MaxValue = 255.0f * MaxRange;
    const float scale = 1.0f / log2(MaxValue);
    float D = MaxValue / exp2(rgbd.a / scale);
    float d = D / (255.0f * 255.0f);
    r.rgb = rgbd.rgb * d;
    r.a = D;
    return r;
}

void VS(float4 iPos : POSITION,
    out float4 oPos : POSITION,
    out float3 oTexCoord : TEXCOORD0)
{
    float4x3 modelMatrix = iModelMatrix;
    float3 worldPos = GetWorldPos(modelMatrix);
    oPos = GetClipPos(worldPos);
    
    oPos.z = oPos.w;
    oTexCoord = iPos.xyz;
}

void PS(float3 iTexCoord : TEXCOORD0,
    out float4 oColor : COLOR0)
{
    float4 sky = DecodeHDR(texCUBE(sDiffCubeMap, iTexCoord.xyz));
    sky.rgb *= sky.a;
    sky.rgb *= cMatEnvMapColor.r;
    oColor = (cMatDiffColor * sky);
}
[/code]

You would then need to use an encoded texture for the sky. The cMatEnvMapColor red channel affects the exposure.

-------------------------

boberfly | 2017-01-02 01:02:21 UTC | #5

BC6H is the HDR format that should be used, although GL2.1/DX9 doesn't support it:
[opengl.org/registry/specs/A ... n_bptc.txt](https://www.opengl.org/registry/specs/ARB/texture_compression_bptc.txt)

Cadaver how is Turso3D these days? :slight_smile:

-------------------------

vivienneanthony | 2017-01-02 01:02:29 UTC | #6

[quote="boberfly"]BC6H is the HDR format that should be used, although GL2.1/DX9 doesn't support it:
[opengl.org/registry/specs/A ... n_bptc.txt](https://www.opengl.org/registry/specs/ARB/texture_compression_bptc.txt)

Cadaver how is Turso3D these days? :slight_smile:[/quote]

Ah. Good to know. I sitll have to find a way to convert a hdr to dds.

-------------------------

vivienneanthony | 2017-01-02 01:02:29 UTC | #7

How did you use it? I would have to use it from the command line.


[quote="hd_"]I don't believe Urho supports any image formats with hdr?

The way that I've gone about it is encoding the hdr information into the texture using an encoding:

Here is a fork of cmft with the ability to export dds with 'bgrd8', 'bgrm8' and 'bgre8' encodings:
[github.com/hdunderscore/cmft/tree/hdr](https://github.com/hdunderscore/cmft/tree/hdr)

Here is the hlsl shader code to decode them:
[code]float4 DecodeBGRM8(in float4 rgbm)
{
    float4 r;
    const float MaxRange = 20.0f;
    const float MaxValue = 255.0f * MaxRange;
    const float scale = 1.0f / log2(MaxValue);
    float M = exp2(rgbm.a / scale);
    float m = M / (255.0f * 255.0f);
    r.rgb = rgbm.rgb * m;
    r.a = M;
    return r;
}

#define DecodeHDR(IN) DecodeBGRM8((IN))
float4 DecodeBGRE8(in float4 rgbe)
{
    float4 r;
    r.a = rgbe.a * 255 - 128;
    r.rgb = rgbe.rgb * exp2(r.a);
    r.a = length(r.rgb);
    return r;
}

float4 DecodeBGRD8(in float4 rgbd)
{
    float4 r;
    const float MaxRange = 20.0f;
    const float MaxValue = 255.0f * MaxRange;
    const float scale = 1.0f / log2(MaxValue);
    float D = MaxValue / exp2(rgbd.a / scale);
    float d = D / (255.0f * 255.0f);
    r.rgb = rgbd.rgb * d;
    r.a = D;
    return r;
}[/code]

This method doesn't support alpha as the alpha channel being used for hdr on encoding.[/quote]

-------------------------

