codingmonkey | 2017-01-02 01:02:46 UTC | #1

Hi folks!
I trying to create something like hitBox for my BigBot and it's work with visible other static geometry in hitBox-node, but if i turn off static model it not work.
node still have Collision Shape & Rigidbody but raycast with (DRAWABLE_ANY) return false.

hitBox is a child-node of some bone in Skeleton
it has Rigidbody(mass 0) and CollisionShape(Capsule shape) and StaticModel with std : Cylinder model
also i'm set var for this node "tag" with value "hitbox" for Raycast sorting


[code]
bool Character::RaycastAnyByTag(String tag, float maxDistance, Vector3& hitPos, Vector3& hitNormal, Drawable*& hitDrawable) 
{
	hitDrawable = 0;
	Node* gunNode_ = nodeGuns_->GetChild("JointFireFx", true);
	Ray gunRay = Ray(gunNode_->GetWorldPosition(), nodeGuns_->GetWorldDirection());
	PODVector<RayQueryResult> results;
	RayOctreeQuery query(results, gunRay, RAY_TRIANGLE, maxDistance, DRAWABLE_ANY, -1); // all
	//RayOctreeQuery query(results, gunRay, RAY_TRIANGLE, maxDistance, DRAWABLE_GEOMETRY, 191); // all except 7 bit (layer for fx)

	Octree* octree = GetScene()->GetComponent<Octree>();
	octree->Raycast(query);

	if (results.Size())
	{
		for (unsigned int i = 0; i < results.Size(); i++)
		{
			RayQueryResult& result = results[i];

			Variant fx = result.node_->GetVar("tag");
			if (fx.GetString() != tag) continue;

			hitPos = result.position_;
			hitNormal = result.normal_;
			hitDrawable = result.drawable_;
			return true;
		}
	}
	return false;
}
[/code]

in this video as first static model is - on ( hitBox - works), then i turn off it from view (and hitBox not work).
[video]http://www.youtube.com/watch?v=JvVnHyX8zso[/video]


maybe i'm doing something wrong, but how to make hitBox without visible shapes / model for hit ? 
Is it possible use for Raycast only CollisionShape w Rigidbody ?

-------------------------

devrich | 2017-01-02 01:02:46 UTC | #2

I agree with you that there should be a way to do it and I hope someone explains how :slight_smile:

However for a cheap work-around; you could use 100% transparent texture for any mesh/sub-mesh you want to be invisible...  My only concern on this work-around would be if shadows would ignore the invisiblly-textured sub-meshes or if they would be shown from or on them as if they were non-transparent textured?

-------------------------

cadaver | 2017-01-02 01:02:47 UTC | #3

AnimatedModel raycast already supports returning the hit bone index in the subObject variable of the raycast result, so you should not need to create new (drawable) components for bone hitboxes. The bone bounding boxes are automatically generated from skinned geometry, but you could adjust them if necessary (access Bone from Skeleton from AnimatedModel)

When you have RigidBody / CollisionShape components in the bone node, you can also choose to use PhysicsWorld raycast instead of Octree raycast; in this case the raycast is not depending on drawables at all but only checks against physics shapes.

-------------------------

codingmonkey | 2017-01-02 01:02:47 UTC | #4

>you can also choose to use PhysicsWorld raycast instead of Octree raycast
Thank's guys!
I added to character the opportunity to let the rays through the physical world. 
Now, all works without any fully-aplha transparent objects on the back of the robot )
[code]
bool Character::PhysicRaycastRigidBodyByNodeTag(String tag, float maxDistance, Vector3& hitPos, Vector3& hitNormal, Node*& hitNode)
{
	hitNode = NULL;
	hitPos = Vector3::ZERO;
	hitNormal = Vector3::ZERO;

	PhysicsWorld* pw = GetScene()->GetComponent<PhysicsWorld>();

	Node* gunNode_ = nodeGuns_->GetChild("JointFireFx", true);
	Ray gunRay = Ray(gunNode_->GetWorldPosition(), nodeGuns_->GetWorldDirection());
	PhysicsRaycastResult result;
	
	pw->RaycastSingle(result, gunRay, maxDistance);

	if (result.body_) {
		Node* parentNode = result.body_->GetNode();

		if (parentNode) {
			Variant v = parentNode->GetVar("tag");
			if (v.GetString() == tag) 
			{
				hitPos = result.position_;
				hitNormal = result.normal_;
				hitNode = parentNode;
				return true;
			}
		}
	}
	
	return false;
}
[/code]


>you could use 100% transparent texture for any mesh/sub-mesh you want to be invisible
Yes, I tried so those: NoTextureAlpha with MatDiffColor (1,1,1) and alpha (0.0f) it also work but it consume fillrate of gpu for non-visible things )

> if they would be shown from or on them as if they were non-transparent textured?
I think if you turn off all the shadow masks, shadows will not be visible from this invisible object. 
That's what I did before disabled all  shadows mask and other masks of static model.

-------------------------

devrich | 2017-01-02 01:02:47 UTC | #5

[quote="codingmonkey"]>you could use 100% transparent texture for any mesh/sub-mesh you want to be invisible
Yes, I tried so those: NoTextureAlpha with MatDiffColor (1,1,1) and alpha (0.0f) it also work but it consume fillrate of gpu for non-visible things )[/quote]

Ahhhh i didn't think about the fillrate, I'll have to keep that in mind thanks for that  :smiley: 

[quote="codingmonkey"]> if they would be shown from or on them as if they were non-transparent textured?
I think if you turn off all the shadow masks, shadows will not be visible from this invisible object. 
That's what I did before disabled all  shadows mask and other masks of static model.[/quote]

Thanks for that too, I'm still getting used to how Urho3D works compared to other engines I have used  :slight_smile:

-------------------------

