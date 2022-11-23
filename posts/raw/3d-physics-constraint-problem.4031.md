anako126n | 2018-02-21 18:43:59 UTC | #1

Hi All,

There is probably an easy way of achieving what I want, but after several days of playing with this I just can't get my head around this issue.

I have few Nodes inside 3D Scene with RigidBodies etc. Some of these nodes have to fall on their side (either way on 3 axis, but always on one axis only. Might go left or right, front or back) without sliding (remaining in their original collision position)

See picture for visual, top part shows what I'm trying to achieve while the bottom shows what exactly happens.

![problem|465x500](upload://2jqqOEeWx4bj22nzXIN2ZkrlzgU.png)

I was trying to use constraints but with the collision enabled node wouldn't even move, with collision disabled the node was rotating around the point (main problem here is that there is no collision with the node below)

Increasing restitution makes it even more awkward and unrealistic.

I could create several point-to-point constraints and active them as required (depending on node rotation), maybe checking for position on update and rectifying as required or is there a different approach I should take?

-------------------------

johnnycable | 2018-02-21 20:41:03 UTC | #2

What's the shape of those objects is exactly?
The collider capsule object have the same shape?

-------------------------

anako126n | 2018-02-21 20:52:12 UTC | #3

Boxes exactly the same size as model, problem is that once it touches another model the bottom slides back.

This is logical, I'm trying to achieve something against physics by somehow fixing the corner point so it doesn't move either way. 

Similar to static pivot point where the object cannot get out of it, imagine a domino effect with dominoes attached to the ground on one side.

-------------------------

Modanung | 2018-02-22 13:11:22 UTC | #4

I'm thinking you might be able to achieve what you want using `RigidBody::SetLinearFactor` and `RigidBody::SetAngularFactor` on collision, combined with high friction for both the floor and tumbling block.

-------------------------

