Leith | 2019-05-28 10:02:14 UTC | #1

It's (very) early days, but here's what I have to show for a couple of weeks on this engine.
![zombies|690x194](upload://xVhmw5h5KDeSH53eWRZ9rPWp4Gp.png)
![yiss|690x194](upload://6dGf05fSpSFTY0oYVX7oYr44cIO.png)

-------------------------

Leith | 2019-02-03 12:24:11 UTC | #2

Today I gave the zombie 25 attack sounds, and when that felt like not enough, I added pitch variation to adjust the frequency of the sounds with some randomness - I still need to reimport all the animations on this zombie, as for some reason and despite my wishes, they have root motions, and this causes them to walk outside their physics hull - stripping the root motion is necessary, yet I can still learn something from the root motion, such as the velocity of the animation, needed to prevent foot slipping when moving... The attack sounds are loaded into a static array, and remain resident, but they average 200kb in size, and are in PCM wave format - its not a great amount of memory to use up, but this is just one character, anyone have advice about resource management for audio?

-------------------------

Modanung | 2019-02-03 13:03:08 UTC | #3

Maybe you can get rid of the root motion with `AnimationController::SetStartBone(...)`?

-------------------------

Leith | 2019-02-03 14:03:20 UTC | #4

Hey thanks! probably I could skip root motion using your technique, but still have it in the animation in terms of a measurable velocity, it never occurred to me but it sounds feasible
Currently I have two character types, zombie and player, and a switch in the character update method, but I am thinking seriously about deriving subcharacters, I just have a thing about making more classes than needed, I try not to make new classes.

-------------------------

Modanung | 2019-02-03 15:21:22 UTC | #5

I like having a `Controllable` class that characters, mounts and vehicles all inherit from. Control can then be easily switched even for unexpected cases like a mind-control-beam mod.


In your case you could even give characters a _zombified_ state. This would keep it one class where AI could take control or the player could switch teams when zombified.

-------------------------

Leith | 2019-02-04 03:33:48 UTC | #6

I tend to think the same way - currently I have a CharacterController that drives the player character (feeds device inputs) but the character class itself, has not been derived - the consequence is that any character can become controlled by the player.

CharacterController holds a reference to a target character, which represents the player character, and the character class currently has switched logic for player and non player characters (zombies, for now) - I am tempted to derive character subclasses, but currently there is not really enough different control code to warrant it. Still early days, but starting to see my undead coming to life. More zombie types coming soon, as well as some human survivor types.

-------------------------

Leith | 2019-02-06 05:28:32 UTC | #7

I'm still thinking about foot-slipping issues, and whether it is worth my time to write an IK based solution to the issue. Our current IK sample does not deal with motion of the character, so it is really half-baked, but probably would act as a good point of reference for a better solution. I note that the Ninja model provides animation triggers on its footfalls for its walk animation - I propose analyzing the animation transforms to find the proper frames to tag for that purpose, and using the resulting events to update the IK targets. Anyone who has already done something like this, would love to hear from you.

-------------------------

Leith | 2019-02-06 06:29:25 UTC | #8

This reminds me - we still have no sample that shows how to properly apply variable frequency to soundsources - it was not difficult to do, but a tiny example might help those who did not grow up with PCM wave audio and understanding how to modify frequency. Personally, I use a scalar to modify the base frequency of the loaded sound, similar to Unity, it's pretty simple but quite effective.

-------------------------

Leith | 2019-02-08 09:30:04 UTC | #9

My next move is to apply IK to solve 'foot slipping' in walk animations, and particularly for non-linear gaits.

If the walk animation gait is linear, we can generally find the right speed to move our model without resorting to IK - at least on a level plane.
But for non-linear gaits, and including inclined planes, the best solution I can think of is applied IK.

I'm using a dynamic character controller - it has dynamic physics, the character is moving, it has some linear velocity - worse still, the linear velocity is subject to change with acceleration - this is not a good fit with the existing IK Sample, so I'm going to adapt that sample to use 'foot-planting' based on Animation Trigger events. This basically means that I need to figure out for each footstep, a world position to plant that foot's IK handle, and some time later when the foot is ready to lift up, release the ik handle. That's the theory, anyway.

I'd love to hear from anyone who's already tackled this.
Starting to think that using Animation Triggers is a bad fit with dynamic physics - it's starting to make more sense to add kinematic rigidbody attachments to the feet, and detect per frame their collision with the ground, both start and end of collision are the points I need to move/disable IK handles on the feet to implement "foot-planting".
[Edit]
Due to acceleration, and because we're not analyzing animation in advance, we can only try to 'guess' where our next footfall will be - so animation triggers is a bad notion in that context. I'm just sorry I spent a day to make animation triggers work (some issues, raised) and happy to invent some physics foot shapes close to the foot bones

-------------------------

Leith | 2019-02-10 05:20:54 UTC | #10

Today I hacked together a solution for foot-slipping without using IK, a cheap form of foot-planting.

I have two animation trigger keys on my Walk animation which represent the frames in my walk cycle where a foot is just starting to touch the ground, ie, being "planted". It's worth noting that my walk cycle is not linear - its a staggering zombie, could be a wounded soldier, etc.

In my handler for animation trigger events, I use booleans to note which foot is currently being "planted", and also note the world position of the planted foot at the time it was planted. 
Very late in the scene (SceneDrawableUpdateFinished) I grab the current worldspace position of the planted foot, measure how far it has "slipped" (due to physics) and subtract the resulting "positional error" from the worldspace position of the character's root node, which results in the character being "teleported" such that the planted foot remains where it was planted. 

The results look quite good for my staggering zombie whose linear velocity and animation speed are both increasing over time (he speeds up his "walk").

Video : The solution was applied to the zombie, but not the player character.
<https://www.dropbox.com/s/qzuo1wcyzylyvbz/FootSlipping.mp4?dl=0>

-------------------------

Dave82 | 2019-02-09 04:55:21 UTC | #11

Can you just upload it on youtube ? I can't watch your video or download it.

-------------------------

Leith | 2019-02-09 05:50:18 UTC | #12

is the dropbox link not working? i had to put some spaces in the https at the front of it
i would rather not youtube or facebook except to establish prior art
the dropbox should be alive

-------------------------

Modanung | 2019-02-10 08:39:17 UTC | #13

To prevent a onebox from being created you can put a link between **< >**.

Looks pretty nice, btw. :slight_smile:

-------------------------

Leith | 2019-02-10 05:27:56 UTC | #14

Happy to hear my ideas are well received - though in this case, the idea was not mine, it's something that 3D artists use in their modelling apps (via scripting) to deal with foot-slipping on animations that contain no root-motion. My implementation for Urho is my original work, but this concept was not mine... just never seen it applied to models being driven by dynamic physics, in a game.

NinjaSnowWar would look a lot better with this added to it - and already has suitable animation triggers on the footfalls. I'd be happy to provide source / explain anything required to see this constraint added to that sample.

-------------------------

Leith | 2019-02-10 05:30:04 UTC | #15

Modanung - thanks for the heads up about the < > stuff - it explains to me why xml is such an issue to post here!

-------------------------

Modanung | 2019-02-10 08:37:31 UTC | #16

Oh, but you can always mark `bits of code` with [grave accent](https://en.wikipedia.org/wiki/Grave_accent)s ( **\`** ). Single ones for within a line, and three of them to mark the start and end of a code block. [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) also supports inline html, btw.

-------------------------

Leith | 2019-02-10 09:02:36 UTC | #17

Is there a document somewhere that describes these things, or is this just something we learn from being here, and with much thanks to kind people who have been here longer?

-------------------------

Modanung | 2019-02-10 09:06:37 UTC | #18

Does this text seem familiar somehow? ;)
>Type here, Use Markdown, BBCode, or HTML to format. Drag or paste images.

Before the Urho3D forums switched to Discourse I was already familiar with Markdown through sites like Github and Diaspora*.

-------------------------

Leith | 2019-02-10 09:08:35 UTC | #19

Markdown is not familiar to me - I come from older stock, such as PHPBB and earlier bulletin boards that predate the current tech. I don't know the markups. Would make a useful addition to be able to read about them in one place, thanks.

-------------------------

Modanung | 2019-02-10 09:18:27 UTC | #20

That's what the second link in this post was for:
https://discourse.urho3d.io/t/wip-screenshot-everyone-loves-zombies/4892/16?u=modanung

A websearch for "Markdown syntax" will get you several other sources. There might be some discrepancies here and there because of different implementations.

-------------------------

Leith | 2019-02-10 09:17:14 UTC | #21

Oh, I intend to look into it, but I was hoping, in vain, for a link to a document. I state that I am lazy by nature, but not that I am lazy by definition. Lazy like a fox, to quote Homer Simpson.

-------------------------

Leith | 2019-02-10 09:19:06 UTC | #22

I appreciate your help, I truly do, it should not take me too long to stop asking the "stupid questions".

-------------------------

Leith | 2019-02-11 10:25:11 UTC | #24

Today, I gave the player character an idle animation, and added three more walk animations - so now I have four walks - left, right, forward and backward... time to start experimenting with weighted blending. I'm of the opinion that basing the blend weight only on which keys are being pressed is the wrong idea, I have linear velocity, and a Facing direction... and feel compelled to use that to determine the weighting for blending these animations. Anyone have tips on this?
[EDIT]
I am not certain that the animations have the same length, this could be a problem too. I currently set the animation speed in proportion to the linear velocity, but I didn't account for blending animations of different length.

-------------------------

Leith | 2019-02-12 02:17:29 UTC | #25

Today I am trying to figure out a cheap way to implement Unity's notion of BlendTrees for blending locomotion animations. Ideally, any number of input animations can be blended together, based on the velocity of the character (with respect to the direction it faces), but in practise, we only have to worry about a maximum of two animations at any moment. It works by defining a 'characterspace direction' in 2D for each animation to be blended - essentially we're distributing animations around a 2D circle which is defined in the unrotated / identity space of the character - ie, relative to the direction that the character is facing.

My current idea goes something like this:
The character is moving with some linear velocity - a 3D vector.
Step number one is to transform that vector into the local space of the character, and drop the Y component, so we can think in terms of a 2D circle, on the XZ plane (and normalize it, so its just a 2D direction with unit length),  and think in terms of trigonometry, where zero degrees is our Right vector, and ninety degrees is our Up vector.
Step two: without making assumptions about how many animations are involved?
We find the 2D dot product between the (transformed, 2D) velocity vector, and the direction associated with each animation. We capture the results in an array, and once we have all the dot values, we normalize the array, by dividing each value with the sum of all values. Note that if a dot value is negative, that animation is effectively disabled, and we set the value as zero. The remaining (positive, and normalized) dot values are the weights we should be applying to our animations.

I'm aware that this could be optimized by computing which Quadrant we're working in, however that introduces a bunch of conditional logic, which is likely to cause the cpu to stall, as the compiler can't optimize on branched logic. For a fistful of operations, it's generally faster to avoid the branches, and simply perform operations that were not really necessary for the solution of the problem.

Anyone done any work in this area? I would love to hear your ideas / opinions!

-------------------------

Sinoid | 2019-02-12 05:16:23 UTC | #26

See the Doom animation talk:

https://www.youtube.com/watch?v=3lO1q8mQrrg

They're quite clear on the animation. There were some older GDC animation talks about correction for foot sliding and root motion, basically boiled down to *correct for the constant motion* not correct to lock a *root* in place.

I've been trying out the quat based retargeting from DOOM and using *jiggle bones* on everything for naturalizing stilted-programmer-animation. Not quite there, but getting there,

-------------------------

Leith | 2019-02-12 06:41:40 UTC | #27

I don't plan to recreate GDC solutions, I plan to find the cheapest path that works for me. I don't think that gdc is the right path, just because someone there said it - math has two altruisms, the direct path to the answer, and the shortcut to the answer

-------------------------

Leith | 2019-02-13 07:04:30 UTC | #28

Today I fixed a bug in my foot-planting solution whereby the zombie was able to walk straight through static scenery. The fix involved two parts - first, I am careful to ignore the Y component of my error term, because I want the physics hull to look after changes of position in Y axis. This looked a lot better, but still not good enough.

Secondly, I needed to add a raycast to correct the resulting Y coordinate to account for the fact that my hull is a Capsule, not a box - the feet are not positioned neatly at the bottom of the capsule.

Now the zombie is able to roam "without foot slipping" across uneven terrain without sinking into it, floating above it, or any other weirdness. Results are "close to perfect" :)

The only current issue with the Zombie physics is that it's using weak impulses to drive the character, which I deliberately have given a lot more mass than the Player - the result is that a slow moving zombie can't climb gentle slopes, it needs to get some momentum happening to make it up a hill.
I'll try switching to a force-based controller later today, and see if I can give the zombie some more "grunt".

[EDIT] Switched to using Forces instead of Impulses - will take a bit of tweaking to get the values right, but there's a lot more control, and no apparent problems with "hill-climbing".

-------------------------

Leith | 2019-02-13 07:16:21 UTC | #29

I have no root motion, and the walk cycle is not constant, not linear...  In the case of my zombie, we don't want constant motion - it's limping, or staggering, and in this case, constant motion actually causes foot-slipping. Therefore, I use a constant (but shifting) frame of reference, being the world position of the planted foot, assuming that only one (or not any) foot is planted at any time. The frame of reference is shifting (not moving) at a rate dictated by the animation, not based on any constant. It's actually working pretty nicely, though there are still some small teething issues to sort out.

-------------------------

Leith | 2019-02-14 05:40:51 UTC | #30

Started working on blending locomotion animations (not using a proper blend tree, I'm using some switched logic and AnimationController layers).
First impressions are pretty bad - but the assets need some polish. My animations are not of equal length - it looks like Urho's animationcontroller somehow compensates for this, because there's no visual glitching occuring in the legs of my character, but there is some glitching in the arms and hands, which are further from the root node. I'll start by making all my walk animations have the same play length, and see if that improves things at all. If all else fails, I can ask an artist for some diagonal walking animations.

-------------------------

Leith | 2019-02-15 05:33:02 UTC | #31

Today I synchronized the play length of my four walk animations (for player character).
Previously, they had the following lengths:
WalkForwards = 40 frames
WalkBackwards = 30 frames
StrafeLeft = 45 frames
StrafeRight = 45 frames

I chose to make them all 45 frames in length.
In order to reduce the glitching that remained when blending / moving diagonally, I set the Weight of forward/backward to 0.7, and the Weight of left/right to 0.3

The only thing that's stopping me from applying my "foot-planting" solution to the player character, is related to how I created the "strafe right" animation - it's a mirror of "strafe left", which means that the leading foot is not the same in those animations - I'll need to cut and paste half of my keyframes in order to rectify that.

Rather than screw around with the playback speed of individual animations, I used Blender to adjust the play lengths of my animations... if anyone is interested in how to do that, feel free to ask me.

-------------------------

Leith | 2019-02-16 05:10:30 UTC | #33

Work has begun on an improved ragdoll implementation.
The idea is to attach our ragdoll armature to our model on instantiation, with all the bodyparts set to Kinematic mode, so that they are driven by animations. If done correctly, we don't care about the initial pose - bodyparts are instantianted in "bonespace". I did not rotate these bodyparts! When it comes time to switch (some or all of) the armature to ragdoll mode, the bodyparts are already aligned to the skeletal armature. There are other advantages, too.
https://global.discourse-cdn.com/standard17/uploads/urho3d/original/2X/2/2aacf2aefce29328af084c316fa89591aa196bfd.png
If this experiment works out well, I can probably afford to throw away the coarse outer collision hull entirely.

-------------------------

Leith | 2019-02-16 06:30:37 UTC | #34

[code]
            CreateRagdollPart(adjustNode, "RightUpLeg", ShapeType::SHAPE_CAPSULE, Vector3(0.2f, .45f, 0.0f),Vector3(0.0f, -0.2f, 0.0f), Quaternion::IDENTITY);
            CreateRagdollPart(adjustNode, "RightLeg",   ShapeType::SHAPE_CAPSULE, Vector3(0.2f, .45f, 0.0f),Vector3(0.0f, -0.2f, 0.0f), Quaternion::IDENTITY);

            CreateRagdollPart(adjustNode, "LeftUpLeg",  ShapeType::SHAPE_CAPSULE, Vector3(0.2f, .45f, 0.0f),Vector3(0.0f, -0.2f, 0.0f), Quaternion::IDENTITY);
            CreateRagdollPart(adjustNode, "LeftLeg",    ShapeType::SHAPE_CAPSULE, Vector3(0.2f, .45f, 0.0f),Vector3(0.0f, -0.2f, 0.0f), Quaternion::IDENTITY);            
            
            CreateRagdollPart(adjustNode, "RightArm",    ShapeType::SHAPE_CAPSULE, Vector3(0.15f, .25f, 0.0f),Vector3(-0.15f, 0, 0), Quaternion(0,0,90)) ;
            CreateRagdollPart(adjustNode, "RightForeArm",ShapeType::SHAPE_CAPSULE, Vector3(0.1f,  .25f, 0.0f),Vector3(-0.15f, 0, 0), Quaternion(0,0,90)) ;

            CreateRagdollPart(adjustNode, "LeftArm",    ShapeType::SHAPE_CAPSULE, Vector3(0.15f, .25f, 0.0f),Vector3(0.15f, 0, 0), Quaternion(0,0,90)) ;
            CreateRagdollPart(adjustNode, "LeftForeArm",ShapeType::SHAPE_CAPSULE, Vector3(0.1f,  .25f, 0.0f),Vector3(0.15f, 0, 0), Quaternion(0,0,90)) ;
[/code]

I'm starting with a code-driven approach for testing and debug purposes, but as soon as I'm happy, I'll shove this data into a file and load it per character, as I already do for animation lists.

-------------------------

Leith | 2019-02-16 07:44:03 UTC | #35

![legsarms|690x403](upload://wLxgkHVKM7JTV8KylruV5Il7XV8.jpeg) 
At this point, I don't even need physics constraints between bodyparts, so this armature is still incomplete, yet each bodypart is doing what it should - under kinematic mode, the bodypart constraints are already enforced without need for physics constraints.

-------------------------

Leith | 2019-02-17 03:05:46 UTC | #36

![armature|690x403](upload://lO7ZB0wn2pCLfQC6WMMtaxOwBQd.png) 
Armature is completed (but still unconstrained by joint constraints). Note that I have bodies on the Feet, I plan to experiment with using collision detection to trigger my footfalls, instead of the animation triggers currently used. This will allow the foot-planting solver to work intelligently with uneven terrain and obstacles such as rubble. Whether or not I'll end up using IK as part of this solver is not yet decided. 
The reason this character appears to step outside its outer bounding hull is because I don't enable the foot-planting solver until the first footfall is detected.

-------------------------

Leith | 2019-02-18 09:38:39 UTC | #37

[code]
            CreateRagdollPart(adjustNode, "Hips",   ShapeType::SHAPE_BOX,       Vector3(0.30f, .15f, 0.2f), Vector3(0,0.05f,0),     Quaternion::IDENTITY);
            CreateRagdollPart(adjustNode, "Spine1", ShapeType::SHAPE_BOX,       Vector3(0.35f, .35f, 0.25f),Vector3(0,0.1f,0),      Quaternion::IDENTITY);
            CreateRagdollPart(adjustNode, "Head",   ShapeType::SHAPE_CAPSULE,   Vector3(0.25f,  .35f, 0.0f),Vector3(0, 0.125f, 0),  Quaternion::IDENTITY) ;

            CreateRagdollPart(adjustNode, "RightUpLeg", ShapeType::SHAPE_CAPSULE, Vector3(0.2f, .45f, 0.0f),Vector3(0.0f, -0.2f, 0.0f), Quaternion::IDENTITY);
            CreateRagdollPart(adjustNode, "RightLeg",   ShapeType::SHAPE_CAPSULE, Vector3(0.2f, .45f, 0.0f),Vector3(0.0f, -0.2f, 0.0f), Quaternion::IDENTITY);

            CreateRagdollPart(adjustNode, "LeftUpLeg",  ShapeType::SHAPE_CAPSULE, Vector3(0.2f, .45f, 0.0f),Vector3(0.0f, -0.2f, 0.0f), Quaternion::IDENTITY);
            CreateRagdollPart(adjustNode, "LeftLeg",    ShapeType::SHAPE_CAPSULE, Vector3(0.2f, .45f, 0.0f),Vector3(0.0f, -0.2f, 0.0f), Quaternion::IDENTITY);

            CreateRagdollPart(adjustNode, "RightArm",    ShapeType::SHAPE_CAPSULE, Vector3(0.15f, .25f, 0.0f),Vector3(-0.15f, 0, 0), Quaternion(0,0,90)) ;
            CreateRagdollPart(adjustNode, "RightForeArm",ShapeType::SHAPE_CAPSULE, Vector3(0.1f,  .25f, 0.0f),Vector3(-0.15f, 0, 0), Quaternion(0,0,90)) ;

            CreateRagdollPart(adjustNode, "LeftArm",    ShapeType::SHAPE_CAPSULE, Vector3(0.15f, .25f, 0.0f),Vector3(0.15f, 0, 0), Quaternion(0,0,90)) ;
            CreateRagdollPart(adjustNode, "LeftForeArm",ShapeType::SHAPE_CAPSULE, Vector3(0.1f,  .25f, 0.0f),Vector3(0.15f, 0, 0), Quaternion(0,0,90)) ;

            CreateRagdollPart(adjustNode, "RightFoot",  ShapeType::SHAPE_CAPSULE, Vector3(0.125f, .25f, 0.0f),Vector3( 0, -0.1f, -0.1f), Quaternion(90,0,0)) ;
            CreateRagdollPart(adjustNode, "LeftFoot",  ShapeType::SHAPE_CAPSULE, Vector3(0.125f,  .25f, 0.0f),Vector3( 0, -0.1f, -0.1f), Quaternion(90,0,0)) ;
[/code]

I've found these values, for this one character, empirically. This sucks, I can't be doing this on every zombie model. I need to find a way to automate it, and make it data-driven. I already load a custom xml file per character model for the purposes of getting a list of animation info that are tied to a hardcoded enumeration. I could just extend that custom file to include bodyparts.

-------------------------

Leith | 2019-02-19 08:42:16 UTC | #38

Zombie can now detect when a foot touches the ground, and when it leaves the ground. I don't need animation triggers to tell me, which bodes well for uneven terrain, and basic hill climbing/descent.
Looking forward to bringing in some new zombies and animations :)

-------------------------

Leith | 2019-02-20 06:35:12 UTC | #39

Oh no, it appears that listening for start and end of collision is totally unreliable for the purpose of detecting footfalls! Here's what happens at runtime:

When the zombie begins to walk, I detect that a foot is beginning to touch the ground. A mere few frames later, the physics step happens (again), and despite the fact that my foot bodies are kinematic (so it's not about collision response), I'm told that the foot has left the ground again - which is simply untrue! That foot is still touching the ground, yet I am told that collision has ended! 

I am just lost for words. I really expected this to work reliably. I'll tweak some numbers, but I have a really bad feeling about how stable a solution this will yield.

-------------------------

I3DB | 2019-02-20 21:26:51 UTC | #40

[quote="Leith, post:39, topic:4892"]
collision has ended
[/quote]

The collision EVENT ended, though the foot is on the ground.

-------------------------

Leith | 2019-02-21 04:18:19 UTC | #41

I was under the impression that "collision ended" indicated that two colliding bodies have separated - if that is not the case, what exactly constitutes the "end of a collision event" ? I ask because several render frames and one physics step have passed between receipt of "collision start" and "collision end" events.

[EDIT] 
I've just stared down the relevant code in PhysicsWorld.cpp and it appears that my assumption was correct: "collision end" is only sent when a collision that was collected in a previous physics step has ceased to exist, indicating that two colliding bodies have just separated. I'm going to debug-spew the world position of one of the feet, taking into account the radius on the foot body, just to double-check that my walk animation does not contain any translational glitch that would explain early detection of separation.

-------------------------

Leith | 2019-02-21 05:48:12 UTC | #42

Tweaking the numbers did help, but now I have yet another new issue - the zombie walk cycle is almost a shuffle - the feet are only raised by a very small amount when walking.
The position of the pelvis is currently dictated by an outer physics hull. That hull is a dynamic body, and now I am fighting the "jitter" introduced by bullet's collision response (impulse-based penetration correction). The numbers introduced by the "jitter" of a dynamic body in constant contact with the ground, are in the same order of magnitude as my "foot lift" maximum height, leading to erratic and unpredictable triggering of the start/end of collision events.
I'm going to need to slightly adjust my animation curves on the zombie walk cycle to defeat the "jitterbug", by raising the foot more than the "skin thickness" that bullet applies during restitution.

[EDIT]
I've just read somewhere that the default skin thickness for bullet is set to 0.001 units : problem is, I am seeing jitter values that average more than ten times that much! I'm seeing values in the order of 0.01 to 0.02 - still very small numbers, but big compared to the raised foot height of a shuffling zombie.
Ah! I remember giving the zombie a mass of 10 (so the player can't push the zombie around). That might explain a lot about the numbers I am seeing :)

[POST EDIT]
I've just hit up one of my 3D artist contacts to beg for some help to adjust the curves on the problem walk cycle. He does not owe me any favours, and I did not offer to pay for his time, so chances are high that I'll end up doing it myself. Technical art is within my realm, but I am definitely not an artist.

-------------------------

Sinoid | 2019-02-22 02:32:52 UTC | #43

You're probably too deep into it for it to matter now, but Bullet has a PID example in the InverseDynamics section: https://github.com/bulletphysics/bullet3/tree/master/src/BulletInverseDynamics it's a raw PID so it's sort of sketchy with high-velocity and sudden stops, but a safe base.

> I was under the impression that “collision ended” indicated that two colliding bodies have separated - if that is not the case, what exactly constitutes the “end of a collision event” ? I ask because several render frames and one physics step have passed between receipt of “collision start” and “collision end” events.

IIRC, bullet constructs the manifold over time/substeps, collision separation likely doesn't occur until the active manifold no longer contains a point sourced from the respective *other* object.

There is a check in PhysicsWorld in Urho3D for the number of contacts to minimize that, but it can only be as reliable as Bullet is. If you really care about accuracy, you're going to have to use a ghost-object/query to find it on demand.

-------------------------

Leith | 2019-02-22 06:19:59 UTC | #44

I don't really care that much about accuracy. All my current problems stem from the fact that the zombie walk is almost a shuffle, and so contact make and break is not reliable. Today I enabled IK, and now the feet of my zombie are spinning around wildly :( Gah.

-------------------------

Modanung | 2019-02-22 10:23:08 UTC | #45

[quote="Leith, post:44, topic:4892"]
the feet of my zombie are spinning around wildly
[/quote]
Maybe you forgot a minus or transform space conversion?

-------------------------

Leith | 2019-02-23 01:20:51 UTC | #46

I have attached the ik to descaling nodes under the respective joints -  this is probably playing hell with two-bone ik solver trying to ascertain parents, but otherwise its basically cut and pasted from the sample

[EDIT]
Yeah it definitely appears to me that my "descaling nodes" are the source of the problems with foot IK.
My model was 100x too big (fbx unit bug in assimp), so I added a scaling node near the root to make it 100x smaller. This presented a problem when I wanted to attach rigidbodies to the skeleton - Urho3D automatically sets the local scale of collision shapes to the inherited scale of the parent node. So to counter that, and rather than make my physics armature 100 bigger to compensate, I injected "descaling" nodes attached to the skeleton, and then attached my rigidbodies (and ik elements) to the descaling nodes. These "false bones" are taken into account by the ik solver as being part of the ik chain(s), causing strange results.
At this point I am seriously tempted to extend AssetImporter with an optional scaling feature, which applies a user-defined scale to all vertex and bone positions, because I think that solution is preferable to having to manually rescale all my assets in Blender or Maya, due to the promise of batch-execution.

-------------------------

Leith | 2019-02-24 04:45:28 UTC | #47

Having fixed up the zombie asset scale in blender, I am now getting "crazy legs" due to foot IK, so I probably somehow didnt scale bone positions in animations or something - I'm a Maya guy, trying to learn blender rapidly :(

-------------------------

Leith | 2019-03-01 04:53:08 UTC | #48

The "crazy-legs" bug has been resolved - I now have a walking zombie, with a foot-slipping solver, and leg ik is working too! I just made my zombie walk with one foot on a slope, and the other on flat ground, and found that my foot-slipping solver works perfectly in conjunction with foot ik!
I'll post a video soon-ish, feeling kinda burned from three days of debugging physics issues.

-------------------------

Leith | 2019-03-01 05:13:08 UTC | #49

<https://www.dropbox.com/s/qzuo1wcyzylyvbz/FootSlipping.mp4?dl=0>
There's a problem with the foot ik orientation, but otherwise, everythings working as expected :)

-------------------------

I3DB | 2019-03-01 17:07:34 UTC | #50

Do you use functions such as [SetRotationSilent](https://urho3d.github.io/documentation/1.4/class_urho3_d_1_1_node.html#a8dae47a30f1521ef9502a34f5787da1b) to help the character or zombie make turns without jumpiness?

-------------------------

Leith | 2019-03-02 01:23:44 UTC | #51

No - a fun side-effect of my "foot-planting" solution allows the walking zombie to "pivot" on the planted foot while turning - it looks quite smooth and natural.
Without talking about how I detect footfalls, here is the code I am using to prevent foot-slipping.
The reason that the zombie appears to pivot on the planted foot is because I am teleporting the character's worldspace position such that the planted foot remains planted, thus any simultaneous rotation of the body is compensated for.
[code]
void Character::HandleFootSlipping(){

    if(rightFoot_)
    {

        auto* phyWorld = node_->GetScene()->GetComponent<PhysicsWorld>();
        Vector3 leftFootPosition = leftFoot_->GetWorldPosition();
        Vector3 rightFootPosition = rightFoot_->GetWorldPosition();

        // Cast ray down to get the normal of the underlying surface
        PhysicsRaycastResult result;

        if(rightFootPlanted){

            phyWorld->RaycastSingle(result, Ray(rightFootPosition + Vector3(0, 1, 0), Vector3(0, -1, 0)), 3.0f, CollisionFilter::Static);
            if (result.body_)
                rightFootPosition = result.position_;

            RigidBody* rb = node_->GetComponent<RigidBody>();
            Vector3 slippedPos = rightFootPosition - FootPlantedPosition;
            slippedPos.y_=0; /// Deliberately ignore error in Y : respect the physics hull!
            Vector3 bodyPos = node_->GetWorldPosition();
            Vector3 newPos = (bodyPos - slippedPos);
            node_->SetWorldPosition( newPos );


        }else if(leftFootPlanted){

            phyWorld->RaycastSingle(result, Ray(leftFootPosition + Vector3(0, 1, 0), Vector3(0, -1, 0)), 3.0f, CollisionFilter::Static);
            if (result.body_)
                leftFootPosition = result.position_;

            RigidBody* rb = node_->GetComponent<RigidBody>();
            Vector3 slippedPos = leftFootPosition - FootPlantedPosition;
            slippedPos.y_=0;
            Vector3 bodyPos = node_->GetWorldPosition();
            Vector3 newPos = (bodyPos - slippedPos);
            node_->SetWorldPosition( newPos );

        }
    }
}

[/code]

My current issue is that the "foot ik" is forcing the orientation of the zombie's feet (and legs, and hips apparently) to all face in the world-z direction that was set up prior to attaching the ik elements. That is to say, the ik solver is being solved in worldspace, and not respecting the fact that I have rotated the entire character around the world Y axis!
When the player character walks up behind a zombie who is facing away from player, the zombie turns around and begins walking toward the player, but its feet (and the rest of the ik chains) remain oriented in the original direction, so now the feet are backwards, and the legs are twisted.

Here's what the IK effector setup looks like (per foot):
[code]
            leftEffector_ = leftFoot_->CreateComponent<IKEffector>();
            leftEffector_->SetChainLength(2);
            leftEffector_->SetINHERIT_PARENT_ROTATION(true);
[/code]

and here's what the ik solver setup looks like:
[code]
        bone = skel.GetBone("Hips");
        if(bone!=nullptr && leftFoot_!=nullptr && rightFoot_!=nullptr)
        {
            Node* hips = bone->node_;//->GetChild("Descaling_Hips");
            solver_ = hips->CreateComponent<IKSolver>();

            // Two-bone solver is more efficient and more stable than FABRIK (but only
            // works for two bones, obviously).
            solver_->SetAlgorithm(IKSolver::TWO_BONE);

            // Disable auto-solving, which means we need to call Solve() manually
            solver_->SetFeature(IKSolver::AUTO_SOLVE, false);

            solver_->SetFeature(IKSolver::JOINT_ROTATIONS, true);       // Character is skinned
            solver_->SetFeature(IKSolver::TARGET_ROTATIONS, false);     // Don't align to target orientation
            solver_->SetFeature(IKSolver::USE_ORIGINAL_POSE, false);    // Don't use original pose
            solver_->SetFeature(IKSolver::UPDATE_ACTIVE_POSE, true);    // Do update animated pose
[/code]

I enabled "Inherit Parent Rotation" on effectors for the following reason:
[quote]
      /*!
         * By default the end effector node will retain its global orientation,
         * even after solving. By enabling this feature, the node will instead
         * "rotate with" its parent node.
         */
INHERIT_PARENT_ROTATION = 0x02
[/quote]
But it seems to be not doing anything :(

Can anyone give me some guidance on how to make the ik solver respect the orientation of the character to which it is attached?

-------------------------

Leith | 2019-03-02 02:23:36 UTC | #52

I've solved all my foot-ik issues.
In my case, I needed to disable both joint and target rotations.
The following quote taken from Urho documentation apparently is not true for my use-case:
[quote]
JOINT_ROTATIONS 	

Should be enabled if your model uses skinning or if you are generally interested in correct joint rotations. Has a minor performance impact.

When enabled, final joint rotations are calculated as a post processing step. If you are using IK on a model with skinning, you will want to enable this or it will look wrong. 
[/quote]

Urho documentation says that disabling joint rotations on skinned characters "will look wrong" - but I handle foot orientation myself (to align feet to slopes) as per the ik sample.
Looking good :slight_smile:![Screenshot%20from%202019-03-02%2013-16-02|690x403](upload://fBGvvcpm8O4oV9HBu1EiF3VvlfU.jpeg) ![Screenshot%20from%202019-03-02%2013-16-41|690x403](upload://ofxcZGBGPpmBkmfOtpov19ACJ6X.jpeg)

[EDIT]
Hmm, that first screenshot does look weird - I may need to do more work on this issue, I'd love to hear from anyone who has dealt with the issue - we want the ik solver to apply rotations in character space, and also to specifically omit the bones where the end-effectors are attached.

-------------------------

Leith | 2019-03-02 02:53:33 UTC | #53

I'm in a jam.
With JOINT_ROTATIONS disabled, the character's foot orientation is coming from the bone animation, and looks correct, but the legs of the character are distorted at the knee.
With JOINT_ROTATIONS enabled, the knee looks correct, but the feet are oriented in a fixed worldspace direction, and when the character rotates 180 degrees in Y, the feet are backwards, the ik chains remain relative to worldspace so the body is contorted from the hips down.
I can't seem to find a combination of settings that lets the ik solver apply joint rotations correctly on a bone-animated skinned character. Somehow, I need to inform the solver root node to inherit the orientation of the character, not to operate in worldspace but to operate in characterspace.

I guess I am running out of options, the only thing I haven't tried is ik target orientation. I guess I could compute the orientation of the target, but it seems like overkill, and likely I'll lose the animated orientation of the raised foot (which flops around adorably). I was hoping not to have to solve foot orientation as part of the ik solver. Love to hear from you guys about it.

-------------------------

I3DB | 2019-03-02 22:38:17 UTC | #54

My view of zombies and kinetics is stilted ... I mean why mess around with lots of details when you can do it in one slap?
![forwardKinetics|232x500](upload://tkkvAVvBOL1V4u1yZcSYviBLzRV.jpeg) 

![zombies|538x383](upload://eXFlIPG3Oz85nULvDFN8uFPvCRl.jpeg)

-------------------------

Leith | 2019-03-03 05:09:14 UTC | #55

Eventually, I did find settings for foot ik that work on an animated skinned mesh that has a dynamic physics controller.
[code]

            solver_->SetFeature(IKSolver::JOINT_ROTATIONS, true);      // Character is skinned - we care about rotations
            solver_->SetFeature(IKSolver::TARGET_ROTATIONS, false);     // Don't align to target orientation
            solver_->SetFeature(IKSolver::USE_ORIGINAL_POSE, false);    // Don't use original pose
            solver_->SetFeature(IKSolver::UPDATE_ACTIVE_POSE, true);    // Do update animated pose
            solver_->SetFeature(IKSolver::UPDATE_ORIGINAL_POSE, true);  // Do apply the solution to the original pose
[/code]

That last one was required to ensure that the ik solver respected the orientation of the character when JOINT_ROTATIONS is enabled :slight_smile:  I truly hope that this information is useful to anyone who attempts to deal with a similar scenario - the ik sample does not use these settings, but then again, that character never moves or rotates.

-------------------------

Leith | 2019-03-04 07:41:15 UTC | #56

My player character derives from the same class as non player characters (well, not quite derives from, there's currently an isPlayer flag, and some switchcase logic, though I plan to derive soon) - I've now applied all this foot-ik and foot-slipping stuff to the player character, who has more locomotion animations than the zombies.
It's a bit twitchy sometimes, and the feet appear to be bent too much on some slopes, but I have not yet tweaked the ik settings (they are default values), or closely examined the foot orientation stuff.

I've got two outstanding issues at the moment - walking downhill looks wrong because the character outer hull prevents the front foot from reaching the ground (I think I can tackle this one easily enough), and the animations for walking forwards and strafing sideways are incompatible - they have the same length, but the footfalls are not on the same keys, so blending them leads to bad-looking results.

Manually cutting and pasting a few keys should bring my animations into synch, and moving the outer hull down to satisfy the lower foot should let the leading foot reach the ground when travelling downhill / walking down steps.

I'm tempted to remove the outer hull altogether, in favour of ragdoll bodypart hulls - but that turned out to be a bad idea in terms of detecting footfalls on a staggering (shuffling) zombie, as it was difficult to tune the foot bodies for clean make-and-break with a level surface, let alone uneven terrain.

-------------------------

Leith | 2019-03-04 10:10:13 UTC | #57

Insight from the work of others:
Here's how I plan to deal with walking "downhill".

Anytime in our walk cycle, we can measure the height of the 'unplanted' foot with respect to a theoretical level plane (lets call it A - in my drawing its zero, so I don't show it). We can also measure the height from that plane to the terrain surface - this is our error term, B (shown in red).
We want to move the root of our character DOWN, such that the height from the terrain to the unplanted foot equals A (I believe this is simply pelvis Y - B, plus accounting for the foot offset, since the foot bone is really the ankle, and is never equal to the plane Y). We want to do this immediately after animation is applied, but before IK is applied. The result should be that the unplanted foot has height A above the terrain, and the planted foot, and its leg, bend further to make that happen.

The proposed solution was borrowed from Unreal engine.

![StepDown|640x400](upload://ho33G3DePhjlPPQvWU8m1Ada6l1.png)

Super sorry for my terrible coder art, but the final result from the proposed solution would be something like this golden thing: (noting, I don't think we need to lean forward and backward at this stage)
![StepDown2|640x400](upload://vDQImih6kUkXc1VTLhOqZamxxjZ.png)

This solution violates the length of a single step in the walk cycle with respect to the animation, but I suspect my foot-planting solution will compensate somewhat for the error, and IK solver will at least try hard to do the rest. Essentially, we will take longer steps when moving downhill, as we already take shorter steps when moving uphill - the animation speed is already tied to the velocity of the hull, and it all should "just work" - maybe.

The foot-planting solver is tied to the animation speed, and adjusts the velocity of the hull (through sheer position teleport) to tie in with footfall triggers in the animations. It effectively "post-empts" the velocity of the hull, and compensates for weirdness in walk cycles. I'm sort of crossing my fingers, but in my engineers mind, there are two levels of compensation on top of basic dynamics, it might just work (on slopes or stairs that climb by a max of 30 degrees per step) :)

I've not needed target orientation for orienting feet so far, and trying hard to resist predicting footfalls (like some other solutions do) as I don't want to analyze animation keys unless I have absolutely run out of options. I don't need perfect accuracy, just fluid motion.

-------------------------

Leith | 2019-03-05 08:28:31 UTC | #58

I'd like someone to doublecheck my logic before I code this up, perhaps it can be optimized.

[quote]
This is for character foot solving when walking downhill.
It should also "just work" for uphill travel.
We perform this code in response to the SceneDrawableUpdateFinished event, such that Animation has already been applied. 

1 - Initialization.
We get the (BindPose) World Position of the Hips, and note the Y offset from the Hips to one of the Feet. This is our Base Foot Offset value, which indicates the length of the legs at the moment when the feet are "crossing" during locomotion.

2 - Runtime.
We get the (Animated) World Translation of the Pelvis / Hips - this acts as our Datum, our point of reference.

3.
Now we find the Y-offset from Hips to the Unplanted Foot - we'll call this the Animated Foot Offset.

4.
We find the difference in Y height between Base and Animated Foot Offsets, we'll call this the Current Foot Height. It represents the height of the Unplanted Foot, when walking on a flat plane.

5.
We cast a ray from the Unplanted Foot down to the terrain.
We note the Offset (in Y Axis) between the foot and the collisionpoint.
We add that value to the Current Foot Height, we call the result the Error Term.

6. 
We subtract the Error Term from the World Position of the Hips.
This brings the Unplanted Foot into contact with the Terrain, while the Planted Foot will sink into the Terrain.
We counter this somewhat by adding the Current Foot Height term.
This raises the Unplanted Foot UP above the Terrain to restore the animated Current Foot Height.

7.
We're now ready to perform IK Solving, which will bend the leg on the Planted Foot such that it no longer penetrates the Terrain.
[/quote]

-------------------------

Modanung | 2019-03-05 08:16:37 UTC | #59

I wonder how this approach will work on steep slopes, stairs and cliff edges.

-------------------------

Leith | 2019-03-05 09:47:10 UTC | #60

It should work well on slopes of (+/-) 30 degrees or less, and stairs, and obstacles, where the "rise over run" is 30 or less. I expect it to work terribly on slopes of 45 or more degrees (which we typically can't climb with a dynamic controller) - but the typical "rise" on staircases happens to be 30 deg.
It won't work for cliffs :P It won't work for Quadrupeds, or for spiders, although I am certain that a similar algorithm could be evolved that can cope with more than two feet (Final IK for Unity manages to do so, therefore it can be done).

I did mention, this technique is not mine - my description of the technique is all I can lay claim to, this stuff was based on a solution that ships with the Unreal engine, and is described somewhat in the documentation.

Also, I expect to have to modify the existing foot ik logic, which makes assumptions about where we want to plant the ik targets for the feet, but I expect that to be trivial, and indeed, I expect to marry the proposed and existing code to eliminate redundant raycasts (my foot-slipping solution runs just after the foot ik solver, and requires a ray be cast from each foot, so I already have something to eliminate in the name of efficiency).

Finally, I have a gut feeling that I'm going to need to execute the IK Solver twice, to deal with the fact that the unplanted foot becomes unplanted when it is leaving the ground, which on a theoretical plane, sets it inside the terrain on a downhill slope.
I hope to take advantage of the foot-planting positions to avoid that, by remembering not just where the current planted foot is, but where the previous planted foot was. I may need to start using more than two keys on my animation triggers (Unreal uses four). The algo as presented will likely be refined. Etc.

-------------------------

Leith | 2019-03-05 09:12:30 UTC | #61

I disable the foot IK stuff when jumping - in debug it looks very funny to see the IK legs stuck to the ground while the character and its physics body (or bodies) are jumping. Falling is equivalent to jumping, if I have to deal with cliffs, and my character is not a spider, I should be ok - maybe.

-------------------------

Leith | 2019-03-05 09:43:32 UTC | #62

One issue with the primitive collision hull (character capsule), due to my foot-planting solution, is that its fairly easy to teleport through solid walls. Effectively, I am teleporting the hull to compensate for the planted foot. CCD could help here. I remember bugs in Star Wars : Battlefront (the first one) that could be explained by this. There were quite a few. (One of my teachers, during my bachelor degree, worked on KOTOR, and Sims 3, he had plenty to say about bugs and deadlines).
I am sorely tempted to eliminate the character hull in favour of potential ragdoll bodypart hulls, and discounting the extra processing cost in terms of "hey, I know what bodypart I hit, I can do a partial ragdoll on that"

-------------------------

I3DB | 2019-03-06 21:37:38 UTC | #63

[quote="Leith, post:58, topic:4892"]
I’d like someone to doublecheck my logic before I code this up, perhaps it can be optimized
[/quote]

Seems like a lot of coding for a minimal outcome. Or perhaps I'm not seeing the value of going through that code logic to upturn or downturn a foot.

Can't normals be compared to figure rotation and then be done and go on?

What happens if someone slaps the zombie? Does it's head turn round? Shoulders react? The full body goes ragdoll (as per the sample by removing physics and collision shapes and adding bones and constraints)?

Just wondering if there isn't an easier approach that works. [Applying forces to a ragdoll body appears already fluid and realistic.](https://urho3d.github.io/samples/13_Ragdolls.html) (with forces, you can cook the zombie with one slap and sprinkle on some angular torque for some sweet eye candy).

-------------------------

Leith | 2019-03-07 03:49:15 UTC | #64

All that code is just needed for downhill locomotion, to pull the outer collision capsule (or just the character root) downwards enough such that the front foot can reach the ground!
Without it, the collision hull prevents the foot ik from being able to reach down lower than the horizontal plane that the walk animation was designed for.

Uphill locomotion I'm not worried about - the capsule does all the work of positioning the character with satisfactory results (the error is too small to worry about) but downhill looks very wrong when the leading foot can not reach the ground. This is most evident when the character is placed such that one foot is standing on a raised ledge, and the other is perched in mid-air, while it rightly should be much lower.

Currently I have no reaction when the zombie is hit - I was thinking of using some additive blending of canned "twitch" animations, rather than full-body ik. I have implemented code for "partial ragdolls" to simulate broken limbs, but I'm going to need a few more animations before I can finish that stuff - what happens if we break both the legs? :)
Unlike the sample, I don't remove hull physics and add the ragdoll bodyparts/constraints at the last moment - I create the ragdoll bodyparts during initialization, leave them unconstrained, and put them into "kinematic mode" so they are animated along with the skinmesh - this lets me determine at runtime exactly which bodypart was hit.
For partial ragdoll, I switch all bodies on a bone chain from kinematic to constrained dynamic mode, so that chain is now in ragdoll mode, but the rest of the skeleton is still animated.

-------------------------

I3DB | 2019-03-07 15:05:05 UTC | #65

[quote="Leith, post:64, topic:4892"]
needed for downhill locomotion, to pull the outer collision capsule (or just the character root) downwards enough such that the front foot can reach the ground
[/quote]

Ok, but why not just rotate the zombie so even on a downhill slope the zombie shape is rotated so the traversed surface remains horizontal for locomotion across it? Meaning a 45 degree incline being traversed will incline the zombie 45 degrees also.

Alternatively, assuming the zombie should remain precisely vertical at all times so the depth of each step might be less or more than the depth of the previous step, based upon some rotation of the normal of the surface underneath it at that point in time. 

In such case the depth of the step is only a function of the normal of the surface (or terrain) being traversed. This can work for some inclines, certain for those of minimally inclining terrain.

In treating the zombie as a body of many parts, the depth of the step changing then causes other changes throughout the zombie body, where you mention things like the hips being affected.

And yet it would seem the rotation can be applied only to the foot of the zombie for some terrain inclinations and not have to involve IK. As the inclination increases, the zombie might just start sliding rather than walking.

What am I saying?

1. So much logic and coding, and I'm not sure just what it achieves of lasting value. Is the code re-useable for other actions of the zombie? If you get the step perfect, can that same code be applied to other actions or reactions of the zombie (for instance, when it gets slapped, or some other envisioned motion or movement of the zombie)?

2. Are there other and much simpler ways to get most of what you're trying to do? Is implementing IK the most important piece of this puzzle you're solving, or is getting the zombie to appear to step properly when examined closely to primary goal? 

3. Are you majoring in IK, when you should be minoring in it? Is IK really needed at all? 

You admit this is just a rewrite of some approach used by Unreal. It might not be a viable approach, just one used for some specific reason rather than a generally applicable and workable approach.

[quote="Leith, post:60, topic:4892"]
Finally, I have a gut feeling that I’m going to need to execute the IK Solver twice
[/quote]

If so, I get a gut feeling the overall approach to solving this could be simplified by doing something else once.

When I'm walking uphill or downhill it's difficult and causes my body to do 'unnatural' motions which vary depending upon the slipperiness and incline amount. Trying to code up these 'unnatural' motions causes a lot of guessing and assumption making. If I drag a leg and try to walk uphill or downhill, it's quite a brain teaser at times.

-------------------------

Leith | 2019-03-08 04:38:36 UTC | #66

Thanks to some clarification about two particular lines of source in the IK Sample, I've been able to head down a completely different path to solving the same issue - which is the need to drag downwards the character when walking downhill.

Currently, I begin by computing the positions of the foot IK effectors as per the sample.
But before I execute the IKSolver, I examine the positions of the foot effectors I've just computed, I transform them into local character space so I can tell which foot is in front of the other, and I am able to then determine if the character is trying to walk downhill or uphill.
If walking downhill, I can now compute an error term (in Y) for the unplanted and leading foot (indicating that the unplanted foot has crossed over in front of the planted foot), and apply it to the root node. I'm not done with the implementation - it's both incomplete, and sub-optimal, but early tests look good.

[code]
        /// Note the worldspace position of each foot-effector
        Vector3 leftEffectorPos  = leftEffector_ ->GetTargetPosition();
        Vector3 rightEffectorPos = rightEffector_->GetTargetPosition();

        /// Note the worldspace Y coordinate of each foot-effector
        float leftEffectorHeight  = leftEffectorPos.y_;
        float rightEffectorHeight = rightEffectorPos.y_;        
        
        /// Transform the effector positions from worldspace to local space of character
        Vector3 lel = node_->WorldToLocal(leftEffectorPos);
        Vector3 rel = node_->WorldToLocal(rightEffectorPos);

        /// If right foot is planted, and left foot is "in front" and is lower than right foot
        /// ie the left foot has "crossed" in front of planted right foot, and we're heading downhill
        if( rightFootPlanted && lel.z_>rel.z_ && lt < rt+0.1f)
        {
            std::cout << "breaktime :z = " << lel.z_ <<","<< rel.z_ << " and y=" << lel.y_<<","<<rel.y_<<std::endl;
        }
        /// ELSE
        /// If left foot is planted, and right foot is "in front" and is lower than right foot
        /// ie the right foot has "crossed" in front of planted left foot, and we're heading downhill
        else if( leftFootPlanted && rel.z_>lel.z_ && lt > rt+0.1f)
        {
            std::cout << "breaktime :z = " << lel.z_ <<","<< rel.z_ << " and y=" << lel.y_<<","<<rel.y_<<std::endl;
        }
[/code]

Obviously this is not production quality code - I like to get things working, then optimize them.

-------------------------

Leith | 2019-03-10 06:58:06 UTC | #67

IK is usually cheaper and generally more accurate than prediction on undulating terrain - I did try not to use IK, but in the end I had to decide between IK (which uses an iterative solver) and prediction (which is generally more prone to error given little to no local knowledge of the geometries, given the absence of a navmesh or even a butterfly mesh). I did not want to create a solution that was based on an assumption that the walk cycle was a linear, regular walk. IK seemed like the best option, in combination with animation on uncertain terrain.

-------------------------

Leith | 2019-03-09 03:53:56 UTC | #68

Why not rotate the zombie?

Unreal's solution does lean the character a little (forwards, on uphill, and backwards, on downhill, counter to the surface normal) when walking up or down slopes.
I think this is accurate, as we need to compensate our center of mass when tackling a slope.
But the amount of rotation is small - it does not follow the surface normal per se - in fact, the direction of the lean rotation is the reflection angle, ie, counter to the normal. So far, I don't bother implementing it, I'm restricting myself to foot solving until I am satisfied with the results in all corner cases.
It would look silly to see a character rotated to 30 degrees on a 30 degree slope - the center of mass would be way off.

-------------------------

Leith | 2019-03-10 06:48:10 UTC | #69

Current solution involves dragging down the root node of the character to match the height of the unplanted foot's effector - when it has crossed ankles ahead of the planted foot's ik-effector, when the effector for the unplanted foot is lower in height (ie we are walking downhill).
That is an incomplete solution, and appears to generate some jitter due to penetration correction of a dynamic hull, but generally seems to work, and indicates I am moving in the right direction.
Effectively, I move the entire character root down to match the height of the effector on the unplanted, leading foot. I let the IK solver deal with the fallout from doing so, but I know that the leading foot can at least reach the ground, minus its animated height. 
After doing all that, I go on to apply the foot-slipping solver, which corrects the torso XZ position, but ignores the Y position correction we made, such that the character root is teleported in XZ to satisfy the planted foot remaining where it was planted.
The order of operations is in question - everything is in question - but it's getting closer to decent.
Man, I am so tempted to get rid of the dynamic hull, but its good for certain things, and I already control animation speed / footfalls / footslipping based on the velocity of the hull in a dynamic world, looking for a way out :stuck_out_tongue:

-------------------------

Leith | 2019-03-10 07:28:19 UTC | #70

The camera has no lerp, so its flickery when we teleport the root of the model it points at, but at least heres some content, with downhill correction looking reasonable
<https://www.dropbox.com/s/qzuo1wcyzylyvbz/FootSlipping.mp4?dl=0 />

-------------------------

Leith | 2019-03-11 03:45:23 UTC | #71

Zombie is now loading all Ragdoll information from its "Character Descriptor" xml file.
I use these custom xml files to "describe" my characters - they contain details for all the character's animations, the names of important bones for Foot IK, ragdoll bodypart descriptors, and joint constraint descriptors, everything required to create a full ragdoll specific to that character. This makes my character class "data-driven" instead of "completely hardcoded and derived per character type".

When I instantiate a ragdoll in "kinematic mode", it perfectly follows the animations applied to the skeleton - problem is though, Bullet does not look for collisions between kinematic bodies, so it looks like a bad choice for detecting where the zombie was hit by, say, a kinematic sword in the kinematic hand of the player character.

I really need to use dynamic bodies - but tie them to the animated skeleton, disregarding Bullet dynamics while manually animating the RigidBodies.

Erwin suggests that I should be measuring the "stress" at the joint constraints, and using the resulting velocities to drive motors on the joints. I think that sounds needlessly complex?

I guess I am reaching the point where I have to reach out further than this community, but I thought it might be worth asking before I dig myself into a new hole.

-------------------------

Leith | 2019-03-13 08:04:42 UTC | #72

I found a slightly improved algorithm for "pulling down" the root node - simply put, we move it to the animated height of the lower foot (while accounting for the bindpose foot offset) from character root.
Anytime in the walk cycle, this is true. No matter which direction we are moving, or on what slope.
Will implement shortly, I was side-tracked slightly by another issue.

-------------------------

Leith | 2019-03-19 07:51:33 UTC | #73

Today I performed a technical fix on my "strafe right" animation.
I had scaled the length of my four cardinal walking animations to be the same (45 frames).

When walking forwards, backwards, or left-strafing, the animations were generally in agreement - the left foot would fall first, and roughly on the same keyframe, and later the right foot, again roughly on the same keyframe.
But the right-strafing animation had been created as a mirror of the left-strafe animation. So it began on the right foot, and although I could still set up animation triggers on the footfalls, the animation itself was unsuitable for blending with forward and backward animations to create eight cardinal directions (four pure animations, and four blended "diagonal" animations).

I used blender to cut and paste half of the animation keys on the right-strafe animation, so that the left foot was the first to move.

Now I tested my changes - animation blending is still very twitchy and unsatifying - the walk cycles are just too different to be blended as such. I am not blaming urho's blending implementation, but I am seeing random flickering during advancement of two blended walks of equal length, and whose footfalls occur at or near the same frame, with the left foot leading in all animations.

I'll need to create some diagonal walk animations to suit myself, based on baking the existing ones in blender. This will give me eight cardinal direction animations, and potentially, 16 that blend more nicely.

I'm also starting to experiment with script objects - hotloading scripts is a lot cooler than rebuilding the app, and scripted classes can be promoted to c++ based on their runtime cost/benefit ratio

-------------------------

Leith | 2019-03-20 06:13:28 UTC | #74

[code]
    // Experimental:.. try to use pre and post physics events to deal with constraining dynamic bodies to animated skeleton
    SubscribeToEvent( E_PHYSICSPRESTEP,  URHO3D_HANDLER(Character, HandlePrePhysicsUpdate ));
    SubscribeToEvent( E_PHYSICSPOSTSTEP, URHO3D_HANDLER(Character, HandlePostPhysicsUpdate));
[/code]

Essentially, I want to animate a constrained set of dynamic bodies: I want the bodies to derive their momentum from the animation. The main problem with that idea, is that in Urho, animation controllers are one of the last things to get updated in a frame.

When bodies are kinematic, Bullet will ask Urho RigidBody for their world transform (via motionstate interface), but when they are dynamic, Bullet will attempt to drive their node transforms (again, via motionstate), which indicates that, for dynamic bodies, I should at least wait until after the physics has updated... Well, I tried that, and it didn't appear to work as expected, so I'll take some more time to trace values and then do some head-scratching based on the empirical data.

-------------------------

Leith | 2019-03-21 09:22:29 UTC | #75

Today, I managed to constrain dynamic bodies to the bones of an animated character.
The result is a little bit shaky, but acceptable, given that competing systems are attempting to adjust the same scene nodes.

The way I achieved this, was to listen for the "post-physics update" event, which tells me that Bullet has just finished messing with my rigidbodies, at which point I call this method:
[code]
void Character::copyModelStateToRagdoll()
{
	for (int i = 0; i < ragdollParts_.Size(); ++i)
	{
        ragdollParts_[i]->SetTransform( Vector3(0,0,0), Quaternion(1,0,0,0));
        RigidBody* body = ragdollParts_[i]->GetComponent<RigidBody>();
        body->SetAngularVelocity(Vector3::ZERO);
        body->SetLinearVelocity(Vector3::ZERO);
        body->ResetForces();
	}
}
[/code]
Note that I connect my rigidbodies not directly to the bone nodes, but to a child node of each bone node, which I call "descaling nodes" (this particular model has not been correctly scaled, one of the nodes near the root introduces a scale factor that needs to be "cancelled" prior to attaching anything to the rig).
The above method forces the local transform of the rigidbody parent nodes to identity, such that they directly inherit the world transform of the bone nodes. This causes the dynamic rigidbodies to follow the animations applied to the bones - not as smoothly as kinematic bodies, but given the advantages of dynamic bodies over kinematic ones, I'll call it a win :slight_smile:
Perhaps I'll upload a video later today, which shows the "shaky but acceptable" results of my efforts.

[Edit]
Oh - I should mention that I'm also creating my ragdoll constraints upfront, and have discovered that the constraint resolver is entirely responsible for the "noise" in the body transforms - I simply need to disable my constraints until I need them, or add them when I need them. For now, I chose to create them upfront, but disable them. They exist, but they are not active.

At this stage, I am ready to try to implement partial ragdolls :)

-------------------------

Leith | 2019-03-22 03:29:48 UTC | #76

I'm uploading a short video of "Animated Dynamic Ragdoll" (applied to Zombie) which also implements "foot-planting" and "foot-ik". The player character currently has no ragdoll, but does have everything else.
<https://www.dropbox.com/s/mkqfdv6q5g6s6lj/DynamicRagdoll.mp4?dl=0>

Currently, I zero out all velocity (and force) when I teleport the dynamic bodies to match the animated pose, but I intend to deliberately omit that step for bodyparts that are "in ragdoll mode". At the moment that a bodypart enters "ragdoll mode", it should inherit the velocity (and implied forces) that are due to the animation. This should result in a "clean handover" from animated mode to ragdoll mode, with the ragdoll dynamics "continuing" from the last known animated pose.

-------------------------

Leith | 2019-03-23 10:03:31 UTC | #77

My next step is to process my "jump" animation, to get rid of that nasty old root motion.
I wish that our export toolchain could just optionally do that.
I use a Dynamic character controller scheme, so I don't want root motion - I provide it, while synchronizing the animation speed. This gives me a lot more control over a character on uncertain terrain, and although it is harder to do and harder to get right than a purely kinematic solution, it is more plausible on uncertain terrain than pure kinematic solutions. It can adapt, within a margin of error.

-------------------------

Leith | 2019-03-27 07:29:53 UTC | #78

Today I added a "falling" animation, and some logic to deal with that.
Somewhere I missed a logic bug, because the results were not as expected.
Time to remap and verify my logic.

-------------------------

Leith | 2019-04-03 05:21:08 UTC | #79

Today I decided to set aside my Dynamic Character controller, and began experimenting with a Kinematic Character controller. To be honest, there's a lot NOT to love about kinematic objects with respect to Bullet physics, but I always explore my options before choosing what feels right for any particular game.

The dynamic controller used dynamic velocity to adjust the playback speed of locomotion animations, which were devoid of root motion.

The kinematic controller will be taking a very different approach: animations will contain root motions, and I'll be using them to drive the kinematics, so that the "feel" that the animators gave to character animations are not lost to the physics engine. I hope to solve foot-slipping "for free", while still applying foot-ik. Animation playback speed will determine motion speed, and not the other way around.

For now, I'm basing my work on that of 1vanK, who provided us with a small wrapper around btKinematicCharacterController, but I'm quite willing to derive from the Bullet class, or even write a proxy based on it, depending on how things turn out... if this works out as I hope, I'll implement the resulting class as a physics component of Urho3D, and issue a PR.

-------------------------

Leith | 2019-04-05 07:06:36 UTC | #80

The main difference between my new kinematic controller, and the original (by 1vanK) is that I don't want to use keyboard input to drive kinematics - instead, I will be using keyboard input ONLY to play animations (containing root motions), and extracting kinematic motion information from the animated model's node... this will present a small challenge, since animation and physics updates are asynchronous, and in those frames where both events fire, the order of execution is not ideal - my physics update will only have access to the results of the previous frame's animated state, and I'll need to track animated state changes inbetween physics frames... this could make life interesting :)

What I'm pointing out, and please correct me if I am wrong, well, it's that Animation is pretty much the last thing that happens in a frame update - and assuming that physics runs at a lower framerate (as we would expect, given we can interpolate it for rendering) then in those frames where physics update does fire, it fires before animation is updated. Therefore, we can't apply the results of animation for the current frame to the physics state - we're always going to have a situation where the physics state is representing the previous animation frame. In this modern age of graphics hardware, I expect that the update/render framerate is always higher than the physics update. Currently I get around 600 FPS (vsync disabled) versus the fixed rate for physics at 30fps. I like to unlock vsync during development, so I can budget my "spend" and quickly notice any serious issues that I have inadvertently, and recently, introduced... if I add a bottleneck by accident, I detect it almost immediately.

-------------------------

Leith | 2019-04-08 08:19:54 UTC | #81

Now I have the new character controller implemented, I am extending it to deal with animations - this is where the fun begins for me. One of the first issues relates to non-looping animations.

So far, I've concentrated a lot on "locomotion", and the animations that drive it. Walking/Running in any direction is always a Looping animation. But Jumping usually is not a looping animation.

That's all ok, until you hold down the jump button, and expect to be able to jump again!
The character will jump, but its animation is frozen in time at the end of the keyframes, and remains so until you change animations :frowning: Calling Stop on the animation is not enough to fix it. And we can't remove the animationstate from the controller, because the remove method is private.

I tried a few different ways to kill off that animation state from its controller, but failed so far to find a way around this.

-------------------------

Leith | 2019-04-11 09:42:59 UTC | #82

The most major change when switching to kinematic player controller is the lack of friction - movement feels very "plastic", and it stops immediately when you released controls - and it seems like I'll have to hack in some basic friction and drag model. I'm working with btPairCachingGhostObject under the hood, it has some advantages in terms of optimizing collision queries, but doesn't impose dynamics.

-------------------------

Leith | 2019-04-13 04:19:11 UTC | #83

With respect to detecting root motion, my jump animation has a problem - the animator decided not to animate the model root node to control the hips, they instead chose to animate the hips directly.
I've asked for help with a workflow for fixing the technical art, but I am already thinking that I can just control this stuff in code, driven by data from my per-character xml animation set information

For each character model, I look for an xml file named after the character model, which contains information about the available animations, the names of some important bones for ik, and so on.

-------------------------

Leith | 2019-04-13 04:30:44 UTC | #84

I added some more locomotion animations to the kinematic controller today, but they're just the old ones, devoid of root motion - I just wanted to get this new controller to about the same state as the old dynamic one before I go changing things too much.
It turns out that detecting root motion derived from animation is non-trivial.
Artists are meant to animate the root bone - but sometimes they don't.

-------------------------

Leith | 2019-04-14 04:56:14 UTC | #85

<https://www.dropbox.com/s/xt5zvl4iylu83ip/WIP.mp4?dl=0>

Player is using a basic kinematic character controller, with no fancy foot-ik or other bells and whistles.
Animations are devoid of root-motion, except for the jump animation, which annoyingly applies animation to the translation of the hips, not the root node. No fix yet implemented.

Zombie is using a dynamic character controller, with fancy foot ik, foot-slipping and stepdown solvers, and pseudo-kinematic physics rig, where dynamic bodies are teleported according to animations, such that they retain their last known momentum when "released" into ragdoll mode.![shot|690x194](upload://pLnIwnWNFarIO3PXaSlLrQ3UVsI.jpeg)

-------------------------

Leith | 2019-04-15 07:56:24 UTC | #86

Today I met AnimationController's IsAtEnd method. This goes part of the way to breaking the ice with respect to non-looping animations in a clamped condition!

[code]
    /// If our Character is "Airborn"
    if(!bulletController_->onGround()){
        /// Is the character currently jumping?
        if(isJumping_)
        {
            /// Character is performing a Jump...
            /// Check if the jump animation has reached the end (it's a non looping animation, clamping at the end frame)
            if(!animCtrl->IsAtEnd(Animations_[Animations_Player::Jump].Name))
            {
                // Adjust Jump animation speed, so that on a level plane, the physics hull ought to land before animation finishes
                animCtrl->SetSpeed(Animations_[Animations_Player::Jump].Name, 0.72f);
                // TODO: Suppress Y translation in the hips (relative to root node)
                animCtrl->PlayExclusive(Animations_[Animations_Player::Jump].Name, 0, false, 0.2f);
            }
            else
            {
                /// Jump animation has ended - but character is not touching the ground...
                /// Start falling!
                animCtrl->PlayExclusive(Animations_[Animations_Player::Fall].Name, 0, false, 0.2f);
            }

        }else{
            /// Character is definitely falling - they've slipped off the edge !!!
                animCtrl->PlayExclusive(Animations_[Animations_Player::Fall].Name, 0, true, 0.2f);
        }
[/code]

-------------------------

Leith | 2019-04-17 06:36:35 UTC | #87

Added animation for Running Forwards, and the key controlling it affects linear speed and animation speed in all cardinal directions. The implication is that running sideways (or backwards) means walking sideways (or backwards) more quickly
Added crouching, and crouch-jumping, and crouch-running, and crouch-run-jumping

You can mix the running, crouching, moving and jumping buttons as you wish - the result looks ok.

-------------------------

Leith | 2019-04-17 06:40:23 UTC | #89

HOW TO BLEND BASE ANIMATIONS ON A SINGLE LAYER

Basically you just need to set the Weights for animations that are Playing.
Calling Play will set the target weight for that animation to 1, which is bad, so we fix it by calling SetWeight, and we're gold.

[code]
               else if(ctrlsDir==Vector3::RIGHT+Vector3::BACK)
               {
                    /// Ensure our animations are playing, and set the animation speed
                    animCtrl->Play(Animations_[Animations_Player::WalkBackward].Name, 0, true, 0.4f);
                    animCtrl->SetSpeed(Animations_[Animations_Player::WalkBackward].Name,MOVE_SPEED);

                    animCtrl->Play(Animations_[Animations_Player::StrafeRight].Name, 0, true, 0.4f);
                    animCtrl->SetSpeed(Animations_[Animations_Player::StrafeRight].Name,MOVE_SPEED);

                    if(isCrouching){
                        /// Set weights for blending three animations
                        animCtrl->SetWeight(Animations_[Animations_Player::WalkBackward].Name, 0.2f);
                        animCtrl->SetWeight(Animations_[Animations_Player::StrafeRight].Name, 0.2f);
                        animCtrl->SetWeight(Animations_[Animations_Player::CrouchIdle].Name, 0.6f);
                    }else{
                        /// Set weights for blending two animations
                        animCtrl->SetWeight(Animations_[Animations_Player::WalkBackward].Name, 0.5f);
                        animCtrl->SetWeight(Animations_[Animations_Player::StrafeRight].Name, 0.5f);
                    }
              }
[/code]

And here is a convoluted example of the level of control you get:
[code]
            /// Character is Idle (and possibly crouching)
            if (dir.LengthSquared() == 0.0f)
            {
                /// Stop all locomotion animations
                if(animCtrl->IsPlaying(Animations_[Animations_Player::WalkForward].Name))
                    animCtrl->Stop(Animations_[Animations_Player::WalkForward].Name,0.4f);
                if(animCtrl->IsPlaying(Animations_[Animations_Player::WalkBackward].Name))
                    animCtrl->Stop(Animations_[Animations_Player::WalkBackward].Name,0.4f);
                if(animCtrl->IsPlaying(Animations_[Animations_Player::StrafeLeft].Name))
                    animCtrl->Stop(Animations_[Animations_Player::StrafeLeft].Name,0.4f);
                if(animCtrl->IsPlaying(Animations_[Animations_Player::StrafeRight].Name))
                    animCtrl->Stop(Animations_[Animations_Player::StrafeRight].Name,0.4f);

                /// Play an idle animation
                if(isCrouching)
                    animCtrl->Play(Animations_[Animations_Player::CrouchIdle].Name, 0, true, 0.4f);
                else
                     animCtrl->Play(Animations_[Animations_Player::Idle].Name, 0, true, 0.4f);
            }
[/code]

-------------------------

Leith | 2019-04-18 06:16:56 UTC | #90

I've added all four Running animations, and dealt with blending them for diagonal movement. Looks cool :slight_smile:

I noticed something strange in my blending of diagonal walk animations today which is worth mentioning.
When blending the Forwards animation with Left or Right animation, the result looks fine.
But when we blend Backwards with Left or Right, suddenly the Hips look like they are oriented incorrectly for walking backwards!!
I solved the issue for backward diagonal movement by swapping the Left and Right animations, and setting their Speed negatively. This produced a much more correct result for blending backwards animation with sideways animation.
[EDIT}
The same thing was true for Running animations - for backward diagonal movement, I again switched the left animation for right, and negated the speed (to make it play that animation in reverse).
I found this to be very counter-intuitive, at first I could not figure out why this had worked!
[code]
               else if(ctrlsDir==Vector3::RIGHT+Vector3::BACK)
               {

                    if(isRunning){
                        /// Ensure our animations are playing, and set the animation speeds
                        animCtrl->Play(Animations_[Animations_Player::RunBackward].Name, 0, true, 0.4f);
                        /// Although we wish to move right, we really wish to face left.
                        /// We'll play the left animation, in reverse.
                        animCtrl->Play(Animations_[Animations_Player::RunLeft].Name, 0, true, 0.4f);
                        animCtrl->SetSpeed(Animations_[Animations_Player::RunLeft].Name, -1);
                        if(isCrouching){
                            /// Set weights for blending three animations
                            animCtrl->SetWeight(Animations_[Animations_Player::RunBackward].Name, 0.2f);
                            animCtrl->SetWeight(Animations_[Animations_Player::RunLeft].Name, 0.2f);
                            animCtrl->SetWeight(Animations_[Animations_Player::CrouchIdle].Name, 0.6f);
                        }else{
                            /// Set weights for blending two animations
                            animCtrl->SetWeight(Animations_[Animations_Player::RunBackward].Name, 0.5f);
                            animCtrl->SetWeight(Animations_[Animations_Player::RunLeft].Name, 0.5f);
                        }
                    }
[/code]

To move forwards, and to the left, we just mix forwards and left. Very simple.
But to move backwards, and to the right, we need to mix backwards, and "minus left" !!!...
Although we wish to move to the right, since we are also moving backwards, we need the hips in the general orientation for walking left, but we want the footfalls to occur in reverse.
The result is far more natural looking for backwards locomotions than just blindly mixing the animations for the cardinal directions.



I also added support for Weapon Attachments - the character can pick up (from the game environment) nearby weapons that the character can wield, the character can ready and unready any weapons they possess, but currently only one at a time can be wielded, and no support for two handed ik. So far, there's only one weapon implemented - a teapot :slight_smile:

Information for instantiating weapon attachments is declared in a custom xml file which contains a bunch of per-character tweakables.
[code]
    <Comment> Weapons that this character can wield </Comment>
    <Weapon Name="Models/TeaPot.mdl" Material="Materials/Stone.xml" AttachTo="RightHand" LocalPos="-25 0 0" LocalRot="-90 -90 0" Scale=".25 .25 .25" Uses="20" Damage="5" />
    <Weapon Name="Models/Sword.mdl" Material="Models/Weapons/Sword/Materials/Sword.xml" AttachTo="RightHand" LocalPos="-25 0 0" LocalRot="-90 -90 0" Scale="1 1 1" Uses="20" Damage="12" />
[/code]

-------------------------

Leith | 2019-04-18 06:44:46 UTC | #91

Just being able to Crouch is good. Crouch-Jump and Run-Crouch-Jump are also good.

But being able to Crouch is not free.
The Bullet kinematic controller does not provide it.
The Urho3D dynamic controller does not provide it.
Both are just demo code, designed to offer a starting point to a proper controller.

I am getting very close to a proper controller, but getting sidetracked by the need to attack my enemy!
I have an enemy, I now have a weapon, I need an attack animation, at least one :(

-------------------------

Leith | 2019-04-29 09:47:47 UTC | #92

I'm experimenting with root motions.
I am inspired by rku's proposed patch to Urho3D's animation framework https://discourse.urho3d.io/t/root-motion-patch/4464

The code is inspiring, but misguided - it gives us a way to obtain the root motions from each animationstate, but I wanted the final, blended root motion resulting from our usual animation blending.

Instead of poisoning the Urho3D codebase, I decided to try to apply the same code logic to my frame update - but instead of targetting individual AnimationStates, I chose to target their blended result at the root bone of the animations (which is currently always the Hips). I let AnimationController apply the root motion to the root bone, and then I step in and correct the root bone, transferring the motion channels I want to my preferred target node. I do so using frame delta transforms, because I don't want to deal with moving things when the rootmotion animation ends, because I plan to blend more than one root motion and don't expect them to be synchronized.

In the Update method, I sample the current localspace transform of the Hips.
In DrawableUpdateCompleted, I sample the new (animated) localspace transform of the Hips.
I choose LocalSpace because I am only interested in motion resulting from animation - not from physics or anything else.
I compute the (localspace) delta-transform as : DeltaXForm = OldXForm.Inverse() * NewXForm
We note the resulting transform is relative to the Hips.

Since AnimationController is updated very late in the frame, I don't do anything with the resulting delta transform yet. Instead I wait until the next frame.

Back to the Update Method - just prior to recording the current localspace of Hips, I apply the delta-transform of the previous frame... I need to move the Hips localspace backwards by DeltaXForm, and I need to transform the character root node localspace forwards by DeltaXForm.

-------------------------

QBkGames | 2019-05-01 06:12:56 UTC | #93

I've implemented a basic crouch by simply scaling the node on the Y-axis by half.
Not the best but works OK.
After looking at the Physx docs and samples, they do it the same way.

-------------------------

Leith | 2019-05-01 06:14:44 UTC | #94

I did the same thing at first!
Then you want to add some interpolation, to smooth the transition from capsule height to height/2
Then you realize you can just measure the AABB of the animated model...
:)

-------------------------

Leith | 2019-05-08 04:50:59 UTC | #95

Today, I got Root Motion working to my satisfaction! Well, at least on level ground :stuck_out_tongue:
No more problems with "foot-slipping" during animations, so no fancy foot-solver!

Character animations may attempt to animate a target root bone (for me, it's the Hips).

I wanted to transfer the animated XZ (LocalSpace) translation of the Hips to my character's true (WorldSpace) root node, such that the character root node's worldspace position reflects that of the rootmotion-animated hips ... 

 This turned out to be both trickier than it sounds, as well as turning out to be almost that simple. 
My solution does not involve editing Urho3D engine sourcecode, I was able to solve the problem within Urho's frame update scheme.

Initially, I tried to use basis-inversion of animated Local transforms to compute inter-frame deltas, but (possibly due to my use of Scale on my model) I found the results were horribly inaccurate, so I abandoned that pathway.

Next I tried computing my deltas in WorldSpace, and quickly noticed another rapidly-compounding error term. It turned out that my method for measuring worldspace deltas was flawed, because my frame of reference was moving! I needed a moving point of reference :)

I realized that the compounding error term could be cancelled easily, by summing the translation delta vectors from previous frames during root motion, and subtracting that sum from the "apparent" worldspace position of the hips when measuring the next delta.

The result was perfect - except for the final frame of root motion animation, which was handled by zeroing the localspace XZ translation on the hips due to unwanted animation in the final frame, and returning early from the root motion handler (so not applying root motion in the final frame).

I'll probably upload a short video to show the results.

The code is still quite horrible... it needs a refactor to make it more generically useful, but the technique works regardless of armature scaling, and should work for multiple blended root motion animations, since the delta-sum is a measure of the combined effect of all animations on the hips (or other preferred target bone) as measured over time.
At the very least, it will work for blending rootmotion animations whose play length has been synchronized (either through changing the animation speeds or total keyframe lengths), and blending rootmotion animations with in-place animations should "just work" without any synching needed.

Next, I need to think about how best to combine root motion translation with physics - we want the character's root motion to be applied to the physics hull, but we also want collisions on the physics hull to determine the final position of the character. The problem is that animation, and root motion handling, happens after physics has updated, so there's a bit of a chicken and egg problem to work out.

-------------------------

Leith | 2019-05-08 06:38:05 UTC | #96

Without discussing the "root motion sum" issue, I'm generally applying root motion within the Urho3D frame update scheme as follows:

[quote]
Update - At start of Frame, note the worldspace position of the hips. This will act as a basis for measuring world delta due to animation later in the same frame.

FixedUpdate - Prior to physics update, move the physics hull to suit the character root node's worldspace position. We want the physics hull to follow our character around!

PhysicsPostStep - After physics update, move the character root node to suit the physics hull (apply collision responses to character). We want the character to respond to uneven terrain!

PostUpdate - Correct the camera view

SceneDrawableUpdateFinished - After animation update, and prior to rendering, apply desired root motion deltas to character root node, and Eliminate same from the Hips local transform. We want to transfer (some or all channels of) root motion from animation target root bone to character root node.
[/quote]

I still need to experiment with blending rootmotions (especially non-synchronized ones) but I feel confident that I can track the weighted contributions of individual rootmotion animations if I find that to be desirable.

Hey, at least physics is working in harmony with root motion! I'm pretty happy with that.

-------------------------

Leith | 2019-05-08 14:52:15 UTC | #97

Now uploading a short video that shows some root motion in action, along with rotating the character mid-way through such a motion. The final attack animation in this video has no root-motion handling applied, so we can see the character step slightly outside the physics hull.
Please excuse my physics debugdrawing, and yes this character still interacts correctly with complex environments, I simply didn't show that here.

<https://www.dropbox.com/s/1r3z9xdi0293ecv/WIP_Latest.mp4?dl=0>

-------------------------

Leith | 2019-05-09 01:25:23 UTC | #98

A brief discussion of measuring (worldspace) animation delta transforms in a moving frame of reference.

Basically, the animated local transforms that Urho's animation system writes to our armature nodes are "absolute local" values. For example, in a walk cycle with root motion, we might see that Hips Local Position Z is moving from 0 to 150 (extreme example, for clarity).
Since the Hips node is a grandchild of the character's root node, any changes made to character root transform will also affect the worldspace position of the hips - but the hips are not aware of this... if we want to constrain our character root node to follow the hips, then we need to realize that each time we apply a correction to the root node transform, it will have a compounding effect on the "apparent" world position of the hips (and therefore the entire rendered model).
The animation keyframes for the Hips are not aware that you are moving the root node, and without further correction, the result looks like the model is rapidly accelerating away from the root node.

There are probably a lot of different ways to handle this situation - I tried several before settling on using a simple yet robust vector sum of translation deltas as a compensation value to counteract the compound error term.

-------------------------

Leith | 2019-05-09 08:52:17 UTC | #99

The logic I use for driving and switching character animations is currently completely hardcoded. Although efficiently structured, it is a big mess of conditional logic. I note that the number of branches in the conditional logic is some orders greater than the reduced set of character behaviour states that it encodes.
[code]
    enum CharacterState_Player{
        Idle,
        Walking,
        Running,
        Attacking,
        Something
    };
[/code]

I am strongly tempted to replace it with a state machine which can be data-driven, and whose state transitions are guarded by soft-programmable conditional logic. What I'm describing would represent something like Unity's Animator component, although I would be proposing to embed the FSM within my Character class, such that it effectively drives the state of Urho's AnimationController.
It's not a trivial undertaking given that the Character class still needs lots of polish, and the added complexity is something I don't actually need right at this very moment, but I believe my existing code would run a lot more efficiently using a state machine pattern than it does now.

I'm now toying with some draft sourcecode, without compiling it or trying to design what I want in my head, just to get a "feel" for what I am trying to achieve and how I intend to get there. I may never use the code - I may never create a design document for this feature - but I will experiment "on a napkin" to see how I feel about how well this mechanism fits in with the concept of my game, and what kinds of pros and cons are associated with it.

-------------------------

Leith | 2019-05-15 04:53:34 UTC | #100

Today I spent some time working on the main menu UI.
I really dislike doing gui stuff, but it's necessary, so I do it.

Implementing the UI stuff today has given me a huge sense of relief about my early adoption of a game state machine implementation.

[code]
        /// MAIN MENU STATE: User has clicked on a UI Element (such as a button)
        void GameMainMenuState::OnUIElementClicked(StringHash eventType, VariantMap& eventData){

            UIElement* clicked = static_cast<UIElement*>(eventData[UIMouseClick::P_ELEMENT].GetPtr());

            if (clicked == PlayButton_)
            {
                /// Switch to LOADING state, and begin performing a scene change
                changeGameState(GAME_STATE_LOADING);
                ((GameState::GameLoadingState*)GameStateManager::getState(GAME_STATE_LOADING))->changeScene("gamescene.xml");

            }else if(clicked == QuitButton_)
                /// Send request for application to quit
                SendEvent(E_EXITREQUESTED);
        }
[/code]

I was reminded yet again about the trap of 2D pixel coordinates versus application window dimensions - the resizing issue. In my own engines, I usually use NDC coordinates to specify 2D window coordinates, and always offer a method to convert between pixel coordinates and NDC coords - I'm not up to date on how to deal with window resizing, could anyone elighten me?

-------------------------

Leith | 2019-05-15 05:57:24 UTC | #101

My skills as a graphic layout artist are negligable, however I do functionality very well.
![Screenshot%20from%202019-05-15%2015-26-57|690x403](upload://bKqyJlQNf882EijXf1N1IYzCBUB.png)

But to be fair: the Stanford Teapot Combo Attack is hilarious, and I may keep it in the game.

-------------------------

Leith | 2019-05-15 07:05:16 UTC | #102

A thought experiment

[quote]
        Describes the character's key behavioural states and conditions for changing state
        Conditions test the values of certain Named Attributes of the Character class
        These values are maintained by the Character::Update method
    </Comment>
    <State Name="Idle">
        <Edge Name="Walking">
            <Condition="Speed > 0" />
            <Condition="isTouchingGround == true" />
            <Condition="isJumping == false" />
        </Edge>
    </State>
    <State Name="Walking">
        <Edge Name="Idle">
            <Condition="Speed == 0" />
            <Condition="isTouchingGround == true" />
            <Condition="isJumping == false" />
        </Edge>
    </State>
    <State Name="Falling">
        <Edge Name="Idle">
            <Condition="isTouchingGround == true" />
            <Condition="isJumping == false" />
        </Edge>
    </State>
[/quote]

I am aware that this is logically incomplete - it is a "thought experiment", and nothing more at this stage.

-------------------------

Leith | 2019-05-16 05:38:32 UTC | #103

Today I experimented with "Dark Lighting" (aka Subtractive Lighting).
I wanted to add "local gloom" to my game scene.
I achieved this by using a negative value for Brightness on a Point Light (no shadows), in the presence of a general Directional Light (with shadows) plus a bit of ambient light.
This turned out pretty well, although I did notice one strange side-effect resulting from the way Urho's lighting equation is implemented,,,
If we give our darklight a colour, the result will appear to be the inverse of that colour.
For example, a "red" darklight gives surfaces a "blue/green" appearance.
Just thought it was interesting :slight_smile:
[EDIT]
There's also a subtle artefact created in the Shadows - dark lighting, with shadows disabled, darkens shadows from light that have shadows enabled,.. but only where the dark light has effect! IE, a dark light does not darken a volume, it literally casts negative light, which falls on surfaces similarly to regular light! This was not exactly what I was after, lol ![shadowartefact_darklight|690x403](upload://5j6XtXxNRM7GQQ66HRRhOm9mEYY.jpeg) 

I also added some quick code to test for character player hitting enemy with a weapon - this was just an instantaneous sphere test on the model's right hand. It works, but it's hardly good enough.
I guess I'll add a proper physics hull to the weapon instead, and use collision detection instead of collision polling, I was just in a hurry to get a result. I want to move on to collision responses as quickly as possible, I intend to use additive blending to add "twitches" to show hit responses. We'll see how that works out before looking at alternatives.

Incase anyone cares, the white cylinder is the "physics outer hull", the blue one indicates where the Hips (aka Pelvis) bone is positioned/oriented, and the purple one indicates where I think the character's "true root node' is positioned/oriented. Just visual tools I use during development to help confirm things are where I think they are, and oriented the way I think they should be, with respect to physics versus animation.

-------------------------

