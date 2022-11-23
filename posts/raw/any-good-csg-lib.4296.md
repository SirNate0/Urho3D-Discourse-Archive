esakylli | 2018-06-08 07:04:44 UTC | #1

Does anyone know of any good, easy-to-use CSG lib out there?
In a first step I just want to subtract (difference) a sphere from a box.
Preferably a lib that could easily be integrated into Urho3D.

-------------------------

johnnycable | 2018-06-08 14:11:45 UTC | #2

Have a look at [PyMesh](http://pymesh.readthedocs.io/en/latest/index.html#). It's a python wrapper over a number of such C++ libraries. Check the docs. Integration should be easy as every of them is managed as cmake project.

EDIT: possibly CSG afaik are carve and cork.

-------------------------

slapin | 2018-06-08 11:10:29 UTC | #3

Can I hijack your topic and ask for good C or C++ CSG library with permissive license (like MIT, BSD, Zlib)?
Bad library with above conditions are fine too though...

-------------------------

johnnycable | 2018-06-08 14:13:08 UTC | #4

http://www.openscad.org/

-------------------------

dakilla | 2018-06-08 16:03:03 UTC | #5

You could use the godot implementation.
I'm also looking for a csg library for a near future...

[article : Godot gets CSG support](https://godotengine.org/article/godot-gets-csg-support)

[code : godot csg module](https://github.com/godotengine/godot/tree/master/modules/csg)

-------------------------

esakylli | 2018-06-11 07:33:57 UTC | #6

Thanks for the pointers!

I also found this javascript lib:
https://evanw.github.io/csg.js/

And a C# port of it:
https://github.com/johnmott59/CGSinCSharp

I'm thinking of giving the C# lib a try (because I'm using C# with UrhoSharp).

-------------------------

Numerator | 2018-06-14 23:13:14 UTC | #7

I think that blender uses carve

https://code.google.com/archive/p/carve/downloads

-------------------------

rku | 2018-06-15 05:17:26 UTC | #8

I experimented with cpp port of csgjs: https://github.com/rokups/Urho3D/commits/feature/CSG
But csgjs is slow, you most likely do not want to use that code. I would work on porting godot's implementation. It is so much faster.

-------------------------

