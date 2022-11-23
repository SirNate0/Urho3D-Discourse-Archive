Tahri | 2017-07-09 18:25:03 UTC | #1

Hello Urho3D Community! First post here been but I've been lurking for a while. Also wanted to say thanks to the Urho3D Team for fantastic work! 

I'm working on an application that uses voxels for a research project. Naturally I drifted towards polyvox as a good library to start from. I've gotten all the basic framework together from the latest tutorial here: [PV Tutorial](https://bitbucket.org/volumesoffun/polyvox/src/c986c9f0b1189737a182fbc8d4f4696436f972c1/documentation/tutorial1.rst?at=develop&fileviewer=file-view-default)

Since the tutorial caters to OpenGL I'm trying to fill in the blanks as best I can. I'm not native to 3D programming or voxels so I'm really just trying to get something to work in the simplest form. 

What I have to get my mesh data into urho3D is below but i can't imagine the process is so straight forward.

Currently I'm getting an pointer error with my vertex buffer. 

 Thanks, any help is much appreciated! :)

[details=world.h]

>
class WorldGen 
{
public:
	SharedPtr<IndexBuffer> ib_;
	SharedPtr<VertexBuffer> vb_;
	SharedPtr<Geometry> geom_;
 	SharedPtr<Model> testModel;
	WorldGen(void);
	~WorldGen(void);
	bool worldLoaded;
	// Convert a PolyVox mesh to OpenGL index/vertex buffers. Inlined because it's templatised.
	void createSphereInVolume(PolyVox::RawVolume<uint8_t>& volData, float fRadius);
	void render(Urho3D::Context* c, Urho3D::Scene* s);
	template typename MeshType
	void addMesh(const MeshType& surfaceMesh,Urho3D::Context Context_, const PolyVox::Vector3DInt32& translation = PolyVox::Vector3DInt32(0, 0, 0), float scale = 1.0f)
	{
		//Handle Buffers 
		vb_ = (new VertexBuffer(context_));
		vb_->SetShadowed(true);
		vb_->SetSize(surfaceMesh.getNoOfIndices(), MASK_POSITION);
		vb_->SetData(surfaceMesh.getRawVertexData());
		//context_->vb_ = vb;
		ib_ = (new IndexBuffer(context_));
		ib_->SetShadowed(true);
		ib_->SetSize(surfaceMesh.getNoOfVertices(), false);
		ib_->SetData(surfaceMesh.getRawIndexData());
		//context_->ib_ = ib
		worldLoaded = true;
	}
};
[/details]

[details=world.cpp]

> 
WorldGen::WorldGen(void) : 	worldLoaded(false)
{
}
WorldGen::~WorldGen(void)
{
}
void WorldGen::createSphereInVolume(PolyVox::RawVolume<uint8_t>& volData, float fRadius)
{
	//This vector hold the position of the center of the volume
	PolyVox::Vector3DFloat v3dVolCenter(volData.getWidth() / 2, volData.getHeight() / 2, volData.getDepth() / 2);
	//This three-level for loop iterates over every voxel in the volume
	for (int z = 0; z < volData.getDepth(); z++)
	{
		for (int y = 0; y < volData.getHeight(); y++)
		{
			for (int x = 0; x < volData.getWidth(); x++)
			{
				//Store our current position as a vector...
				PolyVox::Vector3DFloat v3dCurrentPos(x, y, z);
				//And compute how far the current position is from the center of the volume
				float fDistToCenter = (v3dCurrentPos - v3dVolCenter).length();
				uint8_t uVoxelValue = 0;
				//If the current voxel is less than 'radius' units from the center then we make it solid.
				if (fDistToCenter <= fRadius)
				{
					//Our new voxel value
					uVoxelValue = 255;
				}
				//Wrte the voxel value into the volume	
				volData.setVoxel(x, y, z, uVoxelValue);
			}
		}
	}
}
//
void WorldGen::render(Urho3D::Context* context_, Urho3D::Scene* scene_)
{
	geom_->SetVertexBuffer(0, vb_);
	geom_->SetIndexBuffer(ib_);
	geom_->SetDrawRange(TRIANGLE_LIST, 0, ib_->GetIndexCount());
	testModel->SetNumGeometries(1);
	testModel->SetNumGeometryLodLevels(0, 1);
	testModel->SetGeometry(0, 0, geom_);
	// Define the model buffers and bounding box
	PODVector<unsigned> emptyMorphRange;
	//testModel->SetVertexBuffers(dlvbVector, emptyMorphRange, emptyMorphRange);
	//testModel->SetIndexBuffers(dlibVector);
	testModel->SetBoundingBox(BoundingBox(Vector3(-1.0f, -1.0f, 0.0f), Vector3(1.0f, 1.0f, 0.0f)));
	Node* testnodea = scene_->CreateChild("testsModel");
	testnodea->SetScale(Vector3(1.0f, 1.0f, 1.0f));
	StaticModel* testObjecta = testnodea->CreateComponent<StaticModel>();
	testObjecta->SetModel(testModel);
	//testObjecta->SetMaterial(cache->GetResource<Material>("Materials/Stone.xml"));
	testnodea->SetPosition(Vector3(-1.0f, 5.0f, 2.0f));
	
}
[/details]
[details=main.cpp]
> 
void CharacterDemo::TestArea()
{
	ResourceCache* cache = GetSubsystem<ResourceCache>();
	PolyVox::RawVolume<uint8_t> volData(PolyVox::Region(PolyVox::Vector3DInt32(0, 0, 0), PolyVox::Vector3DInt32(63, 63, 63)));
	world_->createSphereInVolume(volData, 30);
	auto mesh = PolyVox::extractCubicMesh(&volData, volData.getEnclosingRegion());
	//auto mesh = extractMarchingCubesMesh(&volData, volData.getEnclosingRegion());
	auto decodedMesh = PolyVox::decodeMesh(mesh);
	world_->addMesh(decodedMesh, context_);
	//Let us know that the world mesh has been decoded
	//world_->worldLoaded = true; 	
}
[/details]

-------------------------

bloop | 2018-11-28 16:22:54 UTC | #2

Hello!

I am no specialist and I might well be completely wrong, but it seems that you are using the wrong size for setting up the vertex and index buffer
it should be
vb_->SetSize(surfaceMesh.getNoOfVertices(), MASK_POSITION);
and
ib_->SetSize(surfaceMesh.getNoOfIndices(), false);
let me know if that works, I am also looking at polyvox and Urho

-------------------------

