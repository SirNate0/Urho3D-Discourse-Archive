Andy51 | 2017-01-02 00:57:52 UTC | #1

Hi everyone!

I've been messing around the engine for a few days trying to get a simple moving platform/elevator to work, and eventually found out kinematic rigid bodies just does not work right.
I have a setup with a kinematic rigid body and a script attached that moves it around, and a dynamic body placed on top. So that body begins constatly bouncing from the platform when the platform moves down, or "sinking" in when going up. The same scene build in the clean Bullet 2.82 works perfectly fine, at least it seems so.

In the end I found that the body's interpolation position is messed in RigidBody::SetPosition, thus negating the velocity approximation by the physics engine and causing movement artifacts with kinematic objects when controlled externally (and they are actually meant for that). I end up with a workaround
[pastebin]xRtXZewQ[/pastebin]

I kind of understand why this was made, but this seriously breaks the kinematic objects. I suppose there should be some more solid solution though.
BTW, why do we want to update inertia tensor on position change?

Here's the test scene:
<removed "as an anti-spam measure, sorry">

-------------------------

Andy51 | 2017-01-02 00:57:52 UTC | #2

Test scene. Why do i have to make a second post just for that? [size=70][color=#FF0000]New users cannot edit post. cin[/color][/size]
[rghost.ru/download/52328170/4c4a ... ifttest.7z](http://rghost.ru/download/52328170/4c4ab0745a64353618a02adc37569addd5e66631/lifttest.7z)

-------------------------

cadaver | 2017-01-02 00:57:53 UTC | #3

Thanks. This change has been pushed to github.

-------------------------

Andy51 | 2017-01-02 00:57:53 UTC | #4

Well, since this is just a workaround, i thought there might be a better solution, since this one could probably cause jittering again at step zero. Not sure though. And another strange thing: the platform itself still jitter a bit when moving, you can clearly see that when stepping as a first person character on the platform. I was able to completely get rid of it by disabling interpolation in physicsWorld, but still... Any ideas?

-------------------------

cadaver | 2017-01-02 00:57:53 UTC | #5

You should get rid of the rendering jitter by only modifying the kinematic object's position in FixedUpdate(), so that it's called at the same frequency as physics world simulation steps.

-------------------------

Andy51 | 2017-01-02 00:57:53 UTC | #6

Right now i am updating it in PhysicsPreStep. Is it incorrect? Tried FixedUpdate with 60 FPS, result is essentially the same

-------------------------

cadaver | 2017-01-02 00:57:53 UTC | #7

PhysicsPreStep is the same as FixedUpdate.

Went through Bullet documentation and found out that for kinematic rigidbodies, we should not update the rigidbody transform from the scene node. Instead Bullet will continuously ask for it. This change has been pushed. So now you should be able to set the scene node position in Update() and the animation will be smooth. I noticed however that the cube bounced differently if the lift animation is done in Update() versus FixedUpdate(), that happens (I assume) because we're now basically moving the scene node with higher frequency than Bullet keeps track of.

-------------------------

Andy51 | 2017-01-02 00:57:53 UTC | #8

Oops, i somehow did not realize we were actually changing the world transfromation of the body itself there. So, yeah, i like the new patch much better. Thank you for quick response!
And i still believe updateInertiaTensor is not needed in SetPosition, because it does not depend on body position, as far as i can see

-------------------------

cadaver | 2017-01-02 00:57:54 UTC | #9

Checked the code and you're right, it only uses the rotation when calculating the inertia.

-------------------------

Mike | 2017-01-02 01:07:34 UTC | #10

[quote]So now you should be able to set the scene node position in Update() and the animation will be smooth. I noticed however that the cube bounced differently if the lift animation is done in Update() versus FixedUpdate(), that happens (I assume) because we're now basically moving the scene node with higher frequency than Bullet keeps track of.[/quote]
When using ValueAnimation to control a node position:
- when overriding node's height in Update or PostUpdate, body position is not synched
- when using FixedUpdate or FixedPostUpdate, everything is fine

[spoiler][code]
#include "Scripts/Utilities/Sample.as"

void Start()
{
    SampleStart();
    CreateScene();
    SubscribeToEvents();
}

void CreateScene()
{
    scene_ = Scene();
    scene_.CreateComponent("Octree");
    scene_.CreateComponent("PhysicsWorld");
    scene_.CreateComponent("DebugRenderer");

    // FLOOR
    Node@ planeNode = scene_.CreateChild("Plane");
    planeNode.scale = Vector3(100.0f, 1.0f, 100.0f);
    StaticModel@ planeObject = planeNode.CreateComponent("StaticModel");
    planeObject.model = cache.GetResource("Model", "Models/Plane.mdl");
    planeObject.material = cache.GetResource("Material", "Materials/StoneTiled.xml");

    // LIGHT
    Node@ lightNode = scene_.CreateChild("DirectionalLight");
    lightNode.direction = Vector3(0.6f, -1.0f, 0.8f); // The direction vector does not need to be normalized
    Light@ light = lightNode.CreateComponent("Light");
    light.lightType = LIGHT_DIRECTIONAL;

    // MUSHROOMS
    for (uint i = 0; i < 200; ++i)
    {
        Node@ mushroomNode = scene_.CreateChild("Mushroom");
        StaticModel@ mushroomObject = mushroomNode.CreateComponent("StaticModel");
        mushroomObject.model = cache.GetResource("Model", "Models/Mushroom.mdl");
        mushroomObject.material = cache.GetResource("Material", "Materials/Mushroom.xml"); // Apply Vegetation Windy shader
        mushroomNode.position = Vector3(Random(90.0f) - 45.0f, 2.0f, Random(90.0f) - 45.0f);
        mushroomNode.rotation = Quaternion(0.0f, Random(360.0f), 0.0f);
        mushroomNode.SetScale(0.5f + Random(2.0f));
    }

    // CAMERA
    cameraNode = scene_.CreateChild("Camera");
    Camera@ camera = cameraNode.CreateComponent("Camera");
    cameraNode.SetTransform(Vector3(0.0f, 120.0f, 0.0f), Quaternion(90.0f, 0.0f, 0.0f));
    renderer.viewports[0] = Viewport(scene_, camera);

    // Moving cube
    Node@ boxNode = scene_.CreateChild("MovingCube");
    boxNode.position = Vector3(0.0f, 2.0f, 0.0f);
    boxNode.SetScale(10.0f);
    StaticModel@ boxObject = boxNode.CreateComponent("StaticModel");
    boxObject.model = cache.GetResource("Model", "Models/Box.mdl");
    boxObject.material = cache.GetResource("Material", "Materials/StoneEnvMapSmall.xml");

    // Create physics components
    RigidBody@ body = boxNode.CreateComponent("RigidBody");
    body.friction = 0.75f;
    CollisionShape@ shape = boxNode.CreateComponent("CollisionShape");
    shape.SetBox(Vector3(1.0f, 1.0f, 1.0f));
    body.kinematic = true;

    // Create node position animation
    ValueAnimation@ animation = ValueAnimation("PositionAnimation");
    animation.interpolationMethod = IM_SPLINE; // Use spline interpolation method
    animation.splineTension = 0.7f; // Set spline tension
    animation.SetKeyFrame(0.0f, Variant(Vector3(-30.0f, 25.0f, -30.0f)));
    animation.SetKeyFrame(1.0f, Variant(Vector3( 30.0f, 25.0f, -30.0f)));
    animation.SetKeyFrame(2.0f, Variant(Vector3( 30.0f, 25.0f,  30.0f)));
    animation.SetKeyFrame(3.0f, Variant(Vector3(-30.0f, 25.0f,  30.0f)));
    animation.SetKeyFrame(4.0f, Variant(Vector3(-30.0f, 25.0f, -30.0f)));
    boxNode.SetAttributeAnimation("Position", animation);
}

void SubscribeToEvents()
{
    SubscribeToEvent("Update", "HandleUpdate");
    SubscribeToEvent("PostUpdate", "HandlePostUpdate");
    SubscribeToEvent("PostRenderUpdate", "HandlePostRenderUpdate");
}

void HandleUpdate(StringHash eventType, VariantMap& eventData)
{
    // Load/Save
    if (input.keyPress[KEY_F5])
    {
        File saveFile(fileSystem.programDir + "Data/Scenes/04_StaticScene.xml", FILE_WRITE);
        scene_.SaveXML(saveFile);
    }
    if (input.keyPress[KEY_F7])
    {
        File loadFile(fileSystem.programDir + "Data/Scenes/04_StaticScene.xml", FILE_READ);
        scene_.LoadXML(loadFile);
    }

    // Toggle debug geometry with space
    if (input.keyPress[KEY_SPACE])
        drawDebug = !drawDebug;
}

void HandlePostUpdate(StringHash eventType, VariantMap& eventData)
{
    Node@ node = scene_.GetChild("MovingCube", true);
    if (node is null)
        return;
    Vector3 pos = node.position;
    pos.y = -2.0f;
    node.position = pos;
}

void HandlePostRenderUpdate(StringHash eventType, VariantMap& eventData)
{
    scene_.physicsWorld.DrawDebugGeometry(true);
}

// Create XML patch instructions for screen joystick layout specific to this sample app
String patchInstructions = "";
[/code][/spoiler]

-------------------------

