GIMB4L | 2017-01-02 00:58:15 UTC | #1

How would I go about making a billboard sprite that is unaffected by distance from the camera?

-------------------------

friesencr | 2017-01-02 00:58:15 UTC | #2

Like a sprite in 2d screen space?

-------------------------

GIMB4L | 2017-01-02 00:58:15 UTC | #3

Essentially. If there's an easy Vector3::ToScreenSpace function that would work out fine.

-------------------------

friesencr | 2017-01-02 00:58:15 UTC | #4

We just a had a discussion about that not to long ago.

[topic102.html](http://discourse.urho3d.io/t/positioning-nodes-in-screen-space/121/1)

Here is the code he used.
[code]
// This line should set the cube in the very top-left corner of the screen. Or not?
    Vector3 playerPos = camera->ScreenToWorldPoint(Vector3(0, 0, 20));
    cubeNode_->SetPosition(playerPos);
[/code]

The gotcha was aspect ratio in his situation.

-------------------------

