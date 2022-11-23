cap | 2017-01-02 01:07:43 UTC | #1

Trying to correctly set the VertexBuffer for the geometry of a Model created from scratch. We know how to do this in general (following for e.g. the DynamicGeometries sample), but cannot quite get it right when we want to set the color of the model vertex by vertex, e.g., so the object is red in some spots and blue in another, or whatever.

So we are going to do

[code]
SharedPtr<VertexBuffer> vb(new VertexBuffer(context));
vb->SetSize(numVertices, MASK_POSITION|MASK_NORMAL|MASK_COLOR);
vb->SetData((void*)*newVertexData);
[/code]

but we need to initialize newVertexData first. I've reproduced the outline of how we do this below. It's probably more complex than it really needs to be, but since we include colors we seem to need both floats and unsigned chars stored in the same object newVertexData. We would have done this with void* types but we are using Visual Studio 2012 and it seems that over there one must use char*.

The error is we typically get either no object appearing at all, or a crazy shape. So we want to check here if our approach is on the right track because it's hard to interpret the results we're getting. Okay here's that outline of what we tried:

[code]
char** newVertexData = (char**)malloc(numVertices * 10 * sizeof(char*));

for(int i = 0; i < numVertices; i++)
{
	newVertexData[10 * i + 0] = (char*)malloc(sizeof(float));
	newVertexData[10 * i + 1] = (char*)malloc(sizeof(float));
	newVertexData[10 * i + 2] = (char*)malloc(sizeof(float));
	newVertexData[10 * i + 3] = (char*)malloc(sizeof(float));
	newVertexData[10 * i + 4] = (char*)malloc(sizeof(float));
	newVertexData[10 * i + 5] = (char*)malloc(sizeof(float));
	newVertexData[10 * i + 6] = (char*)malloc(sizeof(unsigned char));
	newVertexData[10 * i + 7] = (char*)malloc(sizeof(unsigned char));
	newVertexData[10 * i + 8] = (char*)malloc(sizeof(unsigned char));
	newVertexData[10 * i + 9] = (char*)malloc(sizeof(unsigned char));
}

for(int i = 0; i < triCount; i++)
{

	//v1
	*((float*)newVertexData[30 * i + 0]) = (float)verts[3 * faces[3 * i + 0] + 0];
	*((float*)newVertexData[30 * i + 1]) = (float)verts[3 * faces[3 * i + 0] + 1];
	*((float*)newVertexData[30 * i + 2]) = (float)verts[3 * faces[3 * i + 0] + 2];
	//n1		  
	*((float*)newVertexData[30 * i + 3]) = n.x_;
	*((float*)newVertexData[30 * i + 4]) = n.y_;
	*((float*)newVertexData[30 * i + 5]) = n.z_;
	//c1		
	*((unsigned char*)newVertexData[30 * i + 6]) = (unsigned char) 255;
	*((unsigned char*)newVertexData[30 * i + 7]) = (unsigned char) 0;
	*((unsigned char*)newVertexData[30 * i + 8]) = (unsigned char) 0;
	*((unsigned char*)newVertexData[30 * i + 9]) = (unsigned char) 255;

	//v2
	*((float*)newVertexData[30 * i + 10]) = (float)verts[3 * faces[3 * i + 1] + 0];
	*((float*)newVertexData[30 * i + 11]) = (float)verts[3 * faces[3 * i + 1] + 1];
	*((float*)newVertexData[30 * i + 12]) = (float)verts[3 * faces[3 * i + 1] + 2];
	//n2
	*((float*)newVertexData[30 * i + 13]) = n.x_;
	*((float*)newVertexData[30 * i + 14]) = n.y_;
	*((float*)newVertexData[30 * i + 15]) = n.z_;
	//c2
	*((unsigned char*)newVertexData[30 * i + 16]) = (unsigned char) 0;
	*((unsigned char*)newVertexData[30 * i + 17]) = (unsigned char) 255;
	*((unsigned char*)newVertexData[30 * i + 18]) = (unsigned char) 0;
	*((unsigned char*)newVertexData[30 * i + 19]) = (unsigned char) 255;

	//v3
	*((float*)newVertexData[30 * i + 20]) = (float)verts[3 * faces[3 * i + 2] + 0];
	*((float*)newVertexData[30 * i + 21]) = (float)verts[3 * faces[3 * i + 2] + 1];
	*((float*)newVertexData[30 * i + 22]) = (float)verts[3 * faces[3 * i + 2] + 2];
	//n3		  
	*((float*)newVertexData[30 * i + 23]) = n.x_;
	*((float*)newVertexData[30 * i + 24]) = n.y_;
	*((float*)newVertexData[30 * i + 25]) = n.z_;
	//c3
	*((unsigned char*)newVertexData[30 * i + 26]) = (unsigned char) 0;
	*((unsigned char*)newVertexData[30 * i + 27]) = (unsigned char) 0;
	*((unsigned char*)newVertexData[30 * i + 28]) = (unsigned char) 255;
	*((unsigned char*)newVertexData[30 * i + 29]) = (unsigned char) 255;
}
[/code]

The vertex data is stored in newVertexData. For each vertex, the first 3 entries are vertex coordinates, next 3 are normal coordinates, and next 4 are for the color.

Thanks for any help.

-------------------------

cap | 2017-01-02 01:07:43 UTC | #2

Thank you very much for walking me through it. Clearly I needed it, and I learned a lot from your response.

Much appreciated.

-------------------------

SteveU3D | 2017-03-17 14:41:48 UTC | #3

Hi,

Did you manage to add color to a vertex? I try to add color on to the vertices in sample 34_DynamicGeometry with no success.

Here is the code : 

    		const unsigned numVertices = 18;
		int perVertex = 10;

		float colorFloat = 0.0f;

		float vertexData[] = {
			// Position             Normal					Color
			0.0f, 0.5f, 0.0f,       0.0f, 0.0f, 0.0f,		0.0f, 0.5f, 0.0f, colorFloat, //I tested a lot of things here
			0.5f, -0.5f, 0.5f,      0.0f, 0.0f, 0.0f,		0.5f, -0.5f, 0.5f, colorFloat,//but no change
			0.5f, -0.5f, -0.5f,     0.0f, 0.0f, 0.0f,		0.5f, -0.5f, -0.5f, colorFloat,

			0.0f, 0.5f, 0.0f,       0.0f, 0.0f, 0.0f,		0.0f, 0.5f, 0.0f, colorFloat,
			-0.5f, -0.5f, 0.5f,     0.0f, 0.0f, 0.0f,		-0.5f, -0.5f, 0.5f, colorFloat,
			0.5f, -0.5f, 0.5f,      0.0f, 0.0f, 0.0f,		0.5f, -0.5f, 0.5f, colorFloat,

			0.0f, 0.5f, 0.0f,       0.0f, 0.0f, 0.0f,		0.0f, 0.5f, 0.0f, colorFloat,
			-0.5f, -0.5f, -0.5f,    0.0f, 0.0f, 0.0f,		-0.5f, -0.5f, -0.5f, colorFloat,
			-0.5f, -0.5f, 0.5f,     0.0f, 0.0f, 0.0f,		-0.5f, -0.5f, 0.5f, colorFloat,

			0.0f, 0.5f, 0.0f,       0.0f, 0.0f, 0.0f,		0.0f, 0.5f, 0.0f, colorFloat,
			0.5f, -0.5f, -0.5f,     0.0f, 0.0f, 0.0f,		0.5f, -0.5f, -0.5f, colorFloat,
			-0.5f, -0.5f, -0.5f,    0.0f, 0.0f, 0.0f,		-0.5f, -0.5f, -0.5f, colorFloat,

			0.5f, -0.5f, -0.5f,     0.0f, 0.0f, 0.0f,		0.5f, -0.5f, -0.5f, colorFloat,
			0.5f, -0.5f, 0.5f,      0.0f, 0.0f, 0.0f,		0.5f, -0.5f, 0.5f, colorFloat,
			-0.5f, -0.5f, 0.5f,     0.0f, 0.0f, 0.0f,		-0.5f, -0.5f, 0.5f, colorFloat,

			0.5f, -0.5f, -0.5f,     0.0f, 0.0f, 0.0f,		0.5f, -0.5f, -0.5f, colorFloat,
			-0.5f, -0.5f, 0.5f,     0.0f, 0.0f, 0.0f,		-0.5f, -0.5f, 0.5f, colorFloat,
			-0.5f, -0.5f, -0.5f,    0.0f, 0.0f, 0.0f,		-0.5f, -0.5f, -0.5f, colorFloat
		};

		const unsigned short indexData[] = {
			0, 1, 2,
			3, 4, 5,
			6, 7, 8,
			9, 10, 11,
			12, 13, 14,
			15, 16, 17
		};

		// Calculate face normals now
		for (unsigned i = 0; i < numVertices; i += 3)
		{
			Vector3& v1 = *(reinterpret_cast<Vector3*>(&vertexData[perVertex * i]));
			Vector3& v2 = *(reinterpret_cast<Vector3*>(&vertexData[perVertex * (i + 1)]));
			Vector3& v3 = *(reinterpret_cast<Vector3*>(&vertexData[perVertex * (i + 2)]));
			Vector3& n1 = *(reinterpret_cast<Vector3*>(&vertexData[perVertex * i + 3]));
			Vector3& n2 = *(reinterpret_cast<Vector3*>(&vertexData[perVertex * (i + 1) + 3]));
			Vector3& n3 = *(reinterpret_cast<Vector3*>(&vertexData[perVertex * (i + 2) + 3]));

			Vector3 edge1 = v1 - v2;
			Vector3 edge2 = v1 - v3;
			n1 = n2 = n3 = edge1.CrossProduct(edge2).Normalized();
		}
		//*/

		SharedPtr<Model> fromScratchModel(new Model(context_));
		SharedPtr<VertexBuffer> vb(new VertexBuffer(context_));
		SharedPtr<IndexBuffer> ib(new IndexBuffer(context_));
		SharedPtr<Geometry> geom(new Geometry(context_));

		// Shadowed buffer needed for raycasts to work, and so that data can be automatically restored on device loss
		vb->SetShadowed(false);
		// We could use the "legacy" element bitmask to define elements for more compact code, but let's demonstrate
		// defining the vertex elements explicitly to allow any element types and order
		PODVector<VertexElement> elements;
		elements.Push(VertexElement(TYPE_VECTOR3, SEM_POSITION));
		elements.Push(VertexElement(TYPE_VECTOR3, SEM_NORMAL));
		elements.Push(VertexElement(TYPE_VECTOR4, SEM_COLOR));
		vb->SetSize(numVertices, elements);
		vb->SetData(vertexData);

		ib->SetShadowed(true);
		ib->SetSize(numVertices, false);
		ib->SetData(indexData);

		geom->SetVertexBuffer(0, vb);
		geom->SetIndexBuffer(ib);
		geom->SetDrawRange(TRIANGLE_LIST, 0, numVertices);

		fromScratchModel->SetNumGeometries(1);
		fromScratchModel->SetGeometry(0, 0, geom);
		fromScratchModel->SetBoundingBox(BoundingBox(Vector3(-0.5f, -0.5f, -0.5f), Vector3(0.5f, 0.5f, 0.5f)));

		// Though not necessary to render, the vertex & index buffers must be listed in the model so that it can be saved properly
		Vector<SharedPtr<VertexBuffer> > vertexBuffers;
		Vector<SharedPtr<IndexBuffer> > indexBuffers;
		vertexBuffers.Push(vb);
		indexBuffers.Push(ib);
		// Morph ranges could also be not defined. Here we simply define a zero range (no morphing) for the vertex buffer
		PODVector<unsigned> morphRangeStarts;
		PODVector<unsigned> morphRangeCounts;
		morphRangeStarts.Push(0);
		morphRangeCounts.Push(0);
		fromScratchModel->SetVertexBuffers(vertexBuffers, morphRangeStarts, morphRangeCounts);
		fromScratchModel->SetIndexBuffers(indexBuffers);

		Node* node = scene_->CreateChild("FromScratchObject");
		node->SetPosition(Vector3(0.0f, 3.0f, 0.0f));
		StaticModel* object = node->CreateComponent<StaticModel>();
		object->SetModel(fromScratchModel);

I tested a lot of things instead of

    0.0f, 0.5f, 0.0f, colorFloat,

like unsigned char[4], as according to the documentation it has to be

    Color (unsigned char[4], normalized)

but no change.

Thanks.

-------------------------

Eugene | 2017-03-17 15:22:49 UTC | #4

Do you use appropriate material/techinque that draw color?
Why alpha-channel is zero?

-------------------------

SteveU3D | 2017-03-28 15:13:27 UTC | #5

The 
    
    float colorFloat = 0.0f;
is a mistake. It's equal to 1.0f.

Here is the material part :

    SharedPtr<Material> renderMaterial(new Material(context_));
    renderMaterial->SetTechnique(0, cache->GetResource<Technique>("Techniques/DiffVColor.xml"));
    renderMaterial->SetDepthBias(BiasParameters(-0.001f, 0.0f));
    
    Node* node = scene_->CreateChild("FromScratchObject");
    node->SetPosition(Vector3(0.0f, 3.0f, 0.0f));
    StaticModel* object = node->CreateComponent<StaticModel>();
    object->SetModel(fromScratchModel);

    object->SetMaterial(renderMaterial);

Do I need to add the params

    Texcoord1 (Vector2)
    Texcoord2 (Vector2)

in vertexData?

**EDIT :**
I have been struggling for several days now trying to add color to a vertex but still nothing unfortunately. I am completely stuck with that vertexData unsigned char or float array in which I have to put float / unsigned char values ... as the documentation says : 

    Position (Vector3)
    Normal (Vector3)
    Color (unsigned char[4], normalized)

There are a lot of posts which deal about this subject but no one really helps me since the vertexData array is not explicitly in their code.
So, could someone tell me what to add in sample 34_DynamicGeometry, in vertexData, to add color to the pyramid's vertices please?

I think that I have the good code for the rest, particularly : 

    ....
    elements.Push(VertexElement(TYPE_VECTOR4, SEM_COLOR));
    ...
    SharedPtr<Material> renderMaterial(new Material(context_));
    renderMaterial->SetTechnique(0, cache->GetResource<Technique>("Techniques/NoTextureUnlitVColor.xml"));
    ....
    StaticModel* object2 = node2->CreateComponent<StaticModel>();
    object2->SetModel(fromScratchModel);
    object2->SetMaterial(renderMaterial);

Thanks!

-------------------------

cap | 2017-04-06 12:12:05 UTC | #6

Hey all, SteveU3D and I have discussed this question a bit, and I thought I'd share some code fragments that were helpful. It's not exactly self-documenting, but for those determined enough to do per-vertex coloring it may be helpful.
```
struct VertexData
{
	Vector3 position; // size of 12 bytes +
	Vector3 normal; // size of 12 bytes +
	unsigned color;
};

void BasicArraysFromMesh(vector<VertexData>& vertexData, vector<int>& indexData, Mesh& mesh)
{
	std::vector<double> verts = mesh.get_vertices();
	std::vector<int> faces = mesh.get_faces();

	//data for Urho - we double vertices for face normals
	int triCount = faces.size() / 3;
	int numVertices = faces.size();

	//resize containers
	vertexData.resize(numVertices);
	indexData.resize(triCount * 3);

	//draw with duplication vertices
	for(int i = 0; i < triCount; i++)
	{
		//calc normal
		Vector3 v1(verts[3 * faces[3 * i + 0] + 0], verts[3 * faces[3 * i + 0] + 1], verts[3 * faces[3 * i + 0] + 2]);
		Vector3 v2(verts[3 * faces[3 * i + 1] + 0], verts[3 * faces[3 * i + 1] + 1], verts[3 * faces[3 * i + 1] + 2]);
		Vector3 v3(verts[3 * faces[3 * i + 2] + 0], verts[3 * faces[3 * i + 2] + 1], verts[3 * faces[3 * i + 2] + 2]);				
		Vector3 edge1 = v1 - v2;
		Vector3 edge2 = v1 - v3;
		Vector3 n = edge1.CrossProduct(edge2).Normalized();

		//initialize with default color
		Color faceColor = Color::GRAY;

		VertexData vd1;
		vd1.position = v1;
		vd1.normal = n;
		vd1.color = faceColor.ToUInt();

		VertexData vd2;
		vd2.position = v2;
		vd2.normal = n;
		vd2.color = faceColor.ToUInt();

		VertexData vd3;
		vd3.position = v3;
		vd3.normal = n;
		vd3.color = faceColor.ToUInt();

		vertexData[3*i + 0] = vd1;
		vertexData[3*i + 1] = vd2;
		vertexData[3*i + 2] = vd3;

		indexData[3*i] = 3*i;
		indexData[3*i + 1] = 3*i + 1;
		indexData[3*i + 2] = 3*i + 2;
	}
}

int DrawMeshWithVertexColors(Mesh mesh, Matrix3x4 transform, vector<Color> colors)
{
	int id = -1;

	vector<VertexData> vertexData;
	vector<int> indexData;

	//extract basic arrays
	BasicArraysFromMesh(vertexData, indexData, mesh);

	//assign the colors
	for(int i = 0; i < vertexData.size()/3; i++)
	{
		Color faceCol = Color::GRAY;
		if(colors.size() > 0)
			faceCol = colors[i % colors.size()];

		vertexData[3*i + 0].color = faceCol.ToUInt();
		vertexData[3*i + 1].color = faceCol.ToUInt();
		vertexData[3*i + 2].color = faceCol.ToUInt();
	}

	//call the lower level functions
	id = DrawModelFromBasicArrays(&vertexData[0], 
		vertexData.size(), 
		&indexData[0], 
		indexData.size()/3,
		transform,
		"Materials/VColUnlit.xml"); 

	return id;
}

int DrawModelFromBasicArrays(
  VertexData* vertex_data,
  int num_verts,
  int* index_data,
  int num_faces,
  Matrix3x4 transform,
  String material,
  Scene* scene
)
{
	
	//Get the current scene from app instance
	if(scene == NULL)
		return -1;
	
	Context* context = GetContext();
	SharedPtr<VertexBuffer> vb(new VertexBuffer(context));
	SharedPtr<IndexBuffer> ib(new IndexBuffer(context));
	SharedPtr<Geometry> geom(new Geometry(context));

	// Shadowed buffer needed for raycasts to work, and so that data can be automatically restored on device loss
	vb->SetShadowed(true);
	vb->SetSize(num_verts, MASK_POSITION|MASK_NORMAL|MASK_COLOR);
	vb->SetData((void*)vertex_data);

	ib->SetShadowed(true);
	ib->SetSize(num_faces * 3, true);
	ib->SetData(index_data);

	geom->SetVertexBuffer(0, vb);
	geom->SetIndexBuffer(ib);
	geom->SetDrawRange(TRIANGLE_LIST, 0, num_faces * 3);

	SharedPtr<Model> fromScratchModel(new Model(context));
	fromScratchModel->SetNumGeometries(1);
	fromScratchModel->SetGeometry(0, 0, geom);
	//fromScratchModel->SetGeometry(1, 0, geom);

	//calc bounding box
	Vector<Vector3> vertices;
	for(int i = 0; i < num_verts; i++)
	{
		vertices.Push(vertex_data[i].position);
	}
	fromScratchModel->SetBoundingBox(BoundingBox(&vertices[0], vertices.Size()));

	//add to the scene
	ResourceCache* cache = GetSubsystem<ResourceCache>();
	Material* gMat = cache -> GetResource<Material>(material);
	//Material* wMat = cache->GetResource<Material>("Materials/BasicDiffWireframe.xml");

	Node* new_node = scene->CreateChild("new_obj");
	StaticModel* object = new_node->CreateComponent<StaticModel>();
	object->SetModel(fromScratchModel);
	if(gMat != NULL)
	{
		SharedPtr<Material> tmpMat = gMat -> Clone();
		object->SetMaterial(0,tmpMat);
	}
	//object->SetMaterial(1,wMat);
	object->SetCastShadows(true);

	//set the transform
	new_node->SetTransform(transform.Translation(), transform.Rotation(), transform.Scale());

	return new_node->GetID();
}
```

-------------------------

Sinoid | 2017-04-07 04:22:56 UTC | #7

You can make some bogus calls to VertexBuffer::GetElementOffset and print them to the log to help you with your struct layout. I'd assume though that color being 32bit was probably the big gotcha - color still catches me.

*Note:* don't lock any of this into your head for anything but vertex buffers, the layout rules change for both constant buffers and compute. C-side will not map nicely there as you have 1, 2, and 4 element vectors - that's all, the constant-buffer/compute side code is just sugar defaulting to xyz instead of xyzw. You get some narly bugs mapping an array of C-side vector3's to compute.

-------------------------

