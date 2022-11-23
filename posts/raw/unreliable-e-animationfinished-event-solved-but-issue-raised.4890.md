Leith | 2019-02-02 15:35:38 UTC | #1

Hey guys,
I'm using AnimationController on a Zombie model, which works great for Looping animations.
Today I implemented Attack animations, where Looping is False.
I subscribe to E_ANIMATIONFINISHED in order to receive notification that we've reached the end of a non-looping animation, and in the handler for that event, I Unsubscribe from it.
All good so far, except that after a few attacks, my Zombie fails to receive that important event, and so it just stands there looking stupidly at my player. 
I can trigger further attacks by moving the player away from the zombie, but what I really would like to know, is why my code is not reliably receiving the event in question!

[code]
        }else
        {
            if(okToAttack_)
            {
                /// Choose a random attack
                int rand=Rand();
                float frand = (float)rand / 32768.0f;
                frand *=3; // zombies have three attacks
                int irand = (int)frand;

                /// Play attack animation - looping is FALSE
                animCtrl->PlayExclusive(Animations_[Animations_Zombie::Z_Attack + irand].Name, 0, false, 0.2f);
                /// During attack, it is not ok to attack again
                okToAttack_=false;
                /// We need to be notified when the attack animation has finished
                SubscribeToEvent( GetNode()->GetChild("Adjustment"), E_ANIMATIONFINISHED, URHO3D_HANDLER(Character, HandleAnimationFinished));

            }
        }
    }

}

void Character::HandleAnimationFinished(StringHash eventType, VariantMap& eventData){
    /// Attack animation has finished - we can stop listening for this event
    UnsubscribeFromEvent(GetNode()->GetChild("Adjustment"), E_ANIMATIONFINISHED);
    /// Zombie is now free to attack again
    okToAttack_=true;
}
[/code]

EDIT: 
I have discovered that this bug only occurs when the same non-looping animation is executed twice in a row. AnimationController thinks it has already sent the event once, and so never sends it again, unless a different animation is played. Sure I could keep track of which attack was used last and make sure never to use the same attack twice in a row, and that's fine for my zombie, but it's a big problem for my player character, we have to assume that the player will repeatedly apply the same attack, so short of monitoring the state of the non-looping animation, I'm out of luck! Has anyone else run into this issue? What was your workaround? 
Calling Stop on the previously-played animation did not fix it, the only thing that has worked for me is calling SetTime on the previous animation, and passing in zero as the time.

-------------------------

johnnycable | 2019-02-02 13:59:26 UTC | #2

Didn't try specifically, but it seems the animation controller needs a sort of reset function...

-------------------------

Leith | 2019-02-02 14:32:44 UTC | #3

Yeah man, the Stop method needs to call SetTime(0) for starters

It would be unfair of me to complain, tell you I found a way to fix the issue, and not post code.
Here is my workaround, which assumes that we keep track of the previous non looping animation we played.

[code]
        }else
        {
            if(okToAttack_)
            {


                /// Set time of previous animation to zero to prevent bug in playing same animation twice
                animCtrl->SetTime( Animations_[AttackAnimationIndex].Name,0);

                /// Choose a random attack
                int rand=Rand();
                float frand = (float)rand / 32768.0f;
                frand *=3; // zombies have three attacks
                int irand = (int)frand;
                AttackAnimationIndex = Animations_Zombie::Z_Attack + irand;

                /// Play attack animation - looping is FALSE
                animCtrl->PlayExclusive(Animations_[AttackAnimationIndex].Name, 0, false, 0.2f);
                /// During attack, it is not ok to attack again
                okToAttack_=false;
                /// We need to be notified when the attack animation has finished
                SubscribeToEvent( GetNode()->GetChild("Adjustment"), E_ANIMATIONFINISHED, URHO3D_HANDLER(Character, HandleAnimationFinished));
            }
        }
[/code]

This is not over - I want to see this fixed in the head branch, not just be a footnote I left for the next guy.

-------------------------

lezak | 2019-02-02 17:29:22 UTC | #4

[quote="Leith, post:3, topic:4890"]
This is not over - I want to see this fixed in the head branch, not just be a footnote I left for the next guy.
[/quote]

Well, I just hope that the 'next guy' will read <a href="https://urho3d.github.io/documentation/HEAD/_skeletal_animation.html">the docs first</a> and maybe later<a href ="https://github.com/urho3d/Urho3D/blob/d67533617db737fdc2972d49400eecb4163cf38a/bin/Data/Scripts/NinjaSnowWar/Ninja.as#L231"> go over some samples. </a>

-------------------------

I3DB | 2019-02-03 16:45:15 UTC | #5

I found this paragraph at the top of the docs:

Note that [AnimationController](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_animation_controller.html) does not by default stop non-looping animations automatically once they reach the end, so their final pose will stay in effect. Rather they must either be stopped manually, or the [SetAutoFade()](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_animation_controller.html#a8ae79e48a4111a65e8a22f821df4f03c) function can be used to make them automatically fade out once reaching the end.

-------------------------

Leith | 2019-02-03 01:10:43 UTC | #6

And I said that calling Stop did not resolve the issue of playing a non looping animation twice in a row, but only getting the animation event once - I was quite clear about this - the documentation did not help me - the only thing that did help was manually setting the time to zero, on an animation state that had already finished playing! When I do something consistent, like sign up to receive event X, I expect to receive event X - not just once, but consistently - given that non looping animations do not stop themselves, I needed to receive notification that the animation had finished - I accept that it is a corner case to play the same animation twice, but I believe it to be a very common case as well, and was surprised that the issue appears to have gone unnoticed for all this time.

-------------------------

I3DB | 2019-02-03 16:48:32 UTC | #7

[quote="Leith, post:6, topic:4890"]
the documentation did not help me - the only thing that did help was manually setting the time to zero
[/quote]

[quote="I3DB, post:5, topic:4890"]


Rather they must either be stopped manually, or the [SetAutoFade()](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_animation_controller.html#a8ae79e48a4111a65e8a22f821df4f03c) function can be used to make them automatically fade
[/quote]
SetAutoFade description:

Set animation autofade at end (non-looped animations only.) **_Zero time disables_**. Return true on success.

[quote="lezak, post:4, topic:4890"]
maybe later[ go over some samples.](https://github.com/urho3d/Urho3D/blob/d67533617db737fdc2972d49400eecb4163cf38a/bin/Data/Scripts/NinjaSnowWar/Ninja.as#L231)
[/quote]

That sample sets time to zero, in code, so manually.

-------------------------

Leith | 2019-02-04 04:52:36 UTC | #8

I'm not looking for a fight, but I would like to contribute anything I learn to the documentation, and this is currently an issue - doxygen only includes footnotes left in the sourcecode, and there are gaps in the learning of this engine that remain unfilled, unless you happen to be quite good at poking around in the master sourcecode. I would contribute my findings to a FAQ, but we have none. You're left to scour the forum for help, and cross your fingers for luck.

-------------------------

weitjong | 2019-02-07 12:47:16 UTC | #9

Well, I would disagree to dismiss all the documentation work done by Lasse as “footnotes”. The bulk of the text in the online doc are actually manually authored by Lasse initially in separate files (but using Doxygen format). Granted it could be better but no one is complaining so far. The source code is the best documentation available in the project. Aside from the Doxygen style documentation for the classes and methods, the code are so well commented and clearly written, I don’t need to graduate from a computer science to understand them. That’s what attracted me to the project long time ago. One should manage their expectation. Urho3D Project is a non-profit organization without any sponsors to date. If you want to contribute, please do contribute. Don’t need to find any excuses.

-------------------------

Modanung | 2019-02-04 08:24:08 UTC | #10

[quote="Leith, post:8, topic:4890"]
I would contribute my findings to a FAQ, but we have none.
[/quote]

There's the [wiki](https://github.com/urho3d/urho3d/wiki).

-------------------------

Leith | 2019-02-04 12:20:05 UTC | #11

Modanung, I have had entire wiki pages of my life deleted because of the 'notability clause' which states that your content needs to be a repeat of something pubished elsewhere in order to be 'notable' - so I don't trust wiki to retain my content

-------------------------

Leith | 2019-02-04 13:16:24 UTC | #12

I am complaining, I just got here, and doxygen is not enough - the original notes by lasse are great, but not enough. I am relying on you guys, secondly, and the master source firstly, this is not easy to learn but I wrote a playable game vertical slice in two weeks, so complaining seems like a bad idea

-------------------------

Modanung | 2019-02-04 14:49:13 UTC | #13

[quote="Leith, post:11, topic:4890"]
I have had entire wiki pages of my life deleted because of the ‘notability clause’ which states that your content needs to be a repeat of something pubished elsewhere in order to be ‘notable’
[/quote]

I think that mostly applies to (the English) Wikipedia, not wikis in general but rather encyclopedias.

-------------------------

Leith | 2019-02-06 05:01:04 UTC | #14

This was on my own wiki page, not the main wikipedia - I still had editors come to my page, mark it as not being notable, and delete my content (it was a lot of technical information, with a big chunk of information about undocumented features of various 8-bit cpu and os)
Unsurprisingly, the editor(s) in question did not have to provide any kind of evidence of their expertise in regards to my technical documents, they merely had to perform a basic notability test - namely, google for the information, and if not found, tag as not notable.

-------------------------

