lheller | 2018-11-03 10:17:20 UTC | #1

Hello

Does anybody know, how to create a sphere using **CustomGeometry** then add textures on the **inner** surface of sphere (camera would be also inside) and finally paint anythig on the textures?

-------------------------

jmiller | 2018-11-03 15:43:26 UTC | #2

Hello,

I guess you have reason not to prefer StaticModel.. [**edit:** so I maybe should not get into that yet]
You may have referenced CustomGeometry docs section and sample program, and some CustomGeometry posts and (CSG) tools on the forum..

I've learned a lot studying others' code and there seem to be some interesting articles, e.g. [url=https://duckduckgo.com/?q=C%2B%2B+icosphere]C++ icosphere[/url] generation and UV-mapping, and am curious what others in this bright community might have to say.

-------------------------

Bananaft | 2018-11-04 14:01:57 UTC | #3

If you want to draw inside of a shape you just flip it's normals, or switch culling mode in material properties.

If you want inside and outside show different textures, you have to have two separate meshes with different materials and different culling methods.

-------------------------

Modanung | 2018-11-04 14:24:51 UTC | #4

...and for a sphere constructed around the origin (x == y == z == 0) outward facing normals equal the normalized vertex position. Negated they will face inward.

-------------------------

lheller | 2018-11-06 18:53:02 UTC | #5

Thanks for replies, guys!

At the end I solved it this way:
1. Created/exported a sphere model in [SketchUp](https://app.sketchup.com/app?hl=en) application (DAE format).
2. Using asset imported tool I converted the model from previous step.
3. Imported that model into a StaticModel component and set cull mode for its material to "None".
4. Using raycast/decals I also was able to paint on the inner surface.

-------------------------

Modanung | 2018-11-06 19:47:39 UTC | #6

I've you're going down _that_ path: Have you considered using [Blender](https://www.blender.org/) together with the [Urho3D add-on](https://github.com/reattiva/Urho3D-Blender)?

-------------------------

