Leith | 2019-04-11 09:37:46 UTC | #1

I'm having an issue with attempting to deliberately repeat a non-looping animation (via animationcontroller)
I should mention that I am doing so in the FixedUpdate physics pre-step handler, though I doubt that is relevant.

The Urho docs mention that non-looping animations don't stop by themselves - what happens is that they pause at the last animation keyframe, and the animated character remains in that pose.
That's fine, so I figured that if I called Stop on that animation, then I should be able to immediately thereafter call Play on it, but my animation remains in the final pose. I even tried setting the animation's time to zero, still no dice.

[code]
        /// Character is Grounded, and the Jump Key is being pressed!
        ifkey(CTRL_JUMP){

            /// PHYSICS:
            /// Jump, Homer, Jump!
            bulletController_->jump(btVector3(0, 6, 0));

            /// ANIMATION:
            /// If we're already Jumping (i.e. user held down Jump Key while Landing from a previous Jump ...)
            if(isJumping_){
                /// Try to "forcedly repeat" a non-looping animation (this does not work)
//                animCtrl->RemoveAnimationState(animCtrl->GetAnimationState(Animations_[Animations_Player::Jump].Name));
//                animCtrl->Stop(Animations_[Animations_Player::Jump].Name, 0);
                animCtrl->PlayExclusive(Animations_[Animations_Player::Jump].Name, 0, false, 0);
            }else{
                /// Transition to the Jump Animation
                animCtrl->PlayExclusive(Animations_[Animations_Player::Jump].Name, 0, false, 0.2f);

                /// Try to auto-remove animationstate from controller on completion (this does not work either)
                animCtrl->SetRemoveOnCompletion(Animations_[Animations_Player::Jump].Name, true);
            }
            /// Character is Jumping, until it touches the ground again
            isJumping_=true;
        }
[/code]

Has anyone ever needed to repeat a non-looping animation, without changing to another animation first? How did you reset the state of the animation in question?
SetTime does not work. Stop, and SetAutoFade, as hinted by the docs, are also not able to reset a sole animation played as non looping, to deliberately replay it.

-------------------------

Leith | 2019-04-12 04:22:48 UTC | #2

SetAudoFade does not work either - I am screwed, to repeat a non looping single animation on a single layer ...

-------------------------

Modanung | 2019-04-15 14:39:05 UTC | #3

Why not use an extra layer or modify the animations?
Also, are you absolutely sure you're properly setting the animation time?

-------------------------

Leith | 2019-04-16 08:37:58 UTC | #4

Thanks for the reply :slight_smile:  
I've found a workaround - I will document it soon!

-------------------------

Leith | 2019-04-16 08:54:18 UTC | #5

The workaround is to check the animationcontroller for non looping animations which have ended. The controller offers two methods: IsPlaying() which returns true even if a nonlooping animation got caught by the end of play clamp, and IsAtEnd(), which tells the true story for a non-looping animation.

I also learned about mixing animations on a single layer, but I will comment about it elsewhere.
That post will detail what to expect when you want to mix animations on the same layer, and where other layers comes into things :)

-------------------------

Modanung | 2019-04-16 09:19:25 UTC | #6

Are you familiar with the `AnimationFinished` event? [spoiler]`<DrawableEvents.h>`[/spoiler]
```
URHO3D_EVENT(E_ANIMATIONFINISHED, AnimationFinished)
{
    URHO3D_PARAM(P_NODE, Node);                    // Node pointer
    URHO3D_PARAM(P_ANIMATION, Animation);          // Animation pointer
    URHO3D_PARAM(P_NAME, Name);                    // String
    URHO3D_PARAM(P_LOOPED, Looped);                // Bool
}
```

-------------------------

Leith | 2019-04-16 09:27:43 UTC | #7

No - I only know about SceneDrawableUpdateFinished - I'm using neither so far in the Kinematic controller - looks like another event that LogicController didn't register for...

Oh wait: animation finished? Yeah I know about this event, and yes maybe I should use it instead of polling for event completion, I'll review my stuff but I am getting close to happy with the controller now, it feels good, and the only bad in the look is that camera snaps to location and does not interpolate

When I get happy enough, I will offer a version without network serialization stuff. I am close to happy.

-------------------------

