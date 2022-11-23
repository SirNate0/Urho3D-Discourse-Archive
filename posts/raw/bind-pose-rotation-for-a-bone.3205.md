slapin | 2017-06-04 05:35:23 UTC | #1

Hi, all!

How can I know the initial rotation of the bone.

The full story is that my bone is not Z-front, so I need to find-out initial pose to fixup the rotation.
Urho assumes everything is Z-front, and if not, almost no positioning works.

If I manually fixup things, they work as intended, but I need automatic solution, i.e. I need to know
initial (bind) pose.

I guessed it was Bone *bone->initialRotation_, but it is IDENTITY in my case. However I have to fixup
bone to 180 degrees. Where should I look for initial rotation value?

Thanks!

-------------------------

George1 | 2017-06-04 06:55:19 UTC | #2

I think all engines have this issue.
That is why you use ik on your bones. Lookat function is a rigid body with a single link. So it is easy to do.

Another way of doing this is manually create a coordinate frame, attach this frame to a joint. The frame will be your input. Then in your calculation of orientation, include this frame. This way rotation is applied based on this coordinate frame orientation.

-------------------------

slapin | 2017-06-04 06:58:54 UTC | #3

well, IK still gets to rotating bones. What is difference? The initial rotation is still needed for IK,
I think. Or I'm wrong here? Please provide more detail, I'm new to the subject.

-------------------------

slapin | 2017-06-04 07:01:54 UTC | #4

In general from 2-joint IK I get 2 absolute rotations, so I need to apply them somehow, ahnd I wonder how to do this without knowing initial position?

-------------------------

slapin | 2017-06-04 07:04:16 UTC | #5

as the actual rotation does not make sense without initial bind rotation, so IK should have knowledge of
this initial rotation to proceed, if I understand correctly.

-------------------------

George1 | 2017-06-04 07:40:09 UTC | #6

IK with iterative algorithm e.g. Jacobian, CCD or the one implemented in Urho.  Adjusted position or joint angles using direction to destination. E.g. adjust position or angle interatively until reach destination. So there is no need to identify the facing direction of child bone.


For simple bones like, head bone lookat. Make sure that your character facing Z after import. Once we know the facing or forward direction is. Just use cross product to find rotation axis and find rotation angle then add those to quarterion.
 Or directly initialise a quaternion with 2 directions (from, to). 

Final bone orientation is headParentInverse*HeadCurrentRotation*DeltaOrientation    <--- Depends on left or right handed, this order of multiplication will be different.

-------------------------

George1 | 2017-06-04 07:42:41 UTC | #7

Position is needed. You don't need its facing direction. Because parent inverse already tells you orientation.

-------------------------

George1 | 2017-06-04 07:46:51 UTC | #8

Iterative IK is relative. So it would need current orientation to compute the relative delta orientation to the final orientation.

-------------------------

slapin | 2017-06-04 07:49:24 UTC | #9

Well, the character is facing Z, but not all bones do that.

-------------------------

slapin | 2017-06-04 07:53:26 UTC | #10

The problem is that without knowledge of initial rotation we don't know where to rotate that bone to have proper direction. As everything will lie to us in Urho. Some kind of fixup logic is needed, but I can't find the required information.

@cadaver do you know if initial rotation information is available anywhere?

-------------------------

George1 | 2017-06-04 08:01:17 UTC | #11

What you mean initial orientation?

You have the current orientation. The parent inverse.
So new orientation is parentInverse*currentOrientation*deltaOrientation.

-------------------------

slapin | 2017-06-04 08:06:22 UTC | #12

The orientation (GetWorldRotation() from bone node) will be relative to initial bone position.
If bone is not Z-front, (y-front in Blender world) it will face wrong direction. So you don't have enough information
to rotate bone properly without knowing what zero rotation is. In my case, due to model topology, head bone is slightly bent, not vertical, and also faces -Y, not +Y. As I don't know how to get this information in Urho, it is not possible for me to do proper rotation, actually, for any bone.

-------------------------

George1 | 2017-06-04 15:53:11 UTC | #13

Example of turning head in 4 lines.
Vector3 dir1 = man->GetWorldDirection(); //This is the current direction of the man. After you rotated him.
Vector3 dir2 = box->GetWorldPosition() - head->GetWorldPosition();  //Direction of object of interest from head to target.
Quaternion delta (dir1.Normalized(), dir2.Normalized());

	head->SetRotation(Quaternion());
head->SetRotation(head->GetParent()->GetWorldRotation().Inverse()* delta* head->GetWorldRotation());

or just use.
           head->SetWorldRotation(delta*head->GetWorldRotation());

You have to take care of angle at after some degree (maybe close to 180). I'm not sure why here, maybe Quarternion or direction vector has a bug.

-------------------------

George1 | 2017-06-04 15:57:21 UTC | #14

There are also example from other members in the forum if you look for it.

-------------------------

slapin | 2017-06-04 20:50:48 UTC | #15

Ah, thanks, I think what hits me is 180-degree bug.  As it works fine with almost-same-direction initially,
then starts snapping. But I probably can limit look-at angle to 100 degrees...
But I wonder, I want to rotate chest so that it is in middle from head rotation and the rest of body - how to do this with this example?

-------------------------

slapin | 2017-06-04 20:57:44 UTC | #16

ah, I see Quaternion (dir1, dir2) where dir1 and dir2 are on the same line is ambiguous, so that is natural order.
Can be checked by dot product.

-------------------------

slapin | 2017-06-04 21:27:07 UTC | #17

[quote="George1, post:13, topic:3205"]
head-&gt;SetRotation(head-&gt;GetParent()-&gt;GetWorldRotation().Inverse()* delta* head-&gt;GetWorldRotation());
[/quote]

Well, it constantly rotates in this case, without stopping, so something is wrong in code...

-------------------------

slapin | 2017-06-05 03:59:28 UTC | #18

Well, I give up.
Looks like it is not possible after all.

The rotation actually do not make sense in bone world without knowing what it means.
The Quaternion applied to bone rotation could lead to any random rotation which only depends on skeleton.
Without hardcoding of fixup from world space into bone space there is no sense trying to convert Quaternions.
they will never ever work. This is fundamental issue with skeletons in Urho and not possible to fix.

There are only 2 workarounds - make all bones Z-forward (not possible for me), or create fixup Quaternion for each bone and apply it to fix rotation issue. It looks like I have to go 2nd way.

-------------------------

George1 | 2017-06-05 00:57:07 UTC | #19

You have to disable and enable when you need that lookat. Otherwise it would track the object all the time. You have to manage that in your code, I can't help you with that.

The method/procedure provided should work in any engine including this. You might need to look deeper to why it doesn't work at your end.

If you need the second method, do as I suggested in the first post.

Goodluck

-------------------------

slapin | 2017-06-05 02:59:28 UTC | #20

Thanks for your time. 

I don't think it is possible to get productive with state Urho is now,
so I will get to different things, hoping that after some time the solution will arise.

I currently don't see any possible way to implement looking like this.
I did temporary solution using animation. Will wait until something good appears on horizon.

Thank you for your time and effort.

-------------------------

slapin | 2017-06-05 03:59:28 UTC | #21

Yes, made it work using animations.

I implemented 3 additive animations for head bone, for neck bone, for chest bone.
Then I rotate each one according to look direction. I probably cod do with just one, but I want to have control.
I layer them on top of each other. Works with minimum effort, and got a hour to implement.

Urho does have a long, very long road to implement such things from code, but still I got away this time.

/me congratulates himself

-------------------------

