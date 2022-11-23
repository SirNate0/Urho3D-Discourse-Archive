wakko | 2018-05-18 21:46:13 UTC | #1

How do I add a spotlight (facing in the camera's direction) to the camera node?
When I do the intuitive thing the light won't show up:

    // Create the camera
    cameraNode_ = new Node(context_);
    cameraNode_->SetPosition(Vector3(0.0f, 3.0f, -20.0f));
    Camera* camera = cameraNode_->CreateComponent<Camera>();
    camera->SetFarClip(300.0f);

    // Create a directional light
    m_cameraLightNode = cameraNode_->CreateChild("CameraLight"); // no light appears...
    // m_cameraLightNode = scene_->CreateChild("CameraLightNode"); // this line would show the light
    m_cameraLightNode->SetPosition(Vector3(cameraNode_->GetPosition()));
    m_cameraLightNode->SetDirection(Vector3::FORWARD);
    Light* camlight = m_cameraLightNode->CreateComponent<Light>(); 
    // I have tested this with no effect:
    // Light* camlight = cameraNode_->CreateComponent<Light>(); 
    camlight->SetLightType(LIGHT_SPOT);
    camlight->SetColor(Color(0.4f, 0.4f, 0.4f));
    // ...... more spotlight parameters after this line

The light only appears when I add it to the scene directly...
Adding the spotlight component to the cameraNode_ didn't work either.
What am I doing wrong here?

-------------------------

JTippetts | 2018-05-18 21:46:07 UTC | #2

The light won't show because cameraNode is not a child of the scene, so any of its children are not in the scene's tree. People often leave the camera outside the main scene to avoid the camera being saved/serialized if the scene is serialized. If you don't plan on saving your scenes, your you don't care if the camera gets saved, there is nothing wrong with making cameraNode a child of the scene.

-------------------------

wakko | 2018-05-18 18:13:21 UTC | #3

Thanks for the reply. This helped. :slight_smile:
I already was suspicious about the camera node created as "new Node(context_)" and not as a child of something else. I just didn't try to change that...

-------------------------

