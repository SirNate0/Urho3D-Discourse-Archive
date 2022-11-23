rogerdv | 2017-01-02 01:00:55 UTC | #1

I want to create an isometric-like game in 3D, with controls similar to Wasteland 2. My approach with Ogre and Unity was to create a target node, create a child node with the camera, and make it follow parent rotation and translations (Ogre has autotracking, but Unity required to make camera look at the target node when updated). Is thi smethdo valid in Urho3D or do I need a different approach?

-------------------------

cadaver | 2017-01-02 01:00:55 UTC | #2

Urho does not have autotracking, so yes, the approach would be similar to Unity that you would update the camera position/rotation in a per-frame update function.

-------------------------

rogerdv | 2017-01-02 01:00:55 UTC | #3

How can I make the camera look at an specific point? Im searching for a LookAt member in Camera class, but cant find anything similar.

-------------------------

cadaver | 2017-01-02 01:00:55 UTC | #4

LookAt is in Node class. The Camera component always views and renders along its containing Node's local positive Z axis and cannot be transformed independently of it.

-------------------------

rogerdv | 2017-01-02 01:00:56 UTC | #5

Well, I have some mistake here, when I use lookat the movement becomes a mess with the view jumping from one place to another when I press a key. If I remove the lookAt, the target node moves through the scene pulling the camera node smoothly.

This is camera creation code:

[code]_target = new Urho3D::Node(context_);
				_cameraNode = _target->CreateChild("cam");//new Urho3D::Node(context_);

				camera = _cameraNode->CreateComponent<Camera>();
				camera->SetFarClip(300.0f);
				//camera->SetOrthographic(true);

				// Set an initial position for the camera scene node above the floor
				_target->SetPosition(Urho3D::Vector3(-90.0f, 35.0f, -100.0f));
				_cameraNode->SetPosition(Urho3D::Vector3(0.0f, 15.0f, 15.0f));
				_cameraNode->LookAt(_target->GetPosition(), Vector3::UP, TS_LOCAL);[/code]

This is key event code:

[code]if (key == 'D')
        {
					_target->Translate(Vector3(1.0f, 0.0f,0.0f));
					_cameraNode->LookAt(_target->GetPosition(), Vector3::UP, TS_LOCAL);
				}
				else if (key == 'A')
				{
					_target->Translate(Vector3(-1.0f, 0.0f,0.0f));
					_cameraNode->LookAt(_target->GetPosition(), Vector3::UP, TS_LOCAL);
				}
				else if (key == 'W')
				{					
					_target->Translate(Vector3(0.0f, 0.0f,1.0f));
					_cameraNode->LookAt(_target->GetPosition(), Vector3::UP, TS_LOCAL);
				}
				else if (key == 'S')
				{					
					_target->Translate(Vector3(0.0f, 0.0f,-1.0f));
					_cameraNode->LookAt(_target->GetPosition(), Vector3::UP, TS_LOCAL);
				}[/code]

-------------------------

JTippetts | 2017-01-02 01:00:58 UTC | #6

The way I do a third-person camera:

[code]cameranode=scene->CreateChild();
pitchnode=cameranode->CreateChild();
follownode=pitchnode->CreateChild();
camera=follownode->CreateComponent<Camera>();

follownode->SetPosition(Vector3(0,0,-camerafollowdistance));
pitchnode->SetRotation(Quaternion(camerapitch, Vector3(1,0,0));
cameranode->SetRotation(Quaternion(camerayaw, Vector3(0,1,0));
cameranode->SetPosition(cameralookatposition);[/code]

Essentially, I create the camera transform as a hierarchy of nodes. The root-level node controls the position of the point the camera is looking at and the rotation of the camera around the vertical (Y) axis. The child node of the root node controls the camera's pitch, or angle above the horizon. The child of that node holds the camera component and controls the camera's following distance, or distance from the point being looked at, for zooming purposes.

During runtime, to have the camera track an object I simply mirror the tracked object's position into the root level cameranode. This way, I don't have to worry about calling node->LookAt().

-------------------------

rogerdv | 2017-01-02 01:00:59 UTC | #7

I found my mistake and achieved a good looking isometric view, including ortho projection. The problem was in line
[code]_cameraNode->LookAt(_target->GetPosition(), Vector3::UP, TS_LOCAL);[/code]

I was forcing the camera to look at some local point relaive to parent instead of parent's world coordinates, which is the correct way. Also managed to implement scroll and camera rotation using keyboard (will deal with mouse later). 
Still lack zoom in/out, any advice on this?

-------------------------

JTippetts | 2017-01-02 01:01:02 UTC | #8

Since orthographic projections lack perspective, you can't zoom using camera distance or angle of view. Instead, you can implement zoom using Camera::SetOrthoSize(). Larger values to "zoom out", smaller values to "zoom in".

-------------------------

Mike | 2017-01-02 01:01:02 UTC | #9

You can also use Camera::SetZoom() ([url]http://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_camera.html#aef7f8a3cb5229d3fb8636520ffaaf2da[/url]).
You can refer to Urho2D samples for this.

-------------------------

