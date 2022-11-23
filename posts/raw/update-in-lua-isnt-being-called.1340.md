TheComet | 2017-01-02 01:06:58 UTC | #1

I've added a LuaScriptInstance to a node in my scene in the editor:
[img]http://i.imgur.com/9EsJHRw.png[/img]

The Lua script contains the following code:
[code]CharacterController = ScriptObject()

print("Hello!")

function CharacterController:Update(timeStep)
    print("Update")
end[/code]

Next, in my App, I make sure to create the LuaScript subsystem:
[code]void App::Setup()
{
	context_->RegisterSubsystem(new LuaScript(context_));
}[/code]

I load the scene with the following code:
[code]void App::CreateScene()
{
	ResourceCache* cache = GetSubsystem<ResourceCache>();

	scene_ = new Scene(context_);
	XMLFile* sceneXML = cache->GetResource<XMLFile>("Scenes/TestScene.xml");
	scene_->LoadXML(sceneXML->GetRoot());

	// set up camera
	cameraNode_ = scene_->CreateChild("Camera");
	auto camera = cameraNode_->CreateComponent<Camera>();
	camera->SetFarClip(300.0f);
	cameraNode_->SetPosition(Vector3(0.0f, 5.0f, -20.0f));
}[/code]

When I compile and run my Application, I see the output "Hello!" but I never see "Update".
[code][Sun Sep  6 14:48:15 2015] INFO: Opened log file Urho3D.log
[Sun Sep  6 14:48:15 2015] INFO: Created 1 worker thread
[Sun Sep  6 14:48:15 2015] INFO: Added resource path /home/thecomet/documents/programming/cpp/primal-equestria/bin/Data/
[Sun Sep  6 14:48:15 2015] INFO: Added resource path /home/thecomet/documents/programming/cpp/primal-equestria/bin/CoreData/
[Sun Sep  6 14:48:15 2015] INFO: Set screen mode 1024x768 windowed
[Sun Sep  6 14:48:15 2015] INFO: Initialized input
[Sun Sep  6 14:48:15 2015] INFO: Initialized user interface
[Sun Sep  6 14:48:15 2015] INFO: Initialized renderer
[Sun Sep  6 14:48:15 2015] INFO: Set audio mode 44100 Hz stereo interpolated
[Sun Sep  6 14:48:15 2015] INFO: Initialized engine
[Sun Sep  6 14:48:15 2015] INFO: Loaded Lua script Scripts/CharacterController.lua
Hello!
[Sun Sep  6 14:48:15 2015] INFO: Executed Lua script Scripts/CharacterController.lua
*** Exited normally ***[/code]

What's going on? Why isn't Update() being called? I tried some other built in methods like Start() or FixedUpdate() but they're also never called...

-------------------------

aster2013 | 2017-01-02 01:06:58 UTC | #2

Hi, Welcome to our forum.

Do you have press the RunUpdatePlay button in editor?

-------------------------

TheComet | 2017-01-02 01:06:58 UTC | #3

[quote="aster2013"]Hi, Welcome to our forum.

Do you have press the RunUpdatePlay button in editor?[/quote]

I tried saving the scene with both pause and run pressed. It has no effect.

-------------------------

TheComet | 2017-01-02 01:06:58 UTC | #4

Update: I tried loading the lua script in C++ and seeing if it would run. Same problem:
[code]	ResourceCache* cache = GetSubsystem<ResourceCache>();

	scene_ = SharedPtr<Scene>(new Scene(context_));

	Node* playerNode = scene_->CreateChild("Player");
	LuaScriptInstance* luaScriptInstance = playerNode->CreateComponent<LuaScriptInstance>();
	LuaFile* characterControllerFile = cache->GetResource<LuaFile>("Scripts/CharacterController.lua");
	luaScriptInstance->CreateObject(characterControllerFile, "CharacterController");
[/code]

-------------------------

TheComet | 2017-01-02 01:06:58 UTC | #5

Figured it. I wasn't supplying the script object type in the editor:
[img]http://i.imgur.com/fgwtlRC.png[/img]

I'm pretty sure that's what I was doing with [i]luaScriptInstance->CreateObject(characterControllerFile, "CharacterController");[/i] but now it works for some reason.

-------------------------

