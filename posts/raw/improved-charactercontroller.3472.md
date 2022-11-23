1vanK | 2017-08-21 16:53:22 UTC | #1

Currently character slightly sliding when stay on non-horizontal surface

https://www.youtube.com/watch?v=sxDfXvaCiM8

Small fix for it (18_CharacterDemo.as)
```
void FixedUpdate(float timeStep)
{
    ...

        if (softGrounded &&
            okToJump && moveDir == Vector3::ZERO) // if user pressed no keys (space and arrows)
        {
            body.useGravity = false;
        
            // Stop bouncing from ground when gravity disabled.
            Vector3 fixedSpeed = body.linearVelocity;
            fixedSpeed.y = 0.0f;           
            body.linearVelocity = fixedSpeed;
        }
        else
        {
            body.useGravity = true;
        }

        // Reset grounded flag for next frame
        onGround = false;
    }
}
```

I do not send PR becose I'm not sure this is completely correct. Also still problem with flying character when he run up or down on slope. May be need entirely different approach like https://stackoverflow.com/questions/25605659/avoid-ground-collision-with-bullet/25725502#25725502

-------------------------

