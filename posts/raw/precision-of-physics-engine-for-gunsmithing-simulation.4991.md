mvendra | 2019-10-04 09:12:07 UTC | #1


Hello there,

Would it be possible to use Urho's physics engine to fully simulate the internal mechanisms of firearms?
I mean something like this: https://www.youtube.com/watch?v=_eQLFVpOYm4

Thanks.

-------------------------

TrevorCash | 2019-03-02 15:11:42 UTC | #2

If you turn up the iteration count in bullet you might be able to reproduce the collision effects of the hammer etc.  For things that obviously slide you would want to use sliding constraints and not rely on collision.

If you want a more accurate physics engine you can check out my PR on this page:https://discourse.urho3d.io/t/newton-dynamics-integration/1596/35

-------------------------

Leith | 2019-03-04 08:01:20 UTC | #3

Bullet has an option for using doubles (real8) instead of floats (real4) - but that setting is disabled by default. I'm pretty sure you'll be able to rebuild urho with bullet using double precision by enabling the Bullet double precision option in cmake (I use cmake-gui on linux) - I'm not so sure that urho's physics classes will respect your choice, as I don't think they use btScalar datatype, or equivalent typedef.
Simply put, this would involve changing anything that is physics related and float type to use btScalar instead - this would cause Urho to use whatever datatype Bullet is using...

It would be fairly trivial to change the datatypes used by Urho 3D physics classes to respect a configured typedef, however it would be less trivial to do the same to Urho's math classes (not impossible, but more work) - if you're willing to use Bullet math classes in place of Urho classes like Vector3 and Matrix, at least until we're satisfied that double precision is working, I'd be willing to attempt such changes for the benefit of the community, with a view to extending those changes to our math classes (I don't need to rewrite them, just change a bunch of datatypes to use a predefined type instead of floats)

There are bound to be side-effects in classes like IKSolver, but I'm up for a challenge :)

-------------------------

Modanung | 2019-03-04 09:19:07 UTC | #4

According to @cadaver, two years ago: 

https://discourse.urho3d.io/t/physics-double-precision/2682/2

-------------------------

Leith | 2019-03-04 09:28:59 UTC | #5

Yeah, it's likely to be non-trivial to completely remap Urho to use real8, but I believe we can confine this stuff to the physics classes, and cast back to floats for rendering purposes... the underlying bullet objects would be double precision, but lose precision for rendering - I did not consider angelscript integration, it's definitely not trivial, but maybe can be done in stages.
I'd be willing to have a crack at it on that basis. Hey, I don't plan to rewrite our shaders etc, that is overkill :)
I'll spend some time tomorrow evaluating the requirements, especially the reinterprets, because we can likely eliminate them in favour of a rubber type.
Man I can see all those compiler warnings about losing precision already :D

-------------------------

bvanevery | 2019-03-08 00:22:55 UTC | #6

That video you linked to, is not a *simulation*.  It is a *visualization*.  Just a series of animations meant to illustrate something.  You could certainly *visualize* a gun firing with Bullet and Urho3D.  

Without a lot of knowledge on my part, I'm going to take a wild assed guess that no, you are completely barking up the wrong tree as far as using Bullet for an accurate physical *simulation* of a gun.  To my knowledge, Bullet was designed for *game* physics.  There are inherent tradeoffs when you want things to run fast enough in real time on a computer.

I think if you designed and built a gun based on Bullet simulation, you would literally kill yourself firing the thing.  It would explode in your face.  Hey, maybe those early M16s in Vietnam were designed with the equivalent of the era?  :-)  Or was it the M14, I forget, or the M4A4, could be getting my M's mixed up.  But one of those early guns would jam and blow up in soldiers' faces.

You could make a *virtual toy* that uses Bullet and works like a real gun.  As long as you understand that this is a *virtual toy* and has no bearing on real physical materials working in the real world.  You aren't going to 3D print a gun by working with Bullet.

-------------------------

mvendra | 2019-03-08 13:25:15 UTC | #7

Hey thanks for the reply.

Yes, indeed, that video is basically an animation - not a simulation. I basically wanted to do what the video does, but without pre-animating - with actual physics simulation instead.

As for the accuracy, yes, I wanted to make a "toy" simulation - this was for an indie game, not an actual CAD program, using lots of simplifications, smokes and mirrors and constraints etc. Do you think Bullet could handle something like that?

PS. As for the service rifle you mentioned - the very earliest units of the M16 were known to jam often
because they were issued with improper ammunition. There was even a US congressional hearing about the whole thing. I don't recall reading about actual explosions on soldier's faces but it's possible it happened (that'd be very extreme!).

-------------------------

Leith | 2019-03-09 03:08:10 UTC | #8

Bullet is pretty good at intersection tests, if it's for a game, and its a small bullet moving very fast, you have basically two options: simulate the bullet with a raycast (think of a laser beam), accepting that we're no longer accounting for wind, or ballistics. The other option is to perform a convex cast, such as a spherecast (think of a sphere, extruded along a laser beam), to simulate a bullet with a shape. What we don't try to do, is simulate bullets as dynamic or kinematic rigidbodies, because Bullet starts to do weird things when the size of an object is smaller than a tennis ball, or bigger than a bus, or moving very fast - the numbers get too big, or too small, for the default single-precision floating point numbers. There is an option called CCD we can enable (continuous collision detection) which can help reduce "tunneling" for fast-moving and/or small rigidbodies, but it comes at some cost in terms of processing.

-------------------------

Modanung | 2019-03-09 20:25:11 UTC | #9

[quote="Leith, post:8, topic:4991"]
Bullet starts to do weird things when the size of an object is smaller than a tennis ball, or bigger than a bus
[/quote]

I think this can be better understood as Bullet having a maximum *relative scale range* of `bus:tennisball`. You can scale things up and modify some parameters to shoot a man-sized bullet from a bus-sized gun without _Bullet_ doing "weird things".

-------------------------

Leith | 2019-03-09 07:09:52 UTC | #10

Bullet works in world space, so scaling tricks are not going to fly.

-------------------------

Modanung | 2019-03-09 07:23:46 UTC | #11

@Leith Why not? You could just "pretend" objects are of a different size, it's all virtual anyway.

-------------------------

bvanevery | 2019-03-09 14:29:07 UTC | #12

Yes, Bullet can make a hand-wavy, "toy" simulation of all the parts of a gun working.  I mean heck the software is called Bullet, it would be pretty pathetic if it couldn't!  :smile:  How fast it will be, how many weird simulation killing errors it will generate, and how much special knowledge you'll need to apply to get things to work acceptably, I have no idea.

-------------------------

Leith | 2019-03-10 05:38:30 UTC | #13

Bullet's solver works in terms of worldspace coordinates, so just adding scale to some node in a hierarchy is not going to help - that's all I meant. Sure you can scale the solution up and down, but you must also accept that the scene hierarchy is the wrong place to do that - the derived transforms are handed to Bullet, and that is a problem.

-------------------------

Modanung | 2019-03-10 06:06:27 UTC | #14

So one would scale the `CollisionShape`s and modify some `PhysicsWorld` properties instead, right?

-------------------------

Leith | 2019-03-10 06:25:06 UTC | #15

Scaling the collision shapes is the right answer - but we have to do it after the scene updates the node hierarchy, or alternatively, leave all our rigidbodies connected to root node, because the parent node of a rigidbody will try to apply its derived transform to the collisionshape, which we dont always want. I found a workaround with "descaling nodes" but then I'm working with armatures, and a gun simulation could be done in a single space. I just wanted to enforce that inherited scale due to scene nodes affects the local scale on collisionshapes, and can be a source of problems if the bodies are to be independently scaled for the purpose of avoiding numerical precision issues (mainly dot products) on  single floats.

-------------------------

SirNate0 | 2019-03-13 03:09:14 UTC | #16

In regards to scaling the simulation, it's also possible to just define (interpret) world scale units as something like centimeters or inches rather than meters (decimeters would probably be the best common(ish) unit to scale on for a gun/bullet simulation, if I had to guess). If course, that could fail if you also need to simulate the now building-sized players as well as the bus-sized gun, but if it's just the guns being simulated just make all of your assets with that assumption instead.

-------------------------

