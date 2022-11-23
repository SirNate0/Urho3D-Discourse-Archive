evolgames | 2020-08-30 21:45:35 UTC | #1

I noticed something today in regards to raycasting. Here's why it came up:
I've been doing raycasting in a sniper game to both give the HUD the range of a target, and also to hitscan (I add delay and trajectory data to that to make it realistic).

So what happens is if I attempt multiple raycasts/frame, or even too many per couple frames, only the first one get registered. It will *do* the others, but they will return empty tables of results. The "results" won't be nil, though. This took a while to figure out but I've realized that I need to have gaps in between raycasts.
I'm not only doing RaycastSingle, but instead doing Raycast() to get a table of results and going through them, to make sure the distance of the target makes sense from where it is (i.e. if a bullet takes 3 seconds to get to it's target, and someone walks in between the raycast location and the target, the distance check will negate that).

I don't have an issue here, actually. It's wasteful to grab the range raycast every frame, and I'm doing 30 raycast checks from player to destination, spaced out by bullet travel time. So if there is a limit it doesn't matter here.

But just for future reference, is there a limit on raycasts per frame or per second? Or, do you think this is a hardware limitation? This is integrated graphics, btw.

-------------------------

