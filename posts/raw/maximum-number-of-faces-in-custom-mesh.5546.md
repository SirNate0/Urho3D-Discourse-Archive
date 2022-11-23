sergeyv | 2019-09-03 17:22:57 UTC | #1

Trying to apply Urho to 3D CAD,  complex 2D polygons with many holes  in 3D become complex meshes  with large number of faces. 
Looks like there is some limit for maximum number of faces in custom mesh . 
Meshes with 20-30K faces  work fine.  Meshes with 200-300K faces are displayed as broken mesh.  And larsgest mesh in my tests so far is 1.6M faces 
Usually large meshes are extruded 2D polygons so I can use Clipper to break them into parts and make every part as separate mesh.  
But is there any recommended values ?

-------------------------

Dave82 | 2019-09-03 17:23:04 UTC | #2

Are you using a CustomGeometry component ? I don't know much about this component but in Urho indices are 16 bit so this limit you to 64k faces per mesh. If you're using Geometry and index/vertex buffers then you have to set your index buffer to support large indices (32 bit indices) 
[code]
indexBuffer->SetSize(unsigned indexCount, bool largeIndices, bool dynamic = false);
[/code]
by setting the [b]largeIndices[/b] flag to true

-------------------------

sergeyv | 2019-09-03 14:38:16 UTC | #3

**largeIndices = true** helps.  Thanks a lot !

-------------------------

