Leith | 2019-02-14 05:34:57 UTC | #1

Yesterday I made my first attempt to blend two walk animations.
As I have so far been using AnimationController, I tried to be lazy, I tried to just assign two animations to different Layers, and let the controller blend them:

[code]
          animCtrl->Play(Animations_[Animations_Player::WalkForward].Name,0, true, 0.2f);
          animCtrl->Play(Animations_[Animations_Player::StrafeLeft].Name, 1, true, 0.2f);
                       //animCtrl->GetAnimationState(Animations_[Animations_Player::WalkForward].Name)->SetWeight(0.5f);
                    //animCtrl->GetAnimationState(Animations_[Animations_Player::StrafeLeft].Name)->SetWeight(0.5f);
[/code]

This code does not work - and ensuring their weights add to 1 did not help either - any ideas what I did wrong?

[EDIT]
Nevermind - it was a silly logic bug. When I got it working, I found that I *did* need to set the weights on the two animations to 50 percent, and I also noticed that PlayExclusive is *not* disabling animations on other Layers - The resulting blended animation is very "twitchy" and not at all satisfactory, so I'll probably need to call on an Artist to make me some diagonal walking animations, in which case I can go back to using PlayExclusive and crossfading.

Before I go crying to artists, I'll need to synchronize my animations - in this example they are 40 and 45 frames long, respectively - I did not notice any weirdness resulting from their different lengths, but I did notice two things that look horrible - the crossing feet from the strafe animation are not a good mix with a forward animation (acceptable but not good) and the arms seem to twitch and shake in a completely unacceptable way. At least if I use Blender to rescale one of the animations to the same length as the other, I can discount the play length as a possible source of noise, without resorting to individually scaling the speed of each blended animation.

-------------------------

