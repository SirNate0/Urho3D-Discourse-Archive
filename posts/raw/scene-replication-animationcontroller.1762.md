Aramis | 2017-01-02 01:09:56 UTC | #1

Hello!

I'm trying to replicatea a scene, everything is fine, except the animated models.
I've read the Urho's documentation about Network replication ([url]http://urho3d.github.io/documentation/1.5/_network.html[/url]). It basically tells that animations are replicated through AnimationController. I've modified the Character example and the Scene replication to try this out.

I thought  that it would have worked, since in Character example the Jack model uses the animation controller, and it is [b]NOT [/b]created as local (both Jack and the AnimationController can be replicated).

This part of the code shows this:
[code]void CreateCharacter()
{
    characterNode = scene_.CreateChild("Jack");
    AnimatedModel@ object = characterNode.CreateComponent("AnimatedModel");
    object.model = cache.GetResource("Model", "Models/Jack.mdl");
    object.material = cache.GetResource("Material", "Materials/Jack.xml");
    [...]
    characterNode.CreateComponent("AnimationController");
}[/code]


I also tryed to find how it was done in the NinjaSnowWar, I couldn't find where the animationController was created, it was only referenced in Ninja.as.
Also, why it had an index? Is it for the multiple players? 
[code]AnimationController@ animCtrl = node.children[0].GetComponent("AnimationController");[/code]


Here are the two scripts I'm using to test the Animation Replication:

Server.as (Character example with replication server)
[spoiler]#include "Scripts/Utilities/Sample.as"
#include "Scripts/Utilities/Touch.as"

const uint SERVER_PORT = 2345;

const int CTRL_FORWARD = 1;
const int CTRL_BACK = 2;
const int CTRL_LEFT = 4;
const int CTRL_RIGHT = 8;
const int CTRL_JUMP = 16;

const float MOVE_FORCE = 0.8f;
const float INAIR_MOVE_FORCE = 0.02f;
const float BRAKE_FORCE = 0.2f;
const float JUMP_FORCE = 7.0f;
const float YAW_SENSITIVITY = 0.1f;
const float INAIR_THRESHOLD_TIME = 0.1f;
bool firstPerson = false; // First person camera flag

Node@ characterNode;

// Record for each connected client
class Client
{
    Connection@ connection;
    Node@ object;
}
Array<Client> clients;

void Start()
{
    SampleStart();
    CreateScene();
	network.StartServer(SERVER_PORT);
    CreateCharacter();
    SubscribeToEvents();
}

void CreateScene()
{
    scene_ = Scene();
    scene_.CreateComponent("Octree");
    scene_.CreateComponent("PhysicsWorld");

    cameraNode = scene_.CreateChild("CamCam");
    Camera@ camera = cameraNode.CreateComponent("Camera");
    camera.farClip = 300.0f;
    renderer.viewports[0] = Viewport(scene_, camera);

    Node@ zoneNode = scene_.CreateChild("Zone");
    Zone@ zone = zoneNode.CreateComponent("Zone");
    zone.boundingBox = BoundingBox(-1000.0f, 1000.0f);
    zone.ambientColor = Color(0.15f, 0.15f, 0.15f);
    zone.fogColor = Color(0.5f, 0.5f, 0.7f);
    zone.fogStart = 100.0f;
    zone.fogEnd = 300.0f;

    Node@ lightNode = scene_.CreateChild("DirectionalLight");
    lightNode.direction = Vector3(0.6f, -1.0f, 0.8f);
    Light@ light = lightNode.CreateComponent("Light");
    light.lightType = LIGHT_DIRECTIONAL;
    light.castShadows = true;
    light.shadowBias = BiasParameters(0.00025f, 0.5f);
    light.shadowCascade = CascadeParameters(10.0f, 50.0f, 200.0f, 0.0f, 0.8f);

    // Create the floor object
    Node@ floorNode = scene_.CreateChild("Floor");
    floorNode.position = Vector3(0.0f, -0.5f, 0.0f);
    floorNode.scale = Vector3(200.0f, 1.0f, 200.0f);
    StaticModel@ object = floorNode.CreateComponent("StaticModel");
    object.model = cache.GetResource("Model", "Models/Box.mdl");
    object.material = cache.GetResource("Material", "Materials/Stone.xml");

    RigidBody@ body = floorNode.CreateComponent("RigidBody");
    body.collisionLayer = 2;
    CollisionShape@ shape = floorNode.CreateComponent("CollisionShape");
    shape.SetBox(Vector3(1.0f, 1.0f, 1.0f));
}

void CreateCharacter()
{
    characterNode = scene_.CreateChild("Jack");
    characterNode.position = Vector3(0.0f, 1.0f, 0.0f);

    // Create the rendering component + animation controller
    AnimatedModel@ object = characterNode.CreateComponent("AnimatedModel");
    object.model = cache.GetResource("Model", "Models/Jack.mdl");
    object.material = cache.GetResource("Material", "Materials/Jack.xml");
    object.castShadows = true;
    characterNode.CreateComponent("AnimationController");

    // Set the head bone for manual control
    object.skeleton.GetBone("Bip01_Head").animated = false;

    // Create rigidbody, and set non-zero mass so that the body becomes dynamic
    RigidBody@ body = characterNode.CreateComponent("RigidBody");
    body.collisionLayer = 1;
    body.mass = 1.0f;

    // Set zero angular factor so that physics doesn't turn the character on its own.
    // Instead we will control the character yaw manually
    body.angularFactor = Vector3(0.0f, 0.0f, 0.0f);

    // Set the rigidbody to signal collision also when in rest, so that we get ground collisions properly
    body.collisionEventMode = COLLISION_ALWAYS;

    // Set a capsule shape for collision
    CollisionShape@ shape = characterNode.CreateComponent("CollisionShape");
    shape.SetCapsule(0.7f, 1.8f, Vector3(0.0f, 0.9f, 0.0f));

    // Create the character logic object, which takes care of steering the rigidbody
    characterNode.CreateScriptObject(scriptFile, "Character");
}


void SubscribeToEvents()
{
    // Subscribe to Update event for setting the character controls before physics simulation
    SubscribeToEvent("Update", "HandleUpdate");

    // Subscribe to PostUpdate event for updating the camera position after physics simulation
    SubscribeToEvent("PostUpdate", "HandlePostUpdate");

    // Unsubscribe the SceneUpdate event from base class as the camera node is being controlled in HandlePostUpdate() in this sample
    UnsubscribeFromEvent("SceneUpdate");
	
    SubscribeToEvent("ClientConnected", "HandleClientConnected");
    SubscribeToEvent("ClientDisconnected", "HandleClientDisconnected");
}

void HandleUpdate(StringHash eventType, VariantMap& eventData)
{
    if (characterNode is null)
        return;

    Character@ character = cast<Character>(characterNode.scriptObject);
    if (character is null)
        return;

    // Clear previous controls
    character.controls.Set(CTRL_FORWARD | CTRL_BACK | CTRL_LEFT | CTRL_RIGHT | CTRL_JUMP, false);

    // Update controls using touch utility
    if (touchEnabled)
        UpdateTouches(character.controls);

    // Update controls using keys (desktop)
    if (ui.focusElement is null)
    {
        if (touchEnabled || !useGyroscope)
        {
            character.controls.Set(CTRL_FORWARD, input.keyDown['W']);
            character.controls.Set(CTRL_BACK, input.keyDown['S']);
            character.controls.Set(CTRL_LEFT, input.keyDown['A']);
            character.controls.Set(CTRL_RIGHT, input.keyDown['D']);
        }
        character.controls.Set(CTRL_JUMP, input.keyDown[KEY_SPACE]);

        // Add character yaw & pitch from the mouse motion or touch input
        if (touchEnabled)
        {
            for (uint i = 0; i < input.numTouches; ++i)
            {
                TouchState@ state = input.touches[i];
                if (state.touchedElement is null) // Touch on empty space
                {
                    Camera@ camera = cameraNode.GetComponent("Camera");
                    if (camera is null)
                        return;

                    character.controls.yaw += TOUCH_SENSITIVITY * camera.fov / graphics.height * state.delta.x;
                    character.controls.pitch += TOUCH_SENSITIVITY * camera.fov / graphics.height * state.delta.y;
                }
            }
        }
        else
        {
            character.controls.yaw += input.mouseMoveX * YAW_SENSITIVITY;
            character.controls.pitch += input.mouseMoveY * YAW_SENSITIVITY;
        }
        // Limit pitch
        character.controls.pitch = Clamp(character.controls.pitch, -80.0f, 80.0f);
        // Set rotation already here so that it's updated every rendering frame instead of every physics frame
        characterNode.rotation = Quaternion(character.controls.yaw, Vector3(0.0f, 1.0f, 0.0f));

        // Switch between 1st and 3rd person
        if (input.keyPress['F'])
            firstPerson = !firstPerson;

        // Turn on/off gyroscope on mobile platform
        if (input.keyPress['G'])
            useGyroscope = !useGyroscope;

        // Check for loading / saving the scene
        if (input.keyPress[KEY_F5])
        {
            File saveFile(fileSystem.programDir + "Data/Scenes/CharacterDemo.xml", FILE_WRITE);
            scene_.SaveXML(saveFile);
        }
        if (input.keyPress[KEY_F7])
        {
            File loadFile(fileSystem.programDir + "Data/Scenes/CharacterDemo.xml", FILE_READ);
            scene_.LoadXML(loadFile);
            // After loading we have to reacquire the character scene node, as it has been recreated
            // Simply find by name as there's only one of them
            characterNode = scene_.GetChild("Jack", true);
            if (characterNode is null)
                return;
        }
    }
}

void HandlePostUpdate(StringHash eventType, VariantMap& eventData)
{
    if (characterNode is null)
        return;

    Character@ character = cast<Character>(characterNode.scriptObject);
    if (character is null)
        return;

    // Get camera lookat dir from character yaw + pitch
    Quaternion rot = characterNode.rotation;
    Quaternion dir = rot * Quaternion(character.controls.pitch, Vector3(1.0f, 0.0f, 0.0f));

    // Turn head to camera pitch, but limit to avoid unnatural animation
    Node@ headNode = characterNode.GetChild("Bip01_Head", true);
    float limitPitch = Clamp(character.controls.pitch, -45.0f, 45.0f);
    Quaternion headDir = rot * Quaternion(limitPitch, Vector3(1.0f, 0.0f, 0.0f));
    // This could be expanded to look at an arbitrary target, now just look at a point in front
    Vector3 headWorldTarget = headNode.worldPosition + headDir * Vector3(0.0f, 0.0f, 1.0f);
    headNode.LookAt(headWorldTarget, Vector3(0.0f, 1.0f, 0.0f));
    // Correct head orientation because LookAt assumes Z = forward, but the bone has been authored differently (Y = forward)
    headNode.Rotate(Quaternion(0.0f, 90.0f, 90.0f));

    if (firstPerson)
    {
        // First person camera: position to the head bone + offset slightly forward & up
        cameraNode.position = headNode.worldPosition + rot * Vector3(0.0f, 0.15f, 0.2f);
        cameraNode.rotation = dir;
    }
    else
    {
        // Third person camera: position behind the character
        Vector3 aimPoint = characterNode.position + rot * Vector3(0.0f, 1.7f, 0.0f); // You can modify x Vector3 value to translate the fixed character position (indicative range[-2;2])

        // Collide camera ray with static physics objects (layer bitmask 2) to ensure we see the character properly
        Vector3 rayDir = dir * Vector3(0.0f, 0.0f, -1.0f); // For indoor scenes you can use dir * Vector3(0.0, 0.0, -0.5) to prevent camera from crossing the walls
        float rayDistance = cameraDistance;
        PhysicsRaycastResult result = scene_.physicsWorld.RaycastSingle(Ray(aimPoint, rayDir), rayDistance, 2);
        if (result.body !is null)
            rayDistance = Min(rayDistance, result.distance);
        rayDistance = Clamp(rayDistance, CAMERA_MIN_DIST, cameraDistance);

        cameraNode.position = aimPoint + rayDir * rayDistance;
        cameraNode.rotation = dir;
    }
}

class Character : ScriptObject
{
    // Character controls.
    Controls controls;
    // Grounded flag for movement.
    bool onGround = false;
    // Jump flag.
    bool okToJump = true;
    // In air timer. Due to possible physics inaccuracy, character can be off ground for max. 1/10 second and still be allowed to move.
    float inAirTimer = 0.0f;

    void Start()
    {
        SubscribeToEvent(node, "NodeCollision", "HandleNodeCollision");
    }

    void Load(Deserializer& deserializer)
    {
        controls.yaw = deserializer.ReadFloat();
        controls.pitch = deserializer.ReadFloat();
    }

    void Save(Serializer& serializer)
    {
        serializer.WriteFloat(controls.yaw);
        serializer.WriteFloat(controls.pitch);
    }

    void HandleNodeCollision(StringHash eventType, VariantMap& eventData)
    {
        VectorBuffer contacts = eventData["Contacts"].GetBuffer();

        while (!contacts.eof)
        {
            Vector3 contactPosition = contacts.ReadVector3();
            Vector3 contactNormal = contacts.ReadVector3();
            float contactDistance = contacts.ReadFloat();
            float contactImpulse = contacts.ReadFloat();

            // If contact is below node center and mostly vertical, assume it's a ground contact
            if (contactPosition.y < (node.position.y + 1.0f))
            {
                float level = Abs(contactNormal.y);
                if (level > 0.75)
                    onGround = true;
            }
        }
    }

    void FixedUpdate(float timeStep)
    {
        /// \todo Could cache the components for faster access instead of finding them each frame
        RigidBody@ body = node.GetComponent("RigidBody");
        AnimationController@ animCtrl = node.GetComponent("AnimationController");

        // Update the in air timer. Reset if grounded
        if (!onGround)
            inAirTimer += timeStep;
        else
            inAirTimer = 0.0f;
        // When character has been in air less than 1/10 second, it's still interpreted as being on ground
        bool softGrounded = inAirTimer < INAIR_THRESHOLD_TIME;

        // Update movement & animation
        Quaternion rot = node.rotation;
        Vector3 moveDir(0.0f, 0.0f, 0.0f);
        Vector3 velocity = body.linearVelocity;
        // Velocity on the XZ plane
        Vector3 planeVelocity(velocity.x, 0.0f, velocity.z);

        if (controls.IsDown(CTRL_FORWARD))
            moveDir += Vector3(0.0f, 0.0f, 1.0f);
        if (controls.IsDown(CTRL_BACK))
            moveDir += Vector3(0.0f, 0.0f, -1.0f);
        if (controls.IsDown(CTRL_LEFT))
            moveDir += Vector3(-1.0f, 0.0f, 0.0f);
        if (controls.IsDown(CTRL_RIGHT))
            moveDir += Vector3(1.0f, 0.0f, 0.0f);

        // Normalize move vector so that diagonal strafing is not faster
        if (moveDir.lengthSquared > 0.0f)
            moveDir.Normalize();

        // If in air, allow control, but slower than when on ground
        body.ApplyImpulse(rot * moveDir * (softGrounded ? MOVE_FORCE : INAIR_MOVE_FORCE));

        if (softGrounded)
        {
            // When on ground, apply a braking force to limit maximum ground velocity
            Vector3 brakeForce = -planeVelocity * BRAKE_FORCE;
            body.ApplyImpulse(brakeForce);

            // Jump. Must release jump control inbetween jumps
            if (controls.IsDown(CTRL_JUMP))
            {
                if (okToJump)
                {
                    body.ApplyImpulse(Vector3(0.0f, 1.0f, 0.0f) * JUMP_FORCE);
                    okToJump = false;
                }
            }
            else
                okToJump = true;
        }

        // Play walk animation if moving on ground, otherwise fade it out
        if (softGrounded && !moveDir.Equals(Vector3(0.0f, 0.0f, 0.0f)))
            animCtrl.PlayExclusive("Models/Jack_Walk.ani", 0, true, 0.2f);
        else
            animCtrl.Stop("Models/Jack_Walk.ani", 0.2f);
        // Set walk animation speed proportional to velocity
        animCtrl.SetSpeed("Models/Jack_Walk.ani", planeVelocity.length * 0.3f);

        // Reset grounded flag for next frame
        onGround = false;
    }
}


void HandleClientConnected(StringHash eventType, VariantMap& eventData)
{
    Connection@ newConnection = eventData["Connection"].GetPtr();
    newConnection.scene = scene_;
    Client newClient;
    newClient.connection = newConnection;
    clients.Push(newClient);
}

void HandleClientDisconnected(StringHash eventType, VariantMap& eventData)
{
    Connection@ connection = eventData["Connection"].GetPtr();
    for (uint i = 0; i < clients.length; ++i)
    {
        if (clients[i].connection is connection)
        {
            clients.Erase(i);
            break;
        }
    }
}
String patchInstructions = "no.";[/spoiler]


Client.as (just replicates the character demo scene)
[spoiler]#include "Scripts/Utilities/Sample.as"
String patchInstructions = "null";

const uint SERVER_PORT = 2345;

class Client
{
    Connection@ connection;
}

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
    scene_.CreateComponent("Octree", LOCAL);
    scene_.CreateComponent("PhysicsWorld", LOCAL);
	String address;
    address = "localhost";
    network.Connect(address, SERVER_PORT, scene_);
    cameraNode = Node("Camera");
    Camera@ camera =  cameraNode.CreateComponent("Camera");
    camera.farClip = 300.0f;
}
void SetupViewport()
{
    // Set up a viewport to the Renderer subsystem so that the 3D scene can be seen
    Viewport@ viewport = Viewport(scene_, cameraNode.GetComponent("Camera"));
    renderer.viewports[0] = viewport;
}
void SubscribeToEvents()
{
    SubscribeToEvent("Update", "HandleUpdate");
}
void HandleUpdate(StringHash eventType, VariantMap& eventData)
{
	cameraNode.set_position(scene_.GetChild("CamCam").position);
	cameraNode.set_rotation(scene_.GetChild("CamCam").rotation);
}[/spoiler]


To test the script, you need to start the Server.as first then the Client.as. Use this [b].bat[/b] to help test.
[spoiler]start Urho3DPlayer.exe Server.as -w -x 800 -y 600
SLEEP 1000
start Urho3DPlayer.exe Client.as -w -x 700 -y 500[/spoiler]

If you prefer, I've uploaded the entire example (4MB) on my bitbucket. Download it here ->aramis.bitbucket.org/downloads/temp/AnimRep.zip

Best regards,

- Aramis

-------------------------

rasteron | 2019-07-20 13:46:30 UTC | #2

Hey Aramis,

Check out the [b]Ninja.xml[/b] object under [b]/Data/Objects[/b], it is created in that file along with other stuff.

Ninja.xml
[code]	
...	
<component type="AnimationController" id="7">
  <attribute name="Animations" />
</component>
[/code]

[quote]Also, why it had an index? Is it for the multiple players? [/quote]

Yes NSW is multiplayer ready, but this part searches for the animation component starting with node 0. This code is also a good example so your model's default pose is not displayed and load your preferred idle animation instead, as commented there.. :wink: 

[code]
// Start playing the idle animation immediately, even before the first physics update
        AnimationController@ animCtrl = node.children[0].GetComponent("AnimationController");
        animCtrl.PlayExclusive("Models/NinjaSnowWar/Ninja_Idle3.ani", LAYER_MOVE, true);
[/code]

Hope that helps.

-------------------------

