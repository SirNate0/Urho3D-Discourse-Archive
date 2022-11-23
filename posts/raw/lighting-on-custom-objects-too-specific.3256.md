ppsychrite | 2017-06-30 20:25:16 UTC | #1

I don't know how to describe this but lighting on objects made similar to the Dynamic Geometry sample feel more "on point" with a Directional Light point in a general direction.

Here's what the regular cube .mdl looks like in the Directional light. (The light's direction is 0.6f, -1.0f, 0.8f)

http://prntscr.com/fk976s

Here's what a custom object with a cube model looks like in the Directional light.

http://prntscr.com/fk985e

The custom object cube light seems to be more "on-point" or "specific" and less spread out compared to the .mdl
Here's how a vertex is in my custom objects

    //position           normals                 color                          tmap             tangents 
    0.0f, 0.0f, 0.0f,	0.0f, 0.0f, 0.0f,	color.r_, color.g_, color.b_,	0.0f, 0.0f,   0.0f, 0.0f, 0.0f, 0.0f,


And I calculate normals and tangent this way, doesn't seem to glitch the vertices at all so it seems fine.

    for (int iter = 0; iter < vertexData.size(); iter += 15) {
			ur::Vector3 vertex = { vertexData[iter], vertexData[iter + 1], vertexData[iter + 2] };
			vertex.Normalize();
			vertex.Normalize();


			vertexData[iter + 3] = vertex.x_;
			vertexData[iter + 4] = vertex.y_;
			vertexData[iter + 5] = vertex.z_;
		}
		ur::GenerateTangents(vertexData.data(), 15 * sizeof(float), indexData, sizeof(unsigned short), 0, numIndices, 3 * sizeof(float), 9 * sizeof(float), 11 * sizeof(float));

Is there any reason behind the custom object's lighting looking more "specific"?

-------------------------

Modanung | 2017-06-30 20:24:57 UTC | #2

The difference is in the normals, and with it the number of vertices.
Normals are interpolated along connected faces, but each vertex only holds a single normal direction. So to sharpen the edges they are split. To achieve this effect with custom geometry you'd have to create six separate faces using 24 vertices and orthogonal normals, in case of a cube.
This is why the pyramid in the [DynamicGeometry](https://github.com/urho3d/Urho3D/blob/master/Source/Samples/34_DynamicGeometry/DynamicGeometry.cpp#L163-L263) sample uses 18 vertices, not 5.

-------------------------

ppsychrite | 2017-06-16 16:46:33 UTC | #3

The cube is composed of 6 one-sided squares at the moment (24 vertices in total). To calculate the normals correctly would it be best to double the amount of vertices of each so it's 48 in total? And would the position of the new vertices be the same as the ones for the cube?

-------------------------

Modanung | 2017-06-16 16:51:12 UTC | #4

[quote="ppsychrite, post:3, topic:3256"]
To calculate the normals correctly would it be best to double the amount of vertices of each so it's 48 in total?
[/quote]

No, 24 is enough. In this case you'll want to calculate the normals as in the [linked-to sample](https://github.com/urho3d/Urho3D/blob/master/Source/Samples/34_DynamicGeometry/DynamicGeometry.cpp#L204-L217): By calculating the cross product of the edge direction.

-------------------------

ppsychrite | 2017-06-25 12:08:09 UTC | #5

(Sorry for absence I've had to go to somewhere for a week)
So I tried doing it to my cube with 24 vertices and it turned it black (You can't see it at all)

I tried doing a step over to see if it messed up the vertices but the position looks fine from what I'm seeing, and the normals seem like a reasonable number.

I attempted to try and take out

    n1 = n2 = n3 = edge1.CrossProduct(edge2).Normalized();

And it looks like this: http://prntscr.com/fnxfln

So it is a definite improvement of what I was doing before but it seems to not work if I do the full sample. :neutral_face:

-------------------------

Modanung | 2017-08-25 17:21:14 UTC | #6

Ok, so it seems normals are automatically calculated correctly? :confused:
Did I mention how little experience I have with custom geometry?

If the cube shows up all black the normals might be pointing in the wrong direction or be zero. Try switching `edge1` and `edge2` or negating the normal.

-------------------------

ppsychrite | 2017-06-29 00:49:19 UTC | #7

After toying around with swapping edge1 and edge2 and numerous other things I've managed to make the custom geometry visible (Although extremely dark) But for some reason all of their colors are yellow now. I'm not sure how they turn yellow but eh.

-------------------------

Modanung | 2017-06-29 06:38:32 UTC | #8

Do you have a repository so people could check out and test your code?

-------------------------

ppsychrite | 2017-06-29 16:01:27 UTC | #9

 I don't find it nessecary for now.

Here's the code for making a "cube" with the normals that doesn't work though.
https://hastebin.com/aqipusezat.go

-------------------------

Modanung | 2017-06-30 20:24:57 UTC | #10

Try to find the difference between the math in these lines:
```
for (int iter = 0; iter < vertexData.size(); iter += 15) {
	Vector3& v1 = *(reinterpret_cast<Vector3*>(&vertexData[iter]));
	Vector3& v2 = *(reinterpret_cast<Vector3*>(&vertexData[iter + 1]));
	Vector3& v3 = *(reinterpret_cast<Vector3*>(&vertexData[iter + 2]));
	Vector3& n1 = *(reinterpret_cast<Vector3*>(&vertexData[iter + 3]));
	Vector3& n2 = *(reinterpret_cast<Vector3*>(&vertexData[(iter + 1) + 3]));
	Vector3& n3 = *(reinterpret_cast<Vector3*>(&vertexData[(iter + 2) + 3]));
```
And these:
https://github.com/urho3d/Urho3D/blob/master/Source/Samples/34_DynamicGeometry/DynamicGeometry.cpp#L205-L212

I hope that's enough information. :slight_smile:

-------------------------

ppsychrite | 2017-06-29 22:46:12 UTC | #11

Aha! I got it.
Can't believe I didn't notice that for days.
I'll find a way to implement that for 6 separate planes.
Thank you!

-------------------------

ppsychrite | 2017-06-29 23:40:42 UTC | #12

(All the unneeded parts were cut off)
https://hastebin.com/hoyabugiyi.go

Doing DynamicGeometry's example does make the custom geometry appear (thankfully) and gives it some lighting, but it's in utter darkness even though a light is being shown on it: http://prntscr.com/fpsz0v

-------------------------

Modanung | 2017-06-30 02:03:20 UTC | #13

[quote="ppsychrite, post:12, topic:3256"]
(All the unneeded parts were cut off)
https://hastebin.com/hoyabugiyi.go
[/quote]

Well... I don't see any code at all. :confused:
Bin too hasty? :drum::wink:

-------------------------

ppsychrite | 2017-06-30 14:56:17 UTC | #14

*slaps knee* :rofl:
That's awfully strange, I can view it fine.
Here! Let me convert it to pastebin instead: https://pastebin.com/nRDRtHyK

-------------------------

Modanung | 2017-06-30 15:01:42 UTC | #15

[quote="ppsychrite, post:14, topic:3256"]
That's awfully strange, I can view it fine.
[/quote]

First one worked fine, too.

```
const unsigned short numVertices = 6;
const unsigned short numIndices = 6;
```
```
for (int iter = 0; iter < numVertices; iter += 3) {
```
There's 24 vertices in a flat-shaded box. :slight_smile:

-------------------------

ppsychrite | 2017-06-30 15:04:02 UTC | #16

That calculates the vertices for each side 6 times, not all together.

-------------------------

Modanung | 2017-06-30 15:07:02 UTC | #17

[quote="ppsychrite, post:16, topic:3256, full:true"]
That calculates the vertices for each side 6 times, not all together.
[/quote]

Ah, but shouldn't `numVertices` be 4 then?

Have you tried some good old pen and paper on this? :slight_smile:

-------------------------

ppsychrite | 2017-06-30 15:07:51 UTC | #18

It was like that at first but that didn't work so I tried it the way the custom geometry did (have their be 6 vertices and have the index buffer go through 0,1,2,3,4,5)
Yes I've done pen and paper with it in a lot of ways.

-------------------------

Modanung | 2017-06-30 16:10:59 UTC | #19

Do you add the extra elements, like color and uv coords to the buffer, along these lines?

```
PODVector<VertexElement> elements;
elements.Push(VertexElement(TYPE_VECTOR3, SEM_POSITION));
elements.Push(VertexElement(TYPE_VECTOR3, SEM_NORMAL));
vb->SetSize(numVertices, elements);
```

And shouldn't this:
```
Vector3& v2 = *(reinterpret_cast<Vector3*>(&vertexData[iter * 15 + 1]));
```
Be:
```
Vector3& v2 = *(reinterpret_cast<Vector3*>(&vertexData[(iter + 1) * 15]));
```
?

-------------------------

ppsychrite | 2017-06-30 16:21:13 UTC | #20

Yeah I pushed more  into elements

    elements.Push(ur::VertexElement(ur::TYPE_VECTOR3, ur::SEM_POSITION));
	elements.Push(ur::VertexElement(ur::TYPE_VECTOR3, ur::SEM_NORMAL));
	elements.Push(ur::VertexElement(ur::TYPE_VECTOR3, ur::SEM_COLOR));
	elements.Push(ur::VertexElement(ur::TYPE_VECTOR2, ur::SEM_TEXCOORD));
	elements.Push(ur::VertexElement(ur::TYPE_VECTOR4, ur::SEM_TANGENT));

And I do believe that 

    Vector3& v2 = *(reinterpret_cast<Vector3*>(&vertexData[iter * 15 + 1]));

Does get the correct part of vertexData (the y value)

-------------------------

Modanung | 2017-06-30 16:34:42 UTC | #21

Ah, no. That would read a Vector3, starting at the y value. Giving you a `Vector3(posY, posZ, normX)`, I guess.

`v2` in this case stand for 2nd vertex. That's why the `iter` increases with steps of three. The for loop handles three vertices at once.

-------------------------

ppsychrite | 2017-06-30 16:26:52 UTC | #22

Wait a second.
This entire time I've been assuming v1, v2, and v3 were x, y, z and same for the normals?

...
Well then. :expressionless:
I'll try it the other way when I get home.
I'm displeased with myself.
Thanks Modanung

-------------------------

Modanung | 2017-06-30 16:33:30 UTC | #23

You're welcome! :slight_smile:

-------------------------

ppsychrite | 2017-06-30 19:21:55 UTC | #24

AHAH IT'S BEAUTIFUL!
http://prntscr.com/fq53mv

-------------------------

