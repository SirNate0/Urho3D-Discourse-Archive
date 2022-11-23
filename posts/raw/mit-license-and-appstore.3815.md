f1af | 2017-12-02 20:02:48 UTC | #1

I want use Urho3D for game project, for sell on AppStore. But my employer told my, that Urho3D has ThirdParty libraryes, and this libraries have a different licenses, differ than MIT (like a BSD license, lgpl and e.t.c.) and emplayer told me, that is reason for write new little engine, withot non-MIT dependencies.

So.. my employer - is right or not?

I have some risk, if I will make application based on Urho3D, and sell on AppStore - do I will have a some problem about legal (copyright) my application?

-------------------------

Eugene | 2017-12-02 20:52:23 UTC | #2

[quote="f1af, post:1, topic:3815"]
like a BSD license, lgpl and e.t.c.
[/quote]
Please list licences that you are afraid of.
The worst thing you would ever have to do is to place _somewhere_ some text about licenses of used BSD libraries.

-------------------------

weitjong | 2017-12-03 04:59:05 UTC | #3

As far as I understand our 3rd dependencies are all having permissive licenses, or they wouldn't be accepted in the first place to be included in our repository.
https://urho3d.github.io/documentation/HEAD/_contribution_checklist.html#ContributionThirdParty
https://github.com/urho3d/Urho3D/blob/master/Source/ThirdParty/LICENSES

Disclaimer: IANAL, this is not a legal advice, check with your own company legal department.

-------------------------

Modanung | 2017-12-03 09:27:57 UTC | #4

You can tell your employer not to worry. As @weitjong mentioned, all third party libraries have licenses that are (at least) compatible with Urho's MIT license. If your employer can point out a library where this is not the case, it'll probably be removed/replaced pretty fast.

-----
I too am no lawyer.

-------------------------

