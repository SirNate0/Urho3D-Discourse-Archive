Enhex | 2017-01-02 01:07:24 UTC | #1

Does RigidBody interpolates it's position?
I tried to make a kinematic character controller which sets its position manually, and without vsync I get a motion stutter every once in a while for few seconds, as if it's going out of sync.

If that's the reason is there a way to manually interpolate the rigidbody position over render frames, like a normal rigidbody?

-------------------------

sabotage3d | 2017-01-02 01:07:24 UTC | #2

I think you can set the position only for passive rigid bodies for active you would need to set the velocity with setLinearVelocity .

-------------------------

Mike | 2017-01-02 01:07:24 UTC | #3

Did you set your body as kinematic?

-------------------------

Enhex | 2017-01-02 01:07:24 UTC | #4

[quote="Mike"]Did you set your body as kinematic?[/quote]
Yes. Tho it also happens when I have non-kinematic body with manual velocity using SetPosition()

-------------------------

Enhex | 2017-01-02 01:07:24 UTC | #5

On [urho3d.github.io/documentation/H ... ysics.html](http://urho3d.github.io/documentation/HEAD/_physics.html) it says:
"When the rendering framerate is higher than the physics update rate, physics motion is interpolated so that it always appears smooth."

Does it happen in Urho or Bullet?
It appear Bullet's MotionState doesn't update non-moving objects:
[bulletphysics.org/Bullet/BulletF ... State.html](http://bulletphysics.org/Bullet/BulletFull/classbtMotionState.html)
I guess that non-moving means 0 velocity.


EDIT:
Currently fixed it by manually interpolating the position.

-------------------------

