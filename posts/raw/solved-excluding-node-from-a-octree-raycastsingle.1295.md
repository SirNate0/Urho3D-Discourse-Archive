Enhex | 2017-01-02 01:06:39 UTC | #1

Is there a way to exclude a specific node from octree RaycastSingle?

With the physicsWorld RaycastSingle you could set the node's body on a temporary collision layer to exclude it.

-------------------------

Mike | 2017-01-02 01:06:39 UTC | #2

The same applies to Octree. Use [url=http://urho3d.github.io/documentation/1.4/class_urho3_d_1_1_drawable.html#ab0a0cb81cefb83249a578069c4adc4d8]SetViewMask()[/url] to manage your layers, and set the viewMask accordingly in [url=http://urho3d.github.io/documentation/1.4/class_urho3_d_1_1_ray_octree_query.html#a6d1faa4a6729eda2ae5866c005631988]RayOctreeQuery[/url]

-------------------------

