Dave82 | 2017-01-02 01:05:31 UTC | #1

Hi , i found it a littlebit hard to deeply understand how the animation system works ? 

1st : The IsPlaying(name) function is a bit missleading.It actually returns true if the currently playing animation name and the name you check is matching , and NOT if the animation is actually playing (currentTime == length). 
Isn't the IsPlaying(name) should be :

[code]bool AnimationController::IsPlaying(const Urho3D::String &name)
{
    AnimationState* state = GetAnimationState(name);
   state ? (state->GetTime() == state->GetLength() ? false : true) : false;
}[/code]

2nd What are layers ? I tried everything to undertand them , but all they do is playing the animation with highest bit
for an example :

[code]animCtrl->PlayExclusive("walk.ani" , 1 , true , 0.1f);
animCtrl->PlayExclusive("idle.ani" , 2 , true , 0.1f);
animCtrl->PlayExclusive("jump.ani" , 4 , true , 0.1f);
animCtrl->PlayExclusive("aim.ani" , 8 , true , 0.1f);
[/code]

if i execute this code the "aim" animation will be playing like i just played the aim animation on layer 1 without playing the other animations... So i don't see the purpose of the layers
how do they actually work and what do they achieve? Can someone show me an example how to use them ?

Thanks

-------------------------

cadaver | 2017-01-02 01:05:31 UTC | #2

IsPlaying() has been commented as "Return whether an animation is active." which matches what the function is doing. If the animation has reached its end but is still being blended into the skeleton, it's considered active. (Note that you can set animations to automatically fadeout after they reach the end.) You can inspect the time position separately, or alternatively we could add an IsAtEnd() helper function.

Layers simply specify the animation blending order. They don't help much if all your animations contain tracks for all of the skeleton bones, and you're playing back animations at full weight. In that case the highest layer animation "wins" and others aren't seen in the blending result at all.

For example NinjaSnowWar has full-skeleton animations, and it puts the attack animation on a higher layer, so when it fades in, the stand or run pose (lower layer) gradually fades out from underneath.

When you want to combine things like walking and aiming, you'll get best results if for example the aiming doesn't have keyframe tracks for lower body. Alternatively you can control animation blending weight per-bone, for example set zero weight to all lower body bones in the aim animation to effectively disable them from blending.

-------------------------

Dave82 | 2017-01-02 01:05:32 UTC | #3

Thanks cadaver ! I've get it now. The IsAtEnd(const String &name) would be indeed a great feature.

-------------------------

