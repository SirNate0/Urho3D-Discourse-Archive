spwork | 2018-05-31 07:06:28 UTC | #1

I'm a raw recruit with shaders，i want use two input textures to generate a output，like this:

    <renderpath>
        <rendertarget name="MyTarget" tag="MyPostProcess" sizedivisor="1 1" format="rgba" filter="true" />
        <command type="quad" tag="MyPostProcess" vs="MyPostProcess" ps="MyPostProcess" output="viewport">
    	<texture unit="diffuse" name="viewport" />
    	<texture unit="diffuse" name="d:/mytexture.png" />
        </command>
    </renderpath>

And how to fix this shader to make it generate  superimposed values ​​for two picture colors？

    void VS(float4 iPos : POSITION,
        out float2 oScreenPos : TEXCOORD0,
        out float4 oPos : OUTPOSITION)
    {
        float4x3 modelMatrix = iModelMatrix;
        float3 worldPos = GetWorldPos(modelMatrix);
        oPos = GetClipPos(worldPos);
        oScreenPos = GetScreenPosPreDiv(oPos);
    }

    void PS(float2 iScreenPos : TEXCOORD0,
        out float4 oColor : OUTCOLOR0)
    {
        oColor = Sample2D(DiffMap, iScreenPos);
    }

-------------------------

Eugene | 2018-05-31 10:30:40 UTC | #2

You cannot bind multiple textures to one texture unit.
Find another one (e.g. normal map) that that you don't need for anything else.
Then, sample both and do whatever you want.

https://github.com/urho3d/Urho3D/blob/6d08bcd8c00cc600b0c73315aa61dd7d5c6dec1d/Source/Urho3D/Graphics/Direct3D9/D3D9Graphics.cpp#L2640

-------------------------

