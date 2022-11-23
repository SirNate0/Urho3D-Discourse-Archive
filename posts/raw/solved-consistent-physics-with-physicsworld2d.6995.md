unkkatkumiankka | 2021-09-23 16:59:07 UTC | #1

Hi all,

I'm new to Urho and have been working on a little project for some weeks now. I noticed I have an issue with physics behaving very differently when under a heavy load. What I'd like to happen is time slowing down while retaining consistent physics simulation. It seems like this topic is covered for PhysicsWorld in the documentation:

> The physics simulation has its own fixed update rate, which by default is 60Hz. When the rendering framerate is higher than the physics update rate, physics motion is interpolated so that it always appears smooth. The update rate can be changed with SetFps() function. The physics update rate also determines the frequency of fixed timestep scene logic updates. Hard limit for physics steps per frame or adaptive timestep can be configured with SetMaxSubSteps() function. These can help to prevent a "spiral of death" due to the CPU being unable to handle the physics load. However, note that using either can lead to time slowing down (when steps are limited) or inconsistent physics behavior (when using adaptive step.)

However, I am using PhysicsWorld2D and am not able to find similar settings. I am now wondering what the correct way to do this is. Would anyone be able to offer any pointers? Is there a built-in way of doing this or will I need to implement something myself (such as what is described at https://gafferongames.com/post/fix_your_timestep/ )?

I tried searching the forums and looking into a few of the sample programs but wasn't able to draw much conclusions about things such as: should processing input and applying forces be done in Update or FixedUpdate? Which actions (i.e applying forces/impulses/translations) should actually consider the timestep. I have some assumptions but am a bit confused here. :)

I also noticed that FixedUpdate for my LogicComponents was being called at the same intervals as Update despite the documentation stating it uses fixed timesteps. This was corrected once I added a PhysicsWorld component. Should I include PhysicsWorld in my program despite the fact that I'm really using PhysicsWorld2D?

-------------------------

unkkatkumiankka | 2021-09-19 16:49:39 UTC | #2

So my conclusion is that this functionality has not been implemented for 2D physics. I think I was able to hack it in by just taking the relevant piece of code from the Update method of PhysicsWorld and inserting it into the same method of PhysicsWorld2D.

In case anybody else needs this, I replaced:
```
world_->Step(timeStep, velocityIterations_, positionIterations_);
```
with this (yes, I just hard-coded the values):
```
float internalTimeStep = 1.0f / 60.0f;
int maxSubSteps = (int)(timeStep * 60.0f) + 1;
maxSubSteps = Min(maxSubSteps, 3);
delayedWorldTransforms_.Clear();
timeAcc_ += timeStep;
while (timeAcc_ >= internalTimeStep && maxSubSteps > 0){
    world_->Step(internalTimeStep, velocityIterations_, positionIterations_);
    timeAcc_ -= internalTimeStep;
    --maxSubSteps;
}
```
and in the header file you'll need:
```
float timeAcc_{};
```

I hope that's all the engine code I need to touch as it really is beyond my skill level.

If anybody has any comments on this or any of the other points/questions, I'm still interested in hearing.

Oh, and I believe I'll just need to keep the dummy PhysicsWorld object in my application, just to make FixedUpdate work correctly.

-------------------------

PsychoCircuitry | 2021-09-22 15:33:51 UTC | #3

Hi, no expert here, (and also zero experience with urho2d components, so take my opinions with a grain of salt) but I think your proposed solution is quite possibly the quickest solution for adding fixed timestepping to the 2d physics simulation. PhysicsWorld and PhysicsWorld2D are vastly different as you've encountered, despite the interfacing using similar notions and conventions, the underlying libraries that handle these are completely different in the way that they work.

 I've skimmed thru the relevant source code and altho I'm not sure what exactly the 2d world continuous physics or substepping booleans are used for, if anything, there appears to be no built in methods for fixed timesteps. Ie update method is literally called every scene update and advances the simulation by the length since the last update, regardless of the above mentioned boolean configurations. So if you need box2d to work in a fixed update, I think borrowing the update code from the bullet physics world update method is possibly the simplest way to achieve this.

As per your logic working on a fixed update method, you are correct in that you will need a dummy bullet physics world to facilitate that. The fixed update only happens when it exists, as you've found out. It's handled by the scene sending a scenesubsystem update event. Which updates any scene subsystem and branches out according to what exists, octree, physicsworld, physicsworld2d. Not sure what additional stuff would be needed to create the fixed update events inside just the physicsworld2d component, and not sure if it's even worth pursuing in this case. Not entirely sure what the overhead of a physicsworld with zero objects in the simulation are, I suspect not huge tho, but not sure.

Another thought and this may not be applicable to your case (or desirable depending on how much you have developed your application using urho2d components) but, if you need the fixed timesteps and how that type of simulation works, using bullet physics and restricting the angular factor and linear factor of your simulation objects on the applicable axis, would give you pseudo 2d physics within the 3d physics world. Altho if you're using any of the specialized box2d constraints, I understand this would be not very workable.

Just some thoughts, good luck on your application!

-PsychoCircuitry

-------------------------

unkkatkumiankka | 2021-09-22 16:34:55 UTC | #4

Thanks for your thoughts, I appreciate the input!

Nice to get some validation for my approach. I have wondered if using Bullet would've been an option but I wasn't sure how feasible it would be to restrict the dimensions. I'm not in too deep yet, so switching is still possible but for now I think I'll keep the 2D physics and reconsider if I come across any other challenges.

Again, thanks for taking the time to provide your viewpoint. :slightly_smiling_face: :+1:

-------------------------

PsychoCircuitry | 2021-09-22 17:32:52 UTC | #5

No problem. 

Restricting dimensions in bullet is fairly easy if you decide to go that route, urho3d exposes it as linearFactor(motion) and angularFactor(rotation) which both take a vector3, world factor x,y,z. So if you were using x,y for your 2d scene coordinates, for each dynamic body just SetLinearFactor with Vector3(1,1,0) this will negate all motion forces on the z axis. It's just body.linearFactor =, for angelscript as most of the get/set methods are exposed as properties to the script api, with get and set methods automatically determined by which side of the equation the property is on.

-PsychoCircuitry

-------------------------

unkkatkumiankka | 2021-09-23 16:58:27 UTC | #6

Nice, couldn't be much easier than that, thanks for the tip :+1:

-------------------------

