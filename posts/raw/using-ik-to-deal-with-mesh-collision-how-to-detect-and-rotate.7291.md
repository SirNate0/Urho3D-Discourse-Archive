hunkalloc | 2022-07-01 22:18:42 UTC | #1

Hey y'all. I'm working on a small prototype to get my head around the engine and I was pleasantly surprise to know that it has built-in IK functionality, something that you have to pay for in Unity. I've been trying to implement a feature similar to this one:

https://www.youtube.com/watch?v=NWkLYcgMxUA

You'll notice that, instead of using multiple cameras to avoid the weapon mesh from going through the walls, the dev team of Escape From Tarkov decided to turn this into a gameplay feature and have the muzzle go up by using IK on the player hand/elbow. 

The way I implemented this was, when there is a collision, I play an animation that basically makes the player go high ready, and prevent the shoot() method from ever working. However, I would love to be able to use IK, since that would be much smoother than be just playing the animation every single frame that I detect a collision, then playing the "back to aiming" animation. It feels laggish.

My question is around the rotation of the bone itself. When there is a collision, can I just go directly to the bone of the player and apply a 70 degree rotation, for example? How does the IK "activate"?

-------------------------

JSandusky | 2022-07-02 01:46:38 UTC | #2

In this case you would likely set up 2 IK chains containing shoulder, elbow, and wrist (end effector), then keep updating the target position as you move the hand nodes around by the wrist. For this gun case you'd basically determine where the gun needs to be and then position the hands where they need to be according to whatever relative coordinates (ie. `wristOffsetMatrix = inverseOldGunWorldTransform * wristWorldTransform; newWristWorldTransform = newGunWorldTransform * offsetMatrix;`), then it doesn't matter WTF you do with the gun, the hands are going to stay attached and your arms will track through their IK so long as you don't go outside of reach.

The IK is rotationally clueless, it only solves the rotations to position the points and nothing else like easing an rotation axis through the chain etc. If you look at the 45_InverseKinematics sample you can see that the sample has to explicitly deal with the foot orientation.

---

As to getting the contact information to reposition the weapon. Your best bet is going to be to use a Node user-variable (`Node::GetVar` and `Node::SetVar`) to store the the world-transform of the node at the end of the frame.

When updating you'll do a `PhysicsWorld::ConvexCast` from the old position to the new position and use the contact information you get from that to decide how to correct position to resolve penetration. Then repeat the casting process until you've solved all penetrations or have hit a set limit. It's the same task as a character controller (`outMuzzlePosition = inMuzzlePosition - contactNormal * inMuzzlePosition.DotProduct(contactNormal)`), your character is now just the muzzle of a gun that you're sliding along the surface.

-------------------------

