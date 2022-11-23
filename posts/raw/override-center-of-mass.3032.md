slapin | 2017-04-21 01:50:46 UTC | #1

Well, I try to make my cars properly roll over. I use trimesh collision and default center of mass
is at bottom (as it is node position for spawning). This prevents car from rolling over, even if it tries accidentally,
it always gets back to wheels. If I move node up (i.e. mesh and collision shape down) nothing changes,
it looks like it uses trimesh center as center of mass. Any ideas on how can I move center of mass?
And no, I don't want to use box as collision - I need collision details to be handled properly.

-------------------------

SirNate0 | 2017-04-22 05:42:55 UTC | #2

I think for the center of mass you may be required to move the vertices of the model itself down before export. If that's what you meant by moving the node up, then I have no idea, but here is a discussion about a similar problem from the Bullet forum you might glean something from: http://www.bulletphysics.org/Bullet/phpBB3/viewtopic.php?f=9&t=2209

 I will say that I would recommend using convex hulls or compound shapes of convex hulls if you could get away with that -- they are faster computationally and with trimeshes I have experienced some problems with objects pushing through the triangle mesh and getting stuck inside it (I think this can be avoided with well made meshes, but I like the other benefits of the convex hull myself).

-------------------------

slapin | 2017-04-22 09:17:19 UTC | #3

Yep, I use convex hull.
Not that moving geometry doesn't help at all, but it looks like body rotates around RigidBody center, but
the mass is concentrated at ConvexHull center and effect i.e. I still can't get vehicle to roll over and not go back to wheels :( But if it rolls it rolls around new RigidBody center. If I put center too far it gets into yoyo effect.
It all looks very strange.

-------------------------

