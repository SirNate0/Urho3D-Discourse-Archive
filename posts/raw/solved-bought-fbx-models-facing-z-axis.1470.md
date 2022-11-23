Lumak | 2017-01-02 01:07:59 UTC | #1

Bought .fbx models are facing in the -z axis, so when the char model is running it's facing the camera but moves away from the camera (runs backwards).

Any way to fix this in code?

-------------------------

Lumak | 2017-01-02 01:07:59 UTC | #2

Now that I think about it, I think all I need to do is just flip the camera around and have it move in -z direction for forward movement.

-------------------------

cadaver | 2017-01-02 01:07:59 UTC | #3

Another way is to create additional adjustment node for the model to correct the orientation. This reminds of Unity where it historically imports FBX facing into the wrong axis and corrects this by setting a rotation in the gameobject.

-------------------------

Lumak | 2017-01-02 01:07:59 UTC | #4

You're right about these models being prepared for Unity.  Even though I didn't buy it from Unity Store, it came with Unitypackage, along with model/anim fbx files that I'm using. 

Trying the alternative method of adding an adjustment node works:
[code]
    Node* objectNode = scene_->CreateChild("Jack");
    objectNode->SetPosition(Vector3(0.0f, 1.0f, 0.0f));

    // adjustment node
    Node* adjustNode = objectNode->CreateChild("AdjNode");
    Quaternion qAdjRot(180, Vector3(0,1,0) ); // rotate it by 180 deg.
    adjustNode->SetRotation( qAdjRot );

    // Create the rendering component + animation controller
    AnimatedModel* object = adjustNode->CreateComponent<AnimatedModel>();

[/code]

However, it can't seem to transition from one animation to the next.  It's as if both "run" and "idle" animation are running at the same time.  I'll need to figure out what's going on there.

-------------------------

