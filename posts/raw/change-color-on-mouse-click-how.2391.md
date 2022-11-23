OMID-313 | 2017-01-02 01:15:08 UTC | #1

Hi all,

I want to change the color of a model when the user right clicks on mouse.

The following is my code:

[code]#include "Scripts/Utilities/Sample.as"

Node@ mushroomNode;
StaticModel@ mushroomObject;
Material@ My_Mat;
ValueAnimation@ My_Color;

bool My_Click = false;
bool My_Click2 = false;
int Clk = 1;


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
    light.brightness = 2.0f;

        My_Mat = cache.GetResource("Material", "Materials/wire_255013019.xml");
        My_Color = ValueAnimation();

                mushroomNode = scene_.CreateChild("Mushroom");

                        mushroomNode.position = Vector3(0.0f, 0.0f, 300.0f);

                mushroomNode.rotation = Quaternion(0.0f, 0.0f, 0.0f);
                mushroomNode.SetScale(0.5f);
                mushroomObject = mushroomNode.CreateComponent("StaticModel");

                mushroomObject.model = cache.GetResource("Model", "3D_Models/Shoe_3.mdl");
                mushroomObject.ApplyMaterialList();

        ScriptInstance@ instance = mushroomNode.CreateComponent("ScriptInstance");
        instance.CreateObject(scriptFile, "Rotator");
        Rotator@ rotator = cast<Rotator>(instance.scriptObject);
        rotator.rotationSpeed = Vector3(10.0f, 10.0f, 10.0f);


    cameraNode = scene_.CreateChild("Camera");
    cameraNode.CreateComponent("Camera");
    cameraNode.position = Vector3(0.0f, 20.0f, 0.0f);
}

void SetupViewport()
{
    Viewport@ viewport = Viewport(scene_, cameraNode.GetComponent("Camera"));
    renderer.viewports[0] = viewport;
}

void MoveCamera(float timeStep)
{
    if (ui.focusElement !is null)
        return;

    const float MOVE_SPEED = 10.0f;
    const float MOUSE_SENSITIVITY = 0.05f;

    IntVector2 mouseMove = input.mouseMove;
    yaw += MOUSE_SENSITIVITY * mouseMove.x;
    pitch += MOUSE_SENSITIVITY * mouseMove.y;
    pitch = Clamp(pitch, -90.0f, 90.0f);
        mushroomNode.Rotate(Quaternion(MOUSE_SENSITIVITY * mouseMove.x, MOUSE_SENSITIVITY * mouseMove.y, 0.0f));

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

    if (input.keyDown['Z'])
        mushroomNode.position = Vector3(0.0f, 0.0f, 400.0f);
    if (input.keyDown['X'])
        mushroomNode.position = Vector3(0.0f, 0.0f, 500.0f);


        if (input.mouseButtonPress[MOUSEB_LEFT])
        {
                My_Click = !My_Click;
                if (My_Click)
                        Clk = 0;
                else
                        Clk = 1;
        }


        if (input.mouseButtonPress[MOUSEB_RIGHT])
        {
                My_Click2 = !My_Click2;
                if (My_Click2)
                        My_Color.SetKeyFrame(0.0f, Variant(Color(0.0f, 0.0f, 0.1f, 1.0f)));
                else
                        My_Color.SetKeyFrame(0.0f, Variant(Color(1.0f, 0.0f, 0.1f, 1.0f)));

                mushroomObject.model = cache.GetResource("Model", "3D_Models/Shoe_3.mdl");
                My_Mat.SetShaderParameterAnimation("MatDiffColor", My_Color);
                mushroomObject.ApplyMaterialList();
        }


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
                node.Rotate(Quaternion(rotationSpeed.x * timeStep * Clk, rotationSpeed.y * timeStep * Clk, rotationSpeed.z *$
        }
}


String patchInstructions = "";[/code]

Everything works fine, but the color doesn't change on right click.
What is the problem !!?

-------------------------

Dave82 | 2017-01-02 01:15:08 UTC | #2

At first look you never apply your material to your StaticModel

[code]mushroomObject.SetMaterial(My_Mat);[/code]

-------------------------

OMID-313 | 2017-01-02 01:15:08 UTC | #3

[quote="Dave82"]At first look you never apply your material to your StaticModel

[code]mushroomObject.SetMaterial(My_Mat);[/code][/quote]

I have imported this .obj model by AssetImporter. It creates a .txt file containing the list of 3 .xml material files.
So, I apply the materials with :
[code]mushroomObject.ApplyMaterialList();[/code]

But I want to change only one of those .xml material files.

So, what should I do !!?

-------------------------

Mike | 2017-01-02 01:15:08 UTC | #4

Have a look at ValueAnimation documentation and samples 30_LightAnimation/31_MaterialAnimation. Then ponder if it actually suits your needs.
If not, simply get your material and modify its color:
[code]My_Mat.shaderParameters["MatEmissiveColor"] = Variant(Color(0.0f, 0.0f, 1.0f, 1.0f));[/code]

-------------------------

OMID-313 | 2017-01-02 01:15:08 UTC | #5

[quote="Mike"]Have a look at ValueAnimation documentation and samples 30_LightAnimation/31_MaterialAnimation. Then ponder if it actually suits your needs.
If not, simply get your material and modify its color:
[code]My_Mat.shaderParameters["MatEmissiveColor"] = Variant(Color(0.0f, 0.0f, 1.0f, 1.0f));[/code][/quote]

Thanks @Mike for your reply.
I've used sample codes from examples 30 and 31, but no help.

If I use this code:
[code]My_Mat.shaderParameters["MatEmissiveColor"] = Variant(Color(0.0f, 0.0f, 1.0f, 1.0f));[/code]
Do I have to run 
[code]mushroomObject.ApplyMaterialList();[/code]
to be applied !? or not !?

-------------------------

Mike | 2017-01-02 01:15:08 UTC | #6

Calling ApplyMaterialList() once in CreateScene() is enough, calling it after resets the materials, the exact opposite of what you want to achieve (apply new color value).

-------------------------

OMID-313 | 2017-01-02 01:15:08 UTC | #7

[quote="Mike"]Calling ApplyMaterialList() once in CreateScene() is enough, calling it after resets the materials, the exact opposite of what you want to achieve (apply new color value).[/quote]

Thanks @Mike for your reply.
This solved the problem.

-------------------------

