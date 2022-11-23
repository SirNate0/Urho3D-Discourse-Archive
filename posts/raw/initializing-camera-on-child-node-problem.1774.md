godan | 2017-01-02 01:10:01 UTC | #1

Hi all,

I'm running in to an issue when I try to create a camera component on a child node (in C++). Here's code that works:

[code]	// Create the camera
	cameraNode_ = scene_->CreateChild("OrbitCamera");
	orbit_cam_ = cameraNode_->CreateComponent<OrbitCamera>();
	child_node = scene_->CreateChild("CamNode");

	Camera* camera_ = cameraNode_->CreateComponent<Camera>(); //NOTE: creating a camera on this node works fine
[/code]

However, when I change the code so that I create the camera on a child node of 'cameraNode', I get a black screen:

[code]	// Create the camera
	cameraNode_ = scene_->CreateChild("OrbitCamera");
	orbit_cam_ = cameraNode_->CreateComponent<OrbitCamera>();
	child_node = scene_->CreateChild("CamNode");

	Camera* camera_ = child_node ->CreateComponent<Camera>(); //NOTE: creating a camera now gives me a black screen
[/code]

Can't figure it out. Btw, having a camera on a child object is very useful for 3d Camera rigs (i.e. the parent node is the Pivot point), I would like to get this working. Also, this code is just running in the standard CreateScene method, taken almost verbatim out of the samples.

-------------------------

thebluefish | 2017-01-02 01:10:01 UTC | #2

What's the code look like that creates the Viewport? I have a feeling that the Camera object you're passing to it is now a nullptr.

-------------------------

godan | 2017-01-02 01:10:01 UTC | #3

Here's the viewport code:

[code]Renderer* renderer = GetSubsystem<Renderer>();
	// Set up a viewport to the Renderer subsystem so that the 3D scene can be seen
	IntRect* rect = new IntRect(0,0,1024, 680);
	SharedPtr<Viewport> viewport(new Viewport(context_, scene_, cameraNode_->GetComponent<Camera>()));

	renderer->SetViewport(0, viewport);
	renderer->SetShadowMapSize(2048);
	renderer->SetShadowQuality(2);

	ResourceCache* cache = GetSubsystem<ResourceCache>();
	RenderPath* render_path = new RenderPath();
	render_path->Load(cache->GetResource<XMLFile>("RenderPaths/ForwardDepth.xml"));
	viewport->SetRenderPath(render_path);[/code]

-------------------------

thebluefish | 2017-01-02 01:10:01 UTC | #4

[code]cameraNode_->GetComponent<Camera>()[/code]

Hmmmmmmmmmm................

-------------------------

godan | 2017-01-02 01:10:01 UTC | #5

That'll do it :slight_smile: Thanks for your help.

-------------------------

