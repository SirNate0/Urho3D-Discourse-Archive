Gnollrunner | 2018-12-28 12:26:29 UTC | #1

A while back I asked one question here having to do with using Urho3D with my voxel planetary engine. At that time I wasn't sure if it could do everything I wanted so I chose to go ahead and use DirectX 11 for the time being. Now, since I've got the base functionality working, I'm reconsidering using an engine but I've failed to find one that allows the use of double precision. To be more specific I don't need it (or want it) on the GPU, but everything on the CPU (or at least a lot of things) have to be in double. In addition to that I need to be able to handle the physics myself since everything ends up in my own octree as I build a planet. I'm wondering if this will be possible using Urho3D or am I still restricted to a low level graphics library. Thanks in advance.

-------------------------

S.L.C | 2018-12-28 14:05:07 UTC | #2

As far as I know. Urho is built around single precision floats. I doubt you'll be able to make it use double precision without some major changes to the engine.

-------------------------

jmiller | 2018-12-28 14:52:58 UTC | #3

I would just add that where [url=https://discourse.urho3d.io/search?q=double+precision]double precision[/url] has been raised previously, there may be a bit more detail, e.g. by **Lasse**

https://discourse.urho3d.io/t/physics-double-precision/2682/2

-------------------------

Virgo | 2018-12-28 23:50:37 UTC | #4

but urho does have double precision option in cmakelist? :face_with_raised_eyebrow:

-------------------------

weitjong | 2018-12-29 02:40:51 UTC | #5

It could be just an option from one of the 3rd party libs that you are seeing.

-------------------------

S.L.C | 2018-12-29 11:44:12 UTC | #6

That's an option from the Bullet library.

-------------------------

z80 | 2019-03-05 21:51:42 UTC | #7

Hello! I'd like to confirm that Urho3D does can work with Bullet double precision (with Urho3D code base modification in a couple of places to take care of btVector3 and btQuaternion conversion into Urho3D::Vector3 and Urho3D::Quaternion properly).

But it is only limited to dynamics simulation. Urho3D itself stays single precision with this modification.

In Urho3D/Physics/RigidBody.cpp one need to change one line
from "PODVector< **float** > masses(numShapes);" to "PODVector< **btScalar** > masses(numShapes);"
And add "add_definitions( -DBT_USE_DOUBLE_PRECISION )" to UrhoCommon.cmake.

-------------------------

Leith | 2019-03-06 08:05:13 UTC | #8

Awesome information! I recently offered to replace all mention of floats in the Physics classes to use btScalar type instead of float type, but noted that only the underlying Bullet physics objects will benefit. I'm happy to hear someone has already at least tried to integrate double precision!

-------------------------

