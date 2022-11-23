ghidra | 2017-01-02 00:59:43 UTC | #1

First, as sort of an introduction of myself to the forums, I have a basic question...
Is it possible to create geometry on the fly? Even something simple like a grid with x horizontal division and y vertical division?
Thanks.

-------------------------

friesencr | 2017-01-02 00:59:43 UTC | #2

I did that very thing today.  I had written a procedual dungeon creator combining various tile pieces as seperate tiles of geometry.  But having thousands of small items, while well batched, did stress the cpu performance.  It was also hard to cheat the physics.   So I am trying a new approach using procedural geometry and the idea is to sample textures as much as posible.  Anywho enough blabbing, here is the code:

[code]
	void GenerateGeometry(PODVector<TileInstance> data)
	{
		_geometry = new CustomGeometry(context_);  // SharedPtr<CustomGeometry> held by class
		_geometry->BeginGeometry(0, TRIANGLE_LIST);
		for(unsigned int i=0; i < data.Size(); i++)
		{
			TileInstance tile = data[i];
			// tri 1
			_geometry->DefineVertex(Vector3(tile.x, 0, tile.y));
			_geometry->DefineTexCoord(Vector2(0.0, 0.0));

			_geometry->DefineVertex(Vector3(tile.x, 0, tile.y+1));
			_geometry->DefineTexCoord(Vector2(0.0, 1.0));

			_geometry->DefineVertex(Vector3(tile.x+1, 0, tile.y));
			_geometry->DefineTexCoord(Vector2(1.0, 0.0));

			// tri 2
			_geometry->DefineVertex(Vector3(tile.x, 0, tile.y+1));
			_geometry->DefineTexCoord(Vector2(0.0, 1.0));

			_geometry->DefineVertex(Vector3(tile.x+1, 0, tile.y+1));
			_geometry->DefineTexCoord(Vector2(1.0, 1.0));

			_geometry->DefineVertex(Vector3(tile.x+1, 0, tile.y));
			_geometry->DefineTexCoord(Vector2(1.0, 0.0));
		}
		_geometry->Commit();
	}

[/code]

Hopefully my C++ isn't bad.  I am still very green to c/c++ and I am trying to code only in c++ for game stuff to man me up.

-------------------------

ghidra | 2017-01-02 00:59:43 UTC | #3

magnificent.
I guess I'm not hard enough, cause I'm gonna have to plug this into angelscript.
Thanks for pointing me in a direction. I thank you.

-------------------------

friesencr | 2017-01-02 00:59:43 UTC | #4

Be sure to define tri vertexes in clockwise manner.  The winding determains the direction the tri is facing.  Clockwise gives you an outward facing tri.  Also define the vertex first.  All proceeding commands affect the vertex just defined.

-------------------------

godan | 2017-01-02 01:00:31 UTC | #5

How do you then add the custom geometry to a scene node and render it? So far I've got:

[code]
//create scene node
Node* node = scene_->CreateChild("Object");
node->SetPosition(Vector3(0.0f, 0.0f, 0.0f));
StaticModel* object = node->CreateComponent<StaticModel>();

CustomGeometry*  _geometry = new CustomGeometry(context_); 
_geometry->BeginGeometry(0, TRIANGLE_LIST);

// tri 1
_geometry->DefineVertex(Vector3(-1, 0, 0));
_geometry->DefineTexCoord(Vector2(0.0, 0.0));

_geometry->DefineVertex(Vector3(1, 0, 0));
_geometry->DefineTexCoord(Vector2(0.0, 1.0));

_geometry->DefineVertex(Vector3(1, 0, 1));
_geometry->DefineTexCoord(Vector2(1.0, 0.0));

// tri 2
_geometry->DefineVertex(Vector3(-1, 0, 0));
_geometry->DefineTexCoord(Vector2(0.0, 1.0));

_geometry->DefineVertex(Vector3(1, 0, 1));
_geometry->DefineTexCoord(Vector2(1.0, 1.0));

_geometry->DefineVertex(Vector3(-1, 0, 1));
_geometry->DefineTexCoord(Vector2(1.0, 0.0));

_geometry->Commit();
_geometry->GetLodGeometry(0,0);

Model* model = new Model(context_);
model->SetGeometry(0, 0, _geometry->GetLodGeometry(0,0));

object->SetModel(model);
[/code]

-------------------------

gwald | 2017-01-02 01:00:36 UTC | #6

[quote="godan"]How do you then add the custom geometry to a scene node and render it? So far I've got:
[/quote]

I'm still new, not 100% sure but looking at your geometry data, looks like your creating texture coords without setting a texture(material)?
[code]_geometry->DefineTexCoord(Vector2(1.0, 0.0));[/code]

Also putting the node in the middle of the scene could be hard to see if your camera is at 0,0,0 too
[code]node->SetPosition(Vector3(0.0f, 0.0f, 0.0f));[/code]

-------------------------

cadaver | 2017-01-02 01:00:37 UTC | #7

There are two ways to go about runtime geometry creation. They are not intended to be mixed.

1) Easy way to display one unique object with unindexed geometry. Can be used from scripting. Create a CustomGeometry component to a scene node; you don't need other components. (In this case, do not try to use the CustomGeometry's geometry to build a Model resource. It may work, but is unsupported)

2) The hard way, but allows more freedom. Unindexed or indexed geometry. C++ only. Create a Model, fill vertex + index buffers. Use eg. StaticModel component to show it. There's a from-scratch example now in [github.com/urho3d/Urho3D/blob/m ... ometry.cpp](https://github.com/urho3d/Urho3D/blob/master/Source/Samples/34_DynamicGeometry/DynamicGeometry.cpp). Note that you need an updated master branch for the example to work as is; previously you needed to call model->SetNumGeometryLodLevels() for each geometry, now 1 LOD level is assumed and you no longer require the call in that case.

-------------------------

