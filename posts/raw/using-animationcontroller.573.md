rogerdv | 2017-01-02 01:01:27 UTC | #1

Im trying to underestand how animation works and implement it in my game. From reading the samples, I got the impression that I can use animation states and manually advance animation for each mesh (like I did in Ogre) or use an AnimationCotroller. Does it means that AnimationCotroller automatically updates all animated meshes if I call AnimationController::Update?

-------------------------

cadaver | 2017-01-02 01:01:27 UTC | #2

AnimationController updates the AnimatedModel in the same node it exists in, so you need a separate controller for each animating character. AnimationController::Update() is also automatically called as part of the engine frame processing loop, by responding to the PostUpdate event, so you don't have to call it yourself.

-------------------------

rogerdv | 2017-01-02 01:01:27 UTC | #3

Can you explain a bit how to set up multiple animations then? Im confused if I still need an animationState (or one for each animation).

-------------------------

cadaver | 2017-01-02 01:01:27 UTC | #4

I recommend to look at what NinjaSnowWar does, it plays at least two animations (walk & shoot) at the same time.

Internally AnimationController will create and delete AnimationStates in the model it's controlling. While the animations are running, you're able to query the states from the model component, though the idea is that the AnimationController API should be sufficient usually, and if you also use manually created AnimationStates at the same time in the same model, your code and AnimationController may end up "fighting".

-------------------------

