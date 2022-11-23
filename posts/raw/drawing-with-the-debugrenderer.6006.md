claudeHasler | 2020-03-20 08:22:44 UTC | #1

Im trying to draw some geometry with the debugRenderer
Start():
[Code]
   SubscribeToEvent(E_POSTRENDERUPDATE, URHO3D_HANDLER(MyApp, DrawDebug));

    scene_ = new Scene(context_);
    debugRenderer_ = scene_->CreateComponent<DebugRenderer>();

    // Let the scene have an Octree component!
    scene_->CreateComponent<Octree>();

    // We need a camera from which the viewport can render.
    cameraNode_ = scene_->CreateChild("Camera");
    Camera* camera = cameraNode_->CreateComponent<Camera>();
    camera->SetFarClip(2000);
  
    // Now we setup the viewport. Of course, you can have more than one!
    Renderer* renderer = GetSubsystem<Renderer>();
    SharedPtr<Viewport> viewport(new Viewport(context_, scene_, cameraNode_->GetComponent<Camera>()));
    renderer->SetViewport(0, viewport);
[/Code]

[Code]
void MyApp::DrawDebug(StringHash eventType, VariantMap& eventData)
{
    debugRenderer_->AddLine(Vector3(-10, -10, -100), Vector3(10, 10,100), Color(255,0,0), false);
}
[/Code]

But im not seeing anything. Am i missing a step or is my geometry simply not on screen?

-------------------------

SirNate0 | 2020-03-20 20:22:31 UTC | #2

Is the camera pointed at the line?

-------------------------

claudeHasler | 2020-03-20 20:22:31 UTC | #3

It turns out my camera was not pointing at the line, now it works fine, thanks

-------------------------

