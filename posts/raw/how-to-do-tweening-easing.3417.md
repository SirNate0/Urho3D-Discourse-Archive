russ | 2017-08-04 05:35:46 UTC | #1

I'm porting a 2D game from Javascript, and it uses the standard Penner easing functions to do animations: http://easings.net/.  Is there any equivalent in Urho3D?  I've looked at ValueAnimation, and I see it allows for keyframes and some sort of spline tension mechanism, but I'm not sure how to map that to the basic tweens I'm used to.  

Does anyone have any experience with this?  Thanks.

-------------------------

jmiller | 2017-08-12 15:34:56 UTC | #2

Hi russ,

Have you seen the animation sample 30_LightAnimation ?

-------------------------

russ | 2017-08-18 00:58:32 UTC | #3

Thanks carnalis, I've taken a look at the sample and it helps some.  I should have some time to play around with it this weekend, I'll update this thread if I find a nice way to map the concept of Penner easing onto the Urho animation system.

-------------------------

