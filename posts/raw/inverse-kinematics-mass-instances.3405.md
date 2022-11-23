slapin | 2017-08-01 18:00:29 UTC | #1

@weitjong please do not lock this even if you find similar topic

@TheComet this topic is mainly addressed to you, but I think it should be interesting to others.

As work on bug  #1957 looks like done by @TheComet and IK should be usable on mass instances.

I tried to test it today, but I could not make it work in my case of 100 NPCs.

I'm probably stupid, but I see no effect, but lets clarify proper setup procedure. I know IK is not ready to run Makehuman characters, but anyway I want to see some effect over there.

So what I do: I create IKEffector on foot.L and foot.R
I set chain length to 4 for each.
I add IKSolver
I disable auto-solving
 I subscribe to events
I call Solve() from event

```AngelScript
void Init()
...
        Node@ leftFoot  = node.GetChild("foot.L", true);
        Node@ rightFoot = node.GetChild("foot.R", true);
        IKEffector@ leftEffector  = leftFoot.CreateComponent("IKEffector");
        leftEffector.chainLength = 4;
        IKEffector@ rightEffector = rightFoot.CreateComponent("IKEffector");
        rightEffector.chainLength = 4;
        Node@ spine = node.GetChild("spine02", true);
        IKSolver@ solver = spine.CreateComponent("IKSolver");
        solver.algorithm = IKAlgorithm::FABRIK;
        solver.SetFeature(IKFeature::AUTO_SOLVE, false);
        SubscribeToEvent("SceneDrawableUpdateFinished", "HandleSceneDrawableUpdateFinished");
...
}
void HandleSceneDrawableUpdateFinished(StringHash eventType, VariantMap& eventData)
{
    Node@ rfoot = node.GetChild("foot.R", true);
    Node@ spine = node.GetChild("spine02", true);
    IKSolver@ solver = spine.GetComponent("IKSolver");
    IKEffector@ re = rfoot.GetComponent("IKEffector");
    re.targetPosition = Vector3(0, -1, 0);
    solver.SetFeature(IKFeature::UPDATE_ORIGINAL_POSE, true);
    solver.Solve();
}
```

Do I miss anything?

-------------------------

slapin | 2017-08-01 18:54:39 UTC | #2

The test blend file is available here: http://ossfans.org/man-suit-hidden.blend.gz

-------------------------

slapin | 2017-08-01 19:59:05 UTC | #3

OK, I found what needs to be done (probably needed to be documented) - IK solver should be put
close to chains, if IK do not work it is better to put solver very close to a chain.

-------------------------

TheComet | 2017-08-01 20:06:10 UTC | #4

I took a look at your .blend file, the problem is that you are attaching ```IKSolver``` to a bone that is not a parent of the feet bones (```spine02``` is not a parent of ```Foot.L``` or ```Foot.R```). The solver will only regard nodes that are "below" it in a tree.

The first bone in your model that is a parent of the two effector bones is the bone called ```root``` and you should be creating ```IKSolver``` as a component of this bone.

```cpp
Node@ root = node.GetChild("root", true);
IKSolver@ solver = root.CreateComponent("IKSolver");
```

-------------------------

slapin | 2017-08-01 20:18:36 UTC | #5

Thanks for answer, I got from here. But there are some bad news.

To me it looks like IK sanity depends on root bone rotation, which provides weird effects.

https://youtu.be/Ca4TuZpX7A4

I do not update effector targets here (no difference if I do though), just run Solve().

Any pointers? (same skeleton).
The player character do not have IK, only NPCs.

p.s.
Very nice to hear from you!!!

-------------------------

TheComet | 2017-08-01 20:30:31 UTC | #6

Are you calling Solve() on every IKSolver component? I'd need to see your update code, but to me it looks like you're only calling Solve() for your player.

-------------------------

slapin | 2017-08-01 20:35:54 UTC | #7

Player have no IK at all.

This is for NPC - (every NPC).

```AngelScript
    void Init()
    {
...
        Node@ leftFoot  = node.GetChild("foot.L", true);
        Node@ rightFoot = node.GetChild("foot.R", true);
        IKEffector@ leftEffector  = leftFoot.CreateComponent("IKEffector");
        leftEffector.chainLength = 3;
        IKEffector@ rightEffector = rightFoot.CreateComponent("IKEffector");
        rightEffector.chainLength = 3;
        Node@ spine = node.GetChild("root", true);
        solver = spine.CreateComponent("IKSolver");
        solver.algorithm = IKAlgorithm::FABRIK;
        solver.SetFeature(IKFeature::AUTO_SOLVE, false);
        
        SubscribeToEvent("SceneDrawableUpdateFinished", "HandleSceneDrawableUpdateFinished");
}
    void HandleSceneDrawableUpdateFinished(StringHash eventType, VariantMap& eventData)
    {
        Node@ rfoot = node.GetChild("foot.R", true);
        Node@ lfoot = node.GetChild("foot.L", true);
        IKEffector@ re = rfoot.GetComponent("IKEffector");
        IKEffector@ le = lfoot.GetComponent("IKEffector");
        solver.SetFeature(IKFeature::UPDATE_ORIGINAL_POSE, true);
        solver.Solve();
    }
```

-------------------------

slapin | 2017-08-01 20:38:04 UTC | #8

If I run without IK, NPCs look normal (legs are where they are supposed to be).

-------------------------

TheComet | 2017-08-01 20:43:31 UTC | #9

Are your NPCs animated?

-------------------------

slapin | 2017-08-01 20:54:24 UTC | #10

As you could notice from video, yes. I could upload video w/o IK enabed for you to see...

https://youtu.be/4q72eSFKFiA

Here I run with IK enabled but I do not run Solve, so animations work, but no IK correction functions.

-------------------------

slapin | 2017-08-01 20:54:58 UTC | #11

So you can see how it was looking without Solve() running.

-------------------------

slapin | 2017-08-01 20:59:54 UTC | #12

Sorry for video quality - Urho can't be recorded properly under Linux (at least with nvidia driver).

-------------------------

TheComet | 2019-05-23 13:20:01 UTC | #13

This is really weird. I was actually able to reproduce exactly the behaviour you were having, where the feet of all of the NPCs are pointing to 0,0,0. I undid changes (which fixed it), redid everything again, and then it just started working correctly.

There is certainly a bug here that causes all feet to point to 0,0,0 but I don't think we're sure yet what causes it.

I modified 45_InverseKinematics so it would spawn 25 Jacks instead of just 1. Here, have a play around with it.
https://pastebin.com/zvqxBd9K

Multiple solvers appear to work fine.

![1|661x500](upload://1J9VuaBMIZ8kfgV6UxzqpwX3h99.jpg)

-------------------------

slapin | 2017-08-01 21:39:00 UTC | #14

Do you have plans to make actual Makehuman skeleton (the same like with that file) supported?
This requies bone skipping. I will wait until Makehuman character is supported, so I could integrate IK in my game.
At least this offsetting of legs should be resolved somehow...

Thank you for your work!

-------------------------

slapin | 2017-08-01 23:14:08 UTC | #15

Also another question - will it be possible to run feet IK + arm IK at the same time?
Are several solvers supported for the same skeleton?

-------------------------

slapin | 2017-08-01 23:33:41 UTC | #16

Yes, this looks like all targets point to (0, 0, 0) regardless of what I set them to, which is strange,
and this reproduces for me always, I can't get correct behavior...

-------------------------

slapin | 2017-08-01 23:38:42 UTC | #17

I also see this warning when I set effectors then solver:
```
[Wed Aug  2 02:35:35 2017] INFO: [IK] Warning: Tried iterating the tree, but no tree was set

```

-------------------------

slapin | 2017-08-01 23:53:53 UTC | #18

The code, which produce the warning is the following - 
```AngelScript
        IKEffector@ leftEffector  = leftFoot.CreateComponent("IKEffector");
        leftEffector.chainLength = 2;
        IKEffector@ rightEffector = rightFoot.CreateComponent("IKEffector");
        rightEffector.chainLength = 2;
        Node@ spine = node.GetChild("root", true);
        solver = spine.CreateComponent("IKSolver");
```
Warning is produced by last line.

Also I tried setting different chain length and tried TWO_BONE algorithm, there is
no difference at all.

-------------------------

slapin | 2017-08-02 00:00:36 UTC | #19

Yes, so what I see is targetPosition setting is complely ignored by IK components which results all targets being at (0, 0, 0). Probably I will try to debug this on weekend unless you see what is going on before that.

-------------------------

Mike | 2017-08-02 06:44:42 UTC | #20

At first glance:
- setting targetPosition to Vector3(0, -1, 0) is a request for straight legs (for example, if floor is at 0, you are trying to reach 1 unit below floor level)
- solver.SetFeature(IKFeature::UPDATE_ORIGINAL_POSE, true); is set in HandleSceneDrawableUpdateFinished, should be set only once in Init()
- your chain length seems to vary between 3 and 4

-------------------------

TheComet | 2019-05-23 13:20:01 UTC | #22

[quote="slapin, post:14, topic:3405, full:true"]
Do you have plans to make actual Makehuman skeleton (the same like with that file) supported?

This requies bone skipping. I will wait until Makehuman character is supported, so I could integrate IK in my game.

At least this offsetting of legs should be resolved somehow…
[/quote]

It's definitely a feature worth considering. It will require some non-trivial changes to the IK library, specifically in how the chain tree is built and how the segment lengths are calculated.

I think you'll have a better time adjusting the skeleton so it has two bones rather than trying to force the IK library into special cases where it occasionally skips bones and stuff.

You can add two dummy bones to the skeleton like so

![1|310x500](upload://hpvcCcBMA5m8jeiACByHpluwTP.png)

Attach the IKEffectors to the end of these hidden bones, Solve(), then copy the rotations to the actual bones that matter.

[quote="slapin, post:15, topic:3405, full:true"]
Also another question - will it be possible to run feet IK + arm IK at the same time?

Are several solvers supported for the same skeleton?
[/quote]

Sure, just add more IKEffector components. If there is an IKSolver higher up in the tree then it will take care of solving.

You can add as many IKSolver components to a skeleton as you want, as long as they each have their own subtree. You can technically have conflicting solvers (e.g. if you attach an IKSolver to a node that is a child of another IKSolver, then those two solvers will fight to solve the same chains). Sometimes this can produce interesting results (like your skeleton starts spazzing out) but it isn't recommended.

Also: The advice in the samples stating that you should position the IKSolver as close as possible to the end effectors isn't really valid anymore. The chains are optimized when the tree is built internally so solving is fast. It doesn't matter where you attach the IKSolver now.

-------------------------

Mike | 2017-08-02 09:51:55 UTC | #23

As multi solver is supported, then my code is certainly at fault. I've tried to add a one bone IK for the head in addition to the 2 bone IK in the sample and it segfaults (code inserted at the end of CreateScene):

    // Head solver
	Node@ target = scene_.CreateChild("Target");
	target.position = Vector3(-1.0f, 1.5f, 0.0f);

	Node@ neck = jackNode_.GetChild("Bip01_Head", true);
	Node@ head = jackNode_.GetChild("Bip01_HeadNub", true);
	IKEffector@ headEffector = head.CreateComponent("IKEffector");
	headEffector.chainLength = 1;
	headEffector.targetNode = target;

	IKSolver@ lookAtSolver = neck.CreateComponent("IKSolver");
	lookAtSolver.algorithm = ONE_BONE;
	lookAtSolver.SetFeature(AUTO_SOLVE, true);
	lookAtSolver.SetFeature(UPDATE_ORIGINAL_POSE, true);

Note: I've tested this piece of code successfully in isolation (without the legs solver).

-------------------------

slapin | 2017-08-02 10:40:55 UTC | #24

Well, having limitations of 256 bones per skeleton (or is it 255) adding extra dummy bones is a waste.
I'd better look for a way to skip bone in chain, which would look more effective resource usage...
Also additional rotation copying and having fake skeleton will produce runtime overhead and makes system clumsy and harder to use. I think something better is needed.

-------------------------

slapin | 2017-08-02 10:38:30 UTC | #25

as I understand from example code, the targetPosition is absolute setting.
With my skeleton usage setting targetPososition to any value seems to have no visible effect - both chains are always pointing to (0, 0, 0).

-------------------------

slapin | 2017-08-02 10:49:16 UTC | #26

Well, I think this applies well with constraint logic (as we discussed this before), can be made special constraint for FABRIK algorithm, for TWO_BONE I need to think how to do this better (probably will come up with idea on weekend).

-------------------------

TheComet | 2017-08-02 11:13:06 UTC | #27

@Mike 
Yeah, you've run into exactly the thing I mentioned with two solvers fighting over who's right. In the ```45_InverseKinematics``` example, the solver is attached to "Bip01_Spine". This node is a parent of "Bip01_Head" (to which you are also attaching a solver). So when you add the effectors, the first solver will build a chain for the legs and neck while the second solver also builds a chain for the neck.

Because the first solver is set to TWO_BONE, in debug mode, it will call abort() because the neck doesn't have two bones (only one). That's why it segfaults. You have two options to fix this: 1) Don't add the second solver and instead set the first solver's algorithm to FABRIK. Then it will solve for the neck and the legs, or 2) attach the first solver to a bone that is not a parent of the neck bone.

This seems like an oversight on my part. I think the more appropriate behaviour would be for the first solver to ignore the second solver's subtree.

I opened an issue here: https://github.com/urho3d/Urho3D/issues/2058

-------------------------

slapin | 2017-08-02 11:37:54 UTC | #28

I think that tree building algorithm should consider all solvers in single pass,
not buildin each individual tree separately. Otherwise there will be many usability problems
and non-obvious behavior.

-------------------------

Mike | 2017-08-02 11:40:31 UTC | #29

Many thanks for investigating this issue :racehorse:
Having 'intelligent' solvers would be awesome for performance and versatility.

-------------------------

George1 | 2017-08-03 03:23:50 UTC | #30

Have you try open broadcaster for video recording?

-------------------------

slapin | 2017-08-03 09:36:46 UTC | #31

I use just ffmpeg with x11grab. All other games are recorded perfectly with the same script.
Urho 1.6 IIRC was fine too. I did not dig too much about what changed.

-------------------------

cadaver | 2017-08-03 12:04:38 UTC | #32

On the subject of the ik library asserting, it would be preferable if the engine component using it would never use it in such manner. Or it's otherwise ensured the situation never happens. Because to the user / dev it will seem as "Urho3D crashing".

-------------------------

TheComet | 2017-08-03 12:38:49 UTC | #33

Good point, I didn't honor Urho3D's error handling guidelines. I'll include that in my PR for #2058.

-------------------------

slapin | 2017-08-05 13:03:15 UTC | #34

I think if bones are skipped we should assume that second bone of split limb is either not changes
its transformation while IK is active or have no transformation, that will be fair. If that is not a case
then we can add feature later on top of it. The split-limb case is quite common, I don't think there
will be problems with it.

-------------------------

