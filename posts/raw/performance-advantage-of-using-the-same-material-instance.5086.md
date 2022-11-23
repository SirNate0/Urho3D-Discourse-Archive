NessEngine | 2019-04-06 18:08:28 UTC | #1

Lets say I have two objects with identical materials - does it matter if its actually the same material instance or two different materials with the same properties, from performance perspective? Ofc reusing materials have benefits of less RAM used, but does it affect CPU / GPU usage, like for example does it cause redundant copying of data to shaders or something similar?

I'm asking because I want to know if I can benefit from smart materials caching mechanism for runtime-generated materials I have, where RAM is not really an issue.

Thanks!

-------------------------

Leith | 2019-04-07 03:28:35 UTC | #2

From a performance perspective, there's little cost on the gpu side, and really not that much memory footprint either. There are use-cases where we want materials to be unique, shared, or global.

Using one material instance on multiple renderable objects means that any changes made to the master material object will affect all the renderables that share it.

Using multiple material instances allows you to modify the material uniquely for one target renderable (make a character glow), or for a subset of renderables (make one army of soldiers red, and another blue)

How you choose to use materials really depends on the requirements of your game.

-------------------------

weitjong | 2019-04-07 06:07:11 UTC | #3

Isn’t it the batch count affected by this?

-------------------------

Leith | 2019-04-08 07:41:39 UTC | #4

Absolutely, of course, batch count is affected by the number of unique Materials, but in most engines, instances of a unique material with different material properties don't generally affect the batch count, since the renderables are usually bucketed by material type, maybe sorted by z-order (eg 2D stuff), but generally not by material instance attributes. Specifically for Urho, I admit I don't know as I've spent little time with the rendering pipeline, but I would be suprised if using say, different colours in different instances of the same basic diffuse material caused the batch count to panic.

-------------------------

guk_alex | 2019-04-08 08:52:36 UTC | #5

You can benefit from using the same material if the object count and the number of materials is high enough and the engine supports it. But the effect can be not noticeable because of other aspects of render orders and existing rendering pipeline. But if your object count is less then 1000 I suggest just not to worry about it, or make proof-of-concept tests to be sure if it worth it.

-------------------------

Lumak | 2019-04-08 18:03:04 UTC | #6

Here is a graphics optimization check list from Unity
## Simple checklist to make your game faster

* Keep the vertex count below 200K and 3M per frame when building for PC (depending on the target GPU).
* If you’re using built-in shaders, pick ones from the **Mobile** or **Unlit** categories. They work on non-mobile platforms as well, but are simplified and approximated versions of the more complex shaders.
* Keep the number of different materials per scene low, and share as many materials between different objects as possible.
* Set the `Static` property on a non-moving object to allow internal optimizations like [static batching](https://docs.unity3d.com/Manual/DrawCallBatching.html)A technique Unity uses to draw GameObjects on the screen that combines static (non-moving) GameObjects into big Meshes, and renders them in a faster way. [More info](https://docs.unity3d.com/Manual/DrawCallBatching.html)
See in [Glossary](https://docs.unity3d.com/Manual/Glossary.html#StaticBatching).
* Only have a single (preferably directional) `pixel light` affecting your geometry, rather than multiples.
* Bake lighting rather than using dynamic lighting.
* Use compressed texture formats when possible, and use 16-bit textures over 32-bit textures.
* Avoid using fog where possible.
* Use [Occlusion Culling](https://docs.unity3d.com/Manual/OcclusionCulling.html)
to reduce the amount of visible geometry and draw-calls in cases of complex static scenes with lots of occlusion. Design your levels with occlusion culling in mind.
* Use skyboxes to “fake” distant geometry.
* Use pixel shaders or texture combiners to mix several textures instead of a multi-pass approach.
* Use `half` precision variables where possible.
* Minimize use of complex mathematical operations such as `pow` , `sin` and `cos` in pixel shaders.
* Use fewer textures per fragment.

More to read https://docs.unity3d.com/Manual/OptimizingGraphicsPerformance.html

-------------------------

NessEngine | 2019-04-08 22:17:20 UTC | #7

Thank you all, really useful advises!

[quote="guk_alex, post:5, topic:5086"]
You can benefit from using the same material if the object count and the number of materials is high enough and the engine supports it.
[/quote]

What do you mean by "if the engine supports it" - does Urho support it or not?

-------------------------

QBkGames | 2019-04-09 01:27:47 UTC | #8

Sounds like everybody knows general theory, but no-one really knows how Urho works specifically :slight_smile:.

-------------------------

guk_alex | 2019-04-09 08:45:32 UTC | #9

I can't be sure without digging in it. But with very brief review I found this in the code:

    /// Construct from a drawable's source 
    explicit Batch(const SourceBatch& rhs) :
        distance_(rhs.distance_),
        renderOrder_(rhs.material_ ? rhs.material_->GetRenderOrder() : DEFAULT_RENDER_ORDER),
        ...

-------------------------

Leith | 2019-04-09 09:29:27 UTC | #10

This is probably about z-sorting for 2d renderables (i.e. the UI elements) but do dig on, I'm really interested to see if you can chase this render pipe, I have not yet tried

In 3D, we tend to leave z-sorting to the per pixel level these days, because the hardware can usually do it better than we can.

-------------------------

Leith | 2019-04-09 09:35:37 UTC | #11

We're sort of off-topic, perhaps we need a new post about the render pipe ;)

-------------------------

Modanung | 2019-04-14 09:58:02 UTC | #12

Also note that `StaticModelGroup`s enforce the same material on all instances, just like Unity's *static batching*. Using custom shaders can be a way of adding variation despite all these models sharing a material.

-------------------------

