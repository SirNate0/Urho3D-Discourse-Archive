dev4fun | 2018-02-13 22:03:48 UTC | #1

I was trying to import some models on Urho3D editor, but Im getting some problems with textures that have alpha channel..

Look the pictures:

(Urho3D editor)
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/7/7c22f5199b2515baa73f8962e3fc95efa2153d0b.png'>

(3Ds Max)
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/0/08dcd4267192f2f701d8b5fba3954fffac7c1bc5.png'>

I dont know why, but material its translucent... Im already using DiffAlpha.xml technique. The texture its a TGA using Alpha Channel.

Texture Alpha Channel:
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/4/430dacd07a8ab18ec6f3f949338305bff0b2a456.png'>

Thanks!

-------------------------

Sinoid | 2018-02-13 23:16:42 UTC | #2

Check the value of the `MatDiffColor` parameter in your **material** XML file. If it isn't there then add it as:

`<parameter name="MatDiffColor" value="1 1 1 1" />`

The `MatDiffColor` gets multiplied with the input from your texture. So if it's something like `1, 1, 1, 0.5` then you end up with your texture alpha cut in half. Lets you do fades and tints.

-------------------------

dev4fun | 2018-02-13 23:40:18 UTC | #3

[quote="Sinoid, post:2, topic:4014"]
value of the MatDi
[/quote]


Nothing is changed :frowning:

-------------------------

Sinoid | 2018-02-13 23:42:59 UTC | #4

Copy and paste your material XML so we can see it.

I assume you haven't changed any shaders/techniques from their originals.

-------------------------

dev4fun | 2018-02-13 23:47:06 UTC | #5

Ofc

	<material>
	<technique name="Techniques/DiffAlpha.xml" />
	<texture unit="diffuse" name="Textures/ricarten_Texture42.tga" />
	<parameter name="MatDiffColor" value="1 1 1 1" />
	<parameter name="MatSpecColor" value="0 0 0 2" />
	<parameter name="MatEmissiveColor" value="0 0 0 1" />
	</material>

-------------------------

Dave82 | 2018-02-13 23:55:19 UTC | #6

May i ask which exporter did you use in max? Also try png instead of tga

-------------------------

dev4fun | 2018-02-14 00:01:23 UTC | #7

Im exporting to fbx on 3ds max 2012. 
Samething with png..

-------------------------

Sinoid | 2018-02-14 00:04:44 UTC | #8

Hmmm. Alpha is working overhere.

Have you checked the bit-depth of the images (are they 8 or 16 bits-per-pixel)?

Try the `08_Decals` sample and see if it gives you similar issues. It uses alpha on the decals. Might be worth comparing that material with yours if it doesn't have issues.

-------------------------

Dave82 | 2018-02-14 00:19:44 UTC | #9

It seems like a sorting issue.I assume you export that alpha balcony thing as one mesh ? if that's the case welcome to Alpha sorting nightmare club.Since Alpha sorting is done per mesh level if you export a complex mesh as one transparent object the result will be completely unpredictable.(Faces are not distance-sorted) Try exporting each transparent element as one mesh or use DiffAlphaMask technique

-------------------------

Lumak | 2018-02-14 00:50:00 UTC | #10

Copy below block and save it as DiffAlphaMask.xml and use that **technique** instead. It renders just like diff material, just discards alpha mask.

**DiffAlphaMask.xml**
[code]
<technique vs="LitSolid" ps="LitSolid" psdefines="DIFFMAP ALPHAMASK">
    <pass name="base" />
    <pass name="litbase" psdefines="AMBIENT" />
    <pass name="light" depthtest="equal" depthwrite="false" blend="add" />
    <pass name="prepass" psdefines="PREPASS" />
    <pass name="material" psdefines="MATERIAL" depthtest="equal" depthwrite="false" />
    <pass name="deferred" psdefines="DEFERRED" />
    <pass name="depth" vs="Depth" ps="Depth" />
    <pass name="shadow" vs="Shadow" ps="Shadow" />
</technique>

[/code]
edit: it's a technique, not mat.

-------------------------

dev4fun | 2018-02-14 00:49:57 UTC | #11

This solved my problem. Thanks for ur help! :D

-------------------------

dev4fun | 2018-02-14 23:16:59 UTC | #12

Not have another way to mask be smoother?

-------------------------

Lumak | 2018-02-15 03:10:16 UTC | #13

The pass in DiffAdd.xml technique:
```<pass name="alpha" depthwrite="false" blend="add" />```
results in smoother outcome but uses Unlit shader.  There might be a way to add this to the regular Diff.xml but I haven't experimented with it.

-------------------------

