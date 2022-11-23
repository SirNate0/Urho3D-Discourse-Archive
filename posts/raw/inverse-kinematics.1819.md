TheComet | 2017-01-02 01:10:25 UTC | #1

There seems to be some general interest in the addition of an IK solver to Urho3D (such as this [url=http://discourse.urho3d.io/t/inverse-kinematics/879/1]feature request[/url] and of course the need for IK in my own project). I think it would be very cool for Urho3D to have this capability, so I have taken it upon myself to implement this feature request.

I'd like to clarify a few things before I make any major changes to Urho3D and would be happy if one of the core developers (I'm looking at you cadavar  :smiley:) could give me the "good to go" as well as some advice on some of these points.


[b]Concept[/b]

My current concept for approaching this are 3 new components:

[img]http://i.imgur.com/vQHOeCU.png[/img]

[b]IKSolver[/b] is attached to the root scene node and - as the name implies - is responsible for solving all IK constraints. I plan on implementing the Jacobian Inverse method and the Jacobian Moore?Penrose method for starters, but will probably also look at implementing a more robust algorithm in the future.

[b]IKEffector[/b] can be attached to any node in the scene and marks that node as the beginning of an IK chain. The effector has the methods SetTarget() for controlling the target location of the node and SetChainLength() to control how many parent nodes are affected.

[b]IKConstraint[/b] is attached to nodes part of the IK chain and is used to "fine tune" the behaviour of each node (things such as the "stiffness" and scale factor).


[b]Questions[/b]

[b]1) When to apply IK[/b]
The IK solver is capable of solving an entire scene graph in one pass, so it would make sense to have it kick in only once when needed -- whenever a node part of any IK chain becomes dirty. As I see it, this should happen after animation states have been applied, meaning in E_SCENEDRAWABLEUPDATEFINISHED. The problem is I can't just hijack that event for IK because what if the user wants to add their own bone modifications in addition to IK?

I could insert a new event called something like E_INVERSEKINEMATICUPDATE which is sent just before E_SCENEDRAWABLEUPDATEFINISHED. This begs the question: Do we even need an IK update event? Is this the way I should go, or is there a better way I can insert myself into the engine?

[b]2) Build system[/b]
Should I add a CMake option URHO3D_IK to include/exclude the IK solver, or should it be something that is always available?

That's all of the questions I have for now. I'll post updates in this thread as this project evolves. You can test my progress by checking out the branch InverseKinematics from here: [url]https://github.com/thecomet93/urho3d/tree/InverseKinematics[/url] (currently there's not much IK functionality).

-------------------------

1vanK | 2017-01-02 01:10:26 UTC | #2

[topic1040.html](http://discourse.urho3d.io/t/solved-ik-foot-placement/1010/1)
[topic1273.html](http://discourse.urho3d.io/t/unity-ikcontrol-script/1229/1)

-------------------------

TheComet | 2017-01-02 01:12:44 UTC | #3

I've hardly had the time to work on this (uni, exams), but I haven't given up on this yet!

Below you can see screenshots of before and after the first iteration of FABRIK, the inverse kinematic algorithm I chose to implement. In this case, the arm consists of 3 rigid joints. The end effector is trying to reach a target located on the right (out of bounds).

[img]http://i.imgur.com/85rTLa0.png[/img]

[img]http://i.imgur.com/ms34I0y.png[/img]

The neat thing about FABRIK as opposed to, say, jacobian based methods, is it requires vastly less iterations to reach a target, a single iteration requires less computing time, and it always converges (i.e. no singularities).

-------------------------

Mike | 2017-01-02 01:12:45 UTC | #4

I also think that FABRIK is the way to go, as most of the things I've experimented with gave very unrealistic behavior.
Also one advantage of FABRIK is that it splits the tasks instead of handling everything blindly.
Keep it up  :stuck_out_tongue:

-------------------------

xalinou | 2017-01-02 01:12:45 UTC | #5

[img]http://vignette2.wikia.nocookie.net/walkingdead/images/3/3f/Shut-up-and-take-my-money.jpg/revision/latest/scale-to-width-down/640?cb=20140829235648[/img]

-------------------------

TheComet | 2017-01-02 01:12:45 UTC | #6

Today I implemented initial pose restoring, which allowed me to finally run the algorithm in real-time. Here's a video.

[video]https://www.youtube.com/watch?v=POamRQtPI6c[/video]

I think you can see for yourself why FABRIK is superior. Just 10 iterations and the result is almost perfect. Jacobian based methods will often times require up to 1000 iterations to achieve the same tolerance.

Current issues:
 * Removing IKEffector from a node doesn't update initial pose data
 * Negative maxIteration

Todo:
 * Chain objects need to share the same Vector3 objects for base/effector positions to make solving for multiple chains easier.
 * Apply angles from chain objects back to scene node (currently only translations are applied)
 * Add support for enabling/disabling pose restoring -> will allow support for animations as well as just scene node IK
 * Add support for manually updating initial pose.
 * Apply bullet constraints
 * Optimise

-------------------------

hdunderscore | 2017-01-02 01:12:45 UTC | #7

You are making exciting progress, great work !

-------------------------

Mike | 2017-01-02 01:12:45 UTC | #8

Well done  :wink:

-------------------------

Modanung | 2017-01-02 01:12:46 UTC | #9

Really cool! :smiley:

-------------------------

TheComet | 2017-01-02 01:12:48 UTC | #10

The solver now supports multiple end effectors, as long as they share the same base node. Next up: Multiple end effectors with multiple intermediate base nodes. Have a video:

[video]https://www.youtube.com/watch?v=P8COz7dZO9Y[/video]

Current TODO list:
[code] *  - IKEffector doesn't save target node name when saving scene in editor
 *  - Initial pose is not saved when saving scene in editor. Instead, the
 *    solved state of the chain(s) are saved.
 *  - Target angle in addition to target position -> use weighted angles
 *    approach
 *  - Add an IKEffector weight parameter, so the user can specify
 *    (between [0..1]) how much influence the solved chains have.
 *  - Apply angles from chain objects back to scene nodes (currently only
 *    translations are applied).
 *  - Add support for enabling/disabling initial pose to support animated
 *    models as well as scene nodes.
 *  - Add support for manually updating initial pose.
 *  - Apply bullet constraints to joints.
 *  - Optimise.[/code]

-------------------------

cadaver | 2017-01-02 01:12:48 UTC | #11

Looks like excellent work.

-------------------------

namic | 2017-01-02 01:12:48 UTC | #12

So excited to use this!  :smiley: 

Is it possible to write a grounder with those effectors? e.g: [youtube.com/watch?v=9MiZiaJorws](https://www.youtube.com/watch?v=9MiZiaJorws)

Also, how are rotation limits setup?

-------------------------

TheComet | 2017-01-02 01:12:48 UTC | #13

Thanks guys!

[quote="namic"]Is it possible to write a grounder with those effectors? e.g: [youtube.com/watch?v=9MiZiaJorws](https://www.youtube.com/watch?v=9MiZiaJorws)

Also, how are rotation limits setup?[/quote]

Yes, grounders are the very reason why I started working on this in the first place. My dog model has 3 bones in each leg, so it was no longer a trivial trigonometric problem.

I'm thinking there are two possibilities to implement feet lifting off.
1) Be able to specify a weight from [0..1] on each effector to control how much influence the solved chain will have. This will allow you to specify 0 when the foot should lift off and 1 when the foot touches (and you'll also be able to blend between, which I think is an important feature).
2) It might be easier to just position the IK targets at the same position as the feet when they need to lift off of the ground. That way you won't need a weight parameter any more and the slight performance impact can be avoided.

Rotation limits are currently on the to-do list, along with pole targets. I will most likely try re-use the bullet constraint component for this purpose.

-------------------------

namic | 2017-01-02 01:12:50 UTC | #14

I'm dying to see the integration of this with ragdolls and animation!  :smiley:  :smiley:  :smiley:  :smiley:  :smiley:

-------------------------

Lumak | 2017-01-02 01:12:53 UTC | #15

I like what you're doing with this. Keep it up!

-------------------------

TheComet | 2017-01-02 01:13:01 UTC | #16

The solver now supports arbitrary trees, so if you should feel so inclined, you can solve for something like this (although I wouldn't know why you'd want to):

[img]http://i.imgur.com/YI0Xepk.png[/img]

The point is the solver can handle anything you can throw at it.

Here is an in-editor screen shot of a two-effector one-subbase configuration:

[img]http://i.imgur.com/dxXLy9k.png[/img]

There is currently an issue with applying the solved angles back to the scene nodes correctly. I am working on fixing this.

[img]http://i.imgur.com/XFyGJQS.gif[/img]

-------------------------

Modanung | 2017-01-02 01:13:01 UTC | #17

[quote="TheComet"]The solver now supports arbitrary trees, so if you should feel so inclined, you can solve for something like this (although I wouldn't know why you'd want to)[/quote]
For [url=http://www.gamezone.com/downloads/on-a-rainy-day]On A Rainy Day[/url]-likes. :slight_smile:

-------------------------

sabotage3d | 2017-01-02 01:13:01 UTC | #18

That is really cool feature for procedural creatures like in spore.

-------------------------

George | 2017-01-02 01:15:20 UTC | #19

Hi,
This is the example to update the angle for forward kinematic. You would similarly applied it for every kinematic link on a chain.

Vector3 shoulderJoint = node_lArm->GetWorldPosition();
		Vector3 elbow = node_elbow->GetWorldPosition();
		Vector3 v1 = elbow - shoulderJoint;
		Vector3 v2 = target - shoulderJoint;
		v1.Normalize();
		v2.Normalize();
		Quaternion q;
		q.FromRotationTo(v1, v2);

		Quaternion q1 = node_lArm->GetWorldRotation();
		Quaternion q2 = Quaternion( node_lArm->GetParent()->GetWorldRotation().Inverse());

node_lArm->SetRotation(q2*q*q1);



-------
You could also reset the rotation before those calculation to avoid drifting of the twist angles on the links using node_lArm->SetRotation(Quaternion());

-------------------------

Eugene | 2017-01-02 01:15:23 UTC | #20

That looks great! Any updates?

-------------------------

TheComet | 2017-01-02 01:15:32 UTC | #21

Hi! I really [i]want[/i] to work on this but college is stopping me. :confused:

I do require IK in my game project though, so this will eventually be finished!

-------------------------

Eugene | 2017-01-02 01:15:33 UTC | #22

Glad to hear it.
Actually, I have the same situation with my code stuff, but without college.

-------------------------

TheComet | 2017-03-12 16:54:31 UTC | #23

"Yes teacher I have a question"

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/92dfc2acb4479824c0a8663b2ce7b00bf3853816.jpg" width="476" height="444">

Progress has been slow, but I'm letting you know I haven't stopped working on this yet. I've moved the solver code to a separate library which can be found here: https://github.com/thecomet93/ik

I'm currently working on calculating the correct segment angles. The current issue is that I'm calculating global angles for each node and not taking into account previous rotations.

-------------------------

TheComet | 2017-03-14 00:32:10 UTC | #24

Today I finally fixed calculating correct angles when comparing the solved tree to the original tree. As you can see in the following image, the solver is fine with multiple targets on arbitrary trees. The blue segments you see is the original tree (before solving) and the red segments show the solved tree.

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/59ffe6f0a03d8412688a4217f6754dce8b1d9936.png" width="670" height="500">

The next step now is to support target angles as well as target positions. It would allow rotating the hand correctly.

-------------------------

TheComet | 2017-03-15 00:55:39 UTC | #25

> So excited to use this!  :smiley:

> Is it possible to write a grounder with those effectors? e.g: [youtube.com/watch?v=9MiZiaJorws6](http://youtube.com/watch?v=9MiZiaJorws6)

As promised, here are weighted effectors, which will be useful in providing a smooth transition for grounders. You can specify how much influence an effector should have on the result, ranging from 0.0 to 1.0. I thought about this for a day before the incredibly simple solution struck me: I don't need to write any elaborate tree interpolation algorithms, I just lerp the effector between original position and target position using its weight and solve for the resulting target position.

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/0dfb6f54d76221ba8105bb9eb3032feebd46619c.gif" width="500" height="400">

-------------------------

TheComet | 2017-03-15 17:28:04 UTC | #26

Solver now works with animated characters:

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/a498777dc3a834d3aefd19aea937dffd27edf33c.gif'>

Current TODO:
    /*
     *  - Actually implement tolerance.
     *  - Target angle in addition to target position -> use weighted angles
     *    approach
     *  - Nlerp weighted effectors using total chain length + root node as axis
     *    of rotation (so arm moves in a circle, for example)
 *  - Fix rotation issue with shared sub-base nodes -> rotations need to be
 *    averaged.
 *  - Add support for manually updating initial pose.
 *  - Pole targets?
 *  - Support for "stretchiness" with min/max lengths.
 *  - Support for "stiffness" factor, describes how well a bone rotates.
 *  - Apply bullet constraints to joints.
 *  - Script bindings.
 *  - Optimise.
 *  - Profile.
 */

-------------------------

sabotage3d | 2017-03-15 21:13:38 UTC | #27

Looks really good. For inspiration I would look at Final IK: http://www.root-motion.com/final-ik.html.

-------------------------

TheComet | 2017-03-15 22:03:52 UTC | #28

I'll take a look!

The following shows transitioning with and without nlerp when changing the effector weight. This feature makes transitioning look more natural when the original and solved trees are far apart

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/b730623a4ad776ecbeeba3008eb63bee90cc634a.gif'>

-------------------------

sabotage3d | 2017-03-15 22:02:52 UTC | #29

We could even do FK/IK animation in the editor :)

-------------------------

smellymumbler | 2017-03-15 23:44:30 UTC | #30

That is so amazing! :heart_eyes:

-------------------------

yushli1 | 2017-03-16 02:22:50 UTC | #31

The cat animation looks really good inside the editor. 
Thank you for sharing it!

-------------------------

slapin | 2017-03-17 10:14:32 UTC | #32

Hi, all!

@TheComet, could you please provide compiling instructions?

Thanks!

-------------------------

TheComet | 2017-03-17 10:35:46 UTC | #33

@slapin I have made the proper Urho3D build system changes and am maintaining them in a fork. The easiest thing you can do is clone my fork. For linux, the process is as follows:

```
$ git clone git://github.com/thecomet93/Urho3D.git
$ git checkout InverseKinematics
# ik library is not yet part of Urho3D, so you have to clone it 
# into Source/ThirdParty
$ git clone git://github.com/thecomet93/ik.git Source/ThirdParty
# build as normal
$ mkdir build && cd build
$ cmake ..
$ make
```

If you have issues, feel free to contact me.

-------------------------

slapin | 2017-03-17 10:53:47 UTC | #34

Thanks, this works! Will try to figure out how to use from code.

-------------------------

TheComet | 2017-03-17 12:01:13 UTC | #35

I'd be happy to know what you think! I'm sorry it's not that well documented yet, that's still on my TODO list.

You have to create an IKSolver component and attach it to the model you want to solve for. Then you create IKEffector components and attach them to the bones you want to control. That should be enough to get you started.

These components are also available in the editor under Components->Inverse Kinematics

-------------------------

slapin | 2017-03-17 14:28:00 UTC | #36

When you plan to merge it into Urho? This looks well written to me.

-------------------------

slapin | 2017-03-17 14:29:50 UTC | #37

A small feature request - is it possible to do some special-case IK as part of library?
These should be very fast to compute and speed things up a lot.

-------------------------

TheComet | 2017-03-17 16:02:06 UTC | #38

I'm reluctant to say how much more time I need. Currently it feels like I should be done in about 2 more weeks. I'm still working on an acceptable algorithm for calculating target rotations. That's the last major feature I'll be adding. Then I'll write script bindings and write documentation, and fix some known bugs in the library.

-------------------------

slapin | 2017-03-17 17:05:38 UTC | #39

Thanks for your hard work! Just do in small steps and that will eventually be done.

-------------------------

TheComet | 2017-03-18 01:45:37 UTC | #40

Target rotations are implemented and can optionally be enabled:

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/faea235799b4b8ccc702888031bb656f1ea50d09.gif'>

It's possible to change the rotation weight and decay parameters on a per-effector basis (not shown). And, like everything else, the rotations are propagated correctly over arbitrary trees.

My current TODO list is:
```
 * TODO
 *  - Actually implement tolerance.
 *  - Fix rotation issue with shared sub-base nodes -> rotations need to be
 *    averaged.
 *  - Add support for manually updating initial pose.
 *  - Script bindings.
 *  - Optimise.
 *  - Profile.
 *  - Documentation.
 *
 * FUTURE
 *  - Support for "stretchiness" with min/max lengths.
 *  - Support for "stiffness" factor, describes how well a bone rotates.
 *  - Apply bullet constraints to joints.
```

-------------------------

TheComet | 2017-03-18 17:00:39 UTC | #41

Fixed an issue where nodes with multiple children did not calculate rotations correctly.

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/4e28d1811c1e48f0a845ac4b779e1e7bce5f6e10.png" width="675" height="398">

My TODO list is getting very small. It's mostly gruntwork from here on out. I'll be writing the script bindings now and submit my first pull request. I can work on constraints for future versions.
```
 * TODO
 *  - Add support for manually updating initial pose.
 *  - Script bindings.
 *  - Optimise.
 *  - Profile.
 *  - Documentation.
 *
 * FUTURE
 *  - Support for "stretchiness" with min/max lengths.
 *  - Support for "stiffness" factor, describes how well a bone rotates.
 *  - Apply bullet constraints to joints.
```

-------------------------

Mike | 2017-03-22 13:08:03 UTC | #42

I've just tested and it works great :grinning:

For target nodes, I think it would be better to use node ID instead of node name in the Editor, to match every other components (Constraint, Constraint2D, OffmeshConnection...) behavior (and to allow simply dragging the node in the target slot).

I'll do some more tests, and report feedback. Let me know if I can help in any way :wink:

-------------------------

smellymumbler | 2017-03-18 23:42:57 UTC | #43

You should setup a patreon so we can all donate for your amazing work. :)

-------------------------

TheComet | 2017-04-03 23:58:55 UTC | #44

I'm happy to report the first version has been merged into master! All features you've seen in this thread are now available.

https://github.com/urho3d/Urho3D/pull/1871

If you have questions, feature suggestions, or bug reports, I look forward to hearing from you. I will be actively maintaining this.

There is a new sample, `45_InverseKinematics`, that you can look at. Here's what it looks like:

<img src="http://i.imgur.com/OswlUDa.gif" width="350">

The next thing I will be working on is @1vanK's suggestion to add constraint support.

-------------------------

weitjong | 2017-04-04 02:09:52 UTC | #45

Congrats! The IK samples in C++, AngelScript, and Lua are also available in Web platform now. https://urho3d.github.io/samples/

-------------------------

TheComet | 2017-04-16 18:02:09 UTC | #46

The papers I've found on FABRIK aren't very clear on how constraints should be implemented. Sometimes they're even cryptic. Nevertheless, I think I've been making some progress.

My first attempt at implementing constraints failed. I first thought you could apply constraints to the entire tree every iteration, but as you can see, the algorithm no longer converges. (Here, I'm trying to force one of those joints to always be straight no matter what, but it seems he'd rather remain gay). 

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/0a4e474da16d1857b7c5697956f9c59ff7cc07e3.gif'>

I'm now working on my second attempt where constraints are applied per node as the tree is being iterated. The math is cumbersome as it involves computing joint rotations and transforming to and from local space.

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/406f50e0464dea5678feaa4f4dff821b681803e3.gif'>

It looks like this could work. I think I have to apply constraints during forwards iteration as well as during backwards iteration (right now it's only during backwards iteration). Calculating local joint angles is going to be a lot harder in forward iteration, I'm not yet sure how to tackle this.

The nature of the FABRIK algorithm makes constraint support inherently inefficient, because FABRIK has no need for joint angles and works entirely in global space. Joint constraints require joint angles in local space. There is an unfortunate performance penalty, which is fairly evident by just looking at the code.

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/935c44b0bb5044df01244f9e77180ac5ee601ba4.png'>

-------------------------

slapin | 2017-04-16 18:25:46 UTC | #47

Well, IK constraints were always different from normal contraints (look at how Blender handles IK).
I think you should make universal constraint matrix out of all constraints and apply just that.
That will be a bit more efficient in loop. The other approach is to not require constraints to be justified at all times,
just get to the point iteratively. Just my $.00002 :)

-------------------------

TheComet | 2017-04-16 19:47:27 UTC | #48

I don't think one giant constraint matrix is suitable in this situation. The constraints are being applied during iteration, meaning the tree is in a partial state of being solved. But if you want we can discuss it in more detail and I can explain the algorithm more closely to you.

I tried applying all constraints at once after iterating the tree every time, but it caused the algorithm to diverge.

-------------------------

slapin | 2017-04-16 20:07:21 UTC | #49

Well, I don't want to disturb you, I'm just passing by.  I just remember all these IK lectures telling that you either
solve constraint analytically (all at once) or use Jacobian matrix and solve numerically (iteratively solving
differential equation system).
But what I wanted to say is that constraints for IK in Blender are different from other constraints
and they work independently of constraint system. I think this is way to go. Also I think you'd want only
angular constraints at first.

Also, is it possible to use sparse chains in your IK system, i.e. I want the system to know about a set of bones,
but not touch others. I.E.
an arm consists of  bones AB-CD-E (fingers omitted). I want A and C to be moved by IK, others should
just rotate together with parents not touched by constraint. Will it work?

-------------------------

Mike | 2017-04-16 20:50:10 UTC | #50

There are some good resources here (which you may already checked):
[http://wiki.roblox.com/index.php?title=Inverse_kinematics](http://wiki.roblox.com/index.php?title=Inverse_kinematics)
[https://github.com/FedUni/caliko](https://github.com/FedUni/caliko) and [https://github.com/lo-th/fullik](https://github.com/lo-th/fullik) (with a demo [here](http://lo-th.github.io/fullik/))
However I didn't succeed in implementing them.

-------------------------

smellymumbler | 2017-04-19 14:28:09 UTC | #51

Is there an example on how to do aim offsets? Not only a look at constraint, but something like this: 

https://www.youtube.com/watch?v=rE4nE5tMdnI

-------------------------

TheComet | 2017-04-19 18:43:57 UTC | #53

Seems simple enough. He's created a number of predefined poses for the different angles the gun could be at and then he's blending between those poses when crossing a threshold (first part of the video).

Since you know the target direction, you can slide the gun around on an imaginary sphere depending on the direction, calculate the hand positions and rotations, and use IK to move the hands there.

I'm still working on constraints whenever I have free time, but this should be possible without them.

-------------------------

smellymumbler | 2017-04-19 23:30:38 UTC | #54

Sorry if i'm being too much of a newbie, but do you have a link with an example of pose blending in Urho? I've been trying to use pose blending to improve several animation in my game, heavily [inspired by this](http://www.gdcvault.com/play/1020583/Animation-Bootcamp-An-Indie-Approach), but i can't get my head around it.

-------------------------

slapin | 2017-04-20 00:56:12 UTC | #55

@smellymumbler have you looked at IK demo with current Urho? it shows sort of IK + animation blending.

If you want to blend between animations, look at AnimationController and use layers. For more complicated cases use AnimationState (s). It is very sad there's no really goood example on these, but if you look at Character demo,
you might understand part of it then go back and ask more specific questions.

-------------------------

smellymumbler | 2017-04-20 14:39:45 UTC | #56

I did. But, at least in my head, the animation blending idea does not really work for what i'm aiming for. You have two different layers and you have a blending amount between the two. This is nice: you can make a running animation turn into a walking animation, smoothly, based on user input. 

However, what i'm aiming for is a little different: i have two poses: a standing one and another one in full run. My animation clip is the result of an interpolation between those two poses + input from the user. Are those two different layers? Can i blend them normally?

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/e597524097b2704b2170ef91b7a901de66c4ad58.png" width="501" height="247">

-------------------------

slapin | 2017-04-20 14:58:50 UTC | #57

You can blend on the same layer too. You will always use a combination of blending on the same layer and additional layers. I know the system explodes the brain, but I was enlightened after looking some GDC presentation on youtube
about layered animation, I dn't remember title. The idea is that you need to transit from one animation to another on
the same layer, so just play new pose animation on the same layer at appropriate time and it will blend into it.
Probably not best thing performance-wise, but it should work.

-------------------------

slapin | 2017-04-20 15:00:08 UTC | #58

And also, if you really understand presentation you use for inspiration, please share, I was not able to understand their way.

-------------------------

Sinoid | 2017-04-20 20:32:59 UTC | #59

Blending there is just done on arbitrary response curves between frames. (Desmos graphs for a few MKCB curves: https://www.desmos.com/calculator/bg75j7xv5c)

The "survey wheel" is just circumference vs. distance. Given a distance traveled the degrees turned can be found given the circumference (or diameter/radius -> circ) which drives animation timing. 

The "ticks" in the wheel are a bit of a red-herring that looks more important than it is, they're just visual helpers for where the timings are, the circumference is the important part. The stroke cycles of each leg are overlayed on top of each other into a final gait cycle in the wheel. (Girard, Computational Modeling for the Computer Animation of Legged Figures goes into the nitty gritty as far as actually simulating but most of the math is still valid for finding cycle timings from existing animation).

-------------------------

slapin | 2017-04-21 01:44:13 UTC | #60

Well, i was trying to achieve this differently by timing lowest leg position and change animation speed to
minimize sliding. The problem is that I failed somewhere and could not achieve the goal this way.
I don't want root motion animation, it is too unflexible... Procedural walk loop looks so promising but I was not able to
get 60fps as it was too many calculations per frame...

-------------------------

TheComet | 2017-04-21 01:53:29 UTC | #61

If your goal is to recreate what the Wolfire people achieved with Overgrowth: Let Urho3D do the heavy lifting for you. You don't have to implement blending between keyframes, let Urho3D's animation do that.

1) Create a walking animation
2) Create a running animation with the same length as the walking animation (important! If they're the same length you can easily synchronise them)

Now you can control the speed of both animations depending on stride (the "conveyor wheel" approach) and you can blend between both animations (using layers) depending on the player's velocity.

Overgrowth isn't using IK to prevent foot sliding; they still have that problem, it's just well corrected. They do use IK to align the foot vertically so it's always touching the ground.

-------------------------

slapin | 2017-04-21 03:20:08 UTC | #62

I just wonder how to do correction to prevent too much of foot sliding...

-------------------------

Sinoid | 2017-04-21 03:36:50 UTC | #63

> Well, i was trying to achieve this differently by timing lowest leg position and change animation speed to
minimize sliding. 

You can find the support duration (window in distance of circumferential travel where you can IK pin the foot) as stroke/velocity beginning with the contact frame. Stroke is the distance between the two extremes where the foot is intended to be planted. The actual transfer duration isn't realistic to find in real-time (have to build a Riemannian manifold or QEF it - either way means diagonalization [though QEF can be done in pre-diagonalized matrix form]), and probably best just left as "it's everything but the support duration."

If your legs are in perfect sequence, then you can use offset sine waves to weight the foot anchor (sin(x*PI) and sin((x+1)*PI)). It's incredibly wrong but no one is probably going to notice beyond an uncanny feeling where they know something is off but they think everything is right (as speed increases support duration reduces to near zero with at 18mph a human runs as just slapping their foot to the ground).

> Procedural walk loop looks so promising but I was not able to
get 60fps as it was too many calculations per frame...

Did you do that with the current IK stuff? FABRIK isn't cut out for walking (neither is CCD), walking is Jacobian-transpose or spring-systems only (the squash-stretch of spring systems is glorious + trivial constraints). Walking also has to be solved from the bind-pose or knees will buckle reliably.

-------------------------

slapin | 2017-04-21 03:50:21 UTC | #64

Well, my idea was - I have linear walk (just classic dull walk cycle of 9 frames) and I selected appropriate frame
depending on walk speed, so I just changed speed of animation at real time. Frame drops to about 10fps
and correction is absolutely not perfect (visual sliding still present). It looks like I need to make some parts
of animation faster and some slower to improve effect and control speed at appropriate points, I can't
just set some speed and hope for best :(
I remember old 3D studio (not max yet) had walk designer, probably that is what I miss most. Blender
is so much manual labor... On other hand i could use CMU mocap data and animate walk with
actual motion, and then compensate that, but I think there will be too many side effects
and animation will be locked to single speed. Also I wonder how this will work with RigidBodies...

About procedural loop - I thought not about actuall simulation, I thought about creating procedural animation
using some formulae and then play that animation. The actual animation might be done offline, like on game start or
even at production stage...

-------------------------

slapin | 2017-04-21 03:52:26 UTC | #65

I think the biggest problem with these walk loops is that we want walk as linear motion but the actual walk is not linear,
as it is sequence of almost-falls. So some trickery is needed to combine linear motion and walk, which I still
can't grasp...

-------------------------

TheComet | 2017-04-21 04:01:13 UTC | #66

[quote="slapin, post:62, topic:1819, full:true"]
I just wonder how to do correction to prevent too much of foot sliding...
[/quote]

If you know the length of the walk animation cycle and you know the player's velocity, you can eliminate foot sliding by adjusting the animation speed. It really is that simple.

[quote="Sinoid, post:63, topic:1819"]Did you do that with the current IK stuff? FABRIK isn't cut out for walking (neither is CCD), walking is Jacobian-transpose or spring-systems only (the squash-stretch of spring systems is glorious + trivial constraints). Walking also has to be solved from the bind-pose or knees will buckle reliably.
[/quote]

Constrained FABRIK with stiffness factors can get you very close to what a Jacobian solver has to offer.

If it's a 2 bone problem, then the algorithm is irrelevant, because the only axis of freedom is roll. All solvers (Jacobian, CCD, FABRIK, or even a direct approach using trigonometry) will deliver nearly identical results.

Overgrowth deals exclusively with 2 bone IK problems.

-------------------------

slapin | 2017-04-21 04:01:56 UTC | #67

@TheComet could you explain the idea for noobs/stupid people? I read everywhere about this can be done,
but I can't find a way how it can be done.
The problem is that adjusting speed doesn't really work for me for some strange reason :(

-------------------------

TheComet | 2017-04-21 04:05:28 UTC | #68

[quote="slapin, post:67, topic:1819"]
@TheComet could you explain the idea for noobs/stupid people? I read everywhere about this can be done,
but I can't find a way how it can be done.
The problem is that adjusting speed doesn't really work for me for some strange reason :frowning:
[/quote]

I suggest you open a new thread about this so we can discuss it more in detail there. I also suggest you show some of your code so we can see what you've tried and where you're having trouble.

-------------------------

Sinoid | 2017-04-21 05:36:52 UTC | #69

> Constrained FABRIK with stiffness factors can get you very close to what a Jacobian solver has to offer.

No, it can't. FABRIK also can't cope with squash-stretch to sell a motion. I started with porting Caliko to C++ and abandoned it very quickly as spring-systems gave superior results for my needs of remapping animation that was designed for one morphology onto another entirely different morphology.

Your implementation might have some capability for that, but that would be unique to it.

Jacobi has the best fitment and greatest constraint support. Springs have the best behaviour and though constraints are slow to solve they're trivial in implementation (just plot a quadratic or form a plane sequence upstream). When OpenCL'd they can be solved independently without consequence since they're springs.

FABRIK is just a bad variation of spring-constraints, unfortunately it loses the desirable qualities of springs. I'm running IK for all animation in SprueKit, which is a Spore-Creature-Creator clone, I've been through all IK methods, springs are the only thing you can trust. Even Cholesky methods will fall on their face, despite the fact that they conventionally slaughter Jacobi. Cholesky is so close to right and stable that it's disgusting that it could be wrong.

Springs really win when you have to solve 30k constraints per frame. That's nothing. 240k constraints are still nothing. (OpenCL of course ... CPU that'd be death)

---

Calling it a bad variation sounds worse than I mean, it's good enough for most cases. It is not good enough for "I'm going to IK everything" like I do or "I want solid stability." FABRIK is basically a tweaker.

-------------------------

sabotage3d | 2017-04-21 09:00:47 UTC | #70

When you mention springs for IK problems, do you mean classical spring and damper system? For a more complex rig how would you choose k and d coefficients? As they would vary with the number of springs in the system.

-------------------------

Sinoid | 2017-04-24 02:55:54 UTC | #71

Yes, I solve for the coeffs from the mass (targeting a 80-120% for the extremes) since I'm able to calculate the volume and assume evenly distributed mass from there (some heavy cheating for arbitrary meshes since I require neither manifold nor closed geometry to merge into the dual-grid).

[An Efficient Energy Transfer Inverse Kinematics Solution](http://perso.telecom-paristech.fr/~pelachau/site/allpapers/MIG12_Huang.pdf) was the baseline where I started.

---

Before it pops up, when I mention Cholesky, I mean solving it all as one big linear system of equations constraints and all in some large matrices. It was really ideal, except that when it failed it turned into a twisted knot instead of something minor like knee buckling. (same deal as Laplacian handle deformation, just with more elements)

-------------------------

TheComet | 2017-04-24 10:52:09 UTC | #72

Small update, I added specialised solvers that are optimised for 2 bone and 1 bone problems. This was requested by @slapin. They currently don't take target angles or constraints into consideration, but I'll add that shortly.
 
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/9e62422fe62c63e9457fe53243e07a1e835bd27e.png" width="350" height="92">

[quote="Sinoid, post:71, topic:1819, full:true"]
Yes, I solve for the coeffs from the mass (targeting a 80-120% for the extremes) since I'm able to calculate the volume and assume evenly distributed mass from there (some heavy cheating for arbitrary meshes since I require neither manifold nor closed geometry to merge into the dual-grid).

[An Efficient Energy Transfer Inverse Kinematics Solution](http://perso.telecom-paristech.fr/~pelachau/site/allpapers/MIG12_Huang.pdf) was the baseline where I started.

Before it pops up, when I mention Cholesky, I mean solving it all as one big linear system of equations constraints and all in some large matrices. It was really ideal, except that when it failed it turned into a twisted knot instead of something minor like knee buckling. (same deal as Laplacian handle deformation, just with more elements)
[/quote]

That is a neat approach. They don't go into any details on the physical constants they used (mass, spring constant, or damping factor) so I'm left wondering how you'd go about finding optimal values for those and whether it depends on the system you're solving or not. Obviously you want the system to reach equilibrium as fast as possible, which means minimising overshoot and minimising oscillation.

I see a lot of opportunity to apply control theory to solving this. Since it is an LTI system, instead of simulating the system in the time domain it might be faster to transform it into the frequency domain, where it would be a simple system of linear equations, and transform the results back.

Have you considered contributing your implementation?

-------------------------

slapin | 2017-04-25 06:44:22 UTC | #73

@TheComet
do you have plan to PR these changes yet?

-------------------------

slapin | 2017-04-30 06:27:25 UTC | #74

@TheComet

Hi! What is new about IK?

Especially I'm interested in sparse chains, where I could switch bones off participation
in IK chain. For example my leg consists of 4 bones, 2 for upper leg and 2 for lower leg,
which are used in animation in specific way. However for IK I want to just use upper bones
for both parts, so to save on solving (and have more realistic result). Do you have plans for this?

Thanks!

-------------------------

TheComet | 2017-04-30 15:18:43 UTC | #75

You'll have to make an example of what you expect to happen because I don't understand what you mean.

It's a bad idea to use IK for driving animation. You really should only use it for small corrections.

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/1415cf053f4ffced9cd84cad5bba2d766e8184ab.png" width="286" height="284">

-------------------------

slapin | 2017-04-30 15:49:27 UTC | #76

We have cool image board here!

This is what I struggle with:
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/2469704d841e95d1caf6ac26ac1fd49070e6b013.png" width="500" height="500">

-------------------------

slapin | 2017-04-30 15:50:19 UTC | #77

I think some bone filtering won't hurt.

-------------------------

TheComet | 2017-04-30 16:03:13 UTC | #78

Oh OK, I see what you mean now. You want to combine multiple bones into  a single bone and solve for that.

I can add that to the TODO list, it shouldn't be a difficult modification to make. I'm just wondering whether this should be part of the IK lib or whether Urho3D should already take care of this.

-------------------------

slapin | 2017-04-30 16:07:55 UTC | #79

Well, I don't think "other Urho" should be doing this. These bones are not useless - they are just not used for IK setups.
For some detailed animations (where IK is not used, at least not in all cases) these bones are very useful.
I don't think skeleton changes for every animation are too practical.

-------------------------

slapin | 2017-04-30 16:10:41 UTC | #80

I think some method like IgnoreBone(int/String)/UnIgnoreBone(int/String) could be used
and just keeping array ignored bones. When travelling chain we just skip it and go for its parent.
Should not be too resource consuming...

-------------------------

TheComet | 2017-05-03 05:32:51 UTC | #81

I've decided to tie it into the constraint system. There's a "stiff" constraint you can attach to a node that effectively causes it to get ignored when building the chain tree.

The performance gain for this optimisation is pretty much negligible, at least in the case of constraintless FABRIK.

-------------------------

slapin | 2017-05-26 17:56:52 UTC | #82

Hi, all!

@TheComet it looks like something fishy is going on, but I can't understand what. 

Doing the following:

        Node *head_bone = node_->GetChild("head", true);
        Node *root_bone = node_->GetChild("spine02", true);
        IKEffector *ike = head_bone->CreateComponent<IKEffector>();
        ike->SetChainLength(2);
        iks = root_bone->CreateComponent<IKSolver>();
        iks->EnableAutoSolve(false);
        iks->EnableUpdatePose(true);
        SubscribeToEvent(E_SCENEDRAWABLEUPDATEFINISHED, URHO3D_HANDLER(BTBlackboard, HandleSceneDrawableUpdateFinished));

And get crash on creation of IKSolver.

```
#3  0x0000000000b86994 in Urho3D::IKSolver::BuildTreeToEffector (this=0x0, node=0xd946a20) at /home/slapin/Urho3D/Source/Urho3D/IK/IKSolver.cpp:387
#4  0x0000000000b86ad2 in Urho3D::IKSolver::HandleComponentAdded (this=0xcd2c5b0, eventType=..., eventData=...) at /home/slapin/Urho3D/Source/Urho3D/IK/IKSolver.cpp:423
#5  0x0000000000b894be in Urho3D::EventHandlerImpl<Urho3D::IKSolver>::Invoke (this=0xa0a11a0, eventData=...) at /home/slapin/Urho3D/Source/Urho3D/IK/../IK/../Scene/../Scene/../Scene/../Core/Object.h:307
#6  0x0000000000baf801 in Urho3D::Object::OnEvent (this=0xcd2c5b0, sender=0x2f914c0, eventType=..., eventData=...) at /home/slapin/Urho3D/Source/Urho3D/Core/Object.cpp:121
#7  0x0000000000bb0396 in Urho3D::Object::SendEvent (this=0x2f914c0, eventType=..., eventData=...) at /home/slapin/Urho3D/Source/Urho3D/Core/Object.cpp:355
#8  0x00000000009803ea in Urho3D::Node::AddComponent (this=0xd946a20, component=0xd67f8d0, id=16777474, mode=Urho3D::LOCAL) at /home/slapin/Urho3D/Source/Urho3D/Scene/Node.cpp:1851
#9  0x000000000097c611 in Urho3D::Node::CreateComponent (this=0xd946a20, type=..., mode=Urho3D::LOCAL, id=0) at /home/slapin/Urho3D/Source/Urho3D/Scene/Node.cpp:922
#10 0x00000000008e1820 in Urho3D::Node::CreateComponent<Urho3D::IKEffector> (this=0xd946a20, mode=Urho3D::REPLICATED, id=0) at /home/slapin/Urho3D/include/Urho3D/IK/../Scene/../Scene/Node.h:706
#11 0x00000000008dca85 in BTBlackboard::Start (this=0xd67f6c0) at /home/slapin/dungeon/rework/BehaviorTree.cpp:47
#12 0x0000000000988ef0 in Urho3D::LogicComponent::OnNodeSet (this=0xd67f6c0, node=0xd8eaaa0) at /home/slapin/Urho3D/Source/Urho3D/Scene/LogicComponent.cpp:83
#13 0x0000000000975e0c in Urho3D::Component::SetNode (this=0xd67f6c0, node=0xd8eaaa0) at /home/slapin/Urho3D/Source/Urho3D/Scene/Component.cpp:259
#14 0x0000000000980230 in Urho3D::Node::AddComponent (this=0xd8eaaa0, component=0xd67f6c0, id=0, mode=Urho3D::REPLICATED) at /home/slapin/Urho3D/Source/Urho3D/Scene/Node.cpp:1821
#15 0x000000000097c611 in Urho3D::Node::CreateComponent (this=0xd8eaaa0, type=..., mode=Urho3D::REPLICATED, id=0) at /home/slapin/Urho3D/Source/Urho3D/Scene/Node.cpp:922
#16 0x00000000012197ee in Urho3D::NodeCreateComponent (typeName=..., mode=Urho3D::REPLICATED, id=0, ptr=0xd8eaaa0) at /home/slapin/Urho3D/Source/Urho3D/AngelScript/../AngelScript/APITemplates.h:517
#17 0x0000000000fa7d0f in endstack () at /home/slapin/Urho3D/Source/ThirdParty/AngelScript/source/as_callfunc_x64_gcc.cpp:162
#18 0x0000000000fa8706 in CallSystemFunctionNative (context=0x30d4180, descr=0x2535ed0, obj=0xd8eaaa0, args=0x2f66a98, retPointer=0x0, retQW2=@0x7fffffffd820: 0, secondObject=0x0)
    at /home/slapin/Urho3D/Source/ThirdParty/AngelScript/source/as_callfunc_x64_gcc.cpp:468
#19 0x0000000000908037 in CallSystemFunction (id=2367, context=0x30d4180) at /home/slapin/Urho3D/Source/ThirdParty/AngelScript/source/as_callfunc.cpp:712
#20 0x00000000008eef32 in asCContext::ExecuteNext (this=0x30d4180) at /home/slapin/Urho3D/Source/ThirdParty/AngelScript/source/as_context.cpp:2515
#21 0x00000000008ec423 in asCContext::Execute (this=0x30d4180) at /home/slapin/Urho3D/Source/ThirdParty/AngelScript/source/as_context.cpp:1297
#22 0x00000000009cc314 in Urho3D::ScriptFile::Execute (this=0x2f4b790, function=0x30d4a10, parameters=..., unprepare=true) at /home/slapin/Urho3D/Source/Urho3D/AngelScript/ScriptFile.cpp:324
#23 0x00000000009cf13a in Urho3D::ScriptEventInvoker::HandleScriptEvent (this=0x3103d90, eventType=..., eventData=...) at /home/slapin/Urho3D/Source/Urho3D/AngelScript/ScriptFile.cpp:956
#24 0x00000000009d30d8 in Urho3D::EventHandlerImpl<Urho3D::ScriptEventInvoker>::Invoke (this=0x2411210, eventData=...) at /home/slapin/Urho3D/Source/Urho3D/AngelScript/../AngelScript/../Core/Object.h:307
#25 0x0000000000baf801 in Urho3D::Object::OnEvent (this=0x3103d90, sender=0x1cdfdd0, eventType=..., eventData=...) at /home/slapin/Urho3D/Source/Urho3D/Core/Object.cpp:121
#26 0x0000000000bb0396 in Urho3D::Object::SendEvent (this=0x1cdfdd0, eventType=..., eventData=...) at /home/slapin/Urho3D/Source/Urho3D/Core/Object.cpp:355
#27 0x0000000000bcec7e in Urho3D::Engine::Update (this=0x1cdfdd0) at /home/slapin/Urho3D/Source/Urho3D/Engine/Engine.cpp:695
#28 0x0000000000bce5be in Urho3D::Engine::RunFrame (this=0x1cdfdd0) at /home/slapin/Urho3D/Source/Urho3D/Engine/Engine.cpp:519
#29 0x0000000000bcb162 in Urho3D::Application::Run (this=0x1cdfc40) at /home/slapin/Urho3D/Source/Urho3D/Engine/Application.cpp:86
#30 0x00000000008e6301 in RunApplication () at /home/slapin/dungeon/rework/Urho3DPlayer.cpp:47
#31 0x00000000008e63a8 in main (argc=1, argv=0x7fffffffe248) at /home/slapin/dungeon/rework/Urho3DPlayer.cpp:47
```

This looks like it failed to generate tree, and fails to find any node thus crashing.
I added some debug in the loop to show node name it parses:

```
[Fri May 26 20:44:27 2017] INFO: chain: head
[Fri May 26 20:44:27 2017] INFO: chain: neck03
[Fri May 26 20:44:27 2017] INFO: chain: neck02
[Fri May 26 20:44:27 2017] INFO: chain: neck01
[Fri May 26 20:44:27 2017] INFO: chain: spine01
[Fri May 26 20:44:27 2017] INFO: chain: spine02
[Fri May 26 20:44:27 2017] INFO: chain: spine03
[Fri May 26 20:44:27 2017] INFO: chain: spine04
[Fri May 26 20:44:27 2017] INFO: chain: spine05
[Fri May 26 20:44:27 2017] INFO: chain: root
[Fri May 26 20:44:27 2017] INFO: chain: AdjNode
[Fri May 26 20:44:27 2017] INFO: chain: npc1
[Fri May 26 20:44:27 2017] INFO: chain: 
```
Which looks like it parses till scene, than gets NULL and crashes.
I wonder why it fails building tree completely. I use makehuman model for test.

I created the bug

https://github.com/urho3d/Urho3D/issues/1957

to indicate the issue.

-------------------------

slapin | 2017-05-26 18:07:48 UTC | #83

I wonder why sample works and my code does not, as I'm doing exactly the same thing, only model is different.

-------------------------

slapin | 2017-05-26 19:22:25 UTC | #84

OK, I found the source of a problem - the solver doesn't work on multiple meshes,
it works only on first one.

-------------------------

slapin | 2017-05-26 19:34:51 UTC | #85

INFO: IKSolver::SetAlgorithm() is run only once, even though it is run in constructor - probably constructor is not being called too...

-------------------------

slapin | 2017-05-26 19:41:30 UTC | #86

Yep, I was right - the constructor is not called for all instances except first one.
Is it supposed to be?

-------------------------

slapin | 2017-05-26 20:23:44 UTC | #87

OK, this is related to REPLICATED mode. But even in LOCAL mode I still get crashes.
Looks like function is called second time.

```
[Fri May 26 23:09:40 2017] INFO: IKSolver::SetAlgorithm()
[Fri May 26 23:09:40 2017] INFO: [IK] Creating FABRIK solver
[Fri May 26 23:09:40 2017] INFO: bone nnode: head
[Fri May 26 23:09:40 2017] INFO: looking in: 1b792270
[Fri May 26 23:09:40 2017] INFO: bone nnode: neck03
[Fri May 26 23:09:40 2017] INFO: looking in: 1b792270
[Fri May 26 23:09:40 2017] INFO: bone nnode: neck02
[Fri May 26 23:09:40 2017] INFO: looking in: 1b792270
[Fri May 26 23:09:40 2017] INFO: bone nnode: neck01
[Fri May 26 23:09:40 2017] INFO: looking in: 1b792270
[Fri May 26 23:09:40 2017] INFO: bone nnode: spine01
[Fri May 26 23:09:40 2017] INFO: looking in: 1b792270
[Fri May 26 23:09:40 2017] INFO: node: 1b792270child: 1b70f0e0
[Fri May 26 23:09:40 2017] INFO: node: 1b70f0e0child: 1b70f1e0
[Fri May 26 23:09:40 2017] INFO: node: 1b70f1e0child: 1b70f260
[Fri May 26 23:09:40 2017] INFO: node: 1b70f260child: 1b70f310
[Fri May 26 23:09:40 2017] INFO: node: 1b70f310child: 1b70f3c0
[Fri May 26 23:09:40 2017] INFO: bone nnode: head
[Fri May 26 23:09:40 2017] INFO: looking in: 1b792270
[Fri May 26 23:09:40 2017] INFO: bone nnode: neck03
[Fri May 26 23:09:40 2017] INFO: looking in: 1b792270
[Fri May 26 23:09:40 2017] INFO: bone nnode: neck02
[Fri May 26 23:09:40 2017] INFO: looking in: 1b792270
[Fri May 26 23:09:40 2017] INFO: bone nnode: neck01
[Fri May 26 23:09:40 2017] INFO: looking in: 1b792270
[Fri May 26 23:09:40 2017] INFO: bone nnode: spine01
[Fri May 26 23:09:40 2017] INFO: looking in: 1b792270
[Fri May 26 23:09:40 2017] INFO: bone nnode: spine02
[Fri May 26 23:09:40 2017] INFO: looking in: 1b792270
[Fri May 26 23:09:40 2017] INFO: bone nnode: spine03
[Fri May 26 23:09:40 2017] INFO: looking in: 1b792270
[Fri May 26 23:09:40 2017] INFO: bone nnode: spine04
[Fri May 26 23:09:40 2017] INFO: looking in: 1b792270
[Fri May 26 23:09:40 2017] INFO: bone nnode: spine05
[Fri May 26 23:09:40 2017] INFO: looking in: 1b792270
[Fri May 26 23:09:40 2017] INFO: bone nnode: root
[Fri May 26 23:09:40 2017] INFO: looking in: 1b792270
[Fri May 26 23:09:40 2017] INFO: bone nnode: AdjNode
[Fri May 26 23:09:40 2017] INFO: looking in: 1b792270
[Fri May 26 23:09:40 2017] INFO: bone nnode: npc1
[Fri May 26 23:09:40 2017] INFO: looking in: 1b792270
[Fri May 26 23:09:40 2017] INFO: bone nnode: 
[Fri May 26 23:09:40 2017] INFO: looking in: 1b792270

Program received signal SIGSEGV, Segmentation fault.
0x0000000000976aa4 in Urho3D::Node::GetID (this=0x0) at /home/slapin/Urho3D/Source/Urho3D/Scene/../Scene/../Scene/Node.h:338
338	    unsigned GetID() const { return id_; }
(gdb) bt
#0  0x0000000000976aa4 in Urho3D::Node::GetID (this=0x0) at /home/slapin/Urho3D/Source/Urho3D/Scene/../Scene/../Scene/Node.h:338
#1  0x0000000000b86e2e in Urho3D::IKSolver::BuildTreeToEffector (this=0x1b791d20, node=0xd946250) at /home/slapin/Urho3D/Source/Urho3D/IK/IKSolver.cpp:391
#2  0x0000000000b87140 in Urho3D::IKSolver::HandleComponentAdded (this=0x1b791d20, eventType=..., eventData=...) at /home/slapin/Urho3D/Source/Urho3D/IK/IKSolver.cpp:425
#3  0x0000000000b89b2c in Urho3D::EventHandlerImpl<Urho3D::IKSolver>::Invoke (this=0x1b792080, eventData=...) at /home/slapin/Urho3D/Source/Urho3D/IK/../IK/../Scene/../Scene/../Scene/../Core/Object.h:307
#4  0x0000000000bafe6f in Urho3D::Object::OnEvent (this=0x1b791d20, sender=0x3006060, eventType=..., eventData=...) at /home/slapin/Urho3D/Source/Urho3D/Core/Object.cpp:121
#5  0x0000000000bb0a04 in Urho3D::Object::SendEvent (this=0x3006060, eventType=..., eventData=...) at /home/slapin/Urho3D/Source/Urho3D/Core/Object.cpp:355
#6  0x00000000009807de in Urho3D::Node::AddComponent (this=0xd946250, component=0x1b70f7a0, id=16777478, mode=Urho3D::LOCAL) at /home/slapin/Urho3D/Source/Urho3D/Scene/Node.cpp:1851
#7  0x000000000097ca05 in Urho3D::Node::CreateComponent (this=0xd946250, type=..., mode=Urho3D::LOCAL, id=0) at /home/slapin/Urho3D/Source/Urho3D/Scene/Node.cpp:922
#8  0x00000000008e1bd0 in Urho3D::Node::CreateComponent<Urho3D::IKEffector> (this=0xd946250, mode=Urho3D::LOCAL, id=0) at /home/slapin/Urho3D/include/Urho3D/IK/../Scene/../Scene/Node.h:706
#9  0x00000000008dcf43 in BTBlackboard::DelayedStart (this=0xd67eee0) at /home/slapin/dungeon/rework/BehaviorTree.cpp:58
#10 0x00000000009899f2 in Urho3D::LogicComponent::HandleSceneUpdate (this=0xd67eee0, eventType=..., eventData=...) at /home/slapin/Urho3D/Source/Urho3D/Scene/LogicComponent.cpp:178
#11 0x000000000098a610 in Urho3D::EventHandlerImpl<Urho3D::LogicComponent>::Invoke (this=0xd6641b0, eventData=...) at /home/slapin/Urho3D/Source/Urho3D/Scene/../IO/../Core/Object.h:307
#12 0x0000000000bafe24 in Urho3D::Object::OnEvent (this=0xd67eee0, sender=0x3006060, eventType=..., eventData=...) at /home/slapin/Urho3D/Source/Urho3D/Core/Object.cpp:113
#13 0x0000000000bb0862 in Urho3D::Object::SendEvent (this=0x3006060, eventType=..., eventData=...) at /home/slapin/Urho3D/Source/Urho3D/Core/Object.cpp:325
#14 0x00000000010f57eb in Urho3D::Scene::Update (this=0x3006060, timeStep=0.0525000021) at /home/slapin/Urho3D/Source/Urho3D/Scene/Scene.cpp:781
#15 0x00000000010f7287 in Urho3D::Scene::HandleUpdate (this=0x3006060, eventType=..., eventData=...) at /home/slapin/Urho3D/Source/Urho3D/Scene/Scene.cpp:1171
#16 0x00000000010fd1cc in Urho3D::EventHandlerImpl<Urho3D::Scene>::Invoke (this=0x30ad0d0, eventData=...) at /home/slapin/Urho3D/Source/Urho3D/Scene/../Core/../Core/Object.h:307
#17 0x0000000000bafe6f in Urho3D::Object::OnEvent (this=0x3006060, sender=0x1ce0dd0, eventType=..., eventData=...) at /home/slapin/Urho3D/Source/Urho3D/Core/Object.cpp:121
#18 0x0000000000bb0a04 in Urho3D::Object::SendEvent (this=0x1ce0dd0, eventType=..., eventData=...) at /home/slapin/Urho3D/Source/Urho3D/Core/Object.cpp:355
#19 0x0000000000bcf2ec in Urho3D::Engine::Update (this=0x1ce0dd0) at /home/slapin/Urho3D/Source/Urho3D/Engine/Engine.cpp:695
#20 0x0000000000bcec2c in Urho3D::Engine::RunFrame (this=0x1ce0dd0) at /home/slapin/Urho3D/Source/Urho3D/Engine/Engine.cpp:519
#21 0x0000000000bcb7d0 in Urho3D::Application::Run (this=0x1ce0c40) at /home/slapin/Urho3D/Source/Urho3D/Engine/Application.cpp:86
#22 0x00000000008e66f5 in RunApplication () at /home/slapin/dungeon/rework/Urho3DPlayer.cpp:47
#23 0x00000000008e679c in main (argc=1, argv=0x7fffffffe248) at /home/slapin/dungeon/rework/Urho3DPlayer.cpp:47
```

Well, I give up on this, hope to get some fix from you. Sorry for bother.

-------------------------

TheComet | 2017-05-27 14:51:27 UTC | #88

Yeah, unfortunately you ran into the crash I wanted to fix for the Urho 1.6 release. I still have not had any time to get around to submitting the PR, I have been buried in exams.

-------------------------

slapin | 2017-05-27 17:32:23 UTC | #89

Did you mean 1.7? Any plans? or maybe you have patches, then I could try testing/making PR for you.
so the problems I encountered so far:
1. Early crash in default REPLICATED mode - as it relies on constructor to initialize, and constructor is not run.
2. Even in LOCAL mode there is a crash after a few instances created due to some strange issue,
which I did not debug fully yet as I have no time. But this one happens quite a bit later than first one.

This is what I'm encountered. Hope you will have time soon to fix this. I really would like to use IK for some stuff.

-------------------------

TheComet | 2017-08-06 15:27:16 UTC | #90

Here are a list of things that I still need to fix for 1.7:
  - The interface Urho <-> ik lib needs to use local positions and rotations instead of global positions and rotations. This will fix a major oversight where updating the position of the root node won't affect the chain positions, effectively "locking" the object in place. I believe this is the root cause of the "0,0,0 effector" issue ([#2054](https://github.com/urho3d/Urho3D/issues/2054)). The mechanisms for this fix are already in place, it's just a matter of doing the work.
  - IKEffector INHERIT_PARENT_SCOPE isn't implemented yet.
  - Finish writing documentation in Reference.dox

Here's a list of changes in the currently pending PR:
  - It's now possible to have IKSolver components that share the same subtrees ([#2058](https://github.com/urho3d/Urho3D/issues/2058)).
  - Urho avoids the call to abort() by not calling ik_solver_solve() if the tree is invalid.
  - Fixed a bug in solver_FABRIK_solve() where the root position was incorrectly being set to the original root node position instead of the active root node position. This bug made it impossible to move the root node if USE_ORIGINAL_POSE was disabled.
  - Added a chain tree iterator, which allows Urho to iterate over only the nodes that are affected by the solver instead of having to iterate over all nodes in the tree.
  - The scripting API for SetFeature()/GetFeature() was changed, such that now you can write ```solver.FEATURE_NAME = true``` directly, instead of having to type ```solver.SetFeature(IKFeature.FEATURE_NAME, true)```
  - Updating/Adding docstrings.

Things that are still pending or otherwise need investigating (not necessarily for the 1.7 release)
  - In ```chain_tree.h```, each chain island holds a list of "transform dependent nodes". As far as I can tell, this is no longer necessary.
  - Bone skipping, as explained by @slapin 
  - Joint constraints (this is being worked on in the background but isn't close to being finished yet).
  - Is it necessary to save the "original pose" when serializing?

-------------------------

slapin | 2017-08-06 16:49:43 UTC | #91

Thanks for your great work! Looking forward to it!

-------------------------

TheComet | 2019-05-23 13:20:01 UTC | #92

I was able to get the library to accept positions/rotations in local space now instead of in global space. I'm currently having fun debugging final rotations:

![cool|400x320](upload://gLJeCnsaWCuEMZDmxMblFpXts6N.gif)

-------------------------

TheComet | 2019-05-23 13:20:02 UTC | #93

Alright, fixed the joint rotations. Now that the tree is specified in local space rather than global space, it fixes an issue where if you were to move a parent node of the solver's node, the pose wouldn't inherit that position (or rotation).

You can see me moving the base node first, then move a parent node of that base node, and also rotate the base node.

![cool|500x300](upload://b0lj4N45ZmrBdteqssTPp0K2Jrr.gif)

@slapin I believe this fixes the 0,0,0 effector issues. I would be happy if you could pull and verify if this is the case or not: https://github.com/thecomet93/urho3d/tree/IK1.7

-------------------------

slapin | 2017-08-07 09:28:08 UTC | #94

Well, IKFeature is gone somewhere... but I don't see any other changes.

also setting to TWO_BONE and FABRIK seems irrelevant, looks like setting is ignored.

```AngelScript
void Init()
{
        IKEffector@ leftEffector  = leftFoot.CreateComponent("IKEffector");
        leftEffector.chainLength = 2;
        leftEffector.targetPosition = leftFoot.worldPosition;
        IKEffector@ rightEffector = rightFoot.CreateComponent("IKEffector");
        rightEffector.targetPosition = rightFoot.worldPosition;
        rightEffector.chainLength = 2;
        Node@ spine = node.GetChild("root", true);
        solver = spine.CreateComponent("IKSolver");
//        solver.SetFeature(IKFeature::AUTO_SOLVE, false);
//        solver.SetFeature(IKFeature::UPDATE_ORIGINAL_POSE, true);
        solver.algorithm = IKAlgorithm::FABRIK;
}
...
    void HandleSceneDrawableUpdateFinished(StringHash eventType, VariantMap& eventData)
    {
        Node@ rfoot = node.GetChild("foot.R", true);
        Node@ lfoot = node.GetChild("foot.L", true);
        IKEffector@ re = rfoot.GetComponent("IKEffector");
        IKEffector@ le = lfoot.GetComponent("IKEffector");
        re.targetPosition = Vector3(100.0f, 0.0f, 100);
        le.targetPosition = Vector3(100.0f, 0.0f, -100);
        // solver.SetFeature(IKFeature::UPDATE_ORIGINAL_POSE, true);
        solver.Solve();
    }

```

-------------------------

slapin | 2017-08-07 09:30:11 UTC | #95

And visual representation is the same as with my video on the bug - legs are directed to global (0, 0, 0)

-------------------------

TheComet | 2017-08-07 09:59:32 UTC | #96

That is so strange. Is your project available online? Can I download and debug it?

Yeah I should have told you: I removed IKFeature for the script bindings to make it easier. Now you can type:

        solver = spine.CreateComponent("IKSolver");
        solver.AUTO_SOLVE = false;
        solver.UPDATE_ORIGINAL_POSE = true;

-------------------------

slapin | 2017-08-07 10:28:57 UTC | #97

It is not that small thing to share, If you send me your email via PM I can send you a link.

-------------------------

TheComet | 2017-08-07 10:53:13 UTC | #98

I sent you a PM.

I'm really baffled at what's causing this, because I don't see any way that the target position *cannot* be set. The two relevant functions are these:

    void IKEffector::SetTargetPosition(const Vector3& targetPosition)
    {
        targetPosition_ = targetPosition;
        if (ikEffectorNode_ != NULL)
            ikEffectorNode_->effector->target_position = Vec3Urho2IK(targetPosition);
    }

    void IKEffector::SetIKEffectorNode(ik_node_t* effectorNode)
    {
        ikEffectorNode_ = effectorNode;
        if (effectorNode)
        {
            ikEffectorNode_->effector->target_position = Vec3Urho2IK(targetPosition_);
            ikEffectorNode_->effector->target_rotation = QuatUrho2IK(targetRotation_);
            /* setting other properties here, omitted for clarity */
        }
    }

The two situations you can be in:

  - If you set the target position *before* the tree is built, then ```ikEffectorNode_``` will be NULL, and the target position is stored in ```targetPosition_```. Then, when you call Solve(), the tree is first built and ```SetIKEffectorNode()``` is called. The target position is copied correctly from ```targetPosition_``` into ```effectorNode->effector->target_position```.
  - If you set the target position *after* the tree is built, then ```SetIKEffectorNode()``` will already have been called, thus, ```ikEffectorNode_``` is not NULL and therefore the target position is correctly copied into ```effectorNode->effector->target_position```.

The only thing that could be causing the target position to be something else would be if you set a target node via ```IKEffector.SetTargetNode()``` or if you set a target name via ```IKEffector.SetTargetName()```. You're not doing this in the code you've posted so far, so I assume that's not the issue.

-------------------------

TheComet | 2017-08-07 10:59:37 UTC | #99

Oooh, shit. I think it just dawned on me what's causing it (as I was typing that last sentence). Solve() calls the following code:

    void IKEffector::UpdateTargetNodePosition()
    {
        if (targetNode_ == NULL)
        {
            SetTargetNode(node_->GetScene()->GetChild(targetName_, true));
            if (targetNode_ == NULL)
                return;
        }

        SetTargetPosition(targetNode_->GetWorldPosition());
        SetTargetRotation(targetNode_->GetWorldRotation());
    }

This looks wrong. I'm calling ```GetChild("", true)``` with an empty string. If this returns a valid Node* then we now know what the root of the problem is.

-------------------------

George1 | 2017-08-10 02:20:38 UTC | #100

Looking good.
Have you start looking at constraint?

You could check for constraint satisfaction after the two passes (F. B.) once goal has been reached. Otherwise just check between each pass will also work. You have to manage the case of singularity and maximum reach.

-------------------------

TheComet | 2017-08-10 15:13:45 UTC | #101

I've found that applying constraints after each pass (or at the end) causes the solution to diverge. You have to apply constraints at every step during forwards and backwards iteration for it to work.

I was trying to figure out a way to avoid having to transform the tree from global space into local space, then back again every time I have to constrain a joint. That's where I'm stuck at the moment.

A naive implementation would be to just do those transforms and be done with it. There are more optimal ways, though, like only partially transforming the tree, or an approach where you "ping-pong" between two tree instances (one in global space, the other in local space).

-------------------------

