vivienneanthony | 2017-01-02 01:00:36 UTC | #1

Hello,

I'm trying to figure out how to rotate a camera around a center point looking at it. Do anyone have any ideas or know some links to how?

Also, I need to compute distance like view. like 100%(full person-bounding area) view 150% view. 

Vivienne

-------------------------

gunnar.kriik | 2017-01-02 01:00:37 UTC | #2

Hey,

So you just want to rotate the camera around a target node, if I understand you correctly. Shouldn't be more difficult than this:

[code]
// Class member variable
float cameraYaw = 0.0f;

// Run each frame update
void UpdateCameraRotation(float deltatime, Node* targetNode) {
  cameraYaw += 60.0 * dt;  // Rotate camera N degrees each second
  Quaternion q = Quaternion(cameraYaw, Vector3::UP);   // Construct rotation
  Vector3 cameraOffset(0.0f, -3.0f, 5.0f);  // Camera offset relative to target node 
  Vector3 cameraPosition = targetNode->GetPosition() - (q * cameraOffset);  // New rotated camera position with whatever offset you want

  camera->SetPosition(cameraPosition);  // Set new camera position and lookat values
  camera->LookAt(target->GetPosition());
}
[/code]

[quote]Also, I need to compute distance like view. like 100%(full person-bounding area) view 150% view. [/quote]
I'm not sure I understand this.. Care to elaborate?

-------------------------

vivienneanthony | 2017-01-02 01:00:37 UTC | #3

[quote="gunnar.kriik"]Hey,

So you just want to rotate the camera around a target node, if I understand you correctly. Shouldn't be more difficult than this:

[code]
// Class member variable
float cameraYaw = 0.0f;

// Run each frame update
void UpdateCameraRotation(float deltatime, Node* targetNode) {
  cameraYaw += 60.0 * dt;  // Rotate camera N degrees each second
  Quaternion q = Quaternion(cameraYaw, Vector3::UP);   // Construct rotation
  Vector3 cameraOffset(0.0f, -3.0f, 5.0f);  // Camera offset relative to target node 
  Vector3 cameraPosition = targetNode->GetPosition() - (q * cameraOffset);  // New rotated camera position with whatever offset you want

  camera->SetPosition(cameraPosition);  // Set new camera position and lookat values
  camera->LookAt(target->GetPosition());
}
[/code]

[quote]Also, I need to compute distance like view. like 100%(full person-bounding area) view 150% view. [/quote]
I'm not sure I understand this.. Care to elaborate?[/quote]

I mean this. Being able to zoom out different points of a target for example head, body. If the body, the whole view of the body is shown

[video]https://www.youtube.com/watch?v=yrZFExudO4E[/video]

-------------------------

gwald | 2017-01-02 01:00:37 UTC | #4

Oh that's simple,
You set your camera 'look at' to where you want to look at and you move the camera closer to the obj to zoom in.
Or you can move/rotate the objs (further/closer from the camera) and keep the camera at a fixed location.

-------------------------

vivienneanthony | 2017-01-02 01:00:37 UTC | #5

[quote="gwald"]Oh that's simple,
You set your camera 'look at' to where you want to look at and you move the camera closer to the obj to zoom in.
Or you can move/rotate the objs (further/closer from the camera) and keep the camera at a fixed location.[/quote]

Yea. It is. I just wonder if it's complicated between the target is going change in dimensions.

I haven't posted the video but the player selection works and also when I tell the client to start a scene from the console. It loads the selected player. I wanted to do the characters clothing but got stuck because i would like changeable attachments. I'm not sure if I have to save attachment points per character mesh.

-------------------------

vivienneanthony | 2017-01-02 01:00:40 UTC | #6

[quote="gunnar.kriik"]Hey,

So you just want to rotate the camera around a target node, if I understand you correctly. Shouldn't be more difficult than this:

[code]
// Class member variable
float cameraYaw = 0.0f;

// Run each frame update
void UpdateCameraRotation(float deltatime, Node* targetNode) {
  cameraYaw += 60.0 * dt;  // Rotate camera N degrees each second
  Quaternion q = Quaternion(cameraYaw, Vector3::UP);   // Construct rotation
  Vector3 cameraOffset(0.0f, -3.0f, 5.0f);  // Camera offset relative to target node 
  Vector3 cameraPosition = targetNode->GetPosition() - (q * cameraOffset);  // New rotated camera position with whatever offset you want

  camera->SetPosition(cameraPosition);  // Set new camera position and lookat values
  camera->LookAt(target->GetPosition());
}
[/code]

I just tried this code but kinda lost on it or should i be doing it different.

[code]void ExistenceClient::CameraOrientationRotateMove (float degrees, int movement)
{
    /// get the button that was clicked
    Renderer* renderer = GetSubsystem<Renderer>();
    Graphics* graphics = GetSubsystem<Graphics>();
    UI* ui_ = GetSubsystem<UI>();


    /// The camera will use default settings (1000 far clip distance, 45 degrees FOV, set aspect ratio automatically)
    Node * cameraNode_ = scene_->GetChild("Camera",true);
    Node * playermeshNode_ = scene_->GetChild("playermesh",true);

    /// get position
    Vector3 playermeshPosition=playermeshNode_->GetPosition();
    Vector3 cameraPosition=cameraNode_->GetPosition();

    /// Create a offset
    Vector3  cameraOffset=cameraPosition-playermeshPosition;

    Quaternion q = Quaternion(1,Vector3(0.0f,1.0f,0.0f));   // Construct rotation

    Vector3 cameranewPosition = playermeshPosition- (q * cameraOffset);

    cameraNode_->SetPosition(cameranewPosition);  // Set new camera position and lookat values

    return;
}
[/code]

-------------------------

vivienneanthony | 2017-01-02 01:00:41 UTC | #7

This didn't work. Hmmm.

[code]void ExistenceClient::CameraOrientationRotateMove (float degrees, int movement)
{
    /// get the button that was clicked
    Renderer* renderer = GetSubsystem<Renderer>();
    Graphics* graphics = GetSubsystem<Graphics>();
    UI* ui_ = GetSubsystem<UI>();

    /// The camera will use default settings (1000 far clip distance, 45 degrees FOV, set aspect ratio automatically)
    Node * cameraNode_ = scene_->GetChild("Camera",true);
    Node * playermeshNode_ = scene_->GetChild("playermesh",true);

    /// get position
    Vector3 playermeshPosition=playermeshNode_->GetPosition();

    /// Create a offset
    Quaternion q = Quaternion(1, Vector3::UP);   // Construct rotation
    Vector3 cameraOffset(0.0f, 0.0f, 5.0f);  // Camera offset relative to target node
    Vector3 cameraPosition =  playermeshPosition - (q * cameraOffset);  // New rotated camera position with whatever offset you want

    cameraNode_->SetPosition(cameraPosition);  // Set new camera position and lookat values
    cameraNode_->LookAt(Vector3(0.0f,0.0f,0.0f) );

    return;
}
[/code]

-------------------------

gunnar.kriik | 2017-01-02 01:00:41 UTC | #8

[quote="vivienneanthony"]This didn't work. Hmmm.[/quote]

Looks almost right, but you need to look at the player node position, and define that angle somehow. It depends on what you want - do you want to rotate the camera around the player with the mouse, or do you spin the camera around the player at a given speed? If mouse - do you want to move the camera up-down and left right (yaw and pitch)? The code below will only adjust the yaw angle, if you want pitch too then we can add that. 

[code]
void ExistenceClient::CameraOrientationRotateMove (float degrees, int movement)
{
    /// get the button that was clicked
    Renderer* renderer = GetSubsystem<Renderer>();
    Graphics* graphics = GetSubsystem<Graphics>();
    UI* ui_ = GetSubsystem<UI>();

    /// The camera will use default settings (1000 far clip distance, 45 degrees FOV, set aspect ratio automatically)
    Node * cameraNode_ = scene_->GetChild("Camera",true);
    Node * playermeshNode_ = scene_->GetChild("playermesh",true);

    /// get position
    Vector3 playermeshPosition=playermeshNode_->GetPosition();

    /// Create a offset
    Quaternion q = Quaternion(degrees, Vector3::UP);   // Construct rotation
    Vector3 cameraOffset(0.0f, -3.0f, 5.0f);  // Camera offset relative to target node
    Vector3 cameraPosition =  playermeshPosition - (q * cameraOffset);  // New rotated camera position with whatever offset you want

    cameraNode_->SetPosition(cameraPosition);  // Set new camera position and lookat values
    cameraNode_->LookAt(playermeshPosition);

    return;
}
[/code]

-------------------------

vivienneanthony | 2017-01-02 01:00:41 UTC | #9

[quote="gunnar.kriik"][quote="vivienneanthony"]This didn't work. Hmmm.[/quote]

Looks almost right, but you need to look at the player node position, and define that angle somehow. It depends on what you want - do you want to rotate the camera around the player with the mouse, or do you spin the camera around the player at a given speed? If mouse - do you want to move the camera up-down and left right (yaw and pitch)? The code below will only adjust the yaw angle, if you want pitch too then we can add that. 

[/quote]

I used a different code that's similiar and it seems to work rotating around the origin simulating a yaw rotation. The problem I have now is setting it to roll on the pitch rotation around a origin.  You can see it working 15 or 20 seconds into the video. I just want to add pitch and zoom right now. I am thinking of making a way to change the look at point based on the model being looked at.

Vivienne

[video]https://www.youtube.com/watch?v=YfD1KkhuBJ8&list=UUTObP1VzcIglm7uTgUBQjaw[/video]

[code]/// Rotate a camera around a center point
void ExistenceClient::CameraOrientationRotateMove (float degrees, int movement)
{
    /// get the button that was clicked
    Renderer* renderer = GetSubsystem<Renderer>();
    Graphics* graphics = GetSubsystem<Graphics>();
    UI* ui_ = GetSubsystem<UI>();

    /// The camera will use default settings (1000 far clip distance, 45 degrees FOV, set aspect ratio automatically)
    Node * cameraNode_ = scene_->GetChild("Camera",true);
    Node * playermeshNode_ = scene_->GetChild("playermesh",true);

    /// Get position
    Vector3 playermeshPosition=playermeshNode_->GetWorldPosition();
    Vector3 Offset= playermeshPosition-cameraNode_->GetWorldPosition();

    /// Check to change camera yaw based on origin of the main object
    if(movement == CAMERAORIENTATIONROTATEYAW)
    {
         /// Create a offset
        Quaternion q = Quaternion(0.0f,1.0f*degrees,0.0);   // Construct rotation

        /// Test a offset of x equal 1
        Vector3 cameraOffset(5.0f, 0.0f, 0.0f);  // Camera offset relative to target node
        Vector3 cameraPosition =  playermeshPosition - (q * Offset);  // New rotated camera position with whatever offset you want

        /// Set the camera position
        cameraNode_->SetPosition(cameraPosition);  // Set new camera position and lookat values
    }

    /// Look at orgin
    cameraNode_->LookAt(Vector3(0.0f,1.0f,0.0f) );

    return 1;
}[/code]

-------------------------

thebluefish | 2017-01-02 01:01:32 UTC | #10

Ran across this issue today, and TBH I think the proper solution is to use Node::RotateAround. For example, I have the following node structure:

[*] CameraTarget
[*][*] CameraNode

This is done so that my camera always tracks in relation to an explicit target. This is useful for quickly shuffling around various points-of-interest. Here is an example function that rotates around the target whenever the right mouse button is held down:

[code]
It appears that I copied the wrong code. I will update this on Monday due to holiday weekend.
[/code]

Of course, you can always specify the transform space and coordinates differently depending on what you want to accomplish.

-------------------------

