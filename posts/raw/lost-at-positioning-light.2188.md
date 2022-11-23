rku | 2017-01-02 01:13:47 UTC | #1

I wonder if you can help me with another related thing. I am not sure why light lights up wrong side of figures.

My game field is at 0,0 - 10,20 (think 2d wall). Everything is at z=0 except for light and camera.
[img]https://i.imgur.com/o2hU1rD.png[/img]

This is how i place camera:
[code]
    auto camera = _scene->GetChild("Camera");
    auto camera_object = camera->GetComponent<Camera>();
    camera_object->SetOrthographic(true);
    camera->SetPosition(Vector3(0, 0, -30));
    camera->LookAt(Vector3::ZERO);
    camera->Translate(Vector3(5, 9.4f, 0));
[/code]
Now camera is in front of middle of game field. So far so good. Now i place the light:

[code]        auto lightNode = _scene->CreateChild();
        lightNode->SetPosition(Vector3(-30, 30, -15));
        auto light = lightNode->CreateComponent<Light>();
        lightNode->LookAt(Vector3::ZERO);
        light->SetLightType(LIGHT_DIRECTIONAL);
        light->SetCastShadows(false);
        light->SetRange(500);
        light->SetFadeDistance(500);[/code]

As i understand light ends up at (-30, 30, -15) which is above/to the left/bit in front of game field. That means figures should have their top-left faces lit.

However:
[img]https://i.imgur.com/mQy3qv0.png[/img]

Placing the light on (30, -30, -15) gives desired result:
[img]https://i.imgur.com/z4rvTht.png[/img]

Faces facing light get darker. What did i mess here up?

-------------------------

cadaver | 2017-01-02 01:13:47 UTC | #2

Normals flipped on the models? Can you test with Urho builtin models like Box.mdl to see if there's a difference?

-------------------------

rku | 2017-01-02 01:13:47 UTC | #3

Thanks man. This was a combination of flipped normals and urho3d-blender being weird. Turns out i also needed to select "Bottom (-Z -Y)" to get mesh exported while properly flipping axis (blender up-z -> urho up-y). Sometimes i wish i could switch coordinate system of engine to blender one. But that probably isnt that simple eh?

-------------------------

