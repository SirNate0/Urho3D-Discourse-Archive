dragonCASTjosh | 2017-03-17 18:48:19 UTC | #1

I have recently noticed that Bullet has support for soft body physics built into it and feel that it would be a good addition to Urho, I'm not familiar with Bullet or the physics systems in Urho or else i would of given it a shot, but after a little look over the rigid body system in the engine i don't look like to much work for someone with good understanding on the systems. 

I gathered up some Bullet docs that may help anyone who wants to try an implement soft bodies,
btSoftRigidDynamicsWorld: [url]http://bulletphysics.org/Bullet/BulletFull/classbtSoftRigidDynamicsWorld.html[/url]
btRigidBody: [url]http://bulletphysics.org/Bullet/BulletFull/classbtRigidBody.html[/url]

I also found a reference video of soft body physics implemented using bullet:

https://www.youtube.com/watch?v=9sh-D0nejUY

-------------------------

codingmonkey | 2017-03-17 18:48:05 UTC | #2

Hi dragon or josh )
Actually I try to write something like this earlier, but then i drop code for some reason, i'm do not remember why maybe it has been very complicated for me.
i'm fully based on this tutorial when doing my trying of this.
there are some major problems.
1. the mesh must always dynamically update, you recreate it everytime from bullet 
2. the format must contain "pins vertices" array. I do not know how this make with actual model formal (*.mdl). probably for soft bodies need new special file format to do exports from blender or assetimport tool.

https://www.youtube.com/watch?v=d7_lJJ_j2NE

-------------------------

dragonCASTjosh | 2017-01-02 01:06:46 UTC | #3

hi codingmokey

I think it may be worth me having a try using the tutorial see how it ends up, also i feel there is probably an optimisation soft body updates and they are likely to be used in small amounts within games. As for model formats i believe FBX formats can handle soft body data but not sure if assimp imports this data and i am also not sure about mdl. but a new format to support soft bodies don't sound to bad

btw you can call me josh :slight_smile:

-------------------------

Lumak | 2017-03-17 18:48:37 UTC | #4

I thought it would be fun to actually port this (softbody physics) to Urho.

Here is a softbody mushroom vid

https://youtu.be/XkLMAZWaVB8

-------------------------

dragonCASTjosh | 2017-01-02 01:06:47 UTC | #5

[quote="Lumak"]I thought it would be fun to actually port this (softbody physics) to Urho.[/quote]
For some reason i found that so funny the way it wobbles, is the source for that public

-------------------------

Lumak | 2017-01-02 01:06:47 UTC | #6

I can post the code sample on the code exchange, but I have to tell you that it's no where near code complete.  I was only interested in creating a trimesh softbody and that's the only thing that I implemented.  I didn't put any hooks on debug render or add methods like, settransform(), setmass(), etc.

-------------------------

codingmonkey | 2017-01-02 01:06:47 UTC | #7

>Here is a softbody mushroom vid
it's funny )
did you test clothes with pins or maybe something like long hair ?
Is it possible make some part of one solid static mesh as softbody ?

-------------------------

dragonCASTjosh | 2017-01-02 01:06:47 UTC | #8

[quote="Lumak"]I can post the code sample on the code exchange[/quote]
that would be useful.

-------------------------

Lumak | 2017-03-17 19:03:01 UTC | #9

I posted it on the [code exchange](http://discourse.urho3d.io/t/bullets-softbody-physics-example/1319).

@codingmonkey, I didn't try those.

-------------------------

codingmonkey | 2017-01-02 01:06:48 UTC | #10

i'm try to figure out with this.
i look into urho's physics. And i'm do not understand if RigidBody use CollisionShapes component for store it's own colliding shape (various types). 
Is SoftBody still needed to use collisionShapes or some other collider if they just create from btSoftBodyHelpers::CreateFromTriMesh ?
Maybe instead CollisionShape they must use something like SoftBodyShape just for store only they's TriMesh with some adjustments ? 
I mean if Rigidbody every time need his dual component - CollsionShape, in this case I guess that SoftBody needed his dual component SoftBodyShape. 
But again it also maybe all in one, SoftBody just may store own TriMesh in it self, and in this case it don't needed any ****shape dual component.

Also I see in Bullet Examples/SoftDemo.cpp about cutting SoftBody if i'm think right it is slice mesh into pieces ? and these separated parts are falling down if they are sliced or just disappear ?

-------------------------

Lumak | 2017-01-02 01:06:52 UTC | #11

Looking at the btSoftBody.h file, I see that the class inherits from public btCollisionObject and there is a [b]struct Body[/b] which defines a btRigidBody* along with Cluster*.  It looks to me like it creates its own set of collision objects and make use of rigidbodies (all in one, as you mentioned) without having to add any additional collision shape or rigidbody for any of the softbody types.  The [b]void (*demofncs[])(SoftDemo*)[/b] defines all the examples in the softbody demo. I'd trace those init functions for specific examples.

I can see in the cutting demo that it actually cuts part of the mesh which falls and have colliders themselves.

-------------------------

codingmonkey | 2017-01-02 01:06:52 UTC | #12

Also i want to note that there are have some major problems with tbSoftBody for realtime simulation. but all they are solvable i guess.

1. btSoftBody do not weak up after they turn to sleeping. Actual version of Bullet still do not solve this issue. but there are exist path to solve this, and it give boost in performance.
for more details: [code.google.com/p/bullet/issues/detail?id=439](https://code.google.com/p/bullet/issues/detail?id=439)

2. for btSoftBody you will need keep special vertex array to simulate clothes. And map this vertexes into original geometry every Physics tick.
for more details: [bulletphysics.org/Bullet/php ... =9&t=10154](http://www.bulletphysics.org/Bullet/phpBB3/viewtopic.php?f=9&t=10154)

-------------------------

Shylon | 2017-01-02 01:11:02 UTC | #13

Any News on Urho3d Soft-body physics?

-------------------------

bmcorser | 2017-03-17 17:47:58 UTC | #14

I'm interested in this too. Is there a branch somewhere with this partially integrated into Urho?

-------------------------

Modanung | 2017-03-17 19:02:09 UTC | #15

Seen this thread?
http://discourse.urho3d.io/t/bullets-softbody-physics-example/1319

-------------------------

bmcorser | 2017-03-17 19:32:16 UTC | #16

Yeah, a seemingly no-longer-existing branch on GitHub is referenced: https://github.com/MonkeyFirst/Urho3D/tree/sbtest

I wonder if @codingmonkey still has a copy somewhere 😀

-------------------------

Modanung | 2017-03-17 19:59:12 UTC | #17

[quote=codingmonkey]
Yes, probably i also dont have it even on my hdd (
but all code changes (sources) are in this theme - hided by code/spoilers tag.
I also remember last bug with my SB: i have huge offset between visual SB representation and it physic representation.
[/quote]
You could reconstruct a branch with the code in the thread.

-------------------------

