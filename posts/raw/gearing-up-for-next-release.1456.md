cadaver | 2017-01-02 01:07:50 UTC | #1

I believe soon would be time to release Urho3D again. Will move to the major.minor.patch formatting style (though we probably do not obey the incrementing rules strictly) so it will be called 1.5.0, considering there are new subsystems (Database & Localization.)

The major thing I want to solve before releasing is [github.com/urho3d/Urho3D/issues/954](https://github.com/urho3d/Urho3D/issues/954) (if there is a better resolution to that one, otherwise it can just be re-closed) would be good to be resolved beforehand.

-------------------------

yushli | 2017-01-02 01:07:50 UTC | #2

It is great to have a new release with some many things added. 
[github.com/urho3d/Urho3D/issues/993](https://github.com/urho3d/Urho3D/issues/993)
should also be investigated/fixed since heXon is a nice demo to show off Urho3D's capabilities. 

Look forward for the next release!

-------------------------

cadaver | 2017-01-02 01:07:50 UTC | #3

I was not able to reproduce that bug. If ParticleEffect was null, the emitter would not update either.

-------------------------

weitjong | 2017-01-02 01:07:50 UTC | #4

I will reclose [github.com/urho3d/Urho3D/issues/954](https://github.com/urho3d/Urho3D/issues/954) soon. As the number of functions that need the function attribute to work correctly in higher optimization level increases, due to function inlining of the Matrix or Quaternion class into outer functions, using the local function attribute approach becomes less and less attractive compared to global stackrealign approach. I will make my final assessment to decide whether to commit my changes to use function attribute or not. Regardless, I have already submitting a few commits related to MinGW build as the result of my experimentation with MinGW build, so the experiment has achieved something good.

-------------------------

codingmonkey | 2017-01-02 01:07:50 UTC | #5

It's will be great if new release come with:
 
1. RenderPath animation abilities:
for animating:
-tags (on/off blocks during runtime by established animation)
-shader params (change values for values during runtime by established animation)
-animation events (send events from RP by established animation) 
all things that have animatable class

2. Also maybe some kind functionality of conditional renderer: For automatically on/off the renderPath's tags (RP-blocks), if renderer no seeing any objects with materials that using these RP-blocks.

3. Introduced binary file format for Object Animation and Value Animation

-------------------------

cadaver | 2017-01-02 01:07:50 UTC | #6

I don't think we're adding significant new features at this point, that is not the point of this thread.

-------------------------

thebluefish | 2017-01-02 01:07:51 UTC | #7

Glad to see that I'm not going to be on (potentially) unstable branch just to get certain features working  :laughing: 

As always, great work!

-------------------------

Lumak | 2017-01-02 01:07:52 UTC | #8

[quote]I believe soon would be time to release Urho3D again. Will move to the major.minor.patch formatting style (though we probably do not obey the incrementing rules strictly) so it will be called 1.5.0[/quote]

This upcoming version breaks backward compatibility with 1.4 and that's a major change, so it should be a major version change to 2.0.

I've only been here since Aug/2015 since 1.4, but does every new revision break backward compatibility to the previous?

-------------------------

cadaver | 2017-01-02 01:07:52 UTC | #9

Yes, they pretty much do. That's why I explained that we wouldn't be using semantic versioning in a "strict" manner. However, mostly they're on the level of search-and-replace changes. I would only increment the major number in case of actual major API redesign. Something similar can be seen in Ogre, for example 1.8 -> 1.9 required you to instantiate various subsystems manually, as they were no longer automatically created, yet they only bumped the minor version number.

EDIT: thinking a bit, since the versioning scheme is admittedly somewhat custom, it may be better to go with 1.5 instead of 1.5.0. However decimal formatting like 1.51 will no longer bet used, so if a "patched" version of 1.5 would be necessary in the future, it would be called 1.5.1. Opinions?

-------------------------

yushli | 2017-01-02 01:07:52 UTC | #10

I think it is fine to go with 1.5 instead of 1.5.0?

-------------------------

Lumak | 2017-01-02 01:07:53 UTC | #11

I have no preference.

-------------------------

Enhex | 2017-01-02 01:07:53 UTC | #12

[quote="yushli"]I think it is fine to go with 1.5 instead of 1.5.0?[/quote]
It isn't a decimal number, and writing major.minorpatch will cause collisions with major.minor values.
For example:

1.0
1.1
1.11 <- patch represented as "decimal"
1.2
...
1.9
1.10
1.11 <- collision with actual minor version


(unless you just suggesting to omit the last .0)

-------------------------

yushli | 2017-01-02 01:07:53 UTC | #13

yes just omit the last .0.  the next would be 1.5.1, 1.5.2 etc.
1.5 looks more elegant than 1.5.0 to me.

-------------------------

cadaver | 2017-01-02 01:07:54 UTC | #14

We potentially have to retroactively rename those old tags like 1.31 to 1.3.1, when/if we get to that minor version range.

-------------------------

cadaver | 2017-01-02 01:07:54 UTC | #15

When morph targets are used for a skinned mesh, the positions/normals/tangents can be supplied by a per-instance morph buffer, while UVs and blending data still comes from the original. Instancing is also another case where the instance transforms are supplied by another buffer. In practice, for just a static model, I wouldn't use multiple buffers.

-------------------------

Dave82 | 2017-01-02 01:08:00 UTC | #16

Just an idea that's too small to post in feature request but it would be useful :
A speed param in AnimationController's Play() and PlayExclusive() function.
I mean we have to set the speed anyway after calling these functions , so why not do it in one call ?

-------------------------

cadaver | 2017-01-02 01:08:02 UTC | #17

Adding the speed parameter would make it impossible to *not* set a speed upon playback though, unless there were overloads, so I'd prefer keeping it separate. There are also a lot of other parameters (startbone etc.) that require a separate call.

-------------------------

