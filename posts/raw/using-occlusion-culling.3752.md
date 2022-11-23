nergal | 2017-11-18 15:33:55 UTC | #1

I'm having a lot of custom geometry meshes. How can I use occlusion culling for the scene? I've elaborated a bit with the renderer to set different settings for occluder-functions but debugging the scene is says "0 Occluders" and there are not fewer triangles even though I know some meshes are completely hidden by others.

Am I missing something? Or how can I achieve occlusion culling for my scene?

-------------------------

Bananaft | 2017-11-24 21:20:36 UTC | #2

You pick a few large static models in the scene and set them as occluders in the editor, or in the code. Don't make all objects occludes, keep your occlusion-pass light and simple. If occluder model has too many polys, it is better to make a proxy mesh and put inside it.

-------------------------

nergal | 2017-11-24 21:40:44 UTC | #3

Ah I see. But do I set a node or a model as occluder? And do you have an example how to do that (in C++)? (I can't find any related function for Node/Model in the docs)

Ok, so large poly meshes might be better to create a extra mesh "boundingbox"-style to use a occluder?

-------------------------

Modanung | 2017-11-24 23:10:59 UTC | #4

The occluder flag is set on [`Drawable`](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_drawable.html) components - like the `StaticModel` or `AnimatedModel` - using the `SetOccluder` method.

A `Model` is not a component, it is a `Resource`.

-------------------------

nergal | 2017-11-25 10:42:14 UTC | #5

ok, can I set a occluders to billboardsets as well? In order to occlude billboards?

-------------------------

Modanung | 2017-11-25 15:35:16 UTC | #6

I'm honestly not sure. All `Drawable`s are set to be occludees by default. But occlusion inclusion seems to require the `Drawable::AddTriangles` function to be called. Which the `BillboardSet` doesn't do. But I might be overlooking something.

-------------------------

