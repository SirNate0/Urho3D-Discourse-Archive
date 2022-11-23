amit | 2017-01-02 01:04:09 UTC | #1

I have written a custom fbx to mdl exporter which exports vertices(offcourse), Normal and multiple uv and Morph targets.
The mesh uses single uv for diffuse, normal and specular map.
In the material xml I used diffuse and normal only, yet there is no effect of either light or normal.
But it is strange to see a very dark diffuse on the model. It should be either properly lit  or not seen at all or solid color if there was any error.

As discussed on [topic939.html](http://discourse.urho3d.io/t/solved-normalmap-strange-behavior/917/1) the problem seems similar and they have suggested that we need to also generate tangent.
Below are the material I used and a screenshot from the editor showing both the heart(you have to see closely, it is very dark and to the right of brightly & correctly lit cube face) and a standard cube with same material and directional light.
The cube is render correctly.
[code]<?xml version="1.0"?>
<material>
	<technique name="Techniques/DiffNormalPacked.xml" quality="1" loddistance="0" />
	<technique name="Techniques/Diff.xml" quality="0" loddistance="0" />
	<texture unit="diffuse" name="Textures/Heart_Diff.png" />
	<texture unit="normal" name="Textures/StoneNormal.dds" />
	<texture unit="specular" name="Textures/Heart_Spec.png" />
	<parameter name="UOffset" value="1 0 0 0" />
	<parameter name="VOffset" value="0 1 0 0" />
	<parameter name="MatDiffColor" value="1 1 1 1" />
	<parameter name="MatEmissiveColor" value="0 0 0" />
	<parameter name="MatEnvMapColor" value="1 1 1" />
	<parameter name="MatSpecColor" value="0.3 0.3 0.3 16" />
	<cull value="ccw" />
	<shadowcull value="ccw" />
	<depthbias constant="0" slopescaled="0" />
</material>
[/code]
[img]http://img.ctrlv.in/img/15/03/14/5503ec0e1d413.png[/img]

The model is render properly if unlit material is used, ie no normal and light calculation which really degrades the scene.
I would appreciate if somebody can help me out with a good material with diffuse ,normal and specular map.

-------------------------

codingmonkey | 2017-01-02 01:04:10 UTC | #2

>they have suggested that we need to also generate tangent.
yes, without tangents the normal mapping is not work properly
see blender exporter how they is generated.
also check out your model's normals they must orient not in inwards

-------------------------

amit | 2017-01-02 01:04:10 UTC | #3

Thanks,
Tangent were created, and normals are workin, now there is a seam when lit, but the normal prob is solved.

-------------------------

