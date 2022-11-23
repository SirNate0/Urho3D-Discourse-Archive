rku | 2018-08-17 06:29:51 UTC | #1

I implemented root motion support in animations. Im not entirely sure of it's correctness so be aware. Also i am not entirely happy with the API. Probably there is a better way to do it. This is why i am not submitting PR.

![root-motion|320x349](upload://pckoVrF4Pjegm8TBWzi72DJbPDs.gif) 

Enable root motion:
```cpp
animCtrl->PlayExclusive("walk.ani", 0, true, 0.3f);  // play animation
animCtrl->SetRootMotionMode("walk.ani", ANIM_ROOT_MOTION_XZ);  // enable root motion
```
Apply root motion:
```cpp
SubscribeToEvent(E_POSTRENDERUPDATE, [](StringHash, VariantMap&){
        const auto* state = animCtrl->GetAnimationState("walk.ani");
        const Matrix3x4& motion = state->GetRootMotion();
        node->Translate(motion.Translation() * GetNode()->GetScale());
        node->Rotate(motion.Rotation());  // optional
});
```
Matrix retuned by `GetRootMotion()` contains motion delta. `ANIM_ROOT_MOTION_XZ` means that returned matrix will contain translation delta for X and Z axis + rotation delta for Y axis.


```diff
diff --git a/Source/Urho3D/Graphics/Animation.h b/Source/Urho3D/Graphics/Animation.h
index e7b98be20..07e9b5d11 100644
--- a/Source/Urho3D/Graphics/Animation.h
+++ b/Source/Urho3D/Graphics/Animation.h
@@ -58,6 +58,12 @@ struct AnimationKeyFrame
     Quaternion rotation_;
     /// Bone scale.
     Vector3 scale_;
+
+    /// Returns matrix which encodes position, rotation and scale of this keyframe.
+    Matrix3x4 ToMatrix() const
+    {
+        return Matrix3x4(position_, rotation_, scale_);
+    }
 };
 
 /// Skeletal animation track, stores keyframes of a single bone.
diff --git a/Source/Urho3D/Graphics/AnimationController.cpp b/Source/Urho3D/Graphics/AnimationController.cpp
index da073a236..49aee822d 100644
--- a/Source/Urho3D/Graphics/AnimationController.cpp
+++ b/Source/Urho3D/Graphics/AnimationController.cpp
@@ -915,4 +915,27 @@ void AnimationController::HandleScenePostUpdate(StringHash eventType, VariantMap
     Update(eventData[P_TIMESTEP].GetFloat());
 }
 
+bool AnimationController::SetRootMotionMode(const String& name, AnimationRootMotionFlags flags)
+{
+    unsigned index;
+    AnimationState* state;
+    FindAnimation(name, index, state);
+    if (index == M_MAX_UNSIGNED)
+        return false;
+
+    state->SetRootMotionMode(flags);
+    return true;
+}
+
+AnimationRootMotionFlags AnimationController::GetRootMotion(const String& name) const
+{
+    unsigned index;
+    AnimationState* state;
+    FindAnimation(name, index, state);
+    if (index == M_MAX_UNSIGNED)
+        return ANIM_ROOT_MOTION_NONE;
+
+    return state->GetRootMotionMode();
+}
+
 }
diff --git a/Source/Urho3D/Graphics/AnimationController.h b/Source/Urho3D/Graphics/AnimationController.h
index 2ac391c82..833fd489b 100644
--- a/Source/Urho3D/Graphics/AnimationController.h
+++ b/Source/Urho3D/Graphics/AnimationController.h
@@ -127,6 +127,8 @@ public:
     bool SetSpeed(const String& name, float speed);
     /// Set animation autofade at end (non-looped animations only.) Zero time disables. Return true on success.
     bool SetAutoFade(const String& name, float fadeOutTime);
+    /// Enable or disable root motion for specified animation.
+    bool SetRootMotionMode(const String& name, AnimationRootMotionFlags flags);
     /// Set whether an animation auto-removes on completion.
     bool SetRemoveOnCompletion(const String& name, bool removeOnCompletion);
     /// Set animation blending mode. Return true on success.
@@ -166,6 +168,8 @@ public:
     float GetFadeTime(const String& name) const;
     /// Return animation autofade time.
     float GetAutoFade(const String& name) const;
+    /// Return default root motion status of specified animation.
+    AnimationRootMotionFlags GetRootMotion(const String& name) const;
     /// Return whether animation auto-removes on completion, or false if no such animation.
     bool GetRemoveOnCompletion(const String& name) const;
     /// Find an animation state by animation name.
@@ -208,6 +212,8 @@ private:
     Vector<SharedPtr<AnimationState> > nodeAnimationStates_;
     /// Attribute buffer for network replication.
     mutable VectorBuffer attrBuffer_;
+    /// Default root motion state.
+    AnimationRootMotionFlags defaultRootMotionFlags_{ANIM_ROOT_MOTION_NONE};
 };
 
 }
diff --git a/Source/Urho3D/Graphics/AnimationState.cpp b/Source/Urho3D/Graphics/AnimationState.cpp
index a6a22d16b..b3cc9133c 100644
--- a/Source/Urho3D/Graphics/AnimationState.cpp
+++ b/Source/Urho3D/Graphics/AnimationState.cpp
@@ -93,7 +93,12 @@ AnimationState::AnimationState(Node* node, Animation* animation) :
                 }
 
                 if (stateTrack.node_)
+                {
+                    if (stateTrack.bone_ == model_->GetSkeleton().GetRootBone())
+                        previousRootTransform_ = stateTrack.track_->keyFrames_.Front().ToMatrix();
+
                     stateTracks_.Push(stateTrack);
+                }
             }
         }
     }
@@ -148,6 +153,9 @@ void AnimationState::SetStartBone(Bone* startBone)
 
         if (trackBone && trackBone->node_)
         {
+            if (trackBone == model_->GetSkeleton().GetRootBone())
+                previousRootTransform_ = stateTrack.track_->keyFrames_.Front().ToMatrix();
+
             stateTrack.bone_ = trackBone;
             stateTrack.node_ = trackBone->node_;
             stateTracks_.Push(stateTrack);
@@ -483,6 +491,7 @@ void AnimationState::ApplyTrack(AnimationStateTrack& stateTrack, float weight, b
         return;
 
     unsigned& frame = stateTrack.keyFrame_;
+    unsigned previousFrame = frame;
     track->GetKeyFrameIndex(time_, frame);
 
     // Check if next frame to interpolate to is valid, or if wrapping is needed (looping animation only)
@@ -564,6 +573,58 @@ void AnimationState::ApplyTrack(AnimationStateTrack& stateTrack, float weight, b
         }
     }
 
+    // Root motion
+    if (rootMotionFlags_ & ANIM_ROOT_MOTION_XYZ && channelMask & CHANNEL_POSITION &&
+        stateTrack.bone_ == model_->GetSkeleton().GetRootBone())
+    {
+        Matrix3x4 transform;
+        if (channelMask & CHANNEL_POSITION)
+            transform.SetRotation(newRotation.RotationMatrix());
+        if (channelMask & CHANNEL_ROTATION)
+            transform.SetTranslation(newPosition);
+
+        bool looped = frame < previousFrame;
+        if (looped)
+        {
+            const Matrix3x4 animationStart = stateTrack.track_->keyFrames_.Front().ToMatrix();
+            const Matrix3x4 animationEnd = stateTrack.track_->keyFrames_.Back().ToMatrix();
+            rootMotion_ = (animationEnd * previousRootTransform_.Inverse()) * (transform * animationStart.Inverse());
+        }
+        else
+            rootMotion_ = previousRootTransform_.Inverse() * transform;
+
+        Vector3 positionDelta = rootMotion_.Translation();
+        Vector3 rotationDelta, newRotationEuler;
+        rotationDelta = rootMotion_.Rotation().EulerAngles();
+        newRotationEuler = newRotation.EulerAngles();
+
+        const auto& bonePosition = node->GetPosition();
+        const auto& boneRotation = node->GetRotation();
+
+        for (auto i = 0; i < 3; i++)
+        {
+            auto axis = static_cast<AnimationRootMotionMode>(1 << i);
+            if (rootMotionFlags_ & axis)
+            {
+                // Axis is tracked. Position of root bone is locked, rotation is not provided in root motion delta and applied to the bone.
+                (&newPosition.x_)[i] = bonePosition.Data()[i];
+                (&rotationDelta.x_)[i] = 0;
+            }
+            else
+            {
+                // Axis is not tracked. Position is not provided in root motion delta, rotation is provided in root motion delta and not applied to the bone.
+                (&positionDelta.x_)[i] = 0;
+                (&newRotationEuler.x_)[i] = boneRotation.Data()[i];
+            }
+        }
+
+        newRotation = Quaternion(newRotationEuler);
+        rootMotion_.SetRotation(Quaternion(rotationDelta).RotationMatrix());
+        rootMotion_.SetTranslation(positionDelta);
+
+        previousRootTransform_ = transform;
+    }
+
     if (silent)
     {
         if (channelMask & CHANNEL_POSITION)
diff --git a/Source/Urho3D/Graphics/AnimationState.h b/Source/Urho3D/Graphics/AnimationState.h
index 337708612..b23b70dea 100644
--- a/Source/Urho3D/Graphics/AnimationState.h
+++ b/Source/Urho3D/Graphics/AnimationState.h
@@ -22,8 +22,10 @@
 
 #pragma once
 
+#include "../Container/FlagSet.h"
 #include "../Container/HashMap.h"
 #include "../Container/Ptr.h"
+#include "../Math/Matrix3x4.h"
 #include "../Math/StringHash.h"
 
 namespace Urho3D
@@ -47,6 +49,24 @@ enum AnimationBlendMode
     ABM_ADDITIVE
 };
 
+/// %Animation root motion mode.
+enum AnimationRootMotionMode : unsigned char
+{
+    /// Motion of the root bone is applied directly to that bone.
+    ANIM_ROOT_MOTION_NONE,
+    /// X motion of the root bone is applied to the parent of the bone.
+    ANIM_ROOT_MOTION_X = 1,
+    /// Y motion of the root bone is applied to the parent of the bone.
+    ANIM_ROOT_MOTION_Y = 2,
+    /// Z motion of the root bone is applied to the parent of the bone.
+    ANIM_ROOT_MOTION_Z = 4,
+    /// XZ motion of the root bone is applied to the parent of the bone.
+    ANIM_ROOT_MOTION_XZ = ANIM_ROOT_MOTION_X | ANIM_ROOT_MOTION_Z,
+    /// XYZ motion of the root bone is applied to the parent of the bone.
+    ANIM_ROOT_MOTION_XYZ = ANIM_ROOT_MOTION_XZ | ANIM_ROOT_MOTION_Y,
+};
+URHO3D_FLAGSET(AnimationRootMotionMode, AnimationRootMotionFlags);
+
 /// %Animation instance per-track data.
 struct AnimationStateTrack
 {
@@ -147,6 +167,13 @@ public:
     /// Apply the animation at the current time position.
     void Apply();
 
+    /// Return root motion status.
+    AnimationRootMotionFlags GetRootMotionMode() const { return rootMotionFlags_; }
+    /// Enable or disable root motion.
+    void SetRootMotionMode(AnimationRootMotionFlags flags) { rootMotionFlags_ = flags; }
+    /// Return last frame root motion delta.
+    const Matrix3x4& GetRootMotion() const { return rootMotion_; };
+
 private:
     /// Apply animation to a skeleton. Transform changes are applied silently, so the model needs to dirty its root model afterward.
     void ApplyToModel();
@@ -175,6 +202,12 @@ private:
     unsigned char layer_;
     /// Blending mode.
     AnimationBlendMode blendingMode_;
+    /// Root motion state.
+    AnimationRootMotionFlags rootMotionFlags_{ANIM_ROOT_MOTION_NONE};
+    /// Previous transform of root bone.
+    Matrix3x4 previousRootTransform_;
+    /// Motion delta of root bone.
+    Matrix3x4 rootMotion_;
 };
 
 }
```

-------------------------

TrevorCash | 2018-08-16 14:20:00 UTC | #2

I like how it simply returns the motion matrix and doesn't take over that control and leaves it to the implementer. Just A thought - It may be useful to enable other axis combinations - For example for a spider model animation crawling up a wall which would be motion in the YZ or XY plane. Although you could transform it on the outside as well I suppose

-------------------------

rku | 2018-08-16 14:20:20 UTC | #3

You can do that by freely combining flags in `AnimationRootMotionMode`

-------------------------

TrevorCash | 2018-08-16 14:21:17 UTC | #4

Oh I see that now - nice

-------------------------

S.L.C | 2018-08-16 23:36:50 UTC | #5

The video does not work. If that was supposed to be a video.

-------------------------

rku | 2018-08-17 06:46:28 UTC | #6

Yeah apparently streamable is not good for long-ish term hosting of videos. Replaced it with a gif.

-------------------------

smellymumbler | 2018-08-17 19:00:07 UTC | #7

I don't quite understand the use cases for this. Does this mean i can easily blend an upper body animation (waving a sword, for example) with a walking animation, in different directions?

-------------------------

slapin | 2018-08-18 09:26:30 UTC | #8

I'd prefer to see full delta after all animation blends.
Either way please send PR

-------------------------

rku | 2018-08-19 07:35:11 UTC | #9

@smellymumbler this is useful for animations that do not have a linear movement speed. For instance animation for walking with injured leg - talking step is fast but then character goes to a stop before taking next step. Root motion allows to have perfectly synchronize scene `Node` motion with motion with such  animation having non-linear motion. Gif in the first post has two arrows. Lower red arrow is attached to hips of the character and displays location and rotation of hips. Arrow above character's head is attached to a `Node` that has `AnimatedModel` and is playing animation. Notice how hips and parent node itself are in perfect sync. Without root motion upper arrow would always stay in place and not rotate while lower arrow + entire model animate forward and snap to the starting position.

@slapin you are right, this kind of sucks and delta between all blends would definitely be more proper. I am not entirely sure how to accomplish it.

-------------------------

