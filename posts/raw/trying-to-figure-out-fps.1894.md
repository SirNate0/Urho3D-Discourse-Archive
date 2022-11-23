vivienneanthony | 2017-01-02 01:11:13 UTC | #1

Hi,

I'm trying to figure out what's killing my FPS.  I have a I7-2700k CPU, 16 gig ram, EVGA GTX 950 ti, 128 GB ssd, and huge HD. I'm not sure why the framerate isn't about 60 fps.

Test Video
[youtube.com/watch?v=VlugiYVOZxQ](https://www.youtube.com/watch?v=VlugiYVOZxQ)

Other
[youtube.com/watch?v=r4gcA_GKlQw](https://www.youtube.com/watch?v=r4gcA_GKlQw)

I'm using these base code for this scene. I disabled all rigidbody and collisions since this is pretty much pre-defined.

Vivienne
[code]

void MainMenuView::CreateManualScene(void)
{
    // Update Renderer
    AnimationManager * pAnimationManager = g_pApp->GetGameLogic()->GetAnimationsManager();

    // Update renderer setting decrease rendering quality and increase frame rate
  	m_pRenderer->SetShadowQuality(SHADOWQUALITY_SIMPLE_16BIT);
    m_pRenderer->SetShadowMapSize(1024);
    m_pRenderer->SetDynamicInstancing(true);
    m_pRenderer->SetTextureQuality(QUALITY_MEDIUM);
    m_pRenderer->SetMaterialQuality(QUALITY_MEDIUM);

    // Update scene
    m_pScene = SharedPtr<Scene>(new Scene(context_));


    // Reset Scene for Applications Manager
    pAnimationManager->SetScene(m_pScene);

    // Add octree
    m_pScene->CreateComponent<Octree>();

    // Load a demo file
    LevelManager* pLevelManager = g_pApp->GetGameLogic()->GetLevelManager();
    pLevelManager->LoadLevel(m_pScene, "Levels/LoginScene1.xml", false);

    // Create a temporary Vector
    PODVector<CameraComponent *> Cameras;

    // Get scene camera components
    m_pScene->GetComponents(Cameras, "CameraComponent");

    // Create a iternator
    PODVector<CameraComponent *>::Iterator thisComponent;

    // Loop through each component
    for(thisComponent = Cameras.Begin(); thisComponent!=Cameras.End(); ++thisComponent)
    {
        if((*thisComponent)->GetDefault() == true)
        {
            // Get the Camera Component Node
            m_pCameraNode = (*thisComponent)->GetNode();

            // Set new Viewport using CameraComponent
            m_pViewport = new Viewport(context_, m_pScene, m_pCameraNode->GetComponent<CameraComponent>());

            break;
        }
    }

    // If Camera Node is not Null then there must have been a default camera
    if(m_pCameraNode==NULL)
    {
        // Create a scene node for the camera, which we will move around
        // The camera will use default settings (1000 far clip distance, 45 degrees FOV, set aspect ratio automatically)
        m_pCameraNode = m_pScene->CreateChild(String("Camera").ToHash(), CreateMode::LOCAL);
        m_pCameraNode->CreateComponent<Camera>();

        // Set Position
        m_pCameraNode->SetPosition(Vector3(-400.0f,60.0f,200.0f));

        // Test Look at
        m_pCameraNode->LookAt(Vector3(0.0f,0.0f,0.0f));
        m_pCameraNode->GetComponent<Camera>()->SetFarClip(2000.0);

        // Set new Viewport using Camera
        m_pViewport = new Viewport(context_, m_pScene, m_pCameraNode->GetComponent<Camera>());

    }

    // Set Viewport
    m_pRenderer->SetViewport(0, m_pViewport);

    SharedPtr<RenderPath> m_pFXRenderPath= m_pViewport->GetRenderPath()->Clone();

    m_pFXRenderPath->Append(g_pApp->GetConstantResCache()->GetResource<XMLFile>("PostProcess/Bloom.xml"));
    m_pFXRenderPath->Append(g_pApp->GetConstantResCache()->GetResource<XMLFile>("PostProcess/FXAA3.xml"));

    // Make the bloom mixing parameter more pronounced
    m_pFXRenderPath->SetShaderParameter("BloomMix", Vector2(0.98f, 0.02f));
    m_pFXRenderPath->SetEnabled("Bloom", true);
    m_pFXRenderPath->SetEnabled("FXAA3", true);

    // Set active path
    m_pViewport->SetRenderPath(m_pFXRenderPath);

    // Create a temporary Vector
    PODVector<AnimationControllerComponent *> AnimationControllers;

    // Get scene AnimationController components
    m_pScene->GetComponents(AnimationControllers, "AnimationControllerComponent");

    // Create a iternator
    PODVector<AnimationControllerComponent *>::Iterator thisControllerComponent;

    // Loop through each component
    for(thisControllerComponent = AnimationControllers.Begin(); thisControllerComponent!=AnimationControllers.End(); ++thisControllerComponent)
    {
       pAnimationManager->AddAnimationController(*thisControllerComponent);
    }

    return;[/code]
}

-------------------------

1vanK | 2017-01-02 01:11:14 UTC | #2

Present = 850 ms (try without imgui interface)

-------------------------

thebluefish | 2017-01-02 01:11:14 UTC | #3

[quote="1vanK"](try without imgui interface)[/quote]

At least add additional profiling to imgui to get a better idea of what impact it's making. However I will agree that it is the most likely culprit.

-------------------------

vivienneanthony | 2017-01-02 01:11:14 UTC | #4

[quote="thebluefish"][quote="1vanK"](try without imgui interface)[/quote]

At least add additional profiling to imgui to get a better idea of what impact it's making. However I will agree that it is the most likely culprit.[/quote]

Maybe. Itook out the ImGui base elements which did not help much Now I'm looking at this. I might remove firstly the get screen size every frame which is overkill. The Update Scene and Physics part average around 60, just everything else isn't.


[code]void ImGuiInterface::HandleBeginFrame(StringHash eventType, VariantMap& eventData)
{
    URHO3D_PROFILE(ImGuiInterface_BeginFrame);
    using namespace BeginFrame;
    float timeStep = eventData[P_TIMESTEP].GetFloat();

    // Setup display size (every frame to accommodate for window resizing)
    ImGuiIO& io = ImGui::GetIO();
    io.DisplaySize = ImVec2((float)graphics_->GetWidth(), (float)graphics_->GetHeight());

    // Setup time step
    io.DeltaTime = timeStep > 0.0f ? timeStep : 1.0f / 60.0f;

    // Setup inputs
    // mouse input handling
    if (input_->IsMouseVisible() && !input_->GetTouchEmulation())
    {
        IntVector2 pos = input_->GetMousePosition();
        // Mouse position, in pixels (set to -1,-1 if no mouse / on another screen, etc.)
        io.MousePos.x = (float)pos.x_;
        io.MousePos.y = (float)pos.y_;
    }
    else
    {
        io.MousePos.x = -1.0f;
        io.MousePos.y = -1.0f;
    }
    // TODO: Joystick input handling

    // TODO: touch input handling
    if (touchId_ != -1)
    {
        io.MousePos.x = (float)touchPos_.x_;
        io.MousePos.y = (float)touchPos_.y_;
        io.MouseDown[0] = touch_;
        // disable tracking
        if (!touch_)
            touchId_ = -1;
    }
    else
        io.MouseDown[0] = input_->GetMouseButtonDown(MOUSEB_LEFT);

    io.MouseDown[1] = input_->GetMouseButtonDown(MOUSEB_RIGHT);
    io.MouseDown[2] = input_->GetMouseButtonDown(MOUSEB_MIDDLE);
    io.MouseWheel = (float)input_->GetMouseMoveWheel();

    io.KeyCtrl = input_->GetQualifierDown(QUAL_CTRL);
    io.KeyShift = input_->GetQualifierDown(QUAL_SHIFT);
    io.KeyAlt = input_->GetQualifierDown(QUAL_ALT);

    // Start the frame
    ImGui::NewFrame();

    // show screenkeyboard on text edit
    if (useScreenKeyboard_)
        input_->SetScreenKeyboardVisible(io.WantTextInput);
}

void ImGuiInterface::HandleEndRendering(StringHash eventType, VariantMap& eventData)
{
    URHO3D_PROFILE(ImGuiInterface_Rendering);
    ImGui::Render();
}[/code]

-------------------------

thebluefish | 2017-01-02 01:11:14 UTC | #5

That should work. What does it say now when you run the game?

-------------------------

vivienneanthony | 2017-01-02 01:11:14 UTC | #6

[quote="thebluefish"]That should work. What does it say now when you run the game?[/quote]

Roughly the same numbers.

[i.imgur.com/u1YlTHt.png](http://i.imgur.com/u1YlTHt.png)

-------------------------

1vanK | 2017-01-02 01:11:14 UTC | #7

You need to look all the functions that are used in E_ENDRENDERING

-------------------------

cadaver | 2017-01-02 01:11:16 UTC | #8

A large amount of time spent in Present can simply mean that the GPU has a lot of work to do. You seem to be doing at least several shadowed lights and postprocesses. Have you tried disabling these? (note that the profiler entries under Render but before Present don't accurately represent GPU work, it's just the CPU time taken to submit those render commands). Also, do you have Vsync on? If yes, disable it to see your actual framerate, otherwise it's always 60 divided by something. Vsync waiting goes under Present in the profiler.

-------------------------

vivienneanthony | 2017-01-02 01:11:18 UTC | #9

[quote="cadaver"]A large amount of time spent in Present can simply mean that the GPU has a lot of work to do. You seem to be doing at least several shadowed lights and postprocesses. Have you tried disabling these? (note that the profiler entries under Render but before Present don't accurately represent GPU work, it's just the CPU time taken to submit those render commands). Also, do you have Vsync on? If yes, disable it to see your actual framerate, otherwise it's always 60 divided by something. Vsync waiting goes under Present in the profiler.[/quote]

I took everyone advice. ImGui wasn't the problem but I should optimize that code. The main culprit is the light, shadows, and the VSync.

I got the FPS up from 22/30 to 54 with everything put back. The rest is optimizing the scene.

I was able to pull this off and the video is a bit smoother compared to the original.

[youtube.com/watch?v=v1XraHiSf9w](https://www.youtube.com/watch?v=v1XraHiSf9w)

Ironically, the ground map works better and I get the full 200 fps.

-------------------------

