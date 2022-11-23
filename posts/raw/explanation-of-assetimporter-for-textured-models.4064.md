adrianimajion | 2018-02-28 01:15:34 UTC | #1

Hello,

My question is similar to this [existing one](https://discourse.urho3d.io/t/how-to-import-models-with-texture-images/2744) but the answers there didn't really help me. I'm trying to figure out the asset importer and I'm not understanding something basic about importing textures. I can import models, but only with the default white lambert texture.

If I download an FBX model with an included PNG texture, how do I generate an Urho prefab or model that applies that texture as a material? I'm able to generate a single RootNode model from an FBX, or a prefab of nodes, but I can't determine how define what texture or material to be imported alongside. Sorry if this question is too basic, but what I could really use is just a bullet point explanation of exactly how to import a model and texture into Urho as a textured prefab using the command line tool.

-------------------------

jmiller | 2018-02-28 03:04:53 UTC | #2

I'll leave AssetImporter use to those who know it, but you might want to be aware of the most excellent Urho3D-Blender :)
https://github.com/reattiva/Urho3D-Blender

-------------------------

adrianimajion | 2018-02-28 14:41:34 UTC | #3

Thanks, I came across this in my research and at the moment I'm depending on it for importing properly formatted assets, but I have a lot of resources not built in Blender I'd like to make use of. Thanks for the help, hopefully the AssetImporter experts arrive soon :stuck_out_tongue:

-------------------------

Lumak | 2018-03-01 01:08:27 UTC | #4

Weitjong updated assimp to v 4.0.1 about five months ago, and that'll export embedded textures automatically. Got the latest Urho3d master branch, importe the claire.fbx file from Mixamo and verified that's actually the case.

~~edit: add the below to AssetImporter.cpp, line 516 - required if you're not using the -np option.~~
```
            aiSetImportPropertyInteger(aiprops, AI_CONFIG_IMPORT_FBX_READ_TEXTURES, 1);                  //defualt = true;
```
disregard adding that line.

-------------------------

johnnycable | 2018-03-01 09:51:26 UTC | #5

Be wary that what follows is related to Blender, I've never used Maya.
I use asset importer for Blender to Urho pipeline, together with Reattiva addon for fast prototyping.
As a rule of thumb, I try with the addon first, so I can see if it's a fault on my asset part; if the addon works, I have a good asset.
Aside from asset structure, while importing from my Blender files I've noticed texture skipping in case my images are not embedded into the Blender file. To amend that, I've resolved with forcing embedding before export. So for starters I'd check with this...
Having found a fix I didn't explored the problem any further...

-------------------------

