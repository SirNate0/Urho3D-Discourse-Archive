Mike | 2017-01-02 01:10:04 UTC | #1

When toggling a bone from non-animated to animated, it immediately catches up the animation, without transition.
Is there a convenient way to smoothly transition from custom rotation to animation rotation ?

-------------------------

codingmonkey | 2017-01-02 01:10:04 UTC | #2

[code]    /// Spherical interpolation with another quaternion.
    Quaternion Slerp(Quaternion rhs, float t) const;
    /// Normalized linear interpolation with another quaternion.
    Quaternion Nlerp(Quaternion rhs, float t, bool shortestPath = false) const;[/code]

You may try use this two methods to interpolate quat rotation from curBoneWorldRotation into animBoneWorldRotation

-------------------------

Mike | 2017-01-02 01:10:04 UTC | #3

Thanks, to do this I would have to get the bone's target rotation from keyframe every time step (as other bones are still moving) and slerp until caught up, which is not really convenient.
I'm sure there's a better way, as something similar is already achieved for blending animations together or transitioning/fading from one another.

-------------------------

codingmonkey | 2017-01-02 01:10:04 UTC | #4

I'm found into this code block
[code]void AnimationState::ApplyToModel()
{
    for (Vector<AnimationStateTrack>::Iterator i = stateTracks_.Begin(); i != stateTracks_.End(); ++i)
    {
        AnimationStateTrack& stateTrack = *i;
        float finalWeight = weight_ * stateTrack.weight_;

        // Do not apply if zero effective weight or the bone has animation disabled
        if (Equals(finalWeight, 0.0f) || !stateTrack.bone_->animated_)
            continue;

        if (Equals(finalWeight, 1.0f))
            ApplyTrackFullWeightSilent(stateTrack);
        else
            ApplyTrackBlendedSilent(stateTrack, finalWeight);
    }
}[/code]

and I'm guessing that if aninamated are disabled nodes(bones) are do not transformed by anim track value. 
So, in this case where I may get actual animValue for bone ? 
Maybe from second hided skeleton copy with same animation(and time) but with all enabled bones ?
(or maybe there is need to add additional field to bone struct and silently transform it always, but still not apply for node if animated_ = false, in this case user do this lerp manually and on ending of manual slerp user just turn-on animation for bone, so if this way is fine? this is for - issue task, I guess )

Or maybe in parent space of disabled bone do place for HelperBoneNode and orient\slerp to it. But in this case we do not get own bone animations (as we want) we get only parent space affects on bone in some bind pose.

-------------------------

codingmonkey | 2017-01-02 01:10:04 UTC | #5

I think it's able to change with this way:
- add additional data to bone's struct, where we will be store silent transformation for disabled bone
- change ApplyToModel() with silent applying transforms for bone into this additional data bone struct

So, steps for fix: 

1. Bone struct fix
[spoiler][pastebin]Wr1b4eWJ[/pastebin][/spoiler]

2. fix ApplyTrackFullWeightSilent for checking stateTrack.bone_->animated_ in it.
[spoiler][pastebin]stfq7hMs[/pastebin][/spoiler]

3. Finally fix ApplyToModel() to allow call two methods
[spoiler][pastebin]E4HbmQiF[/pastebin][/spoiler]

4. fix the ApplyTrackBlendedSilent in similar way as ApplyTrackFullWeightSilent (add IF blocks with - !stateTrack.bone_->animated_)

-------------------------

codingmonkey | 2017-01-02 01:10:05 UTC | #6

I try to polish previous trying and I think in some cases of blending we need persistent "shadowed" animation for right blending between keys: 
So, I guess this is final changing for this ability. I do not test this it work but we get now - persistent "shadowed" animation. and we may turn-off and turn-on bones and doing Slep/Lerp to this values in bones struct 
[spoiler][pastebin]geJBWJQe[/pastebin][/spoiler]

EDIT:
I try to testing last code changes, on one animated box with one single bone
box have simple animation - rotating around Y axis (loop)
I disable this one bone from animation
[code]
        animNode = gameScene->scene->GetChild("anim", true);
        animModel = animNode->GetComponent<AnimatedModel>();
        int i = 0;
        animState = animModel->GetAnimationState(i);
        b = animModel->GetSkeleton().GetBone("Bone");
        b->animated_ = false;
[/code]

OnUpdate I add deltatime to Anim State, and as expected it still not animated/move.
And in same time we have actual animation values in bone.shadowedBoneTransform struct

[code]	void HandleUpdate(StringHash eventType, VariantMap& eventData)
	{
		using namespace Update;
		float timeStep = eventData[P_TIMESTEP].GetFloat();

        animState->AddTime(timeStep);
        
        debugUI->debugHud->SetAppStats("shadowed bone position", String(b->shadowedBoneTransform.position));
        debugUI->debugHud->SetAppStats("shadowed bone rotation", String(b->shadowedBoneTransform.rotation));
        debugUI->debugHud->SetAppStats("shadowed bone scale", String(b->shadowedBoneTransform.scale));

	}[/code]

[url=http://savepic.net/7696968.htm][img]http://savepic.net/7696968m.png[/img][/url]

In addition: how to slerp with this shadowed animation:
it simple:
let's say we have two public flags to control our key pressing - key_f3 (turn-on slerp) and key_ f4 (turn-off slerp and bone anim):
[code]    bool goSlerpBones = false;
    float goSlerpTime = 0.0f;

    void HandleKeyDown(StringHash eventType, VariantMap& eventData)
    {
        using namespace KeyDown;
		ResourceCache* cache = context_->GetSubsystem<ResourceCache>();

        // Check for pressing ESC. Note the engine_ member variable for convenience access to the Engine object
        int key = eventData[P_KEY].GetInt();
        if (key == KEY_ESC)
            engine_->Exit();

        if (key == KEY_F2)
            debugUI->ToggleDebugUI();

        if (key == KEY_F3) // start slerp
        {
            goSlerpBones = true;
            goSlerpTime = 0.0f;
            b->animated_ = false;
        }

        if (key == KEY_F4) // stop animation for bone
        {
            goSlerpBones = false;
            goSlerpTime = 0.0f;
            b->animated_ = false;
        }

    }

[/code]

[code]
	void HandleUpdate(StringHash eventType, VariantMap& eventData)
	{
		using namespace Update;
		float timeStep = eventData[P_TIMESTEP].GetFloat();

        animState->AddTime(timeStep);

        const float timeToReachAnimationTrack = 3.0f; // sec

        if (goSlerpBones) 
        {   
            if (goSlerpTime < 1.0f)
            {
                goSlerpTime += ((1.0f / timeToReachAnimationTrack) * timeStep);
                b->node_->SetRotation(b->node_->GetRotation().Slerp(b->shadowedBoneTransform.rotation, goSlerpTime));
            }
            else 
            {
                b->animated_ = true;
                goSlerpTime = 0.0f;
                goSlerpBones = false;
            }
        }
                
        debugUI->debugHud->SetAppStats("shadowed bone position", String(b->shadowedBoneTransform.position));
        debugUI->debugHud->SetAppStats("shadowed bone rotation", String(b->shadowedBoneTransform.rotation));
        debugUI->debugHud->SetAppStats("shadowed bone scale", String(b->shadowedBoneTransform.scale));
        debugUI->debugHud->SetAppStats("shadowed do slerp", String(goSlerpBones));
        debugUI->debugHud->SetAppStats("shadowed slerp factor(normalized time)", String(goSlerpTime));
        debugUI->debugHud->SetAppStats("Is sleketon bone animated", String(b->animated_));
	}

[/code]

Edit2: also I found what quaternions very fast reach angles of each other, even on 0.1f (nq = q.slerp(q, 0.1f)) So, I decide to change factor value to more lower value 0.2f;
I guessing this is only for quaternions, position or scale still need do lerp with full normalized range [0..1f]
[code]
        const float timeToReachAnimationTrack = 3.0f; // sec

        if (goSlerpBones) 
        {   
            if (goSlerpTime < 0.2f)
            {
                goSlerpTime += ((0.2f / timeToReachAnimationTrack) * timeStep);
                b->node_->SetRotation(b->node_->GetRotation().Slerp(b->shadowedBoneTransform.rotation, goSlerpTime));
            }
            else 
            {
                b->animated_ = true;
                goSlerpTime = 0.0f;
                goSlerpBones = false;
            }
        }
[/code]

Edit3: code fix, there is needed use local bone space:

b->node_->SetRotation(b->node_->GetRotation().Slerp(b->shadowedBoneTransform.rotation, goSlerpTime));
there is sources for this example: [github.com/MonkeyFirst/Disabled ... dAnimation](https://github.com/MonkeyFirst/DisabledBoneSlerpWithShadowedAnimation)

-------------------------

magic.lixin | 2017-01-02 01:10:05 UTC | #7

create a manual animation by current pose, and play the pose animation.
   
  below is the sample code:
 
    AnimationController@ ctl = renderNode.GetComponent("AnimationController");
    Animation@ anim = Animation();
    String name = "Test_Pose";
    anim.name = name;
    anim.animationName = name;
    FillAnimationWithCurrentPose(anim, renderNode);
    cache.AddManualResource(anim);

    AnimatedModel@ model = renderNode.GetComponent("AnimatedModel");
    AnimationState@ state = model.AddAnimationState(anim);
    state.weight = 1.0f;
    ctl.PlayExclusive(anim.name, 0, false, 0.0f);

    void FillAnimationWithCurrentPose(Animation@ anim, Node@ _node)
    {
        Array<String> boneNames =
        {
            "Bip01_$AssimpFbx$_Translation",
            "Bip01_$AssimpFbx$_PreRotation",
            "Bip01_$AssimpFbx$_Rotation",
            "Bip01_Pelvis",
            "Bip01_Spine",
            "Bip01_Spine1",
            "Bip01_Spine2",
            "Bip01_Spine3",
            "Bip01_Neck",
            "Bip01_Head",
            "Bip01_L_Thigh",
            "Bip01_L_Calf",
            "Bip01_L_Foot",
            "Bip01_R_Thigh",
            "Bip01_R_Calf",
            "Bip01_R_Foot",
            "Bip01_L_Clavicle",
            "Bip01_L_UpperArm",
            "Bip01_L_Forearm",
            "Bip01_L_Hand",
            "Bip01_R_Clavicle",
            "Bip01_R_UpperArm",
            "Bip01_R_Forearm",
            "Bip01_R_Hand"
        };

        anim.RemoveAllTracks();
        for (uint i=0; i<boneNames.length; ++i)
        {
            Node@ n = _node.GetChild(boneNames[i], true);
            if (n is null)
            {
                log.Error("FillAnimationWithCurrentPose can not find bone " + boneNames[i]);
                continue;
            }
            AnimationTrack@ track = anim.CreateTrack(boneNames[i]);
            track.channelMask = CHANNEL_POSITION | CHANNEL_ROTATION;
            AnimationKeyFrame kf;
            kf.time = 0.0f;
            kf.position = n.position;
            kf.rotation = n.rotation;
            track.AddKeyFrame(kf);
        }
    }

-------------------------

Mike | 2017-01-02 01:10:06 UTC | #8

@ magic.lixin : manual animation was on my todo list, this will save me a lot of time  :wink: 
@ codingmonkey : a big thank for experimentation and complete project to test, will test this as soon as I'll be back home  :slight_smile:

-------------------------

Mike | 2017-01-02 01:10:06 UTC | #9

@ magic.lixin, your solution works perfectly and is trully awesome. This is exactly what I was looking for and I'll be able to use it for many other tasks.
Thanks again  :smiley:

-------------------------

weitjong | 2017-01-02 01:10:06 UTC | #10

Could probably beneficial to add this feature as a generic solution to the engine.

-------------------------

magic.lixin | 2017-01-02 01:10:07 UTC | #11

i was using this piece of code to implement the ragdoll get-up feature
    [video]https://www.youtube.com/watch?v=RbymrZ5mAuM[/video]

-------------------------

Mike | 2017-01-02 01:10:07 UTC | #12

[quote]Could probably beneficial to add this feature as a generic solution to the engine.[/quote]

That's what I had in mind either. Code snippet can be refactored to handle the whole skeleton (iterating through each node) or only a single node. AnimationState is not mandatory.

-------------------------

Mike | 2017-01-02 01:10:07 UTC | #13

Great sample magic.lixin, very professional look and feel  :slight_smile:

-------------------------

weitjong | 2017-01-02 01:10:07 UTC | #14

Nicely done!

-------------------------

