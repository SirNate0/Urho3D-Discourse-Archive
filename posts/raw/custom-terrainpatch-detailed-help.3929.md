vivienneanthony | 2018-01-13 19:40:41 UTC | #1

I made some code that creates a sphere as a sample program. 


A example is :slight_smile:
https://imgur.com/a/jpGMw

I am converting the code to be similar to the https://www.youtube.com/watch?v=rL8zDgTlXso and https://drive.google.com/open?id=1pMkiKikuD0tkTFc0e7S-olPw2-dfKPrm.

The example of the code is here:
http://www.youtube.com/watch?v=rL8zDgTlXso

The first goal is to copy the code into a new file and code  structure. Meaning a Sphere Terain that has six faces as SphereTerrainFace that has a node As SphereTerrainNode that can be a Patch with topology, or have four children of Nodes with topology. The code rework seems correct..

**My main problem is I can’t get the geometry to appear. I am using Urho3d Terrain.h, Terrain.cpp, TerrainPatch.h, and TerrainPatch.cpp.  TerrainPatch.h as a example to work from but I am missing something. I just hoping to get the sphere correct.**

Looking at the following console output. The faces are being created and the index data.

The three primary code files are below but you can see the rest. If I can get it to work I can pull it into the Urho3D base code with the full real-time or static generation.

SphereTerrain
[code]

SphereTerrain::SphereTerrain(Context * context) :
		LogicComponent(context), m_Material(nullptr), m_MaterialShaderEnable(
				false) {

	m_Radius = 1;

	Build(m_Radius);

}

// Build
void SphereTerrain::Build(double radius) {
	// Set initial radius
	m_Radius = radius;

	// Create sides
	for (unsigned int i = 0; i < 6; i++) {
		// Debug
		ALPHAENGINE_LOGINFO("Creating SphereTerrain Face " + String(i));

		// Create Face
		m_SphereTerrainFace[i] = new SphereTerrainFace(g_pApp->GetContext(),
				this, (STFaceDirection) i);
	}

	// Build sides
	for (unsigned int i = 0; i < 6; i++) {
		// Debug
		ALPHAENGINE_LOGINFO("Build SphereTerrain Face " + String(i));

		// Build face
		m_SphereTerrainFace[i]->Build();
	}
}

void SphereTerrain::RegisterObject(Context* context) {
	context->RegisterFactory<SphereTerrain>();
}

SphereTerrain::~SphereTerrain() {

	// Create sides
	for (unsigned int i = 0; i < 6; i++) {
		delete m_SphereTerrainFace[i];
	}
}

// Set Material Recursive to all Patches
void SphereTerrain::SetMaterial(Material * material) {
	// Create sides
	for (unsigned int i = 0; i < 6; i++) {
		m_SphereTerrainFace[i]->SetMaterial(material);
	}
}

[/code]

SphereTerrainPatch
[code]
SphereTerrainPatch::SphereTerrainPatch(Context * context,
		SphereTerrainNode * node = nullptr) :
		Drawable(context, DRAWABLE_GEOMETRY), m_pNode(node), m_pVertexBuffer(
				new VertexBuffer(context)), m_pIndexBuffer(
				new IndexBuffer(context)), m_pGeometry(new Geometry(context)), m_pTopology(
				new SphereTerrainTopology(context, this)), m_pOcclusionBuffer(
				new OcclusionBuffer(context)) {

	// Resize batches
	batches_.Resize(1);

	batches_[0].geometry_ = m_pGeometry;
	batches_[0].geometryType_ = GEOM_STATIC_NOINSTANCING;

	m_BoundingBox.Clear();

	node_ = this->GetNode();
}

void SphereTerrainPatch::RegisterObject(Context* context) {
	context->RegisterFactory<SphereTerrainPatch>();
}

void SphereTerrainPatch::Build() {

	// Debug
	ALPHAENGINE_LOGINFO("Generate Topology ...");

	// Generate Topology and Describe the Type
	m_pTopology->GenerateTopology();

	// Get Topology and set Vertex Buffer
	ALPHAENGINE_LOGINFO("Create vertex data ...");

	// We could use the "legacy" element bitmask to define elements for more compact code, but let's demonstrate
	// defining the vertex elements explicitly to allow any element types and order
	PODVector<VertexElement> elements;
	elements.Push(VertexElement(TYPE_VECTOR3, SEM_POSITION));

	m_pVertexBuffer->SetSize(m_pTopology->GetVertexCounts(), MASK_POSITION,
			false);

	ALPHAENGINE_LOGINFO("Set vertex data ...");
	m_pVertexBuffer->SetData((unsigned char*) m_pTopology->GetVertexData());

	ALPHAENGINE_LOGINFO("Set index data ...");
	m_pIndexBuffer->SetSize(m_pTopology->GetIndexCounts(), false, false);
	m_pIndexBuffer->SetData((unsigned char*) m_pTopology->GetIndexData());

	m_pIndexBuffer->SetShadowed(true);

	m_pIndexBuffer->SetDataRange(m_pTopology->GetIndexData(), 0,
			m_pTopology->GetIndexCounts(), false);

	// Set Geometry to VertexBuffer
	m_pGeometry->SetNumVertexBuffers(1);
	m_pGeometry->SetVertexBuffer(0, m_pVertexBuffer);
	m_pGeometry->SetIndexBuffer(m_pIndexBuffer);

	// Set Draw Range
	m_pGeometry->SetDrawRange(TRIANGLE_LIST, 0, m_pTopology->GetIndexCounts(),
			0, m_pTopology->GetVertexCounts(), false);

	// Add to BOunding box
	ALPHAENGINE_LOGINFO("Vertex Data (Triangles<3) ...");

	float * vectorData = m_pTopology->GetVertexData();
	unsigned int * indexData = m_pTopology->GetIndexData();

	for (unsigned int i = 0; i < 6; i++) {
		Vector3 vectordata;

		for (unsigned int j = 0; j < 3; j += 3) {
			vectordata.x_ = vectorData[(i * 3) + j];
			vectordata.y_ = vectorData[(i * 3) + j + 1];
			vectordata.z_ = vectorData[(i * 3) + j + 2];
		}

		ALPHAENGINE_LOGINFO("VectorData "+vectordata.ToString());
	}

	ALPHAENGINE_LOGINFO(
			"IndexData"+ " " +String(indexData[0])+ " " +String(indexData[1])+ " " +String(indexData[2])+ " " +String(indexData[3])+ " " +String(indexData[4])+ " " +String(indexData[5])+ " " +String(indexData[6]));

	// Add to BOunding box
	ALPHAENGINE_LOGINFO("Generate bounding box ...");

	for (unsigned int i = 0; i < m_pTopology->GetVertexCounts() * 3; i += 3) {
		Vector3 vec = Vector3(vectorData[i], vectorData[i + 1],
				vectorData[i + 2]);
		m_BoundingBox.Merge(vec);

		if (i < 7) {
			ALPHAENGINE_LOGINFO("Adding boundary "+ vec.ToString());
		}
	}

	// Set bounding box
	boundingBox_ = m_BoundingBox;

	// Set Lod
	m_pGeometry->SetLodDistance(0);

	//Set Draw
	drawDistance_ = 1000.f;

	// Draw
	m_pGeometry->Draw(g_pApp->GetGraphics());

	OnMarkedDirty(node_);

}

SphereTerrainPatch::~SphereTerrainPatch() {

}

void SphereTerrainPatch::OnWorldBoundingBoxUpdate() {
	worldBoundingBox_ = boundingBox_.Transformed(node_->GetWorldTransform());
}

STFaceDirection SphereTerrainPatch::GetFaceDirection() {
	m_pNode->GetFaceDirection();
}

void SphereTerrainPatch::SetMaterial(Material * material) {
	// Set material
	m_pMaterial = material;

	// Set the batch material
	batches_[0].material_ = material;
}

bool SphereTerrainPatch::DrawOcclusion(OcclusionBuffer* buffer) {
	bool success = true;

	if (!m_pGeometry) {
		return false;
	}

	// Check that the material is suitable for occlusion (default material always is) and set culling mode
	buffer->SetCullMode(CULL_CW);

	const unsigned char* vertexData;
	unsigned vertexSize;
	const unsigned char* indexData;
	unsigned indexSize;
	const PODVector<VertexElement>* elements;

	m_pGeometry->GetRawData(vertexData, vertexSize, indexData, indexSize,
			elements);

	// Check for valid geometry data
	if (!vertexData || !elements
			|| VertexBuffer::GetElementOffset(*elements, TYPE_VECTOR3,
					SEM_POSITION) != 0) {
		return false;
	}

	// Draw and check for running out of triangles
	success = buffer->AddTriangles(this->GetNode()->GetWorldTransform(),
			vertexData, vertexSize, m_pGeometry->GetVertexStart(),
			m_pGeometry->GetVertexCount());

	return success;
}

void SphereTerrainPatch::UpdateBatches(const FrameInfo& frame) {
	const Matrix3x4& worldTransform = node_->GetWorldTransform();
	distance_ = frame.camera_->GetDistance(GetWorldBoundingBox().Center());

	float scale = worldTransform.Scale().DotProduct(DOT_SCALE);
	lodDistance_ = frame.camera_->GetLodDistance(distance_, scale, lodBias_);

	// set distance from camera and world transform
	batches_[0].distance_ = distance_;
	batches_[0].worldTransform_ = &worldTransform;
}

void SphereTerrainPatch::ProcessRayQuery(const RayOctreeQuery& query,
		PODVector<RayQueryResult>& results) {
	RayQueryLevel level = query.level_;

	switch (level) {
	case RAY_AABB:
		Drawable::ProcessRayQuery(query, results);
		break;

	case RAY_OBB:
	case RAY_TRIANGLE: {
		Matrix3x4 inverse(node_->GetWorldTransform().Inverse());
		Ray localRay = query.ray_.Transformed(inverse);
		float distance = localRay.HitDistance(boundingBox_);
		Vector3 normal = -query.ray_.direction_;

		if (level == RAY_TRIANGLE && distance < query.maxDistance_) {
			Vector3 geometryNormal;
			distance = m_pGeometry->GetHitDistance(localRay, &geometryNormal);
			normal =
					(node_->GetWorldTransform() * Vector4(geometryNormal, 0.0f)).Normalized();
		}

		if (distance < query.maxDistance_) {
			RayQueryResult result;
			result.position_ = query.ray_.origin_
					+ distance * query.ray_.direction_;
			result.normal_ = normal;
			result.distance_ = distance;
			result.drawable_ = this;
			result.node_ = node_;
			result.subObject_ = M_MAX_UNSIGNED;
			results.Push(result);
		}
	}
		break;

	case RAY_TRIANGLE_UV:
		URHO3D_LOGWARNING(
				"RAY_TRIANGLE_UV query level is not supported for TerrainPatch component");
		break;
	}
}


[/code]

SpereTerrainTopology
[code]
SphereTerrainTopology::SphereTerrainTopology(Context * context,
		SphereTerrainPatch * Patch = nullptr) :
		Object(context), m_pPatch(Patch) {
}

void SphereTerrainTopology::RegisterObject(Context* context) {
	context->RegisterFactory<SphereTerrainTopology>();
}

// Build Data
void SphereTerrainTopology::GenerateTopology() {
// Vertex and Index Data
	m_pVertexData = (float *) new float[6 * 3 * PATCH_VERTICES_TOTAL];
	m_pIndexData = (unsigned int *) new unsigned int[PATCH_VERTICES_TOTAL * 6];

	// Set Cube size
	float CubeSize = 10;


	// cleare data
	float * pVertexReference = nullptr;
	m_IndexCount = 0;
	m_VertexCount = 0;

	// Get Cube Center - Create Defaults
	Vector3 center = Vector3::ZERO;
	Vector3 direction_x = Vector3::ZERO;
	Vector3 direction_y = Vector3::ZERO;

	// Create a index
	unsigned short index = 0;

	// Element total size easier to count
	unsigned int VertexElementTotalSize = 6 * 3;

	STFaceDirection faceDirection = m_pPatch->GetFaceDirection();

	// Get Cube Center
	center = (float) CubeSize / 2 * TerrainFaceCoordinate[faceDirection];


	unsigned int face = (unsigned int) faceDirection;

	// Calculate direction based of x
	switch (face) {
	case 0:
		direction_x = CubeSize * Vector3(0, -1, 0);
		direction_y = CubeSize * Vector3(0, 0, 1);
		break;
	case 1:
		direction_x = CubeSize * Vector3(0, -1, 0);
		direction_y = CubeSize * Vector3(0, 0, -1);
		break;
	case 2:
		direction_x = CubeSize * Vector3(0, 0, 1);
		direction_y = CubeSize * Vector3(1, 0, 0);
		break;
	case 3:
		direction_x = CubeSize * Vector3(0, 0, 1);
		direction_y = CubeSize * Vector3(-1, 0, 0);
		break;
	case 4:
		direction_x = CubeSize * Vector3(0, -1, 0);
		direction_y = CubeSize * Vector3(-1, 0, 0);
		break;
	case 5:
		direction_x = CubeSize * Vector3(0, -1, 0);
		direction_y = CubeSize * Vector3(1, 0, 0);
		break;
	}

	// loop through and create a grid of vertices. // do not draw edge
	for (int u = 0; u < PATCH_VERTICES; u++) {
		for (int v = 0; v < PATCH_VERTICES; v++) {
			// Calculate patch size
			Vector3 x0 = (direction_x / PATCH_VERTICES)
					* (v - PATCH_VERTICES / 2);
			Vector3 y0 = (direction_y / PATCH_VERTICES)
					* (u - PATCH_VERTICES / 2);

			// Create the vertex grid around the center of thecube face (which is passed into the function as Vector3 center).
			Vector3 v0 = center + x0 + y0;

			// Calculate patch size
			Vector3 x1 = (direction_x / PATCH_VERTICES)
					* (v - PATCH_VERTICES / 2);
			Vector3 y1 = (direction_y / PATCH_VERTICES)
					* ((u + 1) - PATCH_VERTICES / 2);

			// Create the vertex grid around the center of thecube face (which is passed into the function as Vector3 center).
			Vector3 v1 = center + x1 + y1;

			// Calculate patch size
			Vector3 x2 = (direction_x / PATCH_VERTICES)
					* ((v + 1) - PATCH_VERTICES / 2);
			Vector3 y2 = (direction_y / PATCH_VERTICES)
					* (u - PATCH_VERTICES / 2);

			// Create the vertex grid around the center of thecube face (which is passed into the function as Vector3 center).
			Vector3 v2 = center + x2 + y2;

			// Calculate patch size
			Vector3 x3 = (direction_x / PATCH_VERTICES)
					* ((v + 1) - PATCH_VERTICES / 2);
			Vector3 y3 = (direction_y / PATCH_VERTICES)
					* ((u + 1) - PATCH_VERTICES / 2);

			// Create the vertex grid around the center of thecube face (which is passed into the function as Vector3 center).
			Vector3 v3 = center + x3 + y3;

			unsigned int position = (u * PATCH_SIZE * VertexElementTotalSize)
					+ (v * VertexElementTotalSize);

			pVertexReference = &m_pVertexData[position];

			// copy into memory testing - quad and normal
			*pVertexReference = v0.x_;
			*pVertexReference++;
			*pVertexReference = v0.y_;
			*pVertexReference++;
			*pVertexReference = v0.z_;
			*pVertexReference++;

			m_VertexCount++;

			*pVertexReference = v1.x_;
			*pVertexReference++;
			*pVertexReference = v1.y_;
			*pVertexReference++;
			*pVertexReference = v1.z_;
			*pVertexReference++;

			m_VertexCount++;

			*pVertexReference = v3.x_;
			*pVertexReference++;
			*pVertexReference = v3.y_;
			*pVertexReference++;
			*pVertexReference = v3.z_;
			*pVertexReference++;

			m_VertexCount++;

			*pVertexReference = v0.x_;
			*pVertexReference++;
			*pVertexReference = v0.y_;
			*pVertexReference++;
			*pVertexReference = v0.z_;
			*pVertexReference++;

			m_VertexCount++;

			*pVertexReference = v3.x_;
			*pVertexReference++;
			*pVertexReference = v3.y_;
			*pVertexReference++;
			*pVertexReference = v3.z_;
			*pVertexReference++;

			m_VertexCount++;

			*pVertexReference = v2.x_;
			*pVertexReference++;
			*pVertexReference = v2.y_;
			*pVertexReference++;
			*pVertexReference = v2.z_;
			*pVertexReference++;

			m_VertexCount++;

			m_pIndexData[index] = index;
			index++;
			m_pIndexData[index] = index;
			index++;
			m_pIndexData[index] = index;
			index++;
			m_pIndexData[index] = index;
			index++;
			m_pIndexData[index] = index;
			index++;
			m_pIndexData[index] = index;
			index++;
		}
	}

	// Set Index Data Size
	m_IndexCount = index;

}

SphereTerrainTopology::~SphereTerrainTopology() {
}

void SphereTerrainTopology::AddTriangle(unsigned int position, Vector3 v1,
		Vector3 v2, Vector3 v3)
{
	float * pVertexReference = nullptr;
	pVertexReference = &m_pVertexData[position];

	// copy into memory testing - quad and normal
	*pVertexReference = v1.x_;
	*pVertexReference++;
	*pVertexReference = v1.y_;
	*pVertexReference++;
	*pVertexReference = v1.z_;
	*pVertexReference++;

	m_VertexCount++;

	*pVertexReference = v2.x_;
	*pVertexReference++;
	*pVertexReference = v2.y_;
	*pVertexReference++;
	*pVertexReference = v2.z_;
	*pVertexReference++;

	m_VertexCount++;

	*pVertexReference = v3.x_;
	*pVertexReference++;
	*pVertexReference = v3.y_;
	*pVertexReference++;
	*pVertexReference = v3.z_;
	*pVertexReference++;

	m_VertexCount++;

	m_pIndexData[position] = position;
	position++;
	m_pIndexData[position] = position;
	position++;
	m_pIndexData[position] = position;
	position++;

}

unsigned int SphereTerrainTopology::GetVertexCounts() const {

	return m_VertexCount;
}
;

unsigned int SphereTerrainTopology::GetIndexCounts() const {
	return m_IndexCount;
}
;

[/code]


Output Data

The sphere data made and put into a Geometry, IndexBuffer, and VertexBuffer in a TerrainPatch. and added to Drawable batch[0]_.  FIrst 6 vertices shown.

[code]
Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Creating SphereTerrain Face 0
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Creating SphereTerrain Face 1
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Creating SphereTerrain Face 2
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Creating SphereTerrain Face 3
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Creating SphereTerrain Face 4
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Creating SphereTerrain Face 5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Build SphereTerrain Face 0
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Build Terrain Node ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Generate Topology ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Create vertex data ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Set vertex data ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Set index data ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Vertex Data (Triangles<3) ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData 5 5 -5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData 5 5 -4.375
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData 5 4.375 -4.375
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData 5 5 -5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData 5 4.375 -4.375
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData 5 4.375 -5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] IndexData 0 1 2 3 4 5 6
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Generate bounding box ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Adding boundary 5 5 -5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Adding boundary 5 5 -4.375
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Adding boundary 5 4.375 -4.375
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Build SphereTerrain Face 1
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Build Terrain Node ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Generate Topology ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Create vertex data ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Set vertex data ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Set index data ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Vertex Data (Triangles<3) ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData -5 5 5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData -5 5 4.375
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData -5 4.375 4.375
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData -5 5 5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData -5 4.375 4.375
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData -5 4.375 5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] IndexData 0 1 2 3 4 5 6
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Generate bounding box ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Adding boundary -5 5 5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Adding boundary -5 5 4.375
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Adding boundary -5 4.375 4.375
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Build SphereTerrain Face 2
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Build Terrain Node ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Generate Topology ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Create vertex data ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Set vertex data ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Set index data ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Vertex Data (Triangles<3) ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData -5 -5 -5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData -4.375 -5 -5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData -4.375 -5 -4.375
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData -5 -5 -5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData -4.375 -5 -4.375
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData -5 -5 -4.375
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] IndexData 0 1 2 3 4 5 6
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Generate bounding box ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Adding boundary -5 -5 -5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Adding boundary -4.375 -5 -5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Adding boundary -4.375 -5 -4.375
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Build SphereTerrain Face 3
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Build Terrain Node ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Generate Topology ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Create vertex data ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Set vertex data ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Set index data ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Vertex Data (Triangles<3) ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData 5 5 -5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData 4.375 5 -5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData 4.375 5 -4.375
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData 5 5 -5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData 4.375 5 -4.375
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData 5 5 -4.375
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] IndexData 0 1 2 3 4 5 6
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Generate bounding box ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Adding boundary 5 5 -5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Adding boundary 4.375 5 -5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Adding boundary 4.375 5 -4.375
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Build SphereTerrain Face 4
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Build Terrain Node ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Generate Topology ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Create vertex data ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Set vertex data ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Set index data ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Vertex Data (Triangles<3) ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData 5 5 5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData 4.375 5 5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData 4.375 4.375 5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData 5 5 5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData 4.375 4.375 5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData 5 4.375 5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] IndexData 0 1 2 3 4 5 6
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Generate bounding box ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Adding boundary 5 5 5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Adding boundary 4.375 5 5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Adding boundary 4.375 4.375 5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Build SphereTerrain Face 5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Build Terrain Node ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Generate Topology ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Create vertex data ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Set vertex data ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Set index data ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Vertex Data (Triangles<3) ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData -5 5 -5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData -4.375 5 -5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData -4.375 4.375 -5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData -5 5 -5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData -4.375 4.375 -5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] VectorData -5 4.375 -5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] IndexData 0 1 2 3 4 5 6
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Generate bounding box ...
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Adding boundary -5 5 -5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Adding boundary -4.375 5 -5
[Sat Jan 13 14:02:44 2018] INFO: [ALPHAENGINE] Adding boundary -4.375 4.375 -5
[Sat Jan 13 14:02:56 2018] INFO: [ALPHAENGINE] Game logic life time is - 0.0064151 hours 0.384906 minutes 23.0943 seconds
[/code]

-------------------------

JTippetts | 2018-01-13 16:53:15 UTC | #5

You're not describing your problem very clearly, and it's not at all obvious what the problem is from your screenshot. You'd probably get more help if you could restate your problem. What do you expect to happen vs. what is actually happening.

-------------------------

vivienneanthony | 2018-01-13 17:03:33 UTC | #7

I reposted the message with more information and details. I hope it's clearer.

-------------------------

JTippetts | 2018-01-13 17:28:27 UTC | #8

In your posted code, I don't see where you are creating your bounding boxes. As a first step, you might want to verify that you're creating them correctly.

-------------------------

vivienneanthony | 2018-01-13 17:32:02 UTC | #9

Is that needed for the topology to render?

-------------------------

JTippetts | 2018-01-13 17:34:26 UTC | #10

Yeah, you need your bounding boxes to be accurate, or stuff might get culled incorrectly when rendering.

-------------------------

vivienneanthony | 2018-01-13 19:07:31 UTC | #11

Okay. I added it. From what I can tell Terrain.cpp in Urho3D creates the Boundary Box then tells the patch to set BoundaryBox_ to it. I think I did it correctly. I added more console information for debug and updated my original post.

-------------------------

JTippetts | 2018-01-13 20:08:58 UTC | #12

Try debug-rendering your terrain patch bounding boxes. If the boxes render, but the patches don't, then you can narrow down into your patch generation code. If the boxes don't render, or if they render weirdly, then you can revisit your bounding box generation.

-------------------------

vivienneanthony | 2018-01-13 22:25:19 UTC | #13

I added this piece of  code

[code]
	DebugRenderer * mRenderer = mScene->GetComponent<DebugRenderer>();

	//mRenderer->AddBoundingBox(m_BoundingBox, Color(1.0f,1.0f,1.0f,1.0f), true);

	mRenderer->AddTriangleMesh(m_pTopology->GetVertexData(),
			m_pTopology->GetVertexCounts() * 3, m_pTopology->GetIndexData(),
			m_pTopology->GetIndexCounts(), 0, m_pTopology->GetIndexCounts(),
			Matrix3x4::IDENTITY, Color(1.0f, 1.0f, 1.0f, 1.0f), true);

[/code]

The bounding box and the triangle geometry appears briefly at least the wire frame. Once I figure how to get the debug to stay I'll post a picture.

[code]

mRenderer->AddBoundingBox(m_BoundingBox, Color(1.0f,1.0f,1.0f,1.0f), true);

	mRenderer->AddTriangleMesh(m_pTopology->GetVertexData(),
				sizeof(float)*3, m_pTopology->GetIndexData(),
				sizeof(unsigned int), 0, m_pTopology->GetIndexCounts(),
				Matrix3x4::IDENTITY, Color(1.0f, 1.0f, 1.0f, 1.0f), true);

[/code]

-------------------------

vivienneanthony | 2018-01-14 15:00:22 UTC | #14

I have to revisit the bounding box generation because what I'm getting is weird. When  I run debug->render the box appear but not in the same spot or if i add triangle mesh. You can see the triangles lines show but it's not at a specific spot.

I'll probably compress the subfolders of the code and if anyone wants to take a look. They can because the problem might be simple. I'm just missing it because I have been staring at the same code for a while.

-------------------------

vivienneanthony | 2018-01-14 15:11:27 UTC | #15

Code if someone wants to take a look.

https://drive.google.com/open?id=1nZHRLI03GJN66nmbs-n_ud7SjbSHgqEH
https://drive.google.com/open?id=1oYxRB_0GWxrORF_jeJd5GNpo7WlN9j_7

-------------------------

JTippetts | 2018-01-14 15:53:22 UTC | #16

If the box is that weird, and if you're simply generating it by merging points, then there is probably something wrong with the way you're generating the points.

-------------------------

vivienneanthony | 2018-01-14 17:29:12 UTC | #17

I just found it weird because the way the points are generated is the same of the dynamic geometry sample code. Ill look t it again later.

-------------------------

vivienneanthony | 2018-01-16 03:47:11 UTC | #18

I have some better luck doing it similiar to how Urho3D does the patches except each patch creates the drawable child without calling the creategeometry in the root node. Each node creates a child node with the patch component. 

As you can see the geometry is screwy, I'm not sure why the I got the "inf inf" error shown in the console output.

If I can get to show a box, I can run a cube-to-sphere algorithm and apply some perlin.

-------------------------

vivienneanthony | 2018-01-16 08:52:06 UTC | #19

Error I was mentioning.

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/3/30376aeeb0d600b8ee1dc7a5ea2629413dce460f.png'>

```
[Mon Jan 15 22:39:06 2018] INFO: [ALPHAENGINE] Set index data ...
[Mon Jan 15 22:39:06 2018] INFO: [ALPHAENGINE] Vertex Data (Triangles<3) ...
[Mon Jan 15 22:39:06 2018] INFO: [ALPHAENGINE] VectorData -5 5 -5
[Mon Jan 15 22:39:06 2018] INFO: [ALPHAENGINE] VectorData -4.375 5 -5
[Mon Jan 15 22:39:06 2018] INFO: [ALPHAENGINE] VectorData -4.375 4.375 -5
[Mon Jan 15 22:39:06 2018] INFO: [ALPHAENGINE] VectorData -5 5 -5
[Mon Jan 15 22:39:06 2018] INFO: [ALPHAENGINE] VectorData -4.375 4.375 -5
[Mon Jan 15 22:39:06 2018] INFO: [ALPHAENGINE] VectorData -5 4.375 -5
[Mon Jan 15 22:39:06 2018] INFO: [ALPHAENGINE] IndexData 0 1 2 3 4 5 6
[Mon Jan 15 22:39:06 2018] INFO: [ALPHAENGINE] Generate bounding box ...
[Mon Jan 15 22:39:06 2018] INFO: [ALPHAENGINE] Adding boundary -5 5 -5
[Mon Jan 15 22:39:06 2018] INFO: [ALPHAENGINE] Adding boundary -4.375 5 -5
[Mon Jan 15 22:39:06 2018] INFO: [ALPHAENGINE] Adding boundary -4.375 4.375 -5
[Mon Jan 15 22:39:06 2018] INFO: [ALPHAENGINE] Bounding Box -5 -5 -5 - 5 5 -5
[Mon Jan 15 22:39:06 2018] INFO: [ALPHAENGINE] world inf inf inf - -inf -inf -inf
[Mon Jan 15 22:39:06 2018] INFO: [ALPHAENGINE] world inf inf inf - -inf -inf -inf
[Mon Jan 15 22:39:06 2018] INFO: [ALPHAENGINE] world inf inf inf - -inf -inf -inf
[Mon Jan 15 22:39:06 2018] INFO: [ALPHAENGINE] world inf inf inf - -inf -inf -inf
[Mon Jan 15 22:39:06 2018] INFO: [ALPHAENGINE] world inf inf inf - -inf -inf -inf
[Mon Jan 15 22:39:06 2018] INFO: [ALPHAENGINE] world inf inf inf - -inf -inf -inf
[Mon Jan 15 22:39:54 2018] WARNING: [ALPHAENGINE] GameAsset XML ROOT element was created inside factory !
[Mon Jan 15 22:39:55 2018] WARNING: [ALPHAENGINE] GameAsset XML ROOT element was created inside factory !
[Mon Jan 15 22:39:57 2018] WARNING: [ALPHAENGINE] GameAsset XML ROOT element was created inside factory !
[Mon Jan 15 22:39:58 2018] WARNING: [ALPHAENGINE] GameAsset XML ROOT element was created inside factory !
[Mon Jan 15 22:40:07 2018] WARNING: [ALPHAENGINE] GameAsset XML ROOT element was created inside factory !
[Mon Jan 15 22:40:08 2018] WARNING: [ALPHAENGINE] GameAsset XML ROOT element was created inside factory !
[Mon Jan 15 22:40:32 2018] WARNING: [ALPHAENGINE] GameAsset XML ROOT element was created inside factory !
[Mon Jan 15 22:40:35 2018] WARNING: [ALPHAENGINE] GameAsset XML ROOT element was created inside factory !
[Mon Jan 15 22:40:39 2018] WARNING: [ALPHAENGINE] GameAsset XML ROOT element was created inside factory !
```

-------------------------

vivienneanthony | 2018-01-17 04:56:08 UTC | #20

After many some sweat and tears. Jokingly. I have to do some more work now to get it more functioning and then make it static and realtime. At least static I can get working.

https://imgur.com/a/I4Aug

-------------------------

vivienneanthony | 2018-01-19 03:38:51 UTC | #21

I was thinking of a node derived class so I can hold depth information and other information related. I made a basic one which partially worked.

For example, SphereTerrainNode derived class of Node. From the code, I did. I can add a new node as a child with the node parameter but doing runtime it doesn't work fully meaning it's inaccessible partially on Urho3D side. 

Hmmm.

A better example. 

Example 1
SphereTerrainNode derived from Node. It's created and assigned a id, name etc but if I try to call a function like GetDepth() either I get a segfault error or SphereTerrainNode is considered null or pass it. It doesn't.

Example 2
[code]
SharedPtr<SphereTerrainNode> newTerrainNode = new SphereTerrainNode(context_, this);

pNode(either Node * or SphereTerrainNode)->AddChild(newTerrainNode);
[/code]

[code]
SphereTerrainPatch::SphereTerrainPatch(Context * context, SphereTerrainNode * parent)
:Node(context), m_Parent(parent)
{
  // m_Parent is a SphereTerrainNode * m_Parent;
 m_Depth = 3
}
[/code]

Now if I try to do access it.
m_Parent = null

m_Depth  = 0 nothing

If I try to print something with URHO3D_LOGINFO, nothing outputs to the console




m_Parent

-------------------------

Modanung | 2018-01-19 04:15:57 UTC | #22

About subclassing `Node`:
https://discourse.urho3d.io/t/node-getscene-return-null/96/5?u=modanung

Best inherit from `Component` instead.

-------------------------

vivienneanthony | 2018-01-19 05:01:14 UTC | #23

I think I was able to create derived classes from others. It was a little tricky and some patching Urho3D to do so. :-/

In this case I would like a straight forward, method.
Like a SphereTerrain(Node),SphereTerrainNode(), then if a node has a Patch a additional Component without doing a bunch of GetNode() -> GetComponent code.

-------------------------

vivienneanthony | 2018-01-19 11:18:51 UTC | #24

A better example is the code

The node is a component in this case. 

The line "Creating Sphere" and "Building face appears". The line "Testing a number " fails which the console should read "Testing a number 500". In the component, I specifically set a variable to 500.

[code]
SphereTerrain::SphereTerrain(Context * context) :
		Component(context), m_Material(nullptr), m_MaterialShaderEnable(
				false), m_VisualRadius(10.0f) {

}

void SphereTerrain::Start() {

	// Start if node was assigned to this
	Build(m_VisualRadius);
}

// Build
void SphereTerrain::Build(double radius = 10.0f) {

	// Create a node - m_DummyNode is a SphereTerrain Node *
	Node * test = node_->CreateChild("Some Random node");

	SphereTerrainNode * testing = new SphereTerrainNode(context_, nullptr,
			nullptr);

	test->AddComponent(testing, testing->GetID(), REPLICATED);

	node_->AddChild(test);

	unsigned int a = testing->GetA();

	ALPHAENGINE_LOGINFO("Testing a number"+String((int)a));

	// Set initial radius
	if (radius < 10.0f) {
		radius = 10.0f;
	}

	// Set Visual Radius
	m_VisualRadius = radius;

	// Create sides
	for (unsigned int i = 0; i < 6; i++) {
		// Debug
		ALPHAENGINE_LOGINFO("Creating SphereTerrain Face " + String(i));

		// Create Face
		m_SphereTerrainFace[i] = new SphereTerrainFace(g_pApp->GetContext(),
				this, (STFaceDirection) i, node_);

		// Set owner for each face
		m_SphereTerrainFace[i]->SetSphereTerrain(this);
	}

	// Build sides
	for (unsigned int i = 0; i < 6; i++) {
		// Debug
		ALPHAENGINE_LOGINFO("Build SphereTerrain Face " + String(i));

		// Build face
		m_SphereTerrainFace[i]->Build();
	}
}
[/code]

-------------------------

vivienneanthony | 2018-01-19 08:16:05 UTC | #25

Ignore. Got the tree part working.  Thanks for listening.

I have to figure out size(length) based on depth level

-------------------------

vivienneanthony | 2018-01-27 19:09:54 UTC | #26

Hey,

I got the tree working. 

https://imgur.com/g41wCZe

Right now, I'm trying to figure out how to properly update depth. The way the tree works is there is the main object, a node for the face, then nodes with children or patch. The bounding box adds all the triangles of a patch in a polyhedron then the bounding box is set.

I currently set the maximum depth, but I want to properly calculate the max depth. Before I get the real time worked on. I want to set it up, so a max depth is pre-calculated building the geometry, it's created based 0 depth. Then recalculated on the first UpdateBatch using the camera distance. Which updates the parent main node. The first build sense it would be depth 0 would be really fast. 

The issue is how do I properly use the batches[x].loddistance_  to determine the depth level if the terrain is spherical. I would think on the urho3d post update the main terrain node / logic component would have to calculate depth using the information from the patches to rebuild the geometry if need be.

[code]
void TerrainPatch::UpdateBatches(const FrameInfo& frame)
{
    const Matrix3x4& worldTransform = node_->GetWorldTransform();
    distance_ = frame.camera_->GetDistance(GetWorldBoundingBox().Center());

    float scale = worldTransform.Scale().DotProduct(DOT_SCALE);
    lodDistance_ = frame.camera_->GetLodDistance(distance_, scale, lodBias_);

    batches_[0].distance_ = distance_;
    batches_[0].worldTransform_ = &worldTransform;

    unsigned newLodLevel = 0;
    for (unsigned i = 0; i < lodErrors_.Size(); ++i)
    {
        if (lodErrors_[i] / lodDistance_ > LOD_CONSTANT)
            break;
        else
            newLodLevel = i;
    }

    lodLevel_ = GetCorrectedLodLevel(newLodLevel);
}
[/code]

-------------------------

vivienneanthony | 2018-01-29 06:40:56 UTC | #27

Have anyone written a simple shader? Super basic that can take light a object then changes a color using the mixfunction? Basically I have to create a shader that lerp between some values, and apply a texture based on the height radius from some point to vertex point. 

[code]
#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"
#include "ScreenPos.glsl"
#include "Lighting.glsl"


// Passed values
varying vec3 vNormal;
varying vec4 vWorldPos;


// vertex shasder
void VS()
{
   // Get matrix
   mat4 modelMatrix = iModelMatrix;

   // Get world position
   vec3 worldPos = GetWorldPos(modelMatrix);

   // Get position (Clipped)
   gl_Position = GetClipPos(worldPos);  

   // Get vector world position depth
   vWorldPos = vec4(worldPos, GetDepth(gl_Position));
   
   // Get Noraml
   vNormal = GetWorldNormal(modelMatrix);  
}


// pixel shader
void PS()
{
  //  variables
  vec3 lightColor;
  vec3 lightDir;
  vec3 finalColor;

  // Normalize the vNormal
  vec3 normal = normalize(vNormal);  

  // set color
  vec4 diffColor = vec4(1.0, 0.0, 0.0, 1.0);


  // NOTE:
  // I think to use to mix the color I would use the normal. Distance vector4.0 to world position should be good 
  // but when using it. There was no gradient.

  // diffColor = mix(vec4(0.0,1.0f,0.0f,1.0f), vec4(1.0f,1.0f,1.0f,1.0f), distance(vec4(0.0f,0.0f,0.0f,0.0f), vWorldPos));

  // get diff using world position and light direction amount
  float diff = GetDiffuse(normal, vWorldPos.xyz, lightDir);

  // light color based on current light color
  lightColor = cLightColor.rgb;

  // final color equal diff amount times light color * diffcolor
  finalColor = (diff * lightColor) * diffColor.rgb;

  // fog color equals final color and fog factor of 0
  gl_FragColor = vec4(finalColor, diffColor.a);	

}
[/code]

![shade|573x500](upload://yBfcw5R0XNkj8rFhqaOIo7kQvW0.png)

-------------------------

Sinoid | 2018-01-29 13:35:04 UTC | #28

You need to normalize your distance into something usable (`(vertDist - minDist) / (maxDist - minDist)`), your distance was probably way outside of a usable 0-1 range.

I'd look up the color from a ramp texture, can be authored in Photoshop/Gimp using the gradient map modifier. Though there are simple gradient techniques ([quilez' cos tables](http://www.iquilezles.org/www/articles/palettes/palettes.htm)) they're probably not going to have the range or control you want for serious use. You can also pack gradient LUTs into one texture for specifying which LUT to use in a uniform.

-------------------------

vivienneanthony | 2018-01-29 15:31:39 UTC | #29

Yes. I figured that also. I'm thinking that a heightmap texture would help and that is passed to the shader. I've used that method before in older code.

The only hiccup I have now is somehow calculating the normals better without using a texture.

https://imgur.com/a/gof2h

and also since I'm using the triangle list it's a memory hog although for subdividing terrain the way I need. I think triangle list of creation is best.

-------------------------

Modanung | 2018-01-29 15:57:39 UTC | #30

I would love to see this somehow combined with @JTippetts' [terrain editor](https://github.com/JTippetts/U3DTerrainEditor), btw. :slight_smile:
A future UrhoEdit could include this planet builder.

-------------------------

vivienneanthony | 2018-02-01 22:40:59 UTC | #31

That would be cool including the spherical gravity.

-------------------------

vivienneanthony | 2018-02-01 22:41:47 UTC | #32

I'm trying to create a texture but it's failing. Ideally, I would like to make a single channel texture if possible.

[code]
	// Create memory
	m_pHeightMapTextureData = new float[TEXELSIZEPLUS *TEXELSIZEPLUS*4];

	// Create off texture turn off compression
	m_pHeightMapTexture->SetNumLevels(1);
	m_pHeightMapTexture->SetSize(TEXELSIZEPLUS, TEXELSIZEPLUS, CF_RGBA, TEXTURE_STATIC);
	m_pHeightMapTexture->SetData(0, 0, 0, TEXELSIZEPLUS, TEXELSIZEPLUS,
				m_pHeightMapTextureData);
	m_pHeightMapTexture->SetFilterMode(FILTER_NEAREST);
[/code]

-------------------------

vivienneanthony | 2018-02-02 01:41:46 UTC | #33

I tried the two following codes. I get a segfault.

I changed the code to
[code]
// Create memory
	m_pHeightMapTextureData = new float[TEXELSIZEPLUS *TEXELSIZEPLUS];

	// Create off texture turn off compression
	m_pHeightMapTexture->SetNumLevels(1);
	m_pHeightMapTexture->SetSize(TEXELSIZEPLUS, TEXELSIZEPLUS, GL_RGBA32F, TEXTURE_STATIC);
	m_pHeightMapTexture->SetData(0, 0, 0, TEXELSIZEPLUS, TEXELSIZEPLUS,
				m_pHeightMapTextureData);
	m_pHeightMapTexture->SetFilterMode(FILTER_NEAREST);
[/code]

Attempt 2

[code]
// Create memory
	//m_pHeightMapTextureData = new float();

	// Create off texture turn off compression
	m_pHeightMapTexture->SetNumLevels(1);
	m_pHeightMapTexture->SetSize(TEXELSIZEPLUS, TEXELSIZEPLUS, GL_RGBA32F, TEXTURE_DYNAMIC);
	m_pHeightMapTexture->SetFilterMode(FILTER_NEAREST);

 	m_pHeightMapTexture->GetData(0, m_pHeightMapTextureData);
[/code]

-------------------------

Sinoid | 2018-02-01 23:41:41 UTC | #34

[quote="vivienneanthony, post:32, topic:3929"]
// Create memory
	m_pHeightMapTextureData = new float[TEXELSIZEPLUS * TEXELSIZEPLUS * 4];
[/quote]

Looks like you dropped that 4. You said you want single-channel but you're specifying `GL_RGBA32F` which expects 4 floats per pixel - not 1, you probably want GL_R32F.

---

You should be using the helper functions in `Graphics` for `Graphics::GetFloat32Format()`, `Graphics::GetRGBAFormat()`, etc. If you use those you can be reasonably sure that the code handles them and they're less eye-glaze inducing than the DXGI / GL_ formats.

If you specify arbitrary formats you're counting on `Texture::GetRowDataSize(int)` actually having a case for the format you pass. If it's not there then setting texture data will silently fail as you're *trying* to apply 0-length data.

-------------------------

vivienneanthony | 2018-02-02 04:39:28 UTC | #35

Yea. I was comparing the OpenGL syntax to describe the float 32bit. I wasn't too sure of the Urho3D equivalent. "[TexelSize]x[Texelsize]x4" was a bit excessive. Ideally, I would rather just keep the pointer on Urho3D side and unload all the data onto the GPU.

The next thing I have to tackle is getting some good normals so the triangles aren't showing obviously that want be excessive till I can get the GPU to generate the normals.

-------------------------

vivienneanthony | 2018-02-11 07:13:18 UTC | #36

I'll probably figure this out but does anyone on the shader side get a position on a texture from a vector3? My next step on the shader is passing the generated heightmap per patch and do a gradient.  After adding some uv, for triplanar texturing.

While I do more optimizing and clean up.

https://imgur.com/a/eqce2

-------------------------

vivienneanthony | 2018-02-11 08:07:16 UTC | #37

The other question I have is about the shader.

If a texture is passed to a shader. If I use the shader for another patch. Wouldn't both share the same texture? Or is there a way to assign the different texture.
I think something like this would be enougth,

[code]

void SphereTerrainPatch::SetMaterial(Material * material) {

	// Clone material
	m_pMaterial = material->Clone();

	// Set Texture
	m_pMaterial->SetTexture(TU_CUSTOM1, m_pTopology->GetHeightMap());

	// set material
	for (unsigned i = 0; i < batches_.Size(); ++i)
		batches_[i].material_ = m_pMaterial;
}

[/code]

-------------------------

Modanung | 2018-11-20 09:51:24 UTC | #38

For a more even distribution of vertices one should use a [rhombic triacontahedron](https://en.wikipedia.org/wiki/Rhombic_triacontahedron) instead of a cube as the base solid. It would be formed by 30 patches instead of 6, each with 8 neighboring patches instead of 4.

-------------------------

