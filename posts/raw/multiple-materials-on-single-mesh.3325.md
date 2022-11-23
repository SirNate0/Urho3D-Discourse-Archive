ChunFengTsin | 2017-07-05 15:22:48 UTC | #1

I know this is pretty basic, but I can't seem to figure out how to get it working. I created a simple room mesh in blender with different materials (each having it's own texture) for the walls, floor, and ceiling. I'm using the Urho3D-Blender Exporter to export and generate an .mdl for the room's mesh, and it generates materials and textures for the room.

If I only use one I can get the material/texture to work. If I use more than one, only material is visible (the ceiling) and the rest of the mesh is the blank default material. Not sure what I'm doing wrong. Or if I'm making an incorrect assumption in thinking a single .mdl can have multiple materials.

-------------------------

Alex-Doc | 2018-01-26 11:23:54 UTC | #2

Have you set the StaticModel Material parameters?
IIRC the materials have to be set as list in the StaticModel component:

[code]
<attribute name="Material" value="Material;Materials/first.xml;Materials/second.xml" />
[/code]

A more complete example/prefab:

[code]
<?xml version="1.0"?>
<node id="124">
    <attribute name="Is Enabled" value="true" />
    <attribute name="Name" value="Example" />
    <attribute name="Tags" />
    <attribute name="Position" value="0 0 0" />
    <attribute name="Rotation" value="0.935595 0 -0.353083 0" />
    <attribute name="Scale" value="1 1 1" />
    <attribute name="Variables" />
    <component type="StaticModel" id="1234">
        <attribute name="Model" value="Model;Models/MyModel.mdl" />
<!-- here we set the material list -->
        <attribute name="Material" value="Material;Materials/Pink.xml;Materials/Blue.xml" />
<!-- -->
        <attribute name="Cast Shadows" value="true" />
    </component>
</node>
[/code]

-------------------------

rasteron | 2017-07-05 20:44:03 UTC | #3

[quote="ChunFengTsin, post:1, topic:3325"]
Not sure what I'm doing wrong. Or if I'm making an incorrect assumption in thinking a single .mdl can have multiple materials.
[/quote]

Of course you can set multiple materials and also use a material list, having a quick test with the exporter I don't see any problems here.

I suggest doing a simple test with just a few textures so you can easily check and fix your export issues.

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/43759e253be06e4fb8be46999dd2ac74611cb9a5.png" width="690" height="369">

-------------------------

ChunFengTsin | 2017-07-06 03:07:26 UTC | #4

yes , I have make a lowpoly model in blender ,export as obj format, then import to urho3d-eidtor, and last save scene.
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/beae8b67b522378b1ca07660ef3d49f7920fc79f.png" width="690" height="388">

-------------------------

ChunFengTsin | 2017-07-06 03:15:27 UTC | #5

I've  made it with urho-editor ，then I open the scene xml file ,
 as you said：
`<attribute name="Material" value="Material;Materials/Stone.xml;Materials/Ground.xml;Materials/Snow.xml" />`
 but I don't know  how the points of model find the material correctly?

-------------------------

1vanK | 2017-07-06 03:26:50 UTC | #6

In blender enable "Export materlas > Materials text list"
In game use staticModel->ApplyMaterialList()

-------------------------

rasteron | 2017-07-06 03:38:56 UTC | #7

[quote="ChunFengTsin, post:4, topic:3325"]
yes , I have make a lowpoly model in blender ,export as obj format, then import to urho3d-eidtor, and last save scene. but I don't know  how the points of model find the material correctly?
[/quote]

Both tools ([Blender](https://github.com/reattiva/Urho3D-Blender)/AssetImporter) does this for you automatically, but if you need to make some tweaks, this is how it should look like in your xml scene file

    <component id="xxx" type="StaticModel">
     	<attribute name="Model" value="Model;Models/Ball.mdl"/>
        <attribute name="Material" value="Material;Materials/sphere.xml;Materials/suzanne.xml;Materials/cube.xml"/>
    </component>

Again, if you export your multiple materials correctly even without the textures, the editor/engine will detect the model and supply you with empty fields to fill it out and set your materials/textures.

-------------------------

Modanung | 2020-02-12 05:14:00 UTC | #8

[quote="ChunFengTsin, post:5, topic:3325"]
but I don't know  how the points of model find the material correctly?
[/quote]

In Blender you can sort elements by material. This option can be found in edit mode in the _Mesh_ menu. The upshot of which is that the geometries in Urho will have the same order as the material slots in Blender.

-------------------------

