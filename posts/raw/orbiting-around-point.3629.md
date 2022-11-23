rku | 2017-10-03 14:04:26 UTC | #1

I have a mesh at the `(0, 0, 0)` and camera further away looking At that point. I want to rotate camera around the mesh, however it does not always work as expected. When camera is facing mesh from the front moving mouse up/down on X axis rotates around the mesh as expected:

https://youtu.be/VqUoWhcqpWw

However if i look at mesh from the side then moving mouse up/down on X axis rotates around mesh as if rotation was in mesh local space:

https://youtu.be/wVS4jFtvz7A

This is how i attempt rotation:

```cpp
camera_->GetNode()->RotateAround(Vector3::ZERO, Quaternion(
    input->GetMouseMoveY() * 0.1f * lookSensitivity_,
    input->GetMouseMoveX() * 0.1f * lookSensitivity_, 0
), TS_WORLD);
```

Any idea how i could make it rotate so that moving mouse on X axis would make camera go up/down same way like it works when looking at model from the front?

-------------------------

stark7 | 2017-10-03 14:25:26 UTC | #2

Hey here is something that I started coding just last night for my own purposes, sorry it's in C#:

    class CameraOrbitComponent : Component
        {
            public float _verticalTheta { get; set; } = 0f;
            public float _horizontalTheta { get; set; } = 0f;

            public Node _targetNode { get; set; }

            public Node _cameraNode { get; set; }

            public CameraOrbitComponent()
            {
                ReceiveSceneUpdates = true;
            }

            protected override void OnUpdate(float timeStep)
            {
                Vector3 targetPos = _targetNode.WorldPosition;
                Vector3 heading = targetPos - _cameraNode.WorldPosition;
                float radius = heading.Length;
                
                float moveSpeed = 10.0f;
                if (this.Application.Input.GetKeyDown(Key.A)) _horizontalTheta -= moveSpeed;
                if (this.Application.Input.GetKeyDown(Key.D)) _horizontalTheta += moveSpeed;

                _cameraNode.LookAt(_targetNode.Position, Vector3.Up);
                _cameraNode.Rotation = new Quaternion(_cameraNode.Rotation.PitchAngle, _cameraNode.Rotation.YawAngle, 0f);

                _cameraNode.Position = new Vector3(radius * (float)Math.Cos(_horizontalTheta), _cameraNode.Position.Y, radius * (float)Math.Sin(_horizontalTheta));
            }
        }

-------------------------

Modanung | 2018-09-21 22:02:43 UTC | #3

I use RotateAround for Quatter's camera with pre-multiplied Quaternions:
https://gitlab.com/LucKeyProductions/Quatter/blob/master/quattercam.cpp#L163-L165

-------------------------

stark7 | 2017-10-03 15:08:35 UTC | #4

Your solution is so much better :) - I will be stea.. umm, learn from it thank you very much.

-------------------------

rku | 2017-10-03 16:25:06 UTC | #5

@Modanung that has issue similar to gimbal lock. Besides what exactly is a `rotation`? A delta rotation? Absolute rotation of some kind?

-------------------------

Eugene | 2017-10-03 16:29:35 UTC | #6

[quote="rku, post:5, topic:3629"]
that has issue similar to gimbal lock. Besides what exactly is a rotation? A delta rotation? Absolute rotation of some kind?
[/quote]

I suppose, yaw&pitch angles. And nobody usualy cares about gimbal lock for cameras unless you truly need three degrees of freedom.

-------------------------

rku | 2017-10-03 16:45:45 UTC | #7

I am doing model viewer app. It gets really awkward when trying to look at the head of character if there is gimbal lock.

@Modanung thanks for that snipped, it led to a successful solution:

```cpp
camera_->GetNode()->RotateAround(Vector3::ZERO,
    Quaternion(input->GetMouseMoveX() * lookSensitivity_, camera_->GetNode()->GetUp()) * 
    Quaternion(input->GetMouseMoveY() * lookSensitivity_, camera_->GetNode()->GetRight()),
    TS_WORLD
); 
```

-------------------------

