haroim | 2017-01-02 01:08:55 UTC | #1

Hello,

I am playing around with the polyvox library and Urho3D and I got quite far integrating them by following the samples provided. I now have a voxel sphere of which I can set the size and color (per vertex) in the a scene. But I am facing a strange segmentation fault when I made a slider which controls with size of the sphere. It seems to initial work fine and the sphere increase and decreases in size, but after a while of resizing I get a segmentation fault directly after set the new data in the vertex buffer. 

What I do schematically is the following:
The initial mesh is created in the following way:

[code]
fromScratchModel = new Model(context_);
vb = new VertexBuffer(context_);
ib = new IndexBuffer(context_);
geom = new Geometry(context_);

vb->SetShadowed(true);
vb->SetSize(vertex_data.size(), MASK_POSITION|MASK_NORMAL|MASK_COLOR,false);
vb->SetData(&(vertex_data[0]));

ib->SetShadowed(true);
ib->SetSize(index_data.size(), false);
ib->SetData(&(index_data[0]));

geom->SetVertexBuffer(0, vb);
geom->SetIndexBuffer(ib);
geom->SetDrawRange(TRIANGLE_LIST, 0, index_data.size());

fromScratchModel->SetNumGeometries(1);
fromScratchModel->SetGeometry(0, 0, geom);
fromScratchModel->SetBoundingBox(BoundingBox(Vector3(0.0f, 0.0f, 0.0f), Vector3(200.0f, 200.0f, 200.0f)));

Node* node = scene_->CreateChild("FromScratchObject");
node->SetPosition(Vector3(0.0f, 4.0f, 0.0f));
node->SetScale(1);
StaticModel* object = node->CreateComponent<StaticModel>();
object->SetModel(fromScratchModel);
...
[/code]

Then when I have reason to believe that the mesh has changed I create new vertex data and index data vectors. I have tried just use the SetSize and SetData for the buffers, which worked but got me the segmentation fault after a while. I also tried removing the child from the scene and creating every again (using the same global shared pointers), but it still resulted in the same segmentation fault at the same point (SetData).

I looked a the how big my vertexdata vector is and how large my buffer is, just before setting the data, and they have exactly the same size. Can anyone help me find the problem (and hopefully a solution)? 

Thanks!

P.S. I am quite new to opengl so it might just be a trivial mistake :slight_smile:

-------------------------

cadaver | 2017-01-02 01:08:55 UTC | #2

Welcome to the forums.

I tested the DynamicGeometry sample growing the vertex buffer each frame (on OpenGL), couldn't make it crash.

VertexBuffer::SetSize() takes a vertex count. What is the type of your vertex data vector? If it's e.g. a std::vector<unsigned char> then its size should be numVertices * vertexByteSize. If you have defined a struct for your vertices and your vector holds them instead, then the size being same is correct (barring any struct padding issues.)

-------------------------

haroim | 2017-01-02 01:08:56 UTC | #3

hmm, I feel a bit stupid right now. I forgot to divide the vertex_data.size() by seven when I resized the vertex data. It works great now! 

I am still amazed it didn't crash directly :s

Anyway, thanks for the quick reply!

-------------------------

