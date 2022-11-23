Lumak | 2017-01-02 01:11:30 UTC | #1

Just implemented NVRayTraverse into Urho3D and did a quick raycast time comparison:
-4 static models, total of 2348 triangles

NvRay time = 96 usec.
Urho time = 338 usec.

Just thought I'd share this info.

-------------------------

Lumak | 2017-01-02 01:11:30 UTC | #2

Let me add the test was a CPU ray test using NVRayTraversal. I stripped out everything CUDA.

-------------------------

weitjong | 2017-01-02 01:11:30 UTC | #3

Impressive improvement. Any links you can share? Thanks.

-------------------------

Lumak | 2017-01-02 01:11:30 UTC | #4

[url]https://code.google.com/archive/p/understanding-the-efficiency-of-ray-traversal-on-gpus[/url]

I also stripped out everything GL, so essentially just left CPU ray code.  Just wondering how fast the GL ray cast would be...

Edit: oh, the irony. What I ported is gpu-ray-traversal but implemented gpu-less-ray-traversal.

-------------------------

cadaver | 2017-01-02 01:11:35 UTC | #5

Sounds impressive. Nvidia's code seems permissively licensed so if your modifications don't break Urho's octree usability in general, a PR would be super to see.

-------------------------

yushli | 2017-01-02 01:11:35 UTC | #6

That sounds like a nice performance improvement. Look forward to having it in the main branch soon.

-------------------------

Lumak | 2017-01-02 01:11:36 UTC | #7

[quote="cadaver"]Sounds impressive. Nvidia's code seems permissively licensed so if your modifications don't break Urho's octree usability in general, a PR would be super to see.[/quote]

I wouldn't mind submitting this for PR, but I'm not sure if Nvidia's BVH is actually fit for a game.  It might be better suited as a tool.  Let me explain. 
I specifically integrated Nvidia's BVH for the purpose of implementing SH Lighting that requires a ton of ray casting.  To give you a ball park, it requires casting a ray for each sample per vertex.  My sample size atm is 400, 1335 verts in the scene, and doing over half million ray casts for just what the author calls "shadowed diffuse transfer" but basically AO.  I'm currently implementing the third technique which would require about another 1/4 million ray casts.

So, with so many ray casts required the BVH saves time compared to urho's octree.  There are some cons with BVH:  it takes 10 seconds to build BVH (only with 2348 triangles), and I don't think you can insert/remove polygons at runtime - I load everything up front before building the BVH.

Still interested in seeing it?

Edit: I had a quick look and verified that there are no methods to insert/remove polygons in BVH once it's built.
-

-------------------------

cadaver | 2017-01-02 01:11:36 UTC | #8

Ok, then I understand, it's not generally usable for the realtime octree & raycasts Urho currently uses. I thought it was just about implementing the ray-triangle intersection in the existing octree better. From my side, no need to submit a PR.

-------------------------

