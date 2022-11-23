Jimmy781 | 2017-01-06 21:34:48 UTC | #1

Hey Guys , 

I'm fairly new to urho and i'm not really sure how the light works .

I'm using this : 

                LightNode = scene.CreateChild("DirectionalLight");
                LightNode.SetDirection(new Vector3(0.6f, -1.0f, 0.8f));
                light = LightNode.CreateComponent<Light>();
                light.LightType = LightType.Directional;

I have a plane -

`PlaneNode.Scale = new Vector3(100.0f, 0.0f, 100.0f);`

Which i populate with items


My camera is either at the center of the plane (0,0,0) moving right-left or viewing the plane from a top view (0,50,0) rotated downwards.

------

There are too many shadows and items far away appear black . I would like to keep everything lighted up all the time regardless of my camera position.

i tried playing with the light.intensity but it was making things white completely.

-------------------------

1vanK | 2017-01-06 21:53:25 UTC | #2

use Zone for ambient lighting

-------------------------

Jimmy781 | 2017-01-07 03:35:15 UTC | #3

@1vanK - do you have an example ?

I'm not really sure how to add more light

-------------------------

George1 | 2017-01-07 04:28:55 UTC | #4

// Create a Zone component for ambient lighting & fog control
	Node* zoneNode = scene_->CreateChild("Zone");
	Zone* zone = zoneNode->CreateComponent<Zone>();
	zone->SetBoundingBox(BoundingBox(-10000.0f, 10000.0f));
	zone->SetAmbientColor(Color(0.5f, 0.5f, 0.5f));

	zone->SetFogColor(Color(0.4f, 0.5f, 0.8f));
	zone->SetFogStart(5000.0f);
	zone->SetFogEnd(30000.0f);


//Put large distance for bounding box and the fog thing.

-------------------------

