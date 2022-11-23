Jens | 2021-06-29 11:37:48 UTC | #1

Hi - I have a cube with a single bone, named 'Bone', parented. If no weights have been applied, then the bone is ignored by AssetImporter, even though there are command parameters for including non-skinning bones:

```
AssetImporter_Win64.exe node acube.fbx prefab.xml -s "Bone" -v
```

The bone is exported by the fbx Blender exporter, and can be seen in prefab.xml. That is why I think it might be a problem with AssetImporter (or how I'm using it).

Thing is, I need a character to grab onto another model, say a large tray, using (point) Constraints. The only apparent way to do this is to constrain the finger bone of the character to a non-deforming bone positioned correctly in the tray. This is impossible if weights are applied to the tray, as it just deforms.

I'm reasonably new to Urho, so may well be incorrect in how to constrain the two objects - any pointers much appreciated.

-------------------------

GodMan | 2021-07-09 17:33:06 UTC | #2

Try using .mdl instead of xml. I use bones or nodes with zero weights all the time using Assetimporter and have no issues.

-------------------------

Lumak | 2021-07-13 00:15:59 UTC | #3

I was curious about this and duplicated this process, and debugging it turns out that Assimp (third party lib) returns node structure with models and the bone count was shown as zero. So, you're doing the import correctly by using the "node" command, and it's not necessary to add -s at the end.

-------------------------

Jens | 2021-07-13 10:17:22 UTC | #4

[quote="GodMan, post:2, topic:6905, full:true"]
Try using .mdl instead of xml. I use bones or nodes with zero weights all the time using Assetimporter and have no issues.
[/quote]

Ok thanks, I tried with: 
```
AssetImporter_Win64.exe model shield.fbx  shield.mdl -v
```
Again, no bone structure was shown in the AssetImporter output, and the Skeleton had zero bones in Urho. 
There was only a single bone in the armature, maybe when you use zero weight bones they are connected to other weighted bones?
Otherwise, am not sure why this is failing, maybe a different ver. of AssetImporter?  Mine is:
```
 Assimp 4.0.236295976 amd64 msvc singlethreaded
```

-------------------------

Jens | 2021-07-13 10:24:38 UTC | #5

[quote="Lumak, post:3, topic:6905, full:true"]
I was curious about this and duplicated this process, and debugging it turns out that Assimp (third party lib) returns node structure with models and the bone count was shown as zero. So, you’re doing the import correctly by using the “node” command, and it’s not necessary to add -s at the end.
[/quote]

Thanks. To double-check, you can neither import an armature through Assimp fbx import if it only contains non-weighted bones?

-------------------------

Nerrik | 2021-07-13 18:36:01 UTC | #6

Exporting / Importing any gamemodels with bones and animations with the original FBX Import/Export can be a huge messup with Blender, especially if you want to use it with AssetImporter.

Best result for my models was this Setup:
![blender_fbx|690x368](upload://1Neo9UGpc2r1thPWoWxc46oLaPw.jpeg)

I would recommend to use the "better FBX Importer/Exporter" from

[https://blendermarket.com/products/better-fbx-importer--exporter](https://blendermarket.com/products/better-fbx-importer--exporter)

It`s using the original FBX librarys and with the right settings it works like a charm.

My testsettings with this for export are:

![blender_better|690x373](upload://jc3pyQVqtwZzcXvWesMT91CyPE2.png)

-------------------------

Jens | 2021-07-14 21:43:46 UTC | #7

[quote="Nerrik, post:6, topic:6905"]
I would recommend to use the “better FBX Importer/Exporter” from
[/quote]
Thanks for that information. It would then appear that there is a problem in the Blender default FBX exporter.

-------------------------

