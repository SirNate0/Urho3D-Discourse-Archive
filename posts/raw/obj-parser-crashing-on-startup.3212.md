ppsychrite | 2017-06-06 10:28:20 UTC | #1

So I've recently begun to make an .obj parser (Yeah I do know it's much better to use .mdl but I'm doing it for some specific reasons).

How it's Done:
-Open the file and parse all v's vt's vn's and f's into their separate vectors (face values are put into indices).
-Put them into an index and vertex buffer (here's how I did it):

    ur::Vector<float> vertexData;
	ur::Vector<unsigned short> indexData;

	for (size_t i = 0; i < vectorIndices.Size(); ++i) {
		ur::Vector3 vertex = tempVertices[vectorIndices[i] - 1];
		ur::Vector3 normal = tempNormals[normalIndices[i] - 1];
		ur::Vector2 texcoord = tempTexCoords[texcoordIndices[i] - 1];

		vertexData.Push(vertex.x_);
		vertexData.Push(vertex.y_);
		vertexData.Push(vertex.z_);

		vertexData.Push(normal.x_);
		vertexData.Push(normal.y_);
		vertexData.Push(normal.z_);

		vertexData.Push(texcoord.x_);
		vertexData.Push(texcoord.y_);

		indexData.Push(i);
	}
Now If I were to call it to parse a regular .obj it would run fine without crashing, but when I add the last part of dynamic geometry it crashes. I've also tried using Custom Geometry but that crashes too. I do not know the solution to this (The obj file has a total of 1458 lines so it isn't THAT BIG)
If you want to see the full parser if you didn't think I showed enough code here it is: https://hastebin.com/sasizohubo.php

-------------------------

ppsychrite | 2017-06-06 01:53:12 UTC | #2

I got it to where it complains 
I don't know why but 

    ib->SetSize(indexData.Size(), false);

Is throwing an exception.

EDIT: It turns out Urho3D's Vector class doesn't work when it comes to this, I used the std::vector class and it works fine now. :confused:

-------------------------

Eugene | 2017-06-06 09:37:40 UTC | #3

What's the meaning of `vb->SetData(&vertexData);` and `ib->SetData(&indexData);`?

-------------------------

ppsychrite | 2017-06-06 11:00:13 UTC | #4

Oh, that was originally to put the vector's pointer data as an argument, I'm using the vector class and the .data() function now.

-------------------------

Eugene | 2017-06-06 11:13:10 UTC | #5

That's the problem, I suppose.

-------------------------

