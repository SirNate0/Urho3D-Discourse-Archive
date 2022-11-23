rasteron | 2017-01-02 01:13:09 UTC | #1

Some vibrance effects..

[img]https://cloud.githubusercontent.com/assets/3676827/16691975/8898c13e-4561-11e6-8a9d-45a764a4e26e.png[/img]

[gist]https://gist.github.com/bc75bae59873e342ec94a08e57752046[/gist]
[gist]https://gist.github.com/ceddd66430d24f676e0583201d2ace34[/gist]

enjoy. :slight_smile:

-------------------------

godan | 2017-01-02 01:13:09 UTC | #2

love it!

-------------------------

sabotage3d | 2017-01-02 01:13:09 UTC | #3

Looks cool.

-------------------------

rasteron | 2017-01-02 01:13:09 UTC | #4

thanks guys, hope you'll find this useful. :slight_smile:

-------------------------

sabotage3d | 2017-01-02 01:13:10 UTC | #5

Thanks for sharing those. I would create a whole repository with all these shaders they are wonderful addition to any game or toolset.

-------------------------

Victor | 2017-01-02 01:13:10 UTC | #6

Agreed, this is awesome! I've gone ahead and used your example to implement the HLSL for those using DX11

[b]HLSL for DX11[/b]
[code]
<renderpath>
    <command type="quad" tag="Vibrance" vs="Vibrance" ps="Vibrance" output="viewport">
        <texture unit="diffuse" name="viewport" />

        <parameter name="Amount" value="1.0" />
        <parameter name="Coeff" value="0.299 0.587 0.114 0.0" />
    </command>
</renderpath>
[/code]

[code]
#include "Uniforms.hlsl"
#include "Samplers.hlsl"
#include "Transform.hlsl"
#include "ScreenPos.hlsl"
#include "Lighting.hlsl"

cbuffer CustomVS : register(b6)
{
    float cAmount;
    float4 cCoeff;
}

void VS(
    float4 iPos : POSITION,
    out float2 oScreenPos : TEXCOORD0,
    out float4 oPos : OUTPOSITION
)
{
    float4x3 modelMatrix = iModelMatrix;
    float3 worldPos = GetWorldPos(modelMatrix);
    oPos = GetClipPos(worldPos);
    oScreenPos = GetScreenPosPreDiv(oPos);
}

void PS(
    float2 iScreenPos : TEXCOORD0,
    out float4 oColor : OUTCOLOR0
)
{
    float4 color = Sample2DLod0(DiffMap, iScreenPos);

    float lum = dot(color, cCoeff);
    float4 lum4 = float4(lum, lum, lum, lum); // hlsl wants this expressed explicitly.

    float4 mask = (color - lum4);

    mask = clamp(mask, 0.0, 1.0);

    float lumMask = dot(cCoeff, mask);
    lumMask = 1.0 - lumMask;

    oColor = lerp(lum4, color, 1.0 + cAmount * lumMask);
}
[/code]

-------------------------

rasteron | 2017-01-02 01:13:10 UTC | #7

[quote="sabotage3d"]Thanks for sharing those. I would create a whole repository with all these shaders they are wonderful addition to any game or toolset.[/quote]

Sure thing and that's great sabotage3d!

@Victor

Awesome! nice addition.

-------------------------

