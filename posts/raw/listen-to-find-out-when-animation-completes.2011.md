nairdap | 2017-01-02 01:12:16 UTC | #1

I want to know when an AnimatedSprite2D animation completes but can't seem to find anything like OnAnimationComplete() in the class reference. 
Is there an easy way to find out when and animation ends? With a listener, function call etc?

-------------------------

1vanK | 2017-01-02 01:12:16 UTC | #2

As far as I know is no way for it without modification of engine.

-------------------------

cadaver | 2017-01-02 01:12:16 UTC | #3

Yeah the 2D and 3D animations are just totally different code. It shouldn't be a hard add though, would go to the SpriterInstance class in Urho2D, and the same event (E_ANIMATIONFINISHED in DrawableEvents.h) could be used.

-------------------------

cadaver | 2017-01-02 01:12:17 UTC | #4

E_ANIMATIONFINISHED event has been added to master branch for AnimatedSprite2D (only for Spriter animation mode, since I don't use the proprietary Spine library, and it has its own internal playback update function.) It works just like the 3D counterpart, so that the finish event is sent by the component's scene node.

-------------------------

nairdap | 2017-01-02 01:12:23 UTC | #5

Thank you very much [b]cadaver[/b] for the quick implementation.

I have another question now, this is my code:

I create multiple spriter nodes like this in a loop (just like in the sample [b]Urho2DSpriterAnimation.cpp[/b]):

[code]
spriterNode_ = scene_->CreateChild("SpriterAnimation");
AnimatedSprite2D* spriterAnimatedSprite = spriterNode_->CreateComponent<AnimatedSprite2D>();
spriterAnimatedSprite->SetAnimationSet(spriterAnimationSet);
spriterAnimatedSprite->SetAnimation(spriterAnimationSet->GetAnimation(spriterAnimationIndex_));
[/code]

and subscribe to the event:

[code]SubscribeToEvent(E_ANIMATIONFINISHED, URHO3D_HANDLER(Scene, HandleAnimationFinished));[/code]

and my event handler looks like this:

[code]
void HandleAnimationFinished(StringHash eventType, VariantMap& eventData) {
		using namespace AnimationFinished;

		spriterNode = eventData[P_NODE].GetPtr(); //change this

      ...do something with spriterNode...
}
[/code]

How do I get the spriterNode from eventData? Is this possible?

-------------------------

cadaver | 2017-01-02 01:12:24 UTC | #6

GetPtr() returns a RefCounted* which you can cast to the correct type. In this case it's sure to be an object of type Node so you can use static_cast, but in case you'd be unsure you could use a dynamic cast instead.

-------------------------

