ChunFengTsin | 2017-12-05 07:30:15 UTC | #1

Hello everyone,

This case is that I made a small game like minecraft.

I afraid it is terrible to loading  thousands cube model to scene.

But , If I loading only one cube model in memory  and shared it to others , it also need to send thousands cube data to GPU, 

Is possible to shared the cube  on GPU with Urho3D, like Geometry_instacing with OpenGL or D3D.

: I am not familiar to Geometry_instacing.....

-------------------------

Eugene | 2017-12-05 08:03:11 UTC | #2

[quote="ChunFengTsin, post:1, topic:3819"]
Is possible to shared the cube  on GPU with Urho3D, like Geometry_instacing with OpenGL or D3D
[/quote]
All objects with same model and material are automatically instanced as long as your GPU supports it.

[quote="ChunFengTsin, post:1, topic:3819"]
This case is that I made a small game like minecraft.
[/quote]
The commonplace guideline is to build voxel data geometry manually. For example, via `CustomGeometry` in Urho. It's not so hard and it's more performant than any generic solution.

-------------------------

ChunFengTsin | 2017-12-05 08:18:03 UTC | #3

oh, thanks , where can I find sample code about CustomGeometry?
just  need some few lines code

-------------------------

johnnycable | 2017-12-05 09:40:19 UTC | #4

Here's a [simple](https://discourse.urho3d.io/t/color-on-3d-lines/3414/2?u=johnnycable) one.

-------------------------

ChunFengTsin | 2017-12-05 10:04:52 UTC | #5

The web information :  Sorry, you don't have access to that topic!

-------------------------

Eugene | 2017-12-07 13:45:22 UTC | #6

You could see some examples if you search `CustomGeometry` over codebase:

https://github.com/urho3d/Urho3D/blob/83c17c7dc69044fe904d77f4dedd0b62b834811c/bin/Data/Scripts/Editor/EditorTerrain.as#L18

https://github.com/urho3d/Urho3D/blob/f413945c989e96297bbcc3e610578bb758f968eb/bin/Data/Scripts/Editor/EditorView.as#L1182

-------------------------

johnnycable | 2017-12-07 13:45:22 UTC | #7

Found the solution here: https://www.youtube.com/watch?v=sNT8SMlqLJA1 :sunglasses:


    #create 2d ortho camera

    scene_ = new Scene(context_);
    scene_->CreateComponent<Octree>();

    // Create camera node
    cameraNode_ = scene_->CreateChild("Camera");
    // Set camera's position
    cameraNode_->SetPosition(Vector3(0.0f, 0.0f, -10.0f));

    Camera* camera = cameraNode_->CreateComponent<Camera>();
    camera->SetOrthographic(true);

    Graphics* graphics = GetSubsystem<Graphics>();
    camera->SetOrthoSize((float)graphics->GetHeight() * PIXEL_SIZE);

    // custom geometry lambda
    auto triangleMan = [&](){

    // classical one up
    // center of screen, ortho 2d elevation
    auto scp = camera->ScreenToWorldPoint(Vector3(0.5f,0.5f,-1));
    triangleNode = scene_->CreateChild("triangleNode");
    CustomGeometry* cg = triangleNode->CreateComponent<CustomGeometry>();
    cg->Clear();
    cg->SetNumGeometries(1);
    cg->BeginGeometry(0, PrimitiveType::TRIANGLE_LIST);
    cg->DefineVertex(Vector3(-1,0,0));
    cg->DefineColor(Color::GREEN);
    cg->DefineVertex(Vector3(0,1,0));
    cg->DefineColor(Color::RED);
    cg->DefineVertex(Vector3(1,0,0));
    cg->DefineColor(Color::BLUE);
    Material* mat = new Material(context_);
    auto teq = cache->GetResource<Technique("Techniques/NoTextureUnlitVCol.xml");
    mat->SetTechnique(0, teq);
    cg->SetMaterial(mat);
    mat->SetFillMode(FillMode::FILL_SOLID);
    cg->Commit();
    triangleNode->SetPosition(scp);

    // black one down
    scp = camera->ScreenToWorldPoint(Vector3(0.5f,0.5f,-1));
    Node* lineNode2 = scene_->CreateChild("lineNode2");
    cg = lineNode2->CreateComponent<CustomGeometry>();
    cg->Clear();
    cg->SetNumGeometries(1);
    cg->BeginGeometry(0, PrimitiveType::TRIANGLE_LIST);
    cg->DefineVertex(Vector3(1,0,0));
    cg->DefineVertex(Vector3(0,-1,0));
    cg->DefineVertex(Vector3(-1,0,0));
    cg->DefineColor(Color::WHITE);
    mat = new Material(context_);
    mat->SetFillMode(FillMode::FILL_SOLID);
    cg->SetMaterial(mat);
    cg->Commit();
    lineNode2->SetPosition(scp)
    };

    triangleMan();

-------------------------

ChunFengTsin | 2017-12-05 14:00:20 UTC | #8

thank you all, 
 very nice!!!

-------------------------

ChunFengTsin | 2017-12-16 14:06:57 UTC | #9

Hi!, do you know how to produce shadow of CustomGeometry?

-------------------------

Eugene | 2017-12-16 16:01:20 UTC | #10

[quote="ChunFengTsin, post:9, topic:3819, full:true"]
Hi!, do you know how to produce shadow of CustomGeometry?
[/quote]

Well, should be the same as for any other `Drawable`, just turn on "Cast Shadows"

-------------------------

ChunFengTsin | 2017-12-17 03:14:35 UTC | #11

I just draw a single triangle in scene , it work well with CustomGeometry,  and I SetCastShadows(true); 
it doesn't work..
::else object in scene have shadow normally.

 
    SharedPtr<Node>  TriangleNode(scene_->CreateChild("triangleNode"));
    CustomGeometry * cg = TriangleNode->CreateComponent<CustomGeometry>();
    cg->Clear();
    cg->SetNumGeometries(1);
    cg->BeginGeometry(0, PrimitiveType::TRIANGLE_LIST);

    cg->DefineVertex(Vector3(-1,0,0));
    cg->DefineColor(Color::GREEN);
    cg->DefineVertex(Vector3(0,100,0));
    cg->DefineColor(Color::RED);
    cg->DefineVertex(Vector3(1,0,0));
    cg->DefineColor(Color::BLUE);
    Material* mat = new Material(context_);
    auto teq = cache->GetResource<Technique>("Techniques/NoTextureUnlitVCol.xml");
    mat->SetTechnique(0, teq);
    cg->SetMaterial(mat);
    mat->SetFillMode(FillMode::FILL_SOLID);
    cg->SetCastShadows(true);
    cg->Commit();

it need a thickness ?

-------------------------

Eugene | 2017-12-17 08:23:08 UTC | #12

Standard material may cast shadows only from back faces.
You should either tune material or generate enclosed two-sided surfaces

-------------------------

