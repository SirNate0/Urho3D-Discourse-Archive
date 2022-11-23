rasteron | 2017-01-02 01:07:09 UTC | #1

A simple SplashScreen example as [b]ScriptObject[/b] and derived from Scene and UI Load demo. Some snippets from [b]codingmonkey[/b] and [b]Mike[/b]. This toggles the cursor, root layout and camera/cam controls. Time delay option as well..

[code]
// Scene & UI load example.
// This sample demonstrates:
//      - Loading a scene from a file and showing it
//      - Loading a UI layout from a file and showing it
//      - Subscribing to the UI layout's events
#include "Scripts/Utilities/Sample.as"
float timeToShowScene;
int secCount = 5; //Display time in seconds
Node@ splashNode;

void Start() {
  timeToShowScene = time.systemTime + (1000 * secCount);
  // Create the scene content
  CreateScene();
  // Create the UI content and subscribe to UI events
  CreateUI();
  CreateSplashScreen();
  // Setup the viewport for displaying the scene
  SetupViewport();
  // Subscribe to global events for camera movement
  SubscribeToEvents();
}

void CreateScene() {
  scene_ = Scene();
  // Load scene content prepared in the editor (XML format). GetFile() returns an open file from the resource system
  // which scene.LoadXML() will read
  scene_.LoadAsyncXML(cache.GetFile("Scenes/SceneLoadExample.xml"));
  // Create the camera (not included in the scene file)
  cameraNode = scene_.CreateChild("Camera");
  cameraNode.CreateComponent("Camera");
  cameraNode.enabled = false;
  // Create the rendering and physics components
  //SplashScreen.Init();
  // Set an initial position for the camera scene node above the plane
  cameraNode.position = Vector3(0.0f, 2.0f, -10.0f);
}

void CreateUI() {
  // Set up global UI style into the root UI element
  XMLFile@ style = cache.GetResource("XMLFile", "UI/DefaultStyle.xml");
  ui.root.defaultStyle = style;
  // Create a Cursor UI element because we want to be able to hide and show it at will. When hidden, the mouse cursor will
  // control the camera, and when visible, it will interact with the UI
  Cursor@ cursor = Cursor();
  cursor.SetStyleAuto();
  ui.cursor = cursor;
  // Set starting position of the cursor at the rendering window center
  cursor.SetPosition(graphics.width / 2, graphics.height / 2);
  cursor.visible = false;
  // Load UI content prepared in the editor and add to the UI hierarchy
  UIElement@ layoutRoot = ui.LoadLayout(cache.GetResource("XMLFile", "UI/UILoadExample.xml"));
  ui.root.AddChild(layoutRoot);
  layoutRoot.visible = false;
  // Subscribe to button actions (toggle scene lights when pressed then released)
  Button@ button = layoutRoot.GetChild("ToggleLight1", true);
  if (button!is null) SubscribeToEvent(button, "Released", "ToggleLight1");
  button = layoutRoot.GetChild("ToggleLight2", true);
  if (button!is null) SubscribeToEvent(button, "Released", "ToggleLight2");
}

void ToggleLight1() {
  Node@ lightNode = scene_.GetChild("Light1", true);
  if (lightNode!is null) lightNode.enabled = !lightNode.enabled;
}

void ToggleLight2() {
  Node@ lightNode = scene_.GetChild("Light2", true);
  if (lightNode!is null) lightNode.enabled = !lightNode.enabled;
}

void SetupViewport() {
  // Set up a viewport to the Renderer subsystem so that the 3D scene can be seen
  Viewport@ viewport = Viewport(scene_, cameraNode.GetComponent("Camera"));
  renderer.viewports[0] = viewport;
}

void SubscribeToEvents() {
  // Subscribe HandleUpdate() function for camera motion
  SubscribeToEvent("Update", "HandleUpdate");
}

void HandleUpdate(StringHash eventType, VariantMap & eventData) {
  if (splashNode is null) return;
  SplashScreen@ splash = cast < SplashScreen > (splashNode.scriptObject);
  if (splash is null) return;
  // Take the frame time step, which is stored as a float
  float timeStep = eventData["TimeStep"].GetFloat();
  // Don't move camera until Splashscreen is removed
  if (ui.root.GetChild("Splash") is null)
  // Move the camera, scale movement with time step    
    MoveCamera(timeStep);
}

void MoveCamera(float timeStep) {
  // Right mouse button controls mouse cursor visibility: hide when pressed
  ui.cursor.visible = !input.mouseButtonDown[MOUSEB_RIGHT];
  // Do not move if the UI has a focused element
  if (ui.focusElement!is null) return;
  // Movement speed as world units per second
  const float MOVE_SPEED = 20.0f;
  // Mouse sensitivity as degrees per pixel
  const float MOUSE_SENSITIVITY = 0.1f;
  // Use this frame's mouse motion to adjust camera node yaw and pitch. Clamp the pitch between -90 and 90 degrees
  // Only move the camera when the cursor is hidden
  if (!ui.cursor.visible) {
    IntVector2 mouseMove = input.mouseMove;
    yaw += MOUSE_SENSITIVITY * mouseMove.x;
    pitch += MOUSE_SENSITIVITY * mouseMove.y;
    pitch = Clamp(pitch, -90.0f, 90.0f);
    // Construct new orientation for the camera scene node from yaw and pitch. Roll is fixed to zero
    cameraNode.rotation = Quaternion(pitch, yaw, 0.0f);
  }
  // Read WASD keys and move the camera scene node to the corresponding direction if they are pressed
  if (input.keyDown['W']) cameraNode.Translate(Vector3(0.0f, 0.0f, 1.0f) * MOVE_SPEED * timeStep);
  if (input.keyDown['S']) cameraNode.Translate(Vector3(0.0f, 0.0f, -1.0f) * MOVE_SPEED * timeStep);
  if (input.keyDown['A']) cameraNode.Translate(Vector3(-1.0f, 0.0f, 0.0f) * MOVE_SPEED * timeStep);
  if (input.keyDown['D']) cameraNode.Translate(Vector3(1.0f, 0.0f, 0.0f) * MOVE_SPEED * timeStep);
}

void CreateSplashScreen() {
  splashNode = scene_.CreateChild("Splash");
  splashNode.CreateScriptObject(scriptFile, "SplashScreen");
  SplashScreen@ splash = cast < SplashScreen > (splashNode.scriptObject);
  splash.Init();
}

class SplashScreen : ScriptObject {
    void Init() {
      BorderImage@ splashUI = ui.root.CreateChild("BorderImage", "Splash");
      Texture2D@ texture = cache.GetResource("Texture2D", "Textures/LogoLarge.png"); // Get texture
      splashUI.texture = texture; // Set texture
      splashUI.SetSize(texture.width, texture.height);
      splashUI.SetAlignment(HA_CENTER, VA_CENTER);
    }
    void FixedUpdate(float timeStep) {
      if (timeToShowScene < time.systemTime) {
        if (ui.root.GetChild("Splash")!is null) 
          ui.root.GetChild("Splash").Remove();
        if (ui.root.GetChild("LayoutRoot")!is null) 
          ui.root.GetChild("LayoutRoot").visible = true;
        
        ui.cursor.visible = true;        
        cameraNode.enabled = true;
        // Execute the common startup for samples
        SampleStart();    
      }
    }
}
  // Create XML patch instructions for screen joystick layout specific to this sample app
String patchInstructions = "";
[/code]

I have to foolproof loading the main layout by adding and tagging UILoadExample.xml:

[code]<attribute name="Name" value="LayoutRoot" />[/code]

enjoy!  :wink:

-------------------------

