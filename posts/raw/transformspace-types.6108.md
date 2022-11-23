lheller | 2020-04-22 13:11:14 UTC | #1

Hi!

Can anybody give me an explanation what's the difference between each TransformSpace types (local, parent, world) and some hints, how to visualize the differences using nodes and simple shapes, like boxes, spheres, etc. ? BTW type Local is more or less clear for me, but the Parent and World not really.

Thank you

BR,

Ladislav

-------------------------

lheller | 2020-04-22 13:47:37 UTC | #2

BTW I looked in the samples but there is no sample with TS_PARENT.

-------------------------

SirNate0 | 2020-04-22 16:06:41 UTC | #3

The different modes just describe what coordinate system the transformation happens in. Translations are probably easiest to understand - if you translate `2.0f Vector3::FORWARD` using:
1. TS_LOCAL: you move `2.0f * node->GetWorldDirection()` in world space.
2. TS_PARENT: you move `2.0f * node->GetParent()->GetWorldDirection()` in world space. This one is equivalent to `node->SetPosition(node->GetPosition() + 2.0f * Vector3::FORWARD)`
3. TS_WORLD: you move `2.0f * Vector3::FORWARD` in world space.

Regular functions with Node mostly work in the parent space (so the world Forward, Right, and Up vectors from the parent node at it's world position define the z, x, and y axes and the 0,0,0 point that defines the coordinate system) for functions like GetPosition(). GetWorldPosition(), of course, returns the position in the world space. GetLocalPosition() would be meaningless, as it would just return Vector3::ZERO, so it does not exist.

Scaling may make things a bit more complicated, but hopefully that gives you a good place to start.

-------------------------

