CG-SS | 2019-04-29 22:16:03 UTC | #1

Did someone ever try to create a WebView UI element for Urho3D? I ask because that's something I'm thinking about doing, and I'm just checking if someone already tried so then I could continue their work.

I think it would be a good addition to the UI toolbox since sometimes you're just lazy and want to show a link to your game's wikipedia page instead of putting all the info in the game itself.

-------------------------

jmiller | 2019-04-30 01:02:15 UTC | #2

Welcome to the forum! :confetti_ball:

  https://discourse.urho3d.io/t/cef3-web-browser-integration/993

[quote="Pencheff, post:104, topic:2431"]
Another CEF UI integration:
I can share most part this implementation later
[/quote]

...and there are a few other [CEF-related posts](https://discourse.urho3d.io/search?q=CEF) .

Presumably, other frameworks like Dillo (GPL) et.al. can be integrated similarly (**edit**: though for merging to master, GPL not quite suitable) -- lighter, faster, less deps, different..

-------------------------

CG-SS | 2019-04-30 00:51:35 UTC | #3

Thank you for your reply!

I thought about CEF, but does it works on ARM? Because I believe my contribution won't be merged on Urho3D' master branch if it doesn't work on mobile.

-------------------------

jmiller | 2019-04-30 01:20:16 UTC | #4

Probably someone will know.. It seems that question is where this thread left off (and here we are welcome to continue relevant threads even if older; it may also notify more interested parties):
  https://discourse.urho3d.io/t/cef3-web-browser-integration/993/24

-------------------------

S.L.C | 2019-04-30 02:06:59 UTC | #5

I'm pretty sure that your contribution won't be merged on Urho3D master branch. But not for the reasons you stated. It will not be merged because most people don't need WebView functionality in their games. Most games don't. Therefore, you will be instructed to maintain the component separately and will be linked to it for whoever needs it. I mean... isn't that the purpose of a component based implementation?

And let's be honest, the build-system and third-party folder are already bloated as they are. Dropping CEF in there would simply be unnecessary.

That being said, I'm not saying you're not welcomed to do this. I'm just saying that your expectations might not align with the expectations people have from this engine.

-------------------------

Pencheff | 2019-04-30 09:09:36 UTC | #6

CEF3 works on ARM devices, seen it running on Raspberry Pi, however it doesn't run on Android/IOS and there seems to be no plans to support that. BTW Atomic has a good CEF3 implementation that can be used in Urho3D just by copy-pasting it as a subsystem (and maybe change the namespace), so it could be a good starting point. 

I also can agree with @S.L.C, dropping CEF as dependency for Urho3D is not good, the main libcef.so is ~400MB on linux, 200MB on windows. A separate implementation would be much more easy to use. I'm willing to drop my ideas and help, I spent some good amount of time making my integration as stable and super fast. There are some tricks to make it even faster - using the texture from CEF directly, so you get almost native speed.

-------------------------

CG-SS | 2019-04-30 13:55:59 UTC | #7

I see. Thanks y'all for your pointers! 

I might look into GeckoView, since I wanna support for Android (for handling micro-transactions on webpay). And why not make an Urho3D-extra module repo for things like this? Kinda like OpenCV.

-------------------------

