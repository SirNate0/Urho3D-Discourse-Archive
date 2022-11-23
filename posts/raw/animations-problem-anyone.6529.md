grokko | 2020-11-17 00:34:36 UTC | #1

Hi Gang,
   My missions so far have been very successfull...I have 64 daleks all chasing me on the terrain geomipmapped model you have....My question is this? How do I import a basic Blender animation in, say, 'fbx' format?

I do the animation in Blender in the minimalist scale, and AssetImporter gives me this, where the model animations name is - 'test.fbx'...

test.fbx 34k
test.mdl 3.7k
test_CubeCameraAction.ani 84 bytes
test_CubeCubeAction.001.ani 8k
test__CubeCubeAction.ani 28 bytes

I choose the 8k .ani file in the code, but no action....Is there a trick here?

Lord Fiction

-------------------------

JSandusky | 2020-11-17 04:05:15 UTC | #2

Put your Ani file somewhere it can be downloaded. If it's an object animation the problem is usually the level in the tree where you apply it. The file contains names that tell you the subtree it expects so if you want to check it yourself you can just set breakpoints during the read and look at the names when the ani file is loaded. Odds are that you're applying the animation either too low or too high in the tree.

-------------------------

johnnycable | 2020-11-17 15:51:08 UTC | #3

Had lot of problem with blender -> fbx something -> asset importer. You're probably much better served using the blender exporter to urho...

-------------------------

