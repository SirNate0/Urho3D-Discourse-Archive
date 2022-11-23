Elendil | 2018-12-22 11:10:04 UTC | #1

I struggle how to create collisions for bullets, missiles and all moving objects from shooting weapons. 

I take into consideration Bullet (engine) for that, but I am not sure if isn't take too much performance. 
I thinking about, do it with raycast, but I don't know how to raycast for objects like spheres or objects with custom shapes, because raycast is only 1dimensional line (ray from start point in to end point) and I need something like area damage for explosions. Imagine, when grenade explode near 4enemies, it affect all 4 enemies within explosion range.

What is best solution for that?

-------------------------

Virgo | 2018-12-22 13:42:20 UTC | #2

[SphereOctreeQuery](https://urho3d.github.io/documentation/1.7/class_urho3_d_1_1_sphere_octree_query.html)

-------------------------

Modanung | 2018-12-22 15:36:05 UTC | #3

You may also look into `PhysicsWorld::SphereCast(result, ray, radius, maxDistance)`, `PhysicsWorld::GetRigidBodies(result, sphere)` or [similar functions](https://urho3d.github.io/documentation/1.7/class_urho3_d_1_1_physics_world.html).
In some cases you may want to use triggers instead. These rigid bodies - that had `SetTrigger(true)` called - will signal physics events without any forces being applied as a result.

-------------------------

Elendil | 2018-12-22 15:38:59 UTC | #4

Thanks.

One thing, what if bullet is going too fast? I turn ContinousPhysic Detection (I can't remember the right name) and fast moving camera isn't going throught objects anymore. 
But from documentation, is mentioned it can slow down performance. Imagine I want have machine gun which shoot lot of bullets in high speed. Is it ok to make bullets with Bullets physic engine? Or raycast is better solution? 
Maybe for player character it is not cost performance, but imagine if they will be enemies with machine guns too.

-------------------------

Modanung | 2018-12-22 16:04:44 UTC | #5

[quote="Elendil, post:4, topic:4771"]
Is it ok to make bullets with Bullets physic engine? Or raycast is better solution?
[/quote]

Ironically you're probably better off by indeed casting a ray (or several consecutive ones).

-------------------------

Elendil | 2018-12-22 16:09:49 UTC | #6

Ok.
My idea is create object (simple bullet maybe billboard with bullet texture) and it will be casting ray for object detection as he travel in scene. It is good idea? Only problem is, if he will moving fast, but I have some ideas how to make it correct. Or it is better only cast ray and make damge for first ray hit? But this is unrealistic when objects will be in different distance.

-------------------------

Dave82 | 2018-12-22 21:42:35 UTC | #7

You can use raycast with a bullet velocity as the ray length. Perform raycast between bulletPos and bulletPos + bulletVelocity if no hits were registered you're safe to move your bulletPos to bulletPos + velocity.
keep repeating this process until you hit something or your bullet reach max distance (goes out of level bounds).

-------------------------

SirNate0 | 2018-12-24 18:13:31 UTC | #8

You'd actually want to ray cast with bullet velocity * time since last frame or it will overshoot. If they're slow bullets you could also segment it to trace an approximately parabolic arc from gravity (but of course that would be somewhat more expensive).

-------------------------

smellymumbler | 2018-12-26 16:46:34 UTC | #9

Just so you know: In my game, bullets are affected by gravity and there's penetration logic. Instead of using a rigid body, I just cast rays all the time. Much less buggy.

-------------------------

Elendil | 2018-12-29 10:13:52 UTC | #10

Thanks all for posts. Solution like use bullet velocity and time for the ray distance was what come to my mind when I started thinking about it. But thanks to confirm the idea.

I did bullets with raycast system, which do damage to object. I am going try something with area damage.

[smellymumbler](https://discourse.urho3d.io/u/smellymumbler) thanks for share experience.

-------------------------

Virgo | 2019-02-12 10:04:44 UTC | #11

:laughing:how did you calculate the impact of the bullets
if we used raycast for bullets, how do we calculate the impact and apply the force on the hit object?

-------------------------

smellymumbler | 2019-02-12 16:40:07 UTC | #12

Well, that depends on your game. In my game, impact and force and directly dependent on the character's attributes + dice roll. It's not meant to be realistic. So, the distance traveled by the bullet is the only thing that matters to me, since I used it to roll some dices versus the characters luck, perception, etc. I could add other interesting variables, like wind and so, but again, not trying to be realistic.

Some research material:

http://hyperphysics.phy-astr.gsu.edu/hbase/grav.html#bul
https://revisionmaths.com/advanced-level-maths-revision/mechanics/projectiles
https://medium.com/@3stan/how-do-bullets-work-in-video-games-d153f1e496a8
http://www.garagegames.com/community/forums/viewthread/74911

-------------------------

Virgo | 2019-02-13 05:42:47 UTC | #13

:joy:i didnt go to school, so i have not much knowledge in math or physics.

the only thing im thinking about (now) is how to calculate the impact of hits.
e.g. when shooting a small independent rock on the ground, how should it react to the hit

-------------------------

Virgo | 2019-02-13 06:10:44 UTC | #14

my current idea is to make every bullet a physical object, but with different collision mask from game world, make them not to collide with game objects. then subscribe to E_PHYSICSPOSTSTEP, raycast from last frame's position to current position to determine hit targets. but i stuck right here: i totally have no idea how to implement the logics here :slight_smile:

-------------------------

Leith | 2019-02-13 07:32:36 UTC | #15

My character class is derived from LogicComponent.
This gives me FixedUpdate method which I can override, it is called after the physics update.
I would recommend using raycasts to simulate bullets, don't try to make 3D physics bullet objects which are very small, and send them at very high velocities, it will lead to trouble.

Bullet Physics works best with objects no smaller than a tennis ball, and no larger than a bus.
We can "fake" a physics bullet in a single frame, using a raycast.
We don't need to draw that bullet, though we may wish to draw the damage it did when it hits something. Usually, we don't try to draw bullets, because they are assumed to be moving so fast that we can't really see them. We can use things like trail effects to draw them if we really feel like it.

[EDIT] You are correct in thinking that CCD will help with the case of fast-moving objects, but it's not cheap, and there are still going to be numerical issues with using very small objects.
I needed to use CCD to prevent tunneling in a watermelon racing game, and that melon was 1x1.6 METERS in size, and moving at around 120KPH

-------------------------

Virgo | 2019-02-13 07:32:21 UTC | #16

the reason i make bullets real physics objects is the Bullet physics engine will do the gravity effect, and also make it simpler to do wind effect (just some Body::ApplyForce())
and the bullet can still be seen within the game world, tho its quite hard :v

-------------------------

Leith | 2019-02-13 07:39:32 UTC | #17

The longer you spend making games, the more limitations you will encounter. The real magic is not to try to solve every problem, but to find an acceptable workaround, which does what you want, and then find a way to make it look pretty. First make it work, then worry about what it looks like. In your case, my suggestion to use raycasts will let you get the code working quickly, even though you can't see any damage being done, you will be able to detect the hits and deal the damage and make it work. Once it works, you can make decisions about how that should look, and run into the next bottleneck / limitation.

As for learning math, man I have a degree and I still can't read greek notation - I'd love to teach you what I can, as you find you need it, so don't hesitate to ask - most game math boils down to dot and cross products, interpolation, and a bit of trigonometry - it can be learned on demand, as you find you need it

-------------------------

Virgo | 2019-02-13 07:39:18 UTC | #18

:joy:i mean bullets are made physical objects just to simulate their movement, and use raycast to detect hit targets.
and the problem here is i dont know how to apply "reaction" to the hit targets

-------------------------

Leith | 2019-02-13 07:48:50 UTC | #19

Well I did suggest that how things look should come last, but you could for example, just change the material colour of a dead guy, just to display that something got hit, and i would also look at the Decal sample, which lets you shoot splats on the world
Bullet won't do ALL the math for you, at some point you're gonna need to get to grips with some math, I know it sucks, but if you can use it for something cool, it sucks less.

When I am writing something new, I often just spew some text to the console output, like "oh I got hit"
Debug Spew is underrated.

-------------------------

Virgo | 2019-02-13 07:48:27 UTC | #20

oops, im talking about the reaction of the impact
like shooting a small rock, the rock will "be pushed away"

im thinking of using `RigidBody::ApplyForce()` to make the reaction, just have no idea how to calculate the force for it

sry if my expression makes you confused, im not good at language either

-------------------------

Leith | 2019-02-13 08:14:24 UTC | #21

for ApplyForce, you need to pass in a 3D Vector - you definitely need to learn about vectors. They are imaginary arrows in space, that have a direction, and a magnitude. ApplyForce needs a Vector with direction and magnitude. Magnitude can be thought of as length, but it can also be thought of as force. Vectors are easier to learn about in 2D at first, but the ideas and maths all works in 3D as well, and is central to game programming. Nothing worth doing is easy, I am here to help you if you need help to understand the maths for games - you don't need to become a math whiz, but you need certain math tools in your toolkit.

When hiring in my previous company, my first question was always "Give me an example of how a Dot Product can be used in 2D or 3D games." The reason that I ask this, is because when I started out, I had no maths either, and I had no answer to that question. There are lots of correct answers, but I had no idea, so this gave me an indication about how experienced the programmer was in terms of game development.

-------------------------

Virgo | 2019-02-13 08:17:16 UTC | #22

i have been messing with google on this calculation these days, and almost every equation i found related to forces involves acceleration factor, but since in my case the "collision" is determined by a `Raycast()`, so there is no acceleration at all.

the only values i have are the mass of both collision objects (the bullet and the hit target) and the velocity of the bullet, i cant really "fabricate" a force for the hit target.

i dropped out too early, the only force i learned at school is gravity :confused:

edit: i think the force F=ma may not be the force i want at all

-------------------------

Leith | 2019-02-13 08:41:42 UTC | #23

Don't worry about it too much - ok so lets say we have a direction vector, coming from some point of origin in the world - now we scale it up, we give it magnitude, and we TWEAK the numbers until we like the result - this is perfectly ok. Don't get too caught up on the formulas, just worry about getting the result you want - true understanding comes in small steps, you don't need to know everything to get results, and there are a LOT of people working in the game industry fulltime who have NO IDEA what they are doing, but still manage to keep their jobs.

F=ma is exactly what you want, I suspect you're worried about acceleration. It is a magnitude. Mass is a scalar. A scalar is just a multiplier value. We multiply them together to get the force. You could replace them both with a single Force value and ignore the formula, and it will still work - so force gives you what? just another scalar, to be applied to a unit-length direction vector.

I don't expect you to really understand, but I hope you get the feeling that you can just play with the values and get a result you like. This is the basic stuff for games. At the other end, we have all hell breaking loose, with things like eigenvectors, hamiltonians, and other strangely named beasts. Most of that stuff is not immediately relevant to making games, and you may never need it, but there is definitely a basic level of maths needed, and we can certainly concentrate on just what we need, when we need it.

-------------------------

Virgo | 2019-02-13 09:11:07 UTC | #24

are you suggesting i should just apply some random forces to the hit targets? (I apologize to my english teacher :rofl:) 
but i want the bullet part to be realistic :expressionless: 

ignore other factors
lets say the hit target stops the bullet (so that means the target takes all the kinetic energy that bullet had, right?)
and cuz ![image|94x28](upload://fubwEGDnCvzBvslGnGKTkw93O1Z.png) 
we get new energy applying to the target
E_new
= 1 / 2 * m_target * v_new * v_new 
= 1 / 2 * m_bullet * v_bullet * v_bullet

and so we can get
v_new 
= std::sqrt(m_bullet * v_bullet * v_bullet / m_target)

then combine it with the target's origin velocity

    Vector3 finalVelocity = target.GetLinearVelocity() + v_new;
    target.SetLinearVelocity(finalVelocity);

can i do that? pardon my ignorance and imagination xD

-------------------------

Leith | 2019-02-13 09:28:41 UTC | #25

You're doing too much thinking - I understand that you want to calculate a ballistic trajectory, the math is not this complex given some "known values" such as the mass of the bullet, its direction and its exit velocity

-------------------------

Virgo | 2019-02-13 09:32:57 UTC | #26

i just wanted a parameter for `target::ApplyForce()`
make its movement react to the hit...

-------------------------

Modanung | 2019-02-13 09:39:56 UTC | #27

For bullet impacts I'd use this `RigidBody` method:
```
/// Apply impulse at local position.
void ApplyImpulse(const Vector3& impulse, const Vector3& position);
```

-------------------------

Virgo | 2019-02-13 09:41:21 UTC | #28

:laughing:and what value should i pass to this ApplyImpulse()?

-------------------------

Modanung | 2019-02-13 09:46:43 UTC | #29

> F = m * a

Force (in Newton) equals mass (in kg) times acceleration (in m/s).

This can both be used to calculate a realistic impulse from the bullet and a rewarding impulse on the target. Experimentation also gets you pretty far. Just try out some numbers from the mundane to the insane.

-------------------------

Leith | 2019-02-13 09:45:20 UTC | #30

Impulses work differently to forces - they do not account for Time, they happen "instantaneously".
An impulse is defined as an instantaneous change of velocity.

Forces are more generally more accurate.
Bullet uses impulses to correct object penetrations, which is a kind of math cheat.
In the physical world, forces are almost never applied instantly.

-------------------------

Leith | 2019-02-13 09:47:23 UTC | #31

When a tennis ball hits a wall, it deforms, it absorbs energy, it then acts as a muscle, and returns that stored energy, and this all takes time.

-------------------------

Virgo | 2019-02-13 09:48:13 UTC | #32

:joy:its going more and more complicated for me

-------------------------

Leith | 2019-02-13 09:48:57 UTC | #33

Let's start with some basics like vector math, and work our way up ;)

-------------------------

Leith | 2019-02-13 09:50:54 UTC | #34

Your first thing to learn is the difference between a vector, generally, and a unit vector - what is a unit vector, why is it special.

-------------------------

Modanung | 2019-02-13 09:52:38 UTC | #35

Don't go slapping him with complex quantomic dot productometry: You'll scare him to math! :books::stuck_out_tongue:

-------------------------

Virgo | 2019-02-13 09:54:18 UTC | #36

i guess a unit vector is a vector which length is exactly one unit... it* can be used to indicate direction :thinking:

-------------------------

Modanung | 2019-02-13 09:54:20 UTC | #37

You _are_ a quick learner.

-------------------------

Virgo | 2019-02-13 09:54:51 UTC | #38

:rofl:i spent days on this thing before

-------------------------

Modanung | 2019-02-13 09:56:09 UTC | #39

Rest assured, there's enough knowledge to spend an entire life on.

-------------------------

Leith | 2019-02-13 09:57:38 UTC | #40

There is more to this idea of a unit vector - let's drop back to 2D, and imagine a circle, whose radius is length of ONE - any point on the circle, defines a ray of unit length - we can start to think in terms of angles between two vectors, and this also works in 3D - the way we think about vectors, determines how well we can apply them in games.

-------------------------

Leith | 2019-02-13 10:01:09 UTC | #41

Back in 2D circle land, we can talk about sine and cosine, which give us power over triangles, a concept I could best explain with a picture, but all triangles are just made from two vectors - even 3d triangles

-------------------------

Virgo | 2019-02-13 10:02:31 UTC | #42

angles, are they like (Vector2- Vector1).Normalized() ? :bowing_man:

-------------------------

Leith | 2019-02-13 10:02:04 UTC | #43

there are a few ways we can measure angles between vectors, the most common is called arc cosine, or acos - but it can't tell us about the direction of the angle, just how big the angle is

-------------------------

Leith | 2019-02-13 10:02:56 UTC | #44

the more you get into game dev, the more there is to learn, its pretty cool, just the basics will get you by, but theres always more

-------------------------

Leith | 2019-02-13 10:05:33 UTC | #45

Let's talk about Normalized for a moment - what does that do to a vector?

-------------------------

Virgo | 2019-02-13 10:06:05 UTC | #46

i lost my efficency learning new stuff, so normally i just ask for pseudo code to a solution.

-------------------------

Leith | 2019-02-13 10:06:36 UTC | #47

It throws away the Magnitude, and forces the vector to have a length of 1, so now its just a direction

-------------------------

Leith | 2019-02-13 10:07:17 UTC | #48

This is a useful thing, but often abused, all it does, is turn any vector, into a direction vector

-------------------------

Leith | 2019-02-13 10:08:28 UTC | #49

It's worth looking into HOW normalizing works, because normalizing crops up in a few places other than just basic vector math, and its meaning is the same

-------------------------

Virgo | 2019-02-13 10:09:29 UTC | #50

    void Normalize()
    {
        float lenSquared = LengthSquared();
        if (!Urho3D::Equals(lenSquared, 1.0f) && lenSquared > 0.0f)
        {
            float invLen = 1.0f / sqrtf(lenSquared);
            x_ *= invLen;
            y_ *= invLen;
            z_ *= invLen;
        }
    }
    Vector3 Normalized() const
    {
        float lenSquared = LengthSquared();
        if (!Urho3D::Equals(lenSquared, 1.0f) && lenSquared > 0.0f)
        {
            float invLen = 1.0f / sqrtf(lenSquared);
            return *this * invLen;
        }
        else
            return *this;
    }

these are from engine source :rofl:

-------------------------

Virgo | 2019-02-13 10:09:55 UTC | #51

:bowing_man: lets pause here, gotta have my dinner

-------------------------

Leith | 2019-02-13 10:13:34 UTC | #52

cool man, we'll pick this up later, I'll like you to try to explain what normalizing is and how it works given you can see the code. It's basic stuff for me, and I'm pretty laid back and happy to share my brain, lots of people have contributed to my learning experience, I want to pay it forward.

-------------------------

Leith | 2019-02-13 10:45:03 UTC | #53

I really have to say, what a pile of shit, that sourcecode is, before I even begin to explain how it really works - I hate API that hide math behind constructs like that - no mention of a dot product

```
float lenSquared = LengthSquared();
```

That hideous looking thing, is really, float lenSquared = dot (this vector, and also this vector);
One thing we do learn on the way, is that the dot product of a vector with itself, is its squared length, which we can only learn, by learning how the math works.

-------------------------

Modanung | 2019-02-13 10:50:11 UTC | #54

Wrapping reused code in a function is common practice in object oriented programming.
Indeed this does not conserve _mathematical_ elegance.

-------------------------

Leith | 2019-02-13 10:47:47 UTC | #55

I use oop as I see fit, I am starting to mix pure c with urho, because I am lazy, and because I am lazy like a fox
off topic police will be here any moment

-------------------------

Leith | 2019-02-13 10:52:06 UTC | #56

game development is not my passion, its my calling, I trained for this with robots spitting hot metal at me, getting the decimal point in the wrong place in one line of code caused the 30 foot long monster to try to tear itself apart, it was not acceptable to make mistakes

-------------------------

Modanung | 2019-02-13 10:54:25 UTC | #57

[quote="Leith, post:56, topic:4771"]
it was not acceptable to make mistakes
[/quote]

Yet oh so tempting. :P

-------------------------

Leith | 2019-02-13 10:55:03 UTC | #58

ok so sometimes, I would stall the motor, and warm up my lunch on it

-------------------------

Leith | 2019-02-13 10:58:23 UTC | #59

robots have a sense of humour, and put up with a lot of shit, except putting the decimal point in the wrong place, this is the cardinal sin - I coded up to seven axes, which is just like a bone hierarchy in a game

-------------------------

Leith | 2019-02-13 11:03:12 UTC | #60

its really hard man, to code for many axes, when theres hammers smashing everywhere around you - and not make any mistakes, no errors, no floating point issues, no dot in the wrong spot

-------------------------

Modanung | 2019-02-13 11:05:32 UTC | #61

[quote="Leith, post:59, topic:4771"]
robots have a sense of humour
[/quote]

I was pondering earlier today how a proper AI might only be able to laugh uncontrollably (mainly at us) after it took in enough information.

-------------------------

Leith | 2019-02-13 11:03:59 UTC | #62

I wish I could show you my work on gpu nnai for games, it scared the shit out of me

-------------------------

Leith | 2019-02-13 11:04:37 UTC | #63

we're wayyy off topic, take it to pm

-------------------------

Modanung | 2019-02-13 11:07:14 UTC | #64

:cactus: :oncoming_police_car:

-------------------------

Virgo | 2019-02-13 11:08:32 UTC | #65

[quote="Virgo, post:11, topic:4771, full:true"]
:laughing:how did you calculate the impact of the bullets
if we used raycast for bullets, how do we calculate the impact and apply the force on the hit object?
[/quote]

lets back to this very basic question, should we? 😂

-------------------------

Modanung | 2019-02-13 11:14:21 UTC | #66

Elaborating on my earlier post:

https://discourse.urho3d.io/t/collisions-ohysics-for-missiles-bullets-explosions-etc/4771/29

So you could multiply the mass of the bullet by it's speed and apply that force to the target hit. That would be somewhat realistic. But you may want to increase the force and throw realism out the window, like they do in Hollywood, making a single bullet throw a person through the air.

-------------------------

Leith | 2019-02-13 11:13:35 UTC | #67

ok so we have a ray, it has a direction, and theoretically infinite length, but for the purposes of working out the force, we have direction, mass, and force, where force is, in terms of guns, related to the exit velocity - we can compute the force that left the gun, apply drag and friction and any other slowdowns, and at the end of its travel, when it hits the target, we can make some assumptions, based on what we think we know about physics - its a game, we get to play with the input values, and make them plausible in our game - wait thats wrong, we need to make the OUTCOME plausible, and how we did it, what math cheats we took, are not relevant to the user

-------------------------

Leith | 2019-02-13 11:18:58 UTC | #68

the magic in the magic show, is not in the hand or hat of the magician, its in his assistants underwear, its mostly slight of hand, doing the actual math is too slow, so we find ways to approximate it and get it done, getting shit done is the word of mouth way the game industry works, if you can get shit done, you get a job, and if you cant, you get the sack, its not a perfect world - but you can learn real magic from people around you, and apply it

-------------------------

Virgo | 2019-02-13 11:55:36 UTC | #69

[quote="Modanung, post:66, topic:4771, full:true"]
So you could multiply the mass of the bullet by it's speed and apply that force to the target hit
[/quote]
:thinking: but the mass times speed wont equal force at all

-------------------------

Leith | 2019-02-13 12:40:59 UTC | #70

assuming the bullet is moving in a perfect vacuum, the force will be speed times mass, a basic newtonian physics constant, which I think personally is bullshit, because nothing is perfect, and the universe (mostly) sucks

In a few weeks, I am going back to school, to get a teaching certificate

Newton was very bright, but he did not define our physical world, he merely attempted to define it using the state of the art math he had back then.

-------------------------

Virgo | 2019-02-13 12:40:19 UTC | #71

:rofl:i think i can trust you guys in this one...

now lets talk about explosions, can i do a great number of `RaycastSingle()`s from the explosion origin to all different directions with the length being its effective diameter, instead of doing a `SphereCast()`?
and i wonder if this can be possibly done in 1/60 second?

cuz if i do a SphereCast() to find out the targets being affected by the explosion, i cant think of a way to determine if those targets are behind covers or not :thinking:

-------------------------

Leith | 2019-02-13 12:46:15 UTC | #72

Just, no. you can do a few ray casts, but a shitload of raycasts costs a shitload. Your app will have a heart attack and you'll feel foolish for trying to do a death star explosion with a physics engine.
In physics you get what you paid for, which is why in games, we try to avoid paying full cost

By the way, the original death star explosion in star wars took months, using supercomputers of their era

-------------------------

Virgo | 2019-02-13 13:21:48 UTC | #73

:sob:then any suggestions for determining if a target is behind cover or not? if im to use `SphereCast()`?

-------------------------

jmiller | 2019-02-13 14:03:21 UTC | #74

Hi,

https://discourse.urho3d.io/t/how-do-you-choose-collision-masks-layers-solved/957

-------------------------

Modanung | 2019-02-13 18:00:32 UTC | #75

[quote="Virgo, post:69, topic:4771"]
:thinking: but the mass times speed wont equal force at all
[/quote]

Ah, but it is not mass times _speed_: It's mass times _acceleration_; a _change_ in speed... and let's assume the bullet instantly comes to a full stop upon impact.
This also means that when no forces (like gravity, drag or collisions) are applied to an object it will continue at the same velocity (linear _and_ angular), in the same direction. Like an asteroid in deep space.

[quote="Virgo, post:73, topic:4771"]
:sob:then any suggestions for determining if a target is behind cover or not? if im to use `SphereCast()` ?
[/quote]

You could use a spherecast to find the objects that you would then each check with one or several raycasts for possible escaping of the blast.

-------------------------

Virgo | 2019-02-13 16:03:46 UTC | #76

[quote="Modanung, post:75, topic:4771, full:true"]
You could use a spherecast to find the objects that you would then each check with one or several raycasts for possible escaping of the blast.
[/quote]

this raycasts here is the new question, how to do them? :thinking:
i mean how do i determine the parameters for the raycasts

-------------------------

I3DB | 2019-02-13 17:38:24 UTC | #77

[quote="Modanung, post:75, topic:4771"]
You could use a spherecast to find the objects that you would then each check with one or several raycasts for possible escaping of the blast.
[/quote]

Go over some of the examples that use raycasts.

-------------------------

Modanung | 2019-02-13 17:47:00 UTC | #78

Sample using **`Octree`** raycast:
https://github.com/urho3d/Urho3D/blob/master/Source/Samples/08_Decals/Decals.cpp#L279-L305
Similarly you can use these **`PhysicsWorld`** functions:
https://github.com/urho3d/Urho3D/blob/a476f0c40114b92c2637145c24f50ccef6de5d3c/Source/Urho3D/Physics/PhysicsWorld.h#L186-L202

-------------------------

Virgo | 2019-02-14 10:06:44 UTC | #79

update: about the "force" to apply on the hit target to simulate the reaction of the bullet impact, i accidently found this momentum and its conservation principle, so there is
(subscript b means bullet, t means target)
![SharedScreenshot|460x100](upload://1W8rbAtvWvhuXNQfOZ1cdVJcX2X.jpeg) 
and so the change of target's velocity ![SharedScreenshot4|82x22](upload://mbGfmPlQR25rvqrsrTwSWhP6pJz.jpeg) ![SharedScreenshot2|220x36](upload://6uRzBIDsuRxy2Qzi0PveRciMQrx.jpeg) 
and becuz the mass of both objects and the initial velocity of the bullet when impact are known, the change of bullet's velocity are determined by game logics, ![SharedScreenshot4|82x22](upload://mbGfmPlQR25rvqrsrTwSWhP6pJz.jpeg) is solvable. 

now we can finally & simply do this:

    Vector3 finalVelocity = target.GetLinearVelocity() + change_of_velocity;
    target.SetLinearVelocity(finalVelocity);

im an idiot of logics and math, criticize me if i got anything wrong :bowing_man:

-------------------------

Modanung | 2019-02-14 20:51:03 UTC | #80

The main problem I see is the calling of `SetLinearVelocity`, this is something you want to avoid. Instead apply [forces](https://en.wikipedia.org/wiki/Force) and [impulses](https://en.wikipedia.org/wiki/Impulse_(physics)).

Also, you do not need math to just try out some numbers and (not) see their effect. :)

-------------------------

Virgo | 2019-02-14 23:16:59 UTC | #81

:disappointed_relieved:i just want the codes to generate the impact automatically so i dont need to provide a random number every time

-------------------------

I3DB | 2019-02-15 02:37:36 UTC | #82

[quote="Virgo, post:81, topic:4771, full:true"]
i just want the codes to generate the impact automatically so i dont need to provide a random number every time
[/quote]

To simulate a bullet impact I use code like this:
```
hitRigidBody.ApplyImpulse(((StereoApplication)Application).LeftCamera.Node.Direction*10, result.Value.Position);
```

So 10 times the camera direction. It's quite a powerful bullet. Spins a ragdoll right around and off it's feet.

And another example:
```
hitRigidBody.ApplyTorqueImpulse(Vector3.Up * 4);
```

-------------------------

Leith | 2019-02-15 05:07:58 UTC | #83

I would add some mention of Collision Filtering - ie, Collision Group and Collision Mask (the latter is called collision layers in Urho)

-------------------------

Virgo | 2019-02-15 05:14:32 UTC | #84

:thinking:the real question there is not if the hit targets are correctly collided or not,
but whether there are obstacles between these targets and the explosion center or not.

-------------------------

Leith | 2019-02-15 05:17:15 UTC | #85

You want to determine which object was hit first - a ray cast starts at its origin, and in theory, moves forwards, and you can return the first object that was hit, and determine if it was a wall, or not. Filtering is useful to ignore collisions with things you don't want included in the result, such as trigger (aka sensor) volumes

-------------------------

Virgo | 2019-02-15 05:20:00 UTC | #86

:rofl:im not talking about excluding walls or other non-player related game objects
im talking about how to check if any of the results are actually behind covers

-------------------------

Leith | 2019-02-15 05:21:50 UTC | #87

Ray casts only return the first thing that the ray hit - in your case, you will either be told that the ray hit a wall, or it hit a game character, so we can deduce, hey, if my bullet hit the wall, then the character was not hit.

-------------------------

Virgo | 2019-02-15 05:24:33 UTC | #88

:thinking:i think you mistook `Raycast()` with `RaycastSingle()`

and Modunung's reply you replied to had changed topic from bullet detection to explosion detection :bowing_man:

-------------------------

Leith | 2019-02-15 05:26:43 UTC | #89

Raycast is a general term, I was using it in a general sense. Yes, you want to use RaycastSingle, so you get the closest hit result, you're not interested in raycasting for multiple objects. I apologize for the confusion.

-------------------------

Virgo | 2019-02-15 05:28:12 UTC | #90

:joy:i think you are actually even more confused

so sad i cant draw, or i will draw some to explain what im really talking about

-------------------------

Leith | 2019-02-15 05:30:28 UTC | #91

You want the closest result - if you use Raycast, you'll need to find which result is closest - RaycastSingle returns the closest result - I'm not confused about that :) I've used many engines, and I've used Bullet in my own engines, I'm pretty clear about you wanting the closest hit result, not every hit. Spherecasting is where we tend to want multiple results, but if we wanted to fire a laser beam, we might want to know about all the hit objects.

-------------------------

Virgo | 2019-02-15 05:33:50 UTC | #92

:bowing_man:i think i have finished the topic on bullet detection...

and have moved to that of explosion....

-------------------------

Leith | 2019-02-15 05:39:50 UTC | #93

Excellent :slight_smile:
This is pretty easy, and also relates to your previous questions.
Step one is to use a sphere test to collect all the objects (ie rigid bodies) within range of the explosion.
Step two is to apply a Force to each collected object.
The force should have a direction based on the position of the explosion and the position of the object.
And its magnitude should be related to the distance from the position of explosion to each target object. We're using vectors with magnitude.
Typically, the force should be falling off as the square of the distance, which is how energy tends to dissipate in classical physics models, but you can use another attenuation method, including inventing your own, we just want to apply less force if the target object is further away.

-------------------------

Virgo | 2019-02-15 05:41:42 UTC | #94

:bowing_man::bowing_man::bowing_man:

and the hard one is how to detect if any target is actually behind a cover or not...

-------------------------

Leith | 2019-02-15 05:42:41 UTC | #95

ok, let me add a step.
Step one - collect list of objects inside a sphere
Step two - perform raycasts to eliminate objects that are behind cover
Step three - apply explosion forces to remaining objects in our list

-------------------------

Virgo | 2019-02-15 05:44:03 UTC | #96

and the approach to step two is my concern

-------------------------

Leith | 2019-02-15 05:50:02 UTC | #97

ok, you're missing some basic vector3 maths skills as I mentioned previously.

The vector Direction from Source to Target, is (Target.position - Source.Position).Normalized
The magnitude (or length) of that vector, is square root of ( Target.position.Dot (Source.Position))
We can calculate that using  (Target.position - Source.Position).Length( ), gee isnt it nice that Urho provides us with some shortcuts, for things like that.

We could also use other methods to compute length, such as Pythagorus Theorem, but I'm going off topic, that should be enough information for your problem.

-------------------------

Virgo | 2019-02-15 05:50:46 UTC | #98

uh uh....
im talking about this step two
[quote="Leith, post:95, topic:4771, full:true"]
Step two - perform raycasts to eliminate objects that are behind cover
[/quote]

i think we have some serious issues communicating :joy:

-------------------------

Leith | 2019-02-15 05:52:28 UTC | #99

For each possible target we collected in our sphere, we perform a raycast, from origin of explosion, to candidate object position... to do that, we need to know the direction and length of the vector that begins at the origin of explosion, and ends at the target.
If we hit a wall, then this guy is safe from the explosion, and can be removed from the list of candidates.
But if we have a direct line of sight to the target, we apply the explosion force.

-------------------------

Virgo | 2019-02-15 05:55:15 UTC | #100

but in games targets are not single points, they have shapes... shouldnt be determined with a single raycast

edit: [Modanung](https://discourse.urho3d.io/u/Modanung) talked about doing multiple raycasts, but when i asked how to determine parameters for those raycasts, he disappeared :expressionless:

-------------------------

