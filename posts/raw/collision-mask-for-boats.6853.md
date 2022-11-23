evolgames | 2021-05-17 04:20:33 UTC | #1

I see a few threads on collision masks but I still can't see what I need for my situation. I don't really get how it works. Basically, I have a water plane that I want only boats to collide with. I tried setting the water to:
Layer: 2
and the boat to:
Layer: 1
Mask: 2
but this makes other things collide with the water as well. Other combinations I tried made only the boat collide with the water, but nothing else. Do I need to make everything in my world except the water on a higher layer in this case?

-------------------------

Eugene | 2021-05-17 04:42:10 UTC | #2

[quote="evolgames, post:1, topic:6853"]
but this makes other things collide with the water as well.
[/quote]
Exclude water layer from collision masks of all other objects, maybe?
Not sure how nice it would be to do in the editor

-------------------------

JSandusky | 2021-05-17 06:52:56 UTC | #3

It's a bitwise AND test. You need to provide more information as to your intentions as to what the boat should collide with for us to know what to say. The layer is ANDed with the mask to decide whether to respond or not.

Boats are also an extremely special case, you're in for rough ride. Half of your year rough life.

-------------------------

evolgames | 2021-05-17 07:55:27 UTC | #4

Well I simply want the boat to collide with everything in the world as normal. But nothing collides with the water plane except for the boat. I can easily do an event for the collision if the water's body is a trigger but I need the forces for what I'm doing. What makes it a rough ride? You mean for collision masks or boat physics? Because the game is very rudimentary so it'll stay simple. I have some buoyancy forces and collision shapes I set up to make it bob nicely "in" the water.

-------------------------

Batch | 2021-05-17 18:11:47 UTC | #5

I have a header file I use to do this stuff (you probably saw it in another post), so I'll take a stab at it. This is just theory (and the code behind it that *should* work), so if there's something wrong then my apologies.

```cpp
namespace CollisionLayer
{
    static const unsigned int None = 0;
    static const unsigned int Controllable = 1 << 0;
    static const unsigned int Static = 1 << 1;
    static const unsigned int Platform = 1 << 2;
    static const unsigned int Projectile = 1 << 3;
    static const unsigned int Water = 1 << 4;
    static const unsigned int Boat = 1 << 5;
    static const unsigned int All = -1;
}

namespace CollisionMask
{
    static const unsigned int None = CollisionLayer::None;
    static const unsigned int Controllable = CollisionLayer::Static | CollisionLayer::Platform | CollisionLayer::Projectile | CollisionLayer::Boat;
    static const unsigned int Static = CollisionLayer::Controllable | CollisionLayer::Projectile | CollisionLayer::Boat;
    static const unsigned int Platform = CollisionLayer::Controllable | CollisionLayer::Projectile | CollisionLayer::Boat;
    static const unsigned int Projectile = CollisionLayer::Controllable | CollisionLayer::Static | CollisionLayer::Platform | CollisionLayer::Projectile | CollisionLayer::Boat;
    static const unsigned int Water = CollisionLayer::Boat;
    static const unsigned int Boat = CollisionLayer::Controllable | CollisionLayer::Static | CollisionLayer::Platform | CollisionLayer::Projectile | CollisionLayer::Boat | CollisionLayer::Water;
    static const unsigned int All = CollisionLayer::All;
}

terrainBody->SetCollisionLayerAndMask(CollisionLayer::Platform, CollisionMask::Platform);
boatBody->SetCollisionLayerAndMask(CollisionLayer::Boat, CollisionMask::Boat);
waterBody->SetCollisionLayerAndMask(CollisionLayer::Water, CollisionMask::Water);
playerBody->SetCollisionLayerAndMask(CollisionLayer::Controllable, CollisionMask::Controllable);
```

With this setup I think it should give you what you want, where the player can walk on terrain and stand on the boat, but they'll fall through the water, as would anything else that isn't a boat. Only boats collide with water, and water only collides with boats, but boats collide with everything including other boats.

-------------------------

SirNate0 | 2021-05-18 02:27:17 UTC | #6

Just throwing this out there, I don't know how realistic you're aiming for: You may want to make the water plane a trigger that everything moving will contact. That way you can apply drag forces and maybe buoyancy to other objects besides the boats that float on top. Though you'd probably have to calculate the forces yourself.

-------------------------

evolgames | 2021-05-18 02:52:18 UTC | #7

So that's what I was doing today as my alternate solution actually. Since in my world the sealevel always has water, I just had it check if the boat was below sealevel. If it is, it applies certain torques and linear forces. It actually kind of works. This is about as realistic as I intended, nothing crazy.
![ezgif.com-gif-maker|600x313](upload://5kwV9sU1A0f8NaJ8CdSO2idczM1.gif)

-------------------------

evolgames | 2021-05-18 02:46:47 UTC | #8

This looks good. Although because I'm doing Lua only the bottom part makes sense to me...

-------------------------

Batch | 2021-05-18 16:09:57 UTC | #9

When you think about the problem, it's a matter of assigning labels to objects that indicate whether they bounce off each other, or pass through each other. The Layer values are the labels (just a unique integer), and the Mask values are the collide/pass through rules. The fact that the Layer value is used as bits just means there's only 32 unique values you can use in a 4 byte integer.

Lua should be the same I would think?

In any event I envy your ability to make cool things.

-------------------------

Modanung | 2021-06-10 16:11:35 UTC | #10

Have you seen @Lumak's work from four years ago?

https://discourse.urho3d.io/t/buoyancy-testing/3001

-------------------------

evolgames | 2021-06-11 02:46:19 UTC | #11

Somehow I missed this reply. Thanks for the explanation, that makes more sense.
Should be the same, yeah, when I get back to working on boats in this game I'll try it out.
Thanks! Just a little open world project.

-------------------------

evolgames | 2021-06-11 02:47:32 UTC | #12

I haven't, this is a really good implementation!

-------------------------

