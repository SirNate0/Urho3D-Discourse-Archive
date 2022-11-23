gasp | 2017-01-02 00:58:52 UTC | #1

I have a blender file containing a model with texture ,UV Diffuse texture (see screenshoot).
I try to export it to mdl / material and texture, model .mdl is fine, but can't get the correct material, texture.

what i've tried :
=> Export from blender Exporter, model fine, material created but with technique "notexture"
=> use the "import model" inside the editor with the blender 2.7 RC1 file format , no error message, no file


I tried AssetImporter :
 *  From Blender format, no success (see log below)
 *  From Collada dae format ( export in blender) , succes (see log)

If i set the technique Diff and point to the uv file in the editor, all is good in the editor, but why did the editor import, assetImporter and urho3d exporter didn't find the texture ?

realtime update from file in the editor is really cool :p


Here are my blender, and the editor material screen screen shoot :
[url=http://www.hostingpics.net/viewer.php?id=400335textureError.png][img]http://img4.hostingpics.net/thumbs/mini_400335textureError.png[/img][/url]
Here are the screen in the editor when i correct the material :
[url=http://www.hostingpics.net/viewer.php?id=116021Corrected.png][img]http://img4.hostingpics.net/pics/116021Corrected.png[/img][/url]
Blender format :
[code]Reading file Low Poly Ninja.blend
Info,  T4092: Load Low Poly Ninja.blend
Debug, T4092: Assimp 3.0.1270 x86 gcc noboost singlethreaded
Info,  T4092: Found a matching importer for this file format
Info,  T4092: Import root directory is '.\'
Info,  T4092: BLEND: Blender version is 2.70 (64bit: true, little endian: true)
Debug, T4092: BlenderDNA: Got 556 structures with totally 6435 fields
Warn,  T4092: BlendDNA: Did not find a field named `angle` in structure `Camera`

Warn,  T4092: BlendDNA: Did not find a field named `mat_nr` in structure `MVert`

Skipping one or more lines with the same contents
Info,  T4092: (Stats) Fields read: 92545, pointers resolved: 40, cache hits: 222
3, cached objects: 22
Error, T4092: BLEND: Number of UV faces is larger than the corresponding UV face
 array (#1)
Could not open or parse input file Low Poly Ninja.blend
[/code]

Asset Importer from collada file format : 
[code]

Reading file Low Poly Ninja.dae
Info,  T3236: Load Low Poly Ninja.dae
Debug, T3236: Assimp 3.0.1270 x86 gcc noboost singlethreaded
Info,  T3236: Found a matching importer for this file format
Info,  T3236: Import root directory is '.\'
Debug, T3236: Collada schema version is 1.4.n
Info,  T3236: Entering post processing pipeline
Debug, T3236: RemoveRedundantMatsProcess begin
Debug, T3236: RemoveRedundantMatsProcess finished
Debug, T3236: FindInstancesProcess begin
Debug, T3236: FindInstancesProcess finished. No instanced meshes found
Debug, T3236: Skipping OptimizeMeshesProcess
Debug, T3236: GenUVCoordsProcess begin
Debug, T3236: GenUVCoordsProcess finished
Debug, T3236: TriangulateProcess begin
Debug, T3236: TriangulateProcess finished. There was nothing to be done.
Debug, T3236: FindInvalidDataProcess begin
Debug, T3236: FindInvalidDataProcess finished. Everything seems to be OK.
Debug, T3236: FixInfacingNormalsProcess begin
Debug, T3236: FixInfacingNormalsProcess finished. No changes to the scene.
Debug, T3236: Generate spatially-sorted vertex cache
Debug, T3236: GenVertexNormalsProcess begin
Debug, T3236: GenVertexNormalsProcess finished. Normals are already there
Debug, T3236: JoinVerticesProcess begin
Debug, T3236: Mesh 0 (Cube.006) | Verts in: 13308 out: 3290 | ~75.278%
Info,  T3236: JoinVerticesProcess finished | Verts in: 13308 out: 3290 | ~75.3%
Debug, T3236: MakeLeftHandedProcess begin
Debug, T3236: MakeLeftHandedProcess finished
Debug, T3236: FlipUVsProcess begin
Debug, T3236: FlipUVsProcess finished
Debug, T3236: FlipWindingOrderProcess begin
Debug, T3236: FlipWindingOrderProcess finished
Debug, T3236: LimitBoneWeightsProcess begin
Debug, T3236: LimitBoneWeightsProcess end
Debug, T3236: ImproveCacheLocalityProcess begin
Debug, T3236: Mesh 0 | ACMR in: 2.353922 out: 0.890442 | ~62.2%
Info,  T3236: Cache relevant are 1 meshes (4436 faces). Average output ACMR is 0
.890442
Debug, T3236: ImproveCacheLocalityProcess finished.
Info,  T3236: Leaving post processing pipeline
Writing model Scene
Writing geometry 0 with 3290 vertices 13308 indices
Writing material Low_Poly_Ninja-material
[/code]

material file is created

-------------------------

friesencr | 2017-01-02 00:58:52 UTC | #2

For animated models I highly recommend the urho plugin for blender.  This little gem has saved me so much time and pain.

[github.com/reattiva/Urho3D-Blender](https://github.com/reattiva/Urho3D-Blender)

Exporting animations can take a little getting used to.  I only have problems with this plugin when I have more then 3 weights on a vertex and when I my models have to be all quads.

-------------------------

gasp | 2017-01-02 00:58:52 UTC | #3

I've the same problem with this Urho 3D exporter

-------------------------

reattiva | 2017-01-02 00:58:53 UTC | #4

The Urho3D-Blender exporter supports the Blender Render engine only. There is a warning about this in your screenshot.

-------------------------

