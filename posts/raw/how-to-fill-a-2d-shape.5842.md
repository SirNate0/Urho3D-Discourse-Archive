evolgames | 2020-01-26 16:29:27 UTC | #1

Hello, I'm using the 2dConstraints sample. I want to make objects without image sprites, just filling the 2d primitives with specific colors.

I don't see how I can set the color of the sprite. I noticed it's drawing the outline of the polygon with the Debug renderer, which is fine, but I have no idea how I can modify that debug fill color. I tried doing the following:

```
    for v=1,vn do
    verts[v]=guys[1].shape:GetVertex(v)
    end
   --debugRend:AddPolygon(Vector3(1.2, -0.3,0), Vector3(2.5, -0.8,0), Vector3(2.8, -0.3,0), Vector3(2.8, 0.5,0),Color(1,0,0), false)
   
   local pos=guys[1].body:GetPosition()
   debugRend:AddPolygon(Vector3(verts[1]+pos),Vector3(verts[2]+pos),Vector3(verts[3]+pos),Vector3(verts[4]+pos),Color(1,1,1), false)
```

Because I just want to draw a polygon where these 2d rigid bodies are. But there is no function to find the position of the 2d rigid body. At least not that I can find...

Adding a polygon to the debug renderer lets me choose the color but then  I can't get the position of the body to draw. And for the 2d rigid bodies it appears they can only be drawn with image sprites?

Anyone know how I can just fill a 2d rigidbody with a color?

-------------------------

evolgames | 2020-01-26 16:29:03 UTC | #2

Nevermind I found it. For those of you looking for the same thing:

I took the position of the Node for the rigidbody, not the shape, with:

```local pos=guys[1].node:GetWorldPosition2D()```

This gave me the updated position. Now I just need to scale and rotate it before drawing with the debug renderer and I'll easily be able to set colors.

-------------------------

