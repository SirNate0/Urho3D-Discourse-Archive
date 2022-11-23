XCHG | 2020-05-13 19:35:21 UTC | #1

Hi,

This is my first post, so first I would like to thank you guys because Urho3D looks like an awesome engine. :slight_smile:

So, my question is that is there a way to create programmatically a model in Urho3D?
What I want to do is create a model by manually(programmatically) adding vertices to it from C++.  Is there a standard interface in Urho3D to do this?

Thank you very much :slight_smile:

-------------------------

cadaver | 2020-05-13 19:35:13 UTC | #2

Welcome!

The easy, but less optimal way: use the CustomGeometry component. It's similar to Ogre ManualObject or OpenGL immediate mode in that you can define each vertex position, followed by its normal, texcoord, color or anything that's needed. But it limits you to non-indexed geometry and you can't display multiple instances of the geometry you defined, as each CustomGeometry is unique.

The hard way: take a look at how the AssetImporter tool creates a Model object from the data it reads from the AssImp library. This involves creating VertexBuffer & IndexBuffer objects and filling them with data, plus creating the Geometry object(s) that refer to these buffers and define a draw range. Once done, you could assign that Model to for example a StaticModel component to display it.

-------------------------

XCHG | 2017-01-02 00:58:32 UTC | #3

I suspected that I need to go low level after I took a look at the documentation.
Thanks for the precise directions on how to do that.

-------------------------

JoshuaBehrens | 2017-01-02 00:58:53 UTC | #4

I asked myself the same question and just read this thread. Now I have an other question related to the answer in this thread so I just post it in here.

Is there no way to put a CustomGeometry in the assets-list by code?

-------------------------

cadaver | 2017-01-02 00:58:53 UTC | #5

There is currently no built-in function, but this would be just a matter of taking the CustomGeometry vertex buffer, creating an "identity" index buffer and the Geometry object, and constructing a Model resource from those (which could be either retained in memory, or saved to disk.) This would be similar to Ogre's ManualObject::convertToMesh().

-------------------------

jamies | 2020-05-04 15:22:48 UTC | #6

Are the answers here still valid, or are there other better ways to create manual geometry?

What about physics and collisionshape? I've already successfully used btTriangleIndexVertexArray with bullet, but I don't know if Urho3d does it already.

-------------------------

