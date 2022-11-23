sabotage3d | 2017-01-02 01:02:12 UTC | #1

Hi guys,
Is there any simple example on how to use custom shaders. Something really simple like a constant vertex and fragment shader. 
What is the difference between Materials , Techniques and Renderpaths ?

-------------------------

ghidra | 2017-01-02 01:02:12 UTC | #2

I have been dealing with this the last few weeks.
I am starting to get a grip on it, but that is not to say I fully understand. Just that I am able to make a custom shader.

I wrote a blog post on the subject here:

[url]http://nervegass.blogspot.com/2014/12/urho-shaders-edge-detection.html[/url]

Hopefully it helps. I'm not writer.
I can make a much simpler one tonight if i need to be more clear.

-------------------------

sabotage3d | 2017-01-02 01:02:12 UTC | #3

Thanks ghidra,

Do you happen to have a complete project from your blog ?
Or the C++ files for the sample ?

-------------------------

ghidra | 2017-01-02 01:02:12 UTC | #4

The only source missing from that blog post is my anglescript file, which is actually based on one of the example files.

[code]
#include "Scripts/Utilities/Sample.as"

void Start(){
    SampleStart();
    CreateScene();
    SetupViewport();
    SubscribeToEvents();
}

void CreateScene(){
    scene_ = Scene();
    scene_.CreateComponent("Octree");

    Node@ bgnode = scene_.CreateChild("BG");
    StaticModel@ bgobj = bgnode.CreateComponent("StaticModel");
    bgobj.model = cache.GetResource("Model", "Models/Plane.mdl");
    Material@ bmata = cache.GetResource("Material", "Materials/research/simple.xml");
    Material@ rmata = bmata.Clone();
    Color myCola = Color(Random(1.0f),Random(1.0f),Random(1.0f),1.0f);
    rmata.shaderParameters["ObjectColor"]=Variant(myCola);//single quotes didnt work
    bgobj.material = rmata;

    bgnode.Scale(15.0f);
    bgnode.SetTransform(Vector3(0.0f,0.0f,15.0f),Quaternion(90.0f,Vector3(-1.0f,0.0f,0.0f)));

    const uint NUM_OBJECTS = 100;
    for (uint i = 0; i < NUM_OBJECTS; ++i)
    {
        Node@ boxNode = scene_.CreateChild("Box");
        boxNode.position = Vector3(Random(50.0f) - 25.0f, Random(50.0f) - 25.0f, Random(50.0f) - 25.0f);
        // Orient using random pitch, yaw and roll Euler angles
        boxNode.rotation = Quaternion(Random(360.0f), Random(360.0f), Random(360.0f));
        StaticModel@ boxObject = boxNode.CreateComponent("StaticModel");
        boxObject.model = cache.GetResource("Model", "Models/Box.mdl");

        Material@ bmat = cache.GetResource("Material", "Materials/research/simple.xml");
        Material@ rmat = bmat.Clone();

        Color myCol = Color(Random(1.0f),Random(1.0f),Random(1.0f),1.0f);

        rmat.shaderParameters["ObjectColor"]=Variant(myCol);//single quotes didnt work
        boxObject.material = rmat;

        // Add the Rotator script object which will rotate the scene node each frame, when the scene sends its update event.
        // This requires the C++ component ScriptInstance in the scene node, which acts as a container. We need to tell the
        // script file and class name to instantiate the object (scriptFile is a global property which refers to the currently
        // executing script file.) There is also a shortcut for creating the ScriptInstance component and the script object,
        // which is shown in a later sample, but this is what happens "under the hood."
        ScriptInstance@ instance = boxNode.CreateComponent("ScriptInstance");
        instance.CreateObject(scriptFile, "Rotator");
        // Retrieve the created script object and set its rotation speed member variable
        Rotator@ rotator = cast<Rotator>(instance.scriptObject);
        rotator.rotationSpeed = Vector3(10.0f, 20.0f, 30.0f);
    }

    Node@ lightNode = scene_.CreateChild("DirectionalLight");
    lightNode.direction = Vector3(0.6f, -1.0f, 0.8f); // The direction vector does not need to be normalized
    Light@ light = lightNode.CreateComponent("Light");
    light.lightType = LIGHT_DIRECTIONAL;

    cameraNode = scene_.CreateChild("Camera");
    cameraNode.CreateComponent("Camera");

    cameraNode.position = Vector3(0.0f, 5.0f, -25.0f);
}


void SetupViewport(){
    // Set up a viewport to the Renderer subsystem so that the 3D scene can be seen. We need to define the scene and the camera
    // at minimum. Additionally we could configure the viewport screen size and the rendering path (eg. forward / deferred) to
    // use, but now we just use full screen and default render path configured in the engine command line options
    Viewport@ viewport = Viewport(scene_, cameraNode.GetComponent("Camera"));
    XMLFile@ xml = cache.GetResource("XMLFile", "RenderPaths/research/Forward.xml");
    viewport.SetRenderPath(xml);
    renderer.viewports[0] = viewport;
}

void MoveCamera(float timeStep){
    // Do not move if the UI has a focused element (the console)
    if (ui.focusElement !is null)
        return;

    // Movement speed as world units per second
    const float MOVE_SPEED = 20.0f;
    // Mouse sensitivity as degrees per pixel
    const float MOUSE_SENSITIVITY = 0.1f;

    // Use this frame's mouse motion to adjust camera node yaw and pitch. Clamp the pitch between -90 and 90 degrees
    IntVector2 mouseMove = input.mouseMove;
    yaw += MOUSE_SENSITIVITY * mouseMove.x;
    pitch += MOUSE_SENSITIVITY * mouseMove.y;
    pitch = Clamp(pitch, -90.0f, 90.0f);

    // Construct new orientation for the camera scene node from yaw and pitch. Roll is fixed to zero
    cameraNode.rotation = Quaternion(pitch, yaw, 0.0f);

    // Read WASD keys and move the camera scene node to the corresponding direction if they are pressed
    // Use the Translate() function (default local space) to move relative to the node's orientation.
    if (input.keyDown['W'])
        cameraNode.Translate(Vector3(0.0f, 0.0f, 1.0f) * MOVE_SPEED * timeStep);
    if (input.keyDown['S'])
        cameraNode.Translate(Vector3(0.0f, 0.0f, -1.0f) * MOVE_SPEED * timeStep);
    if (input.keyDown['A'])
        cameraNode.Translate(Vector3(-1.0f, 0.0f, 0.0f) * MOVE_SPEED * timeStep);
    if (input.keyDown['D'])
        cameraNode.Translate(Vector3(1.0f, 0.0f, 0.0f) * MOVE_SPEED * timeStep);
}

void SubscribeToEvents(){
    SubscribeToEvent("Update", "HandleUpdate");
}

void HandleUpdate(StringHash eventType, VariantMap& eventData){
    // Take the frame time step, which is stored as a float
    float timeStep = eventData["TimeStep"].GetFloat();

    // Move the camera, scale movement with time step
    MoveCamera(timeStep);
}

class Rotator : ScriptObject
{
    Vector3 rotationSpeed;

    // Update is called during the variable timestep scene update
    void Update(float timeStep)
    {
        node.Rotate(Quaternion(rotationSpeed.x * timeStep, rotationSpeed.y * timeStep, rotationSpeed.z * timeStep));
    }
}

// Create XML patch instructions for screen joystick layout specific to this sample app
String patchInstructions = "";

[/code]

That's it.
I have worked on it since, and I had to change some names back. so hopefully if you copy and paste it still jsut works.

But the other files, the render path and the techniques, as you can see from the paths, i had in subfolders called "research" in the actual "CoreData" folders.
So /CoreData/techniques/research/simple/xml
/CoreData/RenderPath/research/Forward.xml
etc

I will try and actually make a more basic lesson, with files in the near future as I think it will be helpful for anyone trying to figure this stuff out.

-------------------------

sabotage3d | 2017-01-02 01:02:13 UTC | #5

Thanks it works nice the only thing that seems changed is the this variable [b]ObjectColor [/b] it is missing in the shader.
Where should I add it to get the random color ?

-------------------------

ghidra | 2017-01-02 01:02:13 UTC | #6

In the material xml
[code]
<material>
    <technique name="Techniques/research/simple.xml" />
    <parameter name="ObjectColor" value="1.0 1.0 1.0 16" />
</material>
[/code]
I knew i would miss something, hopefully that takes care of it.

-------------------------

sabotage3d | 2017-01-02 01:02:14 UTC | #7

I think it is missing in the shader as well ?

-------------------------

ghidra | 2017-01-02 01:02:16 UTC | #8

out of curiosity, are you using windows. I noticed that some of my links were weird on my windows box trying to get this to work... Again, at some point in the enar future, I will just put together something simple that I can just hand out as a zip file.

-------------------------

