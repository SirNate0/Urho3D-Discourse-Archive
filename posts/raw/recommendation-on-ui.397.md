vivienneanthony | 2017-01-02 01:00:07 UTC | #1

Hello,

I have a question. What are some recommendations for loading UI's?

Basically, I will have several UI's.

Default - Showing player quick information like a mini scroll health, mini scroll shield, current active weapon if on, maybe current team information including teammates, and radar.
Speciality UI - Tactical, Engineering, Communications, etc.
and other special UI's, specific consoles being interacted with, ev suit, armor.

Game Related - Everything dealing with the game

Basically, I need a quick way to change between UI's. I think loading and unloading UI's on top of the default.

Any thoughts.

Vivienne

-------------------------

cadaver | 2017-01-02 01:00:07 UTC | #2

When you're talking of UI's of different game states (title screen, ingame etc), I would say it's cleanest to unload (destroy) the stuff that you don't need, eg. destroy ingame UI's when you go to the title screen.

But during gameplay, if you want to avoid small framerate hitches that result from reading the XML UI data and instantiating the elements, you can for example have all ingame UI's loaded, but those that are not needed are set invisible by calling SetVisible(false) on them. Then simply call SetVisible(true) when you want to show them. The editor does this for elements like the material editor window - pressing closebutton does not destroy it, just hides it.

-------------------------

vivienneanthony | 2017-01-02 01:00:08 UTC | #3

[quote="cadaver"]When you're talking of UI's of different game states (title screen, ingame etc), I would say it's cleanest to unload (destroy) the stuff that you don't need, eg. destroy ingame UI's when you go to the title screen.

But during gameplay, if you want to avoid small framerate hitches that result from reading the XML UI data and instantiating the elements, you can for example have all ingame UI's loaded, but those that are not needed are set invisible by calling SetVisible(false) on them. Then simply call SetVisible(true) when you want to show them. The editor does this for elements like the material editor window - pressing closebutton does not destroy it, just hides it.[/quote]

Do you know which samples file have a sample or example of loading a UI from a xml file?

-------------------------

weitjong | 2017-01-02 01:00:09 UTC | #4

The editor itself is a good example.

-------------------------

vivienneanthony | 2017-01-02 01:00:09 UTC | #5

[quote="weitjong"]The editor itself is a good example.[/quote]

Yes. I agree.

I just tried some code which seems to work but I am going have to go to the editor because I rather the UI be layered and I'm not sure if the xml is correct with the visible and invisible ability like someone mentioned.

I modifed my loadsceneui which works by itself but when I load the UI it throws everything off. 

[b]So here is the problem I have[/b]

1. I start the editor and create a UI top bar beginning with the root UIElement. It saves. When I attempt to open the file again it says there is no root.
2. When xml file do loads, it offsets the menu and everything else created is in a different location even after a ui_->clear()

Any ideas anyone? This is the last major problem I have which after I can make some type of game client.

[b]loadSceneUI[/b]
[code]
void ExistenceClient::loadSceneUI(void)
{

    // get resources
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    Renderer* renderer = GetSubsystem<Renderer>();
    Graphics* graphics = GetSubsystem<Graphics>();
    UI* ui = GetSubsystem<UI>();
    FileSystem * filesystem = GetSubsystem<FileSystem>();

    // buttons and menus needed
    Button * logoutsceneButton = new Button(context_);
    Text * logoutsceneText = new Text(context_);

    UIElement * menuUIElements = new UIElement (context_);
    UIElement * quickmenu = new UIElement (context_);

    ui->Clear();

    /// Get rendering window size as floats
    float width = (float)graphics->GetWidth();
    float height = (float)graphics->GetHeight();

    // Login screen - Create the Window and add it to the UI's root node
    window_= new Window(context_);

    // Set Window size and layout settings
    window_->SetMinSize(200, 32);
    window_->SetLayout(LM_FREE, 6, IntRect(6, 6, 6, 6));
    window_->SetAlignment(HA_LEFT, VA_TOP);
    window_->SetName("QuickMenu");
    window_->SetMovable(false);
    window_->SetOpacity(.6);

    logoutsceneButton -> SetAlignment(HA_LEFT, VA_TOP);
    logoutsceneButton -> SetFixedSize(2, 32);
    logoutsceneButton -> SetPosition(0, 0);
    logoutsceneButton -> SetName("logoutsceneButton");
    logoutsceneButton -> SetOpacity(.6);

    logoutsceneText -> SetPosition(64, 0);
    logoutsceneText -> SetAlignment(HA_LEFT, VA_CENTER);
    logoutsceneText -> SetTextAlignment(HA_LEFT);
    logoutsceneText -> SetText("LOGOUT");

    // Set font and text color
    logoutsceneText -> SetFont(cache->GetResource<Font>("Fonts/Anonymous Pro.ttf"), 14);

    /// Each Menu element have a button and text
    menuUIElements -> AddChild(logoutsceneButton);
    menuUIElements -> AddChild(logoutsceneText);

    menuUIElements -> SetPosition(0,0);
    menuUIElements -> SetMinSize(158,32);
    menuUIElements -> SetAlignment(HA_LEFT, VA_TOP);
    menuUIElements -> SetStyleAuto();

    menuUIElements -> SetOpacity(.8);

    /// Add  menu elements
    window_->AddChild(menuUIElements);

    /// Add menu to UIElement
    quickmenu->AddChild(window_);

    quickmenu->SetPosition(width-158,height-100);

    uiRoot_->AddChild(quickmenu);

    logoutsceneButton -> SetStyle("logoutsceneButton");

    return;
}[/code]

[b]loadHUDFIle[/b]
[code]bool ExistenceClient::loadHUDFile(const char * filename)
{
    /// Get resources
    ResourceCache * cache = GetSubsystem<ResourceCache>();
    FileSystem * filesystem = GetSubsystem<FileSystem>();
    UI* ui_ = GetSubsystem<UI>();

    /// get current root
    UIElement * RootUIElement = ui_->GetRoot();

    /// Configure resources
    XMLElement hudElement;

    /// Configure string to Urho friendly
    String filenameHUD = String(filename);

    /// Load Resource
    XMLFile* hudFile= cache->GetResource<XMLFile>(filenameHUD);

    /// Get root element XML
    hudElement =  hudFile->GetRoot();

    /// Load UI Element
    RootUIElement -> LoadXML(hudElement);

    return true;
}
[/code]

TopBarWindow.XML
[code]<?xml version="1.0"?>
<element>
	<attribute name="Name" value="MainTopBarUIElement" />
	<attribute name="Position" value="0 0" />
	<attribute name="Layout Mode" value="Horizontal" />
	<element type="Window">
		<attribute name="Name" value="MainTopBarWindow" />
	</element>
</element>[/code]

-------------------------

vivienneanthony | 2017-01-02 01:00:09 UTC | #6

I think I have it working.

-------------------------

vivienneanthony | 2017-01-02 01:00:09 UTC | #7

Shoot. I just tried this XML.

It seems to affect the console window also and the logout button on the right in which they dissappear or half appear.

[video]https://www.youtube.com/watch?v=i1uu3FD4lkQ[/video]

XML file
[quote][code]<?xml version="1.0"?>
<element>
	<attribute name="Name" value="MainTopBarUIElement" />
	<attribute name="Size" value="1440 19" />
	<attribute name="Min Size" value="1440 19" />
	<attribute name="Is Enabled" value="true" />
	<element type="Window">
		<attribute name="Name" value="MainTopBarWindow" />
		<attribute name="Size" value="1440 19" />
		<attribute name="Min Size" value="1440 19" />
		<attribute name="Opacity" value="0.7" />
		<attribute name="Is Editable" value="false" />
		<element type="Text">
			<attribute name="Name" value="RankPlayerNameText" />
			<attribute name="Vert Alignment" value="Center" />
			<attribute name="Top Left Color" value="0.85 0.85 0.85 1" />
			<attribute name="Top Right Color" value="0.85 0.85 0.85 1" />
			<attribute name="Bottom Left Color" value="0.85 0.85 0.85 1" />
			<attribute name="Bottom Right Color" value="0.85 0.85 0.85 1" />
			<attribute name="Text" value="Rank - Player" />
		</element>
	</element>
</element>[/code][/quote]

-------------------------

vivienneanthony | 2017-01-02 01:00:10 UTC | #8

I changed the code to the following which seems to work. The only problem is the alpha. I'm not sure what is causing it to  blend right. The images are RGBa. So, the alpha at 0 should be invisible.

The screenshot is at [sourceforge.net/projects/proteu ... creenshot/](https://sourceforge.net/projects/proteusgameengine/files/Existence/screenshot/)

[b]loadHUDFile(const char * filename, const int positionx, const int positiony)[/b]
[code]// load a HUD File and sets it's position
bool ExistenceClient::loadHUDFile(const char * filename, const int positionx, const int positiony)
{
    /// Get resources
    ResourceCache * cache = GetSubsystem<ResourceCache>();
    FileSystem * filesystem = GetSubsystem<FileSystem>();
    UI* ui_ = GetSubsystem<UI>();

    /// get current root
    UIElement * RootUIElement = ui_->GetRoot();
    UIElement * HUDFileElement= new UIElement(context_);
    UIElement * playerInfoHudElement= new UIElement(context_);

    /// Configure resources
    XMLElement hudElement;

    /// Configure string to Urho friendly
    String filenameHUD = String(filename);

    /// Load Resource
    XMLFile* hudFile= cache->GetResource<XMLFile>(filenameHUD);

    /// Get root element XML
    hudElement =  hudFile->GetRoot();

    /// Add a min top bar
    HUDFileElement-> LoadXML(hudElement);

    /// Add a uielement for the bar
    RootUIElement -> AddChild(HUDFileElement);

    /// Position the window
    HUDFileElement -> SetPosition(positionx,positiony);

    return true;
}[/code]

[b]PlayeInfoWindow.XML[/b][code]
<?xml version="1.0"?>
<element>
	<attribute name="Name" value="PlayerInfoUIElement" />
	<attribute name="Position" value="0 49" />
	<attribute name="Priority" value="1" />
	<attribute name="Opacity" value="0.9" />
	<attribute name="Is Enabled" value="true" />
	<attribute name="Is Editable" value="false" />
	<attribute name="Use Derived Opacity" value="false" />
	<element type="Window">
		<attribute name="Name" value="PlayerInfoWindow" />
		<attribute name="Size" value="402 42" />
		<attribute name="Priority" value="1" />
		<attribute name="Is Editable" value="false" />
		<attribute name="Blend Mode" value="alpha" />
		<element type="Sprite" style="Sprite">
			<attribute name="Name" value="PlayerInfoBackground" />
			<attribute name="Size" value="402 42" />
			<attribute name="Texture" value="Texture2D;Textures/Buttons/playerinfo.png" />
			<attribute name="Image Rect" value="0 0 402 42" />
			<attribute name="Blend Mode" value="alpha" />
			<attribute name="Priority" value="1" />
			<attribute name="Opacity" value="0.9" />
		</element>
	</element>
</element>[/code]

-------------------------

Mike | 2017-01-02 01:00:10 UTC | #9

[quote]The images are RGBa. So, the alpha at 0 should be invisible.[/quote]

Ensure that your images are 8 bits and that you are using the right technique.

-------------------------

vivienneanthony | 2017-01-02 01:00:10 UTC | #10

[quote="Mike"][quote]The images are RGBa. So, the alpha at 0 should be invisible.[/quote]

Ensure that your images are 8 bits and that you are using the right technique.[/quote]

They are. I think I am using the right technique. The code is almost the exact as I posted.  The only thing I can think of is when I clear the UI  maybe it changed some defaults when I call the loadsceneui function.


This is the current code. Hard coded because it won't change.

[code]void ExistenceClient::loadSceneUI(void)
{

    // get resources
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    Renderer* renderer = GetSubsystem<Renderer>();
    Graphics* graphics = GetSubsystem<Graphics>();
    UI* ui = GetSubsystem<UI>();
    FileSystem * filesystem = GetSubsystem<FileSystem>();

    // buttons and menus needed
    Button * logoutsceneButton = new Button(context_);
    Text * logoutsceneText = new Text(context_);

    UIElement * menuUIElements = new UIElement (context_);
    UIElement * quickmenu = new UIElement (context_);

    ui->Clear();

    /// Get rendering window size as floats
    float width = (float)graphics->GetWidth();
    float height = (float)graphics->GetHeight();

    // Login screen - Create the Window and add it to the UI's root node
    window_= new Window(context_);

    //  position menu
    quickmenu->SetPosition(width-158,height-100);
    quickmenu->SetLayout(LM_FREE, 6, IntRect(0, 0, 158, 32));
    quickmenu->SetAlignment(HA_LEFT, VA_TOP);
    quickmenu->SetMinSize(158, 32);
    quickmenu->SetPriority(1);

    // Set Window size and layout settings
    window_->SetPosition(0,0);
    window_->SetMinSize(158, 32);
    window_->SetLayout(LM_FREE, 6, IntRect(0, 0, 158, 32));
    window_->SetAlignment(HA_LEFT, VA_TOP);
    window_->SetMovable(false);
    window_->SetOpacity(.6);

    logoutsceneButton -> SetAlignment(HA_LEFT, VA_TOP);
    logoutsceneButton -> SetFixedSize(2, 32);
    logoutsceneButton -> SetPosition(0, 0);
    logoutsceneButton -> SetName("logoutsceneButton");
    logoutsceneButton -> SetOpacity(.6);
    //logoutsceneButton -> SetBlendMode(BLEND_ADDALPHA);

    logoutsceneText -> SetPosition(64, 0);
    logoutsceneText -> SetAlignment(HA_LEFT, VA_CENTER);
    logoutsceneText -> SetTextAlignment(HA_LEFT);
    logoutsceneText -> SetText("LOGOUT");

    /// Set font and text color
    logoutsceneText -> SetFont(cache->GetResource<Font>("Fonts/Anonymous Pro.ttf"), 14);

    /// Each Menu element have a button and text
    menuUIElements -> AddChild(logoutsceneButton);
    menuUIElements -> AddChild(logoutsceneText);

    menuUIElements -> SetPosition(0,0);
    menuUIElements -> SetMinSize(158,32);
    menuUIElements -> SetAlignment(HA_LEFT, VA_TOP);

    menuUIElements -> SetOpacity(.8);

    /// Add  menu elements
    window_->AddChild(menuUIElements);

    /// Add menu to UIElement
    quickmenu->AddChild(window_);

    // Add to root
    uiRoot_->AddChild(quickmenu);

    window_->SetStyleAuto();
    menuUIElements->SetStyleAuto();
    quickmenu->SetStyleAuto();

    logoutsceneButton -> SetStyle("logoutsceneButton");


    return;
}

[/code]

-------------------------

friesencr | 2017-01-02 01:00:10 UTC | #11

I don't think you need to clear the ui.  I think Urho takes care of that for you.  Also as a general rule always add the newly created item to its parent right away.  It's a little fussy.

-------------------------

vivienneanthony | 2017-01-02 01:00:10 UTC | #12

[quote="friesencr"]I don't think you need to clear the ui.  I think Urho takes care of that for you.  Also as a general rule always add the newly created item to its parent right away.  It's a little fussy.[/quote]

Hmmm. I'll look at it tomorrow. I was messing with the code for a hour trying to arrange it.  It's like its reading the xml  for the buttoon style and applying it but not replacing the built in button for the image.

-------------------------

vivienneanthony | 2017-01-02 01:00:11 UTC | #13

[quote="friesencr"]I don't think you need to clear the ui.  I think Urho takes care of that for you.  Also as a general rule always add the newly created item to its parent right away.  It's a little fussy.[/quote]

I think I did it but still no go.  :frowning:

-------------------------

vivienneanthony | 2017-01-02 01:00:11 UTC | #14

Maybe someone can pick up the errors in this? This is the raw code. It's late and the pic from the scene.

Full Image : [i61.tinypic.com/2i7rci9.jpg](http://i61.tinypic.com/2i7rci9.jpg)

[img]http://i61.tinypic.com/2i7rci9.jpg[/img]

[code]// code to handle actual commans
void ExistenceClient::GenerateScene(const time_t &timeseed,  planet_rule planetrule)
{

    /// play with rules
    srand(timeseed);  // use time as the rule

    /// Define Resouces
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    Renderer* renderer = GetSubsystem<Renderer>();
    Graphics* graphics = GetSubsystem<Graphics>();
    UI* ui = GetSubsystem<UI>();
    FileSystem * filesystem = GetSubsystem<FileSystem>();

    /// create variables (urho3d)
    String InputDataFile;

    /// Create Scene components
    scene_-> CreateComponent<Octree>();
    scene_-> CreateComponent<PhysicsWorld>();
    scene_-> CreateComponent<DebugRenderer>();

    /// Create skybox. The Skybox component is used like StaticModel, but it will be always located at the camera, giving the
    /// illusion of the box planes being far away. Use just the ordinary Box model and a suitable material, whose shader will
    /// generate the necessary 3D texture coordinates for cube mapping
    Node* skyNode = scene_->CreateChild("Sky");
    skyNode->SetScale(500.0f); // The scale actually does not matter
    Skybox* skybox = skyNode->CreateComponent<Skybox>();
    skybox->SetModel(cache->GetResource<Model>("Models/Box.mdl"));
    skybox->SetMaterial(cache->GetResource<Material>("Materials/Skybox.xml"));

    /// Create a Zone component for ambient lighting & fog control
    Node* zoneNode = scene_->CreateChild("Zone");
    Zone* zone = zoneNode->CreateComponent<Zone>();

    Vector3 boundingBoxMin(-1000.0f,0,-1000.0f);
    Vector3 boundingBoxMax(1000.0f,2000.0f,1000.0f);

    /// change bounding box to something more accurate
    zone->SetBoundingBox(BoundingBox(boundingBoxMin,boundingBoxMax));
    zone->SetAmbientColor(Color(0.01f, 0.01f, .01f));
    zone->SetFogColor(Color(1.0f, 1.0f, 1.0f));
    zone->SetFogStart(0.0f);
    zone->SetFogEnd(1000.0f);
    zone->SetHeightFog (false);

    /// Create a directional light to the world. Enable cascaded shadows on it
    Node* lightNode = scene_->CreateChild("DirectionalLight");
    lightNode->SetDirection(Vector3(0.6f, -1.0f, 0.8f));
    Light* light = lightNode->CreateComponent<Light>();
    light->SetLightType(LIGHT_DIRECTIONAL);
    light->SetCastShadows(false);
    light->SetShadowBias(BiasParameters(0.00025f, 0.5f));
    light->SetShadowCascade(CascadeParameters(10.0f, 50.0f, 200.0f, 0.0f, 0.8f));
    light->SetSpecularIntensity(0.0f);
    light->SetBrightness(.9);
    light->SetColor(Color(0.251f, 0.612f, 1.0f));

    /// Create a directional light to the world. Enable cascaded shadows on it
    Node* lightNode2 = scene_->CreateChild("DirectionalLight2");
    Light* light2 = lightNode2->CreateComponent<Light>();
    light2->SetLightType(LIGHT_DIRECTIONAL);
    light2->SetCastShadows(true);
    light2->SetShadowBias(BiasParameters(0.00025f, 0.5f));
    light2->SetShadowCascade(CascadeParameters(10.0f, 50.0f, 200.0f, 0.0f, 0.8f));
    light2->SetSpecularIntensity(2.0f);
    light2->SetBrightness(.7);
    light2->SetColor(Color(1.0f, 1.0f,.95f));

    lightNode2->SetRotation(Quaternion(55.7392,0,0));

    /// Generate Terrain
    Node* terrainNode = scene_->CreateChild("Terrain");

    Terrain* terrain = terrainNode->CreateComponent<Terrain>();
    terrain->SetPatchSize(64);
    terrain->SetSpacing(Vector3(2.0f, 0.8f, 2.0f)); // Spacing between vertices and vertical resolution of the height map
    terrain->SetSmoothing(true);
    terrain->SetCastShadows(true);

    /// generatescene
    terrain->GenerateProceduralHeightMap(planetrule);

    terrain->SetMaterial(cache->GetResource<Material>("Materials/TerrainTriPlanar.xml"));

    RigidBody* terrainbody = terrainNode->CreateComponent<RigidBody>();

    CollisionShape* terrainshape = terrainNode->CreateComponent<CollisionShape>();

    terrainbody->SetCollisionLayer(1);
    terrainshape->SetTerrain();

    /// Create a scene node for the camera, which we will move around
    /// The camera will use default settings (1000 far clip distance, 45 degrees FOV, set aspect ratio automatically)
    cameraNode_ = new Node(context_);

    cameraNode_ = scene_->CreateChild("Camera");
    cameraNode_->CreateComponent<Camera>();

    Camera* camera = cameraNode_->CreateComponent<Camera>();
    camera->SetFarClip(1000.0f);
    // Set an initial position for the camera scene node above the ground
    cameraNode_->SetPosition(Vector3(0.0f, 0.0f, 0.0f));

    SharedPtr<Viewport> viewport(new Viewport(context_, scene_, cameraNode_->GetComponent<Camera>()));
    renderer->SetViewport(0, viewport);

    Vector3 position(0.0f,0.0f);
    position.y_ = terrain->GetHeight(position) + 1.0f;

    /// Position character
    Node * characternode_ = scene_->CreateChild("Character");
    characternode_->SetPosition(Vector3(0.0f, position.y_ , 0.0f));

    /// Create chacter
    CreateCharacter();

    /// Load main UI area
    loadSceneUI();

    /// rest of UI
    loadHUDFile("Resources/UI/MainTopBarWindow.xml",0,0);
    loadHUDFile("Resources/UI/PlayerInfoWindow.xml",0,34);

    /// Add a object to the seen - Pod Node
    Node * PodNode1 = scene_ -> CreateChild("podNode");

    StaticModel* PodObject1 = PodNode1 ->CreateComponent<StaticModel>();

    PodObject1->SetModel(cache->GetResource<Model>("Resources/Models/pod.mdl"));
    PodObject1->ApplyMaterialList("Resources/Models/pod.txt");
    PodObject1->SetCastShadows(true);

    Vector3 position2(4.0f,4.0f);
    position2.y_ = terrain->GetHeight(position2);

    PodNode1->SetPosition(Vector3(4.0f, position2.y_+.6f , 4.0f));

    RigidBody* PodBody= PodNode1->CreateComponent<RigidBody>();
    CollisionShape* Podshape = PodNode1->CreateComponent<CollisionShape>();

    Podshape->SetTriangleMesh (cache->GetResource<Model>("Resources/Models/pod.mdl"));
    PodBody->SetCollisionLayer(1);
    Podshape ->SetLodLevel(1);

    return;
}

// load a HUD File and sets it's position
bool ExistenceClient::loadHUDFile(const char * filename, const int positionx, const int positiony)
{
    /// Get resources
    ResourceCache * cache = GetSubsystem<ResourceCache>();
    FileSystem * filesystem = GetSubsystem<FileSystem>();
    UI* ui_ = GetSubsystem<UI>();

    /// get current root
    UIElement * RootUIElement = ui_->GetRoot();
    UIElement * HUDFileElement= new UIElement(context_);
    UIElement * playerInfoHudElement= new UIElement(context_);

    /// Configure resources
    XMLElement hudElement;

    /// Configure string to Urho friendly
    String filenameHUD = String(filename);

    /// Load Resource
    XMLFile* hudFile= cache->GetResource<XMLFile>(filenameHUD);

    /// Get root element XML
    hudElement =  hudFile->GetRoot();

    /// Add a min top bar
    HUDFileElement-> LoadXML(hudElement);

    /// Add a uielement for the bar
    RootUIElement -> AddChild(HUDFileElement);

    /// Position the window

    HUDFileElement -> SetPosition(positionx,positiony);

    HUDFileElement->SetStyleAuto();

    return true;
}

void ExistenceClient::loadSceneUI(void)
{

    // get resources
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    Renderer* renderer = GetSubsystem<Renderer>();
    Graphics* graphics = GetSubsystem<Graphics>();
    UI* ui = GetSubsystem<UI>();
    FileSystem * filesystem = GetSubsystem<FileSystem>();

    ui->Clear();

    /// Get rendering window size as floats
    float width = (float)graphics->GetWidth();
    float height = (float)graphics->GetHeight();

    UIElement * menuUIElements = new UIElement (context_);
    UIElement * quickmenu = new UIElement (context_);

    // buttons and menus needed
    Button * logoutsceneButton = new Button(context_);
    Text * logoutsceneText = new Text(context_);


    // Login screen - Create the Window and add it to the UI's root node
    window_= new Window(context_);

    //  position menu
    quickmenu->SetPosition(width-158,height-100);
    quickmenu->SetLayout(LM_FREE, 6, IntRect(0, 0, 158, 32));
    quickmenu->SetAlignment(HA_LEFT, VA_TOP);
    quickmenu->SetMinSize(158, 32);
    quickmenu->SetPriority(1);

    // Set Window size and layout settings
    window_->SetPosition(0,0);
    window_->SetMinSize(158, 32);
    window_->SetLayout(LM_FREE, 6, IntRect(0, 0, 158, 32));
    window_->SetAlignment(HA_LEFT, VA_TOP);
    window_->SetMovable(false);

    logoutsceneButton -> SetLayout(LM_FREE, 6, IntRect(0, 0, 158,32));
    logoutsceneButton -> SetAlignment(HA_LEFT, VA_TOP);
    logoutsceneButton -> SetFixedSize(158, 32);
    logoutsceneButton -> SetPosition(0, 0);
    logoutsceneButton -> SetName("logoutsceneButton");
    logoutsceneButton -> SetOpacity(.8);

    logoutsceneText -> SetPosition(64, 0);
    logoutsceneText -> SetAlignment(HA_LEFT, VA_CENTER);
    logoutsceneText -> SetTextAlignment(HA_LEFT);
    logoutsceneText -> SetText("LOGOUT");

    /// Set font and text color
    logoutsceneText -> SetFont(cache->GetResource<Font>("Fonts/Anonymous Pro.ttf"), 14);

    menuUIElements -> SetPosition(0,0);
    menuUIElements -> SetMinSize(158,32);
    menuUIElements -> SetAlignment(HA_LEFT, VA_TOP);
    menuUIElements -> SetOpacity(.8);

    /// Each Menu element have a button and text
    menuUIElements -> AddChild(logoutsceneButton);
    menuUIElements -> AddChild(logoutsceneText);

    /// Add  menu elements
    window_->AddChild(menuUIElements);

    /// Add menu to UIElement
    quickmenu->AddChild(window_);

    /// Add to root
    uiRoot_->AddChild(quickmenu);

    menuUIElements->SetStyleAuto();
    quickmenu->SetStyleAuto();
    window_->SetStyleAuto();

    logoutsceneButton -> SetStyle("logoutsceneButton");


    return;
}



[/code]

-------------------------

vivienneanthony | 2017-01-02 01:00:11 UTC | #15

[quote="friesencr"]I don't think you need to clear the ui.  I think Urho takes care of that for you.  Also as a general rule always add the newly created item to its parent right away.  It's a little fussy.[/quote]

I was using the whole window objects which was causing the problem. I rather use windows for the different areas but since it's not needed yet. I removed them just using UIELements which seems to work right now.

-------------------------

Madman097 | 2017-01-02 01:00:31 UTC | #16

Hi  :slight_smile: 

I was using your code to load UI from XML file and I had similar problem - everything was only white and transparent. After a lot of digging I realized, I'm not loading UI properly. Just keep in mind to load layout trough UI subsystem rather than load an root element of XML file. Here, the simplest and working code:

[code]XMLFile * sett_xml = GetSubsystem<ResourceCache>()->GetResource<XMLFile>("UI/Settings.xml");
SharedPtr<UIElement> window_settings = GetSubsystem<UI>()->LoadLayout(sett_xml);
GetSubsystem<UI>()->GetRoot()->AddChild(window_settings);
window_settings->SetVisible(false);
window_settings->SetPosition(200, 200);
window_settings->SetStyleAuto();
[/code]

-------------------------

vivienneanthony | 2017-01-02 01:00:31 UTC | #17

[quote="Madman097"]Hi  :slight_smile: 

I was using your code to load UI from XML file and I had similar problem - everything was only white and transparent. After a lot of digging I realized, I'm not loading UI properly. Just keep in mind to load layout trough UI subsystem rather than load an root element of XML file. Here, the simplest and working code:

[code]XMLFile * sett_xml = GetSubsystem<ResourceCache>()->GetResource<XMLFile>("UI/Settings.xml");
SharedPtr<UIElement> window_settings = GetSubsystem<UI>()->LoadLayout(sett_xml);
GetSubsystem<UI>()->GetRoot()->AddChild(window_settings);
window_settings->SetVisible(false);
window_settings->SetPosition(200, 200);
window_settings->SetStyleAuto();
[/code][/quote]

Thanks. I isolated the problem to me using a background. I figure there was too much dependencies and inherits so I just minused the window.

The newest videos I have shows that it has been resolved.

-------------------------

