ppsychrite | 2017-06-01 08:09:12 UTC | #1

For some strange reason the way I calculate the normals on my cube spazzes the cube out. I do not know whether it's the normal itself or I'm doing it wrong.

This is what the cube looks like when I comment out the method used: http://prntscr.com/fe0plv
Here's what it looks like when I don't comment it out: http://prntscr.com/fe0pv5

Here's the Vertex Data (Min and Max are variables):

    float vertexData[] = {

		min.x_,          min.y_,          min.z_,							0.0f, 0.0f, 0.0f,
		min.x_ + max.x_, min.y_,		  min.z_,							0.0f, 0.0f, 0.0f,
		min.x_ + max.x_, min.y_ + max.y_, min.z_,							0.0f, 0.0f, 0.0f,
		min.x_,          min.y_ + max.y_, min.z_,							0.0f, 0.0f, 0.0f,

		min.x_,          min.y_,		  min.z_ + max.z_,					0.0f, 0.0f, 0.0f,
		min.x_ + max.x_, min.y_,		  min.z_ + max.z_,					0.0f, 0.0f, 0.0f,
		min.x_ + max.x_, min.y_ + max.y_, min.z_ + max.z_,					0.0f, 0.0f, 0.0f,
		min.x_,			 min.y_ + max.y_, min.z_ + max.z_,					0.0f, 0.0f, 0.0f

	};

Here's the way I calculate normals (The way in the sample glitches out too so I tried a different way, still doesn't work):

    for (unsigned int i = 0; i < 48; i += 6) {

		ur::Vector3 normal({ vertexData[i], vertexData[i + 1], vertexData[i + 2] });
		normal.Normalize();

		vertexData[(i + 3)] = normal.x_;
		vertexData[(i + 3) + 1] = normal.y_;
		vertexData[(i + 3) + 3] = normal.z_;
	}
    ur::SharedPtr<Model> model(new ur::Model(context_));
	ur::SharedPtr<ur::VertexBuffer> vb(new ur::VertexBuffer(context_));
	ur::SharedPtr<ur::IndexBuffer> ib(new ur::IndexBuffer(context_));
	ur::SharedPtr<ur::Geometry> geom(new ur::Geometry(context_));

	vb->SetShadowed(true);

    ur::PODVector<ur::VertexElement> elements;
	elements.Push(ur::VertexElement(ur::TYPE_VECTOR3, ur::SEM_POSITION));
	elements.Push(ur::VertexElement(ur::TYPE_VECTOR3, ur::SEM_NORMAL));
The rest of the code is self-explanatory but I also apply the NoTextureVCol Technique.
There doesn't seem to be any problem in the code that I'm aware of so I'm not sure what's wrong.

-------------------------

Sinoid | 2017-05-31 01:18:24 UTC | #2

[quote="ppsychrite, post:1, topic:3180"]
vertexData[(i + 3) + 3] = normal.z_;
[/quote]

That looks suspect. Shouldn't it be `vertexData[(i+3)+2] = normal.z_;`? Looks to me like you're overwriting X coordinates.

-------------------------

ppsychrite | 2017-05-31 01:37:30 UTC | #3

Holy. Thank you I didn't notice, how stupid of me.
While that does make it a cube, for some dang reason a face of the cube is all black and a vertex.

http://prntscr.com/fe1v6i
http://prntscr.com/fe1vbj

I'm pretty sure now that it doesn't have to do with the normals!

-------------------------

Sinoid | 2017-05-31 01:39:27 UTC | #4

[quote="ppsychrite, post:3, topic:3180"]
I'm pretty sure n ow that it doesn't have to do with the normals!
[/quote]

It probably still is. You're only using 8 vertices for a cube which means your normal calculation is wrong (need to accumulate and then normalize) or you need to add colocal vertices to that which have unique vertices for the corners and use the appropriate indices.

The normals calculation code in the DynamicGeometry sample works because the shape is a simple pyramid with unique vertices for every face. You'll need unique vertices for each face of your cube most likely or integrate your normals.

    for (unsigned int i = 0; i < 48; i += 6) {
        ur::Vector3 normal({ vertexData[i], vertexData[i + 1], vertexData[i + 2] });
        normal.Normalize();

        // NOTE: CHANGE TO +=
        // Accumulate normals
        vertexData[(i + 3)] += normal.x_;
        vertexData[(i + 3) + 1] += normal.y_;
        vertexData[(i + 3) + 2] += normal.z_;
    }

    // Normalize accumulated normals
    for (unsigned int i = 0; i < 48; i += 6)
        ((Vector3*)&vertexData[i+3])->Normalize(); // note this is probably malformed code

Edits: can't use grammar apparently.

-------------------------

ppsychrite | 2017-05-31 01:48:48 UTC | #5

So what you're saying is that after I += normalized values into the vertexData I should then normalize the values accumulated? Got it. Will try when I have time.

-------------------------

ppsychrite | 2017-05-31 12:00:07 UTC | #6

After accumulating and then normalizing it's still the same (Although when I try inserting colors and pushing it to elements all colors appear but lighting doesn't affect it)
http://prntscr.com/fe7iwb

-------------------------

ppsychrite | 2017-06-01 08:09:17 UTC | #7

This probably has to be one of my biggest mistakes this far. :sweat:
Instead of using the rgb values as 0.0f through 1.0f I've been using them as 0 to 255, making it defy lighting. 
I changed it to 1.0f for the red value and it works fine except for a triangle and a face now. :grinning: http://prntscr.com/fegajo
So it's progress!

-------------------------

