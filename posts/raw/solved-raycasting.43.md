GIMB4L | 2017-03-18 23:12:08 UTC | #1

Hey all,

So I tried to implement physics raycasts in my project, but to no avail. I've verified that the ray is pointing in the correct direction, but it just won't hit anything. I've also played with the mask settings, but those don't seem to help either. 

I've noticed that the Ninja demo has working raycasts so that the camera does not collide with geometry, but the only difference I can see between that and my demo would be collision mesh. The ninja demo features a TriangleMesh as the CollisionShape for the playing ground, while my simple building uses a box CollisionShape.

Is there a specific way the physics raycast is intended to be used?

-------------------------

Mike | 2017-01-02 00:57:34 UTC | #2

There are good raycast examples in examples #18 and #15, and in Utilities/Touch either.
Take a look at them and if it still doesn't work, maybe you should post here the piece of code you're using.

-------------------------

GIMB4L | 2017-01-02 00:57:35 UTC | #3

Hey Mike,

I looked at the other samples, and my code is pretty much the same. I'll post it below.

[code]
Ray bulletRay = Ray(cameraNode.worldPosition, cameraNode.worldDirection);
		
PhysicsRaycastResult[] hitObjects = physWorld.Raycast(bulletRay;
[/code]

Could it be that those demos use TriangleMesh for the objects they raycast against?

EDIT: So, I tried switching the CollisionShape type of the models in the demos, and they work fine. It must be my raycast code then.

-------------------------

GIMB4L | 2017-03-18 23:11:56 UTC | #4

Hey, I found the solution to the problem. Don't specify M_INFINITY as the distance. Passing in a non-infinite for the value fixed the problem.

-------------------------

