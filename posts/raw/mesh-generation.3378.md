bmcorser | 2017-07-24 15:12:56 UTC | #1

I've got the simplest mesh generation code I could manage; just add a square grid of vertices and add all their triangles (see snippet linked below). Somehow only a few of the triangles get drawn. I will try to post a video demonstrating what happens.

https://www.irccloud.com/pastebin/n7QyNGIT/mesh%20generation

-------------------------

bmcorser | 2017-07-24 15:15:19 UTC | #2

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/3efbbcae48fc51f106c1b1397726d9a15482bee4.png" width="690" height="388">

-------------------------

Modanung | 2017-07-24 17:50:03 UTC | #3

I'm guessing it's got something to do with the normals. The faces that are not filled may have downward normals.
If this is the case and you're using the code from the dynamic geometry example to calculate the normals, swapping any two vertices for those triangles should do the trick.

-------------------------

bmcorser | 2017-07-24 23:19:06 UTC | #4

I'm not calculating normals at all, just setting all to `Vector3(0, 1, 0)` -- all of the normals are the same. I suspect that some of the triangles aren't being drawn for some reason; I expect I'm doing something wrong in how I set up the index buffer, but haven't been able to figure out where my mistake is.

-------------------------

1vanK | 2017-07-25 09:02:28 UTC | #5

Add two-sided material, if the geometry becomes visible then you need to change the order of the vertices

-------------------------

bmcorser | 2017-07-25 09:47:38 UTC | #6

Setting `<cull value="none" />` and `<shadowcull value="none" />` on the material I'm using gives the same result. Also tried setting all normals to `Vector3(0, -1, 0)`, "down" instead of "up" and still only the first few triangles render.

-------------------------

bmcorser | 2017-07-25 09:49:00 UTC | #7

> change the order of the vertices

Do you mean change the order of the vertices in the triangle or the order in which vertices are created initially?

-------------------------

bmcorser | 2017-07-25 09:55:41 UTC | #8

I'm also confused by `IndexBuffer::SetSize` ... should I pass the number of vertices in the vertex buffer (as is done in the sample) or the number of triangles ... ?

:roll_eyes:

-------------------------

1vanK | 2017-07-25 11:10:42 UTC | #9

IndexBuffer::SetSize - number of INDECES stored in IndexBuffer (it is not count of triangles and not number of vertices in the vertex buffer)

-------------------------

Gentle22 | 2017-07-25 11:56:16 UTC | #10

> Do you mean change the order of the vertices in the triangle or the order in which vertices are created initially?

He means the order of vertices in a triangle. Urho3D uses a clockwise order to define the front of a face. See this link for an explanation of face culling https://learnopengl.com/#!Advanced-OpenGL/Face-culling. Keep in mind, Urho3D uses clockwise order for the front of the face.

The IndexBuffer defines which vertices are used to define your faces. {0,1,2} means that your face (triangle) is created by the vertices v0, v1, v2 (stored in the VertexBuffer at the indices 0, 1 and 2) which must then be in clockwise order to define the front of your triangle.

-------------------------

Gentle22 | 2017-07-25 11:53:31 UTC | #11

> I’m also confused by IndexBuffer::SetSize … should I pass the number of vertices in the vertex buffer (as is done in the sample) or the number of triangles … ?

See this link for an explanation of the IndexBuffer http://www.opengl-tutorial.org/intermediate-tutorials/tutorial-9-vbo-indexing/

The size of the index buffer should be the amount of triangles you want to draw multiplied with 3. If you want to draw a quad consisting of two triangles, the vertex buffer need to have a size of 6, because each triangle is made of three vertices and you want to draw 2 triangles.

-------------------------

Victor | 2017-07-25 13:12:12 UTC | #12

This class might help as well if you'd like to get away from declaring the Vertex/Index buffers yourself. https://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_custom_geometry.html

It's a little less flexible as described here by cadaver https://github.com/urho3d/Urho3D/issues/470#issuecomment-57127827

-------------------------

bmcorser | 2017-07-25 22:14:30 UTC | #13

Thanks for the help guys. Turns out my original issue was in the call to `Geometry::SetDrawRange` ... passing a larger number than `vertexCount` gets all the triangles rendering.

@Victor thanks, I just noticed that exists ... :roll_eyes: I'd like to be able to set vertex positions (for animation) so will look into `CustomGeometry` as a way to do that without having to write too much of my own terrible code.

-------------------------

bmcorser | 2017-07-25 22:14:57 UTC | #14

https://youtu.be/LYzMJrn_JNE

## :tada:

-------------------------

Victor | 2017-07-25 22:28:14 UTC | #15

Nice work! I'm glad you were able to figure out your vertex issue! :)

-------------------------

