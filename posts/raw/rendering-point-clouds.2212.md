sabotage3d | 2017-01-02 01:13:57 UTC | #1

Hi guys,

I am trying to render a large point cloud data. I tried using Billboards but the textures and the quads are too expensive they are killing my performance. Is there a way to use GL_POINTS or other OpenGL point primitive in Urho3D to render dense point clouds?

-------------------------

godan | 2017-01-02 01:13:57 UTC | #2

I'm pretty sure you can specify POINT_LIST in Geometry::SetDrawRange(). However, I have not quite gotten this to work correctly (although I use the same procedure all the time for drawing curves with LINE_STRIP).

If you get it working let me know :wink:

-------------------------

godan | 2017-01-02 01:13:57 UTC | #3

Just read that you are dealing with point cloud data. You might have to split the cloud up in to to groups of points - then the Scene's Octree will kick in and should improve performance. That's the theory at least.

-------------------------

sabotage3d | 2017-01-02 01:13:57 UTC | #4

Is there a good way of passing OpenGL primitives to Urho3D at the moment?

-------------------------

