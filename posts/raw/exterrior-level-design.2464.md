slapin | 2017-01-02 01:15:34 UTC | #1

Hi, all!

As I see there's no accessible way to create heightmap terrains in Urho, I want to just use Blender for the whole scene
export. The scene is just ground, grass, trees and some water. I just want direct approach, i.e. I just do .xml/.mdl export
in Blender and do not touch it in editor but just set necessary stuff from code (utilizing some naming conventions).
So the basic question is - will I have a lot of trouble with this setup for medium/large scenes (2048x2048 units of landscape
attached in chunks of 9)? If that is not effective, could one suggest a workflow which would allow fluent
level design?

-------------------------

rasteron | 2017-01-02 01:15:34 UTC | #2

Hey slapin,

Have you tried JTippet's Terrain Editor?

[discourse.urho3d.io/t/terrain-editor/765/1](http://discourse.urho3d.io/t/terrain-editor/765/1)
[github.com/JTippetts/U3DTerrainEditor](https://github.com/JTippetts/U3DTerrainEditor)

-------------------------

jmiller | 2019-05-18 15:05:14 UTC | #3

Blender and Urho seem to handle Terrain at 2048+ for me.

[Ant Landscape](https://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Add_Mesh/ANT_Landscape) for Blender is powerful.

Blender method to create and manipulate height maps by linking to a plane and rendering as greyscale:
  http://blender.stackexchange.com/questions/9030/create-and-manipulate-height-map-save-as-greyscale-texture

-------------------------

slapin | 2017-01-02 01:15:34 UTC | #4

Well, I really understand how to make heightmap but I want to have stuff placed, i.e. grass, trees, debris,
texture paint the whole thing...
I can do this in Blender, but that effectively prevents using of heightmap. So I wonder how bad that will be,
and is there some combined workflow to produce whole landscape (heightmap + stuff) effectively?

I'm looking at JTippetts' terrain editor to see if that is what I need.

-------------------------

jmiller | 2017-01-02 01:15:35 UTC | #5

I see, you want to use the Terrain collisionshape in editing.

How about in Blender, moving or locking objects' Z origins to to the plane/terrain, assuming one can match the terrain scale? I have not tried that yet.

-------------------------

