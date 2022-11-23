devrich | 2017-01-02 01:02:54 UTC | #1

In my testing; I have made a model and I would like to "add" a geometry to be used specifically for "physics only" and I have a couple quesitons if I may?

In my model the idea is to have the physics be basically a cude or a sphere that would completely encapsulate the actual model inside it.  Think of those bouncing balls at toy stores that are clear and contain a colorful object inside:

[code]MyModel.mdl
'----Outter-Most-Physics-Only-Geometry
       '----Geometry1
             '----Geometry2
                   '----Geometry3
                        '----Geometry_n
[/code]



1:  How to tell Urho3D to use that specific "phsics geometry" for the physics calculations? ( and _ONLY_ use that specific geometry for physics calculations and _not_ use any other geometry in the .mdl ) ?

2:  I am thinking about setting a material to this "physics only" geometry to be 100% transparent -- but do i 'have' to do that or should I just leave it with-out a material ?

?

[i][u]Edit:[/u][/i]  Essentially; I want "Bullet Physics" to do it's calculations on the outside object ( ball, box, capsule, whatever.. ) _but_ have the "Renderer" render the inside geometry while 'ignoring' the outside physics shape.... I hope i'm making sence because as normal and simple as this seems; i appear to be a little lost  :blush:

[i][u]Edit:[/u][/i] I mean is it something simple like just naming my "physics-only-geometry" something specific like "BulletPhysicsONLY" ?


[u][i]Edit:[/i][/u] Another way of looking at this is the idea that we could have say a "ghost" character and have 'only' the hands, feet, and head ( these would all be separate geometries ) be detected by the physics system _but_ leave the other parts not detected by the physics.  This sounds crazy but would actually make for a pretty good ghost game in which all your attacks go through the ghost character but when they hit or kick you ( or other objects ) then the physics reacts on you/the environment and if you hit them then the physics reacts on them.... You could even design such a ghost game that you 'have' to destroy all the physics parts ( hands, feet, head ) to beat the character ( maybe a boss character )...

So I have some ideas ..

-------------------------

jmiller | 2017-01-02 01:02:56 UTC | #2

Hello,

The Physics section of the docs should be useful reading:
[urho3d.github.io/documentation/H ... ysics.html](http://urho3d.github.io/documentation/HEAD/_physics.html)

There are RigidBody, CollisionShape, and Constraints and some good details.
Several samples demonstrate the use of these, like [b]19_VehicleDemo[/b]

[b]13_Ragdolls[/b] demos rig setups.

CollisionShape is independent from viewed models (but it can be constructed from them) and normally they are not rendered, but you can DrawDebugGeometry and samples demonstrate this.

There are several simple, fast shapes like box, sphere, capsule.. SetConvexHull() constructs one from a convex Model.. SetTriangleMesh constructs one from a non-convex Model.. You can also make compound shapes.

-------------------------

devrich | 2017-01-02 01:02:56 UTC | #3

I've read over the Physics page before but after going through the RagDoll sample; some of the concepts in the Physics page make more sence now.

[quote="carnalis"]...
[b]13_Ragdolls[/b] demos rig setups.
...
There are several simple, fast shapes like box, sphere, capsule.. SetConvexHull() constructs one from a convex Model.. SetTriangleMesh constructs one from a non-convex Model.. You can also make compound shapes.[/quote]

"compound shapes" That's apparently exactly what I needed, many thanks! :smiley:


[quote]Both a RigidBody and at least one CollisionShape component must exist in a scene node for it to behave physically (a collision shape by itself does nothing.) Several collision shapes may exist in the same node to create compound shapes. An offset position and rotation relative to the node's transform can be specified for each. [/quote]



[quote="carnalis"]...CollisionShape is independent from viewed models (but it can be constructed from them) and normally they are not rendered, but you can DrawDebugGeometry and samples demonstrate this....[/quote]

DrawDebugGeometry ( [url]http://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_rigid_body.html#a237f7b27735f620d5e2b114a4027092f[/url] ) -- This is something I think I'm going to experiment with to see what all  can get out of it, thanks for that :slight_smile:

-------------------------

