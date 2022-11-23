yushli | 2017-01-02 01:11:02 UTC | #1

Suppose there is an animated Model of human being with head, body, arms and legs. It has several animations such as walk, run, roll. If different parts are hit by a bullet during an animation, it will cause different damages. How can I simulate this situation with Bullet library in Urho3D? Specifically:
1. What kind of collision shape should be used? I suppose it should be SetTriangleMesh. But it may not reflect different parts inside the mesh.
2. How can I make the bullet collision shape sync with the animated model when it runs a certain animation? 
3. If a collision happens, is there a way to tell which bone inside the skeleton the collision takes place?

Maybe there is a completely different way to achieve this in Urho3D? Thanks for any help.

-------------------------

1vanK | 2017-01-02 01:11:03 UTC | #2

[quote="yushli"]Suppose there is an animated Model of human being with head, body, arms and legs. It has several animations such as walk, run, roll. If different parts are hit by a bullet during an animation, it will cause different damages. How can I simulate this situation with Bullet library in Urho3D? Specifically:
1. What kind of collision shape should be used? I suppose it should be SetTriangleMesh. But it may not reflect different parts inside the mesh.
2. How can I make the bullet collision shape sync with the animated model when it runs a certain animation? 
3. If a collision happens, is there a way to tell which bone inside the skeleton the collision takes place?

Maybe there is a completely different way to achieve this in Urho3D? Thanks for any help.[/quote]

Just use collections standart shapes (spheres, capsules) and attach its to bones. Also enable "IS Trigger" option for detect collisions with bullet without physics simulation. So u can detect part of model which was hitted.

-------------------------

yushli | 2017-01-02 01:11:03 UTC | #3

Thanks for your reply. That helps a lot.
And I also find the sample code in the  13_Ragdolls that uses the method similar to yours.

Just that the code 
 CreateRagdollBone("Bip01_R_UpperArm", SHAPE_CAPSULE, Vector3(0.15f, 0.35f, 0.15f), Vector3(0.1f, 0.0f, 0.0f),
            Quaternion(0.0f, 0.0f, 90.0f));
looks really handwritten and time consuming. 

Is this kind of data(size,position,rotation) of each collision shape can be automatically calculated by given the animated model, with the information of the mesh and the bones of the skeleton?

-------------------------

cadaver | 2017-01-02 01:11:03 UTC | #4

You could iterate the skeleton and use the bones' bounding information. The ragdoll is setup by hand since the rotations or limits of the joints are non-obvious or not directly observable from the skeleton. But then, the skeleton is derived from the data needed by the artist for skinning and animation, which may not be the same what the game designer would decide to use for hitboxes.

-------------------------

yushli | 2017-01-02 01:11:03 UTC | #5

I use the following code in 13_Ragdolls CreateRagdoll.cpp after line 56 to iterate over the skeleton:
[code]
auto& bones = node_->GetComponent<AnimatedModel>()->GetSkeleton().GetBones();
		for (auto& bone : bones) {
			auto& name = bone.name_;
			if (name == "Bip01_Head" || name == "Bip01_L_UpperArm" ||
				name == "Bip01_L_Forearm" || name == "Bip01_L_Thigh" ||
				name == "Bip01_L_Calf") {
				CreateRagdollBone(name, SHAPE_BOX, Vector3(bone.boundingBox_.max_.x_ - bone.boundingBox_.min_.x_, bone.boundingBox_.max_.y_ - bone.boundingBox_.min_.y_, bone.boundingBox_.max_.z_ - bone.boundingBox_.min_.z_), bone.initialPosition_, bone.initialRotation_);
			}
		}
[/code]
It turns out that some shapes have rotation and postion problems. 

[img]http://zuoyouxi.gamemei.com/liyusheng/boundingBox.png[/img]

-------------------------

cadaver | 2017-01-02 01:11:03 UTC | #6

Sure, they're bounding AABB's and bounding spheres, and for the AABBs it totally depends on the base pose (and the axes the bones use in that pose) whether they're actually good. Though I don't think the collisions should look as wonky as that. Are you taking bones' rotation into account? (The AnimatedModel raycast uses bone hitboxes already, in a purely graphical sense, and it should work better than that.)

I don't think you're going to get a very good automatic solution out of the box. You could look into Unity's RagdollWizard script, which is basically automatic ragdoll and collider parameters creation based on the user specifying the "key" bones. Then it inspects the vertex data to find the body part dimensions. This is not a lot different what the Urho importer programs are already doing for bone hitbox determination (basically, find vertices that are affected "enough" by a bone and those form the hitbox), but maybe it's more intelligent. Not sure.

-------------------------

yushli | 2017-01-02 01:11:03 UTC | #7

The code passes bone.initialPosition_ and bone.initialRotation_ into CreateRagdollBone. Do I need to consider the bone's parent's position and rotation? As for accuracy, I think as long as the AABB bounding box is oriented and positioned correctly that will be good enough, as shown in this image.

I don't know Urho3D has hitbox implementation. That sounds good for an automatic solution. Would you like to point me to some source code/ sample code about that? Thank you.

-------------------------

cadaver | 2017-01-02 01:11:04 UTC | #8

I was incorrect, it probably wasn't the rotation that was missing, but the bounding box's center in relation to the bone. By default, if no offset is specified, a box collisionshape gets centered to the node.

Here's an AngelScript snippet that can be inserted to the Ragdoll sample to create trigger rigidbodies that should be accurate representation of the bone hitboxes. Note that when I tested it the physics simulation got bogged down by all the interpenetration that resulted, so maybe a better approach on the whole is to only use a coarse collision primitive, like a capsule for the whole character, and when that detects a hit, then check against the bones (which don't even need physics objects, you can just use math)

[code]
            // Create trigger rigidbody & box collider to each bone
            for (uint i = 0; i < modelObject.skeleton.numBones; ++i)
            {
                Bone@ bone = modelObject.skeleton.bones[i];
                Node@ boneNode = bone.node;

                RigidBody@ rb = boneNode.CreateComponent("RigidBody");
                rb.trigger = true;
                CollisionShape@ c = boneNode.CreateComponent("CollisionShape");
                c.SetBox(bone.boundingBox.size, bone.boundingBox.center);
            }
[/code]

-------------------------

yushli | 2017-01-02 01:11:04 UTC | #9

That works terrific! Thank you for your kind help. Urho3D rules!

-------------------------

Mike | 2017-01-02 01:11:05 UTC | #10

Bounding box is computed using nearest vertices and gives rather good results.
However, for joint attachment points I am using the model's node Y position to accurately/perfectly position the rigid bodies and constraints.
Maybe it would be good to compute bones' bounding box on the Y axis that way in AssetImporter and blender exporter.

-------------------------

yushli | 2017-01-02 01:11:07 UTC | #11

@Mike, would you like to share some code on how to do it your way?

-------------------------

Mike | 2017-01-02 01:11:10 UTC | #12

Yes, I'm currently out, I'll have to dig into my compy when I'll get back home saturday or sunday.

-------------------------

Mike | 2017-01-02 01:11:21 UTC | #13

In sample 13_Ragdolls, at the end of CreateRagdollBone() :

[spoiler][code]
		// Use bone's bounding box to compute its CollisionShape's size and position offset
		AnimatedModel@ model = node.GetComponent("AnimatedModel");
		Skeleton@ skeleton = model.skeleton;
		Bone@ bone = skeleton.GetBone(boneName);
		BoundingBox bbox = bone.boundingBox;
		Vector3 shapeSize = bbox.size;
		Vector3 posOffset = bbox.center;

		// Compute Bone length as we can't rely only on bbox to match joints precise location
		if (boneNode.numChildren > 0)
			shapeSize.y = (boneNode.children[0].worldPosition - boneNode.worldPosition).length;

		// We use either a box or a capsule shape for all of the bones
		CollisionShape@ shape = boneNode.CreateComponent("CollisionShape");
		if (type == SHAPE_BOX)
			shape.SetBox(shapeSize, posOffset, rotation);
		else
			shape.SetCapsule(shapeSize.x, shapeSize.y, posOffset, rotation);
[/code][/spoiler]

Note that for the capsules this doesn't work at all with Jack (bones bounding box inaccuracy), so experiment with one of your own models.

-------------------------

yushli | 2017-01-02 01:11:24 UTC | #14

Thanks for sharing this.

-------------------------

