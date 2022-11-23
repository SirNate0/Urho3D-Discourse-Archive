Marcin | 2017-10-20 08:55:06 UTC | #1

Hi,
What is the simplest way to detect collisions between two any meshes? Without any physics, only detect collisions in every simulation step, with information which objects have collisions.
Is there any way to set distance (a margin) to detect a collision?

Thanks in advance,

-------------------------

Bananaft | 2017-10-16 08:26:24 UTC | #2

Even If you don't want actual physical interations, you can use Bullet for just the collision detection. And I belive that's what you should do.

-------------------------

Marcin | 2017-10-16 12:00:00 UTC | #3

Thank you for answer. I tried collision detection from sample 18_Characted_Demo. If I set SetUseGravity(false) for my objects and subscribe to E_NODECOLLISIONSTART then I have almost what I want. Gravity does not work, I have a collision notification, but Physics is still blocking me from programically move one object into another. How to completely turn off physics, leave only collision checking?

-------------------------

Eugene | 2017-10-16 12:09:57 UTC | #4

Have you tried to mark your object as Trigger?
However, I don't know whether the triggers are colliding with each other.

-------------------------

Bananaft | 2017-10-16 12:16:56 UTC | #5

Trigger should work. If it does not, or you have some other motion related issues, you can also try turning on Kinematic mode for your rigid body.

-------------------------

Marcin | 2017-10-16 12:48:22 UTC | #6

If I mark objects as Trigger, it is ok if I set setBox() for CollisionShape. But if I set SetTriangleMesh() for CollisionShape, and mark objects as triggers , then the collision notification will stop working. Turning on Kinematic mode for rigid body does not help.

-------------------------

Eugene | 2017-10-16 12:58:05 UTC | #7

Triangle meshes and heightfields couldn't be dynamic. Does other shapes work?

-------------------------

Marcin | 2017-10-16 13:07:31 UTC | #8

Yes, other meshes work (sphere, capsule itd). So, is it not possible to do it with only triangle meshes (for example mushroom objects)?

-------------------------

Eugene | 2017-10-19 05:34:27 UTC | #9

There are two shape types except trimesh (ConvexHull and GImpactMesh) that have model as input. Try them.

-------------------------

Bananaft | 2017-10-16 20:54:02 UTC | #10

Why you need tri-meshes exactly? Can you give more specific info on what you are trying to do?

Is it two meshes like static level and some entity in it, or it's several movable meshes?

-------------------------

Marcin | 2017-10-17 07:49:39 UTC | #11

I need Tri-Mesh because i have one irregular body and several other U-shaped bodies. The first body is similar to the capsule, but it has a lot of irregular elements on the surface. I need to know when this first body is in collision with any of the U-shaped bodies, but  I can not simplify the shape very much, I must have high accuracy. All meshes are static, I only programmatically change the position of the first object, but no object uses the mechanisms of physics etc. But now it's ok, I set the first body as ConvexHull and the U-shape bodies as Tri-Mesh (I can't set them as convexhull because it simplifies the model and fills the space) and it works ok. I have a question if I can somehow detect the closest distance to a collision? If there is no collision but it is close, how to check the distance?
Thanks in advance.

-------------------------

Bananaft | 2017-10-19 05:34:27 UTC | #12

Remember that you also can use compound shapes if convex hull is not enough.

There is no easy way to get closest distance between two surfaces, I'm afraid. With convexes you can adjust collision margin one step at a time and see if it collides or not.

-------------------------

Marcin | 2017-10-20 07:18:08 UTC | #13

I would like to try use GImpactMesh, is there any example how to use it?

-------------------------

Eugene | 2017-10-20 07:29:11 UTC | #14

Nope, but there is no interface difference between Convex, Trimesh and GImpactMesh except shape type. You set the type, you set the mesh.

-------------------------

Marcin | 2017-10-20 07:37:20 UTC | #15

But there is no GImpactMesh type in CollisionShape.
enum ShapeType
{
    SHAPE_BOX = 0,
    SHAPE_SPHERE,
    SHAPE_STATICPLANE,
    SHAPE_CYLINDER,
    SHAPE_CAPSULE,
    SHAPE_CONE,
    SHAPE_TRIANGLEMESH,
    SHAPE_CONVEXHULL,
    SHAPE_TERRAIN
};

-------------------------

Eugene | 2017-10-20 08:30:12 UTC | #16

I've added this shape type about a month ago. Use fresh master revision.

-------------------------

