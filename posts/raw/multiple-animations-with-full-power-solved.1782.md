1vanK | 2017-01-02 01:10:05 UTC | #1

I have 2 animations: forward and side
How to play both with full power? Is it possible?

I have tried

[code]
        Animation* sideAnimation = cache->GetResource<Animation>("Models/HeroWalkSide.ani");
        AnimationState* state = obj->AddAnimationState(sideAnimation);
        state->SetWeight(1.0f);
        state->SetLooped(true);
        Animation* walkAnimation = cache->GetResource<Animation>("Models/HeroWalkForward.ani");
        AnimationState* state2 = obj->AddAnimationState(walkAnimation);
        state2->SetWeight(1.0f);
        state2->SetLooped(true);
[/code]

but the second animation is completely replaces the first.

SetWeight(0.5f) works, but amplitude of animations is small

-------------------------

cadaver | 2017-01-02 01:10:05 UTC | #2

The animation engine uses lerp-blending, not differences like e.g. Ogre, so applying two animations both with full power to the same bone(s) isn't possible. You can instead apply animations to the skeleton partially by setting the startbone, or by setting per-bone weight masks.

-------------------------

1vanK | 2017-01-02 01:10:06 UTC | #3

Thank you

-------------------------

1vanK | 2017-01-02 01:10:06 UTC | #4

May be is way to increase amplitude of result animation?

Multiplier like speed

-------------------------

cadaver | 2017-01-02 01:10:06 UTC | #5

I don't think that is mathematically well defined, at least in a general case. You could do something like take the offset of the result pose local bone position to the bind pose local bone position, and multiply that (essentially making the animation a difference during runtime) but I'm sure that could easily cause crazy mutilations.

-------------------------

