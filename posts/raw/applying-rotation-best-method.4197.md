vivienneanthony | 2018-04-29 05:08:30 UTC | #1

Hey,

I'm trying to apply rotation current. The best way. I was thinking of getting the automated vehicle rotation. The do something like get the current pitch and roll then inverse it as  quaternion. Then multiply a quaternion identity by each quantity.  Then apply the angular velocity. Replacing the following line "Quaternion delta = Quaternion::IDENTITY					* m_pAutomatedVehicle->GetRotation().Inverse();"

Any feedback is appreciated

Note: I'll like to delete this post. Resolved.

Viv
[code]


void ComputerCoreComponent::HandlePostUpdate(StringHash eventType,
		VariantMap& eventData) {
	if (m_pAutomatedVehicle) {
		float timeStep = eventData[PostUpdate::P_TIMESTEP].GetFloat();

		if (m_LinearVelocity != Vector3::ZERO) {
			// Apply Linear Velocity
			m_pAutomatedVehicle->ApplyImpulse(m_LinearVelocity * 3);

			// Reset all forces
			m_MovementLatitude = m_MovementLongitude = m_MovementVertical =
					0.0f;
		}

		if (m_Yaw != 0.0f) {

					m_pAutomatedVehicle->ApplyRotate(
							Quaternion(m_Yaw * 10 * timeStep, Vector3::UP));

					m_Yaw = 0.0f;
		}

		// Enable Vehicle Mode Balance
		if (m_AutomatedVehicleMode == AutomatedVehicleMode_Enable
				|| m_LinearVelocity != Vector3::ZERO || m_Yaw != 0.0f) {
			// Get from from vehicle
			Quaternion delta = Quaternion::IDENTITY
					* m_pAutomatedVehicle->GetRotation().Inverse();

			float angle;
			Vector3 axis;

			ToAngleAxis(delta, angle, axis);

			if (axis.x_ == 0 || axis.y_ == 0 || axis.z_ == 0) {
				return;
			}

			if (angle > 180.0f) {
				angle = -360.0f;
			}

			// Create a angular
			Vector3 angular = (0.9f * (3.141592653589793 / 180) * angle
					/ timeStep) * axis.Normalized();

			m_pAutomatedVehicle->ApplyAngularVelocity(angular);
		}


	} else {
		//ALPHAENGINE_LOGINFO("Post Update Failed. No Automated Vehicle");
	}
}
[/code]

-------------------------

