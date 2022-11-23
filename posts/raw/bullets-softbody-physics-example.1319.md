Lumak | 2018-04-04 21:16:13 UTC | #1

I became interested in porting bullet's softbody physics after reading Josh's post, [url]http://discourse.urho3d.io/t/soft-body-physics/1313/1[/url].
And the thing that I was really interested in was TriMesh softbody implementation, curious as to whether the softbody needed to be recreated every frame or if just updating the model's vertex buffer would work.
This example shows trimesh softbody implementation that updates model's vertex buffer.  It's no where near code complete, as I have neglected to write methods like settransform(), setmass(), etc., and I coded SoftBody class in PhysicsWorld.h/.cpp for ease of testing.  But I decided to share this as there are others who are more interested in this than myself.

https://youtu.be/XkLMAZWaVB8

Edit: progress update 09/20/15
-This progress is collaborative efforts made by Mike, codingmonkey, and myself - this will eventually make it into the master branch, hopefully.  I found out that there is no way to remove duplicate verts from Blender. So, I wrote a duplicate verts removal (pruning) routine and apply the softbody deformation back to the original model's vertex buffer.  The attached video shows this work.

https://youtu.be/SvdpjhA-Mq8

The lates repo: https://github.com/Lumak/Urho3D-SoftBody

-------------------------

dragonCASTjosh | 2017-01-02 01:06:48 UTC | #2

thanks ill give it a go

-------------------------

codingmonkey | 2017-01-02 01:06:48 UTC | #3

Thanks for this example. 
Good starting point for moving forward to clothes and hair

-------------------------

practicing01 | 2017-01-02 01:06:48 UTC | #4

That's hot.  Any idea of what the performance will be like on android?

-------------------------

rasteron | 2017-01-02 01:06:48 UTC | #5

This looks cool Lumak! Thanks for sharing :slight_smile: You should do a PR for next release. Yes, I'm also wondering about android performance.

-------------------------

Lumak | 2017-01-02 01:06:49 UTC | #6

I'm not sure about performance on android or on any platform for that matter.  Some optimization should be made. One is checking to see if a collision deformation has occurred before blindly copying the vertex buffer every frame.  
This is my first time working with softbody physics and have concerns with bullet's implementation in general.  While running bullet's demo, I noticed that objects can easily penetrate or punch-through some surfaces (also observed with the mushroom example).  I'm not sure if it's because of a) its intended to work as implemented on specific softbody types, b) some softbody parameter settings that are not set properly or c) caused by degenerative triangles. Further studies would be required to figure out what all the softbody parameter settings are, what they do, and what the optimal settings would be. If I were to use softbody physics in an application, I would first process models through NVidia's NvTriStrip, [url]http://www.nvidia.com/object/nvtristrip_library.html[/url], to remove any degenerative triangles and hope that it can also eliminate what looks like tearing when there are, I think, duplicate vertices.
I'm just not all that familiar with softbody physics but hope that there are others in the community who are.

-------------------------

Mike | 2017-01-02 01:06:49 UTC | #7

Many thanks for sharing this Lumak  :stuck_out_tongue: 

For optimization, I will investigate if there is a sleep/rest threshold as there exists for RigidBody.

How do you account for position, rotation and scale? Currently transforms are hard-coded and I have some troubles feeding custom transforms to match softBodyNode transforms.

-------------------------

Lumak | 2017-01-02 01:06:52 UTC | #8

The code sample that I provided is no where near complete.  It was written primarily to test a trimesh softbody functionality. Basic node_ member variable access functions, such as set/get transforms, set scale, etc. were not written.  If you want to write those, look for a line with a comment "// create methods for these" in SoftBody::CreateBodyFromTriMesh(...) function and you can see a list of functions that I neglected to write.

-------------------------

Mike | 2017-01-02 01:06:52 UTC | #9

Thanks, for now I give up.

-------------------------

Mike | 2017-03-17 18:56:21 UTC | #10

Made as a SoftBody component (nothing added, raw extraction, code conventions and simplification):

SoftBody.h

[code]
#pragma once

#include "../Scene/Component.h"

class btSoftBody;

namespace Urho3D
{

/// Physics soft body component.
class URHO3D_API SoftBody : public Component
{
    OBJECT(SoftBody);

public:
    /// Construct.
    SoftBody(Context* context);
    /// Destruct. Free the soft body and geometries.
    ~SoftBody();
    /// Register object factory.
    static void RegisterObject(Context* context);

    /// Handle logic post-update event where we update the vertex buffer.
    void HandlePostUpdate(StringHash eventType, VariantMap& eventData);

    /// Remove the soft body.
    void ReleaseBody();
    /// Create TriMesh from model's geometry.
    void CreateTriMesh();
    /// Create the soft body from a TriMesh.
    bool CreateBodyFromTriMesh(VertexBuffer* vertexBuffer, IndexBuffer* indexBuffer, bool randomizeConstraints = true);
    /// Return Bullet soft body.
    btSoftBody* GetBody() { return body_; }
    /// TODO.
    void SetPosition(const Vector3& position);

protected:
    /// Handle node being assigned.
    virtual void OnNodeSet(Node* node);
    /// Handle scene being assigned.
    virtual void OnSceneSet(Scene* scene);
    /// Handle node transform being dirtied.
//    virtual void OnMarkedDirty(Node* node);

private:
    /// Create the soft body, or re-add to the physics world with changed flags. Calls UpdateMass().
    void AddBodyToWorld();
    /// Remove the soft body from the physics world.
    void RemoveBodyFromWorld();

    /// Physics world.
    WeakPtr<PhysicsWorld> physicsWorld_;
    /// Bullet soft body.
    btSoftBody* body_;
    /// Vertex buffer.
    VertexBuffer* vertexBuffer_;
};

}
[/code]

SoftBody .cpp

[code]
#include "../Precompiled.h"

#include "../Core/Context.h"
#include "../Core/CoreEvents.h"
#include "../Graphics/Geometry.h"
#include "../Graphics/IndexBuffer.h"
#include "../IO/Log.h"
#include "../Graphics/Material.h"
#include "../Graphics/Model.h"
#include "../Physics/PhysicsUtils.h"
#include "../Physics/PhysicsWorld.h"
#include "../Resource/ResourceCache.h"
#include "../Scene/Scene.h"
#include "../Scene/SceneEvents.h"
#include "../Physics/SoftBody.h"
#include "../Graphics/StaticModel.h"
#include "../Graphics/VertexBuffer.h"

#include <Bullet/BulletSoftBody/btSoftBody.h>
#include <Bullet/BulletSoftBody/btSoftRigidDynamicsWorld.h>
#include <Bullet/BulletSoftBody/btSoftBodyHelpers.h>

namespace Urho3D
{

extern const char* PHYSICS_CATEGORY;

SoftBody::SoftBody(Context* context) :
    Component(context),
    body_(NULL),
    vertexBuffer_(NULL)
{
}

SoftBody::~SoftBody()
{
    if (body_)
    {
        delete body_;
        body_ = NULL;
    }

    // We don't own the vertsbuffer
    vertexBuffer_ = NULL;
}

void SoftBody::RegisterObject(Context* context)
{
    context->RegisterFactory<SoftBody>(PHYSICS_CATEGORY);
}

void SoftBody::OnNodeSet(Node* node)
{
    if (node)
        node->AddListener(this);
}

void SoftBody::OnSceneSet(Scene* scene)
{
    if (scene)
    {
        if (scene == node_)
            LOGWARNING(GetTypeName() + " should not be created to the root scene node");

        physicsWorld_ = scene->GetOrCreateComponent<PhysicsWorld>();
        physicsWorld_->AddSoftBody(this);

        AddBodyToWorld();
    }
    else
    {
        ReleaseBody();

        if (physicsWorld_)
            physicsWorld_->RemoveSoftBody(this);
    }
}

void SoftBody::AddBodyToWorld()
{
    if (!physicsWorld_)
        return;

    if (body_)
    {
        btSoftRigidDynamicsWorld* world = (btSoftRigidDynamicsWorld*)physicsWorld_->GetWorld();
        world->addSoftBody(body_);
    }
}

void SoftBody::ReleaseBody()
{
    if (body_)
    {
        RemoveBodyFromWorld();
        delete body_;
        body_ = NULL;
    }
}

void SoftBody::RemoveBodyFromWorld()
{
    if (body_)
    {
        if (physicsWorld_)
        {
            btSoftRigidDynamicsWorld* pSoftRigidWorld = (btSoftRigidDynamicsWorld *)physicsWorld_->GetWorld();
            pSoftRigidWorld->removeSoftBody(body_);
        }
    }
}

void SoftBody::CreateTriMesh()
{
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    Scene* scene = GetScene();

    // Get model
    StaticModel* model = node_->GetComponent<StaticModel>();
    if (!model)
        return;
    Model* originalModel = model->GetModel();
    if (!originalModel)
        return;

    // Clone model
    SharedPtr<Model> cloneModel = originalModel->Clone();
    model->SetModel(cloneModel);

    // Get the vertex and index buffers from the first geometry's first LOD level
    VertexBuffer* vertexBuffer = cloneModel->GetGeometry(0, 0)->GetVertexBuffer(0);
    IndexBuffer* indexBuffer = cloneModel->GetGeometry(0, 0)->GetIndexBuffer();

    // Cretae soft body from TriMesh
    CreateBodyFromTriMesh(vertexBuffer, indexBuffer);
}

bool SoftBody::CreateBodyFromTriMesh(VertexBuffer* vertexBuffer, IndexBuffer* indexBuffer, bool randomizeConstraints)
{
    bool bConstructed = false;

    if (vertexBuffer && indexBuffer)
    {
        btAlignedObjectArray<bool> chks;
        btAlignedObjectArray<btVector3> vtx;

        // Save vertexbuffer ptr
        vertexBuffer_ = vertexBuffer;

        // Copy vertex buffer
        const unsigned char* pVertexData = (const unsigned char*)vertexBuffer_->Lock(0, vertexBuffer_->GetVertexCount());

        if (pVertexData)
        {
            unsigned numVertices = vertexBuffer_->GetVertexCount();
            unsigned vertexSize = vertexBuffer_->GetVertexSize();

            vtx.resize(numVertices);

            // Copy the original verts
            for (unsigned i = 0; i < numVertices; ++i)
            {
                const Vector3& src = *reinterpret_cast<const Vector3*>(pVertexData + i * vertexSize);
                vtx[i] = ToBtVector3(src);
            }
            vertexBuffer_->Unlock();
        }

        // Create softbody
        physicsWorld_ = GetScene()->GetComponent<PhysicsWorld>();
        body_ = new btSoftBody(physicsWorld_->GetSoftBodyInfo(), vtx.size(), &vtx[0], 0);

        // Copy indexbuffer
        const unsigned* pIndexData = (const unsigned*)indexBuffer->Lock(0, indexBuffer->GetIndexCount());
        const unsigned short* pUShortData = (const unsigned short*)pIndexData;
        if (pIndexData)
        {
            unsigned numIndices = indexBuffer->GetIndexCount();
            unsigned indexSize = indexBuffer->GetIndexSize();

            int ntriangles = (int)numIndices / 3;

            int maxidx = 0;
            int i; //,j,ni;

            if (indexSize == sizeof(unsigned short))
            {
                for (i = 0; i < (int)numIndices; ++i)
                {
                    unsigned uidx = pUShortData[i];
                    maxidx = Max(uidx, maxidx);
                }
            }
            else if (indexSize == sizeof(unsigned))
            {
                for (i = 0; i < (int)numIndices; ++i)
                {
                    unsigned uidx = pIndexData[i];
                    maxidx = Max(uidx, maxidx);
                }
            }
            ++maxidx;
            chks.resize(maxidx * maxidx, false);

            for (i = 0; i < (int)numIndices; i += 3)
            {
                int idx[3];
                if (indexSize == sizeof(unsigned short))
                {
                    idx[0] = (int)pUShortData[i];
                    idx[1] = (int)pUShortData[i + 1];
                    idx[2] = (int)pUShortData[i + 2];
                }
                else
                {
                    idx[0] = (int)pIndexData[i];
                    idx[1] = (int)pIndexData[i + 1];
                    idx[2] = (int)pIndexData[i + 2];
                }

                #define IDX(_x_, _y_) ((_y_) * maxidx + (_x_))
                for (int j=2, k=0; k<3; j = k++)
                {
                    if (!chks[IDX(idx[j], idx[k])])
                    {
                        chks[IDX(idx[j], idx[k])] = true;
                        chks[IDX(idx[k], idx[j])] = true;
                        body_->appendLink(idx[j], idx[k]);
                    }
                }
                #undef IDX
                body_->appendFace(idx[0], idx[1], idx[2]);
            }
            indexBuffer->Unlock();
        }

        if (randomizeConstraints)
            body_->randomizeConstraints();

        // Straight out of Bullet's softbody demo for trimesh
        body_->m_materials[0]->m_kLST = 0.1;
        body_->m_cfg.kMT = 0.05;

        btMatrix3x3 m;
        m.setEulerZYX(0, 0, 0);

        // Create methods for these
        body_->transform(btTransform(m, btVector3(0, 4, 0)));
        body_->scale(btVector3(2, 2, 2));
        body_->setTotalMass(50, true);
        body_->setPose(true, true);

        bConstructed = true;
    }

    AddBodyToWorld();
    SubscribeToEvent(E_POSTUPDATE, HANDLER(SoftBody, HandlePostUpdate));

    return bConstructed;
}

void SoftBody::HandlePostUpdate(StringHash eventType, VariantMap& eventData)
{
    // Update vertex buffer
    if (body_ && vertexBuffer_)
    {
        unsigned char* pVertexData = (unsigned char*)vertexBuffer_->Lock(0, vertexBuffer_->GetVertexCount());

        // Copy soft body vertices back into the model vertex buffer
        if (pVertexData)
        {
            unsigned numVertices = vertexBuffer_->GetVertexCount();
            unsigned vertexSize = vertexBuffer_->GetVertexSize();

            // Copy original vertex positions
            for (unsigned i = 0; i < body_->m_nodes.size(); ++i)
            {
                btSoftBody::Node& n = body_->m_nodes[i];
                Vector3& src = *reinterpret_cast<Vector3*>(pVertexData + i * vertexSize);
                src = ToVector3(n.m_x);
            }
            vertexBuffer_->Unlock();
        }
    }
}

void SoftBody::SetPosition(const Vector3& position)
{
    if (body_)
    {
        body_->transform(btTransform(btQuaternion::getIdentity(), ToBtVector3(position)));
        MarkNetworkUpdate();
    }
}

}
[/code]

11_Physics.h

[code]
#include <Urho3D/Physics/SoftBody.h>
[/code]

11_Physics.cpp

[code]
    // Create mushroom
    Node* softBodyNode = scene_->CreateChild("SomeSoftBody");
    StaticModel* model = softBodyNode->CreateComponent<StaticModel>();
    model->SetModel(cache->GetResource<Model>("Models/Mushroom.mdl"));
    model->SetMaterial(cache->GetResource<Material>("Materials/Mushroom.xml"));
    model->SetCastShadows(true);

    // Create SoftBody component
    SoftBody* body = softBodyNode->CreateComponent<SoftBody>();
    body->CreateTriMesh();
[/code]

-------------------------

Mike | 2017-01-02 01:06:53 UTC | #11

PhysicsWorld.h
[spoiler][code]
//
// Copyright (c) 2008-2015 the Urho3D project.
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
// THE SOFTWARE.
//

#pragma once

#include "../Container/HashSet.h"
#include "../IO/VectorBuffer.h"
#include "../Math/BoundingBox.h"
#include "../Math/Sphere.h"
#include "../Math/Vector3.h"
#include "../Scene/Component.h"

#include <Bullet/LinearMath/btIDebugDraw.h>

class btCollisionConfiguration;
class btCollisionShape;
class btBroadphaseInterface;
class btConstraintSolver;
class btDiscreteDynamicsWorld;
class btDispatcher;
class btDynamicsWorld;
class btPersistentManifold;
class btSoftBodyWorldInfo; //===============================

namespace Urho3D
{

class CollisionShape;
class Deserializer;
class Constraint;
class Model;
class Node;
class Ray;
class RigidBody;
class Scene;
class Serializer;
class XMLElement;

//=====================================
class SoftBody;
class IndexBuffer;
class VertexBuffer;
//=====================================

struct CollisionGeometryData;

/// Physics raycast hit.
struct URHO3D_API PhysicsRaycastResult
{
    /// Construct with defaults.
    PhysicsRaycastResult() :
        body_(0)
    {
    }

    /// Test for inequality, added to prevent GCC from complaining.
    bool operator !=(const PhysicsRaycastResult& rhs) const
    {
        return position_ != rhs.position_ || normal_ != rhs.normal_ || distance_ != rhs.distance_ || body_ != rhs.body_;
    }

    /// Hit worldspace position.
    Vector3 position_;
    /// Hit worldspace normal.
    Vector3 normal_;
    /// Hit distance from ray origin.
    float distance_;
    /// Rigid body that was hit.
    RigidBody* body_;
};

/// Delayed world transform assignment for parented rigidbodies.
struct DelayedWorldTransform
{
    /// Rigid body.
    RigidBody* rigidBody_;
    /// Parent rigid body.
    RigidBody* parentRigidBody_;
    /// New world position.
    Vector3 worldPosition_;
    /// New world rotation.
    Quaternion worldRotation_;
};

static const float DEFAULT_MAX_NETWORK_ANGULAR_VELOCITY = 100.0f;

/// Physics simulation world component. Should be added only to the root scene node.
class URHO3D_API PhysicsWorld : public Component, public btIDebugDraw
{
    OBJECT(PhysicsWorld);

    friend void InternalPreTickCallback(btDynamicsWorld* world, btScalar timeStep);
    friend void InternalTickCallback(btDynamicsWorld* world, btScalar timeStep);

public:
    /// Construct.
    PhysicsWorld(Context* scontext);
    /// Destruct.
    virtual ~PhysicsWorld();
    /// Register object factory.
    static void RegisterObject(Context* context);


//=========================================
        // softbody
        btSoftBodyWorldInfo* GetSoftBodyInfo() { return m_softBodyWorldInfo; }
        btSoftBodyWorldInfo* m_softBodyWorldInfo;
//=========================================

    /// Check if an AABB is visible for debug drawing.
    virtual bool isVisible(const btVector3& aabbMin, const btVector3& aabbMax);
    /// Draw a physics debug line.
    virtual void drawLine(const btVector3& from, const btVector3& to, const btVector3& color);
    /// Log warning from the physics engine.
    virtual void reportErrorWarning(const char* warningString);
    /// Draw a physics debug contact point. Not implemented.
    virtual void drawContactPoint
        (const btVector3& pointOnB, const btVector3& normalOnB, btScalar distance, int lifeTime, const btVector3& color);
    /// Draw physics debug 3D text. Not implemented.
    virtual void draw3dText(const btVector3& location, const char* textString);

    /// Set debug draw flags.
    virtual void setDebugMode(int debugMode) { debugMode_ = debugMode; }

    /// Return debug draw flags.
    virtual int getDebugMode() const { return debugMode_; }

    /// Visualize the component as debug geometry.
    virtual void DrawDebugGeometry(DebugRenderer* debug, bool depthTest);

    /// Step the simulation forward.
    void Update(float timeStep);
    /// Refresh collisions only without updating dynamics.
    void UpdateCollisions();
    /// Set simulation substeps per second.
    void SetFps(int fps);
    /// Set gravity.
    void SetGravity(const Vector3& gravity);
    /// Set maximum number of physics substeps per frame. 0 (default) is unlimited. Positive values cap the amount. Use a negative value to enable an adaptive timestep. This may cause inconsistent physics behavior.
    void SetMaxSubSteps(int num);
    /// Set number of constraint solver iterations.
    void SetNumIterations(int num);
    /// Set whether to interpolate between simulation steps.
    void SetInterpolation(bool enable);
    /// Set whether to use Bullet's internal edge utility for trimesh collisions. Disabled by default.
    void SetInternalEdge(bool enable);
    /// Set split impulse collision mode. This is more accurate, but slower. Disabled by default.
    void SetSplitImpulse(bool enable);
    /// Set maximum angular velocity for network replication.
    void SetMaxNetworkAngularVelocity(float velocity);
    /// Perform a physics world raycast and return all hits.
    void Raycast
        (PODVector<PhysicsRaycastResult>& result, const Ray& ray, float maxDistance, unsigned collisionMask = M_MAX_UNSIGNED);
    /// Perform a physics world raycast and return the closest hit.
    void RaycastSingle(PhysicsRaycastResult& result, const Ray& ray, float maxDistance, unsigned collisionMask = M_MAX_UNSIGNED);
    /// Perform a physics world swept sphere test and return the closest hit.
    void SphereCast
        (PhysicsRaycastResult& result, const Ray& ray, float radius, float maxDistance, unsigned collisionMask = M_MAX_UNSIGNED);
    /// Perform a physics world swept convex test using a user-supplied collision shape and return the first hit.
    void ConvexCast(PhysicsRaycastResult& result, CollisionShape* shape, const Vector3& startPos, const Quaternion& startRot,
        const Vector3& endPos, const Quaternion& endRot, unsigned collisionMask = M_MAX_UNSIGNED);
    /// Perform a physics world swept convex test using a user-supplied Bullet collision shape and return the first hit.
    void ConvexCast(PhysicsRaycastResult& result, btCollisionShape* shape, const Vector3& startPos, const Quaternion& startRot,
        const Vector3& endPos, const Quaternion& endRot, unsigned collisionMask = M_MAX_UNSIGNED);
    /// Invalidate cached collision geometry for a model.
    void RemoveCachedGeometry(Model* model);
    /// Return rigid bodies by a sphere query.
    void GetRigidBodies(PODVector<RigidBody*>& result, const Sphere& sphere, unsigned collisionMask = M_MAX_UNSIGNED);
    /// Return rigid bodies by a box query.
    void GetRigidBodies(PODVector<RigidBody*>& result, const BoundingBox& box, unsigned collisionMask = M_MAX_UNSIGNED);
    /// Return rigid bodies that have been in collision with a specific body on the last simulation step.
    void GetRigidBodies(PODVector<RigidBody*>& result, const RigidBody* body);

    /// Return gravity.
    Vector3 GetGravity() const;

    /// Return maximum number of physics substeps per frame.
    int GetMaxSubSteps() const { return maxSubSteps_; }

    /// Return number of constraint solver iterations.
    int GetNumIterations() const;

    /// Return whether interpolation between simulation steps is enabled.
    bool GetInterpolation() const { return interpolation_; }

    /// Return whether Bullet's internal edge utility for trimesh collisions is enabled.
    bool GetInternalEdge() const { return internalEdge_; }

    /// Return whether split impulse collision mode is enabled.
    bool GetSplitImpulse() const;

    /// Return simulation steps per second.
    int GetFps() const { return fps_; }

    /// Return maximum angular velocity for network replication.
    float GetMaxNetworkAngularVelocity() const { return maxNetworkAngularVelocity_; }

    /// Add a rigid body to keep track of. Called by RigidBody.
    void AddRigidBody(RigidBody* body);
    /// Remove a rigid body. Called by RigidBody.
    void RemoveRigidBody(RigidBody* body);

//====================================
    /// Add a soft body to keep track of. Called by SoftBody.
    void AddSoftBody(SoftBody* body);
    /// Remove a soft body. Called by SoftBody.
    void RemoveSoftBody(SoftBody* body);
//====================================

    /// Add a collision shape to keep track of. Called by CollisionShape.
    void AddCollisionShape(CollisionShape* shape);
    /// Remove a collision shape. Called by CollisionShape.
    void RemoveCollisionShape(CollisionShape* shape);
    /// Add a constraint to keep track of. Called by Constraint.
    void AddConstraint(Constraint* joint);
    /// Remove a constraint. Called by Constraint.
    void RemoveConstraint(Constraint* joint);
    /// Add a delayed world transform assignment. Called by RigidBody.
    void AddDelayedWorldTransform(const DelayedWorldTransform& transform);
    /// Add debug geometry to the debug renderer.
    void DrawDebugGeometry(bool depthTest);
    /// Set debug renderer to use. Called both by PhysicsWorld itself and physics components.
    void SetDebugRenderer(DebugRenderer* debug);
    /// Set debug geometry depth test mode. Called both by PhysicsWorld itself and physics components.
    void SetDebugDepthTest(bool enable);

    /// Return the Bullet physics world.
    btDiscreteDynamicsWorld* GetWorld() { return world_; }

    /// Clean up the geometry cache.
    void CleanupGeometryCache();

    /// Return trimesh collision geometry cache.
    HashMap<Pair<Model*, unsigned>, SharedPtr<CollisionGeometryData> >& GetTriMeshCache() { return triMeshCache_; }

    /// Return convex collision geometry cache.
    HashMap<Pair<Model*, unsigned>, SharedPtr<CollisionGeometryData> >& GetConvexCache() { return convexCache_; }

    /// Set node dirtying to be disregarded.
    void SetApplyingTransforms(bool enable) { applyingTransforms_ = enable; }

    /// Return whether node dirtying should be disregarded.
    bool IsApplyingTransforms() const { return applyingTransforms_; }

protected:
    /// Handle scene being assigned.
    virtual void OnSceneSet(Scene* scene);

private:
    /// Handle the scene subsystem update event, step simulation here.
    void HandleSceneSubsystemUpdate(StringHash eventType, VariantMap& eventData);
    /// Trigger update before each physics simulation step.
    void PreStep(float timeStep);
    /// Trigger update after each physics simulation step.
    void PostStep(float timeStep);
    /// Send accumulated collision events.
    void SendCollisionEvents();

    /// Bullet collision configuration.
    btCollisionConfiguration* collisionConfiguration_;
    /// Bullet collision dispatcher.
    btDispatcher* collisionDispatcher_;
    /// Bullet collision broadphase.
    btBroadphaseInterface* broadphase_;
    /// Bullet constraint solver.
    btConstraintSolver* solver_;
    /// Bullet physics world.
    btDiscreteDynamicsWorld* world_;
    /// Extra weak pointer to scene to allow for cleanup in case the world is destroyed before other components.
    WeakPtr<Scene> scene_;
    /// Rigid bodies in the world.
    PODVector<RigidBody*> rigidBodies_;

//===================================
    /// Soft bodies in the world.
    PODVector<SoftBody*> softBodies_;
//===================================

    /// Collision shapes in the world.
    PODVector<CollisionShape*> collisionShapes_;
    /// Constraints in the world.
    PODVector<Constraint*> constraints_;
    /// Collision pairs on this frame.
    HashMap<Pair<WeakPtr<RigidBody>, WeakPtr<RigidBody> >, btPersistentManifold*> currentCollisions_;
    /// Collision pairs on the previous frame. Used to check if a collision is "new." Manifolds are not guaranteed to exist anymore.
    HashMap<Pair<WeakPtr<RigidBody>, WeakPtr<RigidBody> >, btPersistentManifold*> previousCollisions_;
    /// Delayed (parented) world transform assignments.
    HashMap<RigidBody*, DelayedWorldTransform> delayedWorldTransforms_;
    /// Cache for trimesh geometry data by model and LOD level.
    HashMap<Pair<Model*, unsigned>, SharedPtr<CollisionGeometryData> > triMeshCache_;
    /// Cache for convex geometry data by model and LOD level.
    HashMap<Pair<Model*, unsigned>, SharedPtr<CollisionGeometryData> > convexCache_;
    /// Preallocated event data map for physics collision events.
    VariantMap physicsCollisionData_;
    /// Preallocated event data map for node collision events.
    VariantMap nodeCollisionData_;
    /// Preallocated buffer for physics collision contact data.
    VectorBuffer contacts_;
    /// Simulation substeps per second.
    unsigned fps_;
    /// Maximum number of simulation substeps per frame. 0 (default) unlimited, or negative values for adaptive timestep.
    int maxSubSteps_;
    /// Time accumulator for non-interpolated mode.
    float timeAcc_;
    /// Maximum angular velocity for network replication.
    float maxNetworkAngularVelocity_;
    /// Interpolation flag.
    bool interpolation_;
    /// Use internal edge utility flag.
    bool internalEdge_;
    /// Applying transforms flag.
    bool applyingTransforms_;
    /// Debug renderer.
    DebugRenderer* debugRenderer_;
    /// Debug draw flags.
    int debugMode_;
    /// Debug draw depth test mode.
    bool debugDepthTest_;
};

/// Register Physics library objects.
void URHO3D_API RegisterPhysicsLibrary(Context* context);

}

[/code][/spoiler]

PhysicsWorld.cpp
[spoiler][code]
//
// Copyright (c) 2008-2015 the Urho3D project.
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
// THE SOFTWARE.
//

#include "../Precompiled.h"

#include "../Core/Context.h"
#include "../Core/Mutex.h"
#include "../Core/Profiler.h"
#include "../Graphics/DebugRenderer.h"
#include "../Graphics/Model.h"
#include "../IO/Log.h"
#include "../Math/Ray.h"
#include "../Physics/CollisionShape.h"
#include "../Physics/Constraint.h"
#include "../Physics/PhysicsEvents.h"
#include "../Physics/PhysicsUtils.h"
#include "../Physics/PhysicsWorld.h"
#include "../Physics/RigidBody.h"
#include "../Scene/Scene.h"
#include "../Scene/SceneEvents.h"
#include "../Physics/SoftBody.h"

#include <Bullet/BulletCollision/BroadphaseCollision/btDbvtBroadphase.h>
#include <Bullet/BulletCollision/CollisionDispatch/btDefaultCollisionConfiguration.h>
#include <Bullet/BulletCollision/CollisionDispatch/btInternalEdgeUtility.h>
#include <Bullet/BulletCollision/CollisionShapes/btBoxShape.h>
#include <Bullet/BulletCollision/CollisionShapes/btSphereShape.h>
#include <Bullet/BulletDynamics/ConstraintSolver/btSequentialImpulseConstraintSolver.h>
#include <Bullet/BulletDynamics/Dynamics/btDiscreteDynamicsWorld.h>

//==========================================
    #include <Bullet/BulletSoftBody/btSoftBody.h>
    #include <Bullet/BulletSoftBody/btSoftBodyRigidBodyCollisionConfiguration.h>
    #include <Bullet/BulletSoftBody/btSoftRigidDynamicsWorld.h>
    #define TEST_SOFTBODY
//==========================================

extern ContactAddedCallback gContactAddedCallback;

namespace Urho3D
{

const char* PHYSICS_CATEGORY = "Physics";
extern const char* SUBSYSTEM_CATEGORY;

static const int MAX_SOLVER_ITERATIONS = 256;
static const int DEFAULT_FPS = 60;
static const Vector3 DEFAULT_GRAVITY = Vector3(0.0f, -9.81f, 0.0f);

static bool CompareRaycastResults(const PhysicsRaycastResult& lhs, const PhysicsRaycastResult& rhs)
{
    return lhs.distance_ < rhs.distance_;
}

void InternalPreTickCallback(btDynamicsWorld* world, btScalar timeStep)
{
    static_cast<PhysicsWorld*>(world->getWorldUserInfo())->PreStep(timeStep);
}

void InternalTickCallback(btDynamicsWorld* world, btScalar timeStep)
{
    static_cast<PhysicsWorld*>(world->getWorldUserInfo())->PostStep(timeStep);
}

static bool CustomMaterialCombinerCallback(btManifoldPoint& cp, const btCollisionObjectWrapper* colObj0Wrap, int partId0,
    int index0, const btCollisionObjectWrapper* colObj1Wrap, int partId1, int index1)
{
    btAdjustInternalEdgeContacts(cp, colObj1Wrap, colObj0Wrap, partId1, index1);

    cp.m_combinedFriction = colObj0Wrap->getCollisionObject()->getFriction() * colObj1Wrap->getCollisionObject()->getFriction();
    cp.m_combinedRestitution =
        colObj0Wrap->getCollisionObject()->getRestitution() * colObj1Wrap->getCollisionObject()->getRestitution();

    return true;
}

/// Callback for physics world queries.
struct PhysicsQueryCallback : public btCollisionWorld::ContactResultCallback
{
    /// Construct.
    PhysicsQueryCallback(PODVector<RigidBody*>& result, unsigned collisionMask) :
        result_(result),
        collisionMask_(collisionMask)
    {
    }

    /// Add a contact result.
    virtual btScalar addSingleResult(btManifoldPoint&, const btCollisionObjectWrapper* colObj0Wrap, int, int,
        const btCollisionObjectWrapper* colObj1Wrap, int, int)
    {
        RigidBody* body = reinterpret_cast<RigidBody*>(colObj0Wrap->getCollisionObject()->getUserPointer());
        if (body && !result_.Contains(body) && (body->GetCollisionLayer() & collisionMask_))
            result_.Push(body);
        body = reinterpret_cast<RigidBody*>(colObj1Wrap->getCollisionObject()->getUserPointer());
        if (body && !result_.Contains(body) && (body->GetCollisionLayer() & collisionMask_))
            result_.Push(body);
        return 0.0f;
    }

    /// Found rigid bodies.
    PODVector<RigidBody*>& result_;
    /// Collision mask for the query.
    unsigned collisionMask_;
};

PhysicsWorld::PhysicsWorld(Context* context) :
    Component(context),
    collisionConfiguration_(0),
    collisionDispatcher_(0),
    broadphase_(0),
    solver_(0),
    world_(0),
    fps_(DEFAULT_FPS),
    maxSubSteps_(0),
    timeAcc_(0.0f),
    maxNetworkAngularVelocity_(DEFAULT_MAX_NETWORK_ANGULAR_VELOCITY),
    interpolation_(true),
    internalEdge_(true),
    applyingTransforms_(false),
    debugRenderer_(0),
    debugMode_(btIDebugDraw::DBG_DrawWireframe | btIDebugDraw::DBG_DrawConstraints | btIDebugDraw::DBG_DrawConstraintLimits)
{
    gContactAddedCallback = CustomMaterialCombinerCallback;

//===============================================
//    collisionConfiguration_ = new btDefaultCollisionConfiguration();
    #ifndef TEST_SOFTBODY
        collisionConfiguration_ = new btDefaultCollisionConfiguration();
    #else
       collisionConfiguration_ = new btSoftBodyRigidBodyCollisionConfiguration();
    #endif
//===============================================

    collisionDispatcher_ = new btCollisionDispatcher(collisionConfiguration_);
    broadphase_ = new btDbvtBroadphase();
    solver_ = new btSequentialImpulseConstraintSolver();

//===============================================
//    world_ = new btDiscreteDynamicsWorld(collisionDispatcher_, broadphase_, solver_, collisionConfiguration_);
    #ifndef TEST_SOFTBODY
        world_ = new btDiscreteDynamicsWorld(collisionDispatcher_, broadphase_, solver_, collisionConfiguration_);
    #else
       world_ = new btSoftRigidDynamicsWorld(collisionDispatcher_, broadphase_, solver_, collisionConfiguration_, NULL);
    #endif
//===============================================

    world_->setGravity(ToBtVector3(DEFAULT_GRAVITY));
    world_->getDispatchInfo().m_useContinuous = true;
    world_->getSolverInfo().m_splitImpulse = false; // Disable by default for performance
    world_->setDebugDrawer(this);
    world_->setInternalTickCallback(InternalPreTickCallback, static_cast<void*>(this), true);
    world_->setInternalTickCallback(InternalTickCallback, static_cast<void*>(this), false);

//==========================================
    #ifdef TEST_SOFTBODY
        m_softBodyWorldInfo = new btSoftBodyWorldInfo();
        m_softBodyWorldInfo->m_dispatcher = collisionDispatcher_;
        m_softBodyWorldInfo->m_broadphase = broadphase_;
        m_softBodyWorldInfo->air_density = (btScalar)1.2;
        m_softBodyWorldInfo->water_density = 0;
        m_softBodyWorldInfo->water_offset = 0;
        m_softBodyWorldInfo->water_normal = btVector3(0, 0, 0);
        m_softBodyWorldInfo->m_gravity.setValue(0, -10, 0);
        m_softBodyWorldInfo->m_sparsesdf.Initialize();

        softBodies_.Clear();
    #endif
//===========================================
}

PhysicsWorld::~PhysicsWorld()
{
    if (scene_)
    {
        // Force all remaining constraints, rigid bodies and collision shapes to release themselves
        for (PODVector<Constraint*>::Iterator i = constraints_.Begin(); i != constraints_.End(); ++i)
            (*i)->ReleaseConstraint();

        for (PODVector<RigidBody*>::Iterator i = rigidBodies_.Begin(); i != rigidBodies_.End(); ++i)
            (*i)->ReleaseBody();

        for (PODVector<CollisionShape*>::Iterator i = collisionShapes_.Begin(); i != collisionShapes_.End(); ++i)
            (*i)->ReleaseShape();

//====================================
        for (PODVector<SoftBody*>::Iterator i = softBodies_.Begin(); i != softBodies_.End(); ++i)
            (*i)->ReleaseBody();
//====================================
    }

    delete world_;
    world_ = 0;

    delete solver_;
    solver_ = 0;

    delete broadphase_;
    broadphase_ = 0;

    delete collisionDispatcher_;
    collisionDispatcher_ = 0;

    delete collisionConfiguration_;
    collisionConfiguration_ = 0;

//=================================
    if (m_softBodyWorldInfo)
    {
        m_softBodyWorldInfo->m_dispatcher = 0;
        m_softBodyWorldInfo->m_broadphase = 0;

        delete m_softBodyWorldInfo;
        m_softBodyWorldInfo = 0;
    }
//=================================
}

void PhysicsWorld::RegisterObject(Context* context)
{
    context->RegisterFactory<PhysicsWorld>(SUBSYSTEM_CATEGORY);

    MIXED_ACCESSOR_ATTRIBUTE("Gravity", GetGravity, SetGravity, Vector3, DEFAULT_GRAVITY, AM_DEFAULT);
    ATTRIBUTE("Physics FPS", int, fps_, DEFAULT_FPS, AM_DEFAULT);
    ATTRIBUTE("Max Substeps", int, maxSubSteps_, 0, AM_DEFAULT);
    ACCESSOR_ATTRIBUTE("Solver Iterations", GetNumIterations, SetNumIterations, int, 10, AM_DEFAULT);
    ATTRIBUTE("Net Max Angular Vel.", float, maxNetworkAngularVelocity_, DEFAULT_MAX_NETWORK_ANGULAR_VELOCITY, AM_DEFAULT);
    ATTRIBUTE("Interpolation", bool, interpolation_, true, AM_FILE);
    ATTRIBUTE("Internal Edge Utility", bool, internalEdge_, true, AM_DEFAULT);
    ACCESSOR_ATTRIBUTE("Split Impulse", GetSplitImpulse, SetSplitImpulse, bool, false, AM_DEFAULT);
}

bool PhysicsWorld::isVisible(const btVector3& aabbMin, const btVector3& aabbMax)
{
    if (debugRenderer_)
        return debugRenderer_->IsInside(BoundingBox(ToVector3(aabbMin), ToVector3(aabbMax)));
    else
        return false;
}

void PhysicsWorld::drawLine(const btVector3& from, const btVector3& to, const btVector3& color)
{
    if (debugRenderer_)
        debugRenderer_->AddLine(ToVector3(from), ToVector3(to), Color(color.x(), color.y(), color.z()), debugDepthTest_);
}

void PhysicsWorld::DrawDebugGeometry(DebugRenderer* debug, bool depthTest)
{
    if (debug)
    {
        PROFILE(PhysicsDrawDebug);

        debugRenderer_ = debug;
        debugDepthTest_ = depthTest;
        world_->debugDrawWorld();
        debugRenderer_ = 0;
    }
}

void PhysicsWorld::reportErrorWarning(const char* warningString)
{
    LOGWARNING("Physics: " + String(warningString));
}

void PhysicsWorld::drawContactPoint(const btVector3& pointOnB, const btVector3& normalOnB, btScalar distance, int lifeTime,
    const btVector3& color)
{
}

void PhysicsWorld::draw3dText(const btVector3& location, const char* textString)
{
}

void PhysicsWorld::Update(float timeStep)
{
    PROFILE(UpdatePhysics);

    float internalTimeStep = 1.0f / fps_;
    int maxSubSteps = (int)(timeStep * fps_) + 1;
    if (maxSubSteps_ < 0)
    {
        internalTimeStep = timeStep;
        maxSubSteps = 1;
    }
    else if (maxSubSteps_ > 0)
        maxSubSteps = Min(maxSubSteps, maxSubSteps_);

    delayedWorldTransforms_.Clear();

    if (interpolation_)
        world_->stepSimulation(timeStep, maxSubSteps, internalTimeStep);
    else
    {
        timeAcc_ += timeStep;
        while (timeAcc_ >= internalTimeStep && maxSubSteps > 0)
        {
            world_->stepSimulation(internalTimeStep, 0, internalTimeStep);
            timeAcc_ -= internalTimeStep;
            --maxSubSteps;
        }
    }

    // Apply delayed (parented) world transforms now
    while (!delayedWorldTransforms_.Empty())
    {
        for (HashMap<RigidBody*, DelayedWorldTransform>::Iterator i = delayedWorldTransforms_.Begin();
             i != delayedWorldTransforms_.End(); ++i)
        {
            const DelayedWorldTransform& transform = i->second_;

            // If parent's transform has already been assigned, can proceed
            if (!delayedWorldTransforms_.Contains(transform.parentRigidBody_))
            {
                transform.rigidBody_->ApplyWorldTransform(transform.worldPosition_, transform.worldRotation_);
                delayedWorldTransforms_.Erase(i);
            }
        }
    }
}

void PhysicsWorld::UpdateCollisions()
{
    world_->performDiscreteCollisionDetection();
}

void PhysicsWorld::SetFps(int fps)
{
    fps_ = (unsigned)Clamp(fps, 1, 1000);

    MarkNetworkUpdate();
}

void PhysicsWorld::SetGravity(const Vector3& gravity)
{
    world_->setGravity(ToBtVector3(gravity));

    MarkNetworkUpdate();
}

void PhysicsWorld::SetMaxSubSteps(int num)
{
    maxSubSteps_ = num;
    MarkNetworkUpdate();
}

void PhysicsWorld::SetNumIterations(int num)
{
    num = Clamp(num, 1, MAX_SOLVER_ITERATIONS);
    world_->getSolverInfo().m_numIterations = num;

    MarkNetworkUpdate();
}

void PhysicsWorld::SetInterpolation(bool enable)
{
    interpolation_ = enable;
}

void PhysicsWorld::SetInternalEdge(bool enable)
{
    internalEdge_ = enable;

    MarkNetworkUpdate();
}

void PhysicsWorld::SetSplitImpulse(bool enable)
{
    world_->getSolverInfo().m_splitImpulse = enable;

    MarkNetworkUpdate();
}

void PhysicsWorld::SetMaxNetworkAngularVelocity(float velocity)
{
    maxNetworkAngularVelocity_ = Clamp(velocity, 1.0f, 32767.0f);

    MarkNetworkUpdate();
}

void PhysicsWorld::Raycast(PODVector<PhysicsRaycastResult>& result, const Ray& ray, float maxDistance, unsigned collisionMask)
{
    PROFILE(PhysicsRaycast);

    if (maxDistance >= M_INFINITY)
        LOGWARNING("Infinite maxDistance in physics raycast is not supported");

    btCollisionWorld::AllHitsRayResultCallback
        rayCallback(ToBtVector3(ray.origin_), ToBtVector3(ray.origin_ + maxDistance * ray.direction_));
    rayCallback.m_collisionFilterGroup = (short)0xffff;
    rayCallback.m_collisionFilterMask = (short)collisionMask;

    world_->rayTest(rayCallback.m_rayFromWorld, rayCallback.m_rayToWorld, rayCallback);

    for (int i = 0; i < rayCallback.m_collisionObjects.size(); ++i)
    {
        PhysicsRaycastResult newResult;
        newResult.body_ = static_cast<RigidBody*>(rayCallback.m_collisionObjects[i]->getUserPointer());
        newResult.position_ = ToVector3(rayCallback.m_hitPointWorld[i]);
        newResult.normal_ = ToVector3(rayCallback.m_hitNormalWorld[i]);
        newResult.distance_ = (newResult.position_ - ray.origin_).Length();
        result.Push(newResult);
    }

    Sort(result.Begin(), result.End(), CompareRaycastResults);
}

void PhysicsWorld::RaycastSingle(PhysicsRaycastResult& result, const Ray& ray, float maxDistance, unsigned collisionMask)
{
    PROFILE(PhysicsRaycastSingle);

    if (maxDistance >= M_INFINITY)
        LOGWARNING("Infinite maxDistance in physics raycast is not supported");

    btCollisionWorld::ClosestRayResultCallback
        rayCallback(ToBtVector3(ray.origin_), ToBtVector3(ray.origin_ + maxDistance * ray.direction_));
    rayCallback.m_collisionFilterGroup = (short)0xffff;
    rayCallback.m_collisionFilterMask = (short)collisionMask;

    world_->rayTest(rayCallback.m_rayFromWorld, rayCallback.m_rayToWorld, rayCallback);

    if (rayCallback.hasHit())
    {
        result.position_ = ToVector3(rayCallback.m_hitPointWorld);
        result.normal_ = ToVector3(rayCallback.m_hitNormalWorld);
        result.distance_ = (result.position_ - ray.origin_).Length();
        result.body_ = static_cast<RigidBody*>(rayCallback.m_collisionObject->getUserPointer());
    }
    else
    {
        result.position_ = Vector3::ZERO;
        result.normal_ = Vector3::ZERO;
        result.distance_ = M_INFINITY;
        result.body_ = 0;
    }
}

void PhysicsWorld::SphereCast(PhysicsRaycastResult& result, const Ray& ray, float radius, float maxDistance, unsigned collisionMask)
{
    PROFILE(PhysicsSphereCast);

    if (maxDistance >= M_INFINITY)
        LOGWARNING("Infinite maxDistance in physics sphere cast is not supported");

    btSphereShape shape(radius);

    btCollisionWorld::ClosestConvexResultCallback
        convexCallback(ToBtVector3(ray.origin_), ToBtVector3(ray.origin_ + maxDistance * ray.direction_));
    convexCallback.m_collisionFilterGroup = (short)0xffff;
    convexCallback.m_collisionFilterMask = (short)collisionMask;

    world_->convexSweepTest(&shape, btTransform(btQuaternion::getIdentity(), convexCallback.m_convexFromWorld),
        btTransform(btQuaternion::getIdentity(), convexCallback.m_convexToWorld), convexCallback);

    if (convexCallback.hasHit())
    {
        result.body_ = static_cast<RigidBody*>(convexCallback.m_hitCollisionObject->getUserPointer());
        result.position_ = ToVector3(convexCallback.m_hitPointWorld);
        result.normal_ = ToVector3(convexCallback.m_hitNormalWorld);
        result.distance_ = (result.position_ - ray.origin_).Length();
    }
    else
    {
        result.body_ = 0;
        result.position_ = Vector3::ZERO;
        result.normal_ = Vector3::ZERO;
        result.distance_ = M_INFINITY;
    }
}

void PhysicsWorld::ConvexCast(PhysicsRaycastResult& result, CollisionShape* shape, const Vector3& startPos,
    const Quaternion& startRot, const Vector3& endPos, const Quaternion& endRot, unsigned collisionMask)
{
    if (!shape || !shape->GetCollisionShape())
    {
        LOGERROR("Null collision shape for convex cast");
        result.body_ = 0;
        result.position_ = Vector3::ZERO;
        result.normal_ = Vector3::ZERO;
        result.distance_ = M_INFINITY;
        return;
    }

    // If shape is attached in a rigidbody, set its collision group temporarily to 0 to make sure it is not returned in the sweep result
    RigidBody* bodyComp = shape->GetComponent<RigidBody>();
    btRigidBody* body = bodyComp ? bodyComp->GetBody() : (btRigidBody*)0;
    btBroadphaseProxy* proxy = body ? body->getBroadphaseProxy() : (btBroadphaseProxy*)0;
    short group = 0;
    if (proxy)
    {
        group = proxy->m_collisionFilterGroup;
        proxy->m_collisionFilterGroup = 0;
    }

    // Take the shape's offset position & rotation into account
    Node* shapeNode = shape->GetNode();
    Matrix3x4 startTransform(startPos, startRot, shapeNode ? shapeNode->GetWorldScale() : Vector3::ONE);
    Matrix3x4 endTransform(endPos, endRot, shapeNode ? shapeNode->GetWorldScale() : Vector3::ONE);
    Vector3 effectiveStartPos = startTransform * shape->GetPosition();
    Vector3 effectiveEndPos = endTransform * shape->GetPosition();
    Quaternion effectiveStartRot = startRot * shape->GetRotation();
    Quaternion effectiveEndRot = endRot * shape->GetRotation();

    ConvexCast(result, shape->GetCollisionShape(), effectiveStartPos, effectiveStartRot, effectiveEndPos, effectiveEndRot, collisionMask);

    // Restore the collision group
    if (proxy)
        proxy->m_collisionFilterGroup = group;
}

void PhysicsWorld::ConvexCast(PhysicsRaycastResult& result, btCollisionShape* shape, const Vector3& startPos,
    const Quaternion& startRot, const Vector3& endPos, const Quaternion& endRot, unsigned collisionMask)
{
    if (!shape)
    {
        LOGERROR("Null collision shape for convex cast");
        result.body_ = 0;
        result.position_ = Vector3::ZERO;
        result.normal_ = Vector3::ZERO;
        result.distance_ = M_INFINITY;
        return;
    }

    if (!shape->isConvex())
    {
        LOGERROR("Can not use non-convex collision shape for convex cast");
        result.body_ = 0;
        result.position_ = Vector3::ZERO;
        result.normal_ = Vector3::ZERO;
        result.distance_ = M_INFINITY;
        return;
    }

    PROFILE(PhysicsConvexCast);

    btCollisionWorld::ClosestConvexResultCallback convexCallback(ToBtVector3(startPos), ToBtVector3(endPos));
    convexCallback.m_collisionFilterGroup = (short)0xffff;
    convexCallback.m_collisionFilterMask = (short)collisionMask;

    world_->convexSweepTest(static_cast<btConvexShape*>(shape), btTransform(ToBtQuaternion(startRot),
            convexCallback.m_convexFromWorld), btTransform(ToBtQuaternion(endRot), convexCallback.m_convexToWorld),
        convexCallback);

    if (convexCallback.hasHit())
    {
        result.body_ = static_cast<RigidBody*>(convexCallback.m_hitCollisionObject->getUserPointer());
        result.position_ = ToVector3(convexCallback.m_hitPointWorld);
        result.normal_ = ToVector3(convexCallback.m_hitNormalWorld);
        result.distance_ = (result.position_ - startPos).Length();
    }
    else
    {
        result.body_ = 0;
        result.position_ = Vector3::ZERO;
        result.normal_ = Vector3::ZERO;
        result.distance_ = M_INFINITY;
    }
}

void PhysicsWorld::RemoveCachedGeometry(Model* model)
{
    for (HashMap<Pair<Model*, unsigned>, SharedPtr<CollisionGeometryData> >::Iterator i = triMeshCache_.Begin();
         i != triMeshCache_.End();)
    {
        HashMap<Pair<Model*, unsigned>, SharedPtr<CollisionGeometryData> >::Iterator current = i++;
        if (current->first_.first_ == model)
            triMeshCache_.Erase(current);
    }
    for (HashMap<Pair<Model*, unsigned>, SharedPtr<CollisionGeometryData> >::Iterator i = convexCache_.Begin();
         i != convexCache_.End();)
    {
        HashMap<Pair<Model*, unsigned>, SharedPtr<CollisionGeometryData> >::Iterator current = i++;
        if (current->first_.first_ == model)
            convexCache_.Erase(current);
    }
}

void PhysicsWorld::GetRigidBodies(PODVector<RigidBody*>& result, const Sphere& sphere, unsigned collisionMask)
{
    PROFILE(PhysicsSphereQuery);

    result.Clear();

    btSphereShape sphereShape(sphere.radius_);
    btRigidBody* tempRigidBody = new btRigidBody(1.0f, 0, &sphereShape);
    tempRigidBody->setWorldTransform(btTransform(btQuaternion::getIdentity(), ToBtVector3(sphere.center_)));
    // Need to activate the temporary rigid body to get reliable results from static, sleeping objects
    tempRigidBody->activate();
    world_->addRigidBody(tempRigidBody);

    PhysicsQueryCallback callback(result, collisionMask);
    world_->contactTest(tempRigidBody, callback);

    world_->removeRigidBody(tempRigidBody);
    delete tempRigidBody;
}

void PhysicsWorld::GetRigidBodies(PODVector<RigidBody*>& result, const BoundingBox& box, unsigned collisionMask)
{
    PROFILE(PhysicsBoxQuery);

    result.Clear();

    btBoxShape boxShape(ToBtVector3(box.HalfSize()));
    btRigidBody* tempRigidBody = new btRigidBody(1.0f, 0, &boxShape);
    tempRigidBody->setWorldTransform(btTransform(btQuaternion::getIdentity(), ToBtVector3(box.Center())));
    tempRigidBody->activate();
    world_->addRigidBody(tempRigidBody);

    PhysicsQueryCallback callback(result, collisionMask);
    world_->contactTest(tempRigidBody, callback);

    world_->removeRigidBody(tempRigidBody);
    delete tempRigidBody;
}

void PhysicsWorld::GetRigidBodies(PODVector<RigidBody*>& result, const RigidBody* body)
{
    PROFILE(GetCollidingBodies);

    result.Clear();

    for (HashMap<Pair<WeakPtr<RigidBody>, WeakPtr<RigidBody> >, btPersistentManifold*>::Iterator i = currentCollisions_.Begin();
         i != currentCollisions_.End(); ++i)
    {
        if (i->first_.first_ == body)
            result.Push(i->first_.second_);
        else if (i->first_.second_ == body)
            result.Push(i->first_.first_);
    }
}

Vector3 PhysicsWorld::GetGravity() const
{
    return ToVector3(world_->getGravity());
}

int PhysicsWorld::GetNumIterations() const
{
    return world_->getSolverInfo().m_numIterations;
}

bool PhysicsWorld::GetSplitImpulse() const
{
    return world_->getSolverInfo().m_splitImpulse != 0;
}

void PhysicsWorld::AddRigidBody(RigidBody* body)
{
    rigidBodies_.Push(body);
}

void PhysicsWorld::RemoveRigidBody(RigidBody* body)
{
    rigidBodies_.Remove(body);
    // Remove possible dangling pointer from the delayedWorldTransforms structure
    delayedWorldTransforms_.Erase(body);
}


//===================================
void PhysicsWorld::AddSoftBody(SoftBody* body)
{
    softBodies_.Push(body);
}

void PhysicsWorld::RemoveSoftBody(SoftBody* body)
{
    softBodies_.Remove(body);
}
//===================================


void PhysicsWorld::AddCollisionShape(CollisionShape* shape)
{
    collisionShapes_.Push(shape);
}

void PhysicsWorld::RemoveCollisionShape(CollisionShape* shape)
{
    collisionShapes_.Remove(shape);
}

void PhysicsWorld::AddConstraint(Constraint* constraint)
{
    constraints_.Push(constraint);
}

void PhysicsWorld::RemoveConstraint(Constraint* constraint)
{
    constraints_.Remove(constraint);
}

void PhysicsWorld::AddDelayedWorldTransform(const DelayedWorldTransform& transform)
{
    delayedWorldTransforms_[transform.rigidBody_] = transform;
}

void PhysicsWorld::DrawDebugGeometry(bool depthTest)
{
    DebugRenderer* debug = GetComponent<DebugRenderer>();
    DrawDebugGeometry(debug, depthTest);
}

void PhysicsWorld::SetDebugRenderer(DebugRenderer* debug)
{
    debugRenderer_ = debug;
}

void PhysicsWorld::SetDebugDepthTest(bool enable)
{
    debugDepthTest_ = enable;
}

void PhysicsWorld::CleanupGeometryCache()
{
    // Remove cached shapes whose only reference is the cache itself
    for (HashMap<Pair<Model*, unsigned>, SharedPtr<CollisionGeometryData> >::Iterator i = triMeshCache_.Begin();
         i != triMeshCache_.End();)
    {
        HashMap<Pair<Model*, unsigned>, SharedPtr<CollisionGeometryData> >::Iterator current = i++;
        if (current->second_.Refs() == 1)
            triMeshCache_.Erase(current);
    }
    for (HashMap<Pair<Model*, unsigned>, SharedPtr<CollisionGeometryData> >::Iterator i = convexCache_.Begin();
         i != convexCache_.End();)
    {
        HashMap<Pair<Model*, unsigned>, SharedPtr<CollisionGeometryData> >::Iterator current = i++;
        if (current->second_.Refs() == 1)
            convexCache_.Erase(current);
    }
}

void PhysicsWorld::OnSceneSet(Scene* scene)
{
    // Subscribe to the scene subsystem update, which will trigger the physics simulation step
    if (scene)
    {
        scene_ = GetScene();
        SubscribeToEvent(scene_, E_SCENESUBSYSTEMUPDATE, HANDLER(PhysicsWorld, HandleSceneSubsystemUpdate));
    }
    else
        UnsubscribeFromEvent(E_SCENESUBSYSTEMUPDATE);
}

void PhysicsWorld::HandleSceneSubsystemUpdate(StringHash eventType, VariantMap& eventData)
{
    using namespace SceneSubsystemUpdate;

    Update(eventData[P_TIMESTEP].GetFloat());
}

void PhysicsWorld::PreStep(float timeStep)
{
    // Send pre-step event
    using namespace PhysicsPreStep;

    VariantMap& eventData = GetEventDataMap();
    eventData[P_WORLD] = this;
    eventData[P_TIMESTEP] = timeStep;
    SendEvent(E_PHYSICSPRESTEP, eventData);

    // Start profiling block for the actual simulation step
#ifdef URHO3D_PROFILING
    Profiler* profiler = GetSubsystem<Profiler>();
    if (profiler)
        profiler->BeginBlock("StepSimulation");
#endif
}

void PhysicsWorld::PostStep(float timeStep)
{
#ifdef URHO3D_PROFILING
    Profiler* profiler = GetSubsystem<Profiler>();
    if (profiler)
        profiler->EndBlock();
#endif

    SendCollisionEvents();

    // Send post-step event
    using namespace PhysicsPostStep;

    VariantMap& eventData = GetEventDataMap();
    eventData[P_WORLD] = this;
    eventData[P_TIMESTEP] = timeStep;
    SendEvent(E_PHYSICSPOSTSTEP, eventData);
}

void PhysicsWorld::SendCollisionEvents()
{
    PROFILE(SendCollisionEvents);

    currentCollisions_.Clear();
    physicsCollisionData_.Clear();
    nodeCollisionData_.Clear();

    int numManifolds = collisionDispatcher_->getNumManifolds();

    if (numManifolds)
    {
        physicsCollisionData_[PhysicsCollision::P_WORLD] = this;

        for (int i = 0; i < numManifolds; ++i)
        {
            btPersistentManifold* contactManifold = collisionDispatcher_->getManifoldByIndexInternal(i);
            // First check that there are actual contacts, as the manifold exists also when objects are close but not touching
            if (!contactManifold->getNumContacts())
                continue;

            const btCollisionObject* objectA = contactManifold->getBody0();
            const btCollisionObject* objectB = contactManifold->getBody1();

            RigidBody* bodyA = static_cast<RigidBody*>(objectA->getUserPointer());
            RigidBody* bodyB = static_cast<RigidBody*>(objectB->getUserPointer());
            // If it's not a rigidbody, maybe a ghost object
            if (!bodyA || !bodyB)
                continue;

            // Skip collision event signaling if both objects are static, or if collision event mode does not match
            if (bodyA->GetMass() == 0.0f && bodyB->GetMass() == 0.0f)
                continue;
            if (bodyA->GetCollisionEventMode() == COLLISION_NEVER || bodyB->GetCollisionEventMode() == COLLISION_NEVER)
                continue;
            if (bodyA->GetCollisionEventMode() == COLLISION_ACTIVE && bodyB->GetCollisionEventMode() == COLLISION_ACTIVE &&
                !bodyA->IsActive() && !bodyB->IsActive())
                continue;

            WeakPtr<RigidBody> bodyWeakA(bodyA);
            WeakPtr<RigidBody> bodyWeakB(bodyB);

            Pair<WeakPtr<RigidBody>, WeakPtr<RigidBody> > bodyPair;
            if (bodyA < bodyB)
                bodyPair = MakePair(bodyWeakA, bodyWeakB);
            else
                bodyPair = MakePair(bodyWeakB, bodyWeakA);

            // First only store the collision pair as weak pointers and the manifold pointer, so user code can safely destroy
            // objects during collision event handling
            currentCollisions_[bodyPair] = contactManifold;
        }

        for (HashMap<Pair<WeakPtr<RigidBody>, WeakPtr<RigidBody> >, btPersistentManifold*>::Iterator i = currentCollisions_.Begin();
             i != currentCollisions_.End(); ++i)
        {
            RigidBody* bodyA = i->first_.first_;
            RigidBody* bodyB = i->first_.second_;
            if (!bodyA || !bodyB)
                continue;

            btPersistentManifold* contactManifold = i->second_;

            Node* nodeA = bodyA->GetNode();
            Node* nodeB = bodyB->GetNode();
            WeakPtr<Node> nodeWeakA(nodeA);
            WeakPtr<Node> nodeWeakB(nodeB);

            bool trigger = bodyA->IsTrigger() || bodyB->IsTrigger();
            bool newCollision = !previousCollisions_.Contains(i->first_);

            physicsCollisionData_[PhysicsCollision::P_NODEA] = nodeA;
            physicsCollisionData_[PhysicsCollision::P_NODEB] = nodeB;
            physicsCollisionData_[PhysicsCollision::P_BODYA] = bodyA;
            physicsCollisionData_[PhysicsCollision::P_BODYB] = bodyB;
            physicsCollisionData_[PhysicsCollision::P_TRIGGER] = trigger;

            contacts_.Clear();

            for (int j = 0; j < contactManifold->getNumContacts(); ++j)
            {
                btManifoldPoint& point = contactManifold->getContactPoint(j);
                contacts_.WriteVector3(ToVector3(point.m_positionWorldOnB));
                contacts_.WriteVector3(ToVector3(point.m_normalWorldOnB));
                contacts_.WriteFloat(point.m_distance1);
                contacts_.WriteFloat(point.m_appliedImpulse);
            }

            physicsCollisionData_[PhysicsCollision::P_CONTACTS] = contacts_.GetBuffer();

            // Send separate collision start event if collision is new
            if (newCollision)
            {
                SendEvent(E_PHYSICSCOLLISIONSTART, physicsCollisionData_);
                // Skip rest of processing if either of the nodes or bodies is removed as a response to the event
                if (!nodeWeakA || !nodeWeakB || !i->first_.first_ || !i->first_.second_)
                    continue;
            }

            // Then send the ongoing collision event
            SendEvent(E_PHYSICSCOLLISION, physicsCollisionData_);
            if (!nodeWeakA || !nodeWeakB || !i->first_.first_ || !i->first_.second_)
                continue;

            nodeCollisionData_[NodeCollision::P_BODY] = bodyA;
            nodeCollisionData_[NodeCollision::P_OTHERNODE] = nodeB;
            nodeCollisionData_[NodeCollision::P_OTHERBODY] = bodyB;
            nodeCollisionData_[NodeCollision::P_TRIGGER] = trigger;
            nodeCollisionData_[NodeCollision::P_CONTACTS] = contacts_.GetBuffer();

            if (newCollision)
            {
                nodeA->SendEvent(E_NODECOLLISIONSTART, nodeCollisionData_);
                if (!nodeWeakA || !nodeWeakB || !i->first_.first_ || !i->first_.second_)
                    continue;
            }

            nodeA->SendEvent(E_NODECOLLISION, nodeCollisionData_);
            if (!nodeWeakA || !nodeWeakB || !i->first_.first_ || !i->first_.second_)
                continue;

            contacts_.Clear();
            for (int j = 0; j < contactManifold->getNumContacts(); ++j)
            {
                btManifoldPoint& point = contactManifold->getContactPoint(j);
                contacts_.WriteVector3(ToVector3(point.m_positionWorldOnB));
                contacts_.WriteVector3(-ToVector3(point.m_normalWorldOnB));
                contacts_.WriteFloat(point.m_distance1);
                contacts_.WriteFloat(point.m_appliedImpulse);
            }

            nodeCollisionData_[NodeCollision::P_BODY] = bodyB;
            nodeCollisionData_[NodeCollision::P_OTHERNODE] = nodeA;
            nodeCollisionData_[NodeCollision::P_OTHERBODY] = bodyA;
            nodeCollisionData_[NodeCollision::P_CONTACTS] = contacts_.GetBuffer();

            if (newCollision)
            {
                nodeB->SendEvent(E_NODECOLLISIONSTART, nodeCollisionData_);
                if (!nodeWeakA || !nodeWeakB || !i->first_.first_ || !i->first_.second_)
                    continue;
            }

            nodeB->SendEvent(E_NODECOLLISION, nodeCollisionData_);
        }
    }

    // Send collision end events as applicable
    {
        physicsCollisionData_[PhysicsCollisionEnd::P_WORLD] = this;

        for (HashMap<Pair<WeakPtr<RigidBody>, WeakPtr<RigidBody> >, btPersistentManifold*>::Iterator
                 i = previousCollisions_.Begin(); i != previousCollisions_.End(); ++i)
        {
            if (!currentCollisions_.Contains(i->first_))
            {
                RigidBody* bodyA = i->first_.first_;
                RigidBody* bodyB = i->first_.second_;
                if (!bodyA || !bodyB)
                    continue;

                bool trigger = bodyA->IsTrigger() || bodyB->IsTrigger();

                // Skip collision event signaling if both objects are static, or if collision event mode does not match
                if (bodyA->GetMass() == 0.0f && bodyB->GetMass() == 0.0f)
                    continue;
                if (bodyA->GetCollisionEventMode() == COLLISION_NEVER || bodyB->GetCollisionEventMode() == COLLISION_NEVER)
                    continue;
                if (bodyA->GetCollisionEventMode() == COLLISION_ACTIVE && bodyB->GetCollisionEventMode() == COLLISION_ACTIVE &&
                    !bodyA->IsActive() && !bodyB->IsActive())
                    continue;

                Node* nodeA = bodyA->GetNode();
                Node* nodeB = bodyB->GetNode();
                WeakPtr<Node> nodeWeakA(nodeA);
                WeakPtr<Node> nodeWeakB(nodeB);

                physicsCollisionData_[PhysicsCollisionEnd::P_BODYA] = bodyA;
                physicsCollisionData_[PhysicsCollisionEnd::P_BODYB] = bodyB;
                physicsCollisionData_[PhysicsCollisionEnd::P_NODEA] = nodeA;
                physicsCollisionData_[PhysicsCollisionEnd::P_NODEB] = nodeB;
                physicsCollisionData_[PhysicsCollisionEnd::P_TRIGGER] = trigger;

                SendEvent(E_PHYSICSCOLLISIONEND, physicsCollisionData_);
                // Skip rest of processing if either of the nodes or bodies is removed as a response to the event
                if (!nodeWeakA || !nodeWeakB || !i->first_.first_ || !i->first_.second_)
                    continue;

                nodeCollisionData_[NodeCollisionEnd::P_BODY] = bodyA;
                nodeCollisionData_[NodeCollisionEnd::P_OTHERNODE] = nodeB;
                nodeCollisionData_[NodeCollisionEnd::P_OTHERBODY] = bodyB;
                nodeCollisionData_[NodeCollisionEnd::P_TRIGGER] = trigger;

                nodeA->SendEvent(E_NODECOLLISIONEND, nodeCollisionData_);
                if (!nodeWeakA || !nodeWeakB || !i->first_.first_ || !i->first_.second_)
                    continue;

                nodeCollisionData_[NodeCollisionEnd::P_BODY] = bodyB;
                nodeCollisionData_[NodeCollisionEnd::P_OTHERNODE] = nodeA;
                nodeCollisionData_[NodeCollisionEnd::P_OTHERBODY] = bodyA;

                nodeB->SendEvent(E_NODECOLLISIONEND, nodeCollisionData_);
            }
        }
    }

    previousCollisions_ = currentCollisions_;
}

void RegisterPhysicsLibrary(Context* context)
{
    CollisionShape::RegisterObject(context);
    RigidBody::RegisterObject(context);
    Constraint::RegisterObject(context);
    PhysicsWorld::RegisterObject(context);
    SoftBody::RegisterObject(context); // Register softbody ============================
}

}
[/code][/spoiler]

-------------------------

codingmonkey | 2017-01-02 01:06:55 UTC | #12

Great work man! Thanks.
Next step I guess is using vertexes group for pinning and use vertex.color for btSoftBody.m_node stiffness ?
also maybe add air vector for interface SoftBody component ?

did you trying to do stress test with high count of SB component on desktop pc ? how many fps you are got with 1000 SB in scene ?)

-------------------------

Mike | 2017-01-02 01:06:55 UTC | #13

Thanks, the most important thing that is missing is the ability to sync body and node positions, and for now I'm stuck with this. Any help is welcome.

-------------------------

codingmonkey | 2017-03-17 18:59:30 UTC | #14

I think that you need change this
class URHO3D_API SoftBody : public Component
to this
class URHO3D_API SoftBody : public Component, public btMotionState

in this case you are got two virtual functions

[code]/// Return initial world transform to Bullet.
 virtual void getWorldTransform(btTransform& worldTrans) const;
/// Update world transform from Bullet.
 virtual void setWorldTransform(const btTransform& worldTrans);
[/code]

I'm also stuck but with implementing who will be rendered simulated cloth? SB by it's own or it will be just put processed cloth into other drawable, maybe StaticModel like in yours implementation.  

My current implementation of SB but I do not tested it yet and don't know works it or no )
SoftBody.h
[spoiler]
http://pastebin.com/QEby4QeN
[/spoiler]

SoftBody.cpp
[spoiler]
http://pastebin.com/jZR4dd8t
[/spoiler]

-------------------------

codingmonkey | 2017-03-17 19:00:44 UTC | #15

I rewrite some parts of my implementation of SB and it's all most like Mike's SB with staticmodel + softbody. 
It still have a few weird problems, by I try solve it one by one. 
And main problem is:
I do not understand why my SB falling though floor plane and do not bounced from it.
I tried various collision flags for SB body in component.
body_->m_cfg.collisions = btSoftBody::fCollision::CL_RS + btSoftBody::fCollision::CL_SS; 
and various CollisionShapes for plane
but in still no working properly 

there is my current test code
[spoiler]
http://pastebin.com/0B0YWfjv
[/spoiler]

and this is some changes that I made for physics
[github.com/MonkeyFirst/Urho3D/tree/sbtest](https://github.com/MonkeyFirst/Urho3D/tree/sbtest)

now I have worked manual pinnig and sphere.mdl are now hangs on this vertex and do not fall down but still collision with RigidBody not working

-------------------------

Lumak | 2017-01-02 01:06:58 UTC | #16

I downloaded your branch tag. I'll try to reproduce this bug today.

-------------------------

codingmonkey | 2017-01-02 01:06:58 UTC | #17

Currently I found issue why sphere falling though floor plane. 
The problem lays in case of different placement of the physic body_ and his graphic representation - StaticModel. 
If body_ lay on plane(floor) at some moment but his StaticModel still placed in air, but if we create some other colliders and push they into empty space where placed non-visible physic body_ - StaticModel began move.
it's all very complicated.

I found some useful examples with Ogre's SofBody
and get some methods from this topics: [bulletphysics.org/Bullet/phpBB3/ ... c9bd045dca](http://bulletphysics.org/Bullet/phpBB3/viewtopic.php?f=9&t=3428&sid=6b8eba4bcf2c6152eb7098c9bd045dca)

I do not understand if I create SB from original mesh (with dupVerts, from as it is)
btSoftBodyWorldInfo* softBodyWorldInfo_ = GetPhysicsWorld()->GetSoftBodyWorld();
body_ = btSoftBodyHelpers::CreateFromTriMesh(*softBodyWorldInfo_, vertices[0], &indexes[0], ntriangles);

Is it still need to do SB->appendLink() and SB->appendFace() after creation or no ?

Also Bullent provides the btTriangleIndexVertexArray, and I don't know maybe needed use it for create mesh and only then pass it in  btSoftBodyHelpers::CreateFromTriMesh ?

-------------------------

Lumak | 2017-01-02 01:06:58 UTC | #18

Good to hear that you worked it out.  I got your code working but the physics behavior is very different than my original - the mushroom caps get flattened whey the model hits the ground for some reason.

In regards to the renderables and softbody vertex buffer, both need to use the same vertex buffer, otherwise, you'll see a mismatch.

Steps to use the vertex buffer would be:
1) clone the model. the original model's verts/index buffer should not be used in case the model is instanced several times in the scene.
2) remove duplicate verts/indeces from the cloned model's verts buffer (this should be moved to the VertexBuffer class eventually) -> new verts and index buffer
3) assign the new verts/index buffer to the StaticModelt->SetModel( cloneModel );
4) create softbody from the same verts/index buffer which creates appLinks and Faces

Awesome job with the PhysicsWorld and SoftBody class updates.

edit: I had the same exact problem with the softbody not becoming active and had to call 1) SetMass() to place the softbody into the world and then 2) manually call Activate() to activate the body.

-------------------------

Lumak | 2017-01-02 01:07:01 UTC | #19

I figured out what was causing the differences in physics behavior from my sample code to what I built from your branch tag. I'll list them:
a) calling setInterpolationWorldTransform() causes the object to be placed offset from the position specified and sometimes got buried in the ground - I changed this to setTransform() and the object is placed where I specified.
b) whenever setTotalMass() is called, a call to setPose() must be called as the object's face mass/inverse mass is dependent on totalMass 
c) higher the mass of the object, harder for colliding objects to penetrate the softbody and the colliding objects bounce off at faster velocity, lesser mass would cause objects to penetrate more easily. - changed it to mass of 50 and colliders didn't penetrate on the caps.

-------------------------

Lumak | 2017-01-02 01:07:19 UTC | #20

Uploaded a progress video, see the OP.

-------------------------

George | 2017-01-02 01:07:21 UTC | #21

Hi,
This looks good. Works great.

I found a few issues.
Loading Jack.mdl will cause an error. 
Mushroom disappear at numeric angles.
Large performance reduction when loading teapot.

disjointed vertices edges as vertices deform.
Regards

-------------------------

Lumak | 2017-01-02 01:07:23 UTC | #22

I will have to merge my changes to codemonkey's branch eventually, but my changes won't fix:
-performance issue with high poly count like teapot
-issues with skinned mesh, which also results in performance hit.

It can however, load jack.mdl, and fix disjointed verts or duplicate verts.
Frankly, while softbody dynamics look cool, I'm not sure if it's even applicable for games due to performance reasons.

-------------------------

suncore | 2017-01-02 01:13:34 UTC | #23

Hi! I'm trying to get started on softbody physics, but it's difficult since I'm not really familiar with the codebase (Urho3d).
So what happened to this work? Is there a branch on github I can look at?

-- Henrik

-------------------------

Lumak | 2017-01-02 01:13:34 UTC | #24

I was using codingmonkey's repo, [url]https://github.com/MonkeyFirst/Urho3D/tree/sbtest[/url]

-------------------------

suncore | 2017-01-02 01:13:34 UTC | #25

Thanks, but that link does not work any more.

-------------------------

codingmonkey | 2017-03-17 19:56:37 UTC | #26

>I was using codingmonkey's

)) but i remember when I start to figure out with this SB I'm use your code and mike's code and ogre's forum  :smiley:

>Thanks, but that link does not work any more.

Yes, probably i also dont have it even on my hdd ( 
but all code changes (sources) are in this theme - hided by code/spoilers tag.
I also remember last bug with my SB: i have huge offset between visual SB representation and it physic representation.

-------------------------

Miegamicis | 2017-01-02 01:13:39 UTC | #27

This looks interesting. Will give it a go  :slight_smile:

-------------------------

sabotage3d | 2017-01-02 01:14:54 UTC | #28

Hey guys have anyone tried the tetra based solids?

-------------------------

Sir_Nate | 2017-01-02 01:14:54 UTC | #29

Just wondering if the "Remove Doubles" operator in Blender has a flaw that makes it not work for this case (I think it may have been added in a newer version of Blender, so perhaps that is why you wrote the mesh pruning algorithm)? (You just have to select the whole mesh in edit mode, and then Ctrl-V (or Mesh>Vertices) and select Remove Doubles, or just press space and type "Remove Doubles")

-------------------------

Lumak | 2017-01-02 01:14:55 UTC | #30

[quote="Sir Nate"]Just wondering if the "Remove Doubles" operator in Blender has a flaw that makes it not work for this case (I think it may have been added in a newer version of Blender, so perhaps that is why you wrote the mesh pruning algorithm)? (You just have to select the whole mesh in edit mode, and then Ctrl-V (or Mesh>Vertices) and select Remove Doubles, or just press space and type "Remove Doubles")[/quote]

That's not the problem. You can have a perfect model w/o any duplicate verts in a 3D modeling tool and you'll still get this problem.
The duplicate verts problem occurs whenever you apply a UV map to a 3D model (but not a 2D model). 

Look at this image:
[img]http://i.imgur.com/c3NlP7z.jpg[/img]

The vertex V1 in the pic depicts having a UV pair, and this occurs if a vertex happen to be mapped to a uv point on the edge of the uv map. And when the entire column/row of verts become mapped to uv points on the edge, you'll get what looks like a tearing problem in softbody.

-------------------------

sabotage3d | 2017-01-02 01:14:56 UTC | #31

Well the idea is to have a cage sim mesh to deform the render mesh, then you won't have to remove duplicate verts.

-------------------------

Lumak | 2018-04-04 21:34:35 UTC | #32

latest repo: https://github.com/Lumak/Urho3D-SoftBody

I'll also add the link to the latest vid if anyone missed it:
https://youtu.be/SvdpjhA-Mq8

-------------------------

Lumak | 2019-08-07 15:15:59 UTC | #33

Repo updated with performance enhancement and initial stick position.

-------------------------

elix22 | 2019-08-07 16:16:55 UTC | #34

Welcome back :)
..........................

-------------------------

suppagam | 2019-08-07 16:18:28 UTC | #35

@Lumak is the best Urho3D coder around. :heart_eyes:

-------------------------

dertom | 2019-08-09 14:58:23 UTC | #36

I wonder why this never found its way into the engine!?

-------------------------

Modanung | 2019-08-09 19:55:02 UTC | #37

Because you never added it. ;)

-------------------------

Lumak | 2019-08-11 15:09:07 UTC | #38

Softbody will not make it into the engine for two reasons:
* does not follow engine's model-node implementation, i.e. due to performance issues softbody nodes are in world space, Urho3D nodes set at origin, and renderable geometry kept in world space. To conform to the engine's model-node convention, the renderable geometry need to be converted to local space.
* feature incomplete. You can see the Bullet's softbody example and see all that's missing. What's added in my repo are what's mentioned/discussed in the thread.

-------------------------

Modanung | 2019-08-11 14:22:14 UTC | #39

Maybe we should create a branch for this in the main repo?

-------------------------

Lumak | 2019-08-11 15:00:50 UTC | #40

I think softbody is a niche feature, something that's not commonly used in games -- this might be a third reason for not making it into the engine.

-------------------------

Modanung | 2019-08-11 17:45:16 UTC | #41

Indeed it may be entering the grey area of keeping the engine _lightweight_. But Bullet *is* delivered in its entirety with Urho and I think its soft body functionality can be considered on par with the `RaycastVehicle` [spoiler]- which was also not added by @Cadaver -[/spoiler] when looking at how often they are generally used in games.

Who *doesn't* want a dune buggy adorned with waving worn rags and swaying antennae? ;)
I'll turn that into a nice sample when it can be done using only default Urho components. :cake:
[details=Impression]
![Impression|555x415](upload://4KAVSLijy5kzxkhS8fuqhNssAc7.png) 
[/details]

-------------------------

Modanung | 2019-08-11 17:43:47 UTC | #42

Let me put it this way:
#### Should Bullet's soft body physics features be exposed through default engine components?
[poll type=regular results=always public=true]
* Yes, I would like that
* No, it is too niche for Urho
[/poll]
Welcome to the forums, @bejer! :confetti_ball: :slightly_smiling_face:

-------------------------

Modanung | 2019-08-13 10:16:09 UTC | #43

Let me remind you: There is also the *Urho3D-Components* repository for extras.

https://github.com/urho3d/Urho3D-Components

Maybe it could grow on a branch there and be merged into *its* master first, and possibly into core later.
This route may increase the chance of the [baton being passed](https://en.wikipedia.org/wiki/Relay_race) until the component is ready for core.

-------------------------

Sinoid | 2019-08-12 20:22:40 UTC | #44

Doesn't serialize/deserialize (probably crashes by the looks of it), mesh links aren't setup particularly well - shapes will invert themselves easily since there are no *drumhead* links, the mesh canonicalization is sketchy, and there are helper methods that belong in a sample and not the class itself. 

The first is a serious reason to not have been brought into master (**everything** serializes and deserializes in some fashion), the 2nd is technical and arguable if it should even try, and the latter two are *meh*. That's just a quick skim read of it, there's probably more - a lot more if counting the quirky unreliability of Bullet to not be crazy or incompetent.

-------------------------

Lumak | 2019-08-14 12:25:41 UTC | #45

I never know if you're drunk and/or high when you post anything on the forum, but let me tell you that I'm not into listening to your canonical BS on any topic. 

When I found Urho3D, I reviewed your lightmapper repo thinking I could learn something since you spoke of yourself as if you were a graphics guru. And I have to admit it looked great on the surface, BUT I soon realized you over complicate and over engineer your work which result in poor performance and poor results. I suspect you wouldn't know what an elegant solution is if it hit you in the face.

-------------------------

Leith | 2019-08-14 12:46:15 UTC | #46

Be calm friend, there is nothing about the topic (softbody) that can be done optimally (simply yes, optimally never). Let's not get off topic. It's a bad habit we apparently share.
I have some ideas for optimizing softbodies, if you care to hear about it.

-------------------------

