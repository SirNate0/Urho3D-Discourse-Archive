JTippetts | 2019-02-16 15:45:14 UTC | #1

I have just completed (as much as I have time for, at any rate) a submission for the [gamedev.net Dungeon Crawl Challenge](https://www.gamedev.net/blogs/entry/2266345-survive-loot-and-discover-its-time-for-the-dungeon-crawler-challenge/) which has been running for the last 2 months and ends today. My entry is an [ARPG](https://www.gamedev.net/projects/1160-dungeonbot3000/) Diablo/Path of Exile-alike. A couple work-in-progress videos:
https://youtu.be/IkxWX4bCBPM
https://www.youtube.com/watch?v=q8kAMZEEg9I

I ran out of time to do everything I wanted to do, but it's still pretty functional. 10 randomly generated dungeon levels, with a dual boss fight at the end level. Randomly generated dropped loot in traditional Diablo-clone style, with random modifiers. 2 skills: a Spin Attack (like Diablo's Whirlwind) and a channeled Laser Beam attack. Random enemy modifiers such as Berserk, Reflect Damage, etc... It's pretty standard ARPG fare, and you can tell I've been playing a lot of Path of Exile lately.

Anyway, if you want to check it out you can download it [here.](https://www.gamedev.net/projects/1160-dungeonbot3000/) There is also a github source link; pardon the messiness, it was a rushed challenge entry after all. I didn't get as much time in the last 2 months to work on it as I wanted, so some stuff is pretty hacky, and the UI is almost non-existent.

It's written using Urho3D (of course), OpenGL back-end. There are almost certainly bugs. I would like to take the framework of it, and maybe turn it into something real someday.

-------------------------

smellymumbler | 2019-02-17 04:52:05 UTC | #2

Love the HP HUD. Really cool.

-------------------------

Modanung | 2019-02-17 06:19:04 UTC | #3

Indeed. And it seems to be based on the work in [this thread](https://discourse.urho3d.io/t/custom-ui-mesh-source/4244)?

-------------------------

JTippetts | 2019-02-17 15:58:30 UTC | #4

That thread was based on [my original thread](https://discourse.urho3d.io/t/diablo-3-resource-bubbles/3534) implementing the trick from [simonschreibt.de](https://simonschreibt.de/gat/diablo-3-resource-bubbles/). I actually missed Lumak's work, though, so I might need to take a look at it since he probably improved it. My version still doesn't handle transparency, hence the ugly thick ring around the bubble.

Edit:  Yeah, he really did improve it. Gonna grab his code.

-------------------------

Modanung | 2019-02-17 17:44:06 UTC | #5

Ah right that's the thread I was looking for. Good thing I found and mentioned  the other one then. :slight_smile:

-------------------------

JTippetts | 2019-02-17 17:45:42 UTC | #6

Yeah, it is. I wonder if @Lumak has thought about making a PR for his stuff. Would be pretty handy to have that in upstream, since health bubbles aren't the only place you might want to have a custom shader effect in UI.

-------------------------

JTippetts | 2019-02-17 21:35:12 UTC | #7

Looks like it needs to be updated a bit. Not really working with current head.

-------------------------

