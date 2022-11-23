sovereign313 | 2017-01-02 01:09:48 UTC | #1

So, I've set the loop mode to LM_FORCE_CLAMPED on some of the Animated Sprites, but once it reaches the last frame, it loops and continues playing.  Is there a way to stop the animation from looping, and only playing once?

EDIT

Apparently, calling 

[code]
spriterAnimatedSprite->SetLoopMode(LM_FORCE_CLAMPED) 
[/code]

does NOT work.  Instead, you have to call the loop mode when you set the animation:

[code]
spriterAnimatedSprite->SetAnimation(spriterAnimationSet->GetAnimation(0), LM_FORCE_CLAMPED)
[/code]

Solved.

-------------------------

