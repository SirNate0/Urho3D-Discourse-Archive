tni711 | 2018-08-31 07:24:59 UTC | #1

The Quaternion concept is new to me,  I watched some youtube videos but still have hard time to figure out how the concept applied in the CharacterDemo program.

Some basic questions here:

1) What is meaning of this statement? How the pitch and the Vector3::RIGHT value work? 
    Quaternion dir = rot * Quaternion(character_->controls_.pitch_, Vector3::RIGHT);

2) In this case, why uses use GetWorldPosition instead of just GetPosition(). How the value of Vector3 here impact the position of the camera?
    cameraNode_->SetPosition(headNode->GetWorldPosition() + rot * Vector3(0.0f, 0.15f, 0.2f));
    cameraNode_->SetRotation(dir);

Really appreciate any advise or a brief explanation in layman terms of key concepts used in this function.

Source code of the function from the CharacterDemo:
```
void CharacterDemo::HandlePostUpdate(StringHash eventType, VariantMap& eventData)
{
    if (!character_)
        return;

    Node* characterNode = character_->GetNode();

    // Get camera lookat dir from character yaw + pitch
    const Quaternion& rot = characterNode->GetRotation();
    Quaternion dir = rot * Quaternion(character_->controls_.pitch_, Vector3::RIGHT);

    // Turn head to camera pitch, but limit to avoid unnatural animation
    Node* headNode = characterNode->GetChild("Mutant:Head", true);
    float limitPitch = Clamp(character_->controls_.pitch_, -45.0f, 45.0f);
    Quaternion headDir = rot * Quaternion(limitPitch, Vector3(1.0f, 0.0f, 0.0f));
    // This could be expanded to look at an arbitrary target, now just look at a point in front
    Vector3 headWorldTarget = headNode->GetWorldPosition() + headDir * Vector3(0.0f, 0.0f, -1.0f);
    headNode->LookAt(headWorldTarget, Vector3(0.0f, 1.0f, 0.0f));

    if (firstPerson_)
    {
        cameraNode_->SetPosition(headNode->GetWorldPosition() + rot * Vector3(0.0f, 0.15f, 0.2f));
        cameraNode_->SetRotation(dir);
    }
    else
    {
        // Third person camera: position behind the character
        Vector3 aimPoint = characterNode->GetPosition() + rot * Vector3(0.0f, 1.7f, 0.0f);

        // Collide camera ray with static physics objects (layer bitmask 2) to ensure we see the character properly
        Vector3 rayDir = dir * Vector3::BACK;
        float rayDistance = touch_ ? touch_->cameraDistance_ : CAMERA_INITIAL_DIST;
        PhysicsRaycastResult result;
        scene_->GetComponent<PhysicsWorld>()->RaycastSingle(result, Ray(aimPoint, rayDir), rayDistance, 2);
        if (result.body_)
            rayDistance = Min(rayDistance, result.distance_);
        rayDistance = Clamp(rayDistance, CAMERA_MIN_DIST, CAMERA_MAX_DIST);

        cameraNode_->SetPosition(aimPoint + rayDir * rayDistance);
        cameraNode_->SetRotation(dir);
    }
}
```

-------------------------

Dave82 | 2019-03-06 13:38:41 UTC | #2

[quote="tni711, post:1, topic:4507"]
What is meaning of this statement? How the pitch and the Vector3::RIGHT value work?
Quaternion dir = rot * Quaternion(character_-&gt;controls_.pitch_, Vector3::RIGHT);
[/quote]

Well it is hard to explain how quaternions work.When working with quaternions and matrices the * sign doesn't represent multiplication like in most cases (Vectors , real numbers etc) but you can think of it as a "transform" sign. In your example you simply transform Quaternion(character_-&gt;controls_.pitch_, Vector3::RIGHT) by "rot".Or to make it easier to understand : You put the Vector3::RIGHT vector world coordinates in the coordinate system of "rot". The returned quaternion (dir) is a rotation relative to "rot"

[quote="tni711, post:1, topic:4507"]
In this case, why uses use GetWorldPosition instead of just GetPosition(). How the value of Vector3 here impact the position of the camera?
cameraNode_-&gt;SetPosition(headNode-&gt;GetWorldPosition() + rot * Vector3(0.0f, 0.15f, 0.2f));
cameraNode_-&gt;SetRotation(dir);
[/quote]
You must use the GetWorldPosition because the "headNode" is most likely a child of another node (a neck or torso) so getPosition() would return the local coordinates of headNode (relative to neck or torso) This means if the player moves even 10000000 units in a direction the getPosition() would return always the same value (a position realtive to it's parent)

[quote="tni711, post:1, topic:4507"]
How the value of Vector3 here impact the position of the camera?
cameraNode_-&gt;SetPosition(headNode-&gt;GetWorldPosition() + rot * Vector3(0.0f, 0.15f, 0.2f));
[/quote]
The line simply puts the camera in the position of the headNode with some offset (0.15 above and 0.2 behind the player's head thus make the player fit in the camera's viewport).But we can't use the offset  Vector3(0.0f, 0.15f, 0.2f) directly because these are world coordinates. (For an example : what happens if the player is rotated 90 degrees on y axis ? The offset would be invalid since from this point of view x becomes back/forward and z is left/right from the player) We need to transform our vector  by character's rotation.

[b]rot[/b] * Vector3(0.0f, 0.15f, 0.2f)

This makes sure z is always back/forward and x is always left right from the player

-------------------------

Modanung | 2018-08-31 09:01:24 UTC | #3

The identity quaternion (`Quaternion::IDENTITY`) represents no rotation, which is useful for clearing a node's rotation. A `Quaternion` can also be constructed from Euler angles (`float, float, float`) or a single angle and a rotation axis (`float, Vector3`).

-------------------------

tni711 | 2018-08-31 23:35:54 UTC | #4

[quote="Dave82, post:2, topic:4507"]
When working with quaternions and matrices the * sign doesn’t represent multiplication like in most cases (Vectors , real numbers etc) but you can think of it as a “transform” sign. In your example you simply transform Quaternion(character_-&gt;controls_.pitch_, Vector3::RIGHT) by “rot”.Or to make it easier to understand : You put the Vector3::RIGHT vector world coordinates in the coordinate system of “rot”. The returned quaternion (dir) is a rotation relative to “rot”
[/quote]

Thanks for much for the explanation! I think I start to understand this quaternions business. What confused me a bit was a quaternion can store the orientation of a 3D object as well as the change of rotation which can be applied. Also there are different formats to represent a quaternion value.

So is it correct the Quaternion(character_->controls_.pitch_, Vector3::RIGHT) refers to the angle rotation on the x-axis here? I assume the pitch_ is the angle in radian.

The other points about GetWorldPosition vs GetPosition is now crystal clear to me now :slight_smile:

-------------------------

tni711 | 2018-08-31 23:40:46 UTC | #5

[quote="Modanung, post:3, topic:4507"]
The identity quaternion ( `Quaternion::IDENTITY` ) represents no rotation, which is useful for clearing a node’s rotation.
[/quote]

Thanks a lot for the help.
I understand the Eurler and the single angle on a rotation axis representations now.
However, not quite sure how do you use the IDENTIFY quaterion to clear a node's rotation.

Does it means (i am guessing here)

rot2 = rot1 * Quaternion(character_-&gt;controls_.pitch_, Vector3::RIGHT);
rot1 = rot2 * IDENTITY(of rot1)

-------------------------

Modanung | 2018-09-01 07:01:57 UTC | #6

`SetRotation(Quaternion::IDENTITY)` - with a **T** :) - will clear a `Node`'s rotation. Multiplying this `quaternion` by a vector returns the same vector.

-------------------------

tni711 | 2018-09-02 12:43:37 UTC | #7

[quote="Modanung, post:6, topic:4507"]
`SetRotation(Quaternion::IDENTITY)` - with a **T** :slight_smile: - will clear a `Node` 's rotation. Multiplying this `quaternion` by a vector returns the same vector.
[/quote]

Thanks a lot! I think I understand the concept and is ready to use it to fine tune my table tennis game :)

-------------------------

