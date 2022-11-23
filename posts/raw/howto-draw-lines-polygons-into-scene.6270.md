lama2005 | 2020-07-16 10:29:06 UTC | #1

I have modified one of the samples having an empty plane displayed and be able to move around. Now I want to display some polygons on the ground. 
Right now I am only abe to add square rectangles to the scene by using another plane. But what if the polygon isn't a square?
How can I do that?

-------------------------

restless | 2020-07-16 12:16:33 UTC | #2

Maybe you can get answer here https://discourse.urho3d.io/t/runtime-geometry-creation/337/7

-------------------------

jmiller | 2020-07-16 14:41:16 UTC | #3

Hello, and welcome to the forum! :confetti_ball:

There are some informative topics related to [lines](https://discourse.urho3d.io/search?q=lines),
  https://discourse.urho3d.io/t/procedural-geometry-helpers/4547,
  https://discourse.urho3d.io/t/a-mesh-generator/2361 ..

-------------------------

SirNate0 | 2020-07-16 16:36:52 UTC | #4

There's also [`DebugRenderer::AddPolyhedron (const Polyhedron &poly, const Color &color, bool depthTest=true)`](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_debug_renderer.html#a54e0d16a54e6d78dc721ee8c62d82a5f) which I think should allow arbitrary polygons (you could just add one face).

-------------------------

