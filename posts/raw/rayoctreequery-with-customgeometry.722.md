thebluefish | 2017-01-02 01:02:24 UTC | #1

I generate custom geometry the following way:

[code]
_grid->BeginGeometry(1, Urho3D::TRIANGLE_STRIP);

	_grid->DefineVertex(Urho3D::Vector3(-actualGridSize.x_, 0, -actualGridSize.z_) + _gridOffset);
	_grid->DefineColor(COLOR_GRID_MAIN_LINE);
	_grid->DefineVertex(Urho3D::Vector3(-actualGridSize.x_, 0, actualGridSize.z_) + _gridOffset);
	_grid->DefineColor(COLOR_GRID_MAIN_LINE);
	_grid->DefineVertex(Urho3D::Vector3(actualGridSize.x_, 0, -actualGridSize.z_) + _gridOffset);
	_grid->DefineColor(COLOR_GRID_MAIN_LINE);
	_grid->DefineVertex(Urho3D::Vector3(actualGridSize.x_, 0, actualGridSize.z_) + _gridOffset);
	_grid->DefineColor(COLOR_GRID_MAIN_LINE);
	
	_grid->Commit();
[/code]

The geometry is visible. However I cannot get any results from it when performing a RayOctreeQuery:

[code]
	Urho3D::IntVector2 mousePos = input->GetMousePosition();
	Urho3D::PODVector<Urho3D::RayQueryResult> result;

	Urho3D::Ray ray = _camera->GetScreenRay(mousePos.x_, mousePos.y_);
	Urho3D::RayOctreeQuery q(result, ray, Urho3D::RAY_TRIANGLE, Urho3D::M_INFINITY, Urho3D::DRAWABLE_GEOMETRY, -1);
	_scene->GetComponent<Urho3D::Octree>()->Raycast(q);

	if (result.Size() > 0)
	{
		// do stuff
	}
[/code]

I have also tried using Urho3D::RAY_OBB and Urho3D::DRAWABLE_ANY as well, but still no results. Eventually the mesh that I want to detect will need to be invisible.

One idea I had was to instead use physics objects. Now I don't need physics simulation in my scene, would it instead be possible to disable the actual physics simulation so that I can simply run my own custom queries against the PhysicsWorld?

-------------------------

thebluefish | 2017-01-02 01:02:24 UTC | #2

I attempted to go the physics route, but cannot get it to work right. I am attempting to use indexed geometry to create a mode. I am following [url=https://github.com/urho3d/Urho3D/blob/master/Source/Samples/34_DynamicGeometry/DynamicGeometry.cpp]this example[/url]:

[code]
const unsigned numVertices = 4;

	float vertexData[] = {
		// Position             Normal
		-actualGridSize.x_, 0.f, -actualGridSize.z_, 0.0f, 0.0f, 0.0f,
		-actualGridSize.x_, 0.f, actualGridSize.z_, 0.0f, 0.0f, 0.0f,
		actualGridSize.x_, 0.f, -actualGridSize.z_, 0.0f, 0.0f, 0.0f,
		actualGridSize.x_, 0.f, actualGridSize.z_, 0.0f, 0.0f, 0.0f
	};

	const unsigned short indexData[] = {
		0, 1, 2,
		1, 2, 3,
	};

	Urho3D::SharedPtr<Urho3D::VertexBuffer> vb(new Urho3D::VertexBuffer(context_));
	Urho3D::SharedPtr<Urho3D::IndexBuffer> ib(new Urho3D::IndexBuffer(context_));
	Urho3D::SharedPtr<Urho3D::Geometry> geom(new Urho3D::Geometry(context_));
	Urho3D::SharedPtr<Urho3D::Model> fromScratchModel(new Urho3D::Model(context_));
	
	vb->SetSize(numVertices, Urho3D::MASK_POSITION | Urho3D::MASK_NORMAL);
	vb->SetData(vertexData);

	ib->SetSize(6, false);
	ib->SetData(indexData);

	geom->SetVertexBuffer(0, vb);
	geom->SetIndexBuffer(ib);
	geom->SetDrawRange(Urho3D::TRIANGLE_LIST, 0, numVertices);

	fromScratchModel->SetNumGeometries(1);
	fromScratchModel->SetGeometry(0, 0, geom);

	Urho3D::CollisionShape* shape = _gridNode->GetComponent<Urho3D::CollisionShape>();
	shape->SetTriangleMesh(fromScratchModel);
[/code]

However the call to SetTriangleMesh causes a crash in btQuantizedBvh.cpp (line 144)
[code]
btAssert(numIndices>0); // error here

// startIndex = 0
// endIndex = 0
[/code]

I also tried using the existing CustomGeometry as such:

[code]
shape->SetCustomTriangleMesh(_grid);
[/code]

Which doesn't produce a crash, but also doesn't produce any results.

-------------------------

codingmonkey | 2017-01-02 01:02:24 UTC | #3

i guess what you needed set Shadowing() geometry to true or/and add collision component and set your model as collision shape for it

ib->SetShadowed(true) ?

-------------------------

thebluefish | 2017-01-02 01:02:24 UTC | #4

If I set shadowing to true, then I get a crash in a different area. If I manually set it to false, it crashes in the same area. If you look at my existing code, I am already creating the collision component and setting the model as collision shape.

-------------------------

codingmonkey | 2017-01-02 01:02:24 UTC | #5

> I am already creating the collision component and setting the model as collision shape
i see
mb now needed to set collison mask for object ? 
that value it have by default then you try build your custom geometry, you know ? i'm don't know

try to: Node->CreateComponent<Rigidbody>() and set some collision mask / layers

also in example 34:
StaticModel* object = node->CreateComponent<StaticModel>();
object->SetModel(fromScratchModel);

Where your static model in code ?

and i'm don't see bb setup in your code : something like: fromScratchModel->SetBoundingBox();

-------------------------

thebluefish | 2017-01-02 01:02:24 UTC | #6

Still have no idea why it's not working with the physics stuff, however I was able to get it working with just the CustomGeometry. My issue stems from the following "features" that I've discovered:

- Rays query without scaling applied, but report the position with scaling applied. Therefore when I was using my model which was scaled 10x, even though I was setting the position of another model to the position given by the ray query, it would position it further out the further I was from origin.

- Screen coordinates need to be normalized first. This was one of the first things that I corrected before my second post.

- There's something weird when using TRIANGLE_STRIP, the first triangle was drawn just fine but the second was not (and it didn't show up in debug geometry either).

- Using a LINE_LIST (which is how I generate my grid) actually generates full geometry that I can cast rays against. There seems to be a problem with the corners in my case, but most of the geometry worked otherwise.

I went ahead and used OBB due to the simple geometry used in my game example. It works for what I need it to.

-------------------------

