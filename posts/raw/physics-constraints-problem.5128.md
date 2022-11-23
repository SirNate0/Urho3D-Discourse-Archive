capelenglish | 2019-04-29 14:51:52 UTC | #1

I'm struggling with physics constraints. What I have is a rectangular plate that tips over when a impulse is applied. It pivoits about its local x-axis. I have set this up successfully with the local x defined parallel to the world x. (The plate origin is always at y=0.)
![impulse|560x499](upload://34CRtt7RBq6r6KYtzORh6Nkp6A6.png) 
> ...
> Node* targetNode = node;
> Constraint* pinConstraint = targetNode->CreateComponent<Constraint>();
> pinConstraint->SetConstraintType(CONSTRAINT_HINGE);
> pinConstraint->SetWorldPosition(targetNode->GetWorldPosition());
> pinConstraint->SetAxis(Vector3(Vector3::RIGHT));
> pinConstraint->SetOtherAxis(Vector3(Vector3::RIGHT));
> pinConstraint->SetLowLimit(Vector2(0.0f, 0.0f)); 
> pinConstraint->SetHighLimit(Vector2(90.0f, 0.0f));

My problem comes in when I set the plate up at an arbitrary rotation about the y-axis. What I would like to know is how to determine the OtherAxis when the plate is rotated.
![rotated_plate|386x304](upload://6wrnD2LXjriRodpa1s6yrotGj64.png) 

I have tried all sorts of ways using pinConstraint->SetAxis and pinConstraint->SetPosition, but I'm missing something. I can see the constraint when I turn on debug geometry, but I still can't seem to figure out how to get the OtherAxis aligned with the local axis correctly.

BTW, the plate node's parent is the floor/world located at y=0.

-------------------------

QBkGames | 2019-04-29 23:32:35 UTC | #2

This is a question that is probably best placed on the physics engine, such as Bullet, forum (though from my experience your chances of getting an answer is quite low).

Honestly, after reading the Urho3D documentation, the Bullet docs, the Physx docs, I'm still having trouble understanding what all these parameters for constraints really mean. Either I'm dumb or the physics docs suck, because they are written by physics engine designers for other people who also understand how the physics engine works, so the average dumb guys are out of luck.

I think your best bet is to look at Sample 19, the Vehicle demo, it MIGHT give you more clues on how to set up the constraint.

-------------------------

Leith | 2019-04-30 03:43:37 UTC | #3

For setting up Urho3D constraints, it's usually easiest to use the convenience methods...

See the Constraint docs for: SetBody, SetOtherBody, SetWorldPosition, SetAxis, SetOtherAxis.
<https://urho3d.github.io/documentation/1.4/class_urho3_d_1_1_constraint.html>

Note that Axis describes the orientation of the constraint with respect to each BodySpace.

I believe that Urho Constraint expects Body to represent your rigidbody, and OtherBody in your case will be set to null (means attached to static world)... I think? you should have initialized Axis to "rigidbody.LocalToWorld(Vector3::Right)", and OtherAxis to Vector3::Right.

-------------------------

capelenglish | 2019-04-30 11:36:09 UTC | #4

@Leith, I've studied the Urho3D documentation extensively. I understand that SetAxis is relative to the local node and SetOtherAxis is relative to the parent node. In my case, OtherBody is the static world and I leave it null. As I stated in the OP, this constraint works fine until I rotate the plate in the y direction. I've created the constraints in code and using the editor, but I get the same result either way.

@QBkGames,  examples with constraints are few and far between. I've studied the Vehicle demo code in detail. It doesn't have any upper/lower limits set and I think this is part of my problem. If I remove the limits, the plates just swing around in space unconstrained.

-------------------------

Leith | 2019-05-01 05:35:50 UTC | #5

Another way to think about this: for your OtherBody (world), the direction vector for the axis, is from the head, the origin of rotation, to the tail, when not rotated.
For Body, the direction vector for the axis is from the head, the origin of rotation, to the tail, when rotated.

The axis values should differ if you want to start with a rotated state, the amount they differ is based on the change in orientation from the space that you used to define your object. I'm probably not being very clear. Maybe some coder art would be better - even a bad sketch on the back of a napkin can be enlightening.

-------------------------

capelenglish | 2019-05-01 11:55:32 UTC | #6

@Leith Here is my poor attempt at art using PowerPoint:) In the image below, the plate axis (x',y',z') is aligned with with the world axis (X,Y,Z). I set the body axis to **Vector3::Right** and the OtherBody axis to **Vector3::Right**. The **HighLimit** is 90 and the **LowLimit** is 0. This works fine when I apply an impulse (in the +Z direction) to the plate it rotates about x' as it should.
![Screenshot%20-%205_1_2019%20%2C%207_39_23%20AM|602x500,75%](upload://hO0LbILmkbnqfFnFlq5GR9RWEt3.png) 

My problem comes in when I rotate the plate around the y' axis.
![Screenshot%20-%205_1_2019%20%2C%207_44_58%20AM|578x500](upload://ezKzLhJ25i77Hk7SsYzKcPJ9QM5.png) 

My understanding is that, in the second case, the body Axis is still **Vector3::Right** but the OtherAxis must be relative to the world coordinate system. In other words, it must be rotated about **Y** by the amount of the angle **a**. Using this understanding, I've tried all sorts of ways to get this new axis, but nothing works -- I can't get the plate to pivot.

-------------------------

Leith | 2019-05-02 05:46:35 UTC | #7

I think the confusion stems from a difference in convention, between the way Bullet constraints work, and how Urho's wrapper works.

Under Urho, Axis refers to the rigidbody axis, and OtherAxis is used for the worldspace.
Try setting OtherAxis to Right, but set Axis to "rigidbodyparentnode->LocalToWorld(Right)" - this should give us the right vector, defined in rigidbodyspace, and transformed into worldspace. If this doesn't work I'd be happy to recreate your experiment in my current project and provide a better answer!

-------------------------

capelenglish | 2019-05-02 12:30:54 UTC | #8

@Leith First let me thank you for all your help.  The documentation for constraints says:

> [SetAxis](https://urho3d.github.io/documentation/1.4/class_urho3_d_1_1_constraint.html#a4ed9f415e1d759a99d02463a472033b4) (const [Vector3](https://urho3d.github.io/documentation/1.4/class_urho3_d_1_1_vector3.html) &axis)
Set constraint rotation relative to own body by specifying the axis.

And

> [SetOtherAxis](https://urho3d.github.io/documentation/1.4/class_urho3_d_1_1_constraint.html#a3e1e4103e5778593dccbfc4eafed0119) (const [Vector3](https://urho3d.github.io/documentation/1.4/class_urho3_d_1_1_vector3.html) &axis)
Set constraint rotation relative to the other body by specifying the axis.

As you know, in my case the other body is the world. 
I tried your suggestion with the following:

> pinConstraint->SetWorldPosition(node->GetPosition());
pinConstraint->SetAxis(node->LocalToWorld(Vector3::RIGHT)); 
pinConstraint->SetOtherAxis(Vector3::RIGHT);

But this didn't work either. It seems backwards to me based on the documentation. If you can recreate this scenario where the node is rotated about the y-axis (say 45 degrees) I would really appreciate it.

-------------------------

Leith | 2019-05-02 13:57:00 UTC | #9

Absolutely I can because I use Y axis for steering.
I will try to recreate your test conditions tomorrow, we'll find out what's going on. I like puzzles.

-------------------------

esakylli | 2019-05-06 07:01:08 UTC | #10

To my understanding the axis should reflect the axis you want your rigid body to rotate round.
So if you want to rotate round the y-axis, try to with SetAxis(Vector3.UnitY).

-------------------------

Leith | 2019-05-06 08:37:41 UTC | #11

I haven't had a chance to look into this just yet I'm afraid (recently started a teaching course, time is scarce). I've worked with this exact scenario for a hinged "trapdoor" but it's been a while.
I believe the axis values represent the rotation from constraint space to each body space (could be wrong, might be the inverse).. A clearer way of saying this might be "direction from constraint origin to each body origin".

The general concept for Bullet constraints, is that we have two bodies (yes one can be the static world) - forget about world space for a moment, we have two bodyspaces, and we can define a theoretical third space, common to both bodyspaces, because we can define two transforms to get from the two bodyspaces to the common "constraint space", and their inverses to go back again. We don't need world space, we can work directly with these three connected spaces.

In my understanding, the issue you are reporting is that the constraint system is refusing to move as expected when initialized with non-identity values. To this end, I would recommend you begin by relaxing your constraint limits (from -0/+90), to -90 / +90 degrees, to ensure that the issue is not caused by violation of the constraint due to sign of the angle!

-------------------------

