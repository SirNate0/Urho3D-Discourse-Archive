najak3d | 2021-03-12 02:37:30 UTC | #1

Just spent 5 hours debugging some weird "quirks" in my rendering, which looked more and more like my 0.000001 NearClip setting was behaving as 0.01 instead.   Well guess what?   The MIN value for NearClip is 0.01.   I never thought to check that this value was actually being set to my fully legitimate value of 0.00001, and so spent hours trying to figure out what I was messing up in my shaders or code.

In our Map application scene, since we show a World Map, it was very nice to have "1 Unit = 1 Degree" (which is about 60 miles!).    So our scene was just dealing mostly with small values, but the Unit size was meaningful for this context.    The world map was exactly 360 units (i.e. "degrees" wide).

The rest of our app already *thinks* in terms of "Degrees", so this really just made sense for us.

Unfortunately, though, 0.01 unit for us equates to about 3600 feet!   When in Ground Mode, that's where the 0.01 near plan clipping was horrid.... clipping everything closer than 3600 feet.   Ouch.  That's awful for a cockpit view.

I wish Urho hadn't implemented this unnecessary/arbitrary Minimum NearClip value.

As a result, we're forced to use a 100,000 conversion factor, so that 100,000 units is now 1 degree.  And to convert between Urho WorldSpace and the rest of our app, we now need to employ this conversion factor.   All because Urho decided to artificially limit our NearClip to 0.01 minimum.

Just airing a complaint.  And also hoping that maybe this post will help prevent others from running into this same issue.   And maybe this post might inspire Urho team to remove this Minimum (probably not, but worth a shot).

-------------------------

JTippetts1 | 2021-03-12 04:41:09 UTC | #2

The smaller you make nearClip_ the more problems you are likely to encounter regarding depth buffer precision. Using a very small nearClip_ is an excellent way to have Z-fighting.

-------------------------

najak3d | 2021-03-12 07:32:57 UTC | #3

Isn't it 100% about the ratio of FarClip / NearClip.   The way I understand it, if your Far/Near ratio is:
    1.0 / 0.001 = 1000 ratio

has the exact same Z-order precision/performance as:
   1000 / 1.0 = 1000 ratio

And so if my understanding is correct, then the 0.01 minimum clip distance would be an unnecessary restriction.

-------------------------

JTippetts1 | 2021-03-12 14:07:44 UTC | #4

Yes it is about the ratio. PRs are always welcomed, and it's a pretty trivial change to modify it locally yourself regardless.

-------------------------

najak3d | 2021-03-12 18:26:58 UTC | #5

Thanks for confirming what I thought might be true.  Our goal is to use only the released version of UrhoSharp / RbfxSharp.    More of us will be coming (Xamarin/.NET devs using Urho).

If they were to change the main branch code, IMO, they should change "nearClip = max(value, 0.01)" to something like "if (value == 0) value = 0.01;" as the safeguard... or throw an exception.   Then allow users to set their own ranges without limit (except for "0" which is never allowed).

For games/apps that think in "Globe space" (e.g. "earth"), it's very easy to think of all positions as "degrees".  And so your world's min/max 3D position values are all in the range of -180 to +180.... and close up, 0.02 is approximately 1 mile distance, and 0.000005 is about about 1 foot, and is a reasonable NearClip distance for ground-view for apps/games that work inside this Globe scale.

Because of the 0.01 min NearClip, we've altered our scale to 1 Degree = 100,000 units.    Now in debug mode when examining the Vector3 values, it's hard to tell the difference between 5 degrees and 50 degrees --   500000 vs 5000000.     Look too much alike, and have me counting digits constantly.

Or 10 degrees vs 100 degrees --  1000000 vs 10000000.

Not a huge issue, but still an issue that would have been avoided by removing the 0.01 limit on near clip.

-------------------------

