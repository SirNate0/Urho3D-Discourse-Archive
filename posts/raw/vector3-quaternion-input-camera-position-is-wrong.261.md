umen | 2017-01-02 00:59:12 UTC | #1

Hey all
i have some strange Behavior or its that way the engine Behave and i need to understand it . i dont know .. 
this is what i have , 
in the Editor i have 3d object that is placed in:
position : 0,0,0
rotation :0,0,0

Camera placed in :
position :-10.9983f, 4.51806f, -0.278656f
rotation :26.7558, 85.3758,-2.08535

basically camera is looking at the 3d object a little bit above the object .
here is the image attached:
 [url]http://i.imgur.com/sRDbuJZ.png[/url]

now in code i translate it to this:
[code]//3d object 
Node* objectNode = scene_->CreateChild("AirCraft");
objectNode->SetPosition(Vector3(0.0f, 0.0f, 0.0f));
AnimatedModel* object = objectNode->CreateComponent<AnimatedModel>();
object->SetModel(cache->GetResource<Model>("Models/AirCraft.mdl"));
object->SetMaterial(cache->GetResource<Material>("Materials/AirCraftMaterial.xml"));
object->SetCastShadows(true);
objectNode->CreateComponent<AnimationController>();
//camera
cameraNode_ = scene_->CreateChild("Camera");
cameraNode_->CreateComponent<Camera>();    
cameraNode_->SetPosition(Vector3(-10.9983f, 4.51806f, -0.278656f));
cameraNode_->SetRotation(Quaternion(26.7558, 85.3758,-2.08535));

[/code]

when i compile and run the code , the camera is looking in the opposite direction  
i know this by the logging the values of the camera  .
when i print the camera position i get :
[code] Quaternion cameraQuaternion =   cameraNode_->GetRotation();
    Vector3 cameraVec3 = cameraNode_->GetPosition();
    LOGERRORF("  v3-x: %d v3-y: %d v3-z: %d, Q-x: %d Q-y: %d Q-z: %d",cameraVec3.x_,cameraVec3.y_,cameraVec3.z_,cameraQuaternion.x_,cameraQuaternion.y_,cameraQuaternion.z_ );
[/code]
this is the result :

[code]  v3-x: 536870912 v3-y: -1071251679 v3-z: 1610612736, Q-x: 1074926206 Q-y: 0 Q-z: -1076767360[/code]

i have 2 questions :
1. why the Quaternion  values seams to be right  ? but the camera is looking at the opposite direction  
2. why  the values i print are large values and not the one i set in the start ?


here is all the code mybe something is wrong there .
[code]
// Expands to this example's entry-point
DEFINE_APPLICATION_MAIN(HelloWorld)

HelloWorld::HelloWorld(Context* context) :
    Sample(context)
{
}

void HelloWorld::Start()
{
    // Execute base class startup
    Sample::Start();

    cache = GetSubsystem<ResourceCache>();
    CreateScene();
    createAirCraft();
    // Create the UI content
    SetupViewport();

    // Finally subscribe to the update event. Note that by subscribing events at this point we have already missed some events
    // like the ScreenMode event sent by the Graphics subsystem when opening the application window. To catch those as well we
    // could subscribe in the constructor instead.
    SubscribeToEvents();

    Quaternion cameraQuaternion =   cameraNode_->GetRotation();
    Vector3 cameraVec3 = cameraNode_->GetPosition();
    LOGERRORF("Start() v3-x: %d v3-y: %d v3-z: %d, Q-x: %d Q-y: %d Q-z: %d",cameraVec3.x_,cameraVec3.y_,cameraVec3.z_,cameraQuaternion.x_,cameraQuaternion.y_,cameraQuaternion.z_ );
}

 

void HelloWorld::CreateScene()
{
   

    scene_ = new Scene(context_);

    // Create the Octree component to the scene. This is required before adding any drawable components, or else nothing will
    // show up. The default octree volume will be from (-1000, -1000, -1000) to (1000, 1000, 1000) in world coordinates; it
    // is also legal to place objects outside the volume but their visibility can then not be checked in a hierarchically
    // optimizing manner
    scene_->CreateComponent<Octree>();




    // Create static scene content. First create a zone for ambient lighting and fog control
    Node* zoneNode = scene_->CreateChild("Zone");
    Zone* zone = zoneNode->CreateComponent<Zone>();
    zone->SetAmbientColor(Color(0.15f, 0.15f, 0.15f));
    zone->SetFogColor(Color(0.5f, 0.5f, 0.7f));
    zone->SetFogStart(100.0f);
    zone->SetFogEnd(300.0f);
    zone->SetBoundingBox(BoundingBox(-1000.0f, 1000.0f));


   
    // Create a directional light to the world so that we can see something. The light scene node's orientation controls the
    // light direction; we will use the SetDirection() function which calculates the orientation from a forward direction vector.
    // The light will use default settings (white light, no shadows)
    Node* lightNode = scene_->CreateChild("DirectionalLight");
    lightNode->SetDirection(Vector3(0.6f, -1.0f, 0.8f)); // The direction vector does not need to be normalized
    Light* light = lightNode->CreateComponent<Light>();
    light->SetLightType(LIGHT_DIRECTIONAL);
    light->SetCastShadows(true);
    light->SetShadowBias(BiasParameters(0.00025f, 0.5f));
    light->SetShadowCascade(CascadeParameters(10.0f, 50.0f, 200.0f, 0.0f, 0.8f));
    light->SetSpecularIntensity(0.5f);

     
    // Create a scene node for the camera, which we will move around
    // The camera will use default settings (1000 far clip distance, 45 degrees FOV, set aspect ratio automatically)
    cameraNode_ = scene_->CreateChild("Camera");
    cameraNode_->CreateComponent<Camera>();
    // Set an initial position for the camera scene node above the plane
    cameraNode_->SetPosition(Vector3(-10.9983f, 4.51806f, -0.278656f));
    cameraNode_->SetRotation(Quaternion(26.7558, 85.3758,-2.08535));


    
    Quaternion cameraQuaternion =   cameraNode_->GetRotation();
    Vector3 cameraVec3 = cameraNode_->GetPosition();
    LOGERRORF("CreateScene() v3-x: %d v3-y: %d v3-z: %d, Q-x: %d Q-y: %d Q-z: %d",cameraVec3.x_,
                                                                                    cameraVec3.y_,
                                                                                    cameraVec3.z_,
                                                                                    cameraQuaternion.x_,
                                                                                    cameraQuaternion.y_,
                                                                                    cameraQuaternion.z_ );

    
}


void HelloWorld::createPlan()
{
     // Create a child scene node (at world origin) and a StaticModel component into it. Set the StaticModel to show a simple
    // plane mesh with a "stone" material. Note that naming the scene nodes is optional. Scale the scene node larger
    // (100 x 100 world units)
    Node* planeNode = scene_->CreateChild("Plane");
    //planeNode->SetScale(Vector3(100.0f, 1.0f, 100.0f));
    planeNode->SetScale(Vector3(100.0f, 1.0f, 100.0f));
    StaticModel* planeObject = planeNode->CreateComponent<StaticModel>();
    planeObject->SetModel(cache->GetResource<Model>("Models/GroundPlane.mdl"));
    planeObject->SetMaterial(0,cache->GetResource<Material>("Materials/Ground_Material.xml"));
    planeObject->SetMaterial(1,cache->GetResource<Material>("Materials/Mountain_Material.xml"));
    planeObject->SetCastShadows(true);
}

void HelloWorld::createAirCraft()
{
     

    Node* objectNode = scene_->CreateChild("AirCraft");
    objectNode->SetPosition(Vector3(0.0f, 0.0f, 0.0f));

    // Create the rendering component + animation controller
    AnimatedModel* object = objectNode->CreateComponent<AnimatedModel>();
    object->SetModel(cache->GetResource<Model>("Models/AirCraft.mdl"));
    object->SetMaterial(cache->GetResource<Material>("Materials/AirCraftMaterial.xml"));
    object->SetCastShadows(true);
    objectNode->CreateComponent<AnimationController>();

     
}


void HelloWorld::SetupViewport()
{
    Renderer* renderer = GetSubsystem<Renderer>();

    // Set up a viewport to the Renderer subsystem so that the 3D scene can be seen. We need to define the scene and the camera
    // at minimum. Additionally we could configure the viewport screen size and the rendering path (eg. forward / deferred) to
    // use, but now we just use full screen and default render path configured in the engine command line options
    SharedPtr<Viewport> viewport(new Viewport(context_, scene_, cameraNode_->GetComponent<Camera>()));
    renderer->SetViewport(0, viewport);
}

void HelloWorld::MoveCamera(float timeStep)
{
    // Do not move if the UI has a focused element (the console)
    if (GetSubsystem<UI>()->GetFocusElement())
        return;

    Input* input = GetSubsystem<Input>();

    // Movement speed as world units per second
    const float MOVE_SPEED = 20.0f;
    // Mouse sensitivity as degrees per pixel
    const float MOUSE_SENSITIVITY = 0.1f;

    // Use this frame's mouse motion to adjust camera node yaw and pitch. Clamp the pitch between -90 and 90 degrees
    IntVector2 mouseMove = input->GetMouseMove();
    yaw_ += MOUSE_SENSITIVITY * mouseMove.x_;
    pitch_ += MOUSE_SENSITIVITY * mouseMove.y_;
    pitch_ = Clamp(pitch_, -90.0f, 90.0f);

    // Construct new orientation for the camera scene node from yaw and pitch. Roll is fixed to zero
    cameraNode_->SetRotation(Quaternion(pitch_, yaw_, 0.0f));

    // Read WASD keys and move the camera scene node to the corresponding direction if they are pressed
    // Use the Translate() function (default local space) to move relative to the node's orientation.
    if (input->GetKeyDown('W'))
        cameraNode_->Translate(Vector3::FORWARD * MOVE_SPEED * timeStep);
    if (input->GetKeyDown('S'))
        cameraNode_->Translate(Vector3::BACK * MOVE_SPEED * timeStep);
    if (input->GetKeyDown('A'))
        cameraNode_->Translate(Vector3::LEFT * MOVE_SPEED * timeStep);
    if (input->GetKeyDown('D'))
        cameraNode_->Translate(Vector3::RIGHT * MOVE_SPEED * timeStep);
    if (input->GetKeyDown('P'))
    {
        Quaternion cameraQuaternion =   cameraNode_->GetRotation();
        Vector3 cameraVec3 = cameraNode_->GetPosition();
        LOGERRORF("MoveCamera() v3-x: %d v3-y: %d v3-z: %d, Q-x: %d Q-y: %d Q-z: %d",cameraVec3.x_,
                                                                                    cameraVec3.y_,
                                                                                    cameraVec3.z_,
                                                                                    cameraQuaternion.x_,
                                                                                    cameraQuaternion.y_,
                                                                                   cameraQuaternion.z_ );
    }
        
}
void HelloWorld::SubscribeToEvents()
{
    // Subscribe HandleUpdate() function for processing update events
    SubscribeToEvent(E_UPDATE, HANDLER(HelloWorld, HandleUpdate));
}

void HelloWorld::HandleUpdate(StringHash eventType, VariantMap& eventData)
{
    using namespace Update;

    // Take the frame time step, which is stored as a float
    float timeStep = eventData[P_TIMESTEP].GetFloat();

    // Move the camera, scale movement with time step
    MoveCamera(timeStep);
}
[/code]

-------------------------

