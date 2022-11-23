Naros | 2020-11-14 17:08:41 UTC | #1

I'm importing some custom models into Urho3D using a custom `Model` implementation (which extends `Model` and overrides serializing the data from a custom format)  and passing this to the standard `AnimatedModel` class.  If I don't applying a `Skeleton` to the custom `Model`, the model is then rendered as I would expect.  But as soon as I apply the model's skeleton, it is no longer rendered or at least visible.

I'm setting the skeleton which consists of 26 bones in total as follows:
```
Urho3D::Skeleton skeleton;
auto &bones = skeleton.GetModifiableBones();
for (unsigned i = 0u; i < modelFile->GetBones().Size(); ++i)
{
  const auto &modelBone = modelFile->GetBoneByIndex(i);

  Urho3D::Bone bone;
  bone.name_ = Urho3D::ToString("%u", modelBone.boneId);
  bone.nameHash_ = bone.name_;
  bone.initialPosition_ = modelBone.pivot.ToUrho3D();
  // we do not define the following in our bone definitions
  // additionally, bounding box, offset matrix, and radius aren't in the data
  bone.initialRotation_ = Urho3D::Quaternion::IDENTITY;
  bone.initialScale_ = Urho3D::Vector3::ONE;
  bone.parentIndex_ = (modelBone.parentBone == -1 ? i : modelBone.parentBone);

  bones.Push(bone);
  if (bone.parentIndex_ == i)
    skeleton.SetRootBoneIndex(i);
}

// Set the skeleton on the Model
SetSkeleton( skeleton );
```
I wouldn't expect that an `AnimationTrack` needs to be bound to the model because if I disable applying that to the model in the SkeletalAnimation example, the model renders with the skeleton & the base model pose just fine.

Is there potentially something else I need to be setting properly for this to work?

-------------------------

SirNate0 | 2020-11-14 17:38:01 UTC | #2

Maybe the bounding box and/or the nodes for the bones? But those may also be set by the skeleton?

-------------------------

Naros | 2020-11-14 18:11:00 UTC | #3

From what I can tell from the code, when no skeleton is defined, the `boneBoundingBox_` is defined as as the default infinite bounding box.  a new bone uses the same infinite bounding box by default, therefore when no collision is being applied, this should all be fine.  When no collision mask is being applied, I don't see where `radius_` is necessary either.

Just stepped through the bone creation step and those are being created as I would expect them, with the appropriate parent/child relationships being defined between the bones and the nodes within the scene.

The only questionable part here to me was the Bone's `offsetMatrix_`.  This gets used when the model calls `UpdateSkinning` but the default is an identity matrix, so technically this leads to populating the skin matrices by either the constructed bone node's transform or the model's depending if a node is yet attached to the bone at the time the method is called, which again should all be fine.

Suffice to say I'm still stumped.

-------------------------

