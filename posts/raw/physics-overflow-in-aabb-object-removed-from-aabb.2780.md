miz | 2017-02-08 11:35:34 UTC | #1

I saw that this was an issue at some point in 1.5, not sure if it is related, I'm getting it with 1.6 only on Raspberry Pi and not consistently. Happening when my player node collides with another object. Any ideas what this could relate to?

-------------------------

miz | 2017-02-11 10:05:29 UTC | #2

It seems it may have been linked to setting restitution to 0 (something that didn't work anyway http://discourse.urho3d.io/t/bouncing-still-happening-even-with-restitution-set-to-0/2176/2)

After setting restitution to 0.1 I'm no longer getting the same problem.

-------------------------

miz | 2017-02-11 10:06:57 UTC | #3


[quote="miz, post:1, topic:2780, full:true"]
After setting restitution to 0.1 I'm no longer getting the same problem.
[/quote]

Actually it's happening again! Must be something else causing it

-------------------------

hdunderscore | 2017-02-11 11:43:48 UTC | #4

Mind giving more details about the issue? You getting a crash or ?

-------------------------

miz | 2017-02-11 15:37:11 UTC | #5

I don't get a crash, the game stays open but the RigidBody gets removed and I can't move the player Node as a result. It  happens on colliding with other collision boxes but only very occasionally and unpredictably. It seems to happen only when my player is sprinting  (this only changes the velocity [3.2 vs. 1.92]) but I'm not sure whether that is just a coincidence at this stage.

It's quite basic movement - I only move the player by using SetLinearVelocity() and this is always just left, down, right or up.

Still trying to find a pattern to narrow it down a bit more.

All collision objects are boxes, no complex shapes.

-------------------------

hdunderscore | 2017-02-12 04:50:18 UTC | #6

Seems strange that a RigidBody component would remove itself, I'd have to see a small example of the problem. Any chance to share some code?

-------------------------

