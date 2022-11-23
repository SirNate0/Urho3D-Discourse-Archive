OMID-313 | 2017-01-24 14:12:08 UTC | #1

Hi all,

I'm using Urho3D on Raspberry Pi 3.
Up to now, I've been able to import simple 3D models with simple materials (color, ...), with the following command:

`./AssetImporter model /path/to/mymodel.obj /path/to/mymodel.mdl -l`

Since I work with 3Ds Max, usually I export .obj (and .mtl) file from it, so as to be imported to Urho3D.

Now I want to import models that have image textures. But the above command doesn't help.

Any suggestions !?

-------------------------

dakilla | 2017-01-24 17:10:09 UTC | #2

I don't know for 3DS MAX but for Blender when I create internally a new material with textures (diffuse, normal, etc...) and export the model (.fbx), using AssetImporter with the model command create correctly Materials and Textures directories with inside Material.xml and textures images. (just need to edit  the Material.xml to adjust textures path depending where you want to put them). 

Does your Material and Textures dir are created when using AssetImporter ?

-------------------------

OMID-313 | 2017-01-25 05:48:42 UTC | #3

Thanks @dakilla for your reply.
You mean the same command should work even for textured materials !?

`./AssetImporter model /path/to/mymodel.obj /path/to/mymodel.mdl -l`

-------------------------

dakilla | 2017-01-25 06:01:02 UTC | #4

Yes it export model, materials and textures.
note : I don't use -l option.

-------------------------

