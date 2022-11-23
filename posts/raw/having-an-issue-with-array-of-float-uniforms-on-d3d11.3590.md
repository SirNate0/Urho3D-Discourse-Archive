JTippetts | 2017-09-21 14:10:49 UTC | #1

Working on the terrain shader for my terrain editor, and having some issues with the D3D11 version. I am declaring an array of float uniforms as:

    static const int numlayers=8;
    #ifdef COMPILEPS

		cbuffer CustomPS : register(b6)
		{
			float cLayerScaling[numlayers];
		};
	#endif

Then, I access it to scale a terrain texture layer by a specified amount:

    float4 SampleDiffuse(float3 detailtexcoord, int layer, float3 blend)
	{
		return tDetailMap2.Sample(sDetailMap2, float3(detailtexcoord.zy*cLayerScaling[layer], layer))*blend.x +
			tDetailMap2.Sample(sDetailMap2, float3(detailtexcoord.xy*cLayerScaling[layer], layer))*blend.z +
			tDetailMap2.Sample(sDetailMap2, float3(detailtexcoord.xz*cLayerScaling[layer], layer))*blend.y;
	}

In Lua script, I pass the material an array Variant object constructed like so:

    local buf=VectorBuffer()
	buf:WriteFloat(2)
	buf:WriteFloat(2)
	buf:WriteFloat(1.0)
	buf:WriteFloat(1.0)
	buf:WriteFloat(1.0)
	buf:WriteFloat(1.0)
	buf:WriteFloat(1.0)
	buf:WriteFloat(0.25)
	
	local ary=Variant()
	ary:Set(buf)
    TerrainState.terrainMaterial:SetShaderParameter("LayerScaling", ary)

But for some reason, the shader isn't receiving all of the floats in the array. It receives the first float correctly, it receives an incorrect value for the second one, and the rest it receives the value of 0.

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/d1053f0a172aba845dff12421ec8c5cf6591d703.png'>

It works on the OpenGL version just fine, so I don't think it's a problem with constructing the VectorBuffer and setting the parameter:

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/86ffe967bc1b4c7b1a2b82519446863eb9c89698.png'>

Anybody have any ideas?

-------------------------

Eugene | 2017-09-21 15:10:48 UTC | #2

Ty to debug `Graphics::SetShaderParameter(StringHash param, const float* data, unsigned count)`
Does it receive valid values?

-------------------------

JTippetts | 2017-09-21 22:38:17 UTC | #3

I added some logging code, and it looks like it is getting the values:

    [Thu Sep 21 16:29:59 2017] INFO: Shader parameter buffer index 0: 2
    [Thu Sep 21 16:29:59 2017] INFO: Shader parameter buffer index 1: 2
    [Thu Sep 21 16:29:59 2017] INFO: Shader parameter buffer index 2: 1
    [Thu Sep 21 16:29:59 2017] INFO: Shader parameter buffer index 3: 1
    [Thu Sep 21 16:29:59 2017] INFO: Shader parameter buffer index 4: 1
    [Thu Sep 21 16:29:59 2017] INFO: Shader parameter buffer index 5: 1
    [Thu Sep 21 16:29:59 2017] INFO: Shader parameter buffer index 6: 1
    [Thu Sep 21 16:29:59 2017] INFO: Shader parameter buffer index 7: 0.25

I added a check in ConstantBuffer as well to make sure it's not overflowing the buffer, and everything looks good there.

-------------------------

Alex-Doc | 2017-09-22 05:52:40 UTC | #4

Maybe this can be useful for investigating further? 
https://renderdoc.org

-------------------------

Eugene | 2017-09-22 14:25:12 UTC | #5

Arrays are not packed in DX11. Every element of the array is aligned to float4 vector.
https://msdn.microsoft.com/ru-ru/library/windows/desktop/bb509632%28v=vs.85%29.aspx?f=255&MSPPError=-2147217396

-------------------------

JTippetts | 2017-09-22 14:25:39 UTC | #6

Looks like that was the issue. Thank you!

-------------------------

