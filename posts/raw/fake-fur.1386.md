practicing01 | 2017-01-02 01:07:23 UTC | #1

I would like fur for a project and came across this: [malideveloper.arm.com/downloads/ ... 4/fur.html](http://malideveloper.arm.com/downloads/deved/tutorial/SDK/linux/2.4/fur.html) I'm an opengl newbie, how difficult would it be to integrate the code in the white paper linked, into urho?

-------------------------

Bananaft | 2017-01-02 01:07:23 UTC | #2

It seems like a terrible way to draw a fur. It works only with primitives. It super inefficient in both draw calls number and fill rate.

For furry character you should consider something like this:

[sketchfab.com/models/fe7cb500bf ... 54a629abd1](https://sketchfab.com/models/fe7cb500bf314ab58dc42954a629abd1)

Check out the wireframe.

-------------------------

Modanung | 2017-01-02 01:07:42 UTC | #3

You may also consider [url=http://cdn.wolfire.com/blog/furblur/plasterfur.jpg]using normal maps[/url] and soft body physics.
A fur component which extends the particle system might also work.

-------------------------

boberfly | 2017-01-02 01:07:42 UTC | #4

For a prototype character (a bird essentially) I am planning to use a technique like this:
[amd-dev.wpengine.netdna-cdn.com/ ... Slides.pdf](http://amd-dev.wpengine.netdna-cdn.com/wordpress/media/2012/10/Scheuermann_HairSketchSlides.pdf)
But perhaps tweak it a bit so that it uses alpha-to-coverage, weigh the benefits/disadvantages. Sorting/fill rate problems as well.

It's a big problem when you factor in which lighting model you'd want to use. You're basically wanting to go forward-rendered unless you can do alpha-to-coverage with FSAA deferred buffers (can Urho3D do this now with the GL 3.3/DX11 backends?). Or revert to FXAA, saving you a bit from blocky alpha discard.

There is a trick to prevent CPU-level sorting if you use alpha-blend. In the DCC/Blender/Maya/etc. package, if you place out your mesh sheets and merge them in the order of how you'd like them to draw, it sets the vert ordering and will render to that order in 1 draw call. And you'd do the opposite way for backfacing meshes and merge them first and the frontfacing second. It's not perfect but it does work in some situations (the assimp mesh convert might break this trick though, as it changes vert ordering I think). The more overlaps the more fill-rate needed though.

For animated fur on a skinned mesh I can see three ways which I've thought about: Use blendshapes to blend different states, so that they can still be skinned as bones as they are the second transform pass. Or, you'd use transform-feedback and animate them with a separate set of bones as a first pass, which isn't implemented in the main Urho3D codebase. The third way (which is probably the one I'd go for) instead of transform-feedback, it might also be possible in code to set the transform for the fur/feather bones to the average position of 2-4 bones (the same weighting that matches the underlying vertex/face which the fur/feather mesh sits on), but this would require some kind of weighted transform component of sorts, bypassing the parent/child system for these fur bones (and some rigging know-how on the DCC package side to mimic this, maybe with constraints).

Yeah just brain-dumping again, sorry... :slight_smile:

-------------------------

