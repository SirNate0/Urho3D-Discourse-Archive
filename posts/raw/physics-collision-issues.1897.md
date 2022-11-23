dvan | 2017-01-02 01:11:19 UTC | #1

Been playing with these issues for about a month and I've not been able to get collisions to work reliably.

Simple test program (effectively 2D) with a bouncing ball rebounded off walls, and a paddle to hit it with. I've used both Box2d and Bullet physics and gotten different results depending upon which problem I've focused on.

1. Ball falls through wall (floor). This is a Dynamic item hitting a Static one. This works as it should with Box2D (never fails), but not Bullet. As the small ball gains speed (increasing through Restitution settings) it will eventually miss the floor and fall through. Tried all the settings I could find (like CCD, etc.) and other collision fixing things from wiki, but nothing matters.

2. Paddle (fast moving) fails to hit ball (even when standing still). This is a moving non-Dynamic item hitting a usually moving Dynamic one. This fails in both Box2D and Bullet. Paddle is moving under user control.

Right now I'm mostly focused on Bullet since if it works there I can make it work everywhere.

I know size and speed can mater, but I've intentionally keep it small and fast while testing things. Seems like this is a basic issue that should have been solved within the libraries years ago. Most of the related web references I've found seem rather old.

Any clues would be helpful, since I'm at a loss.

-------------------------

Enhex | 2017-01-02 01:11:19 UTC | #2

Are you using triangle meshes or convex hulls?

-------------------------

dvan | 2017-01-02 01:11:19 UTC | #3

No. As simple as it can get, A sphere and some box's.

-------------------------

Enhex | 2017-01-02 01:11:19 UTC | #4

What sizes? Bullet wiki recommends to keep objects size betwee 0.05 and 10:
[bulletphysics.org/mediawiki-1.5. ... _The_World](http://bulletphysics.org/mediawiki-1.5.8/index.php/Scaling_The_World)

-------------------------

gawag | 2017-01-02 01:11:20 UTC | #5

For thin or fast things you may need to use (additionally) ray tracing: [github.com/urho3d/Urho3D/wiki/H ... h%20things](https://github.com/urho3d/Urho3D/wiki/How%20to%20fix%20a%20fast%20object%20not%20colliding%20with%20things)?
Had that issue with a player running against a trimesh wall, sometimes it didn't collide and got stuck inside the trimesh "hull".

-------------------------

dvan | 2017-01-02 01:11:20 UTC | #6

Enhex, ball is 0.32 and probably scaled a little smaller, so don't think things got too small in normal testing. Thanks for the link though, may explain some other inconstancies I noticed in the bullet gravity simulation.

Interestingly from what I could tell, Bullet only seems to use the surface for detection so the size may not mater in this regard (a bigger ball did perform better, as long as physics rate chance caught it on the line). Box2D does seem to be able to respond to "inside the box" (didn't test this directly) which might explain why it does much better with problem #1.

gawag, tried that and a bunch of other gyrations like it. Nothing worked with any consistency. Tried a few of my own version of AABB to no avail, but could be I missed some things on it. Best I got was to program a partial detection on 1 of the specifics of my situation, but to go down that road I might as well forget physics and just do it all manually (could get way too busy down the road and kind of negates the advantage).

At 1 point I did a quick bouncy ball #1 test with Unity and UE4. Unity failed. UE4 always worked, but it's a bloated monster I can't seem to get my head around. Not sure what Unity uses. Think UE4 uses PhyX or such. Don't know if either has tweaked their physics.

-------------------------

Enhex | 2017-01-02 01:11:20 UTC | #7

What CCD parameters did you use?

-------------------------

dvan | 2017-01-02 01:11:21 UTC | #8

Tried all kinds of settings from 0 - 10 on the 2 main params, and also tested others that should not directly relate. What settings should work?

-------------------------

Enhex | 2017-01-02 01:11:22 UTC | #9

[quote="dvan"]Tried all kinds of settings from 0 - 10 on the 2 main params, and also tested others that should not directly relate. What settings should work?[/quote]
Try half the size of the object.

-------------------------

dvan | 2017-01-02 01:11:22 UTC | #10

Thanks!  That was helpful for problem #1. Variance between 1/2 size+- the other 1/2 seems like the valid range mostly. At first try I lost the Restitution, so will have to look into that more detailed. Did about 50 gyrations with about 10-15 params on a few things and had some success, but not on all. Seems to trade off on detection vs. restitution at some levels, but think I at least appeared to have full detection on some combo's. I'll run a few 100 more tests in more systematic ways to verify and see if I can get it to balance.

Didn't notice any big change on problem #2, but not really focusing on it right now.

-------------------------

Enhex | 2017-01-02 01:11:22 UTC | #11

For #2 are you having CCD on the paddle too? I imagine it wouldn't work well because AFAIK CCD is based on position and not rotation.
maybe if you rotate it NOT around the center that would count as moving.

-------------------------

dvan | 2017-01-02 01:11:33 UTC | #12

Giving up on this for now, at least with Bullet. Other things to do.

Can't get Bullet to make it work in any reliable way. Short version is.. as it speeds up (via Restitution), it will eventually punch through. Some settings would cause Restitution to inconsistently slow down on some bounces (thus never bounce through), but that defeats the purpose.

Thanks for the feedback.

-------------------------

Enhex | 2017-01-02 01:11:34 UTC | #13

You could use shpere casting instead of a rigid body to make sure you don't tunnel anything. You'll need to handle bounces and gravity manually.

-------------------------

