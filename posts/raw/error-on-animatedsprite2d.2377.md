carmanuel.zarate | 2017-01-02 01:15:03 UTC | #1

excuse my English, I'm trying to use the integration with spriter, but when trying to apply the LOO_PMODE but will not play the animation, also tried to apply a negative read speed animation but does not work.
[code]
    AnimatedSprite2D* animatedSprite = node_->CreateComponent<AnimatedSprite2D>();
    animatedSprite->SetAnimationSet(animationSet);
    animatedSprite->SetAnimation("run");
    animatedSprite->SetSpeed(-1.5f);

[/code]

[code]
    AnimatedSprite2D* gunanim = weaponnode->CreateComponent<AnimatedSprite2D>();
    gunanim->SetAnimationSet(weaponanimset);
    gunanim->SetAnimation("shoot");
    gunanim->SetLoopMode(LM_FORCE_CLAMPED);
[/code]

-------------------------

Mike | 2017-01-02 01:15:04 UTC | #2

Reverse play (negative speed) is currently not supported.

I cannot reproduce your issue with LM_FORCE_CLAMPED loop mode. Its purpose is to override the scml setting by forcing the animation to only play once, then stop, so maybe your animation is too short for you to notice it. If it's not the case then you should post a simple scml file that allows to reproduce the issue.

-------------------------

