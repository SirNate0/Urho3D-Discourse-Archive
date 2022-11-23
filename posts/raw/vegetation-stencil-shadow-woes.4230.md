Lumak | 2018-05-15 11:11:47 UTC | #1

I finally got the vegetation lighting semi decent, but the shadow is foobar. It's as if only half side is shadowed. Anyone seen something similar?

[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/2/26bdf4f14faa2b63aa9811d080902a55155c8100.png[/img]

-------------------------

JTippetts | 2018-05-15 13:48:43 UTC | #2

In the material definition for your foliage, set `<shadowcull value="none" />` to disable culling of the leaves during the shadow rendering pass.

-------------------------

Lumak | 2018-05-15 13:54:05 UTC | #3

That did the trick, ty.

[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/3/343eb6473f416027ac234a95aabb7c4f14c0dc13.png[/img]

-------------------------

