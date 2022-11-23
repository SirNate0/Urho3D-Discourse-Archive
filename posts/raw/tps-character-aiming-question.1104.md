Dave82 | 2017-01-02 01:05:29 UTC | #1

Hi is there an easy way to aim with a tps character ? in aiming mode the character points his gun forward and plays the aim animation loop. What i want is if the player looks up rotate his arms up or if looks down rotate his hands down (like the character's head in CharacterDemo example but keep the aim animation looping and somehow offsetting his hand''s roation.

I tried to modify the offsetMatrix of the bones but it seems that modifing the matrix of a bone will not affect it's children. So all his children's matrices has to be recalculated as well... So this approach can be a pain in the butt...

So i'm wondering if there's some easier way to do this ?

-------------------------

thatonejonguy | 2017-01-02 01:05:29 UTC | #2

Another option might be to use a control bone in your armature. Parent the arms to your control bone, then set up the control bone similar to the head bone in the character demo example (ie animated to false, update its node's rotation in postupdate). The arms will still play their animations and inherit the rotation from the control bone.

Hope that helps,
-Jon

-------------------------

Dave82 | 2017-01-02 01:05:29 UTC | #3

[quote]Modify the transform of the node that is the bone.

Useful posts:
post6034.html
post5727.html[/quote]

Thanks Sinoid ! by Subscribing to E_SCENEDRAWABLEUPDATEFINISHED solved the problem. Works perfectly !Thanks 


[quote]Another option might be to use a c
ontrol bone in your armature. Parent the arms to your control bone, then set up the control bone similar to the head bone in the character demo example (ie animated to false, update its node's rotation in postupdate). The arms will still play their animations and inherit the rotation from the control bone.
Hope that helps,
-Jon[/quote]

Well i don't think that should work. By disabling a bone's animation will also disable it's children , so the only and best solution is to keep the bones enabledand  post-adjust them

-------------------------

thatonejonguy | 2017-01-02 01:05:29 UTC | #4

[quote="Dave82"]

Well i don't think that should work. By disabling a bone's animation will also disable it's children , so the only and best solution is to keep the bones enabledand  post-adjust them[/quote]

I'm glad you found a working solution. But I did want to mention that disabling a bone's animation *doesn't* disable the animation of it's children.

-------------------------

Dave82 | 2017-01-02 01:05:30 UTC | #5

[quote][quote="thatonejonguy"][quote="Dave82"]

Well i don't think that should work. By disabling a bone's animation will also disable it's children , so the only and best solution is to keep the bones enabledand  post-adjust them[/quote]

I'm glad you found a working solution. But I did want to mention that disabling a bone's animation *doesn't* disable the animation of it's children.[/quote]

[/quote]

You're right , but if i disable the animation fo the specific bone , i need an extra step to go into aiming pose as i need to rotate the disabled bones into the exact "holding the gun and pointing forward" angle , and then adjust it up or right. 
But it's good to know there are other solutions too... i really like how flexible and convenient this engine is , and the fact that i did more with it in two weeks than with irrlicht in 5 months :smiley:
I wish i had found it earlier...

-------------------------

GoogleBot42 | 2017-01-02 01:05:30 UTC | #6

[quote="Dave82"]i really like how flexible and convenient this engine is , and the fact that i did more with it in two weeks than with irrlicht in 5 months :smiley:
I wish i had found it earlier...[/quote]

 :laughing: Me too!  I am not sure why irrlicht is so popular for making games.  It is just a bare-bones renderer.  Its rendering pipeline is obsolete and there likely won't be plans to update it for a long time if at all...

-------------------------

