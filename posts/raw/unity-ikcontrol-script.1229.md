Mike | 2017-01-02 01:06:12 UTC | #1

I've tried to port a Unity script found [url=https://github.com/sam-kelly-dev/ovr-pilot/tree/master/Assets/IK/Scripts/ik]here[/url]. 
Demo [url=https://www.youtube.com/watch?v=FXVtBKVtXjM]here[/url].
It roughly works as expected but not perfect. As I'm totally unfamiliar with Unity I may have missed something or made wrong assumptions.

If someone familiar with Unity could check would be great.

[spoiler][code]
#include "Scripts/Utilities/Sample.as"
#include "Scripts/IKControl.as"

// IK stuff
Node@ upperArmL;
Node@ upperArmR;


float MOVE_SPEED = 1.0f; // Movement speed as world units per second
float MOUSE_SENSITIVITY = 0.1f; // Mouse sensitivity as degrees per pixel

String character = "Jack";


void Start()
{
	SampleStart();
	CreateScene();
	CreateUI();
	SubscribeToEvents();
}


void CreateScene()
{
	// SCENE ROOT
	scene_ = Scene();
	scene_.CreateComponent("Octree");
	scene_.CreateComponent("PhysicsWorld");
	scene_.CreateComponent("DebugRenderer");

	// FLOOR
	Node@ floorNode = scene_.CreateChild("Plane");
	floorNode.position = Vector3(0.0f, -0.5f, 0.0f);
	floorNode.scale = Vector3(100.0f, 1.0f, 100.0f);
	StaticModel@ planeObject = floorNode.CreateComponent("StaticModel");
	planeObject.model = cache.GetResource("Model", "Models/Box.mdl");
	planeObject.material = cache.GetResource("Material", "Materials/StoneTiled.xml");
	RigidBody@ body = floorNode.CreateComponent("RigidBody");
	CollisionShape@ shape = floorNode.CreateComponent("CollisionShape");
	shape.SetBox(Vector3(1.0f, 1.0f, 1.0f));

	// ZONE
	Node@ zoneNode = scene_.CreateChild("Zone");
	Zone@ zone = zoneNode.CreateComponent("Zone");
	zone.boundingBox = BoundingBox(-1000.0f, 1000.0f);
	zone.ambientColor = Color(0.15f, 0.15f, 0.15f);
	zone.fogColor = Color(0.5f, 0.5f, 0.7f);
	zone.fogStart = 100.0f;
	zone.fogEnd = 300.0f;

	// LIGHT
	Node@ lightNode = scene_.CreateChild("DirectionalLight");
	lightNode.direction = Vector3(0.6f, -1.0f, -0.8f);
	Light@ light = lightNode.CreateComponent("Light");
	light.lightType = LIGHT_DIRECTIONAL;
	light.castShadows = true;
	light.shadowBias = BiasParameters(0.00025f, 0.5f);
	// Set cascade splits at 10, 50 and 200 world units, fade shadows out at 80% of maximum shadow distance
	light.shadowCascade = CascadeParameters(10.0f, 50.0f, 200.0f, 0.0f, 0.8f);

	// CAMERA
	cameraNode = scene_.CreateChild("Camera");
	Camera@ camera = cameraNode.CreateComponent("Camera");
	camera.farClip = 300.0f;
	cameraNode.position = Vector3(0.0f, 1.2f, 3.5f);
	cameraNode.rotation = Quaternion(0.0f, 180.0f, 0.0f);

	// VIEWPORT
	Viewport@ viewport = Viewport(scene_, camera);
	renderer.viewports[0] = viewport;

	// BALLS (target position to reach)
	Node@ ball = scene_.CreateChild("Ball");
	ball.SetScale(0.1f);
	ball.position = Vector3(-0.5f, 1.5f, 0.25f);
	StaticModel@ ballModel = ball.CreateComponent("StaticModel");
	ballModel.model = cache.GetResource("Model", "Models/Sphere.mdl");

	Node@ ball2 = ball.Clone();
	ball2.name = "Ball2";
	ball2.position = Vector3(0.5f, 1.5f, 0.5f);

	// CHARACTER & IK CHAINS
	if (character == "Jack")
	{
		Node@ modelNode = scene_.CreateChild("Character");
		AnimatedModel@ modelObject = modelNode.CreateComponent("AnimatedModel");
		modelNode.CreateComponent("AnimationController"); // Create the animation controller

		modelObject.model = cache.GetResource("Model", "Models/Jack.mdl");
		modelObject.material = cache.GetResource("Material", "Materials/Jack.xml");
		upperArmL = modelNode.GetChild("Bip01_L_UpperArm", true);
		upperArmR = modelNode.GetChild("Bip01_R_UpperArm", true);

		// Take manual control of the arms' bones
		Skeleton@ skel = modelObject.skeleton;
		skel.GetBone("Bip01_L_UpperArm").animated = false;
		skel.GetBone("Bip01_L_Forearm").animated = false;
		skel.GetBone("Bip01_L_Hand").animated = false;
		skel.GetBone("Bip01_R_UpperArm").animated = false;
		skel.GetBone("Bip01_R_Forearm").animated = false;
		skel.GetBone("Bip01_R_Hand").animated = false;

		// Create the IK controllers at the top of the IK chains
		IKControl@ ikLeft = cast<IKControl>(upperArmL.CreateScriptObject(scriptFile, "IKControl"));
		ikLeft.armAxis = Vector3(0.0f, -1.0f, 0.0f);
		ikLeft.target = ball;

		IKControl@ ikRight = cast<IKControl>(upperArmR.CreateScriptObject(scriptFile, "IKControl"));
		ikRight.armAxis = Vector3(0.0f, 1.0f, 0.0f);
		ikRight.target = ball2;
	}
	else
	{
		Node@ modelNode = scene_.InstantiateXML(cache.GetFile("Assets/" + character + "/Objects/" + character + ".xml"), Vector3(0.0f, 0.5f, 0.0f), Quaternion(0.0f, 0.0f, 0.0f));
		modelNode.name = "Character";
		modelNode.SetScale(0.9f);
		AnimatedModel@ modelObject = modelNode.GetComponent("AnimatedModel");
		modelNode.CreateComponent("AnimationController"); // Create the animation controller

		upperArmL = modelNode.GetChild("UpperArm.L", true);
		upperArmR = modelNode.GetChild("UpperArm.R", true);

		// Take manual control of the arms' bones
//		Skeleton@ skel = modelObject.skeleton;
//		skel.GetBone("UpperArm.L").animated = false;
//		skel.GetBone("Forearm.L").animated = false;
//		skel.GetBone("Hand.L").animated = false;
//		skel.GetBone("UpperArm.R").animated = false;
//		skel.GetBone("Forearm.R").animated = false;
//		skel.GetBone("Hand.R").animated = false;

		// Create the IK controllers at the top of the IK chains
		IKControl@ ikLeft = cast<IKControl>(upperArmL.CreateScriptObject(scriptFile, "IKControl"));
		ikLeft.armAxis = Vector3(0.0f, -1.0f, 0.0f);
		ikLeft.target = ball;

		IKControl@ ikRight = cast<IKControl>(upperArmR.CreateScriptObject(scriptFile, "IKControl"));
		ikRight.armAxis = Vector3(0.0f, 1.0f, 0.0f);
		ikRight.target = ball2;
	}
}


void CreateUI()
{
	// Create a Cursor UI element because we want to be able to hide and show it at will. When hidden, the mouse cursor will
	// control the camera, and when visible, it will point the raycast target
	Cursor@ cursor = Cursor();
	cursor.SetStyleAuto(cache.GetResource("XMLFile", "UI/DefaultStyle.xml"));
	ui.cursor = cursor;
	// Set starting position of the cursor at the rendering window center
	cursor.SetPosition(graphics.width / 2, graphics.height / 2);

	// Construct new Text object, set string to display and font to use
	Text@ instructionText = ui.root.CreateChild("Text");
	instructionText.text = "Use directional keys & mouse wheel to move the targets\n" "RMB to rotate around the character\n" "F5 to save scene, F7 to load\n" "Space to toggle debug geometry";
	instructionText.SetFont(cache.GetResource("Font", "Fonts/Anonymous Pro.ttf"), 15);
	instructionText.textAlignment = HA_CENTER;

	// Position the text relative to the screen center
	instructionText.horizontalAlignment = HA_CENTER;
	instructionText.verticalAlignment = VA_CENTER;
	instructionText.SetPosition(0, ui.root.height / 4);
}


void SubscribeToEvents()
{
	SubscribeToEvent("Update", "HandleUpdate");
	SubscribeToEvent("PostRenderUpdate", "HandlePostRenderUpdate");
}


void MoveCamera(float timeStep)
{
	// Right mouse button controls mouse cursor visibility: hide when pressed
	ui.cursor.visible = !input.mouseButtonDown[MOUSEB_RIGHT];

	// Do not move if the UI has a focused element (the console)
	if (ui.focusElement !is null)
		return;

	// Rotate camera around model when the cursor is hidden (ie when right mouse click)
	if (!ui.cursor.visible)
	{
		yaw = yaw + MOUSE_SENSITIVITY * input.mouseMove.x;
		cameraNode.RotateAround(scene_.GetChild("Character", true).position, Quaternion(0.0f, yaw * 0.1, 0.0f), TS_WORLD);
	}

	// Save the scene
	if (input.keyPress[KEY_F5])
	{
		File saveFile(fileSystem.programDir + "Data/Scenes/IKControlDemo.xml", FILE_WRITE);
		scene_.SaveXML(saveFile);
	}

	// Load the scene
    if (input.keyPress[KEY_F7])
    {
        File loadFile(fileSystem.programDir + "Data/Scenes/IKControlDemo.xml", FILE_READ);
        scene_.LoadXML(loadFile);
    }

	// Toggle debug geometry with space
	if (input.keyPress[KEY_SPACE])
		drawDebug = !drawDebug;
}


void MoveTarget(float timeStep)
{
	// Read directional keys and move the target to the corresponding direction if they are pressed
	Node@ targetBall = scene_.GetChild("Ball", true);
	Node@ targetBall2 = scene_.GetChild("Ball2", true);
	Vector3 move = Vector3(0.0f, 0.0f, 0.0f);
	if (input.keyDown[KEY_UP]) move += Vector3(0.0f, 1.0f, 0.0f);
	if (input.keyDown[KEY_DOWN]) move += Vector3(0.0f, -1.0f, 0.0f);
	if (input.keyDown[KEY_LEFT]) move += Vector3(1.0f, 0.0f, 0.0f);
	if (input.keyDown[KEY_RIGHT]) move += Vector3(-1.0f, 0.0f, 0.0f);

	// Move target in the Z-axis using mouse wheel
	if (input.mouseMoveWheel != 0) move += Vector3(0.0f, 0.0f, -input.mouseMoveWheel * 2.0f);

	if (!move.Equals(Vector3(0.0f, 0.0f, 0.0f)))
	{
		targetBall.Translate(move * MOVE_SPEED * timeStep);
		targetBall2.position = targetBall.position * Vector3(-1.0f, 1.0f, 1.0f);
	}
}


void HandleUpdate(StringHash eventType, VariantMap& eventData)
{
	float timeStep = eventData["TimeStep"].GetFloat();

	MoveCamera(timeStep);
	MoveTarget(timeStep);

	// Drag IK effector with left mouse button click
	float DRAG_SENSITIVITY = 0.01f;

	// Play animation
	AnimationController@ animCtrl = scene_.GetChild("Character", true).GetComponent("AnimationController");
	if (character == "Jack")
		animCtrl.PlayExclusive("Models/Jack_Walk.ani", 0, true, 0.2);
//	else
//		animCtrl.PlayExclusive("Assets/" + character + "/Models/Run.ani", 0, true, 0.2);
}


void HandlePostRenderUpdate(StringHash eventType, VariantMap& eventData)
{
	if (drawDebug) renderer.DrawDebugGeometry(false);
}


// Create XML patch instructions for screen joystick layout specific to this sample app
String patchInstructions = "";
[/code][/spoiler]

[spoiler][code]
// Script Object is parented to forearm
// node
//	  > armIK
//			  > armRotation

class IKControl : ScriptObject
{

	Node@ forearm; //var forearm : Transform;
	Node@ hand; //var hand : Transform;
	Node@ target; // var target : Transform;
	Vector3 armAxis; // Arm rotation axis. Depends on the way the skeleton has been authored.
	bool slerp = false;

//  float transition = 1.0;
	float elbowAngle = 0.0; // ?????

	Node@ armIK; //private var armIK : Transform;
	Node@ armRotation; //private var armRotation : Transform;

	float upperArmLength;
	float forearmLength;
	float armLength;


void Start()
{
	forearm = node.children[0];
	if (forearm is null)
		return;
	hand = forearm.children[0];
	if (hand is null)
		return;

//  var armIKGameObject = new GameObject("Arm IK");
	armIK = scene.CreateChild("ArmIK"); //armIK = armIKGameObject.transform;
	armIK.parent = node; // Parent to shoulder joint (UpperArm)
//  var armRotationGameObject = new GameObject("Arm Rotation");
	armRotation = scene.CreateChild("ArmRotation"); //armRotation = armRotationGameObject.transform;
	armRotation.parent = armIK;
	upperArmLength = (forearm.worldPosition - node.worldPosition).length; //Vector3.Distance(transform.position, forearm.position);
	forearmLength = (hand.worldPosition - forearm.worldPosition).length; //Vector3.Distance(forearm.position, hand.position);
	armLength = upperArmLength + forearmLength;

	// Subscribe to the SceneDrawableUpdateFinished event which is triggered after the animations have been updated, so we can apply IK to override them
	SubscribeToEvent("SceneDrawableUpdateFinished", "HandleSceneDrawableUpdateFinished");
}


void HandleSceneDrawableUpdateFinished(StringHash eventType, VariantMap& eventData) //function LateUpdate()
{
	if (target is null || forearm is null || hand is null || armAxis.IsNaN())
		return;

	// Store rotation before IK
	Quaternion storeUpperArmRotation = node.worldRotation;
	Quaternion storeForearmRotation = forearm.worldRotation;

	// Upper Arm (node) looks target
	armIK.worldPosition = node.worldPosition;
	armIK.LookAt(forearm.worldPosition);
	armRotation.worldPosition = node.worldPosition;
	armRotation.worldRotation = node.worldRotation;
	armIK.LookAt(target.position);
	node.worldRotation = armRotation.worldRotation;

	// Upper Arm IK angle
	float targetDistance = (target.position - node.worldPosition).length; //Vector3.Distance(transform.position, target.position);
	targetDistance = Min(targetDistance, armLength - 0.00001); //Mathf.Min(targetDistance, armLength - 0.00001);
	float adjacent = ((upperArmLength * upperArmLength) - (forearmLength * forearmLength) + (targetDistance * targetDistance)) / (2 * targetDistance);
	float angle = Acos(adjacent / upperArmLength); //Mathf.Acos(adjacent / upperArmLength) * Mathf.Rad2Deg;
	node.RotateAround(node.worldPosition, Quaternion(angle, armAxis), TS_WORLD); //node.RotateAround(transform.position, transform.forward, -angle);

	// Forearm looks target
	armIK.worldPosition = forearm.worldPosition;
	armIK.LookAt(hand.worldPosition);
	armRotation.worldPosition = forearm.worldPosition;
	armRotation.worldRotation = forearm.worldRotation;
	armIK.LookAt(target.position);
	forearm.worldRotation = armRotation.worldRotation;

	// Elbow angle
	node.RotateAround(node.worldPosition, Quaternion(elbowAngle, target.position - node.worldPosition), TS_WORLD); //node.RotateAround(node.position, target.position - node.position, elbowAngle);

	// Transition IK rotations with animation rotation.
	if (slerp)
	{
		float transition = eventData["TimeStep"].GetFloat() * 8; //Mathf.Clamp01(transition);
		node.worldRotation = storeUpperArmRotation.Slerp(node.worldRotation, transition); //Quaternion.Slerp(storeUpperArmRotation, node.rotation, transition);
		forearm.worldRotation = storeForearmRotation.Slerp(forearm.worldRotation, transition); //Quaternion.Slerp(storeForearmRotation, forearm.rotation, transition);
	}
}

}
[/code][/spoiler]

-------------------------

1vanK | 2017-01-02 01:06:12 UTC | #2

In video i see pole target (it specify the direction of the elbow), but in this example it missing

EDIT: Pole target in blender [youtube.com/watch?v=4C1ssz8qCq0&t=242](https://www.youtube.com/watch?v=4C1ssz8qCq0&t=242)

-------------------------

Mike | 2017-01-02 01:06:13 UTC | #3

Thanks, IKControl.js is certainly incomplete, will check the other script. Pole target aside, some rotation resets are certainly missing.

EDIT: [color=#FF0000]resetting rotations greatly improves the behavior[/color]

-------------------------

1vanK | 2017-01-02 01:06:13 UTC | #4

Modified version:

[code]    // Script Object is parented to forearm
    // node
    //     > armIK
    //           > armRotation

    class IKControl : ScriptObject
    {

       Node@ forearm; //var forearm : Transform;
       Node@ hand; //var hand : Transform;
       Node@ target; // var target : Transform;
       Vector3 armAxis; // Arm rotation axis. Depends on the way the skeleton has been authored.
       bool slerp = false;

    //  float transition = 1.0;
       float elbowAngle = 0.0; // ?????

       Node@ armIK; //private var armIK : Transform;
       Node@ armRotation; //private var armRotation : Transform;

       float upperArmLength;
       float forearmLength;
       float armLength;
       
       Quaternion storeUpperArmRotation;
       Quaternion storeForearmRotation;


    void Start()
    {
       forearm = node.children[0];
       if (forearm is null)
          return;
       hand = forearm.children[0];
       if (hand is null)
          return;

       storeUpperArmRotation = node.worldRotation;
       storeForearmRotation = forearm.worldRotation;

    //  var armIKGameObject = new GameObject("Arm IK");
       armIK = scene.CreateChild("ArmIK"); //armIK = armIKGameObject.transform;
       armIK.parent = node; // Parent to shoulder joint (UpperArm)
    //  var armRotationGameObject = new GameObject("Arm Rotation");
       armRotation = scene.CreateChild("ArmRotation"); //armRotation = armRotationGameObject.transform;
       armRotation.parent = armIK;
       upperArmLength = (forearm.worldPosition - node.worldPosition).length; //Vector3.Distance(transform.position, forearm.position);
       forearmLength = (hand.worldPosition - forearm.worldPosition).length; //Vector3.Distance(forearm.position, hand.position);
       armLength = upperArmLength + forearmLength;

       // Subscribe to the SceneDrawableUpdateFinished event which is triggered after the animations have been updated, so we can apply IK to override them
       SubscribeToEvent("SceneDrawableUpdateFinished", "HandleSceneDrawableUpdateFinished");
    }


    void HandleSceneDrawableUpdateFinished(StringHash eventType, VariantMap& eventData) //function LateUpdate()
    {
       if (target is null || forearm is null || hand is null || armAxis.IsNaN())
          return;

    	// Store rotation before IK
    	node.worldRotation = storeUpperArmRotation;
		forearm.worldRotation = storeForearmRotation;
	
       // Upper Arm (node) looks target
       armIK.worldPosition = node.worldPosition;
       armIK.LookAt(forearm.worldPosition);
       armRotation.worldPosition = node.worldPosition;
       armRotation.worldRotation = node.worldRotation;
       armIK.LookAt(target.position);
       node.worldRotation = armRotation.worldRotation;

       // Upper Arm IK angle
       float targetDistance = (target.position - node.worldPosition).length; //Vector3.Distance(transform.position, target.position);
       targetDistance = Min(targetDistance, armLength - 0.00001); //Mathf.Min(targetDistance, armLength - 0.00001);
       float adjacent = ((upperArmLength * upperArmLength) - (forearmLength * forearmLength) + (targetDistance * targetDistance)) / (2 * targetDistance);
       float angle = Acos(adjacent / upperArmLength); //Mathf.Acos(adjacent / upperArmLength) * Mathf.Rad2Deg;
       node.RotateAround(node.worldPosition, Quaternion(angle, armAxis), TS_WORLD); //node.RotateAround(transform.position, transform.forward, -angle);

       // Forearm looks target
       armIK.worldPosition = forearm.worldPosition;
       armIK.LookAt(hand.worldPosition);
       armRotation.worldPosition = forearm.worldPosition;
       armRotation.worldRotation = forearm.worldRotation;
       armIK.LookAt(target.position);
       forearm.worldRotation = armRotation.worldRotation;

       // Elbow angle
       if (armAxis == Vector3(0.0f, -1.0f, 0.0f))
            elbowAngle = 90;
       else
            elbowAngle = -90;
       
       node.RotateAround(node.worldPosition, Quaternion(elbowAngle, target.position - node.worldPosition), TS_WORLD); //node.RotateAround(node.position, target.position - node.position, elbowAngle);

       // Transition IK rotations with animation rotation.
       if (slerp)
       {
          float transition = eventData["TimeStep"].GetFloat() * 8; //Mathf.Clamp01(transition);
          node.worldRotation = storeUpperArmRotation.Slerp(node.worldRotation, transition); //Quaternion.Slerp(storeUpperArmRotation, node.rotation, transition);
          forearm.worldRotation = storeForearmRotation.Slerp(forearm.worldRotation, transition); //Quaternion.Slerp(storeForearmRotation, forearm.rotation, transition);
       }
    }

    }
[/code]

Really resetting rotations solves the problem. I think, i found cause.
node.RotateAround add angle to current rotation every frame rather than to set a new computed angle.
Therefore, if you set elbowAngle != 0 hand starts to rotate instead of elbow was directed in the right direction

-------------------------

Mike | 2017-01-02 01:06:13 UTC | #5

Thanks 1vanK, that is the solution that I also came up with.:wink: 
I'll also incorporate other interesting optimizations/features from the other script so we can easily do procedural animations.

-------------------------

franck22000 | 2017-01-02 01:06:17 UTC | #6

Hello Mike thanks for working on this ! 

Are you planning to release a c++ version of your code ?

-------------------------

Mike | 2017-01-02 01:06:17 UTC | #7

For now I'm looking at a global approach for procedural animation, in the vein of Overgrowth. Seems that it is way simpler thant I expected.
I'm thinking of using an IK/FK manager component that handles and gives access to 4 limb components (2 arms & 2 legs), rotates the spine and allows feet to be either grounded or reach a target.

In Urho3D porting AngelScript and Lua scripts to C++ is straightforward. Once the project will reach maturity it will be time to port.

-------------------------

namic | 2017-01-02 01:12:21 UTC | #8

That's amazing! Thanks for the code, it's really useful and covers missing docs on the subject. Did you had any progress with your Overgrowth-style animation? I've created a topic about this here: [topic2117.html](http://discourse.urho3d.io/t/ue4-style-ik/2021/1)

-------------------------

Mike | 2017-01-02 01:12:23 UTC | #9

Overall it wasn't perfect and after trying various fixes I gave up.

-------------------------

