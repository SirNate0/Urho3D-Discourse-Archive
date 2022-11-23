codder | 2017-01-02 01:11:46 UTC | #1

Hello,

I have an issue that I can't fix. I have a 3D ball which I move by applying forces.
The problem is the camera. I can't make it following the ball without rotating.

[code]
void Sample::HandlePostUpdate(StringHash eventType, VariantMap& eventData)
{
    Node* ballNode = objectNode;

    const float CAMERA_MIN_DIST = 1.0f;
    const float CAMERA_INITIAL_DIST = 5.0f;
    const float CAMERA_MAX_DIST = 20.0f;

    Quaternion dir(ballNode->GetRotation().YawAngle(), Vector3::UP);
    dir = dir * Quaternion(yaw_, Vector3::UP);
    dir = dir * Quaternion(pitch_, Vector3::RIGHT);

    Quaternion rot = ballNode->GetRotation();

    Vector3 cameraTargetPos = ballNode->GetPosition() -dir * Vector3(0.0f, 0.0f, 10.f);
    Vector3 cameraStartPos = ballNode->GetPosition();
    
    Ray cameraRay(cameraStartPos, cameraTargetPos - cameraStartPos);
    float cameraRayLength = (cameraTargetPos - cameraStartPos).Length();
    PhysicsRaycastResult result;
    scene_->GetComponent<PhysicsWorld>()->RaycastSingle(result, cameraRay, cameraRayLength, 2);
    if (result.body_)
        cameraTargetPos = cameraStartPos + cameraRay.direction_ * (result.distance_ - 0.5f);

    cameraNode_->SetPosition(cameraTargetPos);
    cameraNode_->SetRotation(dir);
}
[/code]

Controls seems also inverted.
yaw_ and pitch_ are related to the camera.

Trying to get something similar to this:
[youtube.com/watch?v=KAgIJcHNE4s](https://www.youtube.com/watch?v=KAgIJcHNE4s)

-------------------------

magic.lixin | 2017-01-02 01:11:46 UTC | #2

just use Node::LookAt

-------------------------

codder | 2017-01-02 01:11:46 UTC | #3

Solved the problem partially by creating the camera node as subnode and adding an offset to make it behind the ball.
Now the problem is the raycast since the camera have local coords.

Summarizing I have:
-ObjectNode (Global)
-CameraNode (Local coords)
-Camera pitch & yaw

How can I solve raycasting?

-------------------------

weitjong | 2017-01-02 01:11:46 UTC | #4

Have you looked at those Urho3D samples that have camera control? The character demo and vehicle demo, for example. Both use raycast too.

-------------------------

codder | 2017-01-02 01:11:46 UTC | #5

Tried the code from Vehicle sample but since the ball have no constraints (freedom on all axis) the camera rotates when the ball rotate.

-------------------------

cadaver | 2017-01-02 01:11:46 UTC | #6

You should be able to ignore the ball's rotation. Do not even parent to it, just get its world position each frame and calculate camera position backward from it (+ camera direction) according to your mouse look yaw & pitch parameters, and the desired distance.

-------------------------

codder | 2017-01-02 01:11:46 UTC | #7

But how to avoid camera looking inside terrain or other static objects?

-------------------------

cadaver | 2017-01-02 01:11:46 UTC | #8

Change the camera distance (or otherwise the position, however you like) if you get a raycast hit inside scenery. VehicleDemo, CharacterDemo, NinjaSnowWar all do this.

-------------------------

gawag | 2017-01-02 01:11:47 UTC | #9

Some games do also give the camera a collider or make it a full physical object.

I heard from an interesting bug in a RTS game where the camera was a destructible(!) object. When the player looked at an explosion from too close the camera "object" was destroyed and the camera could no longer be moved  :unamused: .

-------------------------

codder | 2017-01-02 01:11:47 UTC | #10

Vehicle demo suffers from the same issue. I replaced the vehicle with a sphere.

You can check by replacing Vehicle script object at the end of 19_VehicleDemo.as
[code]
class Vehicle : ScriptObject
{
    RigidBody@ hullBody;

    // Vehicle controls.
    Controls controls;

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

    void Init()
    {
        // This function is called only from the main program when initially creating the vehicle, not on scene load
        StaticModel@ hullObject = node.CreateComponent("StaticModel");
        hullBody = node.CreateComponent("RigidBody");
        CollisionShape@ hullShape = node.CreateComponent("CollisionShape");

        node.scale = Vector3(1.f, 1.0f, 1.0f);
        hullObject.model = cache.GetResource("Model", "Models/Sphere.mdl");
        hullObject.material = cache.GetResource("Material", "Materials/Stone.xml");
        hullObject.castShadows = true;
        hullShape.SetSphere(1.f);
        hullBody.mass = 5.0f;
        hullBody.linearDamping = 0.2f; // Some air resistance
        hullBody.angularDamping = 0.5f;
        hullBody.collisionLayer = 1;
        hullBody.friction = 5.f;
    }

    void FixedUpdate(float timeStep)
    {
        float newSteering = 0.0f;
        float accelerator = 0.0f;

        if (controls.IsDown(CTRL_FORWARD))
        {
            Quaternion dir(controls.yaw, Vector3(0.0f, 1.0f, 0.0f));
            hullBody.ApplyImpulse(dir * Vector3(0.0f, 0.0f, 1.0f) * .3f);
        }
        if (controls.IsDown(CTRL_BACK))
        {
            Quaternion dir(controls.yaw, Vector3(0.0f, 1.0f, 0.0f));
            hullBody.ApplyImpulse(dir * Vector3(0.0f, 0.0f, -1.0f) * .3f);
        }
        if (controls.IsDown(CTRL_LEFT))
        {
            Quaternion dir(controls.yaw, Vector3(0.0f, 1.0f, 0.0f));
            hullBody.ApplyImpulse(dir * Vector3(-1.0f, 0.0f, 0.0f) * .3f);
        }
        if (controls.IsDown(CTRL_RIGHT))
        {
            Quaternion dir(controls.yaw, Vector3(0.0f, 1.0f, 0.0f));
            hullBody.ApplyImpulse(dir * Vector3(1.0f, 0.0f, 0.0f) * .3f);
        }

        // Apply downforce proportional to velocity
        Vector3 localVelocity = hullBody.rotation.Inverse() * hullBody.linearVelocity;
        hullBody.ApplyForce(hullBody.rotation * Vector3(0.0f, -1.0f, 0.0f) * Abs(localVelocity.z) * DOWN_FORCE);
    }
}
[/code]

-------------------------

