coosadog | 2017-01-17 18:19:45 UTC | #1

I've been trying to get this right for days.  I have a lot of low poly models.  I use AssetImporter to convert them and assim does a good job for me.  But, when I put them in my scene, the material texture is all wonked up!  It's a tree with planes for the leaf areas and the image appears to be so messed up that you can't recognize it.  The only thing that's correct is it's green. Haha!  Here's what they look like:
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/1d26e1dd9e28bf98034cd0df767cca7e637b458c.jpg" width="570" height="368">

Here's my texture:
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/af2fb40ad70673e3140585a44e8a4773a5da7932.jpg" width="502" height="499">

Material:
```
<?xml version="1.0"?>
<material>
	<technique name="Techniques/DiffAlpha.xml" />
	<texture unit="diffuse" name="stp-models/vegetation/tree-basswood-medium/Textures/leaves.png" />
	<parameter name="MatDiffColor" value="1 1 1 1" />
	<parameter name="MatSpecColor" value="1 1 1 10" />
	<parameter name="MatEmissiveColor" value="0 0 0 1" />
</material>
```
My code:
```
object->SetModel(cache->GetResource<Model>("stp-models/vegetation/tree-basswood-medium/tree.mdl"));
object->SetMaterial(0,cache->GetResource<Material>("stp-models/vegetation/tree-basswood-medium/Materials/MD3__default__leaves_.xml"));
object->SetMaterial(1,cache->GetResource<Material>("stp-models/vegetation/tree-basswood-medium/Materials/MD3__default__bark_.xml"));
```

-------------------------

coosadog | 2017-01-13 19:26:47 UTC | #2

oooopsy.... I don't know how to paste the XML code.  Here's a screen shot of it:
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/30296bf5baebb727395d745758b36377c6b7cf00.png" width="690" height="106">

-------------------------

SirNate0 | 2017-01-13 19:51:05 UTC | #3

It looks like your model is missing uv coordinates. If you are exporting from blender, try using the Blender plugin [https://github.com/reattiva/Urho3D-Blender](https://github.com/reattiva/Urho3D-Blender) (I've never used Assimp, so I can't  help with that). You can also check Vertex Buffer to see if it has TexCoords (I believe you would need to check for SEM_TEXCOORD) to see if Assimp is actually exporting it correctly.

To insert xml code do surround it with three back ticks (`). To get xml formatting, put xml after the first set of backticks (this may not be necessary).

e.g. 
```
```xml
<?xml version="1.0"?>
<element>
	<attribute name="Size" value="640 480" />
	<element/>
        ...
</element>
$``` <- with no $ before those (I needed a character to keep it from closing the block)
```
Which becomes
```xml
<?xml version="1.0"?>
<element>
	<attribute name="Size" value="640 480" />
	<element/>
        ...
</element>
```

-------------------------

coosadog | 2017-01-13 21:10:56 UTC | #4

Thanks for your reply.  Assimp is the import library that AssetImporter uses.  I use it also, because I take models from different formats and convert them to Collada so that I can edit them with Equinox3D.  I don't use Blender at all.  I can export to .dae with it and then I can reimport with the one I just exported and it works fine.  Here's a screen shot:
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/5abcfbd13ffa53d6c43a8e746421d65f141b0010.jpg" width="542" height="408">
I convert the .dae to .mdl with AssetImporter.  I can't look at the .mdl because it's binary format.  I've never had this problem before and I use this model in another game engine.

-------------------------

SirNate0 | 2017-02-14 15:54:11 UTC | #5

Were you able to resolve your issue? If not, I would suggest querying the model in the code to make sure it has the needed UV coordinates (yes, annoying, but probably less than just looking at the model in a hex editor). Other than that my only suggestions are to try importing to blender and exporting to Urho through that, or perhaps try importing the mdl file instead of the dae... perhaps AssetImporter would play nicer with it.

-------------------------

