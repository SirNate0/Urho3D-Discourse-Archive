grokko | 2021-03-28 21:33:36 UTC | #1

Hello,
  I have a 'beam' that is a scaled StaticModel cylinder and a weapon whose bullet is a StaticModel too.
What material Technique may i use to blend these two together?

grokko

-------------------------

glebedev | 2021-03-30 12:58:55 UTC | #2

it isn't clear what you want to achieve. May I ask you for a simple sketch or reference image?

-------------------------

grokko | 2021-03-30 22:19:15 UTC | #3

Hi,
Sorry if my question wasn't clear...

How can I blend two StaticModels together?

I have a LogicComponent which shoots a queue of StaticModel Nodes into the space. They're load balanced so they
shoot and perform really well...but sometimes when I launch a flurry of shots in the space, and then turn a couple of degrees and launch more...the bullet Nodes hit each other and explode
on each other,,,

I'm kinda new to the great Urho so I suppose such a device of blending might be a technique?

Mike

-------------------------

glebedev | 2021-03-30 22:53:34 UTC | #4

Sounds like you have physics issue. You have to move bullet colliders to a separate layer and disable collisions with the same layer. This way bullets won't collide with eachother only with non-bullet objects.

-------------------------

grokko | 2021-03-31 00:20:56 UTC | #5

> You have to move bullet colliders to a separate layer and disable collisions with the same layer.

Hi,
  Thanks for helping! You mean like this..?

bd->SetCollisionLayer(1);		        
		bd->SetCollisionEventMode(COLLISION_NEVER);

wherein 'bd' is a RigidBody pointer.

I tried a couple combinations, still nothing..

Mike

-------------------------

WangKai | 2021-04-01 14:56:46 UTC | #6

// for bullets
body->SetCollisionLayer(0x01);
body->SetCollisionMask(0x10);

// for targets
body->SetCollisionLayer(0x10);
body->SetCollisionMask(0x01);
 
You can use this layer and mask  patten to avoid collision btw bullets.

-------------------------

glebedev | 2021-04-29 08:17:37 UTC | #7

so the layer is also a bitmask?

-------------------------

Batch | 2021-04-29 18:05:35 UTC | #8

Yes. It's super easy to use, too. Here's a header file for dealing with collision layers that I used in a project recently:

```cpp
#pragma once

// Collision layers and masks are &'ed together to determine if a collision event should occur.

namespace CollisionLayer
{
    static const unsigned int None = 0;
    static const unsigned int Controllable = 1 << 0;
    static const unsigned int Static = 1 << 1;
    static const unsigned int Platform = 1 << 2;
    static const unsigned int Projectile = 1 << 3;
    static const unsigned int All = -1;
}

namespace CollisionMask
{
    static const unsigned int None = CollisionLayer::None;
    static const unsigned int Controllable = CollisionLayer::Static | CollisionLayer::Platform | CollisionLayer::Projectile;
    static const unsigned int Static = CollisionLayer::Controllable | CollisionLayer::Projectile;
    static const unsigned int Platform = CollisionLayer::Controllable | CollisionLayer::Projectile;
    static const unsigned int Projectile = CollisionLayer::Controllable | CollisionLayer::Static | CollisionLayer::Platform;
    static const unsigned int All = CollisionLayer::All;
}
```

The CollisionLayer values are passed as the Layer, and the CollisionMask values are passed as the Mask. In a sense, the Layer is what the thing *is* and the Mask is what the thing *collides with*. In the above example we say our Controllable types (the player) can collide with Static/Platform/Projectile, and that our Projectile types can collide with Controllable/Static/Platform. Projectiles will not collide with other Projectiles as it is currently configured, but you can easily change that by using

```cpp
static const unsigned int Projectile = CollisionLayer::Controllable | CollisionLayer::Static | CollisionLayer::Platform | CollisionLayer::Projectile;
```

To use this, you just set the Layer and Mask of each object to their corresponding values:

```cpp
auto characterBody = characterNode->CreateComponent<RigidBody>();
characterBody->SetCollisionLayerAndMask(CollisionLayer::Controllable, CollisionMask::Controllable);

auto floorBody = floorNode->CreateComponent<RigidBody>();
floorBody->SetCollisionLayerAndMask(CollisionLayer::Platform, CollisionMask::Platform);

auto missileBody = missileNode->CreateComponent<RigidBody>();
missileBody->SetCollisionLayerAndMask(CollisionLayer::Projectile, CollisionMask::Projectile);
```

The `SetCollisionLayerAndMask()` calls become trivial, and I find the collision logic is easier to configure. It's also easy to add more Layers and Masks.

-------------------------

glebedev | 2021-04-29 18:20:38 UTC | #9

I just though that layer is a bit index, not a bitmask itself. Good to know before I spent hours debugging it :)

-------------------------

