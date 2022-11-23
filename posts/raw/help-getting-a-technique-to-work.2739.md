vivienneanthony | 2017-01-23 05:33:24 UTC | #1

Hi, 
I'm trying to get a technique for a material in a model. It seems to be not affected by light.

The technique is

[code]
<technique vs="LitSolid" ps="LitSolid" psdefines="DIFFMAP">
    <pass name="base" psdefines="EMISSIVEMAP" />
    <pass name="light" vsdefines="NORMALMAP" psdefines="NORMALMAP SPECMAP" depthtest="equal" depthwrite="false" blend="add" />
    <pass name="prepass" vsdefines="NORMALMAP" psdefines="PREPASS NORMALMAP SPECMAP" />
    <pass name="material" psdefines="MATERIAL SPECMAP EMISSIVEMAP" depthtest="equal" depthwrite="false" />
[/code]

and my material is

[code]<material>
   <technique name="Techniques/DiffNormalSpecEmissive.xml" />
   <texture unit="diffuse" name="GameData/Textures/Planets/NewCunnun_CubeCorss_Diffuse.png" />
   <texture unit="specular" name="GameData/Textures/Planets/NewCunnun_CubeCorss_Specular.png" />
   <texture unit="normal" name="GameData/Textures/Planets/NewCunnun_CubeCorss_Normal.png" />
   <texture unit="emissive" name="GameData/Textures/Planets/NewCunnun_CubeCorss_Emission.png" />
   <parameter name="MatDiffColor" value="1 1 1 1"/>
   <parameter name="MatSpecColor" value="1 1 1 1"/>
   <parameter name="MatEmissiveColor" value="0 0 0" />
   <cull value="ccw" />
   <shadowcull value="ccw" />
   <fill value="solid" />
   <depthbias constant="0" slopescaled="0" />
</material>
[/code]

Any help appreciated.

Vivienne
    <pass name="deferred" vsdefines="NORMALMAP" psdefines="DEFERRED NORMALMAP SPECMAP EMISSIVEMAP" />
    <pass name="depth" vs="Depth" ps="Depth" />
    <pass name="shadow" vs="Shadow" ps="Shadow" />
</technique>

-------------------------

vivienneanthony | 2017-01-23 07:21:35 UTC | #2

It partially works if I don't use DiffNormalSpec or DiffNormalPackedSpec.xml.  If I use those techniques. Parts of the object is invisible. So, I'm just trying the proper way to set the normal texture so DiffNormalxxxx can be used.

-------------------------

1vanK | 2017-01-23 07:35:20 UTC | #3

> DiffNormalxxxx

May be model has no tangents in vertices

-------------------------

vivienneanthony | 2017-01-23 14:33:24 UTC | #4

I added tangents also.

THe result is this 

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/9ac6f725c4606fb412d76a6f5c260ad0e12b2623.png" width="690" height="431">

So I have to figure out  why it's doing that. The texture is seamless. It started as a cube then rounded into a sphere. Maybe it save the tangent as squared not smooth.

Hmmm.

-------------------------

1vanK | 2017-01-23 14:41:19 UTC | #6

It looks like smooth groups

-------------------------

