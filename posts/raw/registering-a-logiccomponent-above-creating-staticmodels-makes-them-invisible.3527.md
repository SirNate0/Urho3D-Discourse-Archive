ppsychrite | 2017-09-04 02:13:29 UTC | #1

Hello!

For seem reason when I use context's "RegisterFactory" function on a LogicComponent above creating a scene it flat-out makes StaticModels disappear.

Here's what it looks like when I don't register the component: http://prntscr.com/ggox61 (This is what it's supposed to look like)

The result of putting RegisterFactory() above everything makes it a black screen.
Here's my CreateScene() function with where I've tried putting it 

    void PlayingState::CreateScene() {
		//context_->RegisterFactory<brk::PlayerCamera>();

		// <-- Placing registerfactory here is black screen

		ur::ResourceCache *cache = GetSubsystem<ur::ResourceCache>();

		// <-- Placing registerfactory here is black screen

		ur::Node *boxNode = scene->CreateChild();
		ur::StaticModel *model = boxNode->CreateComponent<ur::StaticModel>();
		model->SetModel(cache->GetResource<ur::Model>("Models/Plane.mdl"));
		boxNode->SetScale({ 100.0f, 1.0f, 100.0f });
	
		// <-- Placing registerfactory here is black screen

		ur::Node *cameraNode = scene->CreateChild();
		cameraNode->CreateComponent<ur::Camera>();
		cameraNode->SetPosition({ 0.0f, 10.0f, 0.0f });
	
		// <-- Placing registerfactory here works fine

		Renderer* renderer = GetSubsystem<Renderer>();
		renderer->SetViewport(0, new Viewport(context_, scene, cameraNode->GetComponent<ur::Camera>()));
		
		// <-- Placing registerfactory here works fine
		
	}


Here's the LogicComponent "PlayerCamera", even with it blank it still gives a black screen.

    constexpr float MOVE_SPEED = 20.0f;
	constexpr float MOUSE_SENSITIVITY = 0.1f;

	class PlayerCamera : public ur::LogicComponent {
		URHO3D_OBJECT(Camera, LogicComponent)
		public:
			PlayerCamera(ur::Context *context);
			virtual void Start();
			virtual void Update(float deltaTime);
			
		private:
			float yaw, pitch;
	};

Source:
    
    PlayerCamera::PlayerCamera(ur::Context *context) : ur::LogicComponent(context) {
	
	}

	void PlayerCamera::Start() {
		yaw = pitch = 0.0f;
	
	}

	void PlayerCamera::Update(float deltaTime) {
		ur::Input *input = GetSubsystem<ur::Input>();

		if (!input->HasFocus()) return;
		
		ur::IntVector2 mouseMove = input->GetMouseMove();
		yaw += MOUSE_SENSITIVITY * mouseMove.x_;
		pitch += MOUSE_SENSITIVITY * mouseMove.y_;
		pitch = ur::Clamp(pitch, -85.0f, 85.0f);

		node_->SetRotation(ur::Quaternion(pitch, yaw, 0.0f));

		if (input->GetKeyDown(ur::KEY_W)) node_->Translate(ur::Vector3::FORWARD * MOVE_SPEED * deltaTime);
		else if (input->GetKeyDown(ur::KEY_S)) node_->Translate(ur::Vector3::FORWARD * MOVE_SPEED * deltaTime);
	}
     


Any clues? :confused: I don't know how registering a factory is related to breaking a StaticModel

-------------------------

ppsychrite | 2017-09-04 02:13:20 UTC | #2

Holy cow I didn't notice the

    URHO3D_OBJECT(Camera, LogicComponent)

Mistake, I'm stupid. :man_facepalming: 

Sorry for wasting anyone's time

-------------------------

