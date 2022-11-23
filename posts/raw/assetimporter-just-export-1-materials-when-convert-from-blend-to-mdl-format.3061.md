redmouth | 2017-04-28 14:50:52 UTC | #1

There are 2 materials in the blender model, but with the following command executed, 
**AssetImporter model input.blend out.mdl**
only 1 material named TerrainV2 is saved, the other is missing.

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/ff817cef92185d59a01c40d12020cb8de346b65c.png" width="326" height="399">

-------------------------

Florastamine | 2017-04-28 10:51:17 UTC | #2

Have you tried using the [Blender to Urho3D mesh exporter](https://github.com/reattiva/Urho3D-Blender)? Someone recommended the plugin to me quite a while before and it turned out to be working pretty well.

-------------------------

slapin | 2017-04-28 11:19:52 UTC | #3

I never had any success with AssetImporter on .blends.
Use Blender exporter plugin. The only other path is using .fbx.

-------------------------

rasteron | 2017-04-28 11:27:56 UTC | #4

Yes, it will be much easier if you would just either use reattiva's Blender exporter or export it first to Blender FBX and then with AssetImporter.

-------------------------

redmouth | 2017-04-28 13:58:06 UTC | #5

Thanks for all of your advice. :grin:

-------------------------

