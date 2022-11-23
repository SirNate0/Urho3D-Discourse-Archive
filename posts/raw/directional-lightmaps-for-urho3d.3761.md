GodMan | 2017-11-19 22:56:18 UTC | #1

So I wrote a dx9 hlsl shader for Directional Lightmaps for Irrlicht some time ago. I've seen threads of people having issues with light mapping in urho3d. Will I be able to port my shader over to urho3d I know I have to modify it to use the data that the API expects. Also I did not see anywhere in the documentation how to actually set the lightmap texture to use the 2nd UV set in the materials file.

-------------------------

Dave82 | 2017-11-19 23:41:54 UTC | #2

[quote="GodMan, post:1, topic:3761"]
Also I did not see anywhere in the documentation how to actually set the lightmap texture to use the 2nd UV set in the materials file.
[/quote]

Hi ! Use the TU_EMISSIVE texture slot for the lightmap and be sure you use one of the Lightmap techniques to have the 2nd texture coors in the shader (DiffLightmap.xml or DiffLightmapAlpha.xml)

-------------------------

GodMan | 2017-11-20 00:36:53 UTC | #3

I have the material file that way already but the lightmap is not shown.
material
	technique name="Techniques/DiffLightMap.xml" quality="1"/>
	texture unit="diffuse" name="Textures/metal plate floor ext.tga" />
	texture unit="emissive" name="Textures/lightmap.tga" />
	parameter name="MatDiffColor" value="0.588235 0.588235 0.588235 1" />
	parameter name="MatSpecColor" value="0 0 0 2" />
	parameter name="MatEmissiveColor" value="0.4 0.4 0.4 1" />
material

I removed the <> so urho3d will allow me to post the xml file.

-------------------------

