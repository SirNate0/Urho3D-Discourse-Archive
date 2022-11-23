nergal | 2017-11-29 09:53:33 UTC | #1

I've set SetOcclude(true) and SetOccluder(true) on my objects since they can be both. Is there a way to see that it actually works? Somehow debug the occlusion?

Using the Debug HUD (SHOW_STATS) it just shows number of occluders visible. And SHOW_ALL doesn't really give me the answer?

It would be nice to draw like a box or line where the occlusion occurs so that I can see that it happens. Right now I'm not really sure it happens since my triangle count seems pretty much the same.

-------------------------

Modanung | 2017-11-29 10:48:20 UTC | #2

Using `Camera::SetFillMode(FILL_WIREFRAME)` you can see through your occluders. Would that be enough?

-------------------------

nergal | 2017-11-29 10:51:16 UTC | #3

No, it doesn't really help, or perhaps it did. Because I can still see my other objects behind the in-front-objects. So I guess my occluding is not working? 

I guess it's possible for an object (custom geometry) to be both occluder and occludee, right?

-------------------------

nergal | 2017-11-29 14:57:15 UTC | #4

I doubt that my occlusion works. I've tested to use OcclusionBuffer() manually without success. I just don't get it. What's supposed to be needed to make things work. An occlusion example would be great! :slight_smile:

-------------------------

