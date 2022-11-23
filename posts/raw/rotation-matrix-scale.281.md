vivienneanthony | 2017-01-02 00:59:22 UTC | #1

Hey

Quick question.

1. What is the normal rotation of objects when created? Just curious because I am messing with the following code to display a mesh logo but I'm not sure what direction is everything. So the camera viewport will show directly in front of the logo?

2. I also noticed .8f. What does that mean? Does it mean feet? Also, the matrix scale from Blender to Urho3D.

3. Is the scale 1 to 1.

How are you?

Vivienne


PS. So far I got the UI to show separately from the 3D render view. So, I'm not sure if  both can be mixed. or do I have to do the render layer first then ui.


[quote]   /// Get Needed SubSystems
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    Renderer* renderer = GetSubsystem<Renderer>();
    Graphics* graphics = GetSubsystem<Graphics>();
    UI* ui = GetSubsystem<UI>();

 // create a new scene
    scene_= new Scene(context_);
    scene_-> CreateComponent<Octree>();

    /// Get rendering window size as floats
    float width = (float)graphics->GetWidth();
    float height = (float)graphics->GetHeight();

    SharedPtr<Sprite> backgroundimage(new Sprite(context_));

    // Get the Urho3D fish texture
    Texture2D* decalTex = cache->GetResource<Texture2D>("Resources/Textures/login.png");
    backgroundimage->SetTexture(decalTex);

    /// The UI root element is as big as the rendering window, set random position within it
    backgroundimage->SetPosition(width/2, height/2);

    /// Set sprite size & hotspot in its center
    backgroundimage->SetSize(width,height);
    backgroundimage->SetHotSpot(width/2, height/2);

    /// Add as a child of the root UI element
    ui->GetRoot()->AddChild(backgroundimage);


    Node* existencelogoNode = scene_->CreateChild("Plane");
    //existencelogoNode ->SetScale(Vector3(1.0f,1.0f,1.0f));
    existencelogoNode ->SetPosition(Vector3(0.0,0.0,0.0));
    existencelogoNode ->SetRotation(Quaternion(180.0,90.0,0.0));
    StaticModel* existencelogoObject = existencelogoNode->CreateComponent<StaticModel>();
    existencelogoObject->SetModel(cache->GetResource<Model>("Resources/Models/existencelogo.mdl"));
    existencelogoObject->SetMaterial(cache->GetResource<Material>("Resources/Materials/existencelogo.xml"));

   // Create a directional light to the world so that we can see something. The light scene node's orientation controls the
    // light direction; we will use the SetDirection() function which calculates the orientation from a forward direction vector.
    // The light will use default settings (white light, no shadows)
    Node* lightNode = scene_->CreateChild("DirectionalLight");
    lightNode->SetDirection(Vector3(0.2, .8, 0.8)); // The direction vector does not need to be normalized
    Light* lightObject = lightNode->CreateComponent<Light>();
    lightObject->SetLightType(LIGHT_DIRECTIONAL);

    // Create a scene node for the camera, which we will move around
    // The camera will use default settings (1000 far clip distance, 45 degrees FOV, set aspect ratio automatically)
    cameraNode_ = scene_->CreateChild("Camera");
    cameraNode_->CreateComponent<Camera>();

    // Set an initial position for the camera scene node above the plane
    cameraNode_->SetPosition(Vector3(2.0,-8.0,0.0));
    cameraNode_->SetRotation(Quaternion(-90.0,0.0,90.0));

    // Set up a viewport to the Renderer subsystem so that the 3D scene can be seen. We need to define the scene and the camera
    // at minimum. Additionally we could configure the viewport screen size and the rendering path (eg. forward / deferred) to
    // use, but now we just use full screen and default render path configured in the engine command line options
    SharedPtr<Viewport> viewport(new Viewport(context_, scene_, cameraNode_->GetComponent<Camera>()));
    renderer->SetViewport(0, viewport);
[/quote]

-------------------------

vivienneanthony | 2017-01-02 00:59:22 UTC | #2

This is a screenshot in Blender of what I'm trying to do.

[img]http://averyanthony.com/priv/direction.jpg[/img]

-------------------------

JTippetts | 2017-01-02 00:59:22 UTC | #3

1) "What is the normal rotation of objects when created?"
  The normal rotation is no rotation. The rotation matrix for the object is identity, meaning there is no rotation applied to the object at all.

2) .8f Denotes the value of 0.8 in float (as opposed to double) precision. It has nothing to do with feet, meters, or anything else.

3) Um, sure? Unless you set a scale of something other than 1. Or do you mean to ask if there is a 1 to 1 correlation between Blender's coordinate space and Urho3Ds? In which case, no there isn't.

Urho3D uses a left-hand coordinate system. If you hold your left hand so that the thumb points up, the index finger points forward, and the middle finger points to the right (each finger perpendicular to the others), then you can label the thumb +Y, the index finger +Z and the middle finger +X. This means that when a camera is set up with default settings and no adjustments to the camera scene node's orientation or position, then the camera points along the +Z axis, +X proceeds to the right across the screen, and +Y proceeds up the screen vertically.  The camera near clip defaults to 0.1 and the far clip is set to 1000.0. The camera's node location is (0,0,0). If the camera node is at Z=0 and an object is at Z=0, the object will be clipped by the near clip plane (since the plane sits at Z=0.1). So in your example, the plane object won't be visible since it is located at Z=0. You only translate the camera in X and Y (cameraNode_->SetPosition(Vector3(-.2f,-.1f,0));) so you still won't be able to see the plane.

If you want to view an object that lies at Z=0, you need to translate the camera along -Z by enough to put the object in between the near and far clip distances. And the plane will only be visible if it is aligned along the X and Y axes; if it is aligned along X and Z or Y and Z then you will be viewing it edge-wise.

Blender uses a right-handed coordinate system, where +X is to the right, +Z is up and +Y is forward. Exporting an object without accounting for this fact can result in orientations that might feel incorrect. For example, if you model in Blender, "up" is +Z, but in Urho3D's default view (no camera transformations) "up" is +Y. Exporters commonly allow swapping +Y and +Z upon export to convert from Blender's right-handed space to left-handed space. Some exporters might perform this step automatically, so if you model your plane explicitly on the X/Y axes in Blender, it might get surreptitiously converted to the X/Z axes upon export.

-------------------------

vivienneanthony | 2017-01-02 00:59:22 UTC | #4

[quote="JTippetts"]1) "What is the normal rotation of objects when created?"
  The normal rotation is no rotation. The rotation matrix for the object is identity, meaning there is no rotation applied to the object at all.

2) .8f Denotes the value of 0.8 in float (as opposed to double) precision. It has nothing to do with feet, meters, or anything else.

3) Um, sure? Unless you set a scale of something other than 1. Or do you mean to ask if there is a 1 to 1 correlation between Blender's coordinate space and Urho3Ds? In which case, no there isn't.

Urho3D uses a left-hand coordinate system. If you hold your left hand so that the thumb points up, the index finger points forward, and the middle finger points to the right (each finger perpendicular to the others), then you can label the thumb +Y, the index finger +Z and the middle finger +X. This means that when a camera is set up with default settings and no adjustments to the camera scene node's orientation or position, then the camera points along the +Z axis, +X proceeds to the right across the screen, and +Y proceeds up the screen vertically.  The camera near clip defaults to 0.1 and the far clip is set to 1000.0. The camera's node location is (0,0,0). If the camera node is at Z=0 and an object is at Z=0, the object will be clipped by the near clip plane (since the plane sits at Z=0.1). So in your example, the plane object won't be visible since it is located at Z=0. You only translate the camera in X and Y (cameraNode_->SetPosition(Vector3(-.2f,-.1f,0));) so you still won't be able to see the plane.

If you want to view an object that lies at Z=0, you need to translate the camera along -Z by enough to put the object in between the near and far clip distances. And the plane will only be visible if it is aligned along the X and Y axes; if it is aligned along X and Z or Y and Z then you will be viewing it edge-wise.

Blender uses a right-handed coordinate system, where +X is to the right, +Z is up and +Y is forward. Exporting an object without accounting for this fact can result in orientations that might feel incorrect. For example, if you model in Blender, "up" is +Z, but in Urho3D's default view (no camera transformations) "up" is +Y. Exporters commonly allow swapping +Y and +Z upon export to convert from Blender's right-handed space to left-handed space. Some exporters might perform this step automatically, so if you model your plane explicitly on the X/Y axes in Blender, it might get surreptitiously converted to the X/Z axes upon export.[/quote]

Okay. I will reread and soak that information maybe play with a sphere in real life to grasp it better.

-------------------------

vivienneanthony | 2017-01-02 00:59:22 UTC | #5

The other issue can the 3D interface and UI be mixed like the Editor.

Here is two images. So, the code semi works and I have to play with orientations some more. I'm not certain how to make the background sprite not disappear with the additional staticmodel node in the renderer viewport.

[img]http://averyanthony.com/priv/directions3.jpg[/img]
[img]http://averyanthony.com/priv/directions2.jpg[/img]

-------------------------

vivienneanthony | 2017-01-02 00:59:22 UTC | #6

I am thinking of doing a plane for the texture instead of the UI.

-------------------------

vivienneanthony | 2017-01-02 00:59:23 UTC | #7

I got the main screen to load with a dialog box. I'm trying to figure out how to make display everything for the loginscreen then display a login dialog box int it then once closed a progress status dialog box is displayed.

From what I understand from the engine it's event driven. So would I have to create a function that creates the login dialog boxes. Assign a event handle to it then start it.
Then a second function for the progress load bar with another event handle for that.

If that's the case, I do I tell Urho3D to go from loginscreen -> handle -> progress screen -> handle.


[img]http://averyanthony.com/priv/direction4.jpg[/img]

-------------------------

