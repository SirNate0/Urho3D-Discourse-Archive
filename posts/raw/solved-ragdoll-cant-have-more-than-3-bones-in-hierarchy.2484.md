slapin | 2017-01-02 01:15:43 UTC | #1

As I found-out, any chain in ragdoll can't be more than
3 bones from root to any point, otherwise it explodes.
Looks like bug. Unity and UE4 work with this model without any problems.
Variating mass and various other parameters surprisingly make no difference at all.
Is it Bullet limitation or some Urho thing?
If I just set single chest at root and add 2 bones per limb and one for head it works, but looks really
like Jack - too rigid and not interesting for actual model.
Any ideas?

[youtu.be/2HCR7g2j41E](https://youtu.be/2HCR7g2j41E)

EDIT:

OK, I solved a problem. I fine-tuned ragdoll to avoid too much strain
on constraints, and set physicsWorld.fps = 100, which made it not penetrate surface.
Now I just have to tune bones a bit.

[youtu.be/5Bm1lf4-K8k](https://youtu.be/5Bm1lf4-K8k)

-------------------------

Modanung | 2017-01-02 01:15:43 UTC | #2

Did you try turning off collision on the constraints when making them, like in the sample? Also I'm wondering what the big capsule collision shape is doing there.
Mind sharing the relevant bit of code?

-------------------------

slapin | 2017-01-02 01:15:43 UTC | #3

Well, I partially solved the problem. The basic idea:

0. Don't use ragdoll example, it is confusing. Only use it as reference for what contraints can you use
for which limbs and some reference for limits, not more. It will not work for your skeleton.
0.1 Represent all your constraint positions and rotations in global space for your reference,
and convert to bone local space when actually create bone bodies and constraints.
1. The more bones in ragdoll, the less stable it will be.
2. To improve situation one can do the following to improve stability:
- Increase bone collision sizes
- make sure all (most) of your bones can relax on ground not hanging on constraints. Hanging on constraints reduce stability.
- sometimes adding extra bone improves stability. this happens if your ragdoll is forced on constraint's limits for long time.
this helps it relax a bit. This is mainly relevant for spine though, not for limbs.
- for your biggest mass body parts (spine, chest, pelvis, head, root) use boxes. they tend to stabilize quicker.
Yes, use box for head.
3. Limbs and head tend to penetrate landscape and become super unstable. Use the following script on node to avoid that (or make it less frequent)
[code]
class RagdollPreventIntersection: ScriptObject {
    Vector3 last_pos;
    Vector3 vel;
    void FixedUpdate(float timeStep)
    {
        RigidBody@ body = node.GetComponent("RigidBody");
        if (body is null)
            return;
        Vector3 direction = (node.worldPosition - last_pos).Normalized();
        Ray prev(node.worldPosition, direction);
        RayQueryResult result = sc.octree.RaycastSingle(prev, RAY_TRIANGLE, (node.worldPosition - last_pos).length, DRAWABLE_GEOMETRY);
        if (result.drawable !is null && result.drawable.node is floorNode) {
            Vector3 dv = body.position - last_pos;
            body.position = (body.position + last_pos) / 2.0;
        } else
            last_pos = body.position;
    }
    void Start()
    {
        RigidBody@ body = node.GetComponent("RigidBody");
        if (body !is null) {
            last_pos = body.position;
            vel = body.linearVelocity;
            body.restitution = 0.01f;
            body.ccdRadius = 0.05f;
            body.ccdMotionThreshold = 0.05f;
        }
    }
}
[/code]
But this script should be switched off after some stable pose occured as it will prevent body from resting.

4. Hierarchy of rigid bodies is a problem - unstable root bone can make whole body not rest and jitter. The more bones here
in line the herder for them to be stable. Keep very careful attention on upper hierarchy bones.

5. Sometimes constraints are not strong enough to keep your ragdoll stable. Sometimes limb outstretches and
can't find rest. Especially bottom part (legs). I have not solved this one yet for legs, but upper body is pretty stable.

I have remaining problem of leg separation - the upper part of leg separates from root and ends up under terrain or lying outstretched with constraint wiggling like mad. Looks like it can't cope with so much bones in ragdoll which I have.
It is strange, but in Unity using ragdoll wizard and nothing else the ragdoll is very stable. But AFAIR Unity uses PhysX, not Bullet.
So I wonder if it is Bullet limitation.

-------------------------

slapin | 2017-01-02 01:15:43 UTC | #4

Also I can't really get ragdolls to rest, when added arms. While spine-only ragdolls get to rest in a few minutes,
as I add arms they never get to rest and penetrate surface more often.

[youtu.be/XfoDsP-uNpw](https://youtu.be/XfoDsP-uNpw)

I will provide script as I clean it, as it looks a bit exploded now.

-------------------------

slapin | 2017-01-02 01:15:44 UTC | #5

Yep, and capsule is not active at the time, it is just there displayed by DebugRenderer.

-------------------------

Lumak | 2017-01-02 01:15:44 UTC | #6

Capsule colors indicate their state and white means they're active. I've looked at the Urho's ragdoll sample and in that the capsule is removed when the ragdoll is activated.  Perhaps, you just need to do the same to correct the craziness that's going on.

-------------------------

slapin | 2017-01-02 01:15:45 UTC | #7

I just set main body.enabled = false I really wonder how can it affect anything.
I think I can disable capsule too. Removing seems overkill as I will need them for recovery...

-------------------------

Lumak | 2017-01-02 01:15:45 UTC | #8

Just setting it to false only works if it'll never collide with anything else in the world ever, but as soon as it collides with another body this code
[code]
void RigidBody::ApplyForce(const Vector3& force)
{
    if (body_ && force != Vector3::ZERO)
    {
        Activate();
        body_->applyCentralForce(ToBtVector3(force));
    }
}

[/code]

Activates it.

-------------------------

Lumak | 2017-01-02 02:11:39 UTC | #9

Created some images which may help.
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/648a85255dd3c459f3d89166e9d1862240d78e44.jpg[/img]
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/7e2702d637500c0cfc2b84e27fed2fb1866c0299.jpg[/img]

And code to setup the capsules correctly.
[spoiler][code]
//
// Copyright (c) 2008-2016 the Urho3D project.
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

#include <Urho3D/Graphics/AnimatedModel.h>
#include <Urho3D/IO/Log.h>
#include <Urho3D/Physics/PhysicsEvents.h>
#include <Urho3D/Physics/RigidBody.h>

#include "CreateRagdoll.h"

#include <Urho3D/DebugNew.h>

CreateRagdoll::CreateRagdoll(Context* context) :
    Component(context)
{
}

void CreateRagdoll::OnNodeSet(Node* node)
{
    // If the node pointer is non-null, this component has been created into a scene node. Subscribe to physics collisions that
    // concern this scene node
    if (node)
        SubscribeToEvent(node, E_NODECOLLISION, URHO3D_HANDLER(CreateRagdoll, HandleNodeCollision));
}

void CreateRagdoll::HandleNodeCollision(StringHash eventType, VariantMap& eventData)
{
    using namespace NodeCollision;

    // Get the other colliding body, make sure it is moving (has nonzero mass)
    RigidBody* otherBody = static_cast<RigidBody*>(eventData[P_OTHERBODY].GetPtr());

    if (otherBody->GetMass() > 0.0f)
    {
        // We do not need the physics components in the AnimatedModel's root scene node anymore
        node_->RemoveComponent<RigidBody>();
        node_->RemoveComponent<CollisionShape>();

        // Create RigidBody & CollisionShape components to bones
        CreateRagdollBone("Bip01_Pelvis", SHAPE_BOX, Vector3(0.3f, 0.2f, 0.25f), Vector3(0.0f, 0.0f, 0.0f),
            Quaternion(0.0f, 0.0f, 0.0f));
        CreateRagdollBone("Bip01_Spine1", SHAPE_BOX, Vector3(0.35f, 0.2f, 0.3f), Vector3(0.15f, 0.0f, 0.0f),
            Quaternion(0.0f, 0.0f, 0.0f));
        //CreateRagdollBone("Bip01_L_Thigh", SHAPE_CAPSULE, Vector3(0.175f, 0.45f, 0.175f), Vector3(0.25f, 0.0f, 0.0f),
        //    Quaternion(0.0f, 0.0f, 90.0f));
        CreateCapsuleFromBoneToBone("Bip01_L_Thigh", "Bip01_L_Calf", 0.175f);

        //CreateRagdollBone("Bip01_R_Thigh", SHAPE_CAPSULE, Vector3(0.175f, 0.45f, 0.175f), Vector3(0.25f, 0.0f, 0.0f),
        //    Quaternion(0.0f, 0.0f, 90.0f));
        CreateCapsuleFromBoneToBone("Bip01_R_Thigh", "Bip01_R_Calf", 0.175f);

        //CreateRagdollBone("Bip01_L_Calf", SHAPE_CAPSULE, Vector3(0.15f, 0.55f, 0.15f), Vector3(0.25f, 0.0f, 0.0f),
        //    Quaternion(0.0f, 0.0f, 90.0f));
        CreateCapsuleFromBoneToBone("Bip01_L_Calf", "Bip01_L_Foot", 0.15f);

        //CreateRagdollBone("Bip01_R_Calf", SHAPE_CAPSULE, Vector3(0.15f, 0.55f, 0.15f), Vector3(0.25f, 0.0f, 0.0f),
        //    Quaternion(0.0f, 0.0f, 90.0f));
        CreateCapsuleFromBoneToBone("Bip01_R_Calf", "Bip01_R_Foot", 0.15f);

        CreateRagdollBone("Bip01_Head", SHAPE_BOX, Vector3(0.2f, 0.2f, 0.2f), Vector3(0.1f, 0.0f, 0.0f),
            Quaternion(0.0f, 0.0f, 0.0f));
        //CreateRagdollBone("Bip01_L_UpperArm", SHAPE_CAPSULE, Vector3(0.15f, 0.35f, 0.15f), Vector3(0.1f, 0.0f, 0.0f),
        //    Quaternion(0.0f, 0.0f, 90.0f));
        CreateCapsuleFromBoneToBone("Bip01_L_UpperArm", "Bip01_L_Forearm", 0.15f);

        //CreateRagdollBone("Bip01_R_UpperArm", SHAPE_CAPSULE, Vector3(0.15f, 0.35f, 0.15f), Vector3(0.1f, 0.0f, 0.0f),
        //    Quaternion(0.0f, 0.0f, 90.0f));
        CreateCapsuleFromBoneToBone("Bip01_R_UpperArm", "Bip01_R_Forearm", 0.15f);

        //CreateRagdollBone("Bip01_L_Forearm", SHAPE_CAPSULE, Vector3(0.125f, 0.4f, 0.125f), Vector3(0.2f, 0.0f, 0.0f),
        //    Quaternion(0.0f, 0.0f, 90.0f));
        CreateCapsuleFromBoneToBone("Bip01_L_Forearm", "Bip01_L_Hand", 0.125f);

        //CreateRagdollBone("Bip01_R_Forearm", SHAPE_CAPSULE, Vector3(0.125f, 0.4f, 0.125f), Vector3(0.2f, 0.0f, 0.0f),
        //    Quaternion(0.0f, 0.0f, 90.0f));
        CreateCapsuleFromBoneToBone("Bip01_R_Forearm", "Bip01_R_Hand", 0.125f);

        // Create Constraints between bones
        CreateRagdollConstraint("Bip01_L_Thigh", "Bip01_Pelvis", CONSTRAINT_CONETWIST, Vector3::BACK, Vector3::FORWARD,
            Vector2(45.0f, 45.0f), Vector2::ZERO);
        CreateRagdollConstraint("Bip01_R_Thigh", "Bip01_Pelvis", CONSTRAINT_CONETWIST, Vector3::BACK, Vector3::FORWARD,
            Vector2(45.0f, 45.0f), Vector2::ZERO);
        CreateRagdollConstraint("Bip01_L_Calf", "Bip01_L_Thigh", CONSTRAINT_HINGE, Vector3::BACK, Vector3::BACK,
            Vector2(90.0f, 0.0f), Vector2::ZERO);
        CreateRagdollConstraint("Bip01_R_Calf", "Bip01_R_Thigh", CONSTRAINT_HINGE, Vector3::BACK, Vector3::BACK,
            Vector2(90.0f, 0.0f), Vector2::ZERO);
        CreateRagdollConstraint("Bip01_Spine1", "Bip01_Pelvis", CONSTRAINT_HINGE, Vector3::FORWARD, Vector3::FORWARD,
            Vector2(45.0f, 0.0f), Vector2(-10.0f, 0.0f));
        CreateRagdollConstraint("Bip01_Head", "Bip01_Spine1", CONSTRAINT_CONETWIST, Vector3::LEFT, Vector3::LEFT,
            Vector2(0.0f, 30.0f), Vector2::ZERO);
        CreateRagdollConstraint("Bip01_L_UpperArm", "Bip01_Spine1", CONSTRAINT_CONETWIST, Vector3::DOWN, Vector3::UP,
            Vector2(45.0f, 45.0f), Vector2::ZERO, false);
        CreateRagdollConstraint("Bip01_R_UpperArm", "Bip01_Spine1", CONSTRAINT_CONETWIST, Vector3::DOWN, Vector3::UP,
            Vector2(45.0f, 45.0f), Vector2::ZERO, false);
        CreateRagdollConstraint("Bip01_L_Forearm", "Bip01_L_UpperArm", CONSTRAINT_HINGE, Vector3::BACK, Vector3::BACK,
            Vector2(90.0f, 0.0f), Vector2::ZERO);
        CreateRagdollConstraint("Bip01_R_Forearm", "Bip01_R_UpperArm", CONSTRAINT_HINGE, Vector3::BACK, Vector3::BACK,
            Vector2(90.0f, 0.0f), Vector2::ZERO);

        // Disable keyframe animation from all bones so that they will not interfere with the ragdoll
        AnimatedModel* model = GetComponent<AnimatedModel>();
        Skeleton& skeleton = model->GetSkeleton();
        for (unsigned i = 0; i < skeleton.GetNumBones(); ++i)
            skeleton.GetBone(i)->animated_ = false;

        // Finally remove self from the scene node. Note that this must be the last operation performed in the function
        Remove();
    }
}

void CreateRagdoll::CreateRagdollBone(const String& boneName, ShapeType type, const Vector3& size, const Vector3& position,
    const Quaternion& rotation)
{
    // Find the correct child scene node recursively
    Node* boneNode = node_->GetChild(boneName, true);
    if (!boneNode)
    {
        URHO3D_LOGWARNING("Could not find bone " + boneName + " for creating ragdoll physics components");
        return;
    }

    RigidBody* body = boneNode->CreateComponent<RigidBody>();
    // Set mass to make movable
    body->SetMass(1.0f);
    // Set damping parameters to smooth out the motion
    body->SetLinearDamping(0.05f);
    body->SetAngularDamping(0.85f);
    // Set rest thresholds to ensure the ragdoll rigid bodies come to rest to not consume CPU endlessly
    body->SetLinearRestThreshold(1.5f);
    body->SetAngularRestThreshold(2.5f);

    CollisionShape* shape = boneNode->CreateComponent<CollisionShape>();
    // We use either a box or a capsule shape for all of the bones
    if (type == SHAPE_BOX)
        shape->SetBox(size, position, rotation);
    else
        shape->SetCapsule(size.x_, size.y_, position, rotation);
}

void CreateRagdoll::CreateRagdollConstraint(const String& boneName, const String& parentName, ConstraintType type,
    const Vector3& axis, const Vector3& parentAxis, const Vector2& highLimit, const Vector2& lowLimit,
    bool disableCollision)
{
    Node* boneNode = node_->GetChild(boneName, true);
    Node* parentNode = node_->GetChild(parentName, true);
    if (!boneNode)
    {
        URHO3D_LOGWARNING("Could not find bone " + boneName + " for creating ragdoll constraint");
        return;
    }
    if (!parentNode)
    {
        URHO3D_LOGWARNING("Could not find bone " + parentName + " for creating ragdoll constraint");
        return;
    }

    Constraint* constraint = boneNode->CreateComponent<Constraint>();
    constraint->SetConstraintType(type);
    // Most of the constraints in the ragdoll will work better when the connected bodies don't collide against each other
    constraint->SetDisableCollision(disableCollision);
    // The connected body must be specified before setting the world position
    constraint->SetOtherBody(parentNode->GetComponent<RigidBody>());
    // Position the constraint at the child bone we are connecting
    constraint->SetWorldPosition(boneNode->GetWorldPosition());
    // Configure axes and limits
    constraint->SetAxis(axis);
    constraint->SetOtherAxis(parentAxis);
    constraint->SetHighLimit(highLimit);
    constraint->SetLowLimit(lowLimit);
}

int CreateRagdoll::CreateCapsuleFromBoneToBone(const String& boneName, const String& childBoneName, float diameter)
{
    Node* boneNode = node_->GetChild(boneName, true);

    if (!boneNode)
    {
        URHO3D_LOGWARNING("Could not find bone " + boneName + " for creating ragdoll physics components");
        return -1;
    }

    Node* childBoneNode = boneNode->GetChild(childBoneName);

    if (!childBoneNode)
    {
        URHO3D_LOGWARNING("Bone " + childBoneName + " is not an immediate child of " + boneName);
        return -1;
    }

    // gather info based on child's local space
    Vector3 posLS = childBoneNode->GetPosition();
    Vector3 centerPos = posLS * 0.5f;
    Vector3 direction = posLS.Normalized();
    float length = posLS.Length();
    Vector3 size(diameter, length, 0);
    Quaternion rotation;
    rotation.FromRotationTo(Vector3::UP, direction);

    return CreateCollisionShape(boneNode, centerPos, rotation, size);
}

int CreateRagdoll::CreateCollisionShape(Node *boneNode, const Vector3& position, const Quaternion& rotation, const Vector3& size)
{
    RigidBody* body = boneNode->CreateComponent<RigidBody>();
    // Set mass to make movable
    body->SetMass(1.0f);
    // Set damping parameters to smooth out the motion
    body->SetLinearDamping(0.05f);
    body->SetAngularDamping(0.85f);
    // Set rest thresholds to ensure the ragdoll rigid bodies come to rest to not consume CPU endlessly
    body->SetLinearRestThreshold(1.5f);
    body->SetAngularRestThreshold(2.5f);

    CollisionShape* shape = boneNode->CreateComponent<CollisionShape>();
    shape->SetCapsule(size.x_, size.y_, position, rotation);

    return 0;
}

[/code][/spoiler]

-------------------------

Lumak | 2017-01-02 01:15:45 UTC | #10

And lastly and most importantly, constraint should prevent rigidbody to NOT have collision with its immediate parent, as shown in the code:
[code]
    // Most of the constraints in the ragdoll will work better when the connected bodies don't collide against each other
    constraint->SetDisableCollision(disableCollision);
    // The connected body must be specified before setting the world position
    constraint->SetOtherBody(parentNode->GetComponent<RigidBody>());

[/code]

disableCollision = true by default.

-------------------------

slapin | 2017-01-02 01:15:45 UTC | #11

Yep, I disable collision in constraints, otherwise it is much worse.

-------------------------

slapin | 2017-01-02 01:15:45 UTC | #12

The current progress - I implemented almost all bones I need, but still get not resting ragdolls and
ragdolls penetrating terrain

(this one with big capsules still enabled)
[youtu.be/9iWSvoAEAaI](https://youtu.be/9iWSvoAEAaI)

(this one is with big capsules disabled)
[youtu.be/KKhUYc1CVow](https://youtu.be/KKhUYc1CVow)

-------------------------

slapin | 2017-01-02 01:15:45 UTC | #13

Ok, thanks everyone, now I made it work:

[youtu.be/5Bm1lf4-K8k](https://youtu.be/5Bm1lf4-K8k)

The main key was to set physicsWorld.fps = 100
after that everything magically started working and
average performance increased.

-------------------------

Lumak | 2017-01-02 02:11:47 UTC | #14

That's looking much better, slapin. Looks like your large capsule is changed to a trigger or was it something else?
Not sure why the legs penetrate the terrain on some of your ragdolls, though.

If constraints are created correctly, you should get something like this:
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/8e0c95888c2be2c6138497428f32458a57a6788e.jpg[/img]

edit: added a pic

-------------------------

slapin | 2017-01-02 01:15:46 UTC | #15

Well, now it doesn't penetrate terrain anymore. As for capsule - it doesn't affect anything, I just disable it now together with
RigidBody. My setup is basically the same as with ragdoll demo except that I use global rotations and some tweaking.

Now I want to experiment with active ragdoll path, I just need to understand how this is done.

-------------------------

