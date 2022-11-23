TikariSakari | 2017-01-02 01:03:41 UTC | #1

I was wondering if it would be possible to import empty nodes from blender file? I have used the path blender -> collada -> urho with assetimporter, and it seems to strip away all empty nodes. If I try to add mesh with no vertex or only one vertex, it also takes that away as well.

I would like to use blender as a world editor, so adding stuff like spawning points etc. would be quite nice feature, but currently I cannot figure out a way to do so. As for using collada exporter, from my testing, it seems to be working the best for importing scenes from blender.

-------------------------

cadaver | 2017-01-02 01:03:41 UTC | #2

This should be doable. However the only information you get out of the assimp node is the pos/rot/scale, and name. So you would likely have to encode "meaning" like spawnpoint into the node name.

-------------------------

TikariSakari | 2017-01-02 01:03:41 UTC | #3

[quote="cadaver"]This should be doable. However the only information you get out of the assimp node is the pos/rot/scale, and name. So you would likely have to encode "meaning" like spawnpoint into the node name.[/quote]

That would definitely work. Using some naming conventions to encode the meaning like you said, such as: "Spawn_Player_01", then going through whole scene hierarchy and doing some pattern matching to find all the possible spawn points.

-------------------------

