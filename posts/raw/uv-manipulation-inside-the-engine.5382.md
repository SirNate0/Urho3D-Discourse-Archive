suppagam | 2019-07-31 13:45:11 UTC | #1

I have been using a few prefabs from primitives, like boxes, rectangles, cylinders, etc, to prototype levels before using actual static meshes. However, some primitives look very good and I could use them in the actual game if I could assign textures to them. Unfortunately, just wrapping a material on them doesn't look very good. Is there a way to manipulate the UVs inside the engine? Kinda like the old Hammer editor, or this:

![image|640x360](https://unity3d.com/profiles/unity3d/themes/unity/images/unity/features/probuilder/probuilder-uv-controls.gif) 

![image|690x388](upload://xxUfIw9eEiWjtNwYnAdvqYdQgGs.jpeg)

-------------------------

Modanung | 2019-07-31 14:05:24 UTC | #2

Ever tried [Blender](https://www.blender.org/)? It is famous for its outstanding unwrapping capabilities.

-------------------------

S.L.C | 2019-07-31 14:08:14 UTC | #3

Yeah but you spend extra time on importing stuff back and forth.

It is a nice feature to use for tweaking models quickly. Doesn't have to be full featured. But I doubt it'll be implemented any time soon.

-------------------------

suppagam | 2019-07-31 14:53:41 UTC | #4

I do use Blender for my static meshes, but that's not really the point of the question. As I said, I'm using unwrapped prefabs and primitives for prototyping, but some of them end up looking really good, so I don't have to waste time actually doing a proper mesh for it in Blender, then going through the whole DCC flow. The only thing I need is a texture touch up inside the engine. 

That's even more useful since I tend to use lot's of trim sheets. With basic rectangular shapes and one single texture trim sheet, I can build whole levels, then just decorate with static meshes.

-------------------------

Modanung | 2019-07-31 15:03:35 UTC | #5

Did you look into custom geometry?

-------------------------

Dave82 | 2019-07-31 16:22:53 UTC | #6

I don't think there is a out of box solution for this but you can lock a vertex buffer adjust the uv data then unlock it again.

-------------------------

Leith | 2019-08-02 06:35:17 UTC | #7

Seems to me, the common shader uniforms cUOffset and cVOffset can be used to translate and rotate uv coordinates: https://discourse.urho3d.io/t/animting-uv-offsets/1355/3
I'm not really familiar with our editor, since I only recently got it to work properly, but surely we can expose these properties?

-------------------------

Sinoid | 2019-08-06 01:17:42 UTC | #8

@Leith those should already be added when creating a new material in the Editor (through the new button). If writing materials in text (or loading materials that were initially created that way) you'd have to manually add the `UOffset` and `VOffset` parameters in the GUI.

---

My proc-geometry repo has some aids:

https://github.com/JSandusky/Urho3DProcGeom/blob/master/ProcGeom/TexCoords.cpp

There's only DXUVAtlas & planar there (without rotation), but it's trivial to copy+paste the planar one and then change the mapping function (ie. cylindrical, cube, spherical, etc).

Don't forget, a lot of tools can export OBJ or another format supported by the ASSIMP importer, so you can use Quake/Half-life related tools and just determine what your material mapping is.

-------------------------

