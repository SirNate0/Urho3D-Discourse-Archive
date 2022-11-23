Enhex | 2017-01-02 01:08:20 UTC | #1

[color=#BBBBBB]It seems it takes CustomGeometry at least a frame after creation before it's loaded.

My problem is that my monster AI can see the player at the start of the level because CustomGeometry doesn't take effect immediately.

Is there a way to ensure CustomGeometry takes effect instantly?
Or instead wait for CustomGeometry to be fully loaded?
Would using a Model instead solve this problem?[/color]

EDIT:
The AI uses physicsWorld raycast to see the player.

It happened because I created RigidBody before CollisionShape(s).
In the case of creating them in the wrong order like I did, using RigidBody::ReAddBodyToWorld() also fixes the problem.

BTW is the requirement for creating the component in ordered documented?

-------------------------

