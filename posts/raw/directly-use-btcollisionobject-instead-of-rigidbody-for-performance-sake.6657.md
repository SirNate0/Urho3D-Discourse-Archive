CE184 | 2021-01-11 07:35:22 UTC | #1

I am testing a large scene with thousands of objects moving around.

Each object includes model, material, crowd nav agent. The frame rate is okay.
However, when I tried to add RigidBody to each object, the frame rate drop hugely. Even if the collision_mask is 0 and mass = 0 (static rigidbody, collide with nothing). I only need those rigidbody (collision shape) for raycast detection. So I believe it's wasting a lot of CPU running some unnecessary physics calculation (since there is no raycast added for my test scene).

I searched a little bit about bullet physics and found [this post](https://pybullet.org/Bullet/phpBB3/viewtopic.php?p=13023&sid=11f3a1ba6d3eb322fed1b625a5fa7da2#p13023). It is suggested to use btCollisionObject directly instead of btRigidBody for such cases. People confirmed this could save a lot of memory.
I believe this is the solution for my problem, but I could not find direct usage of btCollisionObject in Urho3D. 
I am thinking to add one custom component Urho wrapper for it. I was wondering if anyone has done something similar so I don't need to do it? or any thoughts?

-------------------------

throwawayerino | 2021-01-11 13:08:22 UTC | #2

Are you adding physics just for raycasting? Unless I'm misunderstanding, what prevents you from using octree casts?

-------------------------

CE184 | 2021-01-12 05:28:17 UTC | #3

Maybe because it's not drawable? That's a good question though.
For example, here I have thousands of collision shape (mostly capsule), they are body parts for each objects. During the combat, lots of raycasts are used to detect those weapon hits.

From your suggestion, I could think a way to make dummy drawables for those collision shapes. But I am not sure if there is any issue for that. We definitely will not render them, but will the octree include them for raycast if it's invisible? or do we have LOD/cull mechanism that causes inaccurate result?

The reason why I used rigidbody in the first place is that if the object is hit and dead, I instantly enable the rigidbody so the ragdoll can kick in very easily. But my real requirement is as discussed above: thousands of capsules and hundreds of weapon raycast segemnts each frame to detect hits. What's the best way to deal with that in Urho3D in the performance sense?

-------------------------

JSandusky | 2021-01-13 03:18:31 UTC | #4

**Collisions specifically**:

I'd do it in OpenCL. One kernel to bin into a grid and another to test + write the compacted hits+rayID. CPU side you'll just sort the hits for each ray because you probably want the nearest one to the ray origin, not sorting on the GPU will keep you from trying to be clever (and shooting yourself in the foot) since sorting is hard there and you'll likely have a fairly limited number of hits per frame in real cases.

If you only have something like a thousand you can just brute force it in the kernel. Matters of large scale justify the ping-pong with the GPU.

Alternatively, do those tests yourself in the job-system so all threads available can attack it. `btTransformUtil.h` in Bullet contains most of the important math bullet does regarding forces so if there's something you need to replicate you can refer to it (I do recommend using the quaternion_derivative instead of the default, the default is really due to more robotics use of bullet and has a rigor you probably don't need).

-------------------------

