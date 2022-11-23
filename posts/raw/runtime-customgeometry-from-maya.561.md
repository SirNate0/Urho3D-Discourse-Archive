sabotage3d | 2017-01-02 01:01:22 UTC | #1

Hello ,
I am trying to figure out how to pass custom geometry to Urho3d from Maya at runtime . I looked in here: [github.com/urho3d/Urho3D/issues/470](https://github.com/urho3d/Urho3D/issues/470)
Ideally I would like to be able to set Urho3d material and rigid body components. 
I exported a simple cube from Maya as an array of vertices and indices.
I am not sure what is the winding in Urho3d . Is it CCW or CW also because in Maya Y is up do I have to rearrange the data ?
This is a simple cube form maya: [codepad.org/O8Muy8U7](http://codepad.org/O8Muy8U7)

Thanks in advance,

Alex

-------------------------

codingmonkey | 2017-01-02 01:01:22 UTC | #2

Hi! And you looked sample 34_DynamicGeometry ?

I recently did something like this,dynMesh with my material(alpha texture) but w/o rigidbody, I think for him to need the right boundbox or something else.

default line of trianles_strip in start proc of script
[code]

typedef struct DYN_VERTEX 
{
	Vector3 p;
	Vector3 n;
	Vector2 uv;
} DYN_VERTEX;

void LineGenerator::Start()
{
	ResourceCache* cache = GetSubsystem<ResourceCache>();

	tailLength_ = 20;
	
	fromScratchModel = new Model(context_);
	vb = new VertexBuffer(context_);
	ib = new IndexBuffer(context_);
	geom = new Geometry(context_);
	
	const unsigned numVertices = tailLength_* 4;

	PODVector<DYN_VERTEX> vertexData;
	vertexData.Resize(numVertices);
	PODVector<unsigned short> indexData;
	indexData.Resize(numVertices);

	Vector3 xstep = Vector3(1.0f, 0.0f, 0.0f);
	Vector3 ystep = Vector3(0.0f, 1.0f, 0.0f);
	Vector3 curPos = Vector3(0,0.0f,0);

	for (int i =0; i < (numVertices); i += 4) 
	{
		vertexData[i].p = curPos;
		curPos += ystep;
		vertexData[i+1].p = curPos;
		curPos += xstep;
		curPos -= ystep;
		vertexData[i+2].p = curPos;
		curPos += ystep;
		vertexData[i+3].p = curPos;
		curPos -= ystep;

		vertexData[i].n = Vector3::UP;
		vertexData[i+1].n = Vector3::UP;
		vertexData[i+2].n = Vector3::UP;
		vertexData[i+3].n = Vector3::UP;

		vertexData[i].uv = Vector2(0.0f, 0.0);
		vertexData[i+1].uv = Vector2(0.0f, 1.0f);
		vertexData[i+2].uv = Vector2(1.0f, 0.0f);
		vertexData[i+3].uv = Vector2(1.0f, 1.0f);

	}
	//indexes
	for (int i =0; i < numVertices; ++i) 
	{
		indexData[i]=i;
	}

	//vb->SetShadowed(true);
	vb->SetSize(numVertices, MASK_POSITION|MASK_NORMAL|MASK_TEXCOORD1);
	vb->SetData(&vertexData[0]);
	

	ib->SetShadowed(true);
	ib->SetSize(numVertices, false);
	ib->SetData(&indexData[0]);

	geom->SetVertexBuffer(0, vb);
	geom->SetIndexBuffer(ib);
	geom->SetDrawRange(TRIANGLE_STRIP, 0, numVertices);
	

	fromScratchModel->SetNumGeometries(1);
	fromScratchModel->SetGeometry(0, 0, geom);
	fromScratchModel->SetBoundingBox(BoundingBox(Vector3(-5.0f, -5.0f, -5.0f), Vector3(5.0f, 5.0f, 5.0f)));

	dynNode_ = GetNode()->GetScene()->CreateChild("dynNode", LOCAL);
	StaticModel* object = dynNode_->CreateComponent<StaticModel>();
	object->SetModel(fromScratchModel);

	object->SetMaterial(cache->GetResource<Material>("Materials/LineGenerator.xml"));
}
[/code]

Completely all, you can save through a blender or AssetImporter, then read vertex buffer from model and modify it as needed in code.
Save from maya to some format for example obj and open with blender and reexport to *.mdl with individuale frefab options in exporter.
And of course you will need add-on for blender install, befor this all.

-------------------------

sabotage3d | 2017-01-02 01:01:22 UTC | #3

Thanks that's will be useful. 
Can we query vertices and indices from Urho3d loaded model ?
Technically I need to pass a model to Urho3d let say an mdl. Then I need to read the vertices and indices. Manipulate them at runtime and then write the new vertices and indices .

-------------------------

cadaver | 2017-01-02 01:01:23 UTC | #4

When you enable CPU memory shadowing on the vertex & index buffers (Model::Load() normally always enables it, and you should do too in any custom defined VBs/IBs meant for "model-like" use), you can inspect the raw vertex buffer & index buffer data. This is the same what raycasts are using. Look for eg. VertexBuffer::GetShadowData() and Geometry::GetRawData() from the codebase to get you started. Access to the vertices as convenient C++ classes like Vector3 is not directly provided.

Using CustomGeometry for serious geometry modification is not recommended, as it only provides unindexed data mode. That's only meant for simple "immediate mode" -like geometry definition and script access.

-------------------------

codingmonkey | 2017-01-02 01:01:23 UTC | #5

>Can we query vertices and indices from Urho3d loaded model ?

I think yes )

I fill vb with my ganerated mesh
like that
[code]
		if (tailMesh_.Size() < 1) return;

		//gen vb
		unsigned vertexSize = vb->GetVertexSize();
		unsigned numVertexes = vb->GetVertexCount();

		DYN_VERTEX* vertexData = (DYN_VERTEX*)vb->Lock(0, vb->GetVertexCount());
		if (vertexData) 
		{
			memcpy(vertexData, &tailMesh_[0], tailMesh_.Size() * vertexSize);
		}
		vb->Unlock();
[/code]
just need a pointer to VB from model, i get it then script starts

and i gusess that IB may changed with same way.

-------------------------

sabotage3d | 2017-01-02 01:01:23 UTC | #6

I will try that tonight thanks a lot :slight_smile:

-------------------------

codingmonkey | 2017-01-02 01:01:23 UTC | #7

>When you enable CPU memory shadowing on the vertex & index buffers (Model::Load() normally always enables it
you mean this shadow (ing) ?
[code]indexBuffer->SetShadowed(true);[/code]
and I thought it was something about real shadows and 'OFF' it   :laughing:

-------------------------

cadaver | 2017-01-02 01:01:23 UTC | #8

Yes. That enables two quite important things:

- CPU access through GetRawData() without locking the buffer, which raycasts want to use
- Automatic restore of data on platforms where it's possible to lose the GPU context (Android and also desktop OpenGL when switching modes)

-------------------------

sabotage3d | 2017-01-02 01:01:48 UTC | #9

Hey guys,

I am having some problems extracting the indices data from a model.
I am doing something like this but I am not sure if it is correct. 
Is there a more convenient way of doing this lets say with Assimp API ?

[code]  
    IndexBuffer* indexBuffer = originalModel->GetGeometry(0, 0)->GetIndexBuffer();
    
    const unsigned char* indexData = (const unsigned char*)indexBuffer->Lock(0, indexBuffer->GetIndexCount());
    
    unsigned numIndices = indexBuffer->GetIndexCount();
    unsigned indexSize = indexBuffer->GetIndexSize();
    
    for (unsigned i = 0; i < numIndices ; ++i)
    {
        const int &iData = *reinterpret_cast<const int*>(indexData + i * indexSize);
        
        std::cout << iData << std::endl;
    }[/code]

-------------------------

codingmonkey | 2017-01-02 01:01:48 UTC | #10

i'm try extract indexes from ib and just write indexes in log )
there is my code of that:

[code]
	Node* planeNode = scene_->GetChild("plane", true);
	StaticModel* model = planeNode->GetComponent<StaticModel>();

	IndexBuffer* ib = model->GetLodGeometry(0, 0)->GetIndexBuffer();

	int len = ib->GetIndexSize(); // 2 bytes(WORD)= (unsigned short) 0-65k indexes
	int count = ib->GetIndexCount(); // 6 = 2 tris
	
	Log* log = GetSubsystem<Log>();
	log->Open("log.txt");


	unsigned short* indexes = (unsigned short*)ib->Lock(0, count);

	for (int i=0; i < count; i++) 
	{
		unsigned short index = indexes[i];
		log->Write(0, String("index:" + String(index)));	
	}

	ib->Unlock();
[/code]

[quote]
[Sun Dec 07 02:48:14 2014] INFO: Opened log file log.txt
[Sun Dec 07 02:48:14 2014] DEBUG: index:1
[Sun Dec 07 02:48:14 2014] DEBUG: index:0
[Sun Dec 07 02:48:14 2014] DEBUG: index:3
[Sun Dec 07 02:48:14 2014] DEBUG: index:3
[Sun Dec 07 02:48:14 2014] DEBUG: index:2
[Sun Dec 07 02:48:14 2014] DEBUG: index:1
[Sun Dec 07 02:48:14 2014] DEBUG: Reloading shaders
[/quote]

-------------------------

sabotage3d | 2017-01-02 01:01:48 UTC | #11

Thanks a lot. But I am having problems converting the data back into a model this is my code: [codepad.org/x5csLmkL](http://codepad.org/x5csLmkL)
I have converted a cube from obj to mdl using the AssetImporter .
It is 8 vertices and 36 indices .
When I query the geometry with the code above I am getting exactly that but when I try to create the same geometry I am having problems as the vertices and indices are different sizes.

The problem is in that part of the code below.

Indices size: 2
Indices count: 36
Vertex size: 24
Vertex count: 8

[code]vb->SetShadowed(true);
vb->SetSize(vertexCount,  MASK_POSITION|MASK_NORMAL);
vb->SetData(vertexArray);

ib->SetShadowed(true);
ib->SetSize(indicesCount, false);
ib->SetData(indicesArray);

geom->SetVertexBuffer(0, vb);
geom->SetIndexBuffer(ib);
geom->SetDrawRange(TRIANGLE_LIST, 0, vertexCount);[/code]

-------------------------

sabotage3d | 2017-01-02 01:01:50 UTC | #12

Is there a way to query normals and uvs ? Are they stored in the vertex buffer ? When I query the vertex buffer I am getting only the positions of the vertices .

-------------------------

