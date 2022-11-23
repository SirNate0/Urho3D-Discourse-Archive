Krathoon | 2017-01-02 01:00:47 UTC | #1

Is there a way to adjust the collision shapes with the mouse in the editor?

For example, I have a static mesh that represents a block in the editor. Now, I add a collision shape of a box to it. When it is created, the box is smaller than the mesh.

So far as I can tell, the editor will not let me adjust only the collision shape with the mouse. If I try, it also changes the size of the mesh. I can, however, adjust it by changing the offset position and size values.

Is there a way to only select and effect just the collision shape?

-------------------------

friesencr | 2017-01-02 01:00:47 UTC | #2

This is something I am working on presently.  I am working on a PolyLine and Polygon that would tesselate a mesh from simple points.  I am struggling getting all the components to fit together.  I have some algorithms made to generate convex hulls from sprites too.  After I finish the sprite packer I will return to this.  If anyone else wants to work on it they can steal it from me or has any suggestions on api speak up.

-------------------------

rogerdv | 2017-01-02 01:00:48 UTC | #3

I noticed this working with the editor. Does it means that the collision box at runtime is smaller than the mesh or is it just a visual glitch?

-------------------------

cadaver | 2017-01-02 01:00:48 UTC | #4

If you use a box shape in CollisionShape component, it has no relation to the visible mesh size, but is fully controlled by the size parameter (X,Y,Z). However, Node scaling will affect both the StaticModel and CollsionShape components.

-------------------------

Krathoon | 2017-01-02 01:00:54 UTC | #5

It would be great if we could adjust the dimensions of the collision box with the mouse.

-------------------------

hdunderscore | 2017-01-02 01:01:03 UTC | #6

The GitHub master branch now has a feature that let's you do that.

-------------------------

