rogerdv | 2017-01-02 01:00:52 UTC | #1

I created a basic scene with the editor and now Im looking in the samples and doc how to load it in my project, but cant find the way. Can somebody explain me how to do it?

-------------------------

gunnar.kriik | 2017-01-02 01:00:52 UTC | #2

Say you save your scene as XML, then you can simply load it as follows (C++):

[code]
ResourceCache* cache = GetSubsystem<ResourceCache>();
scene_ = new Scene(GetContext());
scene_->LoadAsyncXML(cache->GetFile("Scenes/scene-001.xml"));
[/code]

You can also load from binary data in a similar fashion.

-------------------------

rogerdv | 2017-01-02 01:00:52 UTC | #3

Is there any other step required to display it? I load the scene, no errors in the log, but cant see anything, no matter where I place the camera.

-------------------------

gunnar.kriik | 2017-01-02 01:00:52 UTC | #4

I'm assuming you're basing your code off of some of the Urho samples, but do you have a light in your scene? You are also attaching a camera to the scene, right? such as:

[code]
cameraNode_ = scene_->CreateChild("Camera");
cameraNode_->CreateComponent<Camera>();
[/code]

-------------------------

rogerdv | 2017-01-02 01:00:52 UTC | #5

Yes, I have a directional light and Im creating the camera, first tried creating camera in editor, and then in the code (using the same coordinates I tested in the editor, except for the rotation). Neither way I can see the scene.

-------------------------

gunnar.kriik | 2017-01-02 01:00:52 UTC | #6

Hard to tell at this point, but I'm thinking that you might want to eliminate problems by using existing code that you know is working, and then trying to add your code there, e.g. use the StaticScene sample as template (as this is very basic to start with):
[github.com/urho3d/Urho3D/tree/m ... taticScene](https://github.com/urho3d/Urho3D/tree/master/Source/Samples/04_StaticScene)

-------------------------

att | 2017-01-02 01:00:52 UTC | #7

I load scene like this, it is a sync mode,
[code]
#if TEST_GAME_SCENE
    #if LOAD_XML_SCENES
        String sceneFileName("GameData/Scenes/sceneTest.xml");
    #else 
        String sceneFileName("GameData/Scenes/sceneTest.bin");
    #endif // LOAD_XML_SCENES
#else
    SceneMgr *mgr = GetSubsystem<SceneMgr>();
    String sceneFileName("GameData/Scenes/scene");
    #if LOAD_XML_SCENES
        sceneFileName.AppendWithFormat("%d.xml", mgr->GetLevelSelected());
    #else
        sceneFileName.AppendWithFormat("%d.bin", mgr->GetLevelSelected());
    #endif // LOAD_XML_SCENES
#endif // TEST_GAME_SCENE
    File scenedata(context_, GetSubsystem<FileSystem>()->GetProgramDir() + sceneFileName, FILE_READ);
    
#if LOAD_XML_SCENES
    SharedPtr<XMLFile> sceneFileXml(new XMLFile(context_));
    sceneFileXml->Load(scenedata);
    scene_ = new Scene(context_);
    scene_->LoadXML(sceneFileXml->GetRoot());
#else 
    scene_ = new Scene(context_);
    scene_->Load(scenedata);
#endif // LOAD_XML_SCENES[/code]

-------------------------

thebluefish | 2017-01-02 01:00:53 UTC | #8

Hi,

When creating the camera, you need to bind it to a Viewport to display anything.

Here's my code for setting up a MainMenu scene off an existing XML file:

[code]
	// Load the scene and script files
	_scene = new Urho3D::Scene(context_);
	Urho3D::SharedPtr<Urho3D::File> sceneFile = GetSubsystem<Urho3D::ResourceCache>()->GetFile("MainMenu.xml");
	_script = GetSubsystem<Urho3D::ResourceCache>()->GetResource<Urho3D::ScriptFile>("MainMenu.as");

	// Setup scene
	_scene->LoadXML(*sceneFile);
	_scene->SetName("MainMenu");

	Urho3D::Script* script = GetSubsystem<Urho3D::Script>();
	script->SetDefaultScene(_scene);
	script->SetDefaultScriptFile(_script);

	// Setup camera and viewport
	_cameraNode = new Urho3D::Node(context_);
    Urho3D::Camera* camera = _cameraNode->CreateComponent<Urho3D::Camera>();
    camera->SetFarClip(300.0f);
    
    // Set an initial position for the camera scene node above the floor
    _cameraNode->SetPosition(Urho3D::Vector3(0.0f, 3.0f, -20.0f));

	Urho3D::SharedPtr<Urho3D::Viewport> viewport(new Urho3D::Viewport(context_, _scene, _cameraNode->GetComponent<Urho3D::Camera>()));
    GetSubsystem<Urho3D::Renderer>()->SetViewport(0, viewport);
[/code]

This code loads a scene from XML as well as a default script file (To run the scene logic as a script). Then I create a camera node (Created outside of the scene so that it isn't deleted during network replication), setup a viewport to bind the scene and camera, then set this as the primary viewport.

For completeness, MainMenu.xml is actually just a re-named NinjaSnowWar.xml (From Data/Scenes) that can be changed out later. If you're interested to see how the script works, here is MainMenu.as:

[code]
UIElement@ buttonContainer;
Button@ startButton;
Button@ multiplayerButton;
Button@ characterButton;
Button@ settingsButton;
Button@ exitButton;

void Start()
{
    XMLFile@ uiStyle = cache.GetResource("XMLFile", "UI/DefaultStyle.xml");
    // Set style to the UI root so that elements will inherit it
    ui.root.defaultStyle = uiStyle;

    buttonContainer = ui.root.CreateChild("UIElement");
    buttonContainer.SetFixedSize(graphics.width, graphics.height);
    buttonContainer.SetPosition(0, 0);
    buttonContainer.layoutMode = LM_VERTICAL;

    startButton = CreateButton("Start");
    multiplayerButton = CreateButton("Multiplayer");
    characterButton = CreateButton("Character");
    settingsButton = CreateButton("Settings");
    exitButton = CreateButton("Exit");

    SubscribeToEvent(startButton, "Released", "HandleStart");
    SubscribeToEvent(multiplayerButton, "Released", "HandleMultiplayer");
    SubscribeToEvent(characterButton, "Released", "HandleCharacter");
    SubscribeToEvent(settingsButton, "Released", "HandleSettings");
    SubscribeToEvent(exitButton, "Released", "HandleExit");
}

Button@ CreateButton(const String& text)
{
    Font@ font = cache.GetResource("Font", "Fonts/Anonymous Pro.ttf");
    
    Button@ button = buttonContainer.CreateChild("Button");
    button.SetStyleAuto();
    button.SetFixedWidth(240);
    
    Text@ buttonText = button.CreateChild("Text");
    buttonText.SetFont(font, 24);
    buttonText.SetAlignment(HA_CENTER, VA_CENTER);
    buttonText.text = text;
    
    return button;
}

void HandleStart(StringHash eventType, VariantMap& eventData)
{   
    core.LoadMap("testlevel");
}

void HandleMultiplayer(StringHash eventType, VariantMap& eventData)
{   
    
}

void HandleCharacter(StringHash eventType, VariantMap& eventData)
{   

}

void HandleSettings(StringHash eventType, VariantMap& eventData)
{   

}

void HandleExit(StringHash eventType, VariantMap& eventData)
{   
    engine.Exit();
}
[/code]

However the script is completely optional.

-------------------------

rogerdv | 2017-01-02 01:00:55 UTC | #9

How can I adapt this to load the camera from the scene file? I think it is easier to locate and rotate the camera there.

-------------------------

