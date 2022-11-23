Lumak | 2017-01-02 01:12:10 UTC | #1

[url=https://www.mixamo.com/]Mixamo[/url] [url=https://www.mixamo.com/pricing]Pricing[/url]

[quote]
[b]For a limited time, get all these goodies for free with an Adobe ID.[/b]
Adobe Fuse CC (Preview) 	The application is free
Auto-Rigger (Preview) 	Auto-Rigs are free
3D Animations (Preview) 	All animations are free
3D Characters (Preview) 	All characters are free
[/quote]

If anyone is interested.

-------------------------

rku | 2017-01-02 01:12:10 UTC | #2

Added to my account all of the anims and characters using script so i legally own them. Downloaded them from mega as someone shared link on reddit. Its good stuff. Characters are great placeholders. Just not sure about Fuse. I got it installed but it does not show anywhere that i own it permanently or something. So my fear is that to use Fuse we will be forced into subscription model. Doh.

-------------------------

Lumak | 2017-01-02 01:12:11 UTC | #3

I didn't use Fuse but downloaded animations and character models in .fbx format directly.   But I think you're right that Fuse might be a service that you'll pay for eventually.

-------------------------

rku | 2017-01-02 01:12:53 UTC | #4

Did you try mixamo characters/animations? I got character and animation separately. Ideally i would like to apply multiple animations on character and blend them but somehow applying animation does not really work. I wonder if i am missing something obvious here..

-------------------------

Lumak | 2017-01-02 01:12:53 UTC | #5

I downloaded several animation packs and doing a rough count, I have something like 230 animations and about 10 chars. I did try a few animations and they looked good.

-------------------------

rku | 2017-01-02 01:12:53 UTC | #6

I mean did you try them in urho? Because i somehow fail to get them working.

-------------------------

Lumak | 2017-01-02 01:12:53 UTC | #7

I tried them in urho and they worked, but I retarget the animations to my own rig first though.

I opened a few model files in Maya and saw that the base models have transforms at the end of joints, like HeadEnd, etc, and the animation files have locators.  I find it odd that they didn't keep the two consistent.

It might help if you use a [b][color=#0000FF]-s[/color][/b] option w/o any filter in assetimporter to export non-skinning bones.  And the [b][color=#0000FF]dump[/color][/b] option to compare the model's and animation's bone names.

-------------------------

rku | 2017-01-02 01:12:54 UTC | #8

That clears things up. Hows retargeting done? In external tool or some child-parent magic in code? Not exactly sure what i should look for.

-------------------------

Lumak | 2017-01-02 01:12:55 UTC | #9

I retarget my animations in Maya, but I know that Unreal has an animation retargetting utility. I only read about it but never used it, so I'm not sure if it's part of the editor or where it is.  I haven't checked to see if Unity or Cryengine have it.

-------------------------

