burt | 2018-11-12 13:53:16 UTC | #1

I'm trying to reproduce the following technique:

https://www.youtube.com/watch?v=kdjo7nQvD3g

Based on the Urho docs, the only thing I found was the DebugRenderer AddLine function.  But I'm pretty sure I'm not supposed to use that for an in-game feature. Does anyone have any suggestion on how to properly render lines on top of a raycast?

-------------------------

Modanung | 2018-11-11 18:50:44 UTC | #2

You could use a `BillboardSet` for the bullets with the `FaceCameraMode` set to `FC_DIRECTION`. There's a sample demonstrating its use.
A single raycast is instant, so you'd have to add an artificial delay in that case.

-------------------------

johnnycable | 2018-11-12 13:48:52 UTC | #3

Or paint them lines with particles

-------------------------

Modanung | 2018-11-12 13:52:53 UTC | #4

I think that technically comes down to the same with part of the desired control for this situation replaced by unneeded features.

-------------------------

Eugene | 2018-11-12 15:23:21 UTC | #5

I had some prototypes, check this:
https://github.com/eugeneko/Urho3D-Sandbox-Dirty/tree/networking-prototype/Source/FlexEngine/Physics
It looks quite close to what you've shown in video

-------------------------

