vivienneanthony | 2018-04-24 18:02:39 UTC | #1

Hi,

Have anyone tried DecalMachine with Urho3D?   I'm trying to get https://imgur.com/FMmzqZX to show correctly using the NoTextureNormal Technique. 

I got the material to show correctly. It's now getting the texture to show the detail correctly.

This is a example of a low poly that's possible https://skfb.ly/6wW9C

This is the material.

[code]
<material>
	<technique name="Techniques/DiffNormal.xml" quality="0" loddistance="0" />
	<parameter name="MatDiffColor" value="1 1 1 1"/>
	<parameter name="MatSpecColor" value="0.5 0.5 0.5 50"/>
	<texture unit="normal" name="GameData/Textures/ShuttleDoor_Normal_Base.png" />	
	<texture unit="diffuse" name="GameData/Textures/GenericHull4_Diff.png" />
	<cull value="ccw"/>
	<shadowcull value="ccw"/>
</material>
[/code]

Screenshot 

https://imgur.com/a/iYuMJuy
Vivienne

-------------------------

vivienneanthony | 2018-04-26 16:22:06 UTC | #2

The problems I get using DiffNormal or NoTextureNormal. Depending how far the camera is from the material. It does not show. Also, It seems to blur the texture so it doesn't match the detail.

-------------------------

vivienneanthony | 2018-04-26 16:22:20 UTC | #3

I increased the texture size.

-------------------------

