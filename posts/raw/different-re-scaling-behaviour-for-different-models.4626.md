sirop | 2018-10-30 04:43:41 UTC | #1

Hallo.

I use two kind of models. The first kind is very simple, that is a Cube or a Sphere as shipped with  Urho3D.
The second kind is an export from Blender, contains several materials and textures.

Both kinds are placed on a plane. However, when rescaling the models, the Blender exports behave as expected: they get smaller or bigger, but remain on the plane.
This is quite different when applying the same rescaling operation to the Cube or Sphere: they change their size but either grow through the plane when increased or float over the plane when decreased.


![spher_thru|573x500](upload://nIxs8QXmy9ESqUTjTdR5SOqMdGX.jpeg) 


All models are set up in a similar way.
Especially these lines are same for all models:
```
  auto* body = sphereNode->CreateComponent<RigidBody>();
  body->SetCollisionLayer(2);
  auto* shape = sphereNode->CreateComponent<CollisionShape>();
  shape->SetTriangleMesh(sphereObject->GetModel());
```

Any ideas?


Thanks.

-------------------------

jmiller | 2018-10-30 15:33:10 UTC | #3

The primitives' origins seem normal.

As objects scale with respect to their origin, perhaps check your mesh origins in Blender/modeler and the exporter settings?
  https://github.com/reattiva/Urho3D-Blender/blob/master/guide.txt#L67

-------------------------

sirop | 2018-10-30 15:37:40 UTC | #4

I have no problems with the models exported from Blender,
but with the cube/rock and sphere as shipped with Urho.

-------------------------

jmiller | 2018-10-30 18:19:40 UTC | #5

I think I understand. To me, the primitives' 'symmetric' origin seems more generic/natural (makes fewer assumptions about use/scene/gravity) -- just translate as needed.

I suspect if the meshes' origins changed, it would throw off nearly every program that used them. :smile:

-------------------------

Modanung | 2018-10-31 00:28:23 UTC | #6

The models that you mentioned which come with Urho have their origin at their center. It seems like you are placing the origin at floor level for your custom models. Both make sense in different situations.
It's easier to align something with the floor if it has its pivot at its feet, but when things need to roll you want the pivot exactly at the center to prevent it from wobbling.

-------------------------

sirop | 2018-10-31 12:46:37 UTC | #7

Ok. So I have to edit the models in the Editor or Blender.

No way to solve this by Urho's C++?

-------------------------

Modanung | 2018-10-31 14:23:07 UTC | #8

You could create a child node and attach the model to it.

-------------------------

sirop | 2018-10-31 14:25:34 UTC | #9

Thanks. It is similar to https://discourse.urho3d.io/t/solved-bought-fbx-models-facing-z-axis/1470/4?u=sirop

-------------------------

