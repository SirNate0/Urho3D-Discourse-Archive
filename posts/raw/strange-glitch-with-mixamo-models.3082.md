smellymumbler | 2017-05-02 19:24:05 UTC | #1

I'm getting this strange shadow with Mixamo models only. I'm using the AssetImporter with the FBX straight from their website. 

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/fdb0618ded569d7b530efac1aaa9b758b120e81f.png" width="690" height="468">

My material definition:

```
<?xml version="1.0"?>
<material>
	<technique name="Techniques/DiffNormalSpec.xml" />
	<texture unit="diffuse" name="Models/Swat/Textures/body_diffuse.png" />
	<texture unit="normal" name="Models/Swat/Textures/body_normal.png" />
	<texture unit="specular" name="Models/Swat/Textures/body_specular.png" />
	<parameter name="MatDiffColor" value="0.8 0.8 0.8 1" />
	<parameter name="MatSpecColor" value="0.5 0.5 0.5 6.31179" />
	<parameter name="MatEmissiveColor" value="0 0 0 1" />
</material>
```

-------------------------

rasteron | 2017-05-02 19:24:17 UTC | #2

Hey smellymumbler, I got that same result before as well. Have you tried adding the `-t` flag (Generate tangents) in your option?

-------------------------

smellymumbler | 2017-05-01 01:30:15 UTC | #3

It worked! Thanks. Any idea why this happens?

-------------------------

JTippetts | 2017-05-01 13:02:29 UTC | #4

Because if you don't generate tangents, but your material uses them (because it uses the DiffNormalSpec technique) then it's getting garbage instead of tangents. Any technique with Normal in the name, you need to generate tangents or it'll use garbage tangents.

-------------------------

smellymumbler | 2017-05-01 14:27:27 UTC | #5

Thank you for the help. :)

-------------------------

