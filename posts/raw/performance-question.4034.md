slapin | 2018-02-22 06:40:51 UTC | #1

Hi all!

I have large set of mechanical objects - doors/windows, cars (with openable doors, hod, trunk), etc. What is the best way to implement these for best performance -

1) set of StaticModel controlled by nodes
2) AnimatedModel with bones

Models are all mechanical and visually look the same both ways.  No organic shapes.
Animations of open-close are occasional (on event), not persistent.

-------------------------

Sinoid | 2018-02-22 11:30:57 UTC | #2

TL;DR: use whichever is more convenient for you until you see an actual problem. Need it to be able to easily detach? Use scene nodes and attribute animation. Prefer to do as much as possible in max/maya? Use animated model.

---

You'll have to try both and measure if you really want to know for actual performance, there isn't that much extra that happens to bones as opposed to Nodes. Transforming a skeleton only differs from transforming a scene-graph in that a skeleton has to do more book-keeping for weights and state - otherwise it's the same stuff just potentially done many times and mixed.

Although skeletal animations involve some more work in AnimationController, attribute animations potentially have to evaluate curves instead of just lerp/slerp - which may be worse or it may mean even fewer keys.

For rendering it really depends on your modeling habits but when using nodes and static meshes things are more likely to be ad-hoc pieces and that means more draws ... though if many parts are the same (manufacturing robotics arms comes to mind) instancing will make that fairly moot and the vertex shader will be lighter to boot.

There's also the case where you use an AnimatedModel but not an AnimationController, using attribute animation to control the bone nodes.

---

But for memory footprint which you can actually look at AOT ...

You have mesh data regardless. For an animated model you'll have an extra 20 bytes per vertex compared to the static (if shadowed). Each Urho3D::Node is 368 bytes and with an animated model each joint will be reproduced in the scene-graph as a node per instance plus the 168 bytes for the shared bone data and a skeleton is 24 bytes ... so seperate meshes on nodes is a little fatter due to multiple StaticModel components (456 bytes) vs 1 AnimatedModel (696 bytes).

Attribute animation is larger than skeletal animation.

- For skeletal animation a 44 byte keyframe covers position, rotation, scale, and time
- For attribute animation each attribute has a 44 byte keyframe for the Variant and time (variant has become really obese with value type bloat)
    - x3 if animating position + rotation + scale
- Skeletal animation track is 40 bytes
- Attribute animation *track* is 160 bytes

So, just footprint wise - the difference isn't big enough to warrant choosing anything but the most convenient one for you to work with. Attribute animation is definitely fatter, but not enough to really care for something like a door.

---

The save/load APIs for both model animations and attribute animations are equally complete so there really isn't a *"well I could write a little keyframe editor for doing this ad-hoc in the editor"* difference between them either.

If you're concerned about a future *"OMG! I've screwed up! I need to switch to bones!"* you can follow the OBJ export code and write a dump for an MD5 model (or other easy format) based on that with absolute (1.0) bone weights mapped to each mesh's node to get a skeletal model back out for import into an animation tool. Similiarly the .uani format is simple enough to convert to-from skeletal-attribute animation.

-------------------------

slapin | 2018-02-22 17:36:39 UTC | #3

Thanks a lot for your answer. I think writing a small benchmark is a good idea.
It will be sad if I will need to change established asset pipeline because one or other way can't handle 200-300 cars + 100 people + 200 boats on something like android because of incorrect choise at the beginning...

I do not use attribute animation or any animation files, I just control nodes directly
(procedural approach) for door animations.

-------------------------

