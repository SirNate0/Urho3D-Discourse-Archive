GodMan | 2020-02-14 23:25:23 UTC | #1

So I have gotten animation blending working with animation and animation state. I have not gotten this to work with an animation controller however. If I read the docs right I create an animation state then assign that to a layer. I then use the layer in the animation controller. It does not play both animations together. Like it did before using the animation controller. 

Code:

    const int LAYER_MOVE = 1;
    const int LAYER_ATTACK = 0;

    		Animation* combat_sword_idle = cache->GetResource<Animation>("Models/combat_sword_move_front.ani");
    		Animation* combat_sword_melee2 = cache->GetResource<Animation>("Models/combat_sword_melee2.ani");

    		Bone* root = modelObject2->GetSkeleton().GetBone("spine");

    		state = modelObject2->AddAnimationState(combat_sword_idle);
    		state->SetWeight(1.0f);
    		state->SetLooped(true);
    		state->SetLayer(LAYER_MOVE);

    		state2 = modelObject2->AddAnimationState(combat_sword_melee2);
    		state2->SetWeight(0.0f);
    		state2->SetLooped(true);
    		state2->SetStartBone(root);
    		state2->SetLayer(LAYER_ATTACK);

    		swordmelee->Play("Models/combat_sword_melee2.ani", LAYER_ATTACK, true, 0.5f);
    		swordIdle->Play("Models/combat_sword_move_front.ani", LAYER_MOVE, true, 0.5f);

-------------------------

Modanung | 2020-02-14 23:54:20 UTC | #2

[quote="GodMan, post:1, topic:5926"]
swordmelee->Play("Models/combat_sword_melee2.ani", LAYER_ATTACK, true, 0.5f); swordIdle->Play("Models/combat_sword_move_front.ani", LAYER_MOVE, true, 0.5f);
[/quote]
In the comments of the skeletal animation example it states:
> Create an AnimationState for a walk animation. Its time position will need to be manually updated to advance the animation. The *alternative* would be to use an AnimationController component which updates the animation automatically.

There should be one `AnimationController` per `AnimatedModel` and not one for each animation. Telling the AC to play an animation automatically adds an `AnimationState` for that animation.

-------------------------

GodMan | 2020-02-15 01:12:16 UTC | #3

I did have one controller when I initially started it. I still could not get it to work the same as without the controller.

-------------------------

GodMan | 2020-02-15 20:05:46 UTC | #4

Okay I think I tracked it down. Thanks

I thought I would post the code for someone in the future.

If you want to blend lets say a melee animation while your character or NPC is running or walking.

First create a layer.
```
const int LAYER_MOVE = 0;
const int LAYER_ATTACK = 1;
```
LAYER_MOVE has a zero value this means it is the most important animation. It is always playing. Then the LAYER_ATTACK is a one. It is only used with some logic."This animation is not always playing".

Then create a animation controller. `AnimationController* YOURNODE->CreateComponent<AnimationController>();`
```
Animation* combat_sword_idle = cache->GetResource<Animation>("Models/combat_sword_move_front.ani");
Animation* combat_sword_melee2 = cache->GetResource<Animation>("Models/combat_sword_melee2.ani");

Bone* root = modelObject2->GetSkeleton().GetBone("spine");

state = modelObject2->AddAnimationState(combat_sword_idle);
state->SetWeight(1.0f); This is set to 1.0 because the moving animation is the most important.
state->SetLooped(true);
state->SetLayer(LAYER_MOVE);

state2 = modelObject2->AddAnimationState(combat_sword_melee2);
state2->SetWeight(0.0f);
state2->SetLooped(true);
state2->SetStartBone(root); // This animation is for upper body only. So we must set start bone.
state2->SetLayer(LAYER_ATTACK);
```
Then in your main loop or where ever you handle the logic to choose the next animation.
```
swordIdle->Play("Models/combat_sword_melee2.ani", LAYER_ATTACK, true, 0.1f);
state2->SetWeight(0.75f); // This is to blend with the current moving animation.
```
After the animation is finsihed you must call. Otherwise animation will keep playing or character will stop if animation does not loop.
```
state2->SetWeight(0.0f);
```

-------------------------

Modanung | 2020-02-15 18:44:11 UTC | #5

Make sure to have a look at the public methods in `AnimationController.h` to get an idea of other ways this component may be used. I get the feeling you are mixing methods, but it might be legitimate.

[quote="Modanung, post:2, topic:5926"]
In the comments of the skeletal animation example it states:

> Create an AnimationState for a walk animation. Its time position will need to be manually updated to advance the animation. The *alternative* would be to use an AnimationController component which updates the animation automatically.
[/quote]
I read this as:
"An `AnimationController` component is an alternative to creating `AnimationState`s."

-------------------------

GodMan | 2020-02-15 19:04:41 UTC | #6

@Modanung I thought this as well. I felt like I was mixing methods. That is why I created this thread. I think my issue was the state weight. When I tell the NPC to play the melee animation and don't set the state weight for that animation state things do not work correctly.  

I did not see a way to set weights if I use just an animation controller. That is what had me confused.

-------------------------

GodMan | 2020-02-15 19:12:23 UTC | #7

Also I looked at the Ninja project in C++. They use an animation controller as well. However how would I be able to set the start bone for the melee animation just using a controller?

Confused...

-------------------------

Modanung | 2020-02-15 19:44:26 UTC | #8

[quote="GodMan, post:6, topic:5926"]
I did not see a way to set weights if I use just an animation controller.
[/quote]
```
bool AnimationController::SetWeight(const String& name, float weight)
```
[quote="GodMan, post:7, topic:5926"]
However how would I be able to set the start bone for the melee animation just using a controller?
[/quote]
```
bool AnimationController::SetStartBone(const String& name, const String& startBoneName)
```

-------------------------

GodMan | 2020-02-15 19:53:13 UTC | #9

Oh wow. Thanks man. I will make my changes, and post back.

-------------------------

Modanung | 2020-02-15 20:05:46 UTC | #10

These are all the public animation controller functions at your disposal:
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/AnimationController.h#L101-L189

-------------------------

GodMan | 2020-02-15 20:05:44 UTC | #11

Okay so I removed all the animation state methods. Everything is just using one controller, and the controller methods. Everything seems to be working great. Thanks for all the help.

-------------------------

Modanung | 2020-02-15 20:27:54 UTC | #12

You're welcome! :slightly_smiling_face: 

Maybe the skeletal animation sample should include the method demonstrated in NinjaSnowWar, like a 50/50 spread possibly with differently coloured models.   
@GodMan This might be a nice opportunity for you to dip your toes into the PR stream, at your convenience of course. What do you say?

-------------------------

GodMan | 2020-02-15 20:33:41 UTC | #13

Sure. I would not mind helping. Maybe I can make a small demo. Really barebones so other users can understand it. Instead of other projects that have a lot of other things going on in the code.

-------------------------

Modanung | 2020-02-15 20:48:02 UTC | #14

I think it would be best to extend sample six, since - although different - both methods do concern skeletal animation. If you do, be sure to read the coding conventions beforehand:
https://urho3d.github.io/documentation/HEAD/_coding_conventions.html

Also note that samples come in three languages: [C++](https://github.com/urho3d/Urho3D/tree/master/Source/Samples), [AngelScript](https://github.com/urho3d/Urho3D/tree/master/bin/Data/Scripts/) and [Lua](https://github.com/urho3d/Urho3D/tree/master/bin/Data/LuaScripts/).

-------------------------

GodMan | 2020-02-15 21:12:34 UTC | #15

I might do the C++ part. I don't have too much experience with AS,Lua.

-------------------------

Modanung | 2020-02-15 21:23:09 UTC | #16

The samples *could* function as your Rosetta Stone. :slightly_smiling_face:
AS is almost identical to C++. But maybe you would like some feedback on the C++ form even if you were also to create the others after that.

-------------------------

