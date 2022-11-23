burgreen | 2017-09-27 01:23:29 UTC | #1

I converted an STL to MDL format. Once I import the model, how do I render with flat shading instead of the smoothed shading?

-------------------------

godan | 2017-09-27 01:23:37 UTC | #2

Use AssetImporter with -h switch? Haven't tested it....

```
AssetImporter model Path/To/Stl MyMDL.mdl -h
```

More generally, you can get the flat shaded effect by duplicating the vertices of each triangle (i.e. index buffer and vertex buffer are parallel) OR messing around with shaders.

-------------------------

Modanung | 2017-09-27 00:14:56 UTC | #3

You could use [Blender](http://blender.org) to split the edges and export to MDL using the [reattiva plugin](https://github.com/reattiva/Urho3D-Blender).

And welcome to the forums! :slight_smile:

-------------------------

burgreen | 2017-09-27 01:20:49 UTC | #4

-h worked perfectly. I did not want to mess around with shaders.

-------------------------

