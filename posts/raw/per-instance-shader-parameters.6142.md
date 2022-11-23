throwawayerino | 2020-05-06 15:53:47 UTC | #1

My shader takes in a boolean and whenever I toggle the parameter using `SetShaderParameter()` all models with the same material also get changed. I could easily clone the material, but 1) I would lose instancing optimization and 2) isn't easy to do in the editor

-------------------------

Eugene | 2020-05-06 17:42:05 UTC | #2

There is a hack that let you pass additional per-instance data.
However, it can be done only if you make new drawable component and manually fill or edit batches (maybe inherited from existing one).

https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/Drawable.h#L104
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/Renderer.h#L230

-------------------------

