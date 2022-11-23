1vanK | 2017-01-02 01:11:20 UTC | #1

How to make platform that allows to moving up but deprecate to movig down?
[youtube.com/watch?v=-80t-OV1gQ8](https://www.youtube.com/watch?v=-80t-OV1gQ8)
[docs.unity3d.com/Manual/class-Pl ... tor2D.html](http://docs.unity3d.com/Manual/class-PlatformEffector2D.html)

It is possible for Bullet and Box2D? Or it's needed to implement this logic manually?

-------------------------

Enhex | 2017-01-02 01:11:20 UTC | #2

Maybe you could filter collision according to collision normal.

-------------------------

Lichi | 2017-01-02 01:11:27 UTC | #3

You can create two collision shapes, one on top and other down of the player. When if the platform collision touch the collision shape on top, you disable the collision shape of platform.
Other way is disable all collisions shapes of platforms that are above.  :smiley:

Also you can traslate the player up when is in collision.

-------------------------

Modanung | 2017-01-02 01:11:27 UTC | #4

Something like changing collision masks based on player/character/object movement might work. Combined with a separate feet collider that's basically a horizontal line to make intersection avoidable when changing the mask.

-------------------------

