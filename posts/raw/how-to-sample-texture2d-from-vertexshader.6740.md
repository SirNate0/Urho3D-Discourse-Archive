najak3d | 2021-03-02 03:00:56 UTC | #1

We are trying to use a Texture2D heightmap inside the VertexShader to offset the Y positions of the grid.  This is much more efficient than recreating a unique VertexBuffer for each Terrain Tile.  So we can have ONE Vertex Buffer, and then use two parameters "TilePos" and "TileSize" to correctly offset each Grid point into World Space for the Pixel Shader. 

Problem is that I can't seem to get the Vertex Shader to recognize the sDiffMap to sample it.

Here is my Pixel Shader:

    #include "Uniforms.hlsl"
    #include "Samplers.hlsl"
    #include "Transform.hlsl"

    #ifdef COMPILEVS
    cbuffer CustomVS : register(b6)
    {
        float2 cTilePos;
        float2 cTileSize;
    }
    sampler2D sDiffMap : register(s0);
    #endif

    void VS(float4 iPos : POSITION,
    	float2 iTexCoord : TEXCOORD0,
        out float2 oTexCoord : TEXCOORD0,
        out float4 oPos : OUTPOSITION)
    {
        float2 offset = iTexCoord;
        offset.x *= cTileSize.x;
        offset.y *= cTileSize.y;
        offset += cTilePos;

        float2 diffVal = Sample2DLod0(DiffMap, iTexCoord).rg;
        float3 pos = float3(offset.x, diffVal.r, offset.y);

        oPos = GetClipPos(pos);
        oTexCoord = iTexCoord;
    }

===
When Urho3D compiles this, I get the following error:

ERROR: Failed to compile vertex shader Terrain3D_Alerts():
....\Shaders\HLSL\Terrain3D_Alerts.hlsl(514,22-53): error X3004: undeclared identifier 'tDiffMap'

So if I add another line:
    sampler2D tDiffMap : register(s0);

Then it gives me this error:
ERROR: Failed to compile vertex shader Terrain3D_Alerts():
...\Shaders\HLSL\Terrain3D_Alerts.hlsl(515,22-49): error X3087: sampler2D object does not have methods

@JSandusky - you answered my previous post on this, so I posted it fresh here with Shader code so that you might be help to tell me what I'm doing wrong.

[https://discourse.urho3d.io/t/how-to-fetch-sdiffmap-in-vertexshader/904/9](https://discourse.urho3d.io/t/how-to-fetch-sdiffmap-in-vertexshader/904/9)

-------------------------

JSandusky | 2021-03-02 03:11:41 UTC | #2

You need the texture 2D object as well, in HLSL you have to use sampler objects to sample textures. The texture read macros are hiding it from you and that's why the error messages are confounding.

```
Texture2D tDiffMap : register(t0);
SamplerState sDiffMap : register(s0);
```

-------------------------

najak3d | 2021-03-02 03:12:03 UTC | #3

That worked like a charm!  Thank you @JSandusky .

-------------------------

najak3d | 2021-03-02 03:12:37 UTC | #4

Final working code looks like this:

#include "Uniforms.hlsl"
#include "Samplers.hlsl"
#include "Transform.hlsl"

#ifdef COMPILEVS
cbuffer CustomVS : register(b6)
{
    float2 cTilePos;
    float2 cTileSize;
}
Texture2D tDiffMap : register(t0);
SamplerState sDiffMap : register(s0);

#endif

void VS(float4 iPos : POSITION,
	float2 iTexCoord : TEXCOORD0,
    out float2 oTexCoord : TEXCOORD0,
    out float4 oPos : OUTPOSITION)
{
    float2 offset = iTexCoord;
    offset.x *= cTileSize.x;
    offset.y *= cTileSize.y;
    offset += cTilePos;

    float2 diffVal = Sample2DLod0(DiffMap, iTexCoord).rg;
    float3 pos = float3(offset.x, diffVal.r, offset.y);

    oPos = GetClipPos(pos);
    oTexCoord = iTexCoord;
}

-------------------------

