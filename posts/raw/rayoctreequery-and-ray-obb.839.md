practicing01 | 2017-01-02 01:03:21 UTC | #1

I'm raycasting and selecting RAY_OBB but it seems it's picking triangles regardless.  I hacksolved this by aiming at a dummy node that was surrounded by geometry in the model.  I thought RAY_OBB was the big box that surrounds the bounds of the model, am I wrong?  Any thoughts on this matter are greatly appreciated.

-------------------------

cadaver | 2017-01-02 01:03:21 UTC | #2

What is the component you're raycasting against? StaticModel?

-------------------------

practicing01 | 2017-01-02 01:03:21 UTC | #3

The node has an animated model component (it stays almost still though).  I'm not using the latest urho btw, not sure if somewhere between my copy and the latest there were commits that affected raycasting.

-------------------------

cadaver | 2017-01-02 01:03:21 UTC | #4

This looks like a bug, or an ambiguity. AnimatedModel will actually not ever perform triangle-level tests when the model is skinned, rather it tests against bone hitboxes. However this happens in both RAY_OBB & RAY_TRIANGLE modes.

-------------------------

cadaver | 2017-01-02 01:03:22 UTC | #5

The behavior has been changed in the master branch. For AnimatedModel, RAY_OBB now performs an OBB test against the whole model, and only RAY_TRIANGLE performs the bone hitbox testing.

-------------------------

