slapin | 2017-06-04 20:40:25 UTC | #1

I'm really sorry if I said something which could be interpreted as offensive,
I really did not intend to and I don't understand what happened.

@Lumak, @weitjong

This is about the following issue: 
https://github.com/urho3d/Urho3D/issues/1961

As the result of other topic and thanks to comments from people I understand the logic behind
rotation (probably not logic, but merely a system, but that is not important detail).
But I still don't understand about LookAt. It is misbehaving in my point of view.
I tried to get some insight, but for some reason people were offended. I really don't understand why,
I'm just looking for truth. I really respect you all. Please don't be like that.

-------------------------

lezak | 2017-06-03 22:41:08 UTC | #2

The problem is caused by the axis that You use as forward - take a look at image lower: I have attached same "look at teapot" script to both mutant and ninja: 
- positive Z is used as forward for ninja and script works fine, ninja is looking at teapot;
- in case of the mutant forward is negative Z and mutant is looking in opposite direction

Long story short - to use LookAt,  forward should be positive Z otherwise You'll have to invert results
<img src=http://i.imgur.com/sNSpUb2.png>

-------------------------

slapin | 2017-06-03 23:00:02 UTC | #3

Thanks for your answer!

However, I export via Blender exporter in Front mode (-Y+Z) which means Z-front.
And if I move in Z+ direction the model moves and rotates properly, I don't need to fixup.

Can actual bone rotations affect this?

-------------------------

slapin | 2017-06-03 23:01:14 UTC | #4

So do I have to have Z-forward on actual bone, this is question which is last one on this particular thing.

-------------------------

lezak | 2017-06-03 23:32:41 UTC | #5

In blender, select all bones then press ctr+n (or space and search for Recalculate Roll) and pick "Global +Y Axis"

-------------------------

slapin | 2017-06-03 23:38:17 UTC | #6

Will this change affect existing animations?

-------------------------

lezak | 2017-06-03 23:46:34 UTC | #7

Oh, I haven't thought about that. Unfortunately yes.

-------------------------

slapin | 2017-06-03 23:49:11 UTC | #8

So basically LookAt will not work if bone is not Z-front, right?

-------------------------

lezak | 2017-06-04 00:49:46 UTC | #9

[quote="slapin, post:8, topic:3204, full:true"]
So basically LookAt will not work if bone is not Z-front, right?
[/quote]

In angel script:

                head.LookAt(lookAt.position);
                Quaternion rot = Quaternion();
                rot.FromLookRotation(-head.direction, Vector3::UP);
                head.rotation = rot;
head is head bone, lookAt is target to look at.

EDIT:
one more thing ; since LookAt function is already calling FromLookRotation, it may be a better idea to actually modify or create new LookAt function that calls FromLookRotation with '-direction' so it wouldn't be called twice.

-------------------------

slapin | 2017-06-04 00:56:30 UTC | #10

Is there some generic way possible, i.e. is it possible for me to get bone initial rotation and compensate?
Hardcoding such things is getting in huge trap in future...

-------------------------

slapin | 2017-06-04 05:27:47 UTC | #11

This is how it currently works with correction. There is no way to make NPC look directly at camera
or directly at anything. Some correction i needed, but I don't know how to calculate it.

Current looking code:

    void BTBlackboard::HandleSceneDrawableUpdateFinished(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData)
    {
            Node *head = node_->GetChild("head", true);
            Node *spine = node_->GetChild("spine02", true);
            Node *root = node_->GetChild("root", true);
            AnimatedModel *anim = node_->GetComponent<AnimatedModel>(true);
            Skeleton skel = anim->GetSkeleton();
            Bone *head_bone = skel.GetBone("head");
            Bone *spine_bone = skel.GetBone("spine02");
            Quaternion head_r = head_bone->initialRotation_;
            Quaternion spine_r = spine_bone->initialRotation_;
            if (look_at_enabled && look_at) {
                    Node *lookat_target = look_at;
                    PODVector<Node *> children = look_at->GetChildrenWithTag("player");
                    if (children.Size() > 0) {
                            lookat_target = children[0];
                            VariantMap vars = lookat_target->GetVars();
                            bool first_person = vars["first_person"].GetBool();
                            if (first_person)
                                    lookat_target = (Node *) vars["camera_node"].GetPtr();
                            else {
                                    URHO3D_LOGINFO("no camera");
                                    lookat_target = look_at->GetChild("head", true);
                            }
                    } else {
                            lookat_target = look_at->GetChild("head", true);
                    }
                    if (!lookat_target)
                            lookat_target = look_at;
                    URHO3D_LOGINFO("looking at: " + lookat_target->GetName() + " " + lookat_target->GetWorldPosition().ToString());
                    URHO3D_LOGINFO("from: " +  head->GetWorldPosition().ToString());
                    Quaternion prep;
                    Vector3 dir = (lookat_target->GetWorldPosition() - node_->GetWorldPosition() - Vector3(0.0f, 0.7f, 0.0f));
                    URHO3D_LOGINFO("dir: " +  dir.ToString());
                    prep.FromLookRotation(dir, Vector3(0.0f, 1.0f, 0.0f));
                    Quaternion rot = root->GetWorldRotation();
                    spine->SetWorldRotation(rot.Slerp(spine_r.Inverse() * prep, 0.5));
                    head->SetWorldRotation(head_r.Inverse() * prep);
            }
    }


https://youtu.be/e2Sco61dXzs

-------------------------

Modanung | 2017-06-04 19:26:26 UTC | #12

[quote="slapin, post:1, topic:3204"]
I'm just looking for truth
[/quote]
Rightfully so. But in this case the truth may lie in a lesson about stubbornness? ;)
Glad this seems over with.

Nice progress, btw.

-------------------------

johnnycable | 2017-06-04 17:07:07 UTC | #13

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/addef48c9ddff97e435c0ff0f34eb6bd6286d123.png" width="463" height="500">

-------------------------

slapin | 2017-06-04 19:58:03 UTC | #14

But still, the question persists - how to calculate correction in this case?

-------------------------

