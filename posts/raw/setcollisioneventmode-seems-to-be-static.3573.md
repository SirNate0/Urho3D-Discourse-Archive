nergal | 2017-09-17 10:04:26 UTC | #1

My case is that I want different type of instances of a class to either handle collision events or not. So based on a certain property I set the collision event mode such as this:

        if(type == constants::CHUNK_TYPE_WORLD) {
            body->SetCollisionEventMode(COLLISION_NEVER);
         } else {
            body->SetCollisionEventMode(COLLISION_ALWAYS);
        }

So if the type if a world it should not care about collision events, else it should listen for such.

But the problem that I experience is that whenever I set COLLISION_NEVER mask, it seems to apply  for all bodies, not just the one I apply it for.

Are the collision masks applied to the body class and not just the instance?

Edit: It seems like collision events comes in bursts and not at every hit when I do the above if statement. But if I remove the COLLISION_NEVER mask it seems to be applied directly....strange?

-------------------------

Eugene | 2017-09-17 11:40:53 UTC | #2

I did not understand anything, sorry.
But collision masks and layers are applied per body.

-------------------------

nergal | 2017-09-17 14:05:50 UTC | #3

Sorry for my vague explanation.

I think I found my issue. If a body have COLLISION_ALWAYS and collides with a body that has COLLISION_NEVER the collision seems to never occur. Not even for the first body that has COLLISION_ALWAYS set.

Is this the expected behaviour?

-------------------------

Eugene | 2017-09-17 14:33:12 UTC | #4

[quote="nergal, post:3, topic:3573"]
Is this the expected behaviour?
[/quote]

Yes.
Collision layer describes layers that the body belongs to,
Collision mask describes layers that the body collide.
If your body belongs to nowhere, it won't collide at all.

-------------------------

jmiller | 2017-09-17 15:19:12 UTC | #5

Here is one thread about collision masks/layers, if that might help. I also added an example there.

https://discourse.urho3d.io/t/how-do-you-choose-collision-masks-layers-solved/957

-------------------------

Modanung | 2017-09-17 15:31:28 UTC | #6

This part of the PhysicsWorld uses the CollisionEventMode:
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Physics/PhysicsWorld.cpp#L866-L873

That's the great thing about Urho being open source. Searching the code often clarifies. :slight_smile:

So indeed if any of the colliding bodies has the COLLISION_NEVER event mode no event should be signalled:
```
if (bodyA->GetCollisionEventMode() == COLLISION_NEVER || bodyB->GetCollisionEventMode() == COLLISION_NEVER)
    continue;
```

-------------------------

nergal | 2017-09-17 15:33:02 UTC | #7

Thanks for all your input!

The only reason I set COLLISION_NEVER for some objects is to increase performance so that it's not receiving any callbacks. Perhaps I'm performing too early optimisation? :slight_smile:

-------------------------

