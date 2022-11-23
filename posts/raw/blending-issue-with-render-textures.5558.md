MystMagus | 2019-09-13 13:44:19 UTC | #1

I've been having an issue with blending for UI when rendered to a texture to include in the scene. See this issue: https://github.com/urho3d/Urho3D/issues/2500

I've made sure that it wasn't something I introduced myself with local changes to the engine (unless I really messed up), and I've run out of ideas for how to solve it. I've tried changing around the blend modes and while it can have some effect none of them seem to result in the right appearance. I've also tried making sure that blending actually is on, and separating the batches for different elements, but no luck. Does anyone else have any ideas or experience on this topic?

-------------------------

MystMagus | 2019-09-13 13:43:19 UTC | #2

It seems like this issue isn't limited to only UI, but at least to Urho2D as well. I updated the linked issue with a better example app. I really would like for some other people to check on this as well (especially would like to hear from a native windows user to see if it happens with directx as well). As mentioned, I have no ideas on how to solve this.

-------------------------

Modanung | 2019-09-13 17:15:05 UTC | #3

Have you tried updating your drivers or even using an older version of them?

-------------------------

MystMagus | 2019-09-13 21:18:51 UTC | #4

Just tried updating to the most recent driver (was close to it before), but it made no difference. Are you saying that the issue doesn't occur for you in the test case I provided? If so I suppose I can try downgrading as well, but it's just a GeForce GTX 1060 nothing strange. I'm running Ubuntu 18.04.3 LTS.

Ed.: I built a native file and a cross compiled exe if it helps: https://www.dropbox.com/s/1r38z1dcc1y0n71/test.zip?dl=1 (the middle square should be gray, but is green; pressing space changes from rendering to texture to rendering directly)

-------------------------

Modanung | 2019-09-13 22:16:05 UTC | #5

Indeed the square starts out green. I'm afraid it's reproductive. (on Linux Mint 19)

[quote="MystMagus, post:4, topic:5558"]
Just tried updating to the most recent driver (was close to it before), but it made no difference. Are you saying that the issue doesn’t occur for you in the test case I provided?
[/quote]

I ran into a [UI render glitch](https://github.com/urho3d/Urho3D/issues/2367) that seems to have vanished, but I guess it's unrelated.

-------------------------

