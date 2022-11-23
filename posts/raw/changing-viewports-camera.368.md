vivienneanthony | 2017-01-02 00:59:55 UTC | #1

Hello,

I'm trying to setup a first person view using a camera in a local node with a camera component below the main character node. The viewport camera works but I'm not sure why when i attempt to switch. The camera falls.

In the future I would like to  put a camera in a invisible box so I can test collision and move it according to the parent character. I hate seeing through things in games

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

    // Set zero angular factor so that physics doesn't turn the character on its own.
    // Instead we will control the character yaw manually
    body->SetAngularFactor(Vector3::ZERO);

    // Set the rigidbody to signal collision also when in rest, so that we get ground collisions properly
    body->SetCollisionEventMode(COLLISION_ALWAYS);

    // Set a capsule shape for collision
    CollisionShape* shape = objectNode->CreateComponent<CollisionShape>();
    //shape->SetConvexHull(cache->GetResource<Model>("Resources/Models/standardfemale:Body.mdl"));
    shape->SetBox(Vector3::ZERO);
    shape->SetLodLevel(1);

    // Create the character logic component, which takes care of steering the rigidbody
    // Remember it so that we can set the controls. Use a WeakPtr because the scene hierarchy already owns it
    // and keeps it alive as long as it's not removed from the hierarchy
    //character_ = objectNode->CreateComponent<Character>();

    // Create a scene node for the camera, which we will move around
    Node * cameraFirstPersonNode_  = objectNode -> CreateChild("CameraFirstPerson");

    // Set an initial position for the camera scene node above the plane
    cameraFirstPersonNode_->SetPosition(Vector3(0.0f,1.0f,0.0f));
    cameraFirstPersonNode_->SetRotation(Quaternion(0.0,0.0,0.0));

    Camera* cameraObject = cameraFirstPersonNode_->CreateComponent<Camera>();
    cameraObject->SetOrthographic(0);
    cameraObject->SetZoom(0);

    ExistenceGameState.SetCameraMode(CAMERAMODE_FIRSTPERSON);

    // Set up a viewport to the Renderer subsystem so that the 3D scene can be seen. We need to define the scene and the camera
    // at minimum. Additionally we could configure the viewport screen size and the rendering path (eg. forward / deferred) to
    // use, but now we just use full screen and default render path configured	SetOrthographic ( in the engine command line options
    SharedPtr<Viewport> viewFirstPerson(new Viewport(context_, scene_,cameraFirstPersonNode_->GetComponent<Camera>()));
    renderer->SetViewport(0, viewFirstPerson);


    return;
}
[/code]

-------------------------

vivienneanthony | 2017-01-02 00:59:55 UTC | #2

I also tried moving the viewport pointer to the main class for the applications. The program loads but when I attempt to switch cameras I get a segmentation fault. So, I'm assuming I can't switch cameras while the viewport is active??

[code]// Create a scene node for the camera, which we will move around
    Node * cameraFirstPersonNode_  = scene_-> CreateChild("CameraFirstPerson");

    // Set an initial position for the camera scene node above the plane
    cameraFirstPersonNode_->SetPosition(Vector3(1.0f,1.0f,1.0f));
    cameraFirstPersonNode_->SetRotation(Quaternion(0.0,0.0,0.0));

    Camera* cameraObject = cameraFirstPersonNode_->CreateComponent<Camera>();
    cameraObject->SetOrthographic(0);
    cameraObject->SetZoom(0);

    ExistenceGameState.SetCameraMode(CAMERAMODE_FIRSTPERSON);

    // Set up a viewport to the Renderer subsystem so that the 3D scene can be seen. We need to define the scene and the camera
    // at minimum. Additionally we could configure the viewport screen size and the rendering path (eg. forward / deferred) to
    // use, but now we just use full screen and default render path configured	SetOrthographic ( in the engine command line options
    viewport -> SetCamera(cameraObject);
[/code]

-------------------------

vivienneanthony | 2017-01-02 00:59:55 UTC | #3

Hey 

Think  I have it fixed. Thank God! Anyway.

It's not the most elegant of solutions but if someone has a suggestion. I'm open.

Vivienne

[code]  if(parseinput[0] == "/camerafirstpersonmode")
        {
            // locate camera in scene
            Node * cameraNode = scene_->GetChild("CameraFirstPerson",true);
            Camera* cameraObject = cameraNode->CreateComponent<Camera>();

            // create a new viewport
            SharedPtr<Viewport> viewport(new Viewport(context_, scene_, cameraObject));
            renderer->SetViewport(0, viewport);

            ExistenceGameState.SetCameraMode(CAMERAMODE_FIRSTPERSON);
        }

        if(parseinput[0] == "/cameraflymode")
        {
            // locate camera in scene
            Node * cameraNode = scene_->GetChild("Camera",true);
            Camera* cameraObject = cameraNode->CreateComponent<Camera>();

            // create a new viewport
            SharedPtr<Viewport> viewport(new Viewport(context_, scene_, cameraObject));
            renderer->SetViewport(0, viewport);

            ExistenceGameState.SetCameraMode(CAMERAMODE_FLY);
        }
[/code]

-------------------------

