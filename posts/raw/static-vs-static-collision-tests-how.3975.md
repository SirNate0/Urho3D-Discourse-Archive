Dave82 | 2018-02-02 00:05:17 UTC | #1

Hi. I just found out that if both bodies have marked as static (mass = 0.0f) The collision is never reported.Not even if collision mode set to COLLISION_ALWAYS. 

What i'm trying to do is collect colliding bodies with the rigidBody->GetCollidingBodies() but static bodies are always ignored.
How to perform a simple static overlap test between two bodies ? Is it even possible ?

-------------------------

Sinoid | 2018-02-02 16:09:49 UTC | #2

Not out of the box, statics don't collide with each other. You have to use contactPairTest http://www.bulletphysics.org/mediawiki-1.5.8/index.php/Collision_Callbacks_and_Triggers to bypass Bullet's static-static checking.

It has to be done on an explicit pair so you'll need to grab bodies via one of the `GetRigidBodies` volume queries first or know exactly who you want to test.

-------------------------

Dave82 | 2018-02-02 11:23:30 UTC | #4

Thanks ! Now it works.Sort of. I can get all shapes to collide (box vs triangle , box vs sphere , box vs covexHull) but for some reason i can't get the box vs box check to work.The physics debug render shows all the bodies are positioned correctly but no collision is recorded.

-------------------------

Dave82 | 2018-02-02 16:06:54 UTC | #5

EDIT : It works now. It seems that the box should be set to kinematic.I don't know what's the reason behind this but the important thing is it works now.
Thanks !

-------------------------

