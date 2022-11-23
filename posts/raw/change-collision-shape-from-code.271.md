rifai | 2017-01-02 00:59:17 UTC | #1

I want to make wave collision shape. My shape needs to be changed every frame. I want to calculate every vertices position and assign to my collision shape. 
Is there any way to do this? I don't find this in samples.

Thanks  :smiley:

-------------------------

friesencr | 2017-01-02 00:59:17 UTC | #2

I don't know how do this either.  Have you tried using SetCustomConvexHull on the CollisionShape?  It takes a CustomGeometry which gives low level access to the geometry.  I don't know the caveats of doing this.  I am sure there are.

-------------------------

cadaver | 2017-01-02 00:59:21 UTC | #3

Convex hull will likely not encapsulate the proper shape of the wave mesh, as it "wraps" it completely.

A similar SetCustomTriangleMesh() function compared to SetCustomConvexHull() could be added. However the CustomGeometry component is inefficient for per-frame changing data; I'd rather recommend getting comfortable with modifying a Model resource's vertex buffers directly (the model may be loaded from disk, or created programmatically, doesn't matter) in which case you can call SetTriangleMesh() repeatedly. This kind of update is basically "pulling the rug" from under the physics system repeatedly and it will not be able to use any time continuity in the collision detection, so I'd expect poor performance, and possibly misbehaving collision.

Note that there's a physics geometry caching feature which tries to use cached data for a model if possible, and you'll need to circumvent the caching by either making the vertex buffer dynamic, or calling

[code]physicsWorld->RemoveCachedGeometry(model);[/code]
each time before updating.

-------------------------

rifai | 2017-01-02 00:59:21 UTC | #4

Thanks for reply. 
I try the modifying vertex buffer directly from imported model. Problem's solved. 
But new wild problems appear. :smiley: 
Maybe, I will ask another question in new thread.

-------------------------

