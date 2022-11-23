btschumy | 2020-06-15 21:43:27 UTC | #1

This is probably a dumb (non-3D programmer) question but do either nodes or components in Urho3D have a size?  I don't see any mention of it in the somewhat sparse documentation.  

I assume you just use SetScale to change the size on-screen?

How do you know what the size (scale = 1) is of a Component created like:

    var plane = galaxyNode.CreateComponent<StaticModel>();
    plane.Model = CoreAssets.Models.Plane;

Are the dimensions always 1?

If you create a cylinder, is the radius 1 and the height 1?

-------------------------

Eugene | 2020-06-16 08:12:20 UTC | #2

Some components have WorldBoundingBox. This is the closest thing to physical "size" you can get.

-------------------------

btschumy | 2020-06-16 20:51:58 UTC | #3

OK, thanks.  I guess scale is how you do it then.

-------------------------

JTippetts1 | 2020-06-17 10:01:41 UTC | #4

The size at scale=(1,1,1) is determined by how large you model the geometry. It can be modeled at whatever scale you require.

-------------------------

btschumy | 2020-06-17 13:52:18 UTC | #5

But I'm not creating a model and loading it.  I'm talking about using the built-in models.

    var plane = galaxyNode.CreateComponent<StaticModel>();
    plane.Model = CoreAssets.Models.Plane;

The plane seems to have unit length sides.  But what about things like Dome, Torus, Cylinder?  It is not obvious what the default size of this is.  I guess you have to inspect them in the debugger to determine this.

-------------------------

