WangKai | 2020-06-17 13:22:18 UTC | #1

Something infinite should not be culled by frustum, e.g. sky box, infinite grid in tools, etc.

How can I force the drawable to be visible?

Any ideas?

Thanks!

-------------------------

Eugene | 2020-06-17 23:24:28 UTC | #2

Set an infinite bouning box for this drawable.
I mean, it's literally what `Skybox` does, just check its code.

-------------------------

WangKai | 2020-06-18 02:19:16 UTC | #3

Thanks Eugene!

Shall we have a public `SetBoundingBox` interface for `Drawable` ?

Currently, only some of the `Drawable`s have this interface - `NavArea`, `TerrainPatch`, `Zone`, `StaticModel`(private method), and `Model`(as `Resource`).

Edit: It seems local `boundingBox_` sometimes cannot control and even not used when we are calculating `worldBoundingBox_` in `OnWorldBoundingBoxUpdate`, which means, control local bounding box does not work for many cases. 

The original design seems to use `OnWorldBoundingBoxUpdate` to control the eventual world bounding box. I guess rewritting `OnWorldBoundingBoxUpdate` is the right way to go. Though, it means we need to use inheritance and override the interface.

-------------------------

