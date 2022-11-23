sabotage3d | 2017-01-02 01:00:53 UTC | #1

Hello ,

I am new to Urho3d, so far it is awesome.
Is there currently any support for Maya Pipeline : scene, mesh, skeletal and material information ? 
Another option would be FBX with skeletal animation or maybe Ogre3D formats ? Is any of these supported ?
If not is there any workarounds at the moment as I am currently working with Maya.

Thanks in advance,

Alex

-------------------------

friesencr | 2017-01-02 01:00:53 UTC | #2

There is support for both of those however urho will only, at runtime, use its own formats.  To convert them to urho formats there is the OgreImporter and AssetImporter command utils.  For convienience the editor has import model and import scene functions which take fbx and feed the parameters into the AssetImporter tool.  The tools are located in the Bin folder.

-------------------------

sabotage3d | 2017-01-02 01:00:53 UTC | #3

Do they support materials and animation ?
What about a whole Scene is that something only the Urho Editor is capable currently ?

Thanks,

Alex

-------------------------

sabotage3d | 2017-01-02 01:00:53 UTC | #4

Is there any documentation on the urho3d formats ?
For mesh and animation pipeline I think I will be using .mesh and .skeleton export from maya and then converting using the utils from urho3d. If Assimp supports FBX animation it would be a better pipeline, but a few months ago it wasn't great. Does the converter from Ogre3d support materials as well ?

-------------------------

cadaver | 2017-01-02 01:00:54 UTC | #5

For the file formats like models, see here: [urho3d.github.io/documentation/H ... rmats.html](http://urho3d.github.io/documentation/HEAD/_file_formats.html)

Probably the best actual documentation is the importer code itself, like AssetImporter. 

Also the Blender-exporter [github.com/reattiva/Urho3D-Blender](https://github.com/reattiva/Urho3D-Blender) may be worth studying, as it produces Urho model files directly.

-------------------------

sabotage3d | 2017-01-02 01:00:55 UTC | #6

Thanks a lot these will be helpful

-------------------------

