RockRockWhite | 2018-09-12 14:00:50 UTC | #1

(POOR ENGLISH)
I want to realize the pick controls.For example,when I walk to a apple near by,the program create a 
 text whose text is "Press F to pick",and then I press 'F',and pick the apple.I tried to use RaycastSingle() to detect.But I failed. :rofl:  How can I do? Which function should I use?
By the way,how to draw a debug of raycast?

-------------------------

guk_alex | 2018-09-12 14:07:44 UTC | #2

try SphereCast (closest hits by radius) or ConvexCast(provide own shape to detect objects):

    /// Perform a physics world swept sphere test and return the closest hit.
    void SphereCast(PhysicsRaycastResult& result, const Ray& ray, float radius, float maxDistance, unsigned collisionMask = M_MAX_UNSIGNED);
    /// Perform a physics world swept convex test using a user-supplied collision shape and return the first hit.
    void ConvexCast(PhysicsRaycastResult& result, CollisionShape* shape, const Vector3& startPos, const Quaternion& startRot,
        const Vector3& endPos, const Quaternion& endRot, unsigned collisionMask = M_MAX_UNSIGNED);

-------------------------

guk_alex | 2018-09-12 14:17:22 UTC | #3

Also, you can create trigger physic object(SetTrigger to a RigidBody), and then use its collision events to look for objects. I think this method is more elegant than use of ShpereCast every frame.

Here the example:

    SubscribeToEvent(triggerObject, E_NODECOLLISION, [this](auto eventType, auto& eventData) {
        using namespace NodeCollision;

        Node* otherNode = static_cast<Node*>(eventData[P_OTHERNODE].GetPtr());
        // ...
    });

-------------------------

RockRockWhite | 2018-09-13 01:48:35 UTC | #4

Thanks,SphereCast() is what I need! :grinning:  And,how to draw a debug object of SpheraCast?

-------------------------

guk_alex | 2018-09-13 07:47:05 UTC | #5

SphereCast is an operation, not the object, therefore no debug geometry exists for it (but trigger objects have it). In this case you can draw a sphere with same parameters with DebugRenderer yourself.

    void HandlePostRenderUpdate(StringHash eventType, VariantMap & eventData) {
        auto* debug = scene_->GetComponent<DebugRenderer>();
        Sphere sphere(centerPosition, radius);
        debug->AddSphere(sphere, Color::BLUE);
    }

-------------------------

RockRockWhite | 2018-09-13 08:09:48 UTC | #7

Get it .Thank you very much! :slight_smile:

-------------------------

