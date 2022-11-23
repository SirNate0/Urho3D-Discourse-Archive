throwawayerino | 2020-04-24 22:53:53 UTC | #1

When there's only one model with that material it works wonderfully, but when there's two it returns `iModelMatrix` undefined
Shader:
```
#ifdef COMPILEPS

bool cOutlineEnabled = false;

float color_difference(float4 sc, float4 nc)
{
    return abs(sc.r - nc.r) + abs(sc.g - nc.g) + abs(sc.b - nc.b);
}
 
float4 get_pixel(Texture2D tex, SamplerState samp, in float2 coords, in float dx, in float dy)
{
    float4 result = tex.Sample(samp, coords + float2(dx, dy));
    return result;
}
 
// returns pixel color
float IsEdge(Texture2D tex, SamplerState samp, float2 coords)
{
    float dxtex = 1.0 / 1920.0; //image width;
    float dytex = 1.0 / 1080.0; //image height;
    float cd[8];
 
    float4 sc = get_pixel(tex, samp, coords, 0.0 * dxtex, 0.0 * dytex);
    cd[0] = color_difference(sc, get_pixel(tex, samp, coords, -1.0 * dxtex, -1.0 * dytex) ); //color of itself
    cd[1] = color_difference(sc, get_pixel(tex, samp, coords, -1.0 * dxtex, 0.0 * dytex) );
    cd[2] = color_difference(sc, get_pixel(tex, samp, coords, -1.0 * dxtex, 1.0 * dytex) );
    cd[3] = color_difference(sc, get_pixel(tex, samp, coords, 0.0 * dxtex, 1.0 * dytex) );
 
    float4 alt1 = get_pixel(tex, samp, coords, 1.0 * dxtex, 1.0 * dytex);
    float4 alt2 = get_pixel(tex, samp, coords, 1.0 * dxtex, 0.0 * dytex);
    float4 alt3 = get_pixel(tex, samp, coords, 1.0 * dxtex, -1.0 * dytex);
    float4 alt4 = get_pixel(tex, samp, coords, 0.0 * dxtex, -1.0 * dytex);
 
    if (length(alt1.rgb) < 0.1)
    {
        cd[4] = color_difference(sc, alt1);
    }
    else
    {
        cd[4] = 0.0;
    }
    if (length(alt2.rgb) < 0.1)
    {
        cd[5] = color_difference(sc, alt2);
    }
    else
    {
        cd[5] = 0.0;
    }
    if (length(alt3.rgb) < 0.1)
    {
        cd[6] = color_difference(sc, alt3);
    }
    else
    {
        cd[6] = 0.0;
    }
    if (length(alt4.rgb) < 0.1)
    {
        cd[7] = color_difference(sc, alt4);
    }
    else
    {
        cd[7] = 0.0;
    }
 
    return cd[0] + cd[1] + cd[2] + cd[3] + cd[4] + cd[5] + cd[6] + cd[7];
}
#endif
 
void VS(float4 iPos : POSITION,
        float3 iNormal : NORMAL,
        out float4 oPos : OUTPOSITION,
        out float4 vColor : TEXCOORD0,
        out float4 vScreenPos : TEXCOORD1)
{
    float4x3 modelMatrix = iModelMatrix;
    float3 worldPos = GetWorldPos(modelMatrix);
    oPos = GetClipPos(worldPos);
 
#ifdef EDGE
      vScreenPos = GetScreenPos(oPos);
#endif

#ifdef BASE
        float3 n = iNormal+float3(1.0);
        n*=0.5;
        vColor = float4(n, 1.0);
#endif
}
 
void PS(in float4 iPos : POSITION,
        in float4 vColor : TEXCOORD0,
        in float4 vScreenPos : TEXCOORD1,
        out float4 oColor : SV_TARGET)
{
#ifdef BASE
        float4 diffColor = vColor;
        oColor = oColor;
#endif

#ifdef EDGE

    float4 color = float4(0.0, 0.0, 0.0, 1.0);
    float2 coords = vScreenPos.xy / vScreenPos.w;
    if (IsEdge(tEnvMap, sEnvMap, coords) >= 0.5)
    {
        if (cOutlineEnabled)
        {
            color.rgba = float4(0.0, 1.0, 0.0, 1.0);

        }
        else
        {
            color.rgba = float4(1.0, 1.0, 1.0, 1.0);
        }
    }
    else
    {
        color = get_pixel(tEnvMap, sEnvMap, vScreenPos.xy / vScreenPos.w, float(0) * (1.0 / 1920.0), float(0) * (1.0 / 1080.0));
    }
    oColor = color;
#endif
}
```
Technique:
```
<technique vs="LitSolid" ps="LitSolid" psdefines="DIFFMAP">
	<pass name="base" />
    <pass name="litbase" psdefines="AMBIENT" />
    <pass name="light" depthtest="equal" depthwrite="false" blend="add" />
    <pass name="prepass" psdefines="PREPASS" />
    <pass name="material" psdefines="MATERIAL" depthtest="equal" depthwrite="false" />
    <pass name="deferred" psdefines="DEFERRED" />
    <pass name="depth" vs="Depth" ps="Depth" />
    <pass name="shadow" vs="Shadow" ps="Shadow" />
	<pass name="refract" vs="Outline" ps="Outline" vsdefines="EDGE" psdefines="EDGE" blend="alpha"/>
</technique>

```

-------------------------

Eugene | 2020-04-25 12:57:49 UTC | #2

To handle instancing in your custom shader you have to conditionally pass the matrix components as input parameters. See standard LitSolid for example.

-------------------------

throwawayerino | 2020-04-25 12:59:18 UTC | #3

I added
```
#ifdef INSTANCED
float4x3 iModelMatrix  : TEXCOORD4,
#endif
```
to the middle of my VS() signature. Would've been helpful if that was in the docs

-------------------------

