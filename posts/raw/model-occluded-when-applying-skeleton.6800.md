Naros | 2021-04-12 06:07:26 UTC | #1

I have a custom model format that I'm trying to load.  The skeleton definition specifies each bone and whether each bone has a parent and the exact world-space position where the bone is to be rendered.  I attempted to populate the Urho3D `Skeleton` as follows:

```
Urho3D::Vector<Urho3D::Bone>& bones = skeleton.GetModifiableBones();
for ( const ModelBone &mBone : modelBones )
{
  const auto parentIndex = mBone.parentBoneId < 0 ? i : mBone.parentBoneId;

  Urho3D::Bone &bone;
  bone.name_ = Urho3D::ToString( "Bone%u", mBone.boneId );
  bone.nameHash_ = bone.name_;
  bone.parentIndex_ = parentIndex;
  bone.initialPosition_ = Urho3D::Vector3( mBone.pivot.x, mBone.pivot.y, mBone.pivot.z );

  if ( bone.parentIndex_ != i )
  {
    unsigned index = bone.parentIndex_;
    while ( true )
    {
      const Urho3D::Bone &parent = bones[ index ];
      bone.initialPosition_ -= parent.initialPosition_;
      if ( parent.parentIndex_ == index )
        break;

      index = parent.parentIndex;
    }
  }

  bone.offsetMatrix_ = Urho3D::Matrix3x4( -bone.initialPosition_, bone.initialRotation_, bone.initialScale_ );  

  bones.Push( bone );
}
skeleton.SetRootBoneIndex( model->GetRootBoneIndex() );
```

The problem I face is that the model is being occluded, as if the bounding box is outside the frustum.  If I move the camera to a specific angle in the scene, then the model renders.  I believe this has to do with the bone position and offset code above, but I'm not exactly sure what I could be doing wrong.  When I enable the debug render, the skeleton is being drawn where it should be at the correct positions, but I never see the bounding box for the model being drawn.

If I opt not to set any bones in the skeleton and supply an empty skeleton to the model, the model will be rendered without any occlusion problems with the frustum.

Since the bone positions in the data are in world-space, is there some other adjustment or change I need to make to the code above that I didn't account for this?

-------------------------

Eugene | 2021-04-12 08:10:35 UTC | #2

You have to set radius_ or boundingBox_ as well to get propper skeleton occlusion together with collisionMask_

-------------------------

Naros | 2021-04-12 13:14:12 UTC | #3

Even if the collision mask is set to `NONE` by default?  

I tested setting the collision mask to `SPHERE` and assigning a dummy radius of `0.01f` and it does avoid the occlusion problem; however the boundingbox for the model is still not being drawn correctly when enable the debug renderer which still leads me to think there is something amuck with the code above.

This is with the skeleton populated with bones:
![image|301x500](upload://lPMkxQeHy4S4IjjiwMqizFEsI6A.png) 

This is with an empty skeleton that has no bones:
![image|339x500](upload://6t5ORlgBEGnFiasmhpbQIaebjQr.png)

-------------------------

Eugene | 2021-04-12 13:39:54 UTC | #4

[quote="Naros, post:3, topic:6800"]
Even if the collision mask is set to `NONE` by default?
[/quote]
Well, if collision mask is NONE the bone doesn't contribute into bounding box at all.

[quote="Naros, post:3, topic:6800"]
however the boundingbox for the model is still not being drawn correctly
[/quote]
Because your bones are obviously thicker than 0.01 units. You probably need bounding boxes, not spheres.

-------------------------

Naros | 2021-04-12 14:21:42 UTC | #5

> Well, if collision mask is NONE the bone doesn’t contribute into bounding box at all.

Right and my understanding was that if the collision mask is NONE that neither a radius or bounding box need to be specified at least based on the code in `Model.cpp`.  The oddity is when using NONE, this strange frustum occlusion problem arises but when using any other collision mask it doesn't.  I'd like to understand why I need to use anything but NONE or is this a bug?

> Because your bones are obviously thicker than 0.01 units. You probably need bounding boxes, not spheres.

So if I understand, when using bone collision masks, the bounding box of the model is then based entirely on the bone structure rather than the bounding boxes of the associated geometry?  

I'm sorry for the questions but I'm having a small disconnect here as I'm in the process of porting code that used Ogre3D v1 Skeletons to Urho3D.  In this legacy code, it was straight forward where I defined a Skeleton instance, created the Bone instances, set the bone's starting position in world space, and then parented the bone if applicable.

-------------------------

Eugene | 2021-04-12 14:47:12 UTC | #6

[quote="Naros, post:5, topic:6800"]
So if I understand, when using bone collision masks, the bounding box of the model is then based entirely on the bone structure rather than the bounding boxes of the associated geometry?
[/quote]
When using *skeletal animation*, the bounding box of the model is based on bones.
If you want to get sane culling, you have to tell the engine the dimensions of your model, i.e. dimenstions of all bones. Or at least all bones that matter.

If you have different expectation, please clarify the exact requirements.
Let's say you don't want to specify bone bounding boxes. What do you expect the bounding box of animated model to be?

-------------------------

Naros | 2021-04-12 17:34:11 UTC | #7

So we have  a mapping that defines vertex <-> bone relationship.  We used this when defining part of the legacy skeleton data.  I used this mapping in order to resolve the bounding box associated with each bone and that resolved the occlusion issue; however, I still believe my bone position/matrix logic is off.

![image|393x500](upload://dWfGKnL4Kx4aiFy6T50R2oZjmq.png) 

In this image, each of the bone's bounding boxes are represented by the yellow quads.  The entire model's bounding box is represented by the green quad, the skeleton is represented by the red line and the two geometry centers are represented by the magenta spheres.

The yellow bone bounding boxes are calculated as follows:
```
for ( unsigned boneIndex = 0; boneIndex < skeleton.GetNumBones(); ++boneIndex )
{
  Urho3D::Bone *bone = skeleton.GetBone( boneIndex );
  for ( unsigned i = 0; i < vertices.Size(); ++i )
  {
    // Each vertex is assigned up to 4 bone indices for weights
    // If this vertex is associated with the current boneIndex, add vertex to bone bounding box 
    const auto &vertex = vertices[ i ];
    for ( unsigned j = 0; j < 4; ++j )
    {
      if ( vertex.boneIndices[ j ] == boneIndex )
      {
        // vertex position is in world-space coordinates
        bone->boundingBox_.Merge( vertex.position );
      }
    }        
  }
}
```
In order to calculate the bone positions, I'm now using the following:
```
Vector<Bone>& bones = skeleton.GetModifiableBones();
for ( const ModelBone &mBone : modelBones )
{
  // if model bone has parent bone id of -1, it has no parent
  const auto parentIndex = mBone.parentBoneId < 0 ? i : mBone.parentBoneId;

  Urho3D::Bone &bone;
  bone.name_ = ToString( "Bone%u", mBone.boneId );
  bone.nameHash_ = bone.name_;
  bone.parentIndex_ = parentIndex;
  bone.initialPosition_ = Vector3( mBone.pivot.x, mBone.pivot.y, mBone.pivot.z );

  // If the bone has a parent, adjust the position specified above since the position
  // values are provided in the metadata as explicit points without concern for any
  // parent/child relationship
  if ( bone.parentIndex_ != i )
  {
    unsigned index = bone.parentIndex_;
    while ( true )
    {
      const Bone &parent = bones[ index ];
      bone.initialPosition_ -= parent.initialPosition_;
      if ( parent.parentIndex_ == index )
        break;

      index = parent.parentIndex;
    }
  }

  bone.offsetMatrix_ = Matrix3x4( -bone.initialPosition_, bone.initialRotation_, bone.initialScale_ );  

  // note the bone's bounding box will be resolved in a later step by inspecting the vertex/bone
  // association map and bounding the bounding box based on the vertex data.
  bone.collisitionMask_ = BONECOLLISION_BOX;

  bones.Push( bone );

  if ( bone.parentIndex_ == i )
    skeleton.SetRootBoneIndex( i );
}
```

If I adjust the code above and simply initialize the `initialPosition_` to `Vector3::ZERO` rather than the bone pivot position from the bone metadata, I get the bone bounding boxes in the correct positions, see below.  However the skeleton isn't rendered in the image as all bones are `0,0,0`.

![image|427x500](upload://dCKZKILOPJ9BubNtiTxLaIdo046.png) 

I have a feeling that either or both of the `offsetMatrix_` and `initialPosition_` logic above may not be exactly correct given the source data set and what happens under-the-hood when the model is rendered.  Any suggestions on what may be the cause?

-------------------------

Eugene | 2021-04-12 18:33:45 UTC | #8

Bone bounding box is expected to be in bone space, not object space.
Transform vertices with bone offset matrix... Or maybe inverted bone offset matrix, I don't remember.

-------------------------

Naros | 2021-04-14 14:33:49 UTC | #9

Hi @Eugene, thanks for all the help thus far.  I've been able to resolve most of my issues but there is one that remains that still eludes me and I hope it's super simple.

I have a very basic table model shown below that consists of a single `Geometry`.  When I render the model without adding a `Skeleton`, it renders just fine (see here):

![image|533x264](upload://hMSR7hM85tFtN1G7BLQ0EGvA2Gz.jpeg) 

However, as soon as I add the skeleton, it renders as follows:

![image|457x244](upload://9VbGjJPEVW8oJV887W5sCILH9o5.png) 

The export model's skeletal structure consists of a single bone at 0.0160363 0.772063 -0.0104433.  When I construct the `Skeleton` in Urho3D, the bone is:

```text
parentIndex_ = 0
initialPosition_ = 0.0160363 0.772063 -0.0104433
initialRotation_ = 1 0 0 0
initialScale_ = 1 1 1
```
I've spent the last days really looking at the source code for the engine and I don't see anything that stands out that would cause this rendering distortion.  On some other models with multiple geometry parts, I also get some geometry bits scaled up when applying a skeleton; otherwise renders with without a skeleton attached.

In the model creation step, I literally follow what `Model` does when reading from the `MDL` format.  I simply don't supply any geometry bone mappings but otherwise I supply the same information.  Do you or anyone else have any clues or suggestions on what to check that might cause this?

-------------------------

Eugene | 2021-04-14 14:54:54 UTC | #10

Are you sure your bone indices are all zeros for all vertices?
If you have one bone, vertices should reference one bone as well.

-------------------------

Naros | 2021-04-14 17:27:28 UTC | #11

I assume by bone indices, you're referring to `geometryBoneMappings_`?

If so, the `Vector<PODVector<unsigned>>` contains one element and that `PODVector` contains no entries.  The call to `Model::SetGeometryBoneMappings` does nothing because it reports that all values are zero so `geometrySkinMatrices_` and `geometrySkinMatrixPtrs_` are empty.

If that isn't what you're referring to, could you explain?

-------------------------

Eugene | 2021-04-14 17:48:36 UTC | #12

I am talking about `SEM_BLENDINDICES` elements in VertexBuffer of your model.

-------------------------

Naros | 2021-04-14 18:28:41 UTC | #13

No, I am not supplying that element in the VertexBuffer.  Is that necessary?  I don't recall needing to set anything beyond position, normal, and uv coordinates for my shaders in the old engine. 

I've defined the vertex elements as follows
```
desc.vertexElements_.Push( Urho3D::VertexElement( Urho3D::TYPE_VECTOR3, Urho3D::SEM_POSITION ) );
desc.vertexElements_.Push( Urho3D::VertexElement( Urho3D::TYPE_VECTOR3, Urho3D::SEM_NORMAL ) );
desc.vertexElements_.Push( Urho3D::VertexElement( Urho3D::TYPE_VECTOR2, Urho3D::SEM_TEXCOORD ) );
desc.vertexElements_.Push( Urho3D::VertexElement( Urho3D::TYPE_FLOAT, Urho3D::SEM_BLENDINDICES ) );
```

The model without a skeleton contines to render fine but I'm getting the same result when I add the skeleton to the model.

In the vertex buffer initialization code, it does the following:
```
Urho3D::PODVector<float> data;
for ( unsigned i = 0; i < vertices.Size(); ++i )
{
	auto &vertex = vertices[ i ];

	const auto position = vertex.position.ToUrho3D();
	data.Push( position.x_ );
	data.Push( position.y_ );
	data.Push( position.z_ );
	boundingBox.Merge( position );

	const auto normal = vertex.normal.ToUrho3D();
	data.Push( normal.x_ );
	data.Push( normal.y_ );
	data.Push( normal.z_ );

	data.Push( vertex.uvs->u );
	data.Push( vertex.uvs->v );

	// bone indices (4 bytes all 0)
	data.Push( vertex.boneIndices );
}
```

-------------------------

Eugene | 2021-04-14 18:39:13 UTC | #14

[quote="Naros, post:13, topic:6800"]
No, I am not supplying that element in the VertexBuffer. Is that necessary?
[/quote]
How do you expect skeletal model rendering to work if you don't tell it which bones affect which vertices?
I guess it could default to rendering static model if indices are not provided, but I don't see the point.
I mean, if you don't use skeletal animation, you can just render good old static model instead of skinned one.

-------------------------

