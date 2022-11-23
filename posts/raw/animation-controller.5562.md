Askhento | 2019-09-10 20:48:08 UTC | #1

Hello guys, I have a quick question about AnimationController class. I understand some of the features in it and I am able to run looping animation with Play/PlayExclusive method. And for some reason I need to pause the animation, but when I call Stop it resets to the beginning!  Is there any clever way to pause the animation?

Thanks for read this)

-------------------------

Modanung | 2019-09-10 21:37:22 UTC | #2

I assume you could simply set its speed to `0.0f`. :thinking:

-------------------------

Askhento | 2019-09-10 21:38:17 UTC | #3

You are a MAGICIAN! 
Thank you!

-------------------------

Modanung | 2019-09-10 21:42:04 UTC | #4

 ![Dark wizard](https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia1.tenor.com%2Fimages%2F57d10503a586d4084e35826524fc05a8%2Ftenor.gif%3Fitemid%3D10456531&f=1&nofb=1)

-------------------------

Leith | 2019-09-11 05:45:16 UTC | #5

Don't use speed - use Weight.
A weight of zero means animation will have no effect, so we don't bother to calculate for it.
A speed of zero means we do all the same calculations based on the same time, every frame.
Pretty sure animation controller does NOT check for zero time.

-------------------------

Askhento | 2019-09-11 07:56:46 UTC | #6

Wow this one is more like BLACK MAGIC haha!

-------------------------

Modanung | 2019-09-11 09:49:36 UTC | #7

Magic is the grey area. :wink:

-------------------------

Modanung | 2019-09-11 10:51:33 UTC | #8

@Leith But I recon with a weight of zero the animation _would_ still progress. Also the pose would not be displayed when the weight is set to zero, which does not seem like @Askhento's desired behaviour.

-------------------------

Leith | 2019-09-11 13:12:22 UTC | #9

There's code that checks for zero weight, an early out, which is not so for zero time, from what I saw... it's used to stop interpolation when we blend weights, but basically, if weight hits zero, that part of the animation data is no longer considered - time on the other hand, matters not, it seems, to the animation system, it simply infers that the next frame is the current frame, and goes through all the effort to try to interpolate between now, and now, for no raison.

-------------------------

