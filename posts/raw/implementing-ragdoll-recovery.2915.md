slapin | 2017-03-17 10:58:18 UTC | #1

Hi, all!

As I see people are implementing it I wonder how to do it.

Per book it is done like this - we have a number of animations and have skeleton with bones set by ragdoll.
We remove/disable ragdoll from bones leaving transform intact and the looking for best matching animation
which is most close to current ragdoll position, then setting the desired animation to playback and enabling
animations for bones.

The question is - how can I find best matching animation? is there some way to look-up bone positions in
animations without playing them?

Thanks!

-------------------------

jmiller | 2017-03-18 18:52:25 UTC | #2

Studying Lumak's thread and video:
http://discourse.urho3d.io/t/ragdoll-recovery-test/2673

I'm not a specialist here, but it seems to me that his video shows like two standing animations, selected by torso bone transform (facedown/faceup).

-------------------------

slapin | 2017-03-18 21:15:55 UTC | #3

But how to slowly transform curent pose to first frame of animation? It is quite fluent doing that...
@Lumak please tell us the truth!

-------------------------

jmiller | 2017-03-19 16:42:32 UTC | #4

It seems to me that he explained exactly that.
http://discourse.urho3d.io/t/ragdoll-recovery-test/2673/7

or maybe I misunderstood, but I'm not specialist here. If there are questions, maybe he will be kind enough to elaborate on his technique there.

-------------------------

slapin | 2017-03-19 16:48:01 UTC | #5

Well, is it possible to do all that without c++ trickery?
I just wonder how can I access animation transforms directly to do some magic... that would solve everything...

-------------------------

Lumak | 2017-03-19 17:38:15 UTC | #6

[quote="jmiller, post:4, topic:2915"]
It seems to me that he explained exactly that. 
or maybe I misunderstood, but I'm not specialist here. If there are questions, maybe he will be kind enough to elaborate on his technique there.
[/quote]

It's exactly that.  Changes to AnimatedModel and AnimationController classes are required.
[quote="slapin, post:5, topic:2915"]
Well, is it possible to do all that without c++ trickery?
[/quote]

C++ classes mentioned above are required.

-------------------------

slapin | 2017-03-19 17:41:14 UTC | #7

@Lumak thanks a lot for explanation.

Maybe you know, is it possible to get access to animation's transforms for more elaborate solution
to algorithmically select best-fit animation?

-------------------------

Lumak | 2017-03-19 17:52:33 UTC | #8

Anim xforms won't help you.  Instead, you'll have to know before hand what animation would work best. Algorithm I use is to compare the character's rigidbody capsule orientation or its forward direction, via GetDirection(), and compare that to the ragdoll's head node direction from the hip node. If the two are in the same direction, I use getupfromFront animation, otherwise use getupfromBack anim.  Of course you can add more getup animations, such as getupfromRight and getupfromLeft, and make it more elegant.

-------------------------

slapin | 2017-03-19 20:18:44 UTC | #9

Thanks a lot for your sharing, will look into this as next task.

-------------------------

