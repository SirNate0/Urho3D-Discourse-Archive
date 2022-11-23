sabotage3d | 2017-04-21 20:26:36 UTC | #1

Is there currently any way of saving custom geometry to file? For example to obj format? So far I can think only of using Assimp.

-------------------------

cadaver | 2017-04-22 19:38:03 UTC | #2

Try WriteDrawablesToOBJ() function in Drawable.h.

-------------------------

sabotage3d | 2017-05-13 14:07:10 UTC | #3

I am getting empty object if I call it from the Drawable itself. What would be the correct way? This is my code called from inside a custom drawable.

    PODVector<Drawable*> drawables;
    drawables.Push(this);
    String path = "/test.obj";
    SharedPtr<File> file = SharedPtr<File>(new File(context_, path, FILE_WRITE));
    WriteDrawablesToOBJ(drawables,file,false,false);

-------------------------

cadaver | 2017-05-13 14:30:42 UTC | #4

Recommend debugging inside the function. It does IsEnabledEffective() check right in the start, which could result to no output if the drawable / its node is not enabled.

-------------------------

sabotage3d | 2017-05-13 17:35:22 UTC | #5

It is enabled I am drawing RibbonTrail and I have the above code assigned to a hotkey, trying to capture the resulted geometry for debugging. I made my own copy of RibbonTrail and I am calling the code from inside passing this pointer as a drawable.

-------------------------

cadaver | 2017-05-13 20:18:44 UTC | #6

The drawable write will only work on geometries whose buffers have CPU-side shadow data enabled, like ordinary models. RibbonTrail does constant dynamic regeneration, so for it it would be just a performance & memory hog.

-------------------------

sabotage3d | 2017-05-13 22:02:19 UTC | #7

I understand it would be slow but I want to capture just a static state at one frame. How can I modify and copy the data in order to save it?

-------------------------

cadaver | 2017-05-14 09:34:16 UTC | #8

You could maybe go through the Drawable's Geometries, and the Vertex / IndexBuffers it uses, and call SetShadowed(true) on all of them. The next update would then copy the vertex/index data also to main memory for capture. I don't promise this will work.

-------------------------

sabotage3d | 2017-05-14 13:39:31 UTC | #9

It works partially, but the data is a bit scrambled every corner of the triangle is collapsed to a single point. When I import the obj I am getting a line where multiple points lie on top of each other.

-------------------------

cadaver | 2017-05-14 15:09:17 UTC | #10

Part of the work in getting e.g. ribbontrails and billboards to render correctly is in the vertex shader. Therefore just a dump of the vertex data, interpreting positions as just positions and multiplying them with the object's model matrix, isn't necessarily going to work 100%.

It would be the same with skeletal animation - Urho doesn't contain CPU skinning code at all and relies on the vertex shader, so you couldn't dump an AnimatedModel in its actual pose.

-------------------------

sabotage3d | 2017-05-14 17:56:46 UTC | #11

Thanks cadaver. Can you point me to the GLSL code doing this? I can't find any relevant code, It is just using the Unlit shader.

-------------------------

cadaver | 2017-05-15 08:13:47 UTC | #12

The actual vertex transform happens sort of "behind the scenes", as the iModelMatrix is actually a macro and does magic depending on geometry type. Every shader including Unlit typically does mat4 modelMatrix = iModelMatrix; What actually happens, check Transform.glsl, from about line 147 onward.

-------------------------

sabotage3d | 2017-05-16 23:35:23 UTC | #13

I see is it using the TANGENT in the shader for the transformation? Is there any benefit of doing this in the shader?

-------------------------

godan | 2017-05-17 00:18:23 UTC | #14

As I understand it, Billboard (for instance) packs a rotation matrix in the vertex buffer, which is possible because a bunch of added space has been added via setting the TEXCOORD flags.

```
            float rotationMatrix[2][2];
            SinCos(billboard.rotation_, rotationMatrix[0][1], rotationMatrix[0][0]);
            rotationMatrix[1][0] = -rotationMatrix[0][1];
            rotationMatrix[1][1] = rotationMatrix[0][0];

            dest[0] = billboard.position_.x_;
            dest[1] = billboard.position_.y_;
            dest[2] = billboard.position_.z_;
            ((unsigned&)dest[3]) = color;
            dest[4] = billboard.uv_.min_.x_;
            dest[5] = billboard.uv_.min_.y_;
            dest[6] = -size.x_ * rotationMatrix[0][0] + size.y_ * rotationMatrix[0][1];
            dest[7] = -size.x_ * rotationMatrix[1][0] + size.y_ * rotationMatrix[1][1];
```
Then, GraphicsDefs.h exposes some enums (FC_DIRECTION,etc) that are then handled in Transform.glsl.

IMO, it is pretty clever to use the vertex structures in this way, but it makes for a pretty opaque code base. I wonder if there is a better/clearer way.

-------------------------

sabotage3d | 2017-05-18 10:20:44 UTC | #15

I think for Billboard it makes sense but for RibbonTrail I am confused as there is no instancing involved.

-------------------------

