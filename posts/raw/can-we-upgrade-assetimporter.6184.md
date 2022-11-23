throwawayerino | 2020-05-30 14:07:50 UTC | #1

Current version can't import blender 2.8 files but I'm not sure if the newer ones can either. Older versions of blender do work and it's really nice to just drop a blend file on it and get a model.
My current workaround is to export to Collada/FBX and pass that to assimp. It eventually works most of the time, but it's very tiring to pass around files

-------------------------

elix22 | 2020-05-31 05:54:53 UTC | #2

I have a more recent Assimp implementation in my private branch 
Assimp doesn't work well with Blender files .

https://github.com/elix22/Urho3D/tree/dev-flimper/Source/ThirdParty/Assimp


I have written several python blender conversion scripts ,using them as part of an automated conversion process, might be helpful to your conversion process .
Can be found in :
https://github.com/elix22/Urho3D/tree/dev-flimper/FlimperAssets/Python

Example :
blender.exe  blender_file.blend  --background --python convert_blend_to_dae.py  --dae_file.dae

-------------------------

throwawayerino | 2020-06-01 15:52:27 UTC | #3

Here's the issue:
https://github.com/assimp/assimp/issues/2559
As I've said before, exporting to fbx and passing that to assimp fixes it

-------------------------

