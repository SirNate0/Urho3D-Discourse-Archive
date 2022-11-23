Dave82 | 2017-03-19 16:31:18 UTC | #1

Hi ! I'm trying to create a flashlight beam effect (A Custom geometry quad always facing the camera)
The problem is i need to rotate this beamNode only on z axis and leave the other axes untouched.
No matter how i tried so far sometimes it works but if i rotate the flashlight in some direction the up axis is changing and i don't know how to calculate it.

This code works if the flashlight has 0,0,0 rotation 
[code]
Vector3 p = camNode.position - beamNode.get_worldPosition();
p.z = 0.0f;
Quaternion q;
q.FromRotationTo(p , Vector3(0,1,0));
beamNode.rotation = q;
// small correction needed :
Vector3 r = beamNode.rotation.get_eulerAngles();
r.z = 360.0f - r.z;
beamNode.rotation = Quaternion(r.x , r.y , r.z);
[/code]
Once i rotate my flashlight in some direction the beamNode rotation is wrong

-------------------------

Lumak | 2017-03-19 17:39:37 UTC | #2

How about:
> p.z = 0.0f;
> p.Normalize();
> beamNode.rotation = Quaternion(Vector3::FORWARD, p);

Wouldn't that work?

-------------------------

Dave82 | 2017-03-19 17:57:51 UTC | #3

> How about:

>     p.z = 0.0f;
>     p.Normalize();
>     beamNode.rotation = Quaternion(Vector3::FORWARD, p);

> Wouldn't that work?

That again works only if my flashlightNode rotation is set to 0,0,0. once i rotate my flashlight (the flashlight is parent of beamNode) the rotation is invalid

-------------------------

Lumak | 2017-03-19 19:34:54 UTC | #4

Then you'll need to work with worldRotation. Pseudo code would look something like:
1) deltaRotation = beamNode.getworldrotation - Quaternion(Vector3::FORWARD, p); // or use Inverse() but the function operator would do the same thing.
2) beamNode.setworldrotation = beamnode.getworldrotation * deltaRotation ();

Edit: I thought more about this, and you might have to substitute flashlightNode in 1) to get the proper orientation.

-------------------------

Dave82 | 2017-03-19 20:43:31 UTC | #5

Still doesn't work...I get back to it tomorrow. I know i could use a billboard set and set face camera mode , but i want extra control per vertex alpha and calculate the beamMesh opacity based on the angle between the camera direction and flashlight direction.If the angle is smaller the beam is more visible and if the angle is bigger the lens flare is more visible 
something like this.

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/c9cacf55677fe9193b72bbb3d09fb96b7cac1ffe.gif'>

-------------------------

Dave82 | 2017-03-20 12:10:59 UTC | #6

Still no luck , any ideas appreciated.

-------------------------

Lumak | 2017-03-20 16:30:52 UTC | #7

Here is something else that you can try.
> Vector3 p = camNode.position - beamNode.get_worldPosition();
> p.z = 0.0f;
> p.Normalize();
> Quaternion q(beamNode.GetWorldDirection(), p); // delta rotation
> beamNode.SetRotation( beamNode.GetRotation() * q); // add delta rot

If that doesn't work, try debugging it using debug lines - visually seeing what's going on may help.

-------------------------

Dave82 | 2017-03-20 18:30:33 UTC | #8

[quote="Lumak, post:7, topic:2929, full:true"]
Here is something else that you can try.
> Vector3 p = camNode.position - beamNode.get_worldPosition();
> p.z = 0.0f;
> p.Normalize();
> Quaternion q(beamNode.GetWorldDirection(), p); // delta rotation
> beamNode.SetRotation( beamNode.GetRotation() * q); // add delta rot

If that doesn't work, try debugging it using debug lines - visually seeing what's going on may help.
[/quote]

This rotates  the beamNode constantly like a fan and changes the direction according to direction between the camera and the node.
Usually i always draw my ideas on a piece of paper first (vectors , points) and when i'm 100% sure what i want to achieve i just do the math for it.This technique worked so far but this is just beyond my knowledge.
I also tried to apply the Z euler rotation only 
 
beamNode.rotation = Quaternion(0,0,angle);

Where i tried to calculate angle different ways and it didn't worked.This rotates the node on local Z in the desired direction but the angle value is always wrong.

-------------------------

Lumak | 2017-03-20 22:02:29 UTC | #9

Created a test case to set the beamNode in the direction that the camera is facing:
https://youtu.be/ofM7Q0-EXHk

Hierarchy:
 -rightHand
--flashlightNode
---beamNode

code:
>     Node *beamNode = characterNode->GetChild("beamnode", true);
>     if (beamNode)
>     {
>         Vector3 camFwd = cameraNode_->GetWorldDirection();
>         Vector3 lgtFwd = beamNode->GetWorldDirection();
>         Quaternion q(lgtFwd, camFwd);
>         beamNode->SetRotation(beamNode->GetRotation() * q);

>     }

I know you're trying to orient the beamNode based on cam pos, but ideally, the above computation would be similar to the one that I provided previously.

-------------------------

Modanung | 2017-03-21 03:05:02 UTC | #10

I think what you're looking for is something like this:
```
node_->LookAt(node_->GetWorldPosition() + node_->GetDirection(),
              node_->GetWorldPosition() - cameraNode->GetWorldPosition());
```

I expected to find a FaceCameraMode for this, but haven't.

To make the beam fade away you could do something like:
```
node_->GetComponent<StaticModel>()->GetMaterial()
    ->SetShaderParameter("MatDiffColor", Color::WHITE * Clamp(0.9f - Abs(
    1.0f - node_->GetDirection().Angle(
    node_->GetWorldPosition() - cameraNode->GetWorldPosition()) / 90.0f),
    0.0f, 1.0f));
```

-------------------------

Dave82 | 2017-03-20 23:57:42 UTC | #11

After a long struggling, i found the solution.The proper way doing it was (like i first thought) rotate only on z euler.The only problem was i didn't take node rotation into account.It goes like this :

[CODE]
Vector3 diff = camNode.get_worldPosition() - beamNode.get_worldPosition();
diff.Normalize();
diff = node.rotation.Inverse() * diff;
float angleZ = Atan2(diff.y , diff.x) + 90;
beamNode.set_rotation(Quaternion(0,0,angleZ));
[/CODE]

What bothers me in this code is that Atan2 should return the  angle in radians and i should convert it to degrees first but it just works without it for some reason (no need for angleZ * M_RADTODEG)... strange.

-------------------------

Dave82 | 2017-03-21 02:19:28 UTC | #12

> "I think what you're looking for is something like this:

> node_->LookAt(node_->GetWorldPosition() + node_->GetDirection(),
>               cameraNode->GetWorldPosition() - node_->GetWorldPosition());"

Yes ,this works too ! Thanks.And it is more elegant than mine version.

-------------------------

Modanung | 2017-03-21 04:57:37 UTC | #13

And then you'll end up with something like this:

https://vimeo.com/209325270

https://vimeo.com/209327362

https://github.com/Modanung/BeamLight

-------------------------

Dave82 | 2017-03-21 16:06:33 UTC | #14

Or something like this 

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/95879483d83dbcfec9c6cdc77d712ccbd836458f.jpg'>

-------------------------

Dave82 | 2017-03-28 08:52:29 UTC | #15

Wow ! This flashlight effect looks really cool ! I made a 3 min video of playing with the flashlight, :) Also the dynamic lights use inverse square attenuation and looks way better than the default ramp texture (thanks to dragonCASTjosh !)
https://github.com/urho3d/Urho3D/issues/1478

Here's the video.
https://www.youtube.com/watch?v=1u2iXyBeUf0

-------------------------

Modanung | 2017-03-28 16:53:00 UTC | #16

That looks really good indeed! :slight_smile:
One thing that would be an improvement is using something like the soft particles technique. A shader that would make the beam fade to fully transparent before it crosses a surface. A blurred cross section of the world geometry as alpha texture seems like a good option to me. But I'm no shader expert.

-------------------------

