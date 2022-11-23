zerokol | 2017-01-02 01:06:15 UTC | #1

I'm new on Urho3d. I`m trying to create a 2D, i was following the demos.

I was trying to order my images (z axis), not worked.

I want that background.jpg in a layer, over it, olympic-logo.png and text

Am I forgetting something? 

[code]
// Urho2D sprite example.
// This sample demonstrates:
//     - Creating a 2D scene with sprite
//     - Displaying the scene using the Renderer subsystem
//     - Handling keyboard to move and zoom 2D camera

#include "Scripts/Utilities/Sample.as"

void Start()
{
    // Execute the common startup for samples
    SampleStart();

    // Create the scene content
    CreateScene();

    // Setup the viewport for displaying the scene
    SetupViewport();

    // Hook up to the frame update events
    SubscribeToEvents();
}

void CreateScene()
{
    scene_ = Scene();

    // Create the Octree component to the scene. This is required before adding any drawable components, or else nothing will
    // show up. The default octree volume will be from (-1000, -1000, -1000) to (1000, 1000, 1000) in world coordinates; it
    // is also legal to place objects outside the volume but their visibility can then not be checked in a hierarchically
    // optimizing manner
    scene_.CreateComponent("Octree");

    // Create a scene node for the camera, which we will move around
    // The camera will use default settings (1000 far clip distance, 45 degrees FOV, set aspect ratio automatically)
    cameraNode = scene_.CreateChild("Camera");
    // Set an initial position for the camera scene node above the plane
    cameraNode.position = Vector3(0.0f, 0.0f, -10.0f);

    Camera@ camera = cameraNode.CreateComponent("Camera");
    camera.orthographic = true;
    camera.orthoSize = graphics.height * PIXEL_SIZE;

    //----------------------------------------------------------------------------------------
    // background
    Sprite2D@ backgroundSprite = cache.GetResource("Sprite2D", "Textures/background.jpg");

    if (backgroundSprite is null) {
        return;
    }

    Node@ backgroundNode = scene_.CreateChild("StaticSprite2D");
    backgroundNode.position = Vector3(0.0f, 0.0f, 3.0f);

    StaticSprite2D@ backgroundNodeStaticSprite = backgroundNode.CreateComponent("StaticSprite2D");
    // Set blend mode
    backgroundNodeStaticSprite.blendMode = BLEND_ALPHA;
    // Set sprite
    backgroundNodeStaticSprite.sprite = backgroundSprite;
    //----------------------------------------------------------------------------------------
    // Get logo texture
    Sprite2D@ bigLogoSprite = cache.GetResource("Sprite2D", "Textures/olympic-logo.png");

    if (bigLogoSprite is null) {
        return;
    }

    Node@ bigLogoNode = scene_.CreateChild("StaticSprite2D");
    bigLogoNode.position = Vector3(0.0f, 0.0f, 2.0f);

    StaticSprite2D@ bigLogoNodeStaticSprite = bigLogoNode.CreateComponent("StaticSprite2D");
    // Set blend mode
    bigLogoNodeStaticSprite.blendMode = BLEND_ALPHA;
    // Set sprite
    bigLogoNodeStaticSprite.sprite = bigLogoSprite;

    //----------------------------------------------------------------------------------------
    Node@ gameNameNode = scene_.CreateChild("Text3D");
    gameNameNode.position = Vector3(0.0f, 0.0f, 1.0f);
    
    // Construct new Text object
    Text3D@ gameNameText = gameNameNode.CreateComponent("Text3D");

    gameNameText.text = "Matem?tica Ol?mpica";

    // Set font and text color
    gameNameText.SetFont(cache.GetResource("Font", "Fonts/sf-comic-script.ttf"), 110);
    gameNameText.color = Color(0.0f, 0.0f, 0.0f);

    // Align Text center-screen
    gameNameText.horizontalAlignment = HA_CENTER;
    gameNameText.verticalAlignment = VA_CENTER;

    //----------------------------------------------------------------------------------------
    AnimationSet2D@ animationSet = cache.GetResource("AnimationSet2D", "Urho2D/GoldIcon.scml");
    
    if (animationSet is null)
        return;

    Node@ spriteNode = scene_.CreateChild("AnimatedSprite2D");
    spriteNode.position = Vector3(0.0f, 0.0f, -10.0f);

    AnimatedSprite2D@ animatedSprite = spriteNode.CreateComponent("AnimatedSprite2D");
    // Set animation
    animatedSprite.SetAnimation(animationSet, "idle");
}

void SetupViewport()
{
    // Set up a viewport to the Renderer subsystem so that the 3D scene can be seen. We need to define the scene and the camera
    // at minimum. Additionally we could configure the viewport screen size and the rendering path (eg. forward / deferred) to
    // use, but now we just use full screen and default render path configured in the engine command line options
    Viewport@ viewport = Viewport(scene_, cameraNode.GetComponent("Camera"));
    renderer.viewports[0] = viewport;
    renderer.defaultZone.fogColor = Color(1.0f, 1.0f, 1.0f); // Set background color for the scene
}

void MoveCamera(float timeStep)
{
    // Do not move if the UI has a focused element (the console)
    if (ui.focusElement !is null)
        return;

    // Movement speed as world units per second
    const float MOVE_SPEED = 4.0f;

    // Read WASD keys and move the camera scene node to the corresponding direction if they are pressed
    if (input.keyDown['W'])
        cameraNode.Translate(Vector3(0.0f, 1.0f, 0.0f) * MOVE_SPEED * timeStep);
    if (input.keyDown['S'])
        cameraNode.Translate(Vector3(0.0f, -1.0f, 0.0f) * MOVE_SPEED * timeStep);
    if (input.keyDown['A'])
        cameraNode.Translate(Vector3(-1.0f, 0.0f, 0.0f) * MOVE_SPEED * timeStep);
    if (input.keyDown['D'])
        cameraNode.Translate(Vector3(1.0f, 0.0f, 0.0f) * MOVE_SPEED * timeStep);

    if (input.keyDown[KEY_PAGEUP])
    {
        Camera@ camera = cameraNode.GetComponent("Camera");
        camera.zoom = camera.zoom * 1.01f;
    }

    if (input.keyDown[KEY_PAGEDOWN])
    {
        Camera@ camera = cameraNode.GetComponent("Camera");
        camera.zoom = camera.zoom * 0.99f;
    }
}

void SubscribeToEvents()
{
    // Subscribe HandleUpdate() function for processing update events
    SubscribeToEvent("Update", "HandleUpdate");

    // Unsubscribe the SceneUpdate event from base class to prevent camera pitch and yaw in 2D sample
    UnsubscribeFromEvent("SceneUpdate");
}

void HandleUpdate(StringHash eventType, VariantMap& eventData)
{
    // Take the frame time step, which is stored as a float
    float timeStep = eventData["TimeStep"].GetFloat();

    // Move the camera, scale movement with time step
    MoveCamera(timeStep);
}

// Create XML patch instructions for screen joystick layout specific to this sample app
String patchInstructions =
        "<patch>" +
        "    <remove sel=\"/element/element[./attribute[@name='Name' and @value='Button0']]/attribute[@name='Is Visible']\" />" +
        "    <replace sel=\"/element/element[./attribute[@name='Name' and @value='Button0']]/element[./attribute[@name='Name' and @value='Label']]/attribute[@name='Text']/@value\">Zoom In</replace>" +
        "    <add sel=\"/element/element[./attribute[@name='Name' and @value='Button0']]\">" +
        "        <element type=\"Text\">" +
        "            <attribute name=\"Name\" value=\"KeyBinding\" />" +
        "            <attribute name=\"Text\" value=\"PAGEUP\" />" +
        "        </element>" +
        "    </add>" +
        "    <remove sel=\"/element/element[./attribute[@name='Name' and @value='Button1']]/attribute[@name='Is Visible']\" />" +
        "    <replace sel=\"/element/element[./attribute[@name='Name' and @value='Button1']]/element[./attribute[@name='Name' and @value='Label']]/attribute[@name='Text']/@value\">Zoom Out</replace>" +
        "    <add sel=\"/element/element[./attribute[@name='Name' and @value='Button1']]\">" +
        "        <element type=\"Text\">" +
        "            <attribute name=\"Name\" value=\"KeyBinding\" />" +
        "            <attribute name=\"Text\" value=\"PAGEDOWN\" />" +
        "        </element>" +
        "    </add>" +
        "</patch>";

[/code]

-------------------------

codingmonkey | 2017-01-02 01:06:15 UTC | #2

You should use int layer in StaticSprite2D for z-order
[urho3d.github.io/documentation/1 ... icSprite2D](http://urho3d.github.io/documentation/1.4/_script_a_p_i.html#Class_StaticSprite2D)

-------------------------

zerokol | 2017-01-02 01:06:16 UTC | #3

Perfect! Thank you very much!!!

-------------------------

