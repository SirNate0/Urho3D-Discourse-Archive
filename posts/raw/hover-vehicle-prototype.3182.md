Lumak | 2017-06-01 01:51:55 UTC | #1

Couldn't decide what kind of game to make but decided it'll revolve around some type of physics - hover vehicle prototype: no effects, just demonstrating dynamics. 

Had trouble figuring out how to lock the roll angle during turning. First tried detecting if it exceeded max roll value and resetting to it but that caused wobbling/jittering effect. What you see in the video uses btGeneric6DofConstraint.

https://youtu.be/6UUOi_E_bZ4

-------------------------

coldev | 2017-06-01 04:39:22 UTC | #2

nice demo.. no mans sky urho proto....  :grinning:

-------------------------

Bananaft | 2017-06-01 08:07:07 UTC | #3

You can try separating physics object and visual model. Make physics one to never roll, and make visual model to roll based on physics object turn speed.

[quote="coldev, post:2, topic:3182"]
no mans sky urho proto.
[/quote]

no that's empire strikes back hoth battle.

-------------------------

Modanung | 2017-06-01 08:22:57 UTC | #4

Yea looks nice. I would suggest a non-linear relation between the turning speed and banking amount; put a `Sqrt` or `Pow` somewhere.

-------------------------

Lumak | 2017-06-01 17:24:56 UTC | #5

[quote="coldev, post:2, topic:3182"]
nice demo.. no mans sky urho proto....  :grinning:
[/quote]
Thx. Still working on hovering aspect as it still kinda oscillates up and down a bit, but it'll get there.[quote="Bananaft, post:3, topic:3182"]
You can try separating physics object and visual model. Make physics one to never roll, and make visual model to roll based on physics object turn speed.
[/quote]
That might actually be a lot simpler than using btGeneric6DofConstraint method because it was tricky figuring out how to get around the multiple axis constraint issue.
[quote="Modanung, post:4, topic:3182, full:true"]
Yea looks nice. I would suggest a non-linear relation between the turning speed and banking amount; put a Sqrt or Pow somewhere.
[/quote]
Something similar to using a quadratic curve? That might work, not sure if it still won't result in a jitter at desired max roll angles. Will have to test at some point.

-------------------------

Modanung | 2017-06-02 04:11:57 UTC | #6

[quote="Lumak, post:5, topic:3182"]
Something similar to using a quadratic curve?
[/quote]

Quadratic functions are limited to power-of-two situations by definition, but yea some exponential relation. :slight_smile:
[quote="Lumak, post:5, topic:3182"]
That might work, not sure if it still won't result in a jitter at desired max roll angles.
[/quote]
Well, the idea is that the changes in the effect get less and less towards the extremes.

-------------------------

Lumak | 2017-06-02 16:39:35 UTC | #7

Right, it seems exponential computation might be more common than I expected. I'll need to test it sometime.

-------------------------

Modanung | 2017-06-02 17:26:20 UTC | #8

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/9f0f6a6b54797d364f75ebf4b3e336b2ee15f1f1.png" width="690" height="320">

-------------------------

Lumak | 2017-06-02 19:00:21 UTC | #9

All right, took some time to actually integrate btGeneric6DofConstraint from test code to Urho3D::Constraint class.  Currently, its use is similar to using the
[code]
    btGeneric6DofConstraint(btRigidBody& rbB, const btTransform& frameInB, bool useLinearReferenceFrameB);
[/code]
constructor for the caller. But to get around the multiple axis constraint issue when using btGeneric6DofConstraint class, the 2nd btRigidBody is not static but dynamically created (opaque to the caller)  because its rotation is manipulated at runtime to overcome the axis constraint issue. And current implementation only deals with angular limit.

Anyway, I can create a repo for the integrated Urho3D::Constraint with this addition.  Unfortunately, I cannot post the flyer code since it's based on Unity - it's free to use but I believe there's restriction on posting it as open-source code.
Let me know if anyone is interested in seeing a repo for this.

-------------------------

hdunderscore | 2017-06-04 00:18:40 UTC | #10

Any chance to PR it ?

-------------------------

Lumak | 2017-06-04 16:33:54 UTC | #11

I typically just create my own repo.

-------------------------

Lumak | 2017-06-20 18:49:50 UTC | #12

Projectile and explosion testing. I'm posting this because when others post their game progress, it inspires me.

https://youtu.be/BL8w6UBiJ1M

-------------------------

Lumak | 2017-06-21 18:52:04 UTC | #13

From programmers perspective, I thought the cyan plasma and explosion looked good. Maybe I just don't have an artist's eye.

Does this look better? 
[img]http://i.imgur.com/Kyat59m.gif[/img]

-------------------------

Modanung | 2017-06-21 19:35:32 UTC | #14

How about cyan bullets with a cyan-to-orange explosion? To suggest ignition of the backstop by the bullet.

-------------------------

Lumak | 2017-06-21 20:03:22 UTC | #15

So... you don't like either one?

btw, if you get a chance to implement your exponential forces to lock down rotation, I'd like to see it.

-------------------------

johnnycable | 2017-06-21 20:57:47 UTC | #16

seeing projectiles curving gives a fuzzy feeling imho. Gives the impression shooting is difficult. I'd give them a more straight trajectory, while retaining some curvature for effect...

-------------------------

Modanung | 2017-06-21 21:27:08 UTC | #17

[quote="Lumak, post:15, topic:3182"]
So... you don't like either one?
[/quote]

I like both, but may like 'em mixed up best.

-------------------------

Lumak | 2017-06-21 23:46:18 UTC | #18

johnnycable, projectiles actually do travel in straight path, they just appear to be curving when the vehicle and camera are moving.

Modanung, ah ok. I have very little confidence in art that I make and thought that perhaps both were bad ha.

-------------------------

Lumak | 2017-06-23 08:41:36 UTC | #19

## Stress test

## 100 shooter simulation

On average:
~1600 projectiles in the scene
~200 explosions

edit: added info on other images

[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/721d6f605c795bac31f59b91d5922df6924a8442.jpg[/img]

## 50 shooter sim
~900 projectiles in the scene
~100 explosions

[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/db976c7d161e9ffa0d580a245e48c1f65f58d9c7.jpg[/img]

## 20 shooter sim
~340 projectiles in the scene
~50 explosions

[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/7362d359aca913c0e1a61eb7df160af41a7de242.jpg[/img]

@Enhex you're the only other person that I know that's also doing something with shooting - do these numbers look right to you?

-------------------------

Enhex | 2017-06-22 21:39:41 UTC | #20

Depends on things like hardware, implementation details, and what your game demands.

I'd say keep it simple when first implementing stuff, and only when you have performance issues measure & optimize.

I don't know any implementation details so I can't give you actual tips for optimizing.

-------------------------

Lumak | 2017-06-23 08:43:36 UTC | #21

Right, absolutely. What I was curious about was if you ran a similar stress test and evaluated physics process, and perhaps we could've compare notes.  If you haven't, no big deal as I'm done with this part of gameplay and moving onto my next feature.

edit: er, I wouldn't call it gameplay but implementation, testing and proving that I can have several entities fire projectiles in the game.

-------------------------

Enhex | 2017-06-24 22:59:35 UTC | #22

I did run stress tests, and my bottleneck was the AI raycasts - line of sight checks, path collision, etc.
I provided [segmented raycast](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_physics_world.html#a1905d3a9482589b50ad625a5ac23c5eb) implementation to Urho, which in my case doubled the whole game's FPS.

-------------------------

Lumak | 2017-06-24 23:15:32 UTC | #23

Sorry, that didn't come out right when I said you didn't run a similar stress test which sounds like you ran no stress test because every developer does stress test.

I didn't know about the segmented raycast, thanks for that.

-------------------------

