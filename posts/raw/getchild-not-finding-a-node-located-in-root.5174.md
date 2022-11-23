throwawayerino | 2019-05-22 15:53:36 UTC | #1

In main.cpp i have
`Node* ConeNode = GetScene()->CreateChild("ConeMan")`
And it creates a Node, correctly named node. But when I try to do `GetScene()->GetChild("ConeMan")` in the `Start()` of a component it instead returns null and crashed later when I try to access the nonexistent node. 
Instead of trying to search for it I simply passed a reference to the component and it didn't crash, so the problem definitely isn't with creation
Why isn't it finding my correctly named node?

-------------------------

Modanung | 2019-05-22 16:00:13 UTC | #2

Are you sure you're looking at the same `Scene`?

-------------------------

throwawayerino | 2019-05-22 16:04:07 UTC | #3

The component calling the `GetChild()` is attached to and controls the camera, and I can see the cone in the world, so I'm sure it's the correct scene. I'm using the 1.7 release, so maybe it's an old bug fixed in master?

-------------------------

Modanung | 2019-05-22 16:08:34 UTC | #4

[quote="throwawayerino, post:3, topic:5174"]
I’m using the 1.7 release, so maybe it’s an old bug fixed in master?
[/quote]

Unlikely, although it would be wiser to use the latest master branch.
Could you share some more code?

-------------------------

throwawayerino | 2019-05-22 16:23:36 UTC | #5

Creating/Loading scene
 `MainScene = new Scene(GetContext());
MainScene->LoadXML(Cache->GetResource<XMLFile>("Scenes/Help.xml")->GetRoot());`

Start() of Component

    void CameraComponent::Start() {
	SubscribeToEvent(E_UPDATE, URHO3D_HANDLER(CameraComponent, HandleUpdate));

	MainNode = GetNode();
	MainCamera = MainNode->GetComponent<Camera>();
	//ConeMan = GetScene()->GetChild("ConeMan"); <--- problem here
    }


Making the cone and component
Functions in a static class:

    Node* Creators::MakeCamera(Scene* MainScene, Node* ConeMan) {
	Node* CameraNode = MainScene->CreateChild("CameraNode");
	Camera* MainCamera = CameraNode->CreateComponent<Camera>();
	MainCamera->SetFarClip(2000.f);
	//CameraNode->CreateComponent<CameraComponent>();
    // Fix for GetChild()
	CameraComponent* CamComp = (CameraComponent*)CameraNode->CreateComponent(CameraComponent::GetTypeStatic());
	CamComp->ConeMan = ConeMan;
	CameraNode->AddComponent(CamComp, 0U, Urho3D::REPLICATED);
	
	return CameraNode;
    };
.

    Node* Creators::MakeCone(Scene * MainScene, Vector3 Position, Quaternion Rotation) {
	ResourceCache* Cache = MainScene->GetSubsystem<ResourceCache>();

	Node* ConeNode = MainScene->CreateChild("ConeMan");
	ConeNode->SetPosition(Position);
	ConeNode->SetRotation(Rotation);

	StaticModel* ConeModel = ConeNode->CreateComponent<StaticModel>();
	ConeModel->SetModel(Cache->GetResource<Model>("Models/Cone.mdl"));
	ConeModel->SetMaterial(Cache->GetResource<Material>("Materials/StoneTiled.xml"));
	ConeModel->SetCastShadows(true);

	return ConeNode;
    }

Code called in main.cpp

    ConeNode = Creators::MakeCone(MainScene, Vector3(0.f, 1.f, 0.f));
    CameraNode = Creators::MakeCamera(MainScene, ConeNode);

As you can see the scenes passed when making the nodes are the same, so I'm sure it's a bug. I'll move to master and see

-------------------------

Modanung | 2019-05-23 01:50:39 UTC | #6

I think I located the problem: `Start` is called after creation of the component, but *before it is assigned to a node*. No node; no scene.
Try changing `CameraComponent::Start()` to `CameraComponent::OnNodeSet(Node* node)`.

Btw, if you have your `Creators` inherit from `Object` it can `GetSubsystem`s too and even be registered as a subsystem itself.

-------------------------

throwawayerino | 2019-05-23 01:50:46 UTC | #7

Thanks for the reply!

-------------------------

throwawayerino | 2019-05-23 12:57:19 UTC | #8

One last note: I instead chose `OnSceneSet(Scene* scene)`, because when it's called it directly gives me the scene, removing the need for a `GetScene()` call. But if I simply override it, the program will crash when exiting/cleaning up, because it's called during cleanup to set the scene as `nullptr`. Here's the completely working code:

	virtual void OnSceneSet(Scene* scene) override;
---
    void CameraComponent::OnSceneSet(Scene* scene) {
    	if(scene != nullptr)
    		ConeMan = scene->GetChild("ConeMan");
    }

-------------------------

Leith | 2019-05-23 13:29:59 UTC | #9

I use DelayedStart, this one fires after reloads are complete, after everything is essentially ready in the scene, to do late initializing

-------------------------

Modanung | 2019-05-23 16:18:44 UTC | #10

[quote="throwawayerino, post:8, topic:5174"]
`if(scene != nullptr)`
[/quote]
I personally prefer `if (!scene) return;` but indeed safety nets like that are required.

-------------------------

