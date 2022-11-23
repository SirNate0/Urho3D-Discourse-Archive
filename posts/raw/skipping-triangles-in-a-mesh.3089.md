sabotage3d | 2017-05-01 13:40:36 UTC | #1

Hi, 
I am drawing a mesh using a TRIANGLE_LIST. To draw the mesh I am looping over points. 
To draw the TRIANGLE_LIST I have index and vertex buffers.
For example in the code below if I want to skip the triangles in point 5 and If I try with continue to skip this iteration in the loop in both vertex and index buffers I am getting a lot of graphics artefacts. What is the proper way of doing this?

    batches_[0].geometry_->SetDrawRange(TRIANGLE_LIST, 0, (points_.Size() - 1), false);
    float* dest = (float*)vertexBuffer_->Lock(0, (points_.Size() - 1), true);

    // For each point draw triangles
    for (unsigned i = 0; i < points_.Size(); ++i)
    {

    	if(i==5)
    	{
    		// Skip this point
    		// This apporach has graphics artefacts
    		continue;
    	}

    	// Draw triangles
    	// Update dest

    }

-------------------------

slapin | 2017-05-01 15:41:00 UTC | #2

Nah, your approach is too naiive.

You need to build-up triangles in index buffer, and vertex buffer and skip through whole triangle (3 index positions).

-------------------------

sabotage3d | 2017-05-01 17:28:00 UTC | #3

I already have index and vertex buffer but I can't update them properly during the loop. My question is how to do it properly?

-------------------------

Lumak | 2017-05-01 19:37:00 UTC | #4

Take look at my Material Effects repo and see how VCol change happens. You could probably change a bit of that code for your needs.

Edit: hmm, that won't do. Take a look at Geom-Replication repo for reference instead. What you should do is retain the original copy of your idxbuffer and make changes to that to skip triangle draws.

-------------------------

Victor | 2017-05-01 19:29:21 UTC | #5

I haven't tested the performance to heavily on this piece of code, but here's how I handle updating the Vertex/Index buffers. Essentially, I rebuild the vertex list... but again, not sure how much that will effect performance in the long run as it's quick and dirty. I've only used it for low-poly objects. A method can easily be added to remove a face which will rebuild the vertexList when calling the Commit() method.

https://gist.github.com/victorholt/955ae2f76173d1a5d3b9f65fefcbb47e#file-custommesh-cpp-L330-L375

-------------------------

Victor | 2017-05-01 20:04:45 UTC | #6

Oh, also, just a note when updating the StaticMesh component. I've had to do the following

    StaticModel* model = GetStaticModelComponent();
    model->SetModel(null); // Clear out the previous model so this can get updated.
    model->SetModel(YourUpdatedModel());

This is due to this line here (I'd like to know if this is correct however, as it doesn't feel right)...:
https://github.com/urho3d/Urho3D/blob/1b725367fc95552230fd414eadaccfa57faf14b8/Source/Urho3D/Graphics/StaticModel.cpp#L234

-------------------------

