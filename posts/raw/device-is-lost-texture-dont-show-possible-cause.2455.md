vivienneanthony | 2017-01-02 01:15:31 UTC | #1

Hi, 

Do anyone have a idea what would cause a mesh to disappear? I can't figure out if it's the camera or mesh itself. Everything seems normal but as soon as it hits a point  it vanishes. I have no zone setup either.


It seems the device is lost, affecting the vertex buffer. I will have details later.

[video]https://youtu.be/Do0pOChpZm4[/video]

Direct Link
[youtu.be/Do0pOChpZm4](https://youtu.be/Do0pOChpZm4)

The code I'm using  is
[code]
   // If camera exist
    if (m_pCamera)
    {
        // Updaw character yaw and povement
        Quaternion Rot(1.0f, 0.0f, 0.0f, 0.0f);

        // Get mouse position
        IntVector2 MousePosition = m_pInput->GetMousePosition();

        // Calculate look based on screen view
        float mWindowBasePitched = (float)(MousePosition.x_ - (g_pApp->GetGraphics()->GetWidth() / 2));
        float mWindowBaseYaw = (float)(MousePosition.y_ - (g_pApp->GetGraphics()->GetHeight() / 2));

        float newPitch = Clamp((float)mWindowBasePitched, -90.0f, 90.0f);
        float newYaw = Clamp((float)mWindowBaseYaw, -90.0f, 90.0f);

        // If key is hard reseet
        if(m_pInput->GetKeyDown(KEY_LALT) || m_pInput->GetKeyDown(KEY_RALT))
        {
            newPitch = 0;
            newYaw = 0;
        }

        // Create a new quaternion
        Quaternion CameraClamped(newYaw, newPitch, 0.0f);

        Node * pViewCameraNode = m_pCamera->GetNode();

        Quaternion RootRot = pViewCameraNode->GetRotation();

        // Rotate Camera
        if (m_pInput->GetKeyDown(KEY_LCTRL) || m_pInput->GetKeyDown(KEY_RCTRL))
    {
        if (pViewCameraNode)
            {
                // Removed line to figure out better rotation
                // Quaternion NewRot = RootRot.Slerp(Rot*CameraClamped, timeStep*.99);
                Quaternion NewRot =  Rot*CameraClamped;

                pViewCameraNode->SetRotation(NewRot);
            }
        }
    }[/code]

Vivienne

-------------------------

Dave82 | 2017-01-02 01:15:31 UTC | #2

It could be a BoundingBox wrong culling issue.Does the same thing happens if you set 
[code]yourAnimatedModel->SetUpdateInvisible(true);[/code]

-------------------------

vivienneanthony | 2017-01-02 01:15:31 UTC | #3

[quote="Dave82"]It could be a BoundingBox wrong culling issue.Does the same thing happens if you set 
[code]yourAnimatedModel->SetUpdateInvisible(true);[/code][/quote]

It's not the problem. I tried that function and it become invisible then I tried it with false, same problem.

Just in case I tried a static model, and it's the same problem.

-------------------------

vivienneanthony | 2017-01-02 02:10:44 UTC | #4

[quote="Dave82"]It could be a BoundingBox wrong culling issue.Does the same thing happens if you set 
[code]yourAnimatedModel->SetUpdateInvisible(true);[/code][/quote]



[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/ef12ac3dd7c71cd1a6c054fa2ceee49fa071489e.png[/img]

[imgur.com/a/oHfpE](http://imgur.com/a/oHfpE)

You can see the bounding areas here.

-------------------------

vivienneanthony | 2017-01-02 01:15:38 UTC | #5

Hey All,

I tried isolating the problem. I am noticing the graphics system saying device id lost. Affecting the vertex buffer.

All help is appreciated, the mesh and colliding box is correct including physics.  What could cause device lost on linux builx ising opengl. I added the pbr code just before it was merged 1.5. So i am not sure if its code on my end, urho3d, shader.

Vivienne

-------------------------

