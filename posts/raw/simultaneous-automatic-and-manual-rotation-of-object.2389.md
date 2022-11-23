OMID-313 | 2017-01-02 01:15:07 UTC | #1

Hi all,

I want to set up a scene, where a model is rotating automatically. Besides, the user will be able to rotate the model manually by mouse movement.
In other words, the total rotation will be the "automatic rotation + mouse rotation".

The following is the code I've written:

[code]#include "Scripts/Utilities/Sample.as"

Node@ mushroomNode;

void Start()
{
    SampleStart();
    CreateScene();
    SetupViewport();
    SubscribeToEvents();
}

void CreateScene()
{
    scene_ = Scene();

    scene_.CreateComponent("Octree");

    Node@ lightNode = scene_.CreateChild("DirectionalLight");
    lightNode.direction = Vector3(0.6f, -1.0f, 0.8f); // The direction vector does not need to be normalized
    Light@ light = lightNode.CreateComponent("Light");
    light.lightType = LIGHT_DIRECTIONAL;

        mushroomNode = scene_.CreateChild("Mushroom");
        mushroomNode.position = Vector3(0.0f, 0.0f, 300.0f);
        mushroomNode.rotation = Quaternion(0.0f, 0.0f, 0.0f);
        mushroomNode.SetScale(0.5f);
        StaticModel@ mushroomObject = mushroomNode.CreateComponent("StaticModel");
        mushroomObject.model = cache.GetResource("Model", "3D_Models/Shoe_2.mdl");
        mushroomObject.ApplyMaterialList();

        ScriptInstance@ instance = mushroomNode.CreateComponent("ScriptInstance");
        instance.CreateObject(scriptFile, "Rotator");
        Rotator@ rotator = cast<Rotator>(instance.scriptObject);
        rotator.rotationSpeed = Vector3(10.0f, 20.0f, 30.0f);

    cameraNode = scene_.CreateChild("Camera");
    cameraNode.CreateComponent("Camera");

    cameraNode.position = Vector3(0.0f, 30.0f, 0.0f);
}

void SetupViewport()
{
    Viewport@ viewport = Viewport(scene_, cameraNode.GetComponent("Camera"));
    renderer.viewports[0] = viewport;
}

void MoveCamera(float timeStep)
// this function moves the object, not the camera. Only its name is camera !!
{
    if (ui.focusElement !is null)
        return;

    const float MOVE_SPEED = 10.0f;
    const float MOUSE_SENSITIVITY = 0.05f;

    IntVector2 mouseMove = input.mouseMove;
    yaw += MOUSE_SENSITIVITY * mouseMove.x;
    pitch += MOUSE_SENSITIVITY * mouseMove.y;
    pitch = Clamp(pitch, -90.0f, 90.0f);

     mushroomNode.rotation = Quaternion(pitch, yaw, 0.0f);

    if (input.keyDown['W'])
        cameraNode.Translate(Vector3(0.0f, -5.0f, 0.0f) * MOVE_SPEED * timeStep);
    if (input.keyDown['S'])
        cameraNode.Translate(Vector3(0.0f, 5.0f, 0.0f) * MOVE_SPEED * timeStep);
    if (input.keyDown['A'])
        cameraNode.Translate(Vector3(5.0f, 0.0f, 0.0f) * MOVE_SPEED * timeStep);
    if (input.keyDown['D'])
        cameraNode.Translate(Vector3(-5.0f, 0.0f, 0.0f) * MOVE_SPEED * timeStep);
    if (input.keyDown['Q'])
        cameraNode.Translate(Vector3(0.0f, 0.0f, -5.0f) * MOVE_SPEED * timeStep);
    if (input.keyDown['E'])
        cameraNode.Translate(Vector3(0.0f, 0.0f, 5.0f) * MOVE_SPEED * timeStep);
}

void SubscribeToEvents()
{
    SubscribeToEvent("Update", "HandleUpdate");
}

void HandleUpdate(StringHash eventType, VariantMap& eventData)
{
    float timeStep = eventData["TimeStep"].GetFloat();
    MoveCamera(timeStep);
}


class Rotator : ScriptObject
{
        Vector3 rotationSpeed;

        void Update(float timeStep)
        {
                node.Rotate(Quaternion(rotationSpeed.x * timeStep, rotationSpeed.y * timeStep, rotationSpeed.z$
        }
}

String patchInstructions = "";[/code]

But unfortunately, it doesn't rotate the object automatically.
But if I comment out the following line:
[code]mushroomNode.rotation = Quaternion(pitch, yaw, 0.0f);[/code]
which is responsible for rotating the object by mouse, it works.
It means that either automatic or manual rotation works, but not both at the same time.

How can I make them both work at the same time !!?

-------------------------

1vanK | 2017-01-02 01:15:07 UTC | #2

"Rotator" rotate object but after that you rewrite rotation by "mushroomNode.rotation". You need use "node.Rotate()" instead "node.rotation".

-------------------------

OMID-313 | 2017-01-02 01:15:07 UTC | #3

[quote="1vanK"]"Rotator" rotate object but after that you rewrite rotation by "mushroomNode.rotation". You need use "node.Rotate()" instead "node.rotation".[/quote]

Thanks @1vanK for your reply.
This solved my problem  :wink:

-------------------------

