rogerdv | 2017-01-02 01:04:05 UTC | #1

Im trying to figure out how to make my items fit the attach bone more exactly, to avoid finding the correct offset and rotation, and I have a doubt about the difference between both settings in the exporter. Local means that the exported geometry has its own coordinates, starting at 0,0,0 or something like that?

-------------------------

codingmonkey | 2017-01-02 01:04:05 UTC | #2

You are using the reattiva's exporter or AssetImporter tool ?

>Local means that the exported geometry has its own coordinates
I guess local means that vertex positions will be represents as offset's from origin (pivot - in 3dmax terms) of object.

global mean that in geometry data the vertexes position will be writing as offset from global vector3(0,0,0)

but I found that some times( actually most times:) ) we need local geometry but not local Node's position settings.
for this issue i'm made cup of fixes for fork of reattiva's exporter

link: [github.com/MonkeyFirst/Urho3D-Blender](https://github.com/MonkeyFirst/Urho3D-Blender)

but before start export need setup some specific settings:
[spoiler]Select object(s) that need to export
then choice Object ->Apply -> Rotation & Scale ( not Location! this override vertex data in geometry as offset from global(0,0,0) )
then open settings set Front View = "Back" (only this work propertly, because i'm still not found the view's right matrix to mulply, currently just do swap of axis )
origin = local
object = only selected
Export Urho prefabs = True

[url=http://savepic.su/5360750.htm][img]http://savepic.su/5360750m.png[/img][/url]

setup other setting as you needed
press export
you got an Data/Scenes/%Scene%.xml named as Scene.name in Blender
in this Scene you need find Node named as "Scene" you must save it as local node to Data/Objects/ as prefab.
Well, that's all.
Use this prefab in you main scene, the nodes in it are must already placed as they placed in blender scene.[/spoiler]

-------------------------

rogerdv | 2017-01-02 01:04:05 UTC | #3

Yes, I mean Blender exporter. I think you have cleared my doubts.

-------------------------

