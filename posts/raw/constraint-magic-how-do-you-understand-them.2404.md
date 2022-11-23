slapin | 2017-01-02 01:15:13 UTC | #1

Hi, all!

Trying to approach constraints for half a year now, and can't understand a thing here.
Whatever I do it misbehaves, explodes and malfunction. When I see example made by people it works,
but if I try to modify it it immediately stops working and I can't understand what leads to that.
I read Bullet docs, but these are very sparse and can't shed light on anything, so please don't
reference them to me they won't help. Please provide humane understanding in the matter.

1. Hinge constraint.
What axes do? What is relation between axes? How the axes relate to rigid bodies?
What are limits? Why whatever I set to limits it doesn't change anything?
Why the joint tends to keep the same angle regardless of limits?

2. Cone twist constraint
What are axes do? why cones always point rigid bodies up (depending on axes, but always up)? how can I place
it so that it points to direction I need and twists around angle? Looks like this is not related to axes or limits :frowning:

I was looking for tutorials, but there is basically none, there are a lot of gui tools which use bullet, but
there is no any guide on how to write code to implement constraints.

Is there anyone using constraints here? I'd appreciate any help.

-------------------------

slapin | 2017-01-02 01:15:13 UTC | #2

Or is it better to implement custom Verlet integration? Will it be easier to do and understand?

-------------------------

slapin | 2017-01-02 01:15:13 UTC | #3

This is what I tried to do.

Things go fine this far:
[youtu.be/NX31yE8x1GA](https://youtu.be/NX31yE8x1GA)

I can't make constraint to not turn body over. if node with body is rotated it is turn upside down
by constraint. Is it related to axis locations? How can I make it work?
[youtu.be/GoUm_ZH0_Ds](https://youtu.be/GoUm_ZH0_Ds)

Code:
[code]
Scene@ sc;
Node@ cam_node;
Node@ floorNode;
Node@ box1, box2, box3;
void HandlePostRenderUpdate()
{
    renderer.DrawDebugGeometry(false);
    sc.physicsWorld.DrawDebugGeometry(true);
}

void Start()
{
    graphics.windowTitle = "Pairs";
    engine.maxFps = 60.0;
    sc = Scene();
    sc.CreateComponent("Octree");
    sc.CreateComponent("PhysicsWorld");
    sc.CreateComponent("DebugRenderer");

    cam_node = Node();
    Camera@ camera = cam_node.CreateComponent("Camera");
    cam_node.worldPosition = Vector3(10.0, 5.0, -10.0);
    Quaternion cam_rot;
    cam_rot.FromLookRotation(Vector3(0.0, 0.0, 0.0) - cam_node.worldPosition, Vector3(0.0, 1.0, 0.0));
    cam_node.worldRotation = cam_rot;
    renderer.numViewports = 1;
    renderer.viewports[0] = Viewport(sc, camera);
    Node@ zoneNode = sc.CreateChild("Zone");
    Zone@ zone = zoneNode.CreateComponent("Zone");
    zone.boundingBox = BoundingBox(Vector3(-1000.0f,-10000.0, -1000.0f), Vector3(1000, 499, 1000));
    zone.ambientColor = Color(0.15f, 0.15f, 0.15f);
    zone.fogColor = Color(0.5f, 0.5f, 0.7f);
    zone.fogStart = 300.0f;
    zone.fogEnd = 300.0f;
    Node@ lightNode = sc.CreateChild("DirectionalLight");
    lightNode.direction = Vector3(0.0, -1.0f, 0.0f);
    Light@ light = lightNode.CreateComponent("Light");
    light.lightType = LIGHT_DIRECTIONAL;
    light.castShadows = true;
    light.shadowBias = BiasParameters(0.00025f, 0.5f);
    // Set cascade splits at 10, 50 and 200 world units, fade shadows out at 80% of maximum shadow distance
    light.shadowCascade = CascadeParameters(10.0f, 50.0f, 200.0f, 0.0f, 0.8f);
    light.color = Color(1.0, 1.0, 0.86);

    floorNode = sc.CreateChild("Floor");
    floorNode.position = Vector3(0.0f, -0.5f, 0.0f);
    floorNode.scale = Vector3(400.0f, 1.0f, 400.0f);
    StaticModel@ object = floorNode.CreateComponent("StaticModel");
    object.model = cache.GetResource("Model", "Models/Box.mdl");
    object.material = cache.GetResource("Material", "Materials/Stone.xml");

    RigidBody@ body = floorNode.CreateComponent("RigidBody");
    // Use collision layer bit 2 to mark world scenery. This is what we will raycast against to prevent camera from going
    // inside geometry
    body.collisionLayer = 2;
    CollisionShape@ shape = floorNode.CreateComponent("CollisionShape");
    sc.AddChild(floorNode);
    shape.SetBox(Vector3(1.0f, 1.0f, 1.0f));
    /* Creating ragdoll-like structure */
    box2 = sc.CreateChild("box2");
    box1 = box2.CreateChild("box1");
    box3 = box2.CreateChild("box3");
    box2.worldPosition = Vector3(0.0, 6, 0.0);
    box1.worldPosition = Vector3(0.0, 5, 0.0);
    box3.worldPosition = Vector3(0.0, 7, 0.0);
    box3.rotation = Quaternion(0.0, 0.0, 180.0);
    // Creating boxes
    Array<Node@> boxes = {box1, box2, box3};
    for (int i = 0; i < boxes.length; i++) {
        Node@ box = boxes[i];
        RigidBody@ box_body = box.CreateComponent("RigidBody");
        box_body.mass = 20;
        box_body.collisionLayer = 1;
        box_body.friction = 1;
        box_body.angularDamping = 0.2f;
        box_body.linearDamping = 0.2f;
//        StaticModel@ box_model = box.CreateComponent("StaticModel");
//        box_model.model = cache.GetResource("Model", "Models/Box.mdl");
//        box_model.material = cache.GetResource("Material", "Materials/Stone.xml");
        CollisionShape@ box_shape = box.CreateComponent("CollisionShape");
        // Offset to look more like bone
        box_shape.SetBox(Vector3(1.0, 1.0, 1.0), box.rotation * Vector3(0.0, -0.5, 0.0));
    }
    // Now adding constraints
    Constraint@ box_constraint = box1.CreateComponent("Constraint");
    box_constraint.constraintType = CONSTRAINT_HINGE;
    box_constraint.otherBody = box2.GetComponent("RigidBody");
    // Constraint motion means that body it attaches to moves.
    // This way one can offset constraint to the side of body.
    box_constraint.worldPosition = box1.worldPosition;
    box_constraint.axis = Vector3(1.0, 0.0, 0.0);
    box_constraint.otherAxis = Vector3(1.0, 0.0, 0.0);
    box_constraint.lowLimit = Vector2(-180.0, 0.0);
    box_constraint.highLimit = Vector2(180.0, 0.0);
    box_constraint.disableCollision = true;
    Constraint@ head_constraint = box3.CreateComponent("Constraint");
    head_constraint.constraintType = CONSTRAINT_HINGE;
    head_constraint.otherBody = box2.GetComponent("RigidBody");
    head_constraint.worldPosition = box3.worldPosition;
    head_constraint.axis = Vector3(1.0, 0.0, 0.0);
    head_constraint.otherAxis = Vector3(-1.0, 0.0, 0.0);
    head_constraint.lowLimit = Vector2(180.0, 0.0);
    head_constraint.highLimit = Vector2(-180.0, 0.0);
    head_constraint.disableCollision = true;
}
[/code]

-------------------------

