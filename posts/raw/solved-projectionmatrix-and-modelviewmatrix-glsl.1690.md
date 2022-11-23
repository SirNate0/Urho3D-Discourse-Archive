rasteron | 2017-01-02 01:09:30 UTC | #1

Hey guys,

I'm trying to create a skydome material/shader and so the first I did was to derive from skybox and some changes so here's my current shader wip. I was wondering what is the equivalent for [b]position[/b], [b]projectionMatrix[/b] and [b]modelViewMatrix[/b] in Urho3D.

Using the dome model, this works in glsl but the texture is sort of tiled:

[code]
varying vec2 vTexCoord;

void VS()
{

    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
    gl_Position = GetClipPos(worldPos);
    gl_Position.z = gl_Position.w;
    vTexCoord = iPos.xy;

}

void PS()
{   

    vec4 sample = texture2D(sDiffMap, vTexCoord);
    gl_FragColor = vec4(sample.xyz, sample.w); 
    
}
[/code]

[img]http://i.imgur.com/AtadmE9l.jpg[/img]

-------------------------

codingmonkey | 2017-01-02 01:09:30 UTC | #2

May I look at your material xml file and tech xml? 

std Skybox shader use cube maps
gl_FragColor = cMatDiffColor * textureCube(sDiffCubeMap, vTexCoord);

earlier I do some chandes with this shader for FH's skybox with one usual texture
this is it:
<technique vs="SkySphere" ps="SkySphere">
    <pass name="postopaque" depthwrite="false" />
</technique>

dx9 hlsl shader - SkySphere.hlsl
[code]
#include "Uniforms.hlsl"
#include "Samplers.hlsl"
#include "Transform.hlsl"

void VS(float4 iPos : POSITION, 
        float2 iTexCoord: TEXCOORD0,
        out float2 oTexCoord : TEXCOORD0, 
        out float4 oPos : SV_POSITION)
{
    float4x3 modelMatrix = iModelMatrix;
    float3 worldPos = GetWorldPos(modelMatrix);
    oPos = GetClipPos(worldPos);
    
    oPos.z = oPos.w;
    oTexCoord = iTexCoord;
}

void PS(float2 iTexCoord : TEXCOORD0, 
        out float4 oColor : OUTCOLOR0)
{
    oColor = cMatDiffColor * Sample2D(DiffMap, iTexCoord);
}
[/code]

in you case you need to try instead this 
vTexCoord = iPos.xy;
use std texture cords
vTexCoord = iTexCoord;

-------------------------

rasteron | 2017-01-02 01:09:31 UTC | #3

Thanks CodingMonkey! works perfectly :smiley:

-------------------------

