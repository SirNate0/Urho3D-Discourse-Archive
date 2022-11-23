fnadalt | 2018-09-21 13:30:48 UTC | #1

Hi!
I have this "world" project. I'm trying to implement right now item grabbing. The method I'm experimenting with is: parent a node to a hand bone node. That works fine. The item has a rigid body and a cylinder shape. When "grabbed", rigid body is disabled. The problem comes up when reparenting the item node to scene. Physics messes up. What makes the difference is the position and rotation setting when reparenting to the hand; if commented out, physics works, but the item is not properly "held" in the hand. Help please.

Project:
https://drive.google.com/drive/folders/1chko8MpacAUgmSWMnhY0dTEI18wkmxX_?usp=sharing

"Grab" code: Character.as:105.

-------------------------

Bananaft | 2018-09-24 08:13:13 UTC | #2

Some thoughts:
1.) try setting linear and angular velocity to zero.
2.) try calling ResetForces() method for rigid body.
3.) rigid body has it's own position and Quaternion rotation log them out and see if they are properly updated the moment you reenable your rigid body.

-------------------------

fnadalt | 2018-11-14 17:05:05 UTC | #3

Well, I made wome experiments for grabbing arbitrary objects:
1) reposition grabbed object following hand node, at FixedUpdate
2) parenting grabbed object to hand.

objects are grabbed by pressing CTRL while colliding with them. There's a stick to be grabbed inside the house.

The first method works moderately well, needs some tweaking to avoid jittering.
The second works excellent when grabbing the object, but when dropping it the physics state seems to have been "frozen" at previous worldTransform and is buggy.

Neither of them works over networking...
Check bin/Data/Scripts/Person.as

Help!

https://github.com/fnadalt/World

-------------------------

