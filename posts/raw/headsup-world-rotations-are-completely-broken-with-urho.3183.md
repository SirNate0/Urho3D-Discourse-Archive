slapin | 2017-06-01 00:22:05 UTC | #1

Hi, all

Please see the bug:
https://github.com/urho3d/Urho3D/issues/1961

This bug is show stopper for my project.
This one hit me so badly so I suspended all farther work with Urho for now.
Looking forward for the fix. Will provide any details necessary to fix this one.

-------------------------

Modanung | 2017-06-01 08:13:28 UTC | #2

Are you sure the reversal doesn't happen during export/import?

-------------------------

George1 | 2017-06-01 09:22:38 UTC | #3

Na, there's no bug the last time I used it.

I think make sure your character face z after imported into urho. 
Also see Lumak remark about the axis.

Rotation of door are relative, unless it is attached to a parent. Then you have to get the parent inverse and multiply with current rotation and new delta rotation.

-------------------------

Modanung | 2017-06-01 09:28:32 UTC | #4

Ah yes, if there's a node hierarchy involved you'll need to get their world positions to look at.
Could that be it?

-------------------------

slapin | 2017-06-01 09:33:01 UTC | #5

I do world rotation, how all this can be related?

-------------------------

Eugene | 2017-06-01 12:59:12 UTC | #6

I checked your issue.
When you do `doors[i].worldRotation * Quaternion(0.0f, 5.0f, 0.0f)`, you rotate the door in the local space. There is no guarantee that local Y axis is the same as the world up axis.

Was this your question?

-------------------------

slapin | 2017-06-01 17:59:59 UTC | #7

why don't anyone see worldRotation here?

-------------------------

Eugene | 2017-06-01 18:12:15 UTC | #8

Sorry, I didn't understand your reply completely.
Does it answer your question?

**Q:**
> As you can see this should rotate doors 5 degrees upon world Y axis.

**A:**
> you rotate the door in the local space. There is no guarantee that local Y axis is the same as the world up axis.

-------------------------

slapin | 2017-06-01 18:13:29 UTC | #9

worldRotation rotates in world space.

-------------------------

slapin | 2017-06-01 18:13:47 UTC | #10

At least supposed to.

-------------------------

Eugene | 2017-06-01 18:25:04 UTC | #11

Oh, I understood...

`worldRotation` _itself_ works in the world space, of course.
But you don't _set_ world rotation to some value (e.g. `Quaternion(0, 5, 0)`), you _rotate_ world rotation by some delta value.

Rotations are accumulated from right to left.
So, `worldRotation * delta` is _local_ space rotation and actually the same as `rotation * delta`.
To rotate in _world_ space you'd probably need to do `delta * worldRotation`.
BTW, `delta * rotation` is rotation in _parent_ space.

-------------------------

slapin | 2017-06-01 19:06:28 UTC | #12

Thanks for explanation. This is really worth mentioning in documentation.

But it looks nothing to do with local/global space, more in Quaternion multiplication logic.
So Quaternion multiplication can lead to unpredictable results if 2 quats axes do not match, the resulting quat can have
different axes rotations.

But the question is there some 100% sure way to rotate stuff in world space in deltas?
Something which can be used by people who want to forget about math for some time?

-------------------------

Eugene | 2017-06-01 19:17:32 UTC | #13

> But the question is there some 100% sure way to rotate stuff in world space in deltas?

This way:

> To rotate in world space you'd probably need to do delta * worldRotation

Then,

> So Quaternion multiplication can lead to unpredictable results if 2 quats axes do not match, the resulting quat can have different axes rotations

Result is perfectly predictable (as anything in math ;)) if you keep in mind the order of rotations.

> Something which can be used by people who want to forget about math for some time?

Unless you are satisfied with Unity-like pre-programmed assets like `DoorRotator`, this part of math is really important. Transformation mechanism is similar in all engines and it would be very useful for you to keep it in mind at least generically.

-------------------------

slapin | 2017-06-01 19:34:30 UTC | #14

so the only way is to multiply properly is
    Quaternion delta = Quaternion(0, 5, 0);
    doors[i].worldRotation = delta * doors[i].worldRotation;

I wonder why Urho is the only engine I struggle with this in. Probably others did some helpers...
Anyway it is in common with Urho expression ordering where everything is from right to left...
Well, this all needs some kind of documentation...

-------------------------

slapin | 2017-06-01 19:36:13 UTC | #15

Anyway, thanks a lot for your help.

-------------------------

lezak | 2017-06-01 21:43:33 UTC | #16

Wouldn't <a href=https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_node.html#a29dcc8e9fda99ed85de6a63fda84f598>Node::Rotate</a> or <a href+https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_node.html#a8d6d99cb206f468b39f996667e92e3e4>Node::Yaw </a> give You the result that You expect?

-------------------------

slapin | 2017-06-01 21:44:37 UTC | #17

Not for delta rotation

-------------------------

Modanung | 2017-06-02 03:41:42 UTC | #18

Are you aware of the `TransformSpace space` function parameter which is TS_LOCAL by default?

-------------------------

slapin | 2017-06-02 05:33:47 UTC | #19

Yeah, use TS_WORLD. (20 chars filler)

-------------------------

