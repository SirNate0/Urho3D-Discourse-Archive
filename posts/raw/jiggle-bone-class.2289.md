artgolf1000 | 2017-01-02 01:14:31 UTC | #1

Hi,

I've made the jiggle bone class work in Urho3D 1.6, it can be used to control bouncy breast dynamics, hair, etc.

[code]context->RegisterFactory<JiggleBone>();
modelObject->GetSkeleton().GetBone("Hair")->animated_=false;
modelNode->GetChild("Hair", true)->CreateComponent<JiggleBone>();
[/code]

[code]#pragma once

#include <Urho3D/Urho3DAll.h>

/*
 Port of http://wiki.unity3d.com/index.php?title=JiggleBone
 to Urho3D
 */

namespace Urho3D
{
    extern const char* PHYSICS_CATEGORY;
    
    /// Custom logic component for rotating a scene node.
    class JiggleBone : public LogicComponent
    {
        URHO3D_OBJECT(JiggleBone, LogicComponent);
        
    public:
        /// Construct.
        JiggleBone(Context* context) :
        LogicComponent(context),
        boneAxis_(Vector3(0, 1, 0)),
        targetDistance_(2.0f),
        stiffness_(0.05f),
        mass_(0.9f),
        damping_(0.75f),
        gravity_(1.25f),
        squashAndStretch_(false),
        sideStretch_(0.15f),
        frontStretch_(0.2f),
        drawDebug_(false)
        {
            // Only the scene post update event is needed: unsubscribe from the rest for optimization
            SetUpdateEventMask(USE_POSTUPDATE);
        }
        
        virtual ~JiggleBone() {}

        static void RegisterObject(Context* context)
        {
            context->RegisterFactory<JiggleBone>(PHYSICS_CATEGORY);
            
            URHO3D_COPY_BASE_ATTRIBUTES(LogicComponent);
            URHO3D_ACCESSOR_ATTRIBUTE("Is Enabled", IsEnabled, SetEnabled, bool, true, AM_DEFAULT);
            URHO3D_ATTRIBUTE("Bone Axis", Vector3, boneAxis_, Vector3(0, 0, 1), AM_DEFAULT);
            
            URHO3D_ATTRIBUTE("Stiffness", float, stiffness_, 0.1f, AM_DEFAULT);
            URHO3D_ATTRIBUTE("Mass", float, mass_, 0.9f, AM_DEFAULT);
            URHO3D_ATTRIBUTE("Damping", float, damping_, 0.75f, AM_DEFAULT);
            URHO3D_ATTRIBUTE("Gravity", float, gravity_, 0.75f, AM_DEFAULT);
            
            URHO3D_ATTRIBUTE("Allow Stretch", bool, squashAndStretch_, true, AM_DEFAULT);
            URHO3D_ATTRIBUTE("Side Stretch", float, sideStretch_, 0.15f, AM_DEFAULT);
            URHO3D_ATTRIBUTE("Front Stretch", float, frontStretch_, 0.15f, AM_DEFAULT);
        }
        
        /// Called when the component is added to a scene node. Other components may not yet exist.
        virtual void DelayedStart()
        {
            Vector3 forwardVector = GetNode()->GetWorldUp() * targetDistance_;
            targetPos_ = GetNode()->GetWorldPosition() + forwardVector;
            dynamicPos_ = targetPos_;
        }
        
        virtual void PostUpdate(float timeStep)
        {
            if (IsEnabledEffective())
            {
                // Reset the bone rotation so we can recalculate the upVector and forwardVector
                GetNode()->SetRotation(Quaternion());

                // Update forwardVector and upVector
                Vector3 forwardVector = GetNode()->GetWorldUp() * targetDistance_;
                
                // Calculate target position
                targetPos_ = GetNode()->GetWorldPosition() + forwardVector;
                
                // Calculate force, acceleration, and velocity per X, Y and Z
                force_.x_ = (targetPos_.x_ - dynamicPos_.x_) * stiffness_;
                acc_.x_ = force_.x_ / mass_;
                vel_.x_ += acc_.x_ * (1 - damping_);
                
                force_.y_ = (targetPos_.y_ - dynamicPos_.y_) * stiffness_;
                force_.y_ -= gravity_ * 0.1f; // Add some gravity
                acc_.y_ = force_.y_ / mass_;
                vel_.y_ += acc_.y_ * (1 - damping_);
                
                force_.z_ = (targetPos_.z_ - dynamicPos_.z_) * stiffness_;
                acc_.z_ = force_.z_ / mass_;
                vel_.z_ += acc_.z_ * (1 - damping_);
                
                // Update dynamic postion
                dynamicPos_ += vel_ + force_;
                
                // Set bone rotation to look at dynamicPos
                GetNode()->LookAt(dynamicPos_, GetNode()->GetWorldUp());
                GetNode()->Rotate(Quaternion(90.0f, 0.0f, 0.0f));
                
                // ==================================================
                // Squash and Stretch section
                // ==================================================
                if (squashAndStretch_){
                    // Create a vector from target position to dynamic position
                    // We will measure the magnitude of the vector to determine
                    // how much squash and stretch we will apply
                    Vector3 dynamicVec = dynamicPos_ - targetPos_;
                    
                    // Get the magnitude of the vector
                    float stretchMag = dynamicVec.Length();
                    
                    // Here we determine the amount of squash and stretch based on stretchMag
                    // and the direction the Bone Axis is pointed in. Ideally there should be
                    // a vector with two values at 0 and one at 1. Like Vector3(0,0,1)
                    // for the 0 values, we assume those are the sides, and 1 is the direction
                    // the bone is facing
                    float xStretch;
                    if (boneAxis_.x_ == 0)
                        xStretch = 1 + (-stretchMag * sideStretch_);
                    else
                        xStretch = 1 + (stretchMag * frontStretch_);
                    
                    float yStretch;
                    if (boneAxis_.y_ == 0)
                        yStretch = 1 + (-stretchMag * sideStretch_);
                    else
                        yStretch = 1 + (stretchMag * frontStretch_);
                    
                    float zStretch;
                    if (boneAxis_.z_ == 0)
                        zStretch = 1 + (-stretchMag * sideStretch_);
                    else
                        zStretch = 1 + (stretchMag * frontStretch_);
                    
                    // Set the bone scale
                    GetNode()->SetScale(Vector3(xStretch, yStretch, zStretch));
                }
                
                if (drawDebug_) {
                    DebugRenderer* debug = GetScene()->GetComponent<DebugRenderer>();
                    DrawDebugGeometry(debug, false);
                }
            }
        }
        
        virtual void DrawDebugGeometry(DebugRenderer* debug, bool depthTest)
        {
            if (debug && IsEnabledEffective())
            {
                // draw forward line
                debug->AddLine(GetNode()->GetWorldPosition(),
                               GetNode()->GetWorldPosition() + GetNode()->GetWorldDirection() * targetDistance_,
                               Color(0, 0, 1), false);
                // draw the up vector
                debug->AddLine(GetNode()->GetWorldPosition(),
                               GetNode()->GetWorldPosition() + GetNode()->GetWorldUp() * (targetDistance_ * 0.5f),
                               Color(0, 1, 0), false);
                // draw the target position
                debug->AddLine(targetPos_,
                               Vector3::UP * (targetDistance_ * 0.2f),
                               Color(1, 1, 0), false);
                // draw the dynamic position
                debug->AddLine(dynamicPos_,
                               Vector3::UP * (targetDistance_ * 0.2f),
                               Color(1, 0, 0), false);
            }
        }
        
    private:
        Vector3 boneAxis_;
        float targetDistance_;
        float stiffness_;
        float mass_;
        float damping_;
        float gravity_;
        bool squashAndStretch_;
        float sideStretch_;
        float frontStretch_;
        Vector3 targetPos_;
        Vector3 dynamicPos_;
        Vector3 force_;
        Vector3 acc_;
        Vector3 vel_;
        bool drawDebug_;
    };
}
[/code]

-------------------------

1vanK | 2017-01-02 01:14:31 UTC | #2

Thank you, very useful

-------------------------

