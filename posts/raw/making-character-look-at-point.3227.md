slapin | 2017-06-08 18:12:35 UTC | #1

Hi, all!

Still fighting this for a long time now, but got zero success.

I want my character to turn his head, neck, chest and eyes to the point in 3D space.
This character can have any pose at that time and play animation.
Lets consider poses where head is relatively vertical (more vertical than horizontal, or can be made so
without much effects).

So I need:
1. turn head to vertical position
2. and then turn in direction of target.
3. turn chest half-way
4. turn neck half-way

Problems:
1. Rotations are relative and accumulative, each one creates its new coordinate system.
When quaternion multiplication is done, it is done in order from left to right,
so if full transform of head is q1 * q2 * q3 *q4 , only q1 rotates in global space, all the rest
rotate in previous quaternion space. With lots of them it becomes very hard to track target rotation.
Also the transform is non-commutative, which means order is important. So if I want to convert my rotation from global space to local space, I will need to multiply it by inverse rotations in reversed order.
2. To rotate something in global space I will add my rotation at beginning of sequence, it will rotate the whole thing globally. so if q is current rotation of head and qdelta is additional rotation I need to apply, I just do qdelta * q
to get q rotated in global space. But general target is usually a bit different - we need to do local rotation
so that it comply to global goals. So we need to calculate local delta for each rotating bone, and that is where
biggest problem comes.
Initially we have some animation running, with head facing front. We have some global point in space, to which we want to look. We have some global node master which represents global character trasform in space.
Each bone contributes to that transform using its own quaternion each, having head as final.
So having our initial delta rotation, we somehow need to convert it to local rotation of head bone.
The simple approach of multiplying by parent's world transform doesn't work. That is where I stopped.
Tricks like Rotate(x, TS_WORLD) do not help either, so I think the problem is deeper.

This kind of look-at "IK" works quite well in other engines, like Unity, UE4, Godot. But not in Urho.
Probably there is some technical detail about quaternions in Urho, which make it different,
so I'd like to know them. Please note that I look for generic solution, not something which assumes vertical position
or Z-facing. I assume work in any random initial pose (which makes sense for look-at). In my case I think the problem
is solved when character can look-at from head-on pose in addition to standing and sitting.
The challenge looks quite tough.

-------------------------

George1 | 2017-06-09 00:21:15 UTC | #2

[quote="slapin, post:1, topic:3227"]
lots of them it becomes v
[/quote]

Your question is too long. Don't know if anyone will read it.
You don't criticize an engine when you don't know how to use it. These stuff takes time and need patience. Learning takes time.
If you understand the theory correctly, then all engines are the same, including this.

You problem is about inverse kinematic and are dealing with a chain of maybe 3 bones. By the way, why would a person rotate his spine when looking somewhere? This is unnatural pose. We don't do this in practice. Unless in extreme combat condition.

Here's the simplest solution for you.
Just attach another node to the head. Then translate in z a little. 
Then use inverse kinematic code from Urho.

-------------------------

slapin | 2017-06-09 01:50:50 UTC | #3

I don't know why you say so strange things when we look at something we use whole body.

https://www.youtube.com/watch?v=jzDCvlWvhfY

Inverse kinematics in Urho is not yet ready to be used yet. That is why I invent my own wheel.

As for criticizing - I think I have full right to, also, I did not criticize it in this thread at all, just said Urho is different
from other engines regarding this, as  parent 's world transform inverse do not produce local coordinate space.

I know about long questions and tl;dr;, I'm just going to continue speculation about  transformations here in this thread.
The conditions and requirements are quite long.
My current head pose is almost default, i.e. facing -Z. but up -s +Y. This looks like this particular heading
is really a key to my problems, as it looks like the rotation have problems exclusively for head, (and neck as it have the same orientation). Chest doesn't have this problem as it is Z-front and rotate properly.

-------------------------

slapin | 2017-06-09 01:52:00 UTC | #4

I'd say it is first engine I see which is so much depends on everything being Z-front.

-------------------------

TheSHEEEP | 2017-06-09 04:40:51 UTC | #5

It is absolute standard for any engine I've ever worked with that all objects (especially animated ones) have the same facing or problems will ensue. And it is quite logical, since otherwise you'd have to manually rotate everything before usage - not even speaking of more complicated things like IK.

Besides, I just find it a good standard to export every asset facing the same way. More professional than just have things with a random facing ;)

-------------------------

slapin | 2017-06-09 04:52:31 UTC | #6

No, that is not.

1. in Start() I check head facing - if I do GetWorldDirection() it faces Vector3::FORWARD.
No animation is played, everything is default.
All quaternions are identity (1 0 0 0)

2. In HandleSceneDrawableUpdateFinished
Sitting animation is played.
I added debug geometry and see that head is facing back.
Rotating options do not work correctly.
If compensated by quat.FromRotationTo(Vector3(0, 0, 1), Vector3(0, 0, -1));
look start to work.

There is no such behavior in Unity, and UE4 with the same assets. Look works straightforward.

So you tell me complete bullshit without any digging into the problem. Please stop doing that.
Unless you see where the problem might be, from now on I will consider such posts direct aggression
and reserve all right to react in any way I wish.
You did not even care to read my previous posts, you did not care at all to understand the nature of problem
and after that you tell me I did everything wrong. I really hope your karma will hit you in very bad way.

-------------------------

slapin | 2017-06-09 05:03:10 UTC | #7

The engine behavior is inconsistent and unpredictable, so there is no way to manually compensate
bone rotation without hardcoding values. I can't do all animation retargeting and all bone changes to face Z
as that would be enormous waste of time. I try to compensate from code. And that doesn't really work,
while all information should be available to compensate either automatically or from application code.
Looks like everything is fine unless animation is played, which turns nodes in weird ways. But I wonder why
the actual node weird rotations do not affect model? why node world space suddenly change?

-------------------------

slapin | 2017-06-09 06:08:15 UTC | #8

it looks like changing bones sometimes lead to mess when animation is played.
Anyway I found universal solution to fix this for general skeleton case.

1. Requirements - character faces Z, skeleton is irrelevant, bone facing is irrelevant.

2. Creating child note for head, but setting world position to node_->GetWorldPosition() + node_->GetWorldDirection() * 10.0f;

    Node *head_facing = head->CheateChild("facing_dir");
    head_facing->SetWorldPosition(node_->GetWorldPosition()
            + node_->GetWorldDirection() * 10.0f);

3. calculate 2 directions - facing and look
    Vector3 facing_dir = head_facing->GetWorldPosition() - head->GetWorldPosition().Normalized();
    Vector3 target_dir = head->GetWorldPosition() - head->GetWorldPosition().Normalized();

4. Calculate rotational difference
    Quaternion quat;
    quat.FromRotationTo(facing_dir, target_dir);

5. Rotate to difference:
   ``` head->Rotate(quat, TS_WORLD);```

This can't be considered a full solution, as it is mere workaround for a bug.
But it might be useful to somebody.

-------------------------

TheSHEEEP | 2017-06-09 08:20:03 UTC | #9

[quote="slapin, post:6, topic:3227, full:true"]There is no such behavior in Unity, and UE4 with the same assets. Look works straightforward.[/quote]
So, you mean in Unity and UE4, you can just import any asset, no matter how it's facing was done when exported (positive/negative Z, or even positive/negative Y), attach it to any amount of bones and yet they all magically work, facing the same/correct direction without needing any kind of manual adjustment?

Quite honestly, I just don't believe that. Meshes are just 3D vector positions, even the idea of "forward" is foreign to them (if not some kind of new format came up that explicitly stores a "this is forward" information with the mesh). An engine has no way of knowing what "forward" means for any 3D asset. It just has a default assumption (which differs for each engine, though most go with forward or negative Z).

Or are you talking about something completely different?

[quote="slapin, post:6, topic:3227, full:true"]So you tell me complete bullshit without any digging into the problem. Please stop doing that.[/quote]
If you regard a golden rule in 3D development since.. well.. forever... as complete bullshit, just go ahead and see where it takes you ;)

[quote="slapin, post:6, topic:3227, full:true"]Unless you see where the problem might be, from now on I will consider such posts direct aggression
and reserve all right to react in any way I wish.
You did not even care to read my previous posts, you did not care at all to understand the nature of problem
and after that you tell me I did everything wrong. [/quote]
Oh, I did read this thread, but it is hard to tell what exactly is your question or problem. From what I got, everything just points to the same thing: Something does not face the direction you expect it to after a number of manipulations. There can only be three reasons for this:
1. You got your math wrong - since I didn't get what exactly you are even trying to do, I did not comment on this.
2. If your math is right, your assets are wrong. If your assets face different directions, the situation is requiring a fix of the assets or a fix in code (which I think you ended up doing?). From what you said, it doesn't sound like all assets you are using use the same direction of "forward". From experience, this can easily explain your problems.
3. There's actually a bug in Urho. Perfectly possible, of course, but wouldn't that have been noticed already, in such an important system as animation?


[quote="slapin, post:6, topic:3227, full:true"]I really hope your karma will hit you in very bad way.[/quote]
If that happens, I will just hit it right back. With a sledge hammer ;)
Nobody is allowed to hit me in very bad ways, especially not cosmic forces!

-------------------------

johnnycable | 2017-06-09 10:30:18 UTC | #10

To test your code, you could use a trick: switch your asset for something you know for sure it works. You could use the jack or ninja that comes with the examples... 
If your code doesn't work with them, you can be reasonably sure the flaw is in your math.
Contrariwise, if they work, you can be reasonably sure the flaw is in your model.
This left with an option out: the flaw is in the engine. Perfectly possible. But that need you to share a replicable procedure for someone else to test...

-------------------------

Eugene | 2017-06-09 11:58:49 UTC | #11

(offtop)

[quote="slapin, post:7, topic:3227"]
The engine behavior is inconsistent and unpredictable
[/quote]

I can start a list of 'inconsistent and unpredictable' things in the Urho that finally ended up as misuse or misunderstood

1. Degenerate trimeshes cause assert in physics
2. Quaternion math is surprising
3. (this topic subject, TL;DR)
4. (reserved for the future)

-------------------------

slapin | 2017-06-09 12:45:05 UTC | #12

Thank you for your humor, I was feeling bad about being too harsh.

Yes, I speak about different thing. My assets are in general Z-facing (front facing) when exported,
but some bones are not, and that seems normal for other engines.

I have no problem manually rotating bones in any other engines, with animation or not.

I have really have trouble isolating this, as I'm pretty sure there is bug somewhere, but I can't
really find where, otherwise I would just report it to a bug tracker.

I'm really open for discussion of what I'm doing wrong, but that should be quite specific thing,
not speculation.
I do bone rotations in same place IK does them (as my code is kind of IK). I calculate delta difference
between target and current bone rotation and apply that difference to a bone. That is simple.
The proble mis that bone looks at completely wrong place. Research shows that somehow bone facing direction
changes during course of action, as in Start() function the bone is Z-facing, at the event handler the bone becomes
anti-z facing. I calculate this using  quat.FromRotationTo(Vector3(0, 0, 1), node_->GetWorldRotation() * head->GetWorldDirection()); in 2 places. At Start() I get identity quat, at second place I get inverted quat.
So this looks actually like a bug, but I don't know where it lives.
The positioning of node does not change, the only difference is if animation is playing or not, visually head is facing the same spot.

if I change my IK code to use relative-only positioning (like in one of previous posts) everything works like a charm.
That is full story up to current moment. The rush is now lowered, as I can now have look implemented, but I need to
add child node to each involved bone to indicate front side, in this case everything works great. I don't like it but
I could not find better way yet.

-------------------------

slapin | 2017-06-09 12:54:22 UTC | #13

1. A bullet bug. The PR is in queue.
2. Not the math, but some engine approach to it.
3.
4.

Why do you even bother writing?
If you feel sad that I do not respect people's work, don't be.
If you consider software as being sacred that nobody can speak ill of,
I think you should not be in industry. And yes I do respect work of
others and expect the same of mine. And know that errare humanum est,
so I should never trust software neither mine nor someone else's.
And there are bugs. Everywhere. Lurking.
So if you are not helping, please don't bother to interfere at all,
I'm sure you can find much better and interesting things to do
than frustrating me. If you can help, I'm would be really thankful,
if you do.

-------------------------

Eugene | 2017-06-09 13:10:22 UTC | #14

Actually, I'd like to help, but this thread is too big and I don't have enough inspiration to read it. I'll do it later.

-------------------------

slapin | 2017-06-09 13:13:21 UTC | #15

That is really fine by me, don't rush. I have workaround, so I can manage. The hobby should be fun, no schedules,
lots of beer!

-------------------------

George1 | 2017-06-09 18:55:09 UTC | #16

Try to walk with your shoulder, arm and spine rotate like that. It is not natural pose.you will get injury.

https://www.youtube.com/watch?v=8q7N9W5Qzbc

Simple video showing unconstrained one bone head look at from code I pasted responded to one of your other post. 
You can see that Urho works just fine. Just use the Fabrik inverse kinematic code, or you could implement it in less than 100 lines of code for the ik code base itself.

-------------------------

smellymumbler | 2017-06-09 18:19:56 UTC | #17

Hey George, do you have the source of that sample?

-------------------------

George1 | 2017-06-09 18:38:07 UTC | #18

Hi,
I just edit the SkeletalAnimation sample. 
Add the following globals.

Urho3D::Node *head [100];
Urho3D::Node *man [100];
Urho3D::Node *box; //Create this box somewhere.


Inside generating 100 Jack models I do these.

	man[i] = modelNode;
	head[i] = modelNode->GetChild("Bip01_Head", true);
				modelObject->GetSkeleton().GetBone("Bip01_Head")->animated_ = false;



Inside update loop I do this.


box->SetWorldPosition(head[0]->GetWorldPosition() + Vector3(0, 3, 2));

	for (int i = 0; i < 100; ++i)
	{
		Vector3 dir1 = man[i]->GetWorldDirection(); 
		Vector3 dir2 = box->GetWorldPosition() - head[i]->GetWorldPosition();
		Quaternion delta(dir1.Normalized(), dir2.Normalized());

		head[i]->SetRotation(Quaternion());
		head[i]->SetWorldRotation(delta*head[i]->GetWorldRotation());

	}

-------------------------

Lumak | 2017-06-09 20:07:06 UTC | #19

Here's my test:
https://youtu.be/rvSUYXETtTk

-------------------------

coldev | 2017-06-10 00:14:36 UTC | #20

Please share in Github....

Thanks

-------------------------

George1 | 2017-06-10 02:43:58 UTC | #21

Hi Lumak,
I like that coordinate frame very much. It is very useful for many purposes. 

Can you share it in your useful free components source please.

Thanks mate

-------------------------

slapin | 2017-06-10 03:44:39 UTC | #22

Yeah, everything cool about your example, except:
head[i]->SetWorldRotation(delta*head[i]->GetWorldRotation());
sets my model's head 180-degrees rotated and looking away from target.
while in rest pose it is Z-facing.
But if I use relative rotation via Rotate() and use head's child node as aid
for current head direction,everything works as intended.

-------------------------

slapin | 2017-06-10 03:45:47 UTC | #23

btw, how do you record video of Urho or are you all on windows?

-------------------------

George1 | 2017-06-10 03:58:29 UTC | #24

Yes, you could use relative rotation like in my previous respond to your other post.

head->SetRotation(head->GetParent()->GetWorldRotation().Inverse()* delta* head->GetWorldRotation());


Check your character. Maybe send your model to the MOD or developer so they can see what's wrong with it.

There are lots great open source recorder if you search for it. E.g. Open Procaster.

A great pay sourceware is Bandicam.

Best regards

-------------------------

slapin | 2017-06-10 04:05:55 UTC | #25

well, it was working fine until 2 months ago when it broke (I mean video recording), looks like video is out of sync
regardless of vsync setting.
I don't really think anybody will touch this problem regardless of what I do, so I will just wait until somebody else is
hit by it who cares enough to fix it. I worked it around, made people aware of it, so I don't care (that much) anymore.
If anybody will ask me about it I will help and answer, otherwise, let it go to hell.

https://youtu.be/5IUPuzMQU0Y

-------------------------

slapin | 2017-06-10 04:10:15 UTC | #26

[quote="George1, post:16, topic:3227, full:true"]
Try to walk with your shoulder, arm and spine rotate like that. It is not natural pose.you will get injury.
[/quote]

It is not because you can't, it is because you get dizzy. And if you stay still there is nothing wrong about looking up.
Especially if there's something falling from the sky. So that is behavior problem, not animation problem.
Your reasons to not implement this look like very bad excuse. I won't go to your single-bone look club.

-------------------------

George1 | 2017-06-10 04:49:05 UTC | #27

[quote="slapin, post:25, topic:3227"]
people aware
[/quote]

I never said you can't. I said you don't do it.

Well I won't rant about it, it self is a field of study. Look it up.

Well it's your feature requirement, you need it. I don't need it, so I won't create it for you.

-------------------------

weitjong | 2017-06-10 05:00:23 UTC | #28

Please tone down every one.

-------------------------

George1 | 2017-06-10 05:03:01 UTC | #29

The energy of youth is too much to be contained :).

-------------------------

slapin | 2017-06-10 05:07:40 UTC | #30

Yeah, in my 40s I'm young again! And full of energy :-F~~~

-------------------------

slapin | 2017-06-10 05:08:17 UTC | #31

Yeah and I think I can ***overdrink*** anyone here!

-------------------------

George1 | 2017-06-10 05:17:57 UTC | #32

Hehe, great to have some humor back :).

I haven't try or verify the Urho IK feature yet. But try using the IK code for your problem, it will reduce the effort.

In the olden day, if all my characters are back to front for other engine, I would create a node with a basic invisible component. 
Load in my character model attach it to the invisible node and rotate the character. 
Now my character is child to this parent node with the correct direction.

Best regards

-------------------------

slapin | 2017-06-10 09:47:18 UTC | #33

My character itself IS Z-front, just some bone positions are not Z-front.

-------------------------

pqftgs | 2017-06-15 13:02:27 UTC | #35

Had a similar problem about a year ago.  The model was Z = forward, the rig was not.  Tried 3 different engines, all broken, until I exported to FBX.  So there's probably some kind of black magic going on with import/export.

Anyhow I've since re-made the rig with the same forward facing and no more problems.  I do wish the Urho3D exporter was a little more forgiving... but not enough to bother trying to change it.

Hope this helps.

-------------------------

Lumak | 2017-06-25 00:02:09 UTC | #36

[quote="coldev, post:20, topic:3227, full:true"]
Please share in Github....

Thanks
[/quote]

Was this directed at me? Not sure but this is too simple to be a github repo. I'll just post it here.

Test code from the vid:
[spoiler]
[code]
void CharacterDemo::TestHeadRotation()
{
    if (!character_)
        return;

    Node* characterNode = character_->GetNode();
    Vector3 charPos = characterNode->GetPosition();
    Quaternion rot = characterNode->GetRotation();

    // local x, y pos
    float xpos = Sin(scene_->GetElapsedTime() * 90.0f) * 1.25f;// [-1.25 to 1.25]
    float ypos = Sin(scene_->GetElapsedTime() * 90.0f * 0.5f); // [-1.0 to 1.0] but at 1/2 the speed

    Node* headNode = characterNode->GetChild("Mutant:Head", true);
    Vector3 worldPos = rot * Vector3(xpos, ypos, 1.5f);
    Vector3 headWorldTarget = headNode->GetWorldPosition() + worldPos;

    // head lookat rotation
    // same as what's in HandlePostUpdate() but the headDir is based on lookDir not char rotation
    Vector3 lookDir = (headWorldTarget - headNode->GetWorldPosition()).Normalized();
    Quaternion headDir;
    headDir.FromLookRotation(lookDir);

    Vector3 headWorldTarget2 = headNode->GetWorldPosition() + headDir * Vector3(0, 0, -1);
    headNode->LookAt(headWorldTarget2);

    // move the cam at an offset and rotation to see the head rotate
    Vector3 camLookPos = charPos + Vector3(0.0f, 1.0f, 0.0f);
    Vector3 camPos = charPos + rot * Vector3(-5.0f, 1.0f, 4.0f);
    cameraNode_->SetPosition(camPos);
    cameraNode_->LookAt(camLookPos);

    // dbg lines
    DebugRenderer *dbgRenderer = scene_->GetComponent<DebugRenderer>();
    dbgRenderer->AddLine(headWorldTarget, headWorldTarget + Vector3::UP * 0.2f,      Color::GREEN);
    dbgRenderer->AddLine(headWorldTarget, headWorldTarget + Vector3::FORWARD * 0.2f, Color::BLUE);
    dbgRenderer->AddLine(headWorldTarget, headWorldTarget + Vector3::RIGHT * 0.2f,   Color::RED);
    dbgRenderer->AddLine(headWorldTarget, headNode->GetWorldPosition(),              Color::CYAN);

}

[/code]
[/spoiler]

-------------------------

coldev | 2017-06-25 16:15:54 UTC | #38

thanks again :stuck_out_tongue:

-------------------------

S.L.C | 2017-06-25 17:09:45 UTC | #39

While your display of gratitude is definitely appreciated. I would like to inform you guys, that there's a like button bellow each post. Meant for these kind of situations.

----------

_I never really understood why people don't use the builtin functionality of the site. Not just here. But on every community I've been following._

-------------------------

