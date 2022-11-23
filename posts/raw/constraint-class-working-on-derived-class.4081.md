vivienneanthony | 2018-03-11 03:44:12 UTC | #1

Hi

I'm working on a constraint class that is derived from constraint. It seems the constraint is created. If I move a node that rigidbodies changes to match the constraint. The problem is if I hit play letting the physics run normally. The constrained rigidbodies don't move.

Do anyone know where in the urho3d code where they are updating per frame? Or is it entirely on the bullet physics.

Vivienne

-------------------------

RCKraken | 2018-03-11 10:02:52 UTC | #2

Did you assign the Rigidbody a mass?

-------------------------

Sinoid | 2018-03-11 16:27:17 UTC | #3

[quote="vivienneanthony, post:1, topic:4081"]
Do anyone know where in the urho3d code where they are updating per frame? Or is it entirely on the bullet physics.
[/quote]

Bullet does it.

Check if you're adding the constraint to the physics world. `Constraint::OnSceneSet` is the part that does it, though it's also done elsewhere during attribute configuration - which is probably why you have it working while you're setting things up but not when scene construction for playback happens.

That's assuming that *"The constrained rigidbodies don’t move"* means they don't comply with the constraint and not outright refusal to move (unless that makes sense in the context, ie. no gravity).

-------------------------

vivienneanthony | 2018-03-13 03:32:57 UTC | #4

I looked over I looked over the code. The issue was with the rigid body mass and the constraint points. It seems to almost work. Right now it stays in the right spot but rotates continously. I'm working on the proper constraint so it stays aligned. So will post a video of what I mean. The current code is like.

[code]
// Set restrictions
Constraint::SetConstraintType(CONSTRAINT_POINT);

// Set Other body to this;
Constraint::SetOtherBody((RigidBody *) parentRigidBody);

// Set to other center
Constraint::SetOtherPosition(GetNode()->GetPosition());

// Get position
Constraint::SetPosition(Vector3::ZERO);


Constraint::SetRotation(Quaternion::IDENTITY);

Constraint::SetOtherRotation(Quaternion::IDENTITY);


// Disable Collision between the parent
Constraint::SetDisableCollision(true);

// Set Low Limit
SetLowLimit(Vector2(0.0f, 0.0f));

// Set High Limit
SetHighLimit(Vector2(0.0f, 0.0f));

// Set to constraint constructed
m_bConstraint = true;
[/code]

The objects in the constraint attached stays in the right space but start rotating depending on the fall in the constrained spot. Which I am thinking has to do with the angular and linear factors being 1 not zero. I could be mistaken.

https://www.youtube.com/watch?v=CIh1uP3Wflo

-------------------------

vivienneanthony | 2018-03-21 00:36:41 UTC | #6

So, there was several things happening that needed to be updated. I updated the model and also switched to right coordinate system in consideration of the calculation. Plus some Urho3D hack ad-hoc to use fixed constraints. The end results is okay. I am assuming if I get the physics engine btRigid and shape I can get the mass weights as specific spots and adjust the thrust. As for stabilization, put in side thrusters that acts like lateral stabilizers.

https://www.youtube.com/watch?v=3tBglY2bS9E&t=5s

-------------------------

vivienneanthony | 2018-03-22 18:43:58 UTC | #7

I found this code online. This is for Unity. I think it might be able to help me get some stablization after a impulse is applied. I'm assuming the equivalent for angularVelocity() is the GetAngularVelocity() of the parent rigidbody, Mathf.Rad2Deg is 360/(3.14*2). The magnititude I'm not sure because I thought GetAngularVelocity() is the magnititude. There has to be a Urho3D equivalent.

[code]
public float stability = 0.3f;
 public float speed = 2.0f;
 // Update is called once per frame
 void FixedUpdate () {
     Vector3 predictedUp = Quaternion.AngleAxis(
         rigidbody.angularVelocity.magnitude * Mathf.Rad2Deg * stability / speed,
         rigidbody.angularVelocity
     ) * transform.up;
     Vector3 torqueVector = Vector3.Cross(predictedUp, Vector3.up);
     rigidbody.AddTorque(torqueVector * speed * speed);
 }
[/code]

-------------------------

vivienneanthony | 2018-03-22 18:46:27 UTC | #8

The code in the video is this.

[CODE]

void PropulsionThrusterComponent::OnUpdate(float timeStep) {
	// If thrust active is true
	if (m_bThrust) {

		// Check if a parent rigid body exist
		if (!m_ParentRigidBody) {
			// Get Components
			m_ParentRigidBody = m_pNode->GetParent()->GetComponent<
					RigidBodyComponent>();

			// If failed getting the parent rigid body return
			if (!m_ParentRigidBody) {
				return;
			}
		}

		// Turn off Kinematic
		if (m_ParentRigidBody->IsKinematic()) {
			m_ParentRigidBody->SetKinematic(false);
		}

		// Apply force up
		m_Impulse = Vector3::FORWARD * m_ThrustLevel;

		// Get Rotations
		m_ParentWorldRotation = m_pNode->GetParent()->GetWorldRotation();
		m_ChildRotation = m_pNode->GetRotation();

		// Create force level
		m_Force = (m_ParentWorldRotation * (m_ChildRotation * m_Impulse));

		m_ParentRigidBody->ApplyImpulse(m_Force * timeStep,
				Vector3(m_pNode->GetPosition().x_, -0.9f,
						m_pNode->GetPosition().z_));
	}
}
[/code]

-------------------------

Sinoid | 2018-03-22 18:50:13 UTC | #9

Magnitude is synonymous with Length. Is that what you're looking for?

Cartesian naming favors length, tensor/covector naming favors magnitude - it's the same thing though.

-------------------------

vivienneanthony | 2018-03-22 19:17:49 UTC | #10

If I am not mistaken, the length or magnitude would be normalized. As the squared of the velocity. 

The unity code uses angularvelocity and angularvelocity.magnitude. Equivalent would be angularvelocity type form GetAngularVelocity() and then the mangnitude GetAngularVelocity().Length or squared.

-------------------------

vivienneanthony | 2018-03-28 04:26:46 UTC | #12

I'm working on the ship. Right now, I am trying to stabilizing.  I have the following code. The last two lines gets the linear velocity of the parent rigid body and applys a impulse to its lateral movement.  The question is the linear velocity the local velocity of the rigid body. I feel like I should be doing the  linear velocity x and y multiplied by the rotation of the rigid body.

Ideally I would like make it stabilize based on the fixed vector and rotation meaning the parent rigid body. For example, if in a collision box trigger a station. It use the collision box vector and rotation. If in space zero gravity outside maybe to a target and if no target no stabilization since space has no up and down direction.

[code]
void PropulsionThrusterComponent::OnUpdate(float timeStep) {
	// If thrust active is true
	if (m_bThrust) {

		// Check if a parent rigid body exist
		if (!m_ParentRigidBody) {
			// Get Components
			m_ParentRigidBody = m_pNode->GetParent()->GetComponent<
					RigidBodyComponent>();

			// If failed getting the parent rigid body return
			if (!m_ParentRigidBody) {
				return;
			}
		}

		// Turn off Kinematic
		if (m_ParentRigidBody->IsKinematic()) {
			m_ParentRigidBody->SetKinematic(false);
		}

		// Apply force up
		m_Impulse = Vector3::BACK * m_ThrustLevel;

		// Get Rotations
		m_ParentWorldRotation = m_pNode->GetParent()->GetWorldRotation();
		m_ChildRotation = m_pNode->GetRotation();

		// Create force level
		m_Force = (m_ParentWorldRotation * (m_ChildRotation * m_Impulse));

		m_ParentRigidBody->ApplyImpulse(m_Force * timeStep,
				Vector3(m_pNode->GetPosition().x_,m_pNode->GetPosition().y_,
						m_pNode->GetPosition().z_));

//		// Get angular Velocity
//		Vector3 currentAngularVelocity =m_ParentRigidBody->GetAngularVelocity();
//		double RadiusToDegree = 360 * (3.14159 / 2);
//
//		float stability = 0.5f;
//		float speed = 0.2f;
//
//		Quaternion RotationFromAngleAxis = Quaternion();
//
//		RotationFromAngleAxis.FromAngleAxis(
//				currentAngularVelocity.LengthSquared() * RadiusToDegree
//						* stability / speed, currentAngularVelocity);
//
//		Vector3 predictedUp = RotationFromAngleAxis * Vector3::UP;
//
//		// Calculate a torqueVector
//		Vector3 torqueVector = predictedUp.CrossProduct(Vector3::UP);
//
//		m_ParentRigidBody->ApplyImpulse(torqueVector * speed);

			// Get linear velocity
		Vector3 linearVelocity = m_ParentRigidBody->GetLinearVelocity();

		// Get rigid body rotation and change linear assuming it's a local linear velocty
		linearVelocity = m_ParentRigidBody->GetRotation()*linearVelocity;

		// Inverse forward and reverse
		m_ParentRigidBody->ApplyImpulse(Vector3(-(linearVelocity.x_), 0, -(linearVelocity.z_)));
	}
}
[/code]

-------------------------

vivienneanthony | 2018-03-28 04:31:01 UTC | #13

This is the video to the above. Maybe someone has a idea how best to negate forward and backward movement if rotated. I guess on the local coordinate. I'm trying to think of the best way to balance out. So the rotation on x,z in relationship to a fixed point stay balance using impulse.

https://www.youtube.com/watch?v=fS2aa7jYRW8

-------------------------

