GodMan | 2021-12-09 23:56:27 UTC | #1

So I use ConvexCast for my AI melee event and damage. How can I visualize what's going on so I can improve their melee attacks. 

    debug = scene_->GetComponent<DebugRenderer>();

	CollisionShape* shape_ = handboneNode->CreateComponent<CollisionShape>();
	shape_->SetBox(Vector3(2.0f,2.0f,2.0f), Vector3::ZERO, Quaternion::IDENTITY);

	PhysicsRaycastResult raycResult;
	auto* physicsWorld = scene_->GetComponent<PhysicsWorld>();

	const Vector3 start = handboneNode->GetWorldPosition();
	const Vector3 end = start + (Vector3::FORWARD * 1.0f);

	physicsWorld->ConvexCast(raycResult, shape_, start, Quaternion::IDENTITY, end, Quaternion::IDENTITY);

	RigidBody* resultBody{ raycResult.body_ };
	Player* _Node;
	int damage = 10;

	if (resultBody)
	{

		Node* resultNode{ resultBody->GetNode() };
		Node* resulttestNode{ resultBody->GetNode() };

		if (_Node = resultNode->GetDerivedComponent<Player>())
		{
			_Node->setHealth(_Node->getHealth() - damage);
		}

	}

-------------------------

SirNate0 | 2021-12-10 03:59:34 UTC | #2

I don't think there's a direct simple way to visualize the collision shape unfortunately. If there is I'd also like to know it, as I also just had a convex cast I wanted to visualize.

That said, I just wanted to ask whether convex cast works for you? For my game I had to write (mainly copy from the bullet library) a bit of code to allow multiple results to be returned as I think the default implementation only returns the first collision. If you'd like, I'll share that later when I'm back at my computer.

-------------------------

GodMan | 2021-12-10 04:30:59 UTC | #3

Well this works for me as my ai only attack the player. Sometimes though if I'm directly in front of the ai and they swipe at the player they miss, but off to the side of them and they never miss. I just wanted to try and visualize what's going on and improve it.

-------------------------

Modanung | 2021-12-10 12:57:33 UTC | #4

During `PostRenderUpdate` call:
```
shape_->DrawDebugGeometry(scene_->GetComponent<DebugRenderer>(), true);
```
You could also tell the `DebugRenderer` to `AddBoundingBox` or `AddTriangleMesh`, with the advantage of being able to draw both ends of the cast.

-------------------------

GodMan | 2021-12-10 16:48:09 UTC | #5

I was waiting for @Modanung to pop in with some code. Thanks man.
I will try this.

-------------------------

GodMan | 2021-12-10 18:53:53 UTC | #6

> You could also tell the `DebugRenderer` to `AddBoundingBox` or `AddTriangleMesh` , with the advantage of being able to draw both ends of the cast.

@Modanung  Do you have an example of what you mean?

-------------------------

Modanung | 2021-12-10 21:12:35 UTC | #7

Something like this:
```
struct MovingBox
{
    Vector3 size_{ 2.0f, 2.0f, 2.0f };
    Vector3 startPos_{};
    Vector3 endPos_{};
    Quaternion startRot_{};
    Quaternion endRot_{};

    void DrawDebug(DebugRenderer* debug, bool depthTest = true)
    {
        const BoundingBox bounds{ -size * .5f, size * .5f };
        debug->AddBoundingBox(bounds, { startPos_, startRot_, 1.f }, Color::Green, depthTest);
        debug->AddBoundingBox(bounds, {   endPos_,   endRot_, 1.f }, Color::Red,   depthTest);
        debug->AddLine(startPos_, endPos_, Color::Yellow, depthTest);
    }
}
```

-------------------------

GodMan | 2021-12-11 01:50:38 UTC | #8

So I modified the code some. I may not be using it as you intended. This is what I am seeing. The Green and Red boxes seem to be the actual area where the collision events occur. I could be wrong though. 

![Screenshot_Fri_Dec_10_19_47_54_2021|690x291](upload://7j8BEKVgtKtQFvzxiRJqJ6GI59u.jpeg)

-------------------------

SirNate0 | 2021-12-12 02:57:44 UTC | #9

The code I mentioned before for multiple convex cast results, in case someone wants it. And I realize now the reason I thought it wasn't possible to draw the collision shapes directly was because my code created the convex bullet collision shapes directly rather than using `Urho3D::CollisionShape`.

```
#include <BulletCollision/CollisionShapes/btSphereShape.h>
#include <Urho3D/Physics/PhysicsWorld.h>
#include <Urho3D/Physics/CollisionShape.h>
#include <Urho3D/ThirdParty/Bullet/BulletCollision/CollisionShapes/btCollisionShape.h>
#include <Urho3D/ThirdParty/Bullet/BulletDynamics/Dynamics/btDiscreteDynamicsWorld.h>
#include <Urho3D/ThirdParty/Bullet/btBulletDynamicsCommon.h>



#include <Urho3D/ThirdParty/Bullet/btBulletCollisionCommon.h>
#include <Urho3D/ThirdParty/Bullet/btBulletDynamicsCommon.h>
#include <Urho3D/Physics/PhysicsUtils.h>


struct AllHitsConvexResultCallback : public btCollisionWorld::ConvexResultCallback
{
    AllHitsConvexResultCallback(const btVector3& rayFromWorld, const btVector3& rayToWorld)
        : m_convexFromWorld(rayFromWorld),
          m_convexToWorld(rayToWorld)
    {
    }

    btAlignedObjectArray<const btCollisionObject*> m_collisionObjects;

    btVector3 m_convexFromWorld;  //used to calculate hitPointWorld from hitFraction
    btVector3 m_convexToWorld;

    btAlignedObjectArray<btVector3> m_hitNormalWorld;
    btAlignedObjectArray<btVector3> m_hitPointWorld;
    btAlignedObjectArray<btScalar> m_hitFractions;


    virtual btScalar addSingleResult(btCollisionWorld::LocalConvexResult& rayResult, bool normalInWorldSpace)
    {
        m_collisionObjects.push_back(rayResult.m_hitCollisionObject);
        btVector3 hitNormalWorld;
        if (normalInWorldSpace)
        {
            hitNormalWorld = rayResult.m_hitNormalLocal;
        }
        else
        {
            ///need to transform normal into worldspace
            hitNormalWorld = rayResult.m_hitCollisionObject->getWorldTransform().getBasis() * rayResult.m_hitNormalLocal;
        }
        m_hitNormalWorld.push_back(hitNormalWorld);
        btVector3 hitPointWorld;
//        hitPointWorld.setInterpolate3(m_rayFromWorld, m_rayToWorld, rayResult.m_hitFraction);
//        m_hitPointWorld.push_back(hitPointWorld);
        m_hitPointWorld.push_back(rayResult.m_hitPointLocal);
        m_hitFractions.push_back(rayResult.m_hitFraction);
        return m_closestHitFraction; // i.e. 1.0
    }
};

namespace Urho3D {

void SphereCastMultiple(PhysicsWorld* pw, Vector<PhysicsRaycastResult>& results, const Ray& ray, float radius, float maxDistance, unsigned collisionMask)
{

    if (maxDistance >= M_INFINITY)
        URHO3D_LOGWARNING("Infinite maxDistance in physics sphere cast is not supported");

    btSphereShape shape(radius);
    Vector3 endPos = ray.origin_ + maxDistance * ray.direction_;

    AllHitsConvexResultCallback
            convexCallback(ToBtVector3(ray.origin_), ToBtVector3(endPos));
    convexCallback.m_collisionFilterGroup = (short)0xffff;
    convexCallback.m_collisionFilterMask = (short)collisionMask;


    pw->GetWorld()->convexSweepTest(&shape, btTransform(btQuaternion::getIdentity(), convexCallback.m_convexFromWorld),
                                    btTransform(btQuaternion::getIdentity(), convexCallback.m_convexToWorld), convexCallback);

    for (unsigned i = 0; (int)i < convexCallback.m_hitFractions.size(); ++i)
    {
        PhysicsRaycastResult result;
        result.body_ = static_cast<RigidBody*>(convexCallback.m_collisionObjects[i]->getUserPointer());
        result.position_ = ToVector3(convexCallback.m_hitPointWorld[i]);
        result.normal_ = ToVector3(convexCallback.m_hitNormalWorld[i]);
        result.distance_ = convexCallback.m_hitFractions[i] * (endPos - ray.origin_).Length();
        result.hitFraction_ = convexCallback.m_hitFractions[i];

        results.Push(result);
    }
}
void ConvexCastMultiple(PhysicsWorld* pw, Vector<PhysicsRaycastResult>& results, const Ray& ray, CollisionShape* shape, float maxDistance, unsigned collisionMask)
{
    if (!pw || !shape)
        return;

    const auto& btShape = shape->GetCollisionShape();
    if (!btShape || !btShape->isConvex())
        return;

    const btConvexShape* btConvex = static_cast<const btConvexShape*>(btShape);
    ConvexCastMultiple(pw,results,ray,btConvex,maxDistance,collisionMask);
}

void ConvexCastMultiple(PhysicsWorld* pw, Vector<PhysicsRaycastResult>& results, const Ray& ray, const btConvexShape* shape, float maxDistance, unsigned collisionMask)
{
    if (!pw || !shape)
        return;

    if (maxDistance >= M_INFINITY)
        URHO3D_LOGWARNING("Infinite maxDistance in physics convex cast is not supported");

    Vector3 endPos = ray.origin_ + maxDistance * ray.direction_;

    AllHitsConvexResultCallback
            convexCallback(ToBtVector3(ray.origin_), ToBtVector3(endPos));
    convexCallback.m_collisionFilterGroup = (short)0xffff;
    convexCallback.m_collisionFilterMask = (short)collisionMask;


    pw->GetWorld()->convexSweepTest(shape, btTransform(btQuaternion::getIdentity(), convexCallback.m_convexFromWorld),
                                    btTransform(btQuaternion::getIdentity(), convexCallback.m_convexToWorld), convexCallback);

    for (unsigned i = 0; (int)i < convexCallback.m_hitFractions.size(); ++i)
    {
        PhysicsRaycastResult result;
        result.body_ = static_cast<RigidBody*>(convexCallback.m_collisionObjects[i]->getUserPointer());
        result.position_ = ToVector3(convexCallback.m_hitPointWorld[i]);
        result.normal_ = ToVector3(convexCallback.m_hitNormalWorld[i]);
        result.distance_ = convexCallback.m_hitFractions[i] * (endPos - ray.origin_).Length();
        result.hitFraction_ = convexCallback.m_hitFractions[i];

        results.Push(result);
    }
}

}
```

-------------------------

Modanung | 2021-12-12 03:33:30 UTC | #10

[quote="SirNate0, post:9, topic:7097"]
And I realize now the reason I thought it wasn’t possible to draw the collision shapes directly was because my code created the convex bullet collision shapes directly rather than using `Urho3D::CollisionShape` .
[/quote]

You should be able to pour those into a `Polyhedron`, which the `DebugRenderer` can draw.

-------------------------

GodMan | 2021-12-12 20:20:02 UTC | #11

Man I suck with the physics API of Urho3d. LOL.

-------------------------

