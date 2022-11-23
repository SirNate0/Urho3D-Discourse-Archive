GodMan | 2019-01-05 01:13:12 UTC | #1

I'm using dx9, and I've noticed the specular without a cubemap is not very noticeable. I've even used the define `SPECMAP`, and used a rgb texture for the specular map slot.

Material:

    <material>
    	<technique name="Techniques/DiffNormalSpec.xml" />
    	<texture unit="diffuse" name="Textures/head.tga" />
    	<texture unit="normal" name="Textures/grunt_head_bump.tga" />
    	<texture unit="specular" name="Textures/grunt_chest_spec.tga" />
    	<shader  psdefines= "NORMALMAP SPECMAP" />
    	<parameter name="bumpStrength" value="2.0" />
    	<parameter name="MatDiffColor" value="1.0 1.0 1.0 1" />
    	<parameter name="MatSpecColor" value="0.38 0.38 0.38 2" />
    	<parameter name="MatEmissiveColor" value="0 0 0 1" />
    </material>

-------------------------

GodMan | 2019-01-05 10:59:31 UTC | #2

Solved:

You have to set the MatSpecColor alpha value to a much higher value. IF you have experience with shaders the spec value is normally either 32 or 64 for a finer specular result.
   
```
<parameter name="MatSpecColor" value="0.38 0.38 0.38 64" />
```
The default values were always set to between 0 and 1. The alpha value for specular material needs to be much higher or you will get a flat result. Hope this helps someone in the future.

-------------------------

Modanung | 2019-01-05 10:21:36 UTC | #3

This is because in case of the specular colour the fourth value denotes _hardness_ instead of _alpha_.

-------------------------

