friesencr | 2017-01-02 00:58:39 UTC | #1

[code]
0 0 0 // EulerAngle ToString
-1.#IND -1.#IND -1.#IND // EulerAngle ToString
[Sat Mar 29 17:52:24 2014] WARNING: Physics: Overflow in AABB, object removed from simulation
[Sat Mar 29 17:52:24 2014] WARNING: Physics: If you can reproduce this, please email bugs@continuousphysics.com
[Sat Mar 29 17:52:24 2014] WARNING: Physics: Please include above information, your Platform, version of OS.
[Sat Mar 29 17:52:24 2014] WARNING: Physics: Thanks.
[/code]

I am setting the rotation of the node holding a rigid body and the rigid body blows up.  It looks like a divided by zero think.

[code]            
Quaternion q;
q.FromLookRotation(-moveDirection, Vector3(0,1,0));
rotation = rotation.Slerp(q, .3);
node.rotation = rotation;
[/code]

Do i need to check for 0 when applying a rotation?

-------------------------

friesencr | 2017-01-02 00:58:39 UTC | #2

The FromLookRotation is the culprit. Vec3(0,0,-1) causes it to break.  Its pretty easy to hardcode a check in there.  Naive game programmer question:  is it common to have to accommodate these case specifically per case?

-------------------------

