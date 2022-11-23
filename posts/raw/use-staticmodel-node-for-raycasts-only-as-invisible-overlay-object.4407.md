ahorn42 | 2018-07-25 16:06:20 UTC | #1

Hi there,

I am trying to select objects via octree raycast, which works, but the rendering performance isn't great because of to many subobjects (StaticModel with multiple vertex buffers (~10000)). If I am rendering the combined object (one vertex buffer) the performance is okay, but the raycast can't determine a subobject other then `0`, understandably.

So my idea was: taking the one-vertex-buffer model to render the models (that's hidden from the raycast via viewmask) and use a multiple-vertex-buffer model that's hidden from the camera to do a raycast to determine the selected subobject.

But if I do this the performance drops as low as if I use the multiple-vertex-buffer model for rendering.
The only noticeable performance boost was possible if I disabled the multiple-vertex-buffer model, but on a disabled node the raycast does not work either. Setting the multiple-vertex-buffer models `ViewMask` to `0x00000000` or setting its `DrawDistance` to `0` or a very high value (100000) has no effect on the performance. I also tried to set the `Ocludee` property to `true`, with no noticeable impact.
That's quite interesting in my opinion. Shouldn't setting a models `ViewMask` to `0x00000000` prevent it from rendering, because it's invisible for the cameras? But it seems as the vertex buffers still get transferred to the graphics card and causing some performance trouble there. I can not imagine that the raycast hits the performance so hard.

Are there any ideas out there, how to prevent a StaticModel from rendering? (Or an other idea how to perform the model selection?)

Two ideas I still have are:

1. loading the submodels as CollisionShapes and perform a physics raycast (but I think the physics engine will die with that many objects),
2. creating a color coded texture and select the object according to the color at the position where the raycast hits the texture (the problem here is to unwrap the model(s) in blender, because they are very large with high polygon count (~500000 all together) and not easy to unwrap).

best regards,
ahorn42

-------------------------

Eugene | 2018-07-25 22:23:10 UTC | #2

[quote="ahorn42, post:1, topic:4407"]
Shouldn’t setting a models `ViewMask` to `0x00000000` prevent it from rendering, because it’s invisible for the cameras?
[/quote]
`Model` (and so, `VertexBuffer` and `IndexBuffer`) is always created in GPU memory.
However, model with zero view mask shall not be rendered.
Are you sure that your multiple-vertex-buffer model is not rendered?
Ensure that you don't use this model as occlud**er**.

[quote="ahorn42, post:1, topic:4407"]
The only noticeable performance boost was possible if I disabled the multiple-vertex-buffer model, but on a disabled node the raycast does not work either.
[/quote]
If you have known set of Drawable-s to ray test, nothing prevents you from calling `ProcessRayQuery` manually. It doesn't care about enabling things.

-------------------------

ahorn42 | 2018-07-26 11:11:47 UTC | #3

I really like the idea to call ProcessRayQuery manually on an disabled object - I'll try that, but as I am using UrhoSharp I need to extend some of the bindings, because not all public members and types are redirected. So it might take some time, till I can tell if it is working as intended.

-------------------------

Eugene | 2018-07-26 11:26:04 UTC | #4

BTW, what if you put your raycast model into second invisible scene and then use that scene for querying?

-------------------------

ahorn42 | 2018-08-10 07:55:48 UTC | #5

yeahy - I finaly got it, but with an slightly different aproach.

At first I tried to get the `ProcessRayQuery` method working in C#, but I failed on some C++ difficulties I think. But during testing I recognized, that another problem was the time the raycast takes on such a large object. And this would not get much better, by calling `ProcessRayQuery` manually.

My aproach now is to use a second `Octree` where I add the segmentized subobjects of the large object in smaller single objects (about 6000). I disable them, so they don't get used by the renderer and added them manually via `AddManualDrawable` to my own octree.

```csharp
myOct = new Octree();
for (int i = 0; i <= x; i++) {
    var raycastSubObjectModel = raycastSubObject.CreateComponent<StaticModel>();
    raycastSubObjectModel.Model = ResourceCache.GetModel("Models/" + i + ".mdl");
    raycastSubObjectModel.Enabled = false;
    myOct.AddManualDrawable(raycastSubObjectModel);
}
```

The perfomance increased very well from about 50 to 120ms per raycast down to below 2ms per raycast :slight_smile: 

@Eugene thanks for your ideas otherwise I wouldn't have found my current solution ;)

-------------------------

