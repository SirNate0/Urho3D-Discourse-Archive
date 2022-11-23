Dave82 | 2017-01-02 01:09:32 UTC | #1

So i trying to figure out how to blend 2 animations without making transition to the base frame (the AnimatedModel's default frame at export usually a T pose)

So whenever i try to play another animation , Urho starts blending the current animation into the Model's base frame and then into the new animation...
Lets say the character is playing the walk animation , if i start playing the run animation it will first start blending into the base frame T pose , the slightly goes into the run animation.Causing annoying twitching 

Normally this doesn't happening with fadeTime = 0.0f  , but then there's no animation blending either.

[code]controller->PlayExclusive("walk.ani" , 0 , 0.2f);
controller->PlayExclusive("run.ani" , 0 , 0.2f);
this will create a dumb transition to the T pose then plays the run animation.[/code]

So the question is : Is there any way to blend the new animation from the CURRENT frame ? The frame that was used exacly before the new animation was started ?

-------------------------

rasteron | 2017-01-02 01:09:33 UTC | #2

Afaik this is possible and was asked before. Have you checked the wiki or try this tutorial in gawag's wikia?

[urho3d.wikia.com/wiki/Animations](http://urho3d.wikia.com/wiki/Animations).

-------------------------

Dave82 | 2017-01-02 01:09:34 UTC | #3

Hi ! Thanks for the link ,  some of the problems are now solved , at least now i can actually STOP the animation by NOT UPDATING it.However this still isn't what i want.
This way i have to update and control everything manually , which is even more painful and will end up with same result as AnimationController.

The problem is the blending is controlled via weights.So lest say i play the walk animation with weight = 1.0f it means the animation is fully weighted and played properly.If i set the weight to 0.5f the transformation is calculated between the Model's T Pose and the walk animation. Thats the problem i can't bypass ! What i want is when i play another animation , the AnimationController STOP playing the animation on the specific layer AND remember the current bone matrices and start the blending from this frame to the new animation's beginning , then play thye new animation (As i remember that's how animation blending worked in irrlicht)

Blending animations by fading out weights will cause the AnimatedModel "go" into T Pose at some point and you can only control "how much" to go into T Pose by higher/lower weight value.It would be useful to Stop the current animation so the Model Freezes at this frame.
Currently if you stop an animation the AnimatedModel will go into the T pose.


[b]EDIT[/b]

Well for now i found a bit hacky solution but it just works perfectly. Right before i start playing a new animation , i set the initialPosition_ and initialRotation_ for all bones in the Skeleton.


for (int b = 0; b < skeleton.GetNumBones(); b++)
{
	skeleton.GetBone(b)->initialPosition_ = skeleton.GetBone(b)->node_->GetPosition();
	skeleton.GetBone(b)->initialRotation_ = skeleton.GetBone(b)->node_->GetRotation();
}

-------------------------

rasteron | 2017-01-02 01:09:34 UTC | #4

That's great. Afaik with the T-pose issue, it is not directly engine related and it could be fixed in the animation pipeline/process. I have seen some completed character studies on commercial/indie games which implements a different approach and used a default weapon or relaxed pose method, but I think overall it really depends on the majority of animations that you will be using for your game.

-------------------------

gawag | 2017-01-02 01:10:28 UTC | #5

What the hay...  :smiley: 
There was a question about bones and I dug up some older code to show how to manually control bones. Then I thought "Oh I could use the same example to make a new article in the (official) wiki". I wasn't sure about a detail and searched the forum for it and found:
[quote]Afaik this is possible and was asked before. Have you checked the wiki or try this tutorial in gawag's wikia?
[urho3d.wikia.com/wiki/Animations](http://urho3d.wikia.com/wiki/Animations).[/quote]
*reading my own article...*
Ah it's not in there anyway.  :unamused:

Seems like my work is helpful here and there. BTW: We really could need help in the official wiki: [github.com/urho3d/Urho3D/wiki](https://github.com/urho3d/Urho3D/wiki)
I'm again nearly the only one contributing and I haven't had that much time recently. Also there's so much stuff that I don't know and have no idea about. See the idea page or just write down what you know. There are still many questions about relatively basic stuff which could be easily fixed with more documentation/wiki.

-------------------------

