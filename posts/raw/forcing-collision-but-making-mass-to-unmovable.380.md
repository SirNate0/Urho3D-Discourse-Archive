vivienneanthony | 2017-01-02 00:59:59 UTC | #1

Hi,

Is there a way to make something collidable but not movable. For example a wall.

Vivienne

-------------------------

weitjong | 2017-01-02 00:59:59 UTC | #2

So does the floor, doesn't it?

-------------------------

vivienneanthony | 2017-01-02 00:59:59 UTC | #3

[quote="weitjong"]So does the floor, doesn't it?[/quote]

Not sure how to respond. It's late and tired so it's working. I have some quick run through video prob in my morning.

-------------------------

cadaver | 2017-01-02 00:59:59 UTC | #4

You probably figured it out already, but a Rigidbody with mass 0 (static mode) combined with a CollisionShape creates an unmovable colliding object. This can be a triangle mesh shape too (unlike moving objects that cannot be triangle meshes reliably).

-------------------------

vivienneanthony | 2017-01-02 00:59:59 UTC | #5

[quote="cadaver"]You probably figured it out already, but a Rigidbody with mass 0 (static mode) combined with a CollisionShape creates an unmovable colliding object. This can be a triangle mesh shape too (unlike moving objects that cannot be triangle meshes reliably).[/quote]


Yup. I'm just figuring out the best collision setup.  MakeHuman places origins at the base of a skeleton which I think should be centered.  So to use a good bound setup I will have to test the dimensions of a mesh and offset collision bound to the center.

I would love to use convex hull but I have to make a mechanism to reorient itself based on collision areas, gravity, free fall and health. As to camera points for first person view I might use a xml to store mesh attachnent point coordinates.

Hmmm.

-------------------------

vivienneanthony | 2017-01-02 00:59:59 UTC | #6

[quote="cadaver"]You probably figured it out already, but a Rigidbody with mass 0 (static mode) combined with a CollisionShape creates an unmovable colliding object. This can be a triangle mesh shape too (unlike moving objects that cannot be triangle meshes reliably).[/quote]

The video is at [www.youtube.com/watch?v=vcFBM_5I_C4&lis ... 7uTgUBQjaw](http://www.youtube.com/watch?v=vcFBM_5I_C4&list=UUTObP1VzcIglm7uTgUBQjaw)

-------------------------

vivienneanthony | 2017-01-02 01:00:00 UTC | #7

[quote="cadaver"]You probably figured it out already, but a Rigidbody with mass 0 (static mode) combined with a CollisionShape creates an unmovable colliding object. This can be a triangle mesh shape too (unlike moving objects that cannot be triangle meshes reliably).[/quote]

Hello

Is this correct to get a static point center and use it for making the colliding area? I mean to use the bounding box center to set the offset? It seems to be almost accurate.

Vivienne

[code]
// character class
void ExistenceClient::CreateCharacter(void)
{
    // get resources
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    Renderer* renderer = GetSubsystem<Renderer>();
    Graphics* graphics = GetSubsystem<Graphics>();
    UI* ui = GetSubsystem<UI>();
    FileSystem * filesystem = GetSubsystem<FileSystem>();

    //String characternode = String("Character");
    LoadCharacterMesh("Character",1,1);

    Node* objectNode = scene_->GetChild("Character");

    // Create rigidbody, and set non-zero mass so that the body becomes dynamic
    RigidBody* body = objectNode->CreateComponent<RigidBody>();
    body->SetCollisionLayer(1);
    body->SetMass(.2f);

    StaticModel * staticmodelreference = objectNode->GetComponent<StaticModel>();
    Model * staticmodel=staticmodelreference->GetModel();

    BoundingBox   staticmodelbox = staticmodel->GetBoundingBox();
    Vector3  staticmodelboxcenter= Vector3(staticmodelbox.max_-staticmodelbox.min_)/2;

    // Set zero angular factor so that physics doesn't turn the character on its own.
    // Instead we will control the character yaw manually
    body->SetAngularFactor(Vector3::ZERO);

    // Set the rigidbody to signal collision also when in rest, so that we get ground collisions properly
    body->SetCollisionEventMode(COLLISION_ALWAYS);

    // Set a capsule shape for collision
    CollisionShape* shape = objectNode->CreateComponent<CollisionShape>();
    //shape->SetConvexHull(cache->GetResource<Model>("Resources/Models/standardfemale:Body.mdl"));
    shape->SetBox(Vector3::ONE);
    shape->SetPosition(Vector3(staticmodelboxcenter));
    shape->SetLodLevel(1);

    //objectNode->SetPosition(Vector3(staticmodelboxcenter));
    character_ = objectNode->CreateComponent<Character>();

    // Create a scene node for the camera, which we will move around
    // The camera will use default settings (1000 far clip distance, 45 degrees FOV, set aspect ratio automatically)
    Node * cameraNode_ = objectNode ->CreateChild("CameraFirstPerson");

    // Set an initial position for the camera scene node above the plane
    cameraNode_->SetPosition(Vector3(0.0f,0.9f,0.185821f));
    cameraNode_->SetRotation(Quaternion(0.0,0.0,0.0));

    Camera* cameraObject = cameraNode_->CreateComponent<Camera>();
    cameraObject->SetOrthographic(0);
    cameraObject->SetZoom(1);

    ExistenceGameState.SetCameraMode(CAMERAMODE_FIRSTPERSON);

    // Set up a viewport to the Renderer subsystem so that the 3D scene can be seen. We need to define the scene and the camera
    // at minimum. Additionally we could configure the viewport screen size and the rendering path (eg. forward / deferred) to
    // use, but now we just use full screen and default render path configured	SetOrthographic ( in the engine command line options
    //viewport -> SetCamera(cameraObject);

    SharedPtr<Viewport> viewport(new Viewport(context_, scene_, cameraObject));
    renderer->SetViewport(0, viewport);

    return;
}
[/code]

-------------------------

cadaver | 2017-01-02 01:00:00 UTC | #8

Yes, if you want the collision capsule to be centered on the visible mesh's bounding box, then that's correct. You could also use the Center() member function of BoundingBox.

-------------------------

vivienneanthony | 2017-01-02 01:00:00 UTC | #9

[quote="cadaver"]Yes, if you want the collision capsule to be centered on the visible mesh's bounding box, then that's correct. You could also use the Center() member function of BoundingBox.[/quote]

I'll probably use that in a rewrite. The way I did it I realized is a line or two longer but I learned some of the inner workings this way at the same time.

The next feat is either the terrain texture or perlin generated height map.

-------------------------

