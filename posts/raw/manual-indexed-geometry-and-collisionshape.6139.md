jamies | 2020-05-14 11:59:00 UTC | #1

I'm reading the characterdemo sample.

https://github.com/urho3d/Urho3D/blob/master/Source/Samples/18_CharacterDemo/CharacterDemo.cpp#L140

At this point in code, the scale is random, does it mean that anything that is applied on a Node, also affects its physics?

I'm planning to build manual geometry, but SetTriangleMesh takes a model. Should I use bullet internals, or is urho3d able to build a collisionshape from a customgeometry? Can it take indexed geometry as an input?

I've already used btTriangleIndexVertexArray with success with plain opengl, but I'm not sure urho3d does it too.

-------------------------

jamies | 2020-05-13 17:21:42 UTC | #2

I know it's impolite to bump a thread... Is my question poorly formulated?

I also left a comment here: https://discourse.urho3d.io/t/solved-manually-create-model-from-c/161/4

-------------------------

Modanung | 2020-05-13 19:53:14 UTC | #3

The scale of a `Node` affects the size of any `CollisionShape`s it('s children) may have, but it has no effect on `RigidBody`s in any way. See also: [`CollisionShape::UpdateShape()`](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Physics/CollisionShape.cpp#L1014-L1089)

`CollisionShape`s have `SetCustomTriangleMesh`, `SetCustomConvexHull` and `SetCustomGImpactMesh` functions to combine them with `CustomGeometry`.

[quote="jamies, post:2, topic:6139"]
I know it’s impolite to bump a thread...
[/quote]

So is leaving questions unanswered. :slightly_smiling_face:

-------------------------

jamies | 2020-05-14 14:05:13 UTC | #4

I found CustomGeometry::DefineVertex... but how can I make an indexed geometry?

EDIT: sorry seems to be DefineGeometry()

EDIT2: doesn't seem to be that either...

-------------------------

SirNate0 | 2020-05-15 16:15:56 UTC | #5

You can just create a Model manually (setting the vertex and index buffers) if you want to use an indexed geometry. There may be a way to do it with CustomGeometry as well, but I don't use that do I'm not sure myself.

-------------------------

jamies | 2020-05-20 13:07:08 UTC | #6

Would you happen to have some code sample for this?

EDIT:

I really wish there was some code sample for indexed geometry, I don't understand how to use IndexBuffer::SetDataRange() and IndexBuffer::SetData(). Is that a list of 3-integer-tuple?

-------------------------

Eugene | 2020-05-20 13:23:19 UTC | #7

When I was working on lightmapper, I made an utility to construct/decostruct Model. You might want to reuse this code:
 https://github.com/rokups/rbfx/blob/master/Source/Urho3D/Graphics/ModelView.h
 https://github.com/rokups/rbfx/blob/master/Source/Urho3D/Graphics/ModelView.cpp
 https://github.com/rokups/rbfx/blob/master/Source/Urho3D/Graphics/VertexBuffer.cpp
 https://github.com/rokups/rbfx/blob/master/Source/Urho3D/Graphics/IndexBuffer.cpp

-------------------------

jamies | 2020-05-23 16:02:59 UTC | #8

I'm not sure that helps me creating a model manually. What line should I reuse?

For now I'm doing this, for some reason the second line doesn't compile.

        SharedPtr<VertexBuffer>vbf;
        Vector<Vector3> vertices = { {0.f, 0.f, 0.f}, {1.f, 0.f, 0.f}, {0.f, 1.f, 0.f} };
        vbf->SetData(&vertices[0]);

        SharedPtr<IndexBuffer>ibf;
        int index[] = { 0,1,2 };
        ibf->SetData(index);
        auto geom = terrain_node->CreateComponent<Geometry>(CreateMode::LOCAL);
        geom->SetIndexBuffer(ibf);
        geom->SetVertexBuffer(0, vbf);

        auto model = terrain_node->CreateComponent<Model>();

        model->SetGeometry(0, 0, geom);

-------------------------

Eugene | 2020-05-23 16:02:42 UTC | #9

[quote="jamies, post:8, topic:6139"]
What line should I reuse?
[/quote]
All of them, I guess?

I use this code to edit models. It can be used to make one from scratch, too.

Or maybe you can just look how this code builds model and do something similar, but simpler, since you probably don’t need all the features I needed.

-------------------------

jamies | 2020-05-23 16:04:15 UTC | #10

So I cannot manually set indexed geometry in urho3d without your code?

-------------------------

Eugene | 2020-05-23 16:26:25 UTC | #11

You don't have to use my code, obviously. You can write your own code to make a `Model`.

If you are asking if there's simple way, like with `CustomGeometry`, then the answer is no, there's no syntax sugar in Urho to make a Model from scratch with just a few lines of code. You either make your own utility to do that, or you reuse one of utilities already made (e.g. mine, but I saw others on the forum).

-------------------------

jamies | 2020-05-23 19:35:54 UTC | #12

Where should I get started to make a model from scratch? What's the minimum amount of code I should write? Are there requirements?

-------------------------

Eugene | 2020-05-23 20:35:34 UTC | #13

I wrote my code in generic way, so I have a lot of utility functions.
You can use `Vertex/IndexBuffer::SetData` directly instead, if you don't need to be generic.

This part of the code will give you an idea about what you need to do:
https://github.com/rokups/rbfx/blob/master/Source/Urho3D/Graphics/ModelView.cpp#L384-L461

-------------------------

johnnycable | 2020-05-24 14:52:47 UTC | #14

You could check my answer on using [custom geometry](https://discourse.urho3d.io/t/how-to-create-a-point-cloud/3275/10?u=johnnycable). Some more posts down, there's an implementation of this kind of utility.

-------------------------

jamies | 2020-05-24 15:22:21 UTC | #15

Thanks for the reply, but I'm looking for indexed geometry.

-------------------------

