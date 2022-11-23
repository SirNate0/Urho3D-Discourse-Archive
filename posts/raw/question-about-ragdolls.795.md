codingmonkey | 2017-01-02 01:02:56 UTC | #1

Hello folks

I'm trying to understand how the Ragdoll works in Urho
And I'm not quite clear what is meant here is the two parameters.

constraint->SetAxis(axis);
constraint->SetOtherAxis(otherAxis);

What is the first method ?
And what does the second ?

And for all connection types you need to set both options ?

Can this once-in-picture to express?
I love the picture (in reference) more than the text)

-------------------------

devrich | 2017-01-02 01:02:56 UTC | #2

In the 13_Ragdoll script example on lines: #363 and #364 shows the use of the axis but I'm not sure how it is applied....

SetAxis( ) [url]http://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_constraint.html#a4ed9f415e1d759a99d02463a472033b4[/url]

SetOtherAxis( ) [url]http://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_constraint.html#a3e1e4103e5778593dccbfc4eafed0119[/url]

I'm trying to figure out the same thing as you.  But I am also having some trouble understanding. because of the use of the words "relative to the other body".

I found this page but constraints are new to me; does this page help any? [url]http://bulletphysics.org/mediawiki-1.5.8/index.php/Constraints[/url]

I have no idea what Urho3D means by "other body"..........

-------------------------

codingmonkey | 2017-01-02 01:02:56 UTC | #3

thanks for [bulletphysics.org/mediawiki-1.5. ... onstraints](http://bulletphysics.org/mediawiki-1.5.8/index.php/Constraints)
how I see there how looks the - CONSTRAINT_CONETWIST )
also before this i'm read this manual : [cs.uu.nl/docs/vakken/mgp/ass ... Manual.pdf](http://www.cs.uu.nl/docs/vakken/mgp/assignment/Bullet%20-%20User%20Manual.pdf) 

>In the 13_Ragdoll script example 
Yes , i see this example, but on C++

i write my code for ragdoll based on this code example:

[code]
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
[/code]

But the main question is: how to choose the vector for these axes ?
why is there forward and back vectors and not a right and up ?
let's say I have a character rig. 
What do I need to look to choose the right direction for joint bending. 
At the local axis of the same bone or to the global axis? 
And why would there otherAxis() needed ?

-------------------------

cadaver | 2017-01-02 01:02:56 UTC | #4

The axes depend on how the model was authored (local coordinate space of each bone.)

In case of that example which uses the Jack model, the correct axes were determined by trial and error.

OtherAxis is the constraint axis in the other connected rigid body; you need to specify both so that the physics knows how to align both bodies connected to the constraint.

If you can choose to author a new model for purposes of animation and ragdolling, I'd recommend to make it so that Z axis is always "forward" (normal convention in Urho3D), so for example a knee joint would rotate around the X-axis.

-------------------------

codingmonkey | 2017-01-02 01:02:56 UTC | #5

Thanks for the reply.
I understand that it is the local space of the bone.

But I found one strange bug, or maybe it's not a bug, maybe i'm just doing something wrong )
I add switch to the R-button between animation models and Ragdoll
[video]https://www.youtube.com/watch?v=tQHokAeZ-No[/video]

And when I switched model to Ragdoll and it fell, I moved it from a different position on the floor (in ragdoll mode). 
Then I turn the animation on again and off the Ragdoll and in this case the model is again the place from which I moved it.

i'm try to fix world pos of main rigidbody then it enabled, but it does not work as it is necessary
[code]
void BotRagdoll::EnableRagdoll(bool value)
{
	isAlive = !value; // flag for animation update proc

	// tunn on/off default rigidbody and big sphere shape in root node
	GetNode()->GetComponent<RigidBody>()->SetEnabled(!value);
	GetNode()->GetComponent<CollisionShape>()->SetEnabled(!value);

  // if is animation on and ragdoll off
  if (isAlive == true) // fix position the main rigidbody by last node position from ragdoll
    GetNode()->GetComponent<RigidBody>()->SetPosition(GetNode()->GetWorldPosition());
	
	// turn-off animation
	Skeleton* skelet = &model->GetSkeleton();
	for (unsigned i = 0; i < skelet->GetNumBones(); i++)
	{
		skelet->GetBone(i)->animated_ = !value;
	}

	// enable/disable ragdoll's rigid bodines in skeleton
	
	Node* botNode = GetNode();
	Node* bone = botNode->GetChild("Bone", true);
	
	bone->GetComponent<RigidBody>()->SetEnabled(value);
	bone->GetComponent<CollisionShape>()->SetEnabled(value);
	bone->GetComponent<Constraint>()->SetEnabled(value);


	Node* center = botNode->GetChild("Center", true);
	center->GetComponent<RigidBody>()->SetEnabled(value);
	center->GetComponent<Constraint>()->SetEnabled(value);
	center->GetComponent<CollisionShape>()->SetEnabled(value);
	
	Node* RukaL = botNode->GetChild("Ruka.L", true);
	RukaL->GetComponent<RigidBody>()->SetEnabled(value);
	RukaL->GetComponent<Constraint>()->SetEnabled(value);
	RukaL->GetComponent<CollisionShape>()->SetEnabled(value);
	
	Node* RukaL001 = botNode->GetChild("Ruka.L.001", true);
	RukaL001->GetComponent<RigidBody>()->SetEnabled(value);
	RukaL001->GetComponent<Constraint>()->SetEnabled(value);
	RukaL001->GetComponent<CollisionShape>()->SetEnabled(value);

	Node* RukaR = botNode->GetChild("Ruka.R", true);
	RukaR->GetComponent<RigidBody>()->SetEnabled(value);
	RukaR->GetComponent<Constraint>()->SetEnabled(value);
	RukaR->GetComponent<CollisionShape>()->SetEnabled(value);

	Node* RukaR001 = botNode->GetChild("Ruka.R.001", true);
	RukaR001->GetComponent<RigidBody>()->SetEnabled(value);
	RukaR001->GetComponent<Constraint>()->SetEnabled(value);
	RukaR001->GetComponent<CollisionShape>()->SetEnabled(value);

	Node* NogaL001 = botNode->GetChild("Noga.L.001", true);
	NogaL001->GetComponent<RigidBody>()->SetEnabled(value);
	NogaL001->GetComponent<Constraint>()->SetEnabled(value);
	NogaL001->GetComponent<CollisionShape>()->SetEnabled(value);

	Node* NogaL002 = botNode->GetChild("Noga.L.002", true);
	NogaL002->GetComponent<RigidBody>()->SetEnabled(value);
	NogaL002->GetComponent<Constraint>()->SetEnabled(value);
	NogaL002->GetComponent<CollisionShape>()->SetEnabled(value);

	Node* NogaR001 = botNode->GetChild("Noga.R.001", true);
	NogaR001->GetComponent<RigidBody>()->SetEnabled(value);
	NogaR001->GetComponent<Constraint>()->SetEnabled(value);
	NogaR001->GetComponent<CollisionShape>()->SetEnabled(value);


	Node* NogaR002 = botNode->GetChild("Noga.R.002", true);
	NogaR002->GetComponent<RigidBody>()->SetEnabled(value);
	NogaR002->GetComponent<Constraint>()->SetEnabled(value);
	NogaR002->GetComponent<CollisionShape>()->SetEnabled(value);
}
[/code]

-------------------------

cadaver | 2017-01-02 01:02:56 UTC | #6

I'm not 100% sure of your case but I've seen this in both Urho3D and Unity where ragdolls are usually created in a similar way by creating physics components to child bone nodes. The child bones move with physics, but nothing moves the root node of the AnimatedModel, so it actually stays in the position where the ragdoll effect began! As the root node position does not affect skinning, you don't notice the error until you switch the ragdoll off.

This is not really a bug and there is no automatic way to fix this, other than taking the world transform of Bip01_Root (or whatever your root bone node is) and copying it to the AnimatedModel root node's world transform. Immediately after you probably have to reset the Bip01_Root bone world transform too to the same value, as due to the hierarchy its offset position would be applied "twice" if you didn't do that.

-------------------------

codingmonkey | 2017-01-02 01:02:58 UTC | #7

>taking the world transform of Bip01_Root (or whatever your root bone node is) and copying it to the AnimatedModel root node's world transform

Thank's cadaver, i'm now fix that with copying first child of MasteBone->Bone world position to root node world position, when ragdoll turn-off
Also need to reset to zero the rigidbody's ...linear velocity of the root node before disabling, otherwise after ragdoll turn-off and if in animation state the root-node has some velocity, they assign again for it.
i'm mean that the rigidbody remembers his speed, after enabling.

-------------------------

