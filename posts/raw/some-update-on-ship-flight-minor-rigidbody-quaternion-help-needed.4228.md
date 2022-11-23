vivienneanthony | 2018-05-09 00:25:15 UTC | #1

Hello,
I have a general question. If anyone can help. I was able to create a flyable ship in both a zero gravity and artificial gravity environment. Seen the video.

The issue is  I'm trying to implement a complete stop in a zero gravity in the script. The vehicle has a auto-balance code that use quaternions to balance. I create a quaternion identity of the ship multipilied by a quaternion of the yaw with the up angle. Then I use the quaternion produced from getting the inverse of the current ship rotation. Ironically, it works. In a environment simulated gravity it functions but if I put the same ship i a zero gravity environment then do a complete stop of linear and angular velocity to zero. The  balance code produces still a rotation very small but if disabled the ship dead stops as intended.

Line 311-362 and ToAngleAxis on the bottom is the basic part that allows the flight.

https://pastebin.com/4raBMWy1 

You can see this happen here.

Note
2:06 Doesn't work fully with auto on.
2:16 Works with auto off

https://www.youtube.com/watch?v=ouKbAKKqENY


Maybe someone have a idea??

-------------------------

SirNate0 | 2018-05-09 03:03:30 UTC | #2

Should you multiply by the angle and not just the timestep in the auto balancing code when you calculate the angular velocity?

-------------------------

Lumak | 2018-05-09 05:12:17 UTC | #3

Fixed angle adjustment might be a way to go.
[code]
        float lerpRate = 3.0f;
        Quaternion qnewRot;
        qnewRot.FromLookRotation(node_->GetWorldDirection().Orthogonalize(Vector3::UP), Vector3::UP);
        qnewRot = hullBody_->GetRotation().Slerp(qnewRot, lerpRate * timeStep).Normalized();
        hullBody_->SetRotation(qnewRot);

[/code]

-------------------------

vivienneanthony | 2018-05-10 18:54:14 UTC | #4

[quote="SirNate0, post:2, topic:4228, full:true"]
Should you multiply by the angle and not just the timestep in the auto balancing code when you calculate the angular velocity?
[/quote]


I think I use the angle and timepstep because to not over compensate the rotation.

-------------------------

vivienneanthony | 2018-05-10 19:06:11 UTC | #5

[quote="Lumak, post:3, topic:4228"]
Fixed angle adjustment might be a way to go.
[/quote]

I'm going try that and see what happens

-------------------------

vivienneanthony | 2018-05-12 17:13:17 UTC | #6

[quote="Lumak, post:3, topic:4228"]
Fixed angle adjustment might be a way to go.
[/quote]

It worked less reliably. I tried simplifying the process by calculating the quaternion difference between  a quaternion with yaw only and the inverse of the current rotation like before. Then using the inverse of the erulerangle to create the velocity change.

I think the issue might be how it creates the target yaw. I could use a varialbe with fix yaw but it will become problematic.

[code]
// Get Rotation in Quaternion
				Quaternion vehicleRotation = m_pAutomatedVehicle->GetRotation();

				// Create a Identity which is one
				Quaternion targetRotation = Quaternion::IDENTITY;

				// Create a angle axis using the current vehicle rotation specifically the rigidbody
				targetRotation.FromAngleAxis(vehicleRotation.YawAngle(),
						Vector3::UP);

				// Times the rotations by the inverse
				Quaternion deltaRotation = targetRotation
						* vehicleRotation.Inverse();

				// Convert delta time to axis and angle
				//ToAngleAxis(deltaRotation, angle, axis);

				Vector3 degrees = deltaRotation.EulerAngles();

				Vector3 test = -degrees.Normalized() * timeStep;

				// Apply angular velocity to vehicle
				m_pAutomatedVehicle->ApplyAngularVelocity(test);
[/code]

-------------------------

Lumak | 2018-05-12 19:00:56 UTC | #7

Do you know what that code snippet does? It simply flattens out **any** pitch and roll angle regardless of linear and angular velocity. If you used only that and nothing else it's guarantee it'll do what it's intended, but if you try to add other stuff with it then it'll probably not work.

-------------------------

vivienneanthony | 2018-05-12 21:11:39 UTC | #8

[quote="Lumak, post:7, topic:4228, full:true"]
Do you know what that code snippet does? It simply flattens out **any** pitch and roll angle regardless of linear and angular velocity. If you used only that and nothing else it’s guarantee it’ll do what it’s intended, but if you try to add other stuff with it then it’ll probably not work.
[/quote]

The reason why I'm trying to account the rotation because I'm letting the physics handle most of the movement. I think if I try fix rotation like set rotation. It would throw collisions off because I'm not accounting for physics movement.

So I need to account for rotation and angular velocity.

The original code handled it better move foward up and down or rotating. When moving in several directions up and right. It doesn't flatten out like expected to zero pitch and zero roll. I have a idea that i should use the node world rotation and othorgonal instead of the quaternion with the yaw rotation.

-------------------------

Lumak | 2018-05-12 22:23:04 UTC | #9

I see. I think I understand what you mean. It's hard to determine the kind of dynamics that the other person is trying to achieve despite how much description that's given.  

One last thing that I want to mention -- knowing the desired quaternion (referring to the **qnewRot** from the snippet), you can convert that to torque or angular velocity and apply that instead of manipulating the rotation directly.  But I think you already know that.  Anyway, good luck with what you're trying to accomplish.

-------------------------

vivienneanthony | 2018-05-12 23:12:11 UTC | #10

[quote="Lumak, post:9, topic:4228"]
One last thing that I want to mention – knowing the desired quaternion (referring to the **qnewRot** from the snippet), you can convert that to torque or angular velocity and apply that instead of manipulating the rotation directly. But I think you already know that. Anyway, good luck with what you’re trying to accomplish.
[/quote]

Thanks. I'm looking for informatoin on the web that shed some light like https://math.stackexchange.com/questions/39553/how-do-i-apply-an-angular-velocity-vector3-to-a-unit-quaternion-orientation/39651#39651

-------------------------

