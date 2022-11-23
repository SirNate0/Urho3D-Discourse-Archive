sabotage3d | 2017-01-02 01:01:04 UTC | #1

Hello,

I am having some performance issues with Sample 11 Physics on IOS. It is extremely slow compared to a quick test I did a while ago using Ogre3d and Bullet Physics. Is it possible that the entity system is causing the slowdown ? Is there a good way to do proper profiling ?

Thanks,

Alex

-------------------------

weitjong | 2017-01-02 01:01:04 UTC | #2

A profiler is built into the game engine by default (unless you have turned this build option off explicitly). In iOS sample app, you can turn on the profiler display output by pressing the Setting button (cogwheel) and then the HUD button.

-------------------------

cadaver | 2017-01-02 01:01:05 UTC | #3

If the physics sample seems exceedingly slow, you may be running it in debug mode. Turning off shadows will also help performance, but they shouldn't kill it.

-------------------------

sabotage3d | 2017-01-02 01:01:05 UTC | #4

I have disabled shadows and shaders. And I am running in release mode. But still multiple active rigid bodies are spiking the CPU until they come to rest again. Is there a way to log the profiling to file so that I can post my results ? 
I hope that SIMD is working properly on IOS . Do we have BT_USE_NEON enabled ?

-------------------------

cadaver | 2017-01-02 01:01:05 UTC | #5

I'm quite sure Neon is not enabled. Engine::DumpProfiler() writes accumulated profiler status to the log, but in iOS release mode logging is disabled, so it's not directly available. The amount of objects in the example 11 is not high so we might have some "stupid" performance bug that has creeped in. I will be able to test this on Android first.

-------------------------

sabotage3d | 2017-01-02 01:01:05 UTC | #6

Thanks a lot. The last time I checked Neon for Bullet physics was available only for IOS . Not sure if it will work on Android but still might be a good test case. Let me know if you need me to test something on IOS device.

-------------------------

cadaver | 2017-01-02 01:01:06 UTC | #7

Testing the 11_Physics example on Android I saw a quite high usage of CPU time (about 20ms per frame, and even 40ms once there were more objects) when spawned boxes collided with the stack and made everything to wake up. Will have to see if this is an actual performance regression.

-------------------------

cadaver | 2017-01-02 01:01:06 UTC | #8

Did not find regressions or specific code hotspots that would have appeared. One thing I did (pushed to master) was to disable Bullet's hierarchical profiling, as that causes system calls under the hood on Unix-like systems. Will test iOS later. On a slow CPU, physics is something you can easily make to "spiral to its death" due to physics & rendering load causing longer frame time deltas, which the physics needs to catch up by taking more internal simulation steps.

-------------------------

sabotage3d | 2017-01-02 01:01:06 UTC | #9

Is it currently exposed to tweak Bullet's Broadphase schemes or substeps ?

-------------------------

cadaver | 2017-01-02 01:01:06 UTC | #10

Likely not to the degree you'd want. I recommend digging into the PhysicsWorld.cpp code, which does the Bullet world and collision setup.

-------------------------

sabotage3d | 2017-01-02 01:01:07 UTC | #11

Thanks I will take a look.  Are you familiar with BtOgre : [github.com/nikki93/btogre/tree/master](https://github.com/nikki93/btogre/tree/master)
It was slightly more tweakable on the Bullet Physics side .

-------------------------

sabotage3d | 2017-01-02 01:01:07 UTC | #12

I took a peek but still I am not extremely familiar with the code I will need to test it although it might be a good idea to expose the numbers of substeps for Bullet Physics. 
It seems by default it is trying to be adaptive based on fps. If maxSubSteps is exposed it will be really neat for greater control over the solver.

[code]void PhysicsWorld::Update(float timeStep)
{
    PROFILE(UpdatePhysics);

    float internalTimeStep = 1.0f / fps_;
    delayedWorldTransforms_.Clear();

    if (interpolation_)
    {
        int maxSubSteps = (int)(timeStep * fps_) + 1;
        world_->stepSimulation(timeStep, maxSubSteps, internalTimeStep);
    }
    if (manualSubstep)
    {
        int maxSubSteps = 10;
        world_->stepSimulation(timeStep, maxSubSteps, internalTimeStep);
        
    }    
    else
    {
        timeAcc_ += timeStep;
        while (timeAcc_ >= internalTimeStep)
        {
            world_->stepSimulation(internalTimeStep, 0, internalTimeStep);
            timeAcc_ -= internalTimeStep;
        }
    }[/code]

-------------------------

cadaver | 2017-01-02 01:01:07 UTC | #13

Currently we tick the physics at the same internal substep length (by default 60fps) and always try to cover all the passed time.

Allowing a cap for max substeps will lead to physics time slowing down, if it tries to cover too much time. This is probably still the better option than adapting the substep length on the fly, as that could actually cause differing physics behavior (constraint explosion, tunneling etc.)

-------------------------

sabotage3d | 2017-01-02 01:01:07 UTC | #14

Let say we want 1 substep for cheap approximation can we just compensate, maybe just using euler integrator would help ?

-------------------------

doodloo | 2017-01-02 01:01:07 UTC | #15

Unrelated, but i noticed that someone is talking about his "Release Build" of the engine for iOS. How do you guys do this, given the fact that generating a XCode project for compiling a iOS version gives a wrong target / action association pairs?

Thanks,
Doodloo.

-------------------------

cadaver | 2017-01-02 01:01:07 UTC | #16

There is now a possibility to cap physics substeps or enable adaptive step (always 1 substep per rendering frame), see PhysicsWorld::SetMaxSubSteps(). Both have their problems, but should help to prevent the "spiral of death" issue.

-------------------------

sabotage3d | 2017-01-02 01:01:07 UTC | #17

Awesome thanks a lot :slight_smile:

-------------------------

sabotage3d | 2017-01-02 01:01:08 UTC | #18

Can we add  BT_USE_NEON as default for mobile in the cmake ?

-------------------------

cadaver | 2017-01-02 01:01:08 UTC | #19

Looked into it further and what I said earlier may be incorrect. I'm not 100% sure whether all the conditionals within Bullet's btScalar.h are triggered right, but URHO3D_SSE should be defined by default, which in turn should result in it being enabled. If you have time, please verify.

-------------------------

sabotage3d | 2017-01-02 01:01:08 UTC | #20

I can confirm that default Urho3d build has SIMD enabled by default on IOS devices. 
I tested on IOS device and just to be sure I checked all the BT_USE_NEON conditionals and they all are set to 1 .

-------------------------

sabotage3d | 2017-01-02 01:01:09 UTC | #21

I am really curious how this game is working in realtime with bullet physics on IOS without going into the spiral of death. There must be some cheating or some performance optimizations. There must be more rigid bodies in these videos than the samples from Urho3d also they are convex hull which is more complex to solve than cubes. I also tried the game on the same iphone that I am testing Urho3d I must say in the first few levels it works without any slow down. 
I am interested in pursuing the same effect with Urho3d but I am not convinced that I will be able to solve the same amount of rigid bodies.

[youtube.com/watch?v=ZGzNZObLR9Q](https://www.youtube.com/watch?v=ZGzNZObLR9Q)
[youtube.com/watch?v=gjarUm2gGK8](https://www.youtube.com/watch?v=gjarUm2gGK8)

This is the full article if anyone is interested:

[tuxedolabs.blogspot.co.uk/2014/0 ... 4980932077](http://tuxedolabs.blogspot.co.uk/2014/05/cracking-destruction_13.html?showComment=1415200151289#c4317332874980932077)

-------------------------

cadaver | 2017-01-02 01:01:09 UTC | #22

I think what likely kills the 11_Physics on slower CPU's is the stack of rigidbodies. Eg. 100 cubes bouncing on the floor should be cheaper than a stack of 100 rigidbodies, as in the latter there is a lot more contacts between different objects, and the stack on the whole is kept awake.

Also, PhysicsWorld runs the physics by default at 60 fps and with 10 solver iterations; reducing either should reduce the CPU load.

Another thing to optimize Urho physics is to disable collision events generation from the rigidbodies when they are not needed (eg. scenery).

-------------------------

sabotage3d | 2017-01-02 01:01:09 UTC | #23

Thank you for your tips. 
What is the best way to change the target FPS from 60 to 30 ?
How do we disable collision events generation ?
If Urho3d math library is not SIMD optimized and Bullet Physics is do we get slow down as we are constantly converting Vectors and Matrices between the two API's ?

-------------------------

Mike | 2017-01-02 01:01:09 UTC | #24

To set FPS to 30, use Engine::SetMaxFps(30)
To disable collision events for a given RigidBody, use RigidBody::SetCollisionEventMode(COLLISION_NEVER)

-------------------------

sabotage3d | 2017-01-02 01:01:10 UTC | #25

Is it the same if I use Collision mask and Collision Layer explicitly per rigidbody to disable the collisions ?

-------------------------

weitjong | 2017-01-02 01:01:10 UTC | #26

I think Lasse was referring to Physics simulation update rate, which is set by PhysicsWorld::SetFps().

-------------------------

Mike | 2017-01-02 01:01:10 UTC | #27

Yes, thanks weitjong, engine fps doesn't relate to physics. I'm using both for mobiles.

-------------------------

cadaver | 2017-01-02 01:01:10 UTC | #28

The collision mask and layer are the values that go to Bullet, ie. you can use them to completely disable collisions and make objects go through each other. This is the most effective optimization, as the collision detection and solver will get less work.

But if you still need the collisions to happen (like an object hitting the floor) but just don't need Urho's physics events for notifying that a collision happened, then you can change the RigidBody event mode to reduce the Urho side processing load.

-------------------------

