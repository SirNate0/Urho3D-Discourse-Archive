vivienneanthony | 2018-04-19 20:35:16 UTC | #1

Hello,
I have a general question that assistance would be helpful. I have been able to get the physics update to work mostly. So ship flight. I have some code that I use similiar to the CharacterDemo.cpp. 

Right now, I have to simulate gravity of a character which is a node with a rigidbody to a ship node with a rigidbody. When the character enters a ship I flag and save the ship rigidbody and node so the character component has the info as it also handle if a character is locked. 

I'm trying to think of the best way to update the character rigidbody to allow movement inside a ship while maintaining the proper rotation and location inside the ship rigidbody. the character node is a independent node not under the ship node tree.

The rough code is below. The latter code is basically the RigidBody of the ship or whatever chosen object.

[code]


void CharacterComponent::FixedUpdate(float timeStep) {
	static bool usUpdating = false;

	// update if it is server or we set flag that it is local component
	//if (!g_pApp->GetGameLogic()->IsProxy() || m_bIsLocal)
	if (g_pApp->GetAppType() != ApplicationType_Server) {
		// If RigidBody exist and animation controller
		if (m_pBody && m_pAnimControl && !usUpdating) {
			// if character is not locked
			if (m_bLockedPosition == false) {
				// Update the in air timer. Reset if grounded
				if (!m_bIsOnGround) {
					m_InAirTime += timeStep;
				} else {
					m_InAirTime = 0.0f;
				}

				// When CharacterComponent has been in air less than 1/10 second, it's still interpreted as being on ground
				bool softGrounded = (m_InAirTime = 0.0f < g_InAirThreshHoldTime)
						!= 0;

				// Update movement & animation
				const Quaternion& rot = node_->GetRotation();

				// Normalize move vector so that diagonal strafing is not faster
				if (m_MoveDir.LengthSquared() > 0.0f) {
					m_MoveDir.Normalize();
				}

				// Calculate move force
				m_MoveDir *= .5;

				Vector3 MovementImpulse;

				if (softGrounded) {
					// If in air, allow control, but slower than when on ground
					if (m_MoveDir != Vector3::ZERO) {
						if (!m_bStopWalk) {
							if (m_MoveForce != 0.0f) {
								// m_pBody->ApplyImpulse(rot * m_MoveDir * (softGrounded ? m_MoveForce : INAIR_MOVE_FORCE));
								MovementImpulse = rot * m_MoveDir
										* (softGrounded ?
												m_MoveForce : g_InAirMoveForce);
							} else {
								//m_pBody->ApplyImpulse(rot * m_MoveDir * (softGrounded ? MOVE_FORCE : INAIR_MOVE_FORCE));
								MovementImpulse = rot * m_MoveDir
										* (softGrounded ?
												g_MoveForce : g_InAirMoveForce);
							}

							//m_pBody->ApplyImpulse(rot * m_MoveDir);
							m_pBody->ApplyImpulse(MovementImpulse);

						} else {
							//Vector3 moveDir = Vector3::ZERO;
							const Vector3& velocity =
									m_pBody->GetLinearVelocity();

							// Velocity on the XZ plane
							Vector3 planeVelocity(velocity.x_, 0.0f,
									velocity.z_);

							// When on ground, apply a braking force to limit maximum ground velocity
							Vector3 brakeForce = -planeVelocity;
							m_pBody->SetLinearVelocity(brakeForce);

							// Reset Stop Walk
							m_bStopWalk = false;
						}

						// Reset move direction
						m_MoveDir = Vector3::ZERO;

					} else {
						//Vector3 moveDir = Vector3::ZERO;
						const Vector3& velocity = m_pBody->GetLinearVelocity();

						// Velocity on the XZ plane
						Vector3 planeVelocity(velocity.x_, 0.0f, velocity.z_);

						// When on ground, apply a braking force to limit maximum ground velocity
						Vector3 brakeForce = -planeVelocity * g_BrakeForce;
						m_pBody->ApplyImpulse(brakeForce);

					}

					// Jump. Must release jump control inbetween jumps
					if (m_bIsInJump) {
						if (m_bIsOnJump) {
							//Vector3 moveDir = Vector3::ZERO;
							const Vector3& velocity =
									m_pBody->GetLinearVelocity();

							// If vvelocity below 0 or above 1 assume either falling or moving
							if (velocity.y_ < 0.1f && velocity.y_ >= 0.0f) {

								// Apply force to jump
								if (m_JumpForce) {
									m_pBody->ApplyImpulse(
											Vector3::UP * m_JumpForce);
								} else {
									m_pBody->ApplyImpulse(
											Vector3::UP * g_JumpForce);
								}
							} else {
								// If force could not  be apply assume model stopped set In Jump to false
								m_bIsInJump = false;
							}

							m_bIsOnJump = false;
						}
					} else {
						m_bIsOnJump = true;
					}

					// Set rotation based on turned direction
					if (m_TurnDirection == TURN_LEFT) {
						// Get node rotation quaternion
						Quaternion rot = GetNode()->GetRotation();

						// Create a quaternion
						Quaternion baseRot = Quaternion(1.0f, 0.0f, 0.0f, 0.0f);

						// Get a quaternion from a default quaternoin identity
						baseRot.FromAngleAxis(-16, Vector3(0.0f, 1.0f, 0.0f));

						Quaternion NewRot = rot * baseRot;

						float dt;

						if (timeStep > 1.0f / 30.0f) {
							dt = 1.0f / 30.0f;
						} else {
							dt = timeStep;
						}

						//GetNode()->SetRotation(rot.Slerp(NewRot, timeStep/1.0f));
						GetNode()->SetRotation(rot.Slerp(NewRot, dt));
					} else if (m_TurnDirection == TURN_RIGHT) {
						// Get node rotation quaternion
						Quaternion rot = GetNode()->GetRotation();

						// Create a quaternion
						Quaternion baseRot = Quaternion(1.0f, 0.0f, 0.0f, 0.0f);

						// Get a quaternion from a default quaternoin identity
						baseRot.FromAngleAxis(16, Vector3(0.0f, 1.0f, 0.0f));

						Quaternion NewRot = rot * baseRot;

						float dt;

						if (timeStep > 1.0f / 30.0f) {
							dt = 1.0f / 30.0f;
						} else {
							dt = timeStep;
						}

						//GetNode()->SetRotation(rot.Slerp(NewRot, timeStep/1.0f));
						GetNode()->SetRotation(rot.Slerp(NewRot, dt));
					}
				}
			} else {
				// Locked position
				// Constraints handle the position of the character
			}
		}
	}

	// If camera exist
	if (m_pCamera) {
		// Updaw character yaw and povement
		Quaternion Rot(1.0f, 0.0f, 0.0f, 0.0f);

		// Get mouse position
		IntVector2 MousePosition = m_pInput->GetMousePosition();

		// Calculate look based on screen view
		float mWindowBasePitched = (float) (MousePosition.x_
				- (g_pApp->GetGraphics()->GetWidth() / 2));
		float mWindowBaseYaw = (float) (MousePosition.y_
				- (g_pApp->GetGraphics()->GetHeight() / 2));

		float newPitch = Clamp((float) mWindowBasePitched, -90.0f, 90.0f);
		float newYaw = Clamp((float) mWindowBaseYaw, -90.0f, 90.0f);

		// If key is hard reseet
		if (m_pInput->GetKeyDown(KEY_LALT) || m_pInput->GetKeyDown(KEY_RALT)) {
			newPitch = 0;
			newYaw = 0;
		}

		// Create a new quaternion
		Quaternion CameraClamped(newYaw, newPitch, 0.0f);

		Node * pViewCameraNode = m_pCamera->GetNode();

		Quaternion RootRot = pViewCameraNode->GetRotation();

		// Rotate Camera
		if (m_pInput->GetKeyDown(KEY_LCTRL) || m_pInput->GetKeyDown(KEY_RCTRL)
				|| m_pInput->GetKeyDown(KEY_LALT)
				|| m_pInput->GetKeyDown(KEY_RALT)) {
			if (pViewCameraNode) {
				// Removed line to figure out better rotation
				// Quaternion NewRot = RootRot.Slerp(Rot*CameraClamped, timeStep*.99);
				Quaternion NewRot = Rot * CameraClamped;

				pViewCameraNode->SetRotation(NewRot);
			}
		}
	}

	// if not updating
	if (!g_pApp->GetGameLogic()->IsProxy() && !usUpdating) {

		// Get node rotation quaternion
		Vector3 pos = m_pBody->GetPosition();
		Quaternion rotation = m_pBody->GetRotation();

		// if position and rotation different
		if (rotation != m_PreviousRotation || pos != m_PreviousPosition) {

			// if changed
			VariantMap data;
			data["CONTENT_ID"] = 1;
			data[CHARACTER_MOVE::P_GAME_ASSET_ID] = node_->GetID();
			data[CHARACTER_MOVE::P_GAME_ASSET_LOCATION] = node_->GetVar(
					"location").GetString();
			data[CHARACTER_MOVE::P_NEW_ORIENTATION] = rotation;
			data[CHARACTER_MOVE::P_NEW_POSITION] = pos;
			SendEvent(REMOTE_EVENT_CHARACTER_MOVE, data);

			// save position
			m_PreviousPosition = pos;
			m_PreviousRotation = rotation;
		}
	}

	// Reset grounded flag for next frame
	m_bIsOnGround = false;
	m_TurnDirection = TURN_NONE;

	// Reset move direction
	m_MoveDir = Vector3::ZERO;

}
[/code]

[code]
void CharacterComponent::SetGravityNode(Node * pNode) {
	{
		if (pNode) {
			m_pGravityNode = pNode;
			m_pGravityRigidBody = pNode->GetComponent<RigidBodyComponent>();
		} else {
			m_pGravityNode = nullptr;
			m_pGravityRigidBody = nullptr;
		}

	}
}
[/code]

-------------------------

vivienneanthony | 2018-04-19 21:23:42 UTC | #2

The first movement I'm trying is if I can get it to compile

[code]
	if (m_pGravityRigidBody) {
								btTransform transform;

								// Get world transform
								Vector3 impulse =
										m_pGravityRigidBody->GetRotation()
												* m_pGravityRigidBody->GetPosition();

								Vector3 newMovementImpulse = impulse
										* Vector3(0.0f, -9.81f, 0.0f)
										* MovementImpulse;

								m_pBody->ApplyImpulse(newMovementImpulse);
							} else {
								m_pBody->ApplyImpulse(MovementImpulse);
							}
[/code]

-------------------------

vivienneanthony | 2018-04-19 23:51:06 UTC | #3

I think I might have to confusing with the post.

-------------------------

vivienneanthony | 2018-04-20 03:16:58 UTC | #4

This better explains it. If the player is in the ship. I would have to fake gravity inside the ship in the character component shown above if the character is kinematic.

https://www.youtube.com/watch?v=tbiNPjwxMcg&t=44s

-------------------------

SirNate0 | 2018-04-20 05:27:14 UTC | #5

If the other movements (walking around and such) would still work fine my first suggestion would be to just set the parent of the character to the ship when the character enters it. Otherwise perhaps just watch how the ship transforms from one update to the next and transform the player accordingly.

-------------------------

vivienneanthony | 2018-04-20 13:18:25 UTC | #6

[quote="SirNate0, post:5, topic:4190, full:true"]
If the other movements (walking around and such) would still work fine my first suggestion would be to just set the parent of the character to the ship when the character enters it. Otherwise perhaps just watch how the ship transforms from one update to the next and transform the player accordingly.
[/quote]

The latter probably would be a better solution. I would like to keep the independence of the character from the ship structure.  So, like you mentioned, I have to apply the same transform of the ship to the player or maybe add the DOF  for Generic 6 Degrees of Freedom (DoF) Constraint bullet physics constraint.

-------------------------

