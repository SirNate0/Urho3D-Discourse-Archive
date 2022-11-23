entretoize | 2019-05-03 16:15:41 UTC | #1

Hello, I need to be able to add custom mesh (programmatically created) of 1 and more polygons.
I only found example to draw lines with a debug renderer but this is not what I need.
Is there a sample demonstrating how to build and render a single polygon just one frame ?

Thanks

-------------------------

johnnycable | 2019-05-03 13:19:08 UTC | #2

https://discourse.urho3d.io/t/draw-a-line-with-custom-geometry-in-2d/3192

-------------------------

entretoize | 2019-05-03 13:57:49 UTC | #3

OK, nice, but first in your topic you say the lines are white but them are yellow, and for me them are black...

-------------------------

Modanung | 2019-05-03 16:20:38 UTC | #4

The material assigned to a geometry determines its color and fill mode (solid or wire).

@entretoize And welcome! :confetti_ball: :slightly_smiling_face:

-------------------------

entretoize | 2019-05-03 16:28:29 UTC | #5

OK, it's logic, but I don't see how to have a white material.
My actual code :

        //a simple plane with texture:
        Node* planeNode = scene_->CreateChild("Plane");
        planeNode->SetScale(Vector3(100.0f, 1.0f, 100.0f));
        auto* planeObject = planeNode->CreateComponent<StaticModel>();
        planeObject->SetModel(cache->GetResource<Model>("Models/Plane.mdl"));
        planeObject->SetMaterial(cache->GetResource<Material>("Materials/StoneTiled.xml"));


    	// custom geometry
    	Node* lineNode = scene_->CreateChild("lineNode");
    	CustomGeometry* cg = lineNode->CreateComponent<CustomGeometry>();
    	cg->Clear();
    	cg->SetNumGeometries(1);
    	cg->BeginGeometry(0, PrimitiveType::TRIANGLE_LIST);
    	cg->DefineVertex(Vector3::Vector3(0, 0, 0));
    	cg->DefineVertex(Vector3::Vector3(10, 10, 0));
    	cg->DefineVertex(Vector3::Vector3(10, 0, 0));
    	cg->DefineColor(Color::WHITE);
    	//Material* mat = new Material(context_);
    	//mat->SetFillMode(FillMode::FILL_SOLID);
    	cg->SetMaterial(cache->GetResource<Material>("Materials/StoneTiled.xml"));
    	cg->Commit();

    	lineNode->SetPosition(Vector3::Vector3(0, 0, 0));

As you see I build a plane and a custom polygon, the plane is well textured so I used the same material to try, but the triangle is dark grey.

-------------------------

Modanung | 2019-05-03 18:15:26 UTC | #6

The stone material has a normal map which requires *tangent* data to be rendered correctly. Try with a simpler material.

-------------------------

entretoize | 2019-05-04 12:44:54 UTC | #7

OK, I found the first problem was not setting a normal, this is my modified code:

    	cg->DefineVertex(Vector3::Vector3(0, 0, 0));
    	cg->DefineNormal(Vector3::Vector3(0, 1, 0));
    	cg->DefineVertex(Vector3::Vector3(10, 10, -10));
    	cg->DefineNormal(Vector3::Vector3(0, 1, 0));
    	cg->DefineVertex(Vector3::Vector3(10, 0, 0));
    	cg->DefineNormal(Vector3::Vector3(0, 1, 0));
    	Material* mat = new Material(context_);
    	mat->SetFillMode(FillMode::FILL_SOLID);
    	mat->SetShaderParameter("MatDiffColor", Vector4(1,0,0,1));
    	mat->SetCullMode(CullMode::CULL_NONE);
    	cg->SetMaterial(mat);

Thanks for your replies.

-------------------------

Leith | 2019-05-06 09:07:01 UTC | #8

Welcome to the world of lighting! If we have surface normals in our model at all, they are typically only there at all for lighting purposes. Unlit materials don't need them.

Per-Vertex Lighting (performed in the Vertex Shader stage, using Vertex Normals) kind of sucks though - there is a way to remove normals from vertices in the mesh, and instead put them in a texture, which encodes surface normals for rapid per pixel lookup in the pixel (fragment) shader.
Enter Normal Maps!

These can encode the surface bumpyness from a much higher resolution mesh, baked to texture, and applied in the shader to a much lower resolution mesh. You get nice high resolution rendering at low cost, but you need to take some time to pre-bake your normal map(s). We trade some offline processing time for both faster and better looking results at runtime ;)

One single triangle can benefit from per pixel lighting, a single textured quad (two triangles) is a prime example. Embossing and other per pixel effects can be implemented using textures, moving the art requirement into the hands of the artists, while reducing the technical requirements for vertex data at runtime.

-------------------------

