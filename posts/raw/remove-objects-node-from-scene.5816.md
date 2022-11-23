MGokcayK | 2020-01-14 20:00:42 UTC | #1

Hi, I am new for Urho3D and Graphics Engines world. I am trying to learn Urho to create my simulation enviorenment :slight_smile: then apply bullet physics. 

Today, I tried to remove node from scene. I tried node->Remove() function but it is not worked. Actually it is worked when I call scene_->Clear() function after node->Remove() and create again node with same properties  and object created in gray (because of light) and call again node->Remove() and the node is dissappeard.

Yet, it is not I want because I do not want to re-create scene. Therefore I seached a lot and in this [topic](https://discourse.urho3d.io/t/deleting-nodes-recursively-in-c/983/2), I found solution. I used same approach (create vector for deleting nodes and iterate it to delete) and it is worked.

So what is question? The question is why this is worked? I do not understand the reason. Also, I wonder why node->Remove() not work proper for me?

I am not CS guy; thus, I lost sometimes :slight_smile:. Maybe this topic is not needed but I want to ask them.

Thanks in advance..

-------------------------

throwawayerino | 2020-01-15 00:09:01 UTC | #2

Did the node have any custom component children? Overriding `OnNodeSet` Or `OnSceneSet` without calling base function or checking nullptr will crash your program.
What do you have inside the nodes you're trying to remove?

-------------------------

restless | 2020-01-15 04:13:02 UTC | #3

[quote="MGokcayK, post:1, topic:5816"]
node->Remove() function but it is not worked
[/quote]

You shouldn't need to do anything else.

Looks like problem is somewhere else... Can you show the code?

If `node->Remove()` is called on the same `node` that you call `node->CreateComponent<StaticModel>()`, then it should work..

-------------------------

MGokcayK | 2020-01-15 11:37:51 UTC | #4

Thanks for answers, 

[quote="throwawayerino"]
What do you have inside the nodes you’re trying to remove?
[/quote]

I had an node that has sphere with static model. So, I don't have custom component.

[quote="restless"]
Can you show the code?
[/quote]

Yes, it is :

    #include "app.h"

    void gApp::Setup()
    {
    	engineParameters_[EP_FULL_SCREEN] = false;
    	engineParameters_[EP_WINDOW_RESIZABLE] = true;
    	engineParameters_[EP_WINDOW_WIDTH] = 1280;
    	engineParameters_[EP_WINDOW_HEIGHT] = 720;

    	InitGlobalHandleFunctions();
    }


    void gApp::InitGlobalHandleFunctions()
    {
    	SubscribeToEvent(E_KEYDOWN, URHO3D_HANDLER(gApp, KeyPressed));
    	SubscribeToEvent(E_UPDATE, URHO3D_HANDLER(gApp, UpdateFrame));
    }


    void gApp::Start()
    {
    	// create resource cache
    	ResourceCache* cache = GetSubsystem<ResourceCache>();

    	// create scene
    	scene_ = new Scene(context_);
    	scene_->CreateComponent<Octree>(); // create scene component

    	// create ground
    	Node* groundNode = scene_->CreateChild("Ground");
    	groundNode->SetPosition(Vector3(0, 0, 0));
    	groundNode->SetScale(Vector3(50, 3, 50));
    	StaticModel* groundObj = groundNode->CreateComponent<StaticModel>();
    	groundObj->SetModel(cache->GetResource<Model>("Models/Box.mdl"));

    	// create ui style
    	auto* uiStyle = cache->GetResource<XMLFile>("UI/DefaultStyle.xml"); // load window style from souce

    	uiRoot_ = GetSubsystem<UI>()->GetRoot();
    	uiRoot_->SetDefaultStyle(uiStyle);

    	// make window
    	window_ = new Window(context_);
    	window_->SetSize(300,400);
    	window_->SetLayout(LM_VERTICAL, 6, IntRect(6, 6, 6, 6));
    	window_->SetAlignment(HA_LEFT, VA_TOP);
    	window_->SetName("Window");

    	// make window title
    	auto* windowTitle = new Text(context_);
    	windowTitle->SetName("WindowTitle");
    	windowTitle->SetText("Debug Console!");

    	// make fps text
    	fpsText = new Text(context_);
    	fpsText->SetName("FpsText");

    	// make obj text
    	objText = new Text(context_);
    	objText->SetName("ObjText");

    	// edit window and its childs
    	window_->SetStyleAuto();
    	window_->AddChild(windowTitle);
    	window_->AddChild(fpsText);
    	window_->AddChild(objText);
    	windowTitle->SetStyleAuto();
    	fpsText->SetStyleAuto();
    	objText->SetStyleAuto();

    	// add window to ui
    	uiRoot_->AddChild(window_);


    	// We need a camera from which the viewport can render.
    	cameraNode_ = scene_->CreateChild("Camera");
    	cameraNode_->SetPosition(Vector3(0, 30, -50));
    	cameraNode_->Yaw(-0);
    	cameraNode_->Pitch(30);
    	Camera* camera = cameraNode_->CreateComponent<Camera>();
    	camera->SetFarClip(1000);

    	// Create a directional light (sun)
    	{
    		lightNode = scene_->CreateChild();
    		lightNode->SetDirection(Vector3::FORWARD);
    		lightNode->SetPosition(Vector3(0, 30, -30));
    		lightNode->Yaw(0);     // horizontal
    		lightNode->Pitch(20);   // vertical
    		lightDirection = 1;
    		Light* light = lightNode->CreateComponent<Light>();
    		light->SetLightType(LIGHT_POINT);
    		light->SetBrightness(1.6);
    		light->SetRange(150);
    		light->SetColor(Color(1.0, 1., 1., 1));
    		light->SetCastShadows(true);
    	}

    	// Now we setup the viewport. Of course, you can have more than one!
    	Renderer* renderer = GetSubsystem<Renderer>();
    	SharedPtr<Viewport> viewport(new Viewport(context_, scene_, cameraNode_->GetComponent<Camera>()));
    	renderer->SetViewport(0, viewport);
    }


    void gApp::Stop()
    {}


    void gApp::KeyPressed(StringHash eventType, VariantMap& eventData)
    {
    	using namespace KeyDown;
    	int key = eventData[P_KEY].GetInt();
    	if (key == KEY_ESCAPE)
    		engine_->Exit();

    	if (key == KEY_TAB)    // toggle mouse cursor when pressing tab
    	{
    		GetSubsystem<Input>()->SetMouseVisible(!GetSubsystem<Input>()->IsMouseVisible());
    	}
    }


    void gApp::UpdateFrame(StringHash eventType, VariantMap& eventData)
    {
    	float timeStep = eventData[Update::P_TIMESTEP].GetFloat();
    	framecount_++;
    	time_ += timeStep;
    	if (time_ > 0)
    	{
    		float diffFrame = framecount_ - oldframe_;
    		framecount_ = 0;
    		oldframe_ = framecount_;
    		// update debug console values
    		fpsText->SetText("FPS : " + String(diffFrame / timeStep) + " " + String(lightNode->GetPosition().x_));
    	}

    	// move light
    	if (lightNode->GetPosition().x_ < -10 || lightNode->GetPosition().x_ > +10)
    		lightDirection *= -1;
    	float locX = lightNode->GetPosition().x_ + timeStep*lightDirection;
    	lightNode->SetPosition(Vector3(locX , 20, 0));

    	// Movement speed as world units per second
    	float MOVE_SPEED = 10.0f;
    	// Mouse sensitivity as degrees per pixel
    	const float MOUSE_SENSITIVITY = 0.1f;

    	// Key Inputs
    	Input* input = GetSubsystem<Input>();
    	if (input->GetKeyDown(KEY_SHIFT))
    		MOVE_SPEED *= 10;
    	if (input->GetKeyDown(KEY_W))
    		cameraNode_->Translate(Vector3(0, 0, 1)*MOVE_SPEED*timeStep);
    	if (input->GetKeyDown(KEY_S))
    		cameraNode_->Translate(Vector3(0, 0, -1)*MOVE_SPEED*timeStep);
    	if (input->GetKeyDown(KEY_A))
    		cameraNode_->Translate(Vector3(-1, 0, 0)*MOVE_SPEED*timeStep);
    	if (input->GetKeyDown(KEY_D))
    		cameraNode_->Translate(Vector3(1, 0, 0)*MOVE_SPEED*timeStep);

    	if (input->GetMouseButtonDown(MOUSEB_LEFT))
    		SpawnObject();
    	if (input->GetMouseButtonDown(MOUSEB_RIGHT))
    	{
    		DeleteObject();
    	}

    	// Update POV with Mouse Movement
    	if (!GetSubsystem<Input>()->IsMouseVisible())
    	{
    		// Use this frame's mouse motion to adjust camera node yaw and pitch. Clamp the pitch between -90 and 90 degrees
    		IntVector2 mouseMove = input->GetMouseMove();
    		float yaw_ = cameraNode_->GetRotation().YawAngle();
    		float pitch_ = cameraNode_->GetRotation().PitchAngle();
    		yaw_ += MOUSE_SENSITIVITY*mouseMove.x_;
    		pitch_ += MOUSE_SENSITIVITY*mouseMove.y_;
    		pitch_ = Clamp(pitch_, -90.0f, 90.0f);
    		// Reset rotation and set yaw and pitch again
    		cameraNode_->SetDirection(Vector3::FORWARD);
    		cameraNode_->Yaw(yaw_);
    		cameraNode_->Pitch(pitch_);
    	}

    }


    void gApp::SpawnObject()
    {
    	// Spawn object when left mouse button clicked
    	ResourceCache* cache = GetSubsystem<ResourceCache>();
    	sphereNode_ = scene_->CreateChild("SmallBox");
    	sphereNode_->SetPosition(Vector3(0, 10, 0));
    	StaticModel *sphereObject = sphereNode_->CreateComponent<StaticModel>();
    	sphereObject->SetModel(cache->GetResource<Model>("Models/Sphere.mdl"));
    	sphereObject->SetMaterial(cache->GetResource<Material>("Materials/uvMat.xml"));
    	sphereObject->SetCastShadows(true);
    	objText->SetText("Object created!");
    	vWeakPtrDelete.Push(sphereNode_); // deleter vector store nodes which will be delete
    }

    void gApp::DeleteObject()
    {
    	// delete objects which stored deleter vector when right mouse button clicked
    	for (auto itr = vWeakPtrDelete.Begin(); itr != vWeakPtrDelete.End(); itr++)
    	{
    		WeakPtr<Node> node = *itr;

    		if (!node || !node->GetParent() || !node->GetScene())
    			continue;

    		node->Remove();

    		objText->SetText("Object removed!");
    	}
    	vWeakPtrDelete.Clear();
    }

This is my arranged code. As I said above actually it is removed but not from scene_. This version of code working but when I used sphereNode_->Remove() instead of DeleteObject() function error occured.

-------------------------

SirNate0 | 2020-01-15 17:31:54 UTC | #5

I suspect that your problem was that you didn't check if sphereNode_ was a valid pointer (i.e. `if (sphereNode_) sphereNode_->Remove();`), so the second time you called sphereNode_->Remove() the node had already been deleted.

-------------------------

MGokcayK | 2020-01-15 17:36:55 UTC | #6

Thank you for answer, 

I tried your suggestion. Unfortunately it is not work. :frowning:

-------------------------

Modanung | 2020-01-15 17:43:06 UTC | #7

Maybe try an `assert(sphereNode_);` for testing purposes, to make sure it's there?

Welcome to the forums, btw. :confetti_ball: :slightly_smiling_face:

-------------------------

MGokcayK | 2020-01-15 17:54:37 UTC | #8

Hi :slight_smile:, Thanks for answer, it is not worked :confused:.

-------------------------

MGokcayK | 2020-01-15 18:18:19 UTC | #9

Actually I found the problem, problem is when I spawn object, it create more than 1. For example, when I clicked left mouse button, It creates 5 sphere. When I called remove sphereNode_, it removes just one of them. 

I understand the problem during applying linear velocity :) . So, why it creates more than one sphere?

-------------------------

Dave82 | 2020-01-15 20:17:04 UTC | #10

[quote="MGokcayK, post:9, topic:5816"]
So, why it creates more than one sphere?
[/quote]

As i see you use GetMouseButtonDown for spawning objects. This function will return true constantly until you release the button so it might run 5 more frames until you release it. Use GetMouseButtonPress This function return true only once until you release the button and press again.

-------------------------

MGokcayK | 2020-01-15 18:38:50 UTC | #11

[quote="Dave82, post:10, topic:5816"]
GetMouseButtonPress
[/quote]

Thank you so much, I did not focus on that. To learn how it works, I dive on samples :D so i take some parts directly. Anyway this topic can be closed. Thank you everyone :)

-------------------------

