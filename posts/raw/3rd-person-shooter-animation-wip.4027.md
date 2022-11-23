Lumak | 2018-02-17 23:56:56 UTC | #1

Animation is so hard. This sample set took me a week to do. This must be... hmm, my **nth** prototype but I think I finally got a game that I can make :wink:

https://youtu.be/jnPbmKX1d7g

-------------------------

Lumak | 2018-02-18 21:58:29 UTC | #2

To be fair, all animations that I stitched together are from Mixamo. And even then it still took me a week to map them onto my character, tweak, and combine into a set that you see in the vid. I still have a ton of tweaking to do, re-skin my char (and maybe my toon's underwear don't show when she jumps), create LOD, etc.

Not to promote anyone's site, but if you're a programmer and need some art, I got my toon from 3DRT.

-------------------------

burt | 2018-02-18 22:06:48 UTC | #3

Excellent piece of work! It looks very responsive and you did a great job with the animation layers. Congratulations!

-------------------------

Lumak | 2018-03-07 17:03:22 UTC | #4

Thanks for kind words, burt.

New vid, testing out vertical aim animation.

https://youtu.be/I45amgGjJf4

Significance of this animation is that it's driven by char's controls.pitch_ var. It's a layered anim with three frames, keys on arms, forearms, hands, and neck:
frame 0 - aim up
frame 1 - horizontal
frame 2 - aim down

**code:**
[code]
    animCtrl_->PlayExclusive("RifleAimLY.ani", 1, false);
    animCtrl_->SetSpeed("RifleAimLY.ani", 0.0f);

    float animLen = animCtrl_->GetLength("RifleAimLY.ani");
    float pitchInv = InverseLerp(-50.0f, 50.0f, controls_.pitch_);
    animCtrl_->SetTime("RifleAimLY.ani", animLen * pitchInv);
[/code]

-------------------------

Bluemoon | 2018-03-05 18:11:22 UTC | #5

Mehn!!! This is simply awesome :+1:

-------------------------

Lumak | 2018-03-06 20:04:12 UTC | #6

I'm glad to see that at least four people understand what it is to have *variable controlled animation*.

edit: other use cases:
- char look, left/right (similar to up/down, if you do both then one must become ADDITIVE)
- vehicle suspension, up/down
- vehicle steering (as in char's hands on the steering wheel), left/right.

-------------------------

yushli1 | 2018-03-07 03:10:53 UTC | #7

Do you have a demo so that we can take a look and try out? A repo would be great. Thank you for your nice work!

-------------------------

Lumak | 2018-03-07 16:35:05 UTC | #8

No demo or repo, just the video, description of the animation make up, and the code provided above. Should be easy to create your own animation sample to test.

-------------------------

