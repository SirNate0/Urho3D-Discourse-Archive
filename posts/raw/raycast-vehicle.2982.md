slapin | 2017-04-05 17:52:03 UTC | #1

Hi, all!

For some time I was making city sandbox and got some progress.

Doing a car (AI and controlled by player) I was using Urho example
from vehicle demo and now I find that it doesn't fit what I make due to following reasons:
1. It is very difficult to control, car is getting stuck quickly and in general it is very hard
to make it work in complicated environment. One ends-up hacking-up all behavior,
so while using physics is great, working-around physics is not, and it seems that Bullet
physics is not advance enough to make reliable vehicles. Not mentioning wheels stuck in terrain :(

2. LODding  the vehicle behaviors (i.e. path motion/physics motion with collision) and spawning does have
too much side effects.

So after fighting things for several months I think it is better to move on and go for raycast vehicle.
I've been reading Internet for quite some time on subject but it looks like I don't have some basic knowledge
pros know, so I still can't understand the concept.

[b]So what I really ask for is to put me into right direction - are there any good theory links to read about
these? I want GTA3 level of car physics. I know it is hard work, I don't have problem with it I just need to know
where to begin.[/b]

-------------------------

Modanung | 2017-04-05 19:25:14 UTC | #2

Starting with the sample, adding some suspension to the vehicle would help a lot when it comes to both realism and control.

-------------------------

slapin | 2017-04-05 19:55:56 UTC | #3

Sorry for being so dumb, but - what do you mean by "adding suspension"?

-------------------------

johnnycable | 2017-04-05 20:28:28 UTC | #4

A counter-force impulse when the car bump into something, like the bump cars in playing parks... you know that, don't you?
Just a little spin, not too strong... a little recoil...
then measure the "medium stuck force" of your simulation and set the bump to go over that...
just messin :wink:

-------------------------

Modanung | 2017-04-05 21:06:01 UTC | #5

What I guess I'm saying is... flinstone mobile ain't got these: ;)
[<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/82a3af5e5fe200138f503dd8990689b48c4cc685.jpg' alt='Car suspension'>](https://en.wikipedia.org/wiki/Suspension_(vehicle))

Tires [spoiler]not shown in image ;P [/spoiler] also add some bounciness in real life making for longer contact with the road on take off. But this squeezing could probably be neglected after adding suspension. Tire friction does vary with pressure (both from air and suspension).

-------------------------

johnnycable | 2017-04-05 21:01:51 UTC | #6

Exactly what I had in mind, I swear :grin:

-------------------------

Modanung | 2017-04-05 21:15:19 UTC | #7

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/27114e7d35f64676b3789fd1a92631e27941e327.gif'>

-------------------------

slapin | 2017-04-05 21:36:43 UTC | #8

I see you guys having fun, I like it.

Well, I found the simplest case.

1. I now understand what spring force is. The idea is that I do raycast from some point to ground and notice its length.
then I find the compression value [b]comp = raycast_distance / raycast_length[/b]. And then I can find my force by

[b]Vector3 spring = Vector3(0.0f, 1.0f, 0.0f) * k * comp[/b] where k is multiplier value.

2. The problem is what to do with the result. If I do [b]body.AddForce(spring)[/b] either nothing happens, or
everything explodes. Any ideas on what to do next?

-------------------------

slapin | 2017-04-05 21:40:09 UTC | #9

Also original example with 5 rigid bodies and constraints puts too much strain to CPU,
which puts even i7 2500K to crawling position with 10 vehicles. I expect raycast car to be less intense...

-------------------------

lezak | 2017-04-05 22:33:42 UTC | #10

Have You seen <a href="http://discourse.urho3d.io/t/offroad-vehicle/2450">offroad vehicle </a> made by @Lumak?

-------------------------

Modanung | 2017-04-05 22:45:11 UTC | #11

In most cases you'll want to multiply your force with the timeStep.

-------------------------

Lumak | 2017-04-06 00:10:16 UTC | #12

He's already admitted that that is too complicated for him.

Edit: just realized that he said:
[quote="slapin, post:1, topic:2982"]
Bullet physics is not advance enough to make reliable vehicles
[/quote]

deleted my suggestion.

-------------------------

slapin | 2017-04-06 00:51:52 UTC | #13

@Lumak It appears that I said not really what I intended to say.

I just mean that full physical vehicle with rigidbody for everything done in Urho3D
Bullet integration does not allow to implement reliable vehicles. By this I mean vehicle based on example.
The main problem is torque transform from RigidBody to actual motion - it is very hard (probably impossible)
to get proper (controllable, predictable) behavior due to too many side effects. I never intended to say it is not possible to implement the required thing using Bullet directly as it exports enough hooks. But I'm really not ready for Bullet.
It is too complicated to set up and too little documentation for me to understand. So I'd prefer to stick to some simple
things for now. And yes, [b]your RaycastVehicle demo is great, but it is too complicated for me to understand at my current level[/b].

-------------------------

suncaller | 2017-04-06 04:04:28 UTC | #14

The Rocket League team implemented their own "fake physics" for similar reasons to what you suggest. I've read various discussions online about this simplified physics on reddit, GDC talks by the devs, etc. It might help to look into this game. Bullet physics likely won't do the job here if you want to simulate some serious, complex vehicles.

-------------------------

Lumak | 2017-04-06 04:57:26 UTC | #15

Ah, ok. What I was going to suggest was this, http://discourse.urho3d.io/t/btraycastvehicle-example/1306 
A simple demonstration of btRaycastVehicle dynamics.

But after reading what you said, or at least what I thought you meant, it would've been pointless to even suggest it.  But most raycast vehicle dynamics are about the same, you typically code the dynamics you're looking for.

-------------------------

johnnycable | 2017-04-06 13:52:09 UTC | #16

Why not add checks for physics values into the update cycles? It's easy to give infinite power impulse to a body, especially if you drag them around by changing their position with setPositionSomething...
this is evil :smiling_imp: you get teleport... :fearful:
you need a good way of number crunching to fine tune physics...
if you take for instance @Modanung "bumping car" physics example above, you see you could easily "sample" the impulse the car is being applied, then reverse it someway...

-------------------------

slapin | 2017-04-07 15:13:24 UTC | #17

Well, it looks like it is not possible to implement raycast vehicle in Urho, as AddForce to RigidBody consumes extreme amount of CPU and FPS drops to about 12 fps for 10 cars on i7 2600K.
For single vehicle and no other processing that is probably OK, but for several vehicles this doesn't work at all.

Is there any other ideas? I think I can just do ray/spherecast and move wheels up/down to prevent
terrain penetration and use distances for proper hull positioning. Is there anything else I can do?

Thanks!

    void update(float timeStep)
    {
        float comp = 0.0f;
        float spring = 21000.0f;
        PhysicsRaycastResult result = sc.physicsWorld.RaycastSingle(
            Ray(wheel.parent.worldRotation *
                   position + wheel.parent.worldPosition,
                wheel.parent.worldRotation * Vector3(0.0f, -1.0f, 0.0f)),
            length,
            STATIC_LAYER|VEHICLE_LAYER|CHARACTER_LAYER);
        float distance;
        if (result.body !is null) {
            comp = 1.0f - result.distance / length;
            distance = result.distance;
        } else
            distance = length;
        float springv = (distance - prevdistance) / timeStep;
        float springf = spring * (length - distance);
        float damperf = damping * springv;
        float force = springf - damperf;
        RigidBody@ body = wheel.parent.GetComponent("RigidBody");
        body.ApplyForce(wheel.worldRotation * Vector3(0.0f, 1.0f, 0.0f) * force, position);
        prevdistance = distance;
    }

-------------------------

slapin | 2017-04-07 15:34:04 UTC | #18

Also this way never gets good results, it never hovers, just either jumps or lays on collision shape.
Strangely, similar code works in Unity. Looks like Bullet was not made for it and something have
to be hacked on low level...

-------------------------

slapin | 2017-04-07 18:21:23 UTC | #19

Well, it looks like the problem is either AngelScript or something...
C++ version of code works fine and stable. Also @Lumak 's Bullet raycast vehicle code works great.

@Lumak do you plan to submit bullet vehicle as standard component to Urho?
I stress-tested it with 100 cars and don't see much CPU load.
I wonder how Unity people live with JavaScript - looks like JavaScript is much faster than
AngelScript running FixedUpdate... So now I have to rewrite all my tight loops in C++.
Too bad I'm so not into C++, I hope I can glue C code in there, so to maintain sanity...
Hope I will get there eventually...

-------------------------

