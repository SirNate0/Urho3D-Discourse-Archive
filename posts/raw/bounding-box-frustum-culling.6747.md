Athos | 2021-03-04 04:19:08 UTC | #1

Shadow flickering is occurring whenever the camera is looking exactly 90 degrees down at a shadow of an out of view object.

Which led me to this function:
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Math/Frustum.h#L154

Adding a break statement after the highlighted condition solved the problem.

But why there isn't a break statement after the condition there ? I mean if one plane is not outside, then it must be at least intersecting, right?

-------------------------

JSandusky | 2021-03-04 05:26:01 UTC | #2

I assume what you did is:

```
if (dist < -absDist)
    return OUTSIDE;
break; // this doesn't end up doing what you think it will

// and not something super terrible like:

if (dist < -absDist)
    break; // if did this, slap yourself
```

[quote="Athos, post:1, topic:6747"]
I mean if one plane is not outside, then it must be at least intersecting, right?
[/quote]

No. Because the entire box could be on the backside of 1 plane without any other corners on the backside of any other plane.

In that case the box would be out of view off to one side, or behind the nearplane, etc. Your change *fixes your problem* because you've broken the test to return false-positives very liberally, so virtually everything will pass containment tests.

---

Which type of light is having the shadow flicker? For instance directional light's have an extrusion (`GetShadowMaxExtrusion` `SetShadowMaxExtrusion`) move back the light from it's bounded fit so that offscreen things cast shadows. Default for that is 1000, if you're using a tiny unit (like 1.0 == 1cm) then you only have 10m of peeling back.

If other lights are doing it then there's a containment test problem somewhere either in selecting the light or selecting the shadowcasters to render (more likely the former). You'll have to step through passing and failing frames. I'd use Renderdoc to capture both cases to see what the shadowmap passes are doing (ie. are the shadowmaps differing between the two) first to make some determinations of where to go next.

---

If you need more help then post scene files or at least pictures so we can see what's going on.

-------------------------

Athos | 2021-03-04 14:33:21 UTC | #3

> I assume what you did is:
> 
> ```
> if (dist < -absDist)
>     return OUTSIDE;
> break; // this doesn't end up doing what you think it will
> ```
Yes.

> Which type of light is having the shadow flicker?

All light types.

> If other lights are doing it then there’s a containment test problem somewhere either in selecting the light or selecting the shadowcasters to render (more likely the former). You’ll have to step through passing and failing frames.

I've checked the frames and it seems the model is being culled.

> If you need more help then post scene files or at least pictures so we can see what’s going on.

Uploaded a short video:
[https://youtu.be/U9XF9XFV2TY](https://youtu.be/U9XF9XFV2TY)

-------------------------

Eugene | 2021-03-04 15:16:07 UTC | #4

Can you reproduce this bug on _unmodified_ Urho samples?
I'm 90% certain you messed up with scene setup.

-------------------------

Athos | 2021-03-04 16:54:10 UTC | #5

> Can you reproduce this bug on *unmodified* Urho samples?

Yes, sample 15-Navigation:
[https://youtu.be/Xv1-ghnCOm8](https://youtu.be/Xv1-ghnCOm8)

I used the 1.8 Alpha.

-------------------------

Eugene | 2021-03-04 21:33:33 UTC | #6

Oh shit. Thank you. I _think_ I saw this bug before and I investigated it. Lemme re-check.

-------------------------

Eugene | 2021-03-05 10:31:49 UTC | #7

Okay, I have good news.
This bug happens _only_ if you literally have just flat plane perpendicular to the look direction and nothing else.
The difference between minZ_ and maxZ_ is too small and something breaks.

Just do something like maxZ_ += 1 if minZ_ and maxZ_ are too close around here:
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/View.cpp#L952

The bad news is that I'm too lazy to commit this fix upstream. DIY if you wish.

-------------------------

Modanung | 2021-03-05 11:48:12 UTC | #8

Something like this?
```css
    if (Equals(minZ_, maxZ_))
        maxZ_ += 1.0f;
```
Seems to work.

-------------------------

Athos | 2021-03-04 23:19:32 UTC | #9

Flickering is gone.
Thank you.

-------------------------

JSandusky | 2021-03-05 03:49:52 UTC | #10

Floor it or use a large epsilon. The numeric_limits epsilon used in `Equals` is really tiny. I was still able to reproduce the flicker (less atrociously) using just `Equals`. Flooring or using `M_LARGE_EPSILON` both worked for me in the case where you nail your look angle to the floor and spin around until you get the flicker.

    if (Equals(Floor(minZ_), Floor(maxZ_)))
        maxZ_ += 1.0f;

-------------------------

Eugene | 2021-03-05 07:38:29 UTC | #11

[quote="JSandusky, post:10, topic:6747"]
The numeric_limits epsilon used in `Equals` is really tiny
[/quote]
It amazes me how many people use numeric_limits epsilon. Whereas I believe that if you use numeric_limits epsilon, you are doing something wrong. So far I have *never* encountered legitimate use of this constant, only mis-uses. Have you ever seen legitimate use?

-------------------------

Modanung | 2021-03-05 13:34:40 UTC | #12

How's this then?

```
if (Equals(minZ_, maxZ_, M_LARGE_EPSILON))
    maxZ_ += 1.0f;
```

```
template <class T> inline bool Equals(T lhs, T rhs, T margin = std::numeric_limits<T>::epsilon())
{ return lhs + margin >= rhs && lhs - margin <= rhs; }
```

-------------------------

JSandusky | 2021-03-05 19:04:46 UTC | #13

[quote="Eugene, post:11, topic:6747"]
Have you ever seen legitimate use?
[/quote]

Complete integration over every single possible value in a floating point range.

-------------------------

