Denthor | 2017-01-02 01:09:32 UTC | #1

Hi there, in the following function I load a mdl file, and then create a CustomGeometry over it.

When I run this, the model has correct lighting, but the CustomGeometry is black. There is no difference adding or removing DefineNormal.

Camera and lighting as per sample 5 AnimatingScene.

Any ideas on what I'm doing wrong?

[code]
void CreateCylinder()
{
// Create something we know to work for information
	Urho3D::ResourceCache* cache = application->GetSubsystem<Urho3D::ResourceCache>();
	Node* boxNode = m_pNode->CreateChild("Box");
	StaticModel* boxObject = boxNode->CreateComponent<StaticModel>();
	boxObject->SetModel(cache->GetResource<Model>("Models/Box.mdl"));
	boxObject->SetMaterial(cache->GetResource<Material>("Materials/Stone.xml"));

// Precalc verts for normals later
	float existingShapeSize = 3;
	Vector3 verts[512];
	float a = 0.0f;
	int nPos = 0;


	for (int i = 0; i < 256; i++)
	{
		float step = 6.283185307179586476925286766559f / (float)255;
		float nY = (float)sin(a) * existingShapeSize;
		float nZ = (float)cos(a) * existingShapeSize;

		float nTextY = (float)i / 256.0f;//((nZ + 2) / 4);

		verts[i*2] = Vector3(-1, nY, nZ);
		verts[i * 2 + 1] = Vector3(1, nY, nZ);

		a += step;
	}

// Set up custom geometry
	geometry = m_pNode->CreateComponent<Urho3D::CustomGeometry>();
	geometry->BeginGeometry(0, TRIANGLE_STRIP);

	a = 0.0f;
	nPos = 0;

	for (int i = 0; i < 256; i++)
	{
		float step = 6.283185307179586476925286766559f / (float)255;
		float nY = (float)sin(a) * existingShapeSize;
		float nZ = (float)cos(a) * existingShapeSize;

		float nTextY = (float)i / 256.0f;//((nZ + 2) / 4);

		geometry->DefineVertex(Vector3(-1, nY, nZ));
		geometry->DefineTexCoord(Vector2(1.0, 1.0f - nTextY));

		if (i * 2 + 3 < 512)
		{
			Vector3 v1 = verts[i * 2];
			Vector3 v2 = verts[i * 2 + 1];
			Vector3 v3 = verts[i * 2 + 2];
			Vector3 n1 = verts[i * 2 + 3];
			Vector3 n2 = verts[i * 2 + 3];
			Vector3 n3 = verts[i * 2 + 3];

			Vector3 edge1 = v1 - v2;
			Vector3 edge2 = v1 - v3;
			n1 = n2 = n3 = edge1.CrossProduct(edge2).Normalized();
			geometry->DefineNormal(n1);
		}



		geometry->DefineVertex(Vector3(1, nY, nZ));
		geometry->DefineTexCoord(Vector2(0.0, 1.0f - nTextY));
		if (i * 2 + 3 < 512)
		{
			Vector3 v1 = verts[i * 2];
			Vector3 v2 = verts[i * 2 + 1];
			Vector3 v3 = verts[i * 2 + 2];
			Vector3 n1 = verts[i * 2 + 3];
			Vector3 n2 = verts[i * 2 + 3];
			Vector3 n3 = verts[i * 2 + 3];

			Vector3 edge1 = v1 - v2;
			Vector3 edge2 = v1 - v3;
			n1 = n2 = n3 = edge1.CrossProduct(edge2).Normalized();
			geometry->DefineNormal(n1);
		}

		a += step;
	}
	geometry->Commit();
	geometry->SetMaterial(cache->GetResource<Urho3D::Material>("Materials/Stone.xml"));
}
[/code]

-------------------------

Enhex | 2017-01-02 01:09:32 UTC | #2

I think you need DefineTangent() too.

-------------------------

Denthor | 2017-01-02 01:09:33 UTC | #3

That worked, thank you.

-------------------------

