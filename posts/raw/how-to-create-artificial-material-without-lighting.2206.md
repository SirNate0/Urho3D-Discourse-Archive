Ray_Koopa | 2017-01-02 01:13:55 UTC | #1

I require a "visualizer material" which should just display the raw RGBA color of pixels in texture A, with the alpha multiplied with the alpha in texture B.

I read through the whole techniques and material pages, but I'm kinda baffled since it explains a lot, but I couldn't find what I need... any hints in what I need and should look into? =3

-------------------------

1vanK | 2017-01-02 01:13:55 UTC | #2

You mean how to define 2 textures in material and mix them in a shader?

-------------------------

Ray_Koopa | 2017-01-02 01:13:55 UTC | #3

Yeah, basically like it. Just one simple color texture not affected by any light, and another which alpha is multiplied to the first.

-------------------------

1vanK | 2017-01-02 01:13:55 UTC | #4

For sending textures to material use any textue slots (for examble diffuse and normal)

Materials\Mix2Tex.xml
[code]
<material>
    <technique name="Techniques/Mix2Tex.xml" />
    <texture unit="diffuse" name="Textures/Mushroom.dds" />
    <texture unit="normal" name="Textures/Smoke.dds" />
</material>
[/code]

Techniques\Mix2Tex.xml
[code]<technique vs="Mix2Tex" ps="Mix2Tex">
    <pass name="base" />
</technique>[/code]

Shaders\GLSL\Mix2Tex.glsl
[code]
#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"

varying vec2 vTexCoord;

void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
    gl_Position = GetClipPos(worldPos);
    vTexCoord = iTexCoord;
}

void PS()
{
    vec4 tex1 = texture2D(sDiffMap, vTexCoord);
    vec4 tex2 = texture2D(sNormalMap, vTexCoord);
    gl_FragColor = mix(tex1, tex2, tex2.a);
}
[/code]

-------------------------

1vanK | 2017-01-02 01:13:55 UTC | #5

Mixed texture on plane:
[url=http://savepic.ru/11092116.htm][img]http://savepic.ru/11092116m.png[/img][/url]

-------------------------

1vanK | 2017-01-02 01:13:55 UTC | #6

If you using DirectX, you need hlsl version of shader

p.s. sorry I accidentally deleted your message. I not yet accustomed to new buttons xD

-------------------------

Ray_Koopa | 2017-01-02 01:13:55 UTC | #7

is there no higher lever way? i don't know hlsl

-------------------------

1vanK | 2017-01-02 01:13:55 UTC | #8

I do not use hlsl, so I'm not sure it's correct:

[code]#include "Uniforms.hlsl"
#include "Samplers.hlsl"
#include "Transform.hlsl"

void VS(float4 iPos : POSITION,
    float2 iTexCoord : TEXCOORD0,
    out float2 oTexCoord : TEXCOORD0,
    out float4 oPos : OUTPOSITION)
{
    float4x3 modelMatrix = iModelMatrix;
    float3 worldPos = GetWorldPos(modelMatrix);
    oPos = GetClipPos(worldPos);
    oTexCoord = iTexCoord;
}

void PS(float2 iTexCoord : TEXCOORD0,
    out float4 oColor : OUTCOLOR0)
{
    float4 tex1 = Sample2D(DiffMap, iTexCoord.xy);
    float4 tex2 = Sample2D(NormalMap, iTexCoord.xy);
    oColor = lerp(tex1, tex2, tex2.a);
}
[/code]

-------------------------

