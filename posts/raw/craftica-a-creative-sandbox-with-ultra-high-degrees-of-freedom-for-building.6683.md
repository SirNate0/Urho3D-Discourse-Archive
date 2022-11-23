daokoder | 2021-02-06 16:57:43 UTC | #1

Hello,

This is a game and the first game I created. I am a bit unsure if it is qualified as a showcase here, if not, I am sorry and I will delete this post.

This game is built upon a game engine I forked from Urho3D. This game engine was initially forked from the Atomic Game Engine, from which I first got to know Urho3D. When the Atomic Game Engine was discontinued, I rebased my fork on Urho3D.

Before Urho3D and Atomic, I have tried a number of open source game engines. I must say Urho3D is one of the best open source engines I could find. If the reasons for which I forked the engine are considered, it is the best and only (these reasons include integration with Qt and easy to wrap for Dao).

Now about this game. The game is named [Craftica](http://craftica.net).

Craftica is a creative sandbox game with ultra high degrees of freedom for building. It is partially inspired by Minecraft, but Craftica supports multiscale subvoxels so that smoother objects can be built in more realistic scales, and makes it possible to build elegant architectures.

Craftica also provides a large number of electronic and mechanical as well as other related device items, allowing players to build sophisticated circuits and circuit-controlled electronic and mechanical devices. Players can even build vehicles, aircrafts, robots and computers etc. high-tech objects from items as basic as logical gates.

![Robotic_Vehicle|600x338](upload://iXx45BX69mczidof0FfnsG2wcnC.gif) 

This game was release on Steam EA nearly a year ago. But it is not until recently that it starts to really become what I hoped for this game. You may take a look at the following youtube video if you are interested:
[Craftica: Building Your Wonderland](https://www.youtube.com/watch?v=YCMCbWW8ymk)

-------------------------

Modanung | 2021-02-06 17:40:15 UTC | #2

That looks pretty advanced!

May I ask what changes you made in relation to Qt integration?

-------------------------

daokoder | 2021-02-06 18:04:12 UTC | #3

[quote="Modanung, post:2, topic:6683, full:true"]
May I ask what changes you made in relation to Qt integration?
[/quote]

Actually, if I remember correctly, only a few methods in the Graphics and Input subsystems were changed to virtual functions for Qt integration. Then my Qt application implemented two derived subsystems and reimplemented these virtual functions.

There might be a few other changes, but I don't remember exactly. These changes were done 3 or 4 years ago, I need to look into the source code to be sure.

But what I can say for sure is that, it is actually not that hard, once you know it is possible :grinning:

-------------------------

JTippetts1 | 2021-02-06 18:35:28 UTC | #4

This looks pretty nice, good job.

-------------------------

throwawayerino | 2021-02-06 19:03:47 UTC | #5

I'm more intrigued by the physics aspect of the thing and the fact that the walker in the gif looks pretty stable. Did you use bullet's constraints or made something custom? Were there any challenges with making a stable machine editor?

-------------------------

SirNate0 | 2021-02-07 06:27:39 UTC | #6

Looks amazing! If I may ask, how do you handle the sub-voxels?

-------------------------

daokoder | 2021-02-07 09:03:44 UTC | #7

[quote="throwawayerino, post:5, topic:6683, full:true"]
I'm more intrigued by the physics aspect of the thing and the fact that the walker in the gif looks pretty stable. Did you use bullet's constraints or made something custom? Were there any challenges with making a stable machine editor?
[/quote]

I used bullet's constraints, but with some adjustments. After each simulation step, the expected relative location and orientation of the constraints (only hinge and slider constraints are handled) calculated, if their actual relative location and orientation deviate significantly, a minor force or torque is calculated applied to the each part of the constraints to force them toward the expect states.

If the adjustment force is tuned properly, this works fine most of the time, but it still fails in a few cases. However, it appears to fail consistently, so I believe with further tuning the problem in those cases could be eliminated.

-------------------------

Modanung | 2021-02-07 10:36:53 UTC | #8

Are you familiar with the *motor* functionality of Bullet constraints? This is not exposed/wrapped.

-------------------------

throwawayerino | 2021-02-07 11:43:13 UTC | #9

What's the class name? Are you referring to the gear constraint? I would love to have that exposed via the API.

-------------------------

Modanung | 2021-02-07 12:36:30 UTC | #10

It's woven into the Bullet constraint classes. Search for "motor" in `ThirdParty/Bullet/src/BulletDynamics/ConstraintSolver/bt*Constraint.*`. You can access these functions by static casting the `btTypedConstraint` returned by `Constraint::GetConstraint()`.

-------------------------

johnnycable | 2021-02-08 16:06:48 UTC | #11

This is absolutely fine. Mechanic constructions are amazing! :smile:

-------------------------

daokoder | 2021-02-08 16:59:02 UTC | #12

[quote="SirNate0, post:6, topic:6683, full:true"]
Looks amazing! If I may ask, how do you handle the sub-voxels?
[/quote]

First, the subvoxels are defined as cubes with one or more corners chopped off. So there are only three distinct shapes for the subvoxels. Differently orientated shapes are considered as different subvoxels, there are exactly 28 types of subvoxels.

The handling of them is indeed much more complicated than just handling the full cube as voxel. But due to their symmetry, many places in the various handling of them can actually be simplified. Also these subvoxels have one thing in common - they all have exactly one slope face, this property can also be exploited to simplify the handling.

Among other things, I found two things are also important in handling these subvoxels: spatial imagination and patience. Because regardless how you manage to simplify it, the handling of these subvoxels remains tedious and error prone.

Your question is a bit general, I find it a bit difficult to answer. I hope my answer is to the point in some way.

-------------------------

daokoder | 2021-02-08 17:02:34 UTC | #13

[quote="Modanung, post:8, topic:6683, full:true"]
Are you familiar with the *motor* functionality of Bullet constraints? This is not exposed/wrapped.
[/quote]

Not really, this is the first time I heard about it. I will have a look into it. Thank you for pointing it out, it might turn out to be something really useful.

-------------------------

daokoder | 2021-02-08 17:15:04 UTC | #14

[quote="johnnycable, post:11, topic:6683, full:true"]
This is absolutely fine. Mechanic constructions are amazing! :smile:
[/quote]

I hope I can make this part as fun as possible in this game :grinning:

-------------------------

daokoder | 2021-09-04 08:06:08 UTC | #15

Hello, I have made some significant improvements to this game. Now the voxels and subvoxels are deformable, namely, the blocks can be made more round or more sharp, and the models can become very smooth with round blocks. The terrain generation has also been improved greatly.

https://www.youtube.com/watch?v=i1M_loVqhEM

-------------------------

