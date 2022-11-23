darkirk | 2017-04-29 13:56:22 UTC | #1

Has anyone used voronoi to do realtime mesh deformation and fracturing in Urho3D? How would you guys do it? 

https://www.assetstore.unity3d.com/en/#!/content/9411

Right now, i'm doing everything by hand: i create a normal mesh, then a fractured one in Blender, and then when the damage is higher than X, i swap the meshes and play a baked animation.

-------------------------

slapin | 2017-04-29 14:01:14 UTC | #2

I think the way you do it is the most practical one.
How do you bake animation for fracturing for Urho?

-------------------------

darkirk | 2017-04-29 14:03:27 UTC | #3

It is practical, but it sucks for the player: everything he blows up a box or something, the same pieces go to the same places. Also, the pieces are not affected by physics, so they go through walls and everything. I have to carefully place everything. 

https://www.youtube.com/watch?v=38eEZyNfd3A
https://www.youtube.com/watch?v=uXEk0dp79ik

-------------------------

S.L.C | 2017-04-29 18:29:16 UTC | #4

Bullet physics seems to [have something similar](https://github.com/bulletphysics/bullet3/tree/master/examples/VoronoiFracture) but you'll have to port it to Urho3D in order to use it. Probably not much but it's a start.

-------------------------

darkirk | 2017-04-29 18:38:46 UTC | #5

Isn't Urho already integrated with Bullet?

-------------------------

TheComet | 2017-04-29 20:30:33 UTC | #6

Yes but Urho only wraps the collision and rigidbody systems.

-------------------------

darkirk | 2017-04-29 20:39:14 UTC | #7

Is there a tutorial on how to integrate other parts?

-------------------------

TheComet | 2017-04-29 23:30:01 UTC | #8

I'm not aware of any tutorials on that, but my best advice is to just read the source code and try. The community helps you a lot if you have specific questions.

-------------------------

slapin | 2017-04-30 01:25:20 UTC | #9

Well, some people implement fracturing using particles. Also you can add variation using separate animations, and use some raycasts to prevent wall passing (but this might use some CPU).

-------------------------

haolly | 2018-01-24 12:57:22 UTC | #10

I have used the Exploder Unity plugin, seems it use https://github.com/jhasse/poly2tri  library to cut polygons.
So, If U can obtain the mesh data, and do something on it, which is beyond my knowledge :no_mouth:

-------------------------

Enhex | 2018-01-26 00:00:50 UTC | #11

Games like Half-Life 2 just spawn few pre-defined "piece" models, usually with some explosion to hide the switching from the intact model to its pieces.

-------------------------

johnnycable | 2018-01-26 09:52:40 UTC | #12

Why don't you simply creates five other more "destroyable" animations and mix between them? Consider that, unless yours a game for happy destructors, most player probably won't even notice...

-------------------------

Sinoid | 2018-01-26 19:39:39 UTC | #13

The license on the Carve library was changed to MIT by the original author, [his github repo for CarveCSG](https://github.com/folded/carve) is easy to miss since the top google result is an old fork by someone else. It's pretty weird to work with, so getting the results you want can be a bit of trial and error.

There's [Alembic](https://github.com/alembic/alembic) for baking simulation results - it's practically made for the cooked demolition scenario, though it's almost as nasty to compile as [OpenVDB](http://www.openvdb.org/) (which can do fracture as well if voxelizing is okay) is.

The talk on [Rainbox Six: siege's destruction](https://www.youtube.com/watch?v=SjkQxowsL0I) is also on youtube - it's pretty simple.

-------------------------

rku | 2018-03-08 10:45:35 UTC | #14

@Sinoid any idea whats the performance of Carve lib? Is it useable realtime?

-------------------------

Sinoid | 2018-03-08 12:51:03 UTC | #15

@rku anywhere between 200ms - 500ms for Carve, on a potato Surface Pro 1st gen. Fast enough to appear real-time when threaded (which is the case where I got all of these measurements).

- 4500 triangles **minus** 12 triangle cube
    - That's actually 3 ops (A-B, B-A, A u -B)
- Ran in C++/CLI in actual CLI code for most of the intermediary ... so not exactly a rocket
- Measured via System::Diagnostics::Stopwatch
    - Not the most accurate thing
- Includes the time to build the vertex data and then translate the results back into something renderable
    - Carve uses a table based storage for attributes of vertices/edges/faces, so that's quite a bit of workload
    - Preparing the mesh takes: ~145ms
        - Canonicalize
        - Fill buffers
        - Difficult for me to actually measure as I do cache the half-edge mesh used for canonicals
    - Extracting the mesh takes: ~16ms

So, as a threaded work item yes. Keeping all of the intermediate Carve specific data should be enough to make the difference between usable and not usable.

-------------------------

rku | 2018-03-08 13:17:06 UTC | #16

Thank you very much for taking time to do the test! While not the rocket it isnt too slow either. With some trickery like mentioned in R6:S talk you posted it can be totally realtime.

-------------------------

Sinoid | 2018-03-08 14:49:26 UTC | #17

No problem, I kept all the Carve code around even though I ended up rolling my own CSG.

---

It certainly makes sense as part of a solution. I wouldn't use it for something simple like subway-columns or a heightfield/planar slice.

The planar blocks from the R6:S edge talk have the huge advantage that it's trivial to generate a decal skirt for those, with vanilla CSG that's an additional intersection and the output is triangle-soup so it means looking at edge connectivity to figure out UVs - which doesn't sound like fun.

-------------------------

TheComet | 2018-05-30 11:01:46 UTC | #18

[quote="Sinoid, post:17, topic:3070"]
looking at edge connectivity to figure out UVs
[/quote]

UV data is stored per vertex, it has nothing to do with edges.

-------------------------

rku | 2018-06-01 08:23:23 UTC | #19

Godot recently added their own realtime CSG component. Code looks fairly easily portable. https://github.com/godotengine/godot/tree/master/modules/csg

-------------------------

urho3d | 2018-06-21 08:26:15 UTC | #20

6 posts were split to a new topic: [[Split - toxic] Realtime mesh fracturing](/t/split-toxic-realtime-mesh-fracturing/4337)

-------------------------

urho3d | 2018-06-21 08:28:12 UTC | #21

Toxic posts removed. Please keep things civil and on topic.

-------------------------

