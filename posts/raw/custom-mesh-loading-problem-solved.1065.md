Dave82 | 2017-01-02 01:05:09 UTC | #1

Hi , i finished my mesh loader but  i can't get it to work properly... It seems that the data is loaded correctly , but it's always 1/3 of my mesh is rendered (i'm assuming that theres something wrong with the index buffer but can't figure it out , its like the draw range should be indexCount * 3...) 

There should be 10 spheres on this picture but only 3.33 of them are visible :
[img]http://s28.postimg.org/4q54fxxpp/spheres.jpg[/img]

Here's my loading code (NOTE : I used the push method to fill the buffers so it's easier to read the code)


[code]Urho3D::StaticModel * TFSceneLoader::readStaticModel(Urho3D::File &file)
{
	// parse the file and load the corresponding data (exported from 3ds max)
	int numMeshBuffers = file.ReadInt();

	// Use dynamic lighting ? (Not used in Urho3D)
	bool useDynamicLighting = file.ReadBool();

	// list of all materials used by this model
	Urho3D::Vector<Urho3D::SharedPtr<Urho3D::Material> > materials;

	INFLOG("---------- LOADING MESH STARTED --------------------\n");
	INFLOG("       Num mesh buffers : %d " , numMeshBuffers)

	// first read materials.They are stored in the same order as the VertexBuffers
	for (int x = 0; x < numMeshBuffers; x++)
	{
		Urho3D::SharedPtr<Urho3D::Material> mat(readMaterial(file));
		materials.Push(mat);
	}
	
	Urho3D::SharedPtr<Urho3D::Model> model(new Urho3D::Model(context_));
	model->SetNumGeometries(numMeshBuffers);

	Urho3D::BoundingBox bb;

	// read Geometries (mesh buffers in irrlicht)
	// One geometry component holds 1 vertex and index buffer
	for (int m = 0; m < numMeshBuffers; m++)
	{
		Urho3D::SharedPtr<Urho3D::Geometry> newGeometry(new Urho3D::Geometry(context_));
		
		int numVertices = file.ReadInt();
		char uvSets = file.ReadByte();

		INFLOG("              Num Vertices : %d " , numVertices)
		INFLOG("              Vertex type : %d " , uvSets)

		unsigned int vertexDecl = Urho3D::MASK_POSITION|Urho3D::MASK_NORMAL|Urho3D::MASK_TEXCOORD1;
		if (uvSets == 2) vertexDecl |= Urho3D::MASK_TEXCOORD2;
		
		// Create vertexData buffer
		Urho3D::Vector<float> vertexData;

		for (int v = 0; v < numVertices; v++)
		{
			Urho3D::Vector3 pos = file.ReadVector3(); 
			Urho3D::Vector3 normal = file.ReadVector3(); 
			Urho3D::Vector2 uv1 = file.ReadVector2();

			vertexData.Push(pos.x_); vertexData.Push(pos.y_); vertexData.Push(pos.z_);
			vertexData.Push(normal.x_); vertexData.Push(normal.y_); vertexData.Push(normal.z_);
			vertexData.Push(uv1.x_); vertexData.Push(uv1.y_);
                                          
                                          // If there's 2nd uv set for lightmap...
			if (vertexDecl & Urho3D::MASK_TEXCOORD2)
			{
				Urho3D::Vector2 uv2 = file.ReadVector2();
				vertexData.Push(uv2.x_);
				vertexData.Push(uv2.y_);
			}
			// store aabb point;
			bb.Merge(pos);
		}

		// read index buffer :
		int indexCount =  file.ReadInt();
		Urho3D::Vector<unsigned short> indexData;

		INFLOG("              Num indices : %d " , indexCount)

		for (int ib = 0; ib < indexCount; ib++)
		{
			indexData.Push(file.ReadUShort());
			indexData.Push(file.ReadUShort());
			indexData.Push(file.ReadUShort());
		}
	
		// create vertex buffer
		Urho3D::SharedPtr<Urho3D::VertexBuffer> vertexBuffer(new Urho3D::VertexBuffer(context_));
		vertexBuffer->SetShadowed(true);
		vertexBuffer->SetSize(numVertices , vertexDecl);
		vertexBuffer->SetData(&vertexData[0]);
		
		// create index buffer
		Urho3D::SharedPtr<Urho3D::IndexBuffer> indexBuffer(new Urho3D::IndexBuffer(context_));
		indexBuffer->SetShadowed(true);
		indexBuffer->SetSize(indexCount , false);
		indexBuffer->SetData(&indexData[0]);
	
		// add buffers to geometry
		newGeometry->SetVertexBuffer(0 , vertexBuffer);
		newGeometry->SetIndexBuffer(indexBuffer);
		newGeometry->SetDrawRange(Urho3D::TRIANGLE_LIST, 0, indexCount);

		model->SetGeometry(m , 0 , newGeometry);
		model->SetNumGeometryLodLevels(m,1);	
	}

	model->SetBoundingBox(bb);

	INFLOG("---------- LOADING MESH FINISHED --------------------\n");

	Urho3D::StaticModel * staticModel = new Urho3D::StaticModel(context_);
	staticModel->SetModel(model);
	
	for (int m = 0; m < numMeshBuffers; m++)
	{
		staticModel->SetMaterial(materials[m]);
	}
	return staticModel;
}[/code]


I checked : i load the correct number of vertices and indices.

-------------------------

Dave82 | 2017-01-02 01:05:10 UTC | #2

AHHH how could i be so blind... i had to 

[code]indexBuffer->SetSize(indexCount * 3, false);[/code]

and not

[code]indexBuffer->SetSize(indexCount , false);[/code]

It works perfectly now...

-------------------------

