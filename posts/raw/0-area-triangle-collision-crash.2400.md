Sir_Nate | 2017-01-02 01:15:12 UTC | #1

If you have a (fuzzy) 0 area triangle in your collision mesh and something collides with it, you end up with a crash (an assert with debug mode, presumably a divide by 0 error with release). Is there a way to validate the meshes, either during load, or during model export (from Blender, using the plugin), or, preferably, a tool to remove all of these triangles (and then re-save the model)?

-------------------------

Lumak | 2017-01-02 01:15:14 UTC | #2

Degenerate triangles are flushed out in Assimp, not sure about blender (ok, obviously it doesn't).

Edit: let me add that creating a separate convex hull of a model for collision might be better suited for performance, or use SHAPE_CONVEXHULL.

-------------------------

godan | 2017-01-02 01:15:14 UTC | #3

I've actually triggered this crash with a Raycast Query against a mesh that defines a line (i.e. only has two points). Not sure what to do about it though...

-------------------------

Lumak | 2017-01-02 01:15:14 UTC | #4

Some options:
1) write a custom collision derived from btEmptyShape class and modify parts of Bullet for a line collision
2) if in 2D space: convert 2 points of a line into a quad 
3) if in 3D space: a long skinny box?

edit: scratch these ideas. The more I thought about this, the more I became confused as to how you have a mesh that defines a line. My guess is that the mesh is dynamically created at run time which results in a line.

-------------------------

