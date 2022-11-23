Bart | 2017-01-02 01:13:37 UTC | #1

Hello all,
I am experiencing strange issue with materials that use transparency and/or normal maps. Some surfaces/textures disappear when rotating the view around object. It is dependent on view angle, so I guess this has something to do with lighting. My setup:

[ul]
[li]Windows 7 x64[/li]
[li]MSVC 2013 x64[/li]
[li]D3D11[/li]
[li]Nvidia GTX980Ti[/li]
[li]Both Urho 1.5 stable and head branch tested, same behaviour[/li]
[li]Forward renderpath[/li][/ul]


[b]Situation 1 : Disappearing polygons with transparent textures[/b]

[ul]
[li]used "DiffAlpha" technique and transparent PNG texture[/li][/ul]

[b]Material:[/b]
[code]
<material>
	<technique name="Techniques/DiffAlpha.xml" />
	<texture unit="diffuse" name="04_Objects/Trees/Tree_test_02/Textures/TexturesCom_Branches0013_1_alphamasked_S.png" />
	<parameter name="MatDiffColor" value="1 1 1 1" />
	<parameter name="MatSpecColor" value="0 0 0 40" />
	<parameter name="MatEmissiveColor" value="0 0 0 1" />
</material>
[/code]

[video]https://youtu.be/NMa9X0tWsss[/video]

[b]Situation 2 : Disappearing textures when used normal map[/b]

[ul]
[li]used "DiffNormalSpec" technique with diffuse, specular and normal maps[/li]
[li]the problem appears only when some external light is used (besides zonelight)[/li]
[li]error appears when a light is added: [i]ERROR: Failed to create input layout for shader LitSolid(NORMALMAP PERPIXEL POINTLIGHT), missing element mask 128[/i][/li][/ul]

[b]Material:[/b]
[code]
<material>
	<technique name="Techniques/DiffNormalSpec.xml" quality="1" />
    <technique name="Techniques/Diff.xml" quality="0" />
	<texture unit="diffuse" name="04_Objects/Wall_test_03/03_Urho/Textures/TexturesCom_BrickSmallBrown0094_1_seamless_S.jpg" />
	<texture unit="specular" name="04_Objects/Wall_test_03/03_Urho/Textures/TexturesCom_BrickSmallBrown0094_1_seamless_S_specular.png" />
	<texture unit="normal" name="04_Objects/Wall_test_03/03_Urho/Textures/TexturesCom_BrickSmallBrown0094_1_seamless_S_normal.jpg" />
	<parameter name="MatDiffColor" value="1 1 1 1" />
	<parameter name="MatSpecColor" value="0.18 0.18 0.18 80" />
	<parameter name="MatEmissiveColor" value="0 0 0 1" />
</material>
[/code]

[video]https://youtu.be/f42ZedUBBuw[/video]


Would you have a hint what to test? Are my materials parametrized correctly (I hope so, I copied the examples)? Are there some setting that I should check?

Thank you very much for any suggestions/help.

-------------------------

cadaver | 2017-01-02 01:13:37 UTC | #2

Normal mapping needs tangents. D3D11 is strict in that sense that it fails to render if shader expects tangents and there aren't none.

In AssetImporter, you can generate tangents with -t switch when you save your model file.

-------------------------

yushli | 2017-01-02 01:13:38 UTC | #3

It looks like the tangent issue has bitten quite a few people. Maybe it should be enabled to generate by default in assimporter?

-------------------------

Bart | 2017-01-02 01:13:45 UTC | #4

Hi cadaver,
thank you very much for the advice, the second problem (with normal maps) was really caused by missing tangents in the model. All that was needed was to add -t parameter in AssetImporter. However, the first problem still stands and there are no issues reported in the log. Would you have any clues what to check? The model is simple tree with "leaves" (branches) with transparent textures.

Thanks a lot

-------------------------

1vanK | 2017-01-02 01:13:45 UTC | #5

I think it is problem with sorting for alpha pass (part of the model lean too close to each other and they can not be sorted correctly). Yu need use AlphaMask instead Alpha for leaves. It also solves the problem with the shadows from the tree.

-------------------------

Bart | 2017-01-02 01:13:45 UTC | #6

Thanks 1vanK! That was exactly the cause.

-------------------------

