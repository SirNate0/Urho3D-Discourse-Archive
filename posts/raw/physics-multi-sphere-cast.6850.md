SirNate0 | 2021-05-16 16:34:36 UTC | #1

I needed to be able to get multiple collisions for a sphere cast. There was a brief guide for how to do it somewhere on the bullet forum (basically combine the code from the multi-ray-cast with the code for the sphere-cast). Here is the result:

```
// For the header
void SphereCastMultiple(PhysicsWorld* pw, Vector<PhysicsRaycastResult>& results, const Ray& ray, float radius, float maxDistance, unsigned collisionMask = M_MAX_UNSIGNED);


// In the .cpp file
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

    /// used to calculate hitPointWorld from hitFraction
    btVector3 m_convexFromWorld;        
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
            //need to transform normal into worldspace
            hitNormalWorld = rayResult.m_hitCollisionObject->getWorldTransform().getBasis() * rayResult.m_hitNormalLocal;
        }
        m_hitNormalWorld.push_back(hitNormalWorld);
        btVector3 hitPointWorld;
        m_hitPointWorld.push_back(rayResult.m_hitPointLocal);
        m_hitFractions.push_back(rayResult.m_hitFraction);
        return m_closestHitFraction;     
    }
};


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
```

-------------------------

