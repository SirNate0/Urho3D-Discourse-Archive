Enhex | 2017-01-02 01:08:47 UTC | #1

[newtondynamics.com/](http://newtondynamics.com/)
[github.com/MADEAPPS/newton-dynamics](https://github.com/MADEAPPS/newton-dynamics)

While Bullet works fine for simple scenarios, but once more complex things are needed it performs poorly.

Bullet has a maddening trait which is collision margins:
Using 0 collision margin breaks raycasts and convexcasts, and possibly more things, so it isn't really an option.
Collision margins create rounded corners. For example with character controllers it breaks combining maximum climb slope and auto stair stepping algorithms, because stairs are now round and have portion of steep slope.
It causes small unexpected bugs too. For example my monster AI code has ledge detection that first checks if the monster stands on the ground, and because of collision margins it always missed. I solved it my moving the raycast up by the collision margin length.
Also the roundness only apply to some of the shape-shape collision combinations (which is btw not documented and only explained in [url=https://www.youtube.com/watch?v=BGAwRKPlpCw]this video[/url]).

Bullet also uses force based recovery from penetration, which can cause bad behaviors.
It may be the cause of bumping between convex hull floor segments, a body slightly penetrates the floor and bumps into the side of an adjacent floor body. (trimesh has edge connectivity utility that deals with that, but not convex hull)

I've observed small bodies getting pulling in between adjacent bodies like stairs, for example: [youtube.com/watch?v=2QVRYrcqrdE](https://www.youtube.com/watch?v=2QVRYrcqrdE)

Also, while trying to implement a character controller with advanced features (more than just pushing a rigid body), I've run into a lot of problems, and most of them led to catch-22's with some broken feature in Bullet. for example:
- Using 0 margin to avoid round stairs breaks ray/convex casting.
- Using setContactProcessingThreshold(0) to [url=http://www.bulletphysics.org/Bullet/phpBB3/viewtopic.php?f=9&t=10888]avoid bumps between floor segments[/url] causes unstable collision with walls.
I haven't seen a single advanced character controller which works properly in Bullet (The sample one that comes with Bullet [url=http://www.bulletphysics.org/Bullet/phpBB3/viewtopic.php?f=9&t=10843]doesn't even handle recovery from penetration properly[/url]).

I find Bullet unsuitable for games which have complex environments, or require an advanced character controller, and those are quite general cases.
I don't know how Newton Dynamics compares to Bullet, but AFAIK it doesn't use collision margins which is a huge advantage over Bullet, so maybe it could properly handle things Bullet can't.

Did anyone use Newton Dynamics, especially recent versions? Are there any problems with it?
I also wonder if physics engine choice could be abstracted under Urho's Physics API?
If not would it be similar like choosing between Lua and AngelScript?

-------------------------

1vanK | 2017-01-02 01:08:47 UTC | #2

> I've observed small bodies getting pulling in between adjacent bodies like stairs, for example:

try to tuning CCD Radius and CCD Motion Threshold

-------------------------

Enhex | 2018-06-26 02:10:37 UTC | #3

[quote="1vanK"]
> I've observed small bodies getting pulling in between adjacent bodies like stairs, for example:

try to tuning CCD Radius and CCD Motion Threshold
[/quote]

That was the first thing I tried, it doesn't fix it. Neither does changing the collision margin, or trying to use capsule instead of a cylinder.
This one isn't even a catch-22 that you could try to do magic to bypass, you simply can't do anything about it.
Anyway this is not a support thread.

The thread is about if there are other Physics engines that function properly where Bullet breaks.
Newton Dynamics seems like the best candidate for this role - It doesn't use collision margins, it has ray & convex cast, it's actively developed, it's documented.

-------------------------

bvanevery | 2018-06-26 02:10:56 UTC | #4

[quote="Enhex"]
The thread is about if there are other Physics engines that function properly where Bullet breaks.
Newton Dynamics seems like the best candidate for this role - It doesn't use collision margins, it has ray & convex cast, it's actively developed, it's documented.
[/quote]

Isn't maintaining multiple physics engines going to be hell on Urho3D core developers?  I don't recall seeing lots of manpower handling the various things needing to get done.  For the most part I've seen 2 people doing most of the work.  Although possibly I have a limited perspective on how Urho3D contributions flow and how they are maintained.  Anyways I'm generally aware that the more doo dads are added to an engine, the more maintenance effort is watered down.  I suppose I would ask, what is so broken about Bullet that it can't be fixed?  I don't have any experience with it really, I'm just asking.  And, why can't it be fixed upstream of Urho3D?

-------------------------

thebluefish | 2017-01-02 01:08:49 UTC | #5

The fun thing about Urho3D's use of systems is that you can bring in another physics engine without having to do anything with the original physics engine. It's just a set of components. Just create the components that controls Newton's system instead and refrain from using the Bullet components. Boom, integrated.

On that note, I have a basic Newton implementation already in place for libblu. So far only boxes, but I only spent a few hours on it.

-------------------------

bvanevery | 2017-01-02 01:08:49 UTC | #6

[quote="thebluefish"]The fun thing about Urho3D's use of systems is that you can bring in another physics engine without having to do anything with the original physics engine.[/quote]

Well sure but that makes it "what you're doing in your own project," not a feature request.

-------------------------

Enhex | 2017-01-02 01:08:50 UTC | #7

[quote="thebluefish"]The fun thing about Urho3D's use of systems is that you can bring in another physics engine without having to do anything with the original physics engine.[/quote]

That's true. I'm proposing adding another engine because Bullet has traits that could make it less suitable for specific tasks, so another engine could help to better cover the engine's possibility space.

-------------------------

bvanevery | 2018-06-26 02:11:11 UTC | #8

[quote="Enhex"]
That's true. I'm proposing adding another engine because Bullet has traits that could make it less suitable for specific tasks, so another engine could help to better cover the engine's possibility space.
[/quote]

Are you going to add and maintain it, or at least show proof of concept of how to add it?

-------------------------

cadaver | 2017-01-02 01:08:50 UTC | #9

bvanevery is quite spot on regarding the core developer manpower. It would be no problem to integrate Newton as an option (I will not make comments on its quality since I've not tested it personally in depth) if we got a contributor who does the integration and is then willing to maintain it. In general Urho3D's problem is accumulating features while former steady contributors become inactive, leaving for the most part me and Yao Wei Tjong to maintain the whole.

-------------------------

TrevorCash | 2018-06-25 19:40:39 UTC | #10

I have started integrating newton.  It is still very early on in the process, But I thought I would show a video and see if anyone is interested in helping out with the integration.

There is recent (and ongoing work) in newton to support sse4, avx and avx2 speedups as well as multithreading enhancements which I'm excited about.

https://www.youtube.com/watch?v=qDgJN_D3bpk

https://github.com/TrevorCash/Urho3D/tree/ThirdParty/NewtonDynamics

-------------------------

S.L.C | 2018-06-26 20:05:36 UTC | #11

One thing I've noticed on Newton is that it doesn't support MinGW. For example, it looks for `_MSC_VER` instead of `_WIN32` to identify windows platform in macros. Includes a little non-standard(?) code as well. For example, uses members of types with constructors in anonymous structs/aggregates.

Example of win32 detection: https://github.com/MADEAPPS/newton-dynamics/blob/master/sdk/dgCore/dgTypes.cpp#L32

Example of non-standard code: https://github.com/MADEAPPS/newton-dynamics/blob/master/sdk/dgPhysics/dgWorldDynamicsParallelSolver.h#L142

While these are minor and can be fixed with a quick find and replace. It makes me believe that the library never even considered MinGW as a potential compiler. So there may further issues. (_actually there are a few more_)

The build system(s?) is pretty broken. Especially for Windows. But then again, that's true for most other physics engine library out there.

Beyond that, the physics engine seems neat.

-------------------------

TrevorCash | 2018-06-27 16:40:00 UTC | #12

Yeah it does need some love when it comes to the build system.  Julio seems pretty open to pull requests regarding details like that.

Currently I am linking using objects and that is working very simply.  I was able to cut out the project files and extra cmake stuff that was part of the newton sdk.  I would like to get it linking using dlls though.

-------------------------

TrevorCash | 2018-08-03 18:40:47 UTC | #14

Starting to integrate joints (these are fixed distance joints in the video below):
https://youtu.be/bvDDcLheEV8

-------------------------

TrevorCash | 2018-08-23 00:59:28 UTC | #15

Terrain and Scene Collisions are working now.  As well as the Kinematics Joint that is used to pick up the objects with the camera. (super useful if you just want a rigid body to go somewhere while still regarding physics laws)

Random CollisionShapes are added to the scene node at random transformations (and scales).  When geometry is part of the scene collision - it is very fast and you can add lots of geometry.  It is faster than spawning individual nodes with rigid bodies and collision shapes and setting their mass to zero which of course will have the same effect.

https://youtu.be/olnuxqNa9Gg

-------------------------

QBkGames | 2018-08-28 10:19:21 UTC | #16

It's nice to have another option besides Bullet, however I would have preferred nVidia PhysX. It seems to be the engine of choice for all major commercial engines (Unreal, Unity, CryEngine/Lumberyard, etc). Also it has a couple of game specific features that I like: world center shifting (useful for large worlds) and setting a scaling factor when initializing the engine (so you are not stuck to the 5cm-10m range of Bullet).

-------------------------

Modanung | 2018-08-28 14:00:53 UTC | #17

[quote="QBkGames, post:16, topic:1596"]
I would have preferred nVidia PhysX
[/quote]
PhysX is proprietary. It is not a valid candidate for integration.

-------------------------

TrevorCash | 2018-09-03 17:57:06 UTC | #18

I seem to remember reading newton has a scaling feature - I'll look into it.  Also has double precision as an option.
I myself would have a hard time using phys x in any scenario - Its integration method is fast but not as stable as newton.

Here are some good comparison videos: https://www.youtube.com/watch?v=qMy7vqK7mvc

-------------------------

slapin | 2018-09-04 03:58:33 UTC | #19

Just needed to tell you that Bullet also has scaling and double precision if you want them.

-------------------------

QBkGames | 2018-09-07 08:59:23 UTC | #20

I want them, especially the scaling, I just never noticed they were there or how to set them up.

-------------------------

TrevorCash | 2018-09-17 20:35:00 UTC | #21

Porting the Ragdoll demo:
https://www.youtube.com/watch?v=RFWIPIc5MyQ&feature=youtu.be

-------------------------

TrevorCash | 2018-09-18 22:09:26 UTC | #22

Here is a video of the physics world scale set to 1/16:
https://youtu.be/yf03HjFLhHE

-------------------------

TrevorCash | 2018-09-27 16:54:54 UTC | #23

Porting The Urho3D Vehicle Demo to use Newton Dynamics.  Steering is now properly controlled by a hinge actuator instead of applying a strong counter torque to over control bullet's weak joints:

https://youtu.be/FHrZGXRl-eM

-------------------------

TrevorCash | 2018-10-01 20:59:21 UTC | #24

Adding the SliderConstraint to the vehicle demo (not a raycast car):
https://youtu.be/g_h0nqcc5Jw

-------------------------

QBkGames | 2019-01-21 09:55:41 UTC | #25

What is the status of the Newton Dynamics integration? Is it production ready yet (or at least at in testable state)?

After spending months building a world at realistic scale, I'm getting sick and tired of Bullet letting objects fall through the floor and other objects hovering above the ground, etc. I'd really like to try another physics engine in the near future.

-------------------------

TrevorCash | 2019-03-06 00:37:40 UTC | #26

It is very much in a testable and perhaps even usable state. It is built on the rokups branch. 

you can try it on https://github.com/rokups/rbfx/pull/61




The things that come to mind that need finished.
* basic physics demo needs restored to its simple former self. (I have used that sample as a testing ground)

* Improve the cmake integration. (Just needs more testing)

* Tool/Resource support for Importing Compound Collisions From meshes using https://github.com/kmammou/v-hacd

* Shape to Shape "RayCasting"

* Kinematic Bodies mode for RigidBody (Done)

* world scale feature has a small bug in it (some small bug I intruduced recently)

* add the double precision option (Done and Works)

Newton also relies on a constant update rate (which Urho should have but doesn't)  It still works without it but is much more stable if you use my branch: https://github.com/TrevorCash/Urho3D/tree/enginetimingchanges2
which changes the Engine.cpp to prioritize constant update rates.

Another fun video:
https://www.youtube.com/watch?v=8Zkb2HEsil4

-------------------------

QBkGames | 2019-01-30 02:56:11 UTC | #27

I started having a look at this and it looks promising.
Is there a way to enable the profiler statistics in the samples like in the original Urho samples, I'd like to compare the performance of Newton with Bullet in Sample 12 "Physics Stress Test"? Thanks.

-------------------------

TrevorCash | 2019-01-30 23:50:08 UTC | #28

I did this awhile ago - you can use tracy to profile:

Bullet:
![image|690x398](upload://vj44AZLwOCIgpmwIqGaMDW87E4I.png) 

Newton:
![image|690x402](upload://dOwOh5YK7dTFmrU9D7sm4gqbwUi.png) 

Here is a link to the discussion thread: https://gitter.im/Urho3DNewton/Lobby

-------------------------

Leith | 2019-02-02 14:58:51 UTC | #29

Newton is certainly more accurate than Bullet, but it costs something for that accuracy - what is your use-case that requires such accuracy, and how does it apply to a game engine? Oh - and did you try Bullet with double enabled? real8 is a lot more accurate than real4 floating point

-------------------------

TrevorCash | 2019-02-02 18:29:10 UTC | #30

In my tests I've found newton to be on par with bullet as far as performance is concerned.  I use this integration because of the rigidity and accuracy of the simulation.  Constraints are rock solid and don't suffer from joint wobble near as much as Bullet per the same iteration count/cpu cycles.

-------------------------

Alan | 2019-02-02 18:58:05 UTC | #31

@TrevorCash for real solid joints you shouldn't have simulated joints at all, but a single rigid body with the colliders (aka compound). Is there anything preventing you from doing that in your use case?
Edit: I just realized you might be talking about joints other than fixed, like for example hinge joints... you have to sim those ofc

-------------------------

TrevorCash | 2019-02-02 19:16:13 UTC | #32

Hi Alan,  Yes of course, if you have 2 bodies with no degrees of freedom its best to make a compound.  Its pretty easy with the API just add multiple CollisionShape components and 1 RigidBody component to a node.  The RigidBody will use all attached CollisionShapes and form a compound internally.

If you look at the motorcycle video - the midframe of the bike is a compound formed this way.

with regards to joints - yes I am talking about well, the joints :slight_smile:

-------------------------

S.L.C | 2019-02-02 19:55:06 UTC | #33

Performance from code only represents a percentage of your overall performance. A bunch more can be obtained from well crafted assets.

@TrevorCash This looks good man. I tried the vehicle demo on the Newton demos and it definitely controls better than whatever Bullet has. So far I like this.

-------------------------

QBkGames | 2019-02-03 05:51:22 UTC | #34

My biggest problem with Bullet is the size limit of the dynamic objects:
_"The minimum object size for moving objects is about 0.2 units, 20 centimeters for Earth gravity."_ quote from Bullet's manual. And also the largest size is about 5 or 7 meters (from what I remember).

So if you want to do a survival game and you want to have a box of matches which is 5 x 2 x 1 cm, you can't do it with Bullet, as it's too small and the object will fall through (the terrain or other objects) when you drop it. So, I tried scaling up the whole world to try and make the smallest object large enough, but then if you want to have vehicles, than you exceed the upper size limit and also if your terrain is too large, you start loosing float range accuracy (going to double would most likely affect performance). I could also try increasing the simulation rate, but then again you are reducing the performance of the game.

I'm hoping Newton can handle a wide range of sizes for dynamic objects (I'm yet to find out).

-------------------------

Leith | 2019-02-08 06:07:44 UTC | #35

Bullet Dynamics works best with objects whose size ranges from a tennis ball, to a bus.
Outside of these limits, the numbers get too big or too small for the default 32 bit math.
You can switch your build settings for Bullet to use 64 bit math (double floats) and this gives you a much richer experience, with generally the same performance as 32 bit, just a greater numerical range to work with. I don't know if Newton has some magical way to deal with numerical precision, but I suspect it uses 64 bits by default, where the platform can support it.

[EDIT]
Oh, and the limits mainly apply to dynamic objects. Static objects can be enormous, Kinematic objects suffer tunneling issues at your discretion, and CCD helps a lot with tunneling on dynamic objects at high velocities, even on 32 bit precision. I would say that Newton and Bullet are similar in performance, except where it comes to things like impulse chains, where Bullet offers things like featherstone solver, but Newton uses classical iterative methods in its resolvers.

-------------------------

TrevorCash | 2019-02-17 00:28:03 UTC | #36



From the newton website:
> Newton Dynamics implements a deterministic solver, which is not based on traditional LCP or iterative methods

Quick update - double precision is working now as well as the world scaling option.

Double precision also works with the SSE, AVX and AVX2 plugins!

-------------------------

TrevorCash | 2019-05-06 22:18:04 UTC | #37

I've made numerous fixes and refactors as well as lots of continuous testing while making my current physics based game project.

So I am happy to finally release the project!
https://github.com/TrevorCash/rbfx-newton

It is provided as a plugin for rbfx but could be adapted to work with upstream urho as well. (you would have to remove the new eastl containers)

The project comes with one Sample that showcases and tests many of the functionalities of newton.

I'd be happy to answer any question to users who are using it.

and of course bug fixes are always welcome! 

I plan on continued development as I work on my own project that uses this plugin.

-------------------------

Leith | 2019-05-07 04:49:54 UTC | #38

I've hit limits recently with single precision in Urho3D - not in Bullet per se, but in the Node class, which underpins character bone animation. I'm trying to measure delta-transforms on the character hips and apply the delta-translations to the character's true root node. Numerical precision is terrible when I use inverse transforms on a scaled model. The order of error is large. Note I zeroed the Y value in this computation, but here I compare my output numbers to my expectations. The scale of the error is often approaching 10.

WARNING: WorldHips WAS -0.0136105 0.944575 -0.00740542-->-0.0133018 0.941086 -0.00822335 Inverse-Computed Delta -0.000887255 0 -0.000894101

-------------------------

TrevorCash | 2019-05-07 17:19:06 UTC | #39

Hi Lieth,

Generally I have found ( and I'm sure you know) that avoiding node scale as much as possible always helps.  Usually in your hierarchy for the ragdoll if you enforce that all nodes should have (1,1,1) scale and then have child nodes that do have scale for visual stuff. then you can do the math on the root nodes without worrying about the scaling side effects.

-------------------------

