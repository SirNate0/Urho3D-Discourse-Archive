rogerdv | 2017-01-02 01:01:19 UTC | #1

Yesterday I was learning to use navigation mesh and path finding and noticed that some scene nodes were not included in the navigation data. After comparing the nodes included with the nodes ignored, I found that the ignored nodes had a collision shape. Is this behaviour correct?

-------------------------

cadaver | 2017-01-02 01:01:19 UTC | #2

You will have to debug inside NavigationMesh::CollectGeometries to see what's actually happening. The behavior is supposed to be such that for each node, it should actually prefer to take the physics geometry if it can (box, trianglemesh or convexhull collision shape) and if it can't, take the visible drawable geometry.

-------------------------

