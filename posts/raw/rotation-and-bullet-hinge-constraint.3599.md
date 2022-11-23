esakylli | 2017-09-23 14:51:08 UTC | #1

My use case is this:
I have created a Node with a RigidBody, which I have rotated 90 degrees round z-axis.
Then I have created a hinge constraint on it, connecting it to another RigidBody.
I want to rotate the body round x-axis. I have set the axis on the constraint like this:
constraint.SetAxis(Vector3.UnitY);
constraint.SetOtherAxis(-Vector3.UnitX);

The rotation works. But the thing I'm stuck on is setting the limit on the constraint.
When I set low and high limit to 0 the body rotates automatically 90 degrees!?
But if I set the limit to 90, the body doesn't rotate.
If I don't rotate the body (and rotate it round y-axis instead), and having the limit set to 0, it doesn't rotate automatically.
It makes me believe that the angle starting values are different when rotating round y-axis and round x-axis?

I would also like to know how many degrees the body has rotated round x-axis, in able to set it on the limit (so that the body is locked in current angle). But I can't get this to work, probably because of my first problem (the 90 degrees offset).

-------------------------

stark7 | 2017-09-24 17:13:22 UTC | #2

First you need to set both axes to be the same for hinge.

Setting the low and high limit to be the same, creates a fixed relative constraint, what you want is to set the low limit higher than the high limit for the body to move freely around the constraint axes/points.

You also want to create the constraint on your other body that does the constrained movement because it simplifies the process of removing these when you remove bodies.

-------------------------

esakylli | 2017-09-26 14:05:41 UTC | #3

I don't know if I was clear about my requirements...

On creation I want to lock the bodies in place, so that they don't rotate (hence setting both low and high limit to 0).
It's when the user takes some action in the game I set the low limit to -180 and the high limit to 180, so that the body can rotate freely 360 degrees.
And when the user takes another action I want to lock the body in it's current rotation angle (by setting the low and high limit to the same).
Once the bodies and constraint are created at startup I don't want to remove any of them.

My code (in regard to the body and constraint creation) is basically based on the Urho sample VehicleDemo.
In my case though, I have the node rotated (before creating the body and constraint) and I want to lock the rotation initially.
And the rotation works, it's just setting the limit right where I have problems.

I don't know if my problem lies in the constraint creation or a faulty assumption of how the limits/angle values works on the different axis...
If we talk generally about quaternions and starting angle values on the different axis, do you know of any good internet resource that explains this in a good way (preferably with a visual explanation)?

-------------------------

Modanung | 2017-09-26 15:50:58 UTC | #4

Have you tried with debug rendering?

-------------------------

esakylli | 2017-09-27 11:24:39 UTC | #5

Yes, in debug it looks OK.
It's just that the body rotated 90 degrees off (round the right axis), from what I would expect.

-------------------------

esakylli | 2017-09-29 14:50:19 UTC | #7

I have rotated my node/body round x-axis instead and set the constraint axis like this:
constraint.SetAxis(Vector3.UnitY);
constraint.SetOtherAxis(-Vector3.UnitZ);

Now I can rotate the body round z-axis, but upon creation the body automatically rotates 180 degrees to settle at angle 0 (which is what I have set the limits to).
And when I look at the debug rendering, it shows that the constraint axis is pointing downwards instead of upwards as I would expect (hence the 180 degrees automatic rotation).
So it seems that I have trouble understanding the direction of the axis... Could it have something to do with that Bullet expects the axis to be defined in forward-direction for the hinge-constraint?

Anyway, instead I was thinking of maybe it's better to try to read out the hinge angle from the constraint and use that to lock the body in it's current axis rotation.
I found the below functions in the Bullet constraint code, which I might be able to use.
Problem is that I'm using UrhoSharp and can't access those Bullet-specific functions (only Urho-specific code)... so I'm asking here for help, if some kind person could translate that code into Urho-specific C++ code (then I could port that over to C# code)?

		btScalar btHingeConstraint::getHingeAngle()
		{
			return getHingeAngle(m_rbA.getCenterOfMassTransform(), m_rbB.getCenterOfMassTransform());
		}

		btScalar btHingeConstraint::getHingeAngle(const btTransform& transA,const btTransform& transB)
		{
			const btVector3 refAxis0 = transA.getBasis() * m_rbAFrame.getBasis().getColumn(0);
			const btVector3 refAxis1 = transA.getBasis() * m_rbAFrame.getBasis().getColumn(1);
			const btVector3 swingAxis = transB.getBasis() * m_rbBFrame.getBasis().getColumn(1);
			//	btScalar angle = btAtan2Fast(swingAxis.dot(refAxis0), swingAxis.dot(refAxis1));
			btScalar angle = btAtan2(swingAxis.dot(refAxis0), swingAxis.dot(refAxis1));
			return m_referenceSign * angle;
		}

-------------------------

esakylli | 2017-09-30 12:35:50 UTC | #8

I came up with the C# code below. It seems to work at a quick test (needs more testing though).
I would be very grateful if someone could confirm that the math is right, because I'm not that comfortable with the matrix multiplications and using the "columns" from it.

		private static float GetHingeAngle(RigidBody bodyA, RigidBody bodyB, Constraint hingeConstraint)
		{
			Matrix4 matrixPosA = Matrix4.CreateTranslation(bodyA.Position) * Matrix4.Rotate(bodyA.Rotation);
			Matrix4 matrixPosB = Matrix4.CreateTranslation(bodyB.Position) * Matrix4.Rotate(bodyB.Rotation);

			Matrix4 matrixRotA = Matrix4.Rotate(hingeConstraint.Rotation);
			Matrix4 matrixRotB = Matrix4.Rotate(hingeConstraint.OtherRotation);

			return GetHingeAngle(matrixPosA, matrixPosB, matrixRotA, matrixRotB);
		}

		private static float GetHingeAngle(Matrix4 matrixPosA, Matrix4 matrixPosB, Matrix4 matrixRotA, Matrix4 matrixRotB)
		{
			//Vector4 refAxis0 = matrixRotA.Column0;
			//Vector4 refAxis1 = matrixRotA.Column1;
			//Vector4 swingAxis = matrixRotB.Column1;
			Vector4 refAxis0 = (matrixPosA * matrixRotA).Column0;
			Vector4 refAxis1 = (matrixPosA * matrixRotA).Column1;
			Vector4 swingAxis = (matrixPosB * matrixRotB).Column1;

			float dot1 = Vector4.Dot(swingAxis, refAxis0);
			float dot2 = Vector4.Dot(swingAxis, refAxis1);

			float angle = (float)Math.Atan2(dot1, dot2);
			angle = MathHelper.RadiansToDegrees(angle);
			System.Diagnostics.Debug.WriteLine("** angle = " + angle);
			return angle;
		}

-------------------------

esakylli | 2017-10-02 17:40:45 UTC | #9

The code worked only on startup (when bodies and constraint are created).
As soon as I rotate the body (via ApplyTorque) it doesn't work.
I tried with this code also (for defining the three axis):

			Vector4 refAxis0 = Vector4.Transform(matrixRotA.Column0, matrixPosA);
			Vector4 refAxis1 = Vector4.Transform(matrixRotA.Column1, matrixPosA);
			Vector4 swingAxis = Vector4.Transform(matrixRotB.Column1, matrixPosB);

But it doesn't work either.

Doesn't anyone have any suggestions I could try? Please...

-------------------------

