burt | 2018-11-10 08:49:23 UTC | #1

I'm trying to apply an effect on my camera over time. In Unity, coroutines are often used for this. How would one do this in Urho?

https://www.youtube.com/watch?v=9A9yj8KnM8c

-------------------------

Sinoid | 2018-11-10 02:47:20 UTC | #2

@Urho3D @weitjong can we get a sticky for script requests and github-gists for *pot-shots* like this?

---

@burt you can do this with a script attached to the node you want to manipulate. They get a `FixedUpdate` call and you can interpolate during that.

Do you need an example? In Lua or Angelscript?

-------------------------

weitjong | 2018-11-10 05:45:02 UTC | #3

[quote="Sinoid, post:2, topic:4664"]
@Urho3D @weitjong can we get a sticky for script requests and github-gists for *pot-shots* like this?
[/quote]

I believe any of the moderators in the forum have the privilege to do that. We have more moderators than admins. However, we have reached the quota and cannot include more. Let's see how this thread goes first before making it sticky.

-------------------------

Modanung | 2018-11-10 08:56:32 UTC | #4

What I'd do is subclass `LogicComponent` to create a custom camera component with support for shaking. The shaking itself could be handled during the `Update` of this component or as a `ValueAnimation` that the component adds to some offset child node.

-------------------------

Sinoid | 2018-11-11 18:28:58 UTC | #5

Here's an angelscript gist of the basic behviour:

https://gist.github.com/JSandusky/1dfe49a2fcf600f667f96f3338ddfcfb

I don't really think that's good enough to use out of the box. Requires some tuning and it's really way too smooth - part of that is due to how I did the blending over time.

For serious use I'd fix the blending and enforce a minimum distance between the random shake vectors (I'd just dot-prod them and add a threshold variable).

Edit: I deliberately called this *Shake* and not *CameraShake* because with a couple of tweaks it should be able to take care of your recoil post as well.

-------------------------

Sinoid | 2018-11-10 21:18:26 UTC | #6

@weitjong I agree after the fact, I'll toss of up a `ScriptLibrary` repo with a dump of misc helper scripts.

-------------------------

burt | 2018-11-11 18:31:17 UTC | #7

Thanks a lot for such a detailed and thoughtful response! :star_struck:

Is the interval based on the amount of internal engine "ticks"? Is it framerate independent?

-------------------------

Sinoid | 2018-11-11 19:27:43 UTC | #8

The smoothing is framerate dependent, otherwise it's all tied to time-deltas, so engine-ticks don't really effect much.

The **interval** is a time-window, it's basically the time between shakes. So a bunch of intervals means a lot of shakes, where as just a few intervals means very few. 

For the duration of the interval the camera will interpolate towards the shake the target direction. A lot of control could be had on using some basic easing functions on the `weight` variable, such as a bounce-out easing to make it oscillate towards the end of each shake.

That'd be as easy as `weight = MyEasingFunction(weight);`

When the interval ends, if it's not the end of the shake the next interval's shake target direction will be determined. If the `returnToRef` switch is enabled then once out of intervals the camera will return to its original (parent relative) orientation. The parent-relative bit is important, as otherwise you'd have issues like a head/gun-holding-wrist pointing in bizarre locations if the whole orientation of the object changed.

Note: I fixed a null access in there (when removing self), the gist is updated for that.

-------------------------

