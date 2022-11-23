vivienneanthony | 2017-01-02 01:00:11 UTC | #1

Hey,
Quick question. Does this code make sense? I have a character node which has a child node that is  a camera. I want to simulate eye movement in first person. The code isn't complete but I wonder does these lines make sense. I will have to add cameracontrol to the character class. to make it work and update some events.

Vivienne

Brainstorming
I think I would have to add camera_yaw and camera_pitch to controls_ in controls.h and reset it to 0.



[code]

// Update a camera control like a eye
character_->controls_.camera_yaw_ += (float)input->GetMouseMoveX() * YAW_SENSITIVITY;
character_->controls_.camera_pitch_ += (float)input->GetMouseMoveY() * YAW_SENSITIVITY;


// Turn head to camera pitch, but limit to avoid unnatural animation
Node* cameraNode = characterNode->GetChild("camerafistperson", true);

Quaternion cameraRotation = GetRotation();

// Clamp direction of the camera control
float limitPitch = Clamp(character_->controls_.camera_yaw_ , -90.0f, 90.0f);
float limitYaw = Clamp(character_->controls_.camera_pitch_ , -90.0f, 90.0f_);

// Create a new rotation from the current rotation and limit of pitch and yaw
Quaternion newCameraRotation = cameraRotation * Quaternion(limitPitch, Vector3(1.0f, 0.0f, 0.0f)*Quaternion(limitYaw, Vector3(0.0f,0.0f, 1.0f);


// Change Camera Rotation
cameraNode_->SetRotation(newCameraRotation);
[/code]

-------------------------

