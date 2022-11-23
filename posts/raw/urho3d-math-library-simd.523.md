sabotage3d | 2017-01-02 01:01:05 UTC | #1

Hello,

I big performance optimization will be adding SIMD support in Urho's math library for  Dekstop [b] SSE[/b]  and for mobile [b]ARM NEON[/b] .
There are some libraries already supporting the majority of SIMD like Eigen: [eigen.tuxfamily.org/index.php?title=Main_Page](http://eigen.tuxfamily.org/index.php?title=Main_Page)
I have used Eigen before and I can say its performane is the best compared  to others open source math libraries. 
Now the license is more loose and extensions are easy to make.

These are some tests that I did on my ancient Q6600 with SSE enabled :

[code]Testing Eigen library Matrix4f class.
Performing additions.
Took 30 milliseconds.
Performing multiplications.
Took 94 milliseconds.
Testing GLM library Matrix4f class.
Performing additions.
Took 133 milliseconds.
Performing multiplications.
Took 616 milliseconds.
Testing CML library Matrix4f class.
Performing additions.
Took 186 milliseconds.
Performing multiplications.
Took 1136 milliseconds.
Testing Imath library Matrix44 class.
Performing additions.
Took 139 milliseconds.
Performing multiplications.
Took 432 milliseconds.[/code]

-------------------------

silverkorn | 2017-01-02 01:01:06 UTC | #2

Just something I've seen earlier;
Maybe it's not at the same level but I share it just in case :slight_smile:
[url=http://libtom.org/?page=features&newsitems=5&whatfile=tfm]TomsFastMath[/url]

-------------------------

sabotage3d | 2017-01-02 01:01:07 UTC | #3

Nice one but seems to be missing ARM NEON which is bad for the mobile developers :slight_smile:

-------------------------

sabotage3d | 2017-01-02 01:01:13 UTC | #4

If anyone is interested I can port Eigen to be compatible with Urho3d's math library ?

-------------------------

codingmonkey | 2017-01-02 01:01:13 UTC | #5

Guys, somebody knows is Urho3D uses here such optimization for transformations ?
[research.scee.net/files/presenta ... CAP_09.pdf](http://research.scee.net/files/presentations/gcapaustralia09/Pitfalls_of_Object_Oriented_Programming_GCAP_09.pdf)

-------------------------

cadaver | 2017-01-02 01:01:13 UTC | #6

No, Urho3D is your basic object oriented rendering engine, where transformation data is contained in scene node & drawable component objects, and it doesn't apply well to data-oriented optimizations, as well as getting the maximum out of SIMD, without significant refactoring. There are always tradeoffs involved, for example in Urho3D application logic you're always able to move scene nodes and request their updated world transforms any time, which are lazy-evaluated as necessary. An optimization-focused engine might calculate the world transforms once per frame within a tightly optimized loop, in which case the updated world transforms would not be immediately available.

-------------------------

sabotage3d | 2017-01-02 01:01:14 UTC | #7

So you think it is hard to port Eigen to Urho. I think it is just a matter of redoing the same functions in Eigen that exists in Urho and including them. It is pretty straightforward as Eigen supports both column-major and row-major matrices, it also supports conversions to arrays. Eigen also does lazy evaluation: [eigen.tuxfamily.org/dox/TopicLazyEvaluation.html](http://eigen.tuxfamily.org/dox/TopicLazyEvaluation.html)

-------------------------

cadaver | 2017-01-02 01:01:14 UTC | #8

I answered codingmonkey's question and didn't comment at all on the feasibility of replacing the math library. You probably misunderstood what I meant with lazy evaluation in that context. I meant it in terms of "has the world transform changed? If yes, recalculate it when it's being asked."

-------------------------

codingmonkey | 2017-01-02 01:01:14 UTC | #9

[b]cadaver[/b], thanks for the quick reply, that's all I wanted to know.

-------------------------

OvermindDL1 | 2017-01-02 01:01:18 UTC | #10

As I understand it Bullet has one of the most optimized math libraries of anything, so calling those when available would be useful.  Otherwise I have used Eigen and I highly recommend it as well.

-------------------------

sabotage3d | 2017-01-02 01:01:20 UTC | #11

As far as I know Bullet is not SIMD optimized on Android, also its library is very limited in terms of functionality.

-------------------------

OvermindDL1 | 2017-01-02 01:01:20 UTC | #12

[quote="sabotage3d"]As far as I know Bullet is not SIMD optimized on Android, also its library is very limited in terms of functionality.[/quote]
It is limited yes, unsure about the Android optimization on it, but for the bits it does have its speed is hard to beat.  Eigen is still a very good library, one of the best.

-------------------------

boberfly | 2017-01-02 01:03:45 UTC | #13

Hi all,

What Cadaver is saying is that an SIMD math lib won't get you massive performance gains if your code logic causes lots of cache misses, like Urho3D will do going through many objects in a loop which evaluate transforms from that object. You will only get significant gains if you have massive arrays of data that are piece-meal'd in small structure of arrays in a tight loop that fits in CPU cache and you need to do some math logic on it (the blendshape blending comes to mind, or if you want to do CPU skinning or a cloth sim, stuff like that would be the easiest to apply SIMD onto).

Another suggestion is to use intel's ISPC for these tasks, which could run on Urho worker threads as well. There's a NEON backend also for ARM.

I think Turso3D would benefit from a lot of this stuff more than Urho3D would, outside of optimising blendshapes or making your own animated mesh which stores its own bones into simple matrices instead of using bone objects, losing flexibility in the process eg. attaching ragdolls to it or applying IK or some constraints.

A future thought in these cases would you cater for the majority/simplest case and then just do 'smart/slow' logic to the bones/nodes which actually do need them? Perhaps using masks to know which of those are. Bonus points if this system is seamlessly done low-level without the high-level needing to deal with it.

-------------------------

boberfly | 2017-01-02 01:03:45 UTC | #14

[quote="sabotage3d"]As far as I know Bullet is not SIMD optimized on Android, also its library is very limited in terms of functionality.[/quote]

[bullet.googlecode.com/files/bul ... ev2531.zip](https://bullet.googlecode.com/files/bullet-2.80-rev2531.zip)

Look in Extras/PhysicsEffects for NEON SIMD support for Bullet. I've not used it but it looks like a different physics engine to me, I'm curious to see how this integrates/replaces the mainline Bullet lib, with threading also.

-------------------------

cadaver | 2017-01-02 01:03:45 UTC | #15

Thanks boberfly for the explanations, that basically sums up very well where SIMD will get the most benefit.

As for Turso3D, it did end up being quite similar to Urho, that it's still an object-oriented scene graph. The point about flexibility vs. performance vs. ease-of-use is quite critical; lately I've seen some engine API's that go really far to support a data-oriented approach, but in doing so they actually present a quite "hostile" API to the user, for example you may not be free to reconfigure a scene sub-graph (reparenting nodes) after creating it, in the interest of maximum performance.

I will probably examine at some point, when Urho's render refactoring is in good shape, whether Turso3D can be modified to become a godlike data-oriented engine which still remains friendly for use. But that's again a bit offtopic and not at all guaranteed.

-------------------------

