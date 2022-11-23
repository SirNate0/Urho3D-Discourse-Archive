vivienneanthony | 2017-01-02 00:59:55 UTC | #1

Hello

So, I created a basic client ui with a scene loader. I'm trying to figure out the best way to setup the character.

I would like to program a dynamic worldspace environment of objects. Each object has the typical coordinates information but can be of any subtype being one a character. So, a scene has 100 objects that interact either NPC(enemy or ally), another player, concrete wall, and so on. Additionally some objects are in objects.

The thing with Urho3D. Do I make the structure dynamic as a third party integrated code so I can use that code for something else? Also, Where do I setup the code to loop through objects  before a screen update? 

Vivienne

Old Proteus Code
[sourceforge.net/projects/proteu ... oteusCore/](https://sourceforge.net/projects/proteusgameengine/files/ProteusCore/)

Existence Code
[sourceforge.net/projects/proteu ... Existence/](https://sourceforge.net/projects/proteusgameengine/files/Existence/)

-------------------------

cadaver | 2017-01-02 00:59:55 UTC | #2

I don't have time to go more into detail, but if you want to do things "Urho3D way" you would have your own Component subclasses for the state information that you want to represent. You then add these into scene nodes in addition with the Urho's inbuilt components that for example do rendering & physics. See the CharacterDemo & VehicleDemo samples that implement a walking character and a car using this approach.

For catching updates, you need to use events. See [urho3d.github.io/documentation/a00013.html](http://urho3d.github.io/documentation/a00013.html) for the events that are transmitted during each frame. Alternatively, if you subclass the LogicComponent helper class, you can directly write an Update() virtual function that will be called each frame. But in that case you're no longer in control of looping through objects to be upated; rather each LogicComponent subscribes to the scene update event on its own to do the update.

-------------------------

vivienneanthony | 2017-01-02 00:59:55 UTC | #3

[quote="cadaver"]I don't have time to go more into detail, but if you want to do things "Urho3D way" you would have your own Component subclasses for the state information that you want to represent. You then add these into scene nodes in addition with the Urho's inbuilt components that for example do rendering & physics. See the CharacterDemo & VehicleDemo samples that implement a walking character and a car using this approach.

For catching updates, you need to use events. See [urho3d.github.io/documentation/a00013.html](http://urho3d.github.io/documentation/a00013.html) for the events that are transmitted during each frame. Alternatively, if you subclass the LogicComponent helper class, you can directly write an Update() virtual function that will be called each frame. But in that case you're no longer in control of looping through objects to be upated; rather each LogicComponent subscribes to the scene update event on its own to do the update.[/quote]

Part A
I am looking over the two examples. I am thinking I'm looking at the future. I'm assuming how there is a PhysicsWorld I would also need to create a PhysicsSpace. The "Urho Way" would be for every node to be like a object of various types. That's the first possible way short term.  I just have to figure out what to do if a object like player moves into a ship and take control of that. Then I somehow have to move that node hierarchy into the ship object node. 

Part B
The latter sounds easier but I'm going have to be able to loop through objects nodes. I guess.

It's going get get super more complicated but trying to figure it out. So, I hope people don't mind the questions.

Note.
It would be nice if the Editor can have muiltiple resource paths.

-------------------------

jmiller | 2017-01-02 00:59:56 UTC | #4

All good sample apps, CharacterDemo shows a bunch of useful things. I'll throw some ideas your way, and hopefully I'm not too far off. :wink:

A.
PhysicsWorld component: It's a scene-level component and only one is allowed, but it can do 'space physics', see SetGravity(vec).
Also, for RigidBody you can SetGravityOverride(vec) or SetUseGravity(bool) so you could have local gravities if you want.

In your example you might have a Character component with related attributes like faction.
If you want to make a node a container: you could have a Container component that reparents (or stores NodeIDs in a vector) the contained nodes and disables/hides them, or stores info to recreate them from scratch and removes them...
Also good to know that components can receive your own custom events, which can simplify things; see EVENT()

B.
I think using LogicComponent should not interfere with you looping through nodes 'normally'. You can also set which events it subscribes to, but if you don't use any of its convenience methods you might as well use Component; it's only a bit more to type. :slight_smile:

-------------------------

vivienneanthony | 2017-01-02 00:59:57 UTC | #5

Fixed!

I'm assuming this code handles the collision. Now I am figuring out how to stop it from going through a terrain or plane. I'm assuming in the function of FixedUpdate. (Edit) I tried to test movement in the handlecollision!

I have to test if the character is below ground then apply a applyimpulse or velocity to count a down movement?

Just in case.

Vivienne

[code]void Character::HandleNodeCollision(StringHash eventType, VariantMap& eventData)
{
    // Check collision contacts and see if character is standing on ground (look for a contact that has near vertical normal)
    using namespace NodeCollision;

    /// Could cache the components for faster access instead of finding them each frame
    RigidBody* body = GetComponent<RigidBody>();

    MemoryBuffer contacts(eventData[P_CONTACTS].GetBuffer());

    while (!contacts.IsEof())
    {
        Vector3 contactPosition = contacts.ReadVector3();
        Vector3 contactNormal = contacts.ReadVector3();
        float contactDistance = contacts.ReadFloat();
        float contactImpulse = contacts.ReadFloat();

        // If contact is below node center and mostly vertical, assume it's a ground contact
        if (contactPosition.y_ < (node_->GetPosition().y_ + 1.0f))
        {
            float level = Abs(contactNormal.y_);
            if (level > 0.90f)
            {
                onGround_ = true;
            }

                     if (node_->GetPosition().y_-contactPosition.y_<0)
            {

                body -> SetLinearVelocity(Vector3(0.0f,-(node_->GetPosition().y_-contactPosition.y_)*2,0.0f));
            }
         

        }
    }
}[/code][/code]

-------------------------

vivienneanthony | 2017-01-02 00:59:57 UTC | #6

Hi,

Maybe someone can give me some insight on this. I should be using the XYZ left hand coordinates(y-up) of the unless I'm incorrect. From the variable dump. It seems to me position is the difference from the last frame. So, it's unclear what I should be testing. I highlighted what I think I should be comparing then reversing the velocity of the node if it's below the contact position??.
[b]
Contact Position is 0.0652326 [color=#FF80FF]-0.100322 [/color]-3.57323 Node is 0.0646458 [color=#FF80FF]-0.10627 [/color]-3.55957 - Character above plane
Contact Position is 0.0916598 -[color=#FF80FF]0.284643[/color]  -3.57257 Node is 0.0646466 [color=#FF80FF]-0.278103 [/color]-3.55957[/b] - [b]Character far below plane[/b]

Hmmmm. 

Vivienne

Matching Code
[code]void Character::HandleNodeCollision(StringHash eventType, VariantMap& eventData)
{
    // Check collision contacts and see if character is standing on ground (look for a contact that has near vertical normal)
    using namespace NodeCollision;

    /// Could cache the components for faster access instead of finding them each frame
    RigidBody* body = GetComponent<RigidBody>();

    MemoryBuffer contacts(eventData[P_CONTACTS].GetBuffer());

    while (!contacts.IsEof())
    {
        Vector3 contactPosition = contacts.ReadVector3();
        Vector3 contactNormal = contacts.ReadVector3();
        float contactDistance = contacts.ReadFloat();
        float contactImpulse = contacts.ReadFloat();
        Vector3 nodePosition = node_->GetPosition();

        // If contact is below node center and mostly vertical, assume it's a ground contact
        if (contactPosition.y_ < (node_->GetPosition().y_ + 1.0f))
        {
            float level = Abs(contactNormal.y_);

            if (level > 0.75)
            {
                onGround_ = true;
            }
        }

        cout << "Contact Position is " << contactPosition.ToString().CString()  << " Node is "<< nodePosition.ToString().CString() << "\r\n";

    }
}[/code]

-------------------------

vivienneanthony | 2017-01-02 00:59:57 UTC | #7

Hello,

I'm stumped on this. I tried using reverse direction using ApplyForce and/or ApplyImpulse using the difference between node.y_ and body.y_ but it's not working.

Maybe someone can tell me if I'm wrong. If I am using various surfaces like terrain or plane. Should I be testing the normal location of the plane or terrain, testing if the body location is below it then reposition slightly above then do a reverse apply force.

I think I might making it more complicated in my head.

Vivienne

-------------------------

jmiller | 2017-01-02 00:59:58 UTC | #8

If setup like the samples, the physics system should prevent things from falling through, and it applies forces from collisions (like bounce). RigidBody has attributes to set its restitution, friction, etc.

Maybe in your setup stage, you miss a SetCollisionLayer() for your terrain/surfaces/bodies, or do not add that in the editor?

-------------------------

vivienneanthony | 2017-01-02 00:59:58 UTC | #9

[quote="carnalis"]If setup like the samples, the physics system should prevent things from falling through, and it applies forces from collisions (like bounce). RigidBody has attributes to set its restitution, friction, etc.

Maybe in your setup stage, you miss a SetCollisionLayer() for your terrain/surfaces/bodies, or do not add that in the editor?[/quote]

Hi

I doubt it. I'll copied parts of the xml and code to here. When I open the .xml in the editor both says collision layer 1. Maybe I have to manually edit the xml and add the collision layer?

Vivienne

airbike2.xml
[code]	<node id="16777246">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="" />
		<attribute name="Position" value="0 -0.207637 0" />
		<attribute name="Rotation" value="1.37679e-07 -1.37679e-07 0.707107 0.707107" />
		<attribute name="Scale" value="1 1 1" />
		<attribute name="Variables" />
		<component type="StaticModel" id="16777270">
			<attribute name="Model" value="Model;Models/airbrake.plane.mdl" />
			<attribute name="Material" value="Material;Materials/airbrake.plane.xml" />
		</component>
		<component type="CollisionShape" id="16777271">
			<attribute name="Shape Type" value="ConvexHull" />
			<attribute name="Model" value="Model;Models/airbrake.plane.mdl" />
			<attribute name="LOD Level" value="1" />
		</component>
		<component type="RigidBody" id="16777272">
			<attribute name="Physics Rotation" value="1.37679e-07 -1.37679e-07 0.707107 0.707107" />
			<attribute name="Physics Position" value="0 -0.207637 0" />
		</component>
	</node>[/code]

terrain.xml[code]
<node id="16798325">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="Terrain" />
		<attribute name="Position" value="0 0 0" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="1 1 1" />
		<attribute name="Variables" />
		<component type="Terrain" id="16777303">
			<attribute name="Height Map" value="Image;Textures/heightmap2.png" />
			<attribute name="Smooth Height Map" value="true" />
			<attribute name="Is Occluder" value="true" />
			<attribute name="Cast Shadows" value="true" />
		</component>
		<component type="RigidBody" id="16777304">
			<attribute name="Collision Event Mode" value="Always" />
			<attribute name="Use Gravity" value="false" />
		</component>
		<component type="CollisionShape" id="16777305">
			<attribute name="Shape Type" value="Terrain" />
		</component>
	</node>[/code]


Code
[code]void ExistenceClient::CreateCharacter(void)
{
    // get resources
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    Renderer* renderer = GetSubsystem<Renderer>();
    Graphics* graphics = GetSubsystem<Graphics>();
    UI* ui = GetSubsystem<UI>();
    FileSystem * filesystem = GetSubsystem<FileSystem>();

    //String characternode = String("Character");
    LoadCharacterMesh("Character",1,1);

    Node* objectNode = scene_->GetChild("Character");

    // Create rigidbody, and set non-zero mass so that the body becomes dynamic
    RigidBody* body = objectNode->CreateComponent<RigidBody>();
    body->SetCollisionLayer(1);
    body->SetMass(.2f);

    // Set zero angular factor so that physics doesn't turn the character on its own.
    // Instead we will control the character yaw manually
    body->SetAngularFactor(Vector3::ZERO);

    // Set the rigidbody to signal collision also when in rest, so that we get ground collisions properly
    body->SetCollisionEventMode(COLLISION_ALWAYS);

    // Set a capsule shape for collision
    CollisionShape* shape = objectNode->CreateComponent<CollisionShape>();
    //shape->SetConvexHull(cache->GetResource<Model>("Resources/Models/standardfemale:Body.mdl"));
    shape->SetBox(Vector3::ZERO);
    shape->SetLodLevel(1);

    character_ = objectNode->CreateComponent<Character>();

    // Create a scene node for the camera, which we will move around
    // The camera will use default settings (1000 far clip distance, 45 degrees FOV, set aspect ratio automatically)
    Node * cameraNode_ = objectNode ->CreateChild("CameraFirstPerson");

    // Set an initial position for the camera scene node above the plane
    cameraNode_->SetPosition(Vector3(0.0f,0.1f,-0.185821f));
    cameraNode_->SetRotation(Quaternion(0.0,-180.0,0.0));

    Camera* cameraObject = cameraNode_->CreateComponent<Camera>();
    cameraObject->SetOrthographic(0);
    cameraObject->SetZoom(1);

    ExistenceGameState.SetCameraMode(CAMERAMODE_FIRSTPERSON);

    // Set up a viewport to the Renderer subsystem so that the 3D scene can be seen. We need to define the scene and the camera
    // at minimum. Additionally we could configure the viewport screen size and the rendering path (eg. forward / deferred) to
    // use, but now we just use full screen and default render path configured	SetOrthographic ( in the engine command line options
    //viewport -> SetCamera(cameraObject);

    SharedPtr<Viewport> viewport(new Viewport(context_, scene_, cameraObject));
    renderer->SetViewport(0, viewport);




    return;
}[/code]

-------------------------

jmiller | 2017-01-02 00:59:58 UTC | #10

[quote="vivienneanthony"][code]
    shape->SetBox(Vector3::ZERO);
[/code][/quote]

CollisionShape needs volume to collide; try Vector3::ONE or whatever?

-------------------------

vivienneanthony | 2017-01-02 00:59:58 UTC | #11

[quote="carnalis"][quote="vivienneanthony"][code]
    shape->SetBox(Vector3::ZERO);
[/code][/quote]

CollisionShape needs volume to collide; try Vector3::ONE or whatever?[/quote]

Just tried it. It seems to work but will mess with testing some scenes in the morning. Thanks!

I was looking at some major crazy solution and it was just one word.

-------------------------

vivienneanthony | 2017-01-02 00:59:59 UTC | #12

[quote="carnalis"][quote="vivienneanthony"][code]
    shape->SetBox(Vector3::ZERO);
[/code][/quote]

CollisionShape needs volume to collide; try Vector3::ONE or whatever?[/quote]

I placed a new video log on Youtube.  I am thinking it works now. I just need to make the collison bound better.

 [www.youtube.com/watch?v=vcFBM_5I_C4&lis ... 7uTgUBQjaw](http://www.youtube.com/watch?v=vcFBM_5I_C4&list=UUTObP1VzcIglm7uTgUBQjaw)

-------------------------

