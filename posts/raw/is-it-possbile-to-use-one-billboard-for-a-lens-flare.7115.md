GodMan | 2022-01-02 03:10:49 UTC | #1

I need to create a single quad that faces the camera for a lens flare effect. All I see is just possibly billboards. Is it possible to use the billboard system for just one quad that is static and always faces the camera? 

Not use it for an actual particle system.

-------------------------

Modanung | 2022-01-02 12:06:37 UTC | #2

Yes, that's perfectly possible. :+1:

Besides, you might run into multiple bright light sources later. Maybe you could subclass the `BillboardSet` as a `LensFlareSet` to which you can add `Light`s (similar to adding `Node`s to a `StaticModelGroup`). This would be generalized for varying colours, brightness *and* light types while checking the visibility of each with a screen ray cast.

-------------------------

GodMan | 2022-01-02 18:52:43 UTC | #3

Okay I'll see what I can come up with.

-------------------------

Modanung | 2022-01-02 20:03:39 UTC | #4

You could also use a `Sprite`, btw. The main difference being that it's a `UIElement`.

-------------------------

GodMan | 2022-01-02 20:28:37 UTC | #5

It's not really for a lens flare. This is what halo calls them. I just need a quad that faces the camera like the particle system does. 

I'm trying to make the sentinel lights.

https://i.pinimg.com/originals/1a/be/2b/1abe2b6aca20cc845061bd20e3670ddd.jpg

-------------------------

Modanung | 2022-01-02 21:40:48 UTC | #6

That *is* what I think of when I hear the term "lens flare" in a game development context.

-------------------------

GodMan | 2022-01-02 22:18:06 UTC | #7

okay. I'm gonna try this with the billboard system.

-------------------------

GodMan | 2022-01-03 00:16:05 UTC | #8

Okay I got it. Thanks @Modanung . Going to add the other lights.

![Screenshot_Sun_Jan_02_18_14_00_2022|690x291](upload://hF8U8j969wLS28upB6y4jolytru.jpeg)

-------------------------

Modanung | 2022-01-03 00:47:46 UTC | #9

If you'd like to get rid of the flare intersecting with the model - which I imagine you would - simply add `depthtest="always"` to the technique of the flare's material.

-------------------------

GodMan | 2022-01-03 01:46:06 UTC | #10

Fixed the flare colors to be more accurate. Added the depthtest to the technique. 
![Screenshot_Sun_Jan_02_19_44_11_2022|690x291](upload://gxmq4pN5nm4DYqtggNJzpRS8xxY.jpeg)

-------------------------

SirNate0 | 2022-01-03 02:30:12 UTC | #11

With the "always" setting for depth testing I think you'll also need to make sure that it's only visible when it should be, i.e. walls and such need to occlude it in software and/or you need to check whether the flare should be shown with a raycast to the center point or something. Otherwise I'm pretty sure you'll see it through the walls even though the turret itself isn't visible.

-------------------------

GodMan | 2022-01-03 03:55:54 UTC | #12

Yeah I'm aware of this. I'll have to think of a simple approach for this though.

-------------------------

Modanung | 2022-01-03 08:54:18 UTC | #13

I'd do an octree raycast and then quickly fade the flare in or out - with a little scaling - using a `ValueAnimation`, when the visibility should change. You might want to disable occlusion to make sure the fade out finishes, preventing the flare from suddenly disappearing.

-------------------------

GodMan | 2022-01-03 19:50:08 UTC | #14

I have no idea how to do the octree raycast.

-------------------------

Modanung | 2022-01-03 20:18:57 UTC | #15

Have a look at the `Raycast` function from the Decals sample; 08.
Where you would of course replace `NormalizedScreenPos` with `WorldToScreenPos`. Apart from that change, you basically have your (in)visibility check right there. You might even do without the parameterization, use the distance from the light to the camera as `maxDistance` and disregard the hit position and drawable. Maybe send it just a `const Vector3& worldPos`.

-------------------------

Modanung | 2022-01-03 21:30:39 UTC | #16

I guess you would at least want to check the `Drawable`'s type to prevent other `BillboardSet`s (or the same) from hiding the flares. Which also means you'd need to use the `Octree`'s non-single raycast, as these may be the first hit drawable.

-------------------------

GodMan | 2022-01-03 21:37:51 UTC | #17

Great post @Modanung I will look into this when I get a chance.

-------------------------

