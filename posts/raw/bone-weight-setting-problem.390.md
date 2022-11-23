rifai | 2017-01-02 01:00:04 UTC | #1

What's the correct way to limit animation to specified bones? For example, punch animation I only need upper body bone animation. 

This is how I did :
1. Add Animationstate to Animatedcontroller from code. 
2. Set some unnecessary bones weight to 0 in Animationstate. 
3. Play animation from AnimationController component. 

Animation is run correctly only in first play. Play again animation, bone weight setting is gone. Looks like every time I play animation, its animationState setting is reset.

-------------------------

weitjong | 2017-01-02 01:00:04 UTC | #2

Halo, selamat datang di forum kami.

You can disable animation for individual bone by setting the bone's animated_ property to false. See CharacterDemo for an example of how this works.

-------------------------

cadaver | 2017-01-02 01:00:04 UTC | #3

The easiest way to limit animation (if that is artistically satisfying enough) is to specify the start bone in the bone hierarchy. See SetStartBone() in either AnimationController or AnimationState, both should work. But if that's not enough, then setting the weights per bone is just as proper.

AnimationController will remove one-shot AnimationStates that have been played to the finish and that have been set to automatically fade out upon end. This means the bone weight or start bone settings in the AnimationState are lost and you need to set them again when playing the animation the next time. 

In case this is a problem, note that you can also add AnimationStates to your model and advance them manually without using the AnimationController at all.

-------------------------

rifai | 2017-01-02 01:00:04 UTC | #4

[quote="weitjong"]Halo, selamat datang di forum kami.[/quote]
Haha.. terima kasih.  :smiley: 

[quote="weitjong"] 
You can disable animation for individual bone by setting the bone's animated_ property to false. See CharacterDemo for an example of how this works.
[/quote]
I think that's not gonna work. That'll disable bone from all animations. I want different bone setting for each animation states. 

@cadaver :
Maybe, I'll try animating without AnimationController. Out of curiosity, why animationcontroller works that way? Why don't it save animation state in a kind of cache variable for later usage, so we dont have to set them again? 


Thanks.

-------------------------

cadaver | 2017-01-02 01:00:04 UTC | #5

It's because AnimationController also deals with network replication of animations, and to transmit minimal data it's better to remove states that don't contribute anything visibly. Also, when updating animations, it's faster when we don't have to loop through disabled states only to find that we can skip them.

-------------------------

