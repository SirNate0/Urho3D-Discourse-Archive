sovereign313 | 2017-01-02 01:09:29 UTC | #1

Hi,

So I'm building an FPS game.  I got help recently with putting an object into the scene by attaching it to the camera.  This worked wonderfully, but I'm having trouble stopping the camera from falling through the ground.  I've tried this two ways:

1) create a rigidbody (and collision object) on the camera node.
2) create a 'mainNode' and attach the camera to the main node, and attach a rigidbody / collisionbody to the main node.

Either way, I still fall through the ground.  I use the default heightmap and terrain.xml.  Here is the relevant code:

[b]The Terrain[/b]
[code]
    Node* terrainNode = scene_->CreateChild("Terrain");
    terrainNode->SetPosition(Vector3(0.0f, 0.0f, 0.0f));
    Terrain* terrain = terrainNode->CreateComponent<Terrain>();
    terrain->SetPatchSize(64);
    terrain->SetSpacing(Vector3(2.0f, 0.5f, 2.0f)); // Spacing between vertices and vertical resolution of the height map
    terrain->SetSmoothing(true);
    terrain->SetHeightMap(cache->GetResource<Image>("Textures/HeightMap.png"));
    terrain->SetMaterial(cache->GetResource<Material>("Materials/Terrain.xml"));
    // The terrain consists of large triangles, which fits well for occlusion rendering, as a hill can occlude all
    // terrain patches and other objects behind it
    terrain->SetOccluder(true);

    RigidBody *body = terrainNode->CreateComponent<RigidBody>();
    body->SetCollisionLayer(2);
    CollisionShape *shape = terrainNode->CreateComponent<CollisionShape>();
    shape->SetTerrain();
[/code]

[b]The Camera/Mainnode[/b]
[code]
    Node* mainNode = scene_->CreateChild("MainNode");
    mainNode->SetScale(1.0f);

    // Camera Stuff
    cameraNode_ = mainNode->CreateChild("Camera");
    Camera* camera = cameraNode_->CreateComponent<Camera>();
    camera->SetFarClip(750.0f);
    cameraNode_->SetPosition(Vector3(0.0f, 27.0f, -10.0f));

    // Add Our Gun
    Node* actorNode = cameraNode_->CreateChild("Actor");
    AnimatedModel *actor = actorNode->CreateComponent<AnimatedModel>();
    actor->SetModel(cache->GetResource<Model>("Models/compact_handgun.mdl"));
    actor->SetMaterial(cache->GetResource<Material>("Materials/Stone.xml"));
    actor->SetCastShadows(true);
    actorNode->SetScale(Vector3(0.0005f, 0.0005f, 0.0005f));
    actorNode->SetPosition(Vector3(0.2f, -0.1f, 0.5f));
    actorNode->SetRotation(Quaternion(5, 185, 0));

    RigidBody *cambody = mainNode->CreateComponent<RigidBody>();
    cambody->SetUseGravity(true);
    cambody->SetCollisionLayer(2);
    cambody->SetMass(1.0f);

    CollisionShape *camshape = mainNode->CreateComponent<CollisionShape>();
    shape->SetSphere(15.0f);
[/code]

I can actually see the sphere wire frame (debug is on) in the camera, but it's supposed to be a part of the node that the camera is actually attached to as well.

-------------------------

