codingmonkey | 2019-07-25 14:15:11 UTC | #1

Hi folks, it's again me )
I'm trying to figure out how to use lightmaps.
I have 10 objects, each has its own unique diffuse texture.
And each objects have two UV-channels (pos, norm, ... uv1, uv2). First uv1 for own unique diffuse and second uv2 for ligthmap texture. 
This lightmap is one big texture, it's baked in blender for all scene ( 10 objects:) )

What technique should I choose in material editor and how to setup material to render all this objects with one lightmap for all ?

-------------------------

cadaver | 2019-07-25 14:15:01 UTC | #2

Choose the DiffLightMap.xml technique, put diffuse texture normally to diffuse slot, and the shared lightmap texture to emissive slot. You'll need unique materials for each object because of the different diffuse texture.

-------------------------

codingmonkey | 2017-01-02 01:01:20 UTC | #3

Thank, [b]cadaver[/b].

I'm still not good at Urho3D.
So also wanted to ask how I can set the texture offset (not tiling) of any material, but I recently found myself this option ) 
This is the last value in the parameters U(V)Offset Vector, in material editor.

-------------------------

