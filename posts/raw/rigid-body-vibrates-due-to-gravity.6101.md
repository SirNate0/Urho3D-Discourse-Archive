NessEngine | 2020-04-19 19:22:24 UTC | #1

Hi all,
I created a floor with custom geometry collision shape, and few rigid bodies.
I noticed that all bodies are vibrating while on floor, relative to gravity force (the stronger the gravity - the bigger the shake). If I disable gravity, or reduce it by a lot, vibrating stops (but then not enough gravity..).

Any idea what could be the problem and how to fix it?
This is how I create the bodies:

    var rigidBody = rigidBodyContainer.CreateComponent<Urho.Physics.RigidBody>();
                    rigidBody.SetAngularFactor(new Vector3(0, 0, 0));
                    rigidBody.Mass = 75;
                    rigidBody.Friction = 5f;
                    rigidBody.Restitution = 0f;
                    rigidBody.SetCollisionLayerAndMask((uint)collisionLayer, (uint)collisionMask);

Gravity vector is 
`new Vector3(0, -450, 0)`

Less than that is too slow. Is this a sign my scene is too big btw? Or a normal value?

Thanks!

-------------------------

SirNate0 | 2020-04-19 20:51:18 UTC | #2

Maybe decrease friction and gravity? Unless your working on Jupiter or in inches or something that is far too large for a gravity vector on Earth at least.
How large is your scene, you just have the gravity vector?

-------------------------

NessEngine | 2020-04-20 20:43:57 UTC | #4

@SirNate0  Thanks, already scaled down my scene it still shakes. Changing friction doesn't change it.

@jmiller  Thanks but I know all these stuff, already played with substeps, restitution and all that jazz. In fact, I tried every single public setter available and the only thing that affected the shaking was substep, but I was only able to make it worse.. :confused:
As I mentioned, I switched to default gravity now.

-------------------------

Lumak | 2020-04-20 21:12:10 UTC | #5

There was physics jitter problem which was found and fixed by 1vank sometime ago:
https://github.com/urho3d/Urho3D/issues/2491

Perhaps you don't have this update.

-------------------------

NessEngine | 2020-04-20 21:21:21 UTC | #6

Interesting, it looks very similar, but in my case jittering stops when body goes to sleep so I'm not sure its it. I'll check it out!

-------------------------

NessEngine | 2020-04-20 22:14:25 UTC | #8

OK solved! I don't know if its undefined behavior and I did something silly or a bug, but I attached two custom collision shapes to the same node with a single rigid body (floor + walls), and while everything seemed to be working and collision was overall OK, it created the jittering. Note that the collision shapes were not actually on each other or anything, just sharing same node. + they were static (mass = 0). But I guess its still problematic.

I split it into separate nodes and now everything is smooth. Thank you all for the tips!

-------------------------

