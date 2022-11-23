evolgames | 2020-03-07 02:07:59 UTC | #1

For some reason, using a triangle mesh causes my tank to fall through terrain.
Convex hull has collisions, but is weirdly off balanced.
SetBox works great, and I will use it if I have to, but it would be nicer to have mesh-based collisions for impacts and the like.

Any idea why this happens?

I've modified the raycast vehicle sample.

```
    local node = self.node
    local hullObject = node:CreateComponent("StaticModel")
    self.hullBody = node:CreateComponent("RigidBody")
    local hullShape = node:CreateComponent("CollisionShape")
    node.scale = Vector3(.01,.01,.01)
    hullObject.model = cache:GetResource("Model", "Models/hull2.mdl")
    local material=Material:new()
    material:SetShaderParameter("MatDiffColor",Variant(Vector4(.05,.1,.05,1)))
    hullObject:SetMaterial(material)
    hullObject.castShadows = true
    hullShape:SetBox(Vector3(500,180,750))
    hullShape:SetTriangleMesh(hullObject.model)
```
Image order:
1. Convex Hull
2 & 3 are with SetBox
4. Triangle Mesh falling through the terrain
![Screenshot|690x369, 75%](upload://xblK9QyYcLXLfOW8LO0ugstT84N.jpeg) ![Screenshot-1|690x369, 75%](upload://wKB3cEwO9ZMVvyHTVUHw7ilnUQO.jpeg) ![Screenshot-2|690x369, 75%](upload://iGoBrtq1KvMD5ULzDQFn5hZ5PIa.jpeg) ![Screenshot-3|690x369, 75%](upload://kAhbn5h4tyoHNr6GDkCgKDYrDGd.png)

The mass of the top parts are .01 so as not to affect balance.

-------------------------

Modanung | 2020-03-07 22:14:04 UTC | #2

I believe Bullet expects triangle meshes to remain stationary. You _could_ of course combine several convex hulls/shapes instead, if you really need that extra detail.

-------------------------

GodMan | 2020-03-07 03:46:27 UTC | #3

I use trianglemesh for static objects. Like @Modanung said it;s meant for only objects that don't move.

-------------------------

evolgames | 2020-03-07 04:28:54 UTC | #4

oh I see. that makes sense. I'll stick with some boxes then. it's not a big deal.

-------------------------

dertom | 2020-03-07 06:48:46 UTC | #5

Concerning the convex shape. Do I see it right that you try to use your 'highdetail' mesh as input? 
That isn't convex at all and that might be the cause for being 'offballanced'. 
You would need to create a special, more simple convex collision mesh for being used as covex-collision model and the one you already have will only be used for rendering.

Are you modelling in blender? Afaik there is a function called make convex or similar... Not sure how good that works though.

-------------------------

evolgames | 2020-03-08 07:44:07 UTC | #6

Oh okay I see now. I was under the impression that I could easily create a mesh-based collision shape, making things easier for impacts.

Yeah I made some very basic models in Blender for this. It's not a big deal though, I can manage with boxes :slight_smile:

-------------------------

GodMan | 2020-03-08 18:20:06 UTC | #7

Yeah it's a shame that you cant use a simplified mesh for collision on an animated model.

-------------------------

Modanung | 2020-03-08 22:37:05 UTC | #8

You could maybe use some zero-gravity "physics overlay" that *tries* to follow the skeletal animation by force or constraints, basically a driven ragdoll. Together with the right collisionmask these objects could override the bone positions when they differs too much.
It may not be as simple, but impossible is nothing. :slightly_smiling_face:

-------------------------

GodMan | 2020-03-09 00:02:08 UTC | #9

Can I add lets say a small box shapes to each bone in the skeleton? That way it is still using a built in physics shape, but more accurate? Kind of like the Ragdoll physics?

-------------------------

Modanung | 2020-03-09 00:10:02 UTC | #10

The problem is that Bullet doesn't like it when positions or velocities of `RigidBody`s are modified by other processes as this messes up the simulation, yet that is exactly what a skeletal animation does.
Therefor one should think in terms of - what I would call - an _overlay_, and not direct attachment.

-------------------------

