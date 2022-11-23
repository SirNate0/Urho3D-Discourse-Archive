sirop | 2018-10-13 07:08:00 UTC | #1

Hallo.

My Camera has several knots (Vector3) to run through. I use a CATMULL_ROM_CURVE
for this. This works.

Now there is an array of camera Zoom values that should correspond to the Vector3 spline knots above / be reached at the same time as the Vector3 spline knots.

Shall I simply make up Vector4 knot out of Vector3 knot and zoom value and then apply the usual CATMULL_ROM_CURVE  routine? Any better suggestions?

Thanks in advance.

-------------------------

Modanung | 2018-10-13 10:12:54 UTC | #2

If you want to slerp quaternions next I think you may be better off creating custom subclasses.

-------------------------

sirop | 2018-10-13 10:16:59 UTC | #3

Vector4 might have confused you, but Vector4 is meant to be Vector4 here, not necessarily a quaternion.

See https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Core/Spline.cpp#L216

-------------------------

Modanung | 2018-10-13 10:21:15 UTC | #4

Ah, no I was not confused by that. Maybe I should have elaborated a bit more.
I meant creating your own Knot class that holds:
```
Vector3 position_;
Quaternion rotation_;
float fov_;
```

-------------------------

sirop | 2018-10-13 10:33:53 UTC | #5

In my special case camera orientation can be arbitrary as it is manually controlled by the user.
So I'd try the case

    Vector4 vec4 = [ position_, zoom_];

-------------------------

Modanung | 2018-10-13 10:37:44 UTC | #6

You're not planning any cut-scenes or other interruptions to the control?

-------------------------

sirop | 2018-10-13 10:40:10 UTC | #7

My camera movement along a precalculated spline can be paused and then resumed.
No other interruptions are planned.

-------------------------

Modanung | 2018-10-23 11:29:05 UTC | #8

The Vector4 solution should _work_ fine. I just think semantically it's a bit iffy.

-------------------------

