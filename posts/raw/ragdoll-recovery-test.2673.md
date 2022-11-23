Lumak | 2017-01-06 06:31:04 UTC | #1

video
https://youtu.be/zS26DxVsimw

edit: changed the title to "ragdoll recovery test"

-------------------------

Mike | 2017-01-05 20:24:53 UTC | #2

Awesome! :grinning:
Reminds me of magic.lixin experiments.

-------------------------

ghidra | 2017-01-05 22:10:57 UTC | #3

Thats is totally awesome!

-------------------------

Lumak | 2017-01-06 06:29:36 UTC | #4

His Batman videos? Yeah, kinda does

-------------------------

rasteron | 2017-01-08 07:38:44 UTC | #5

Looking good and awesome, keep it up!

-------------------------

sabotage3d | 2017-01-08 11:35:23 UTC | #6

Looks really nice. Are you using IK solver? How are you blending?

-------------------------

Lumak | 2017-01-08 15:44:59 UTC | #7

No IK. Blending is done by blending to the ragdoll's node transforms instead of skeleton.

In AnimatedModel::ApplyAnimation(), I wrap skeleton_.ResetSilent() with:
      
            if (!ragdollRecovery_)
            {
                skeleton_.ResetSilent();
            }

Then adding a slight delay in AnimationController::Update() for ragdoll blending to the 1st frame of the stand up animaiton.

-------------------------

