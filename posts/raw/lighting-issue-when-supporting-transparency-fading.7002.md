daokoder | 2021-09-25 08:58:49 UTC | #1

I am trying to implement a fading effect by increasing material transparency. I duplicated the DiffAlpha technique, and changed depth write from false to true. Now the object fades properly, but its lighting seems gone, and become dimmed.

![Urho3D_IssueReport_Screenshot|640x480](upload://rTdcfAk0lQArVlMpVQ9KOoI38lX.png)

I tried to add additional passes, but I can only get either lighting properly or fading properly, never both. Any suggestions?

-------------------------

SirNate0 | 2021-09-25 11:30:14 UTC | #2

You have a second transparent object, right, a large plane or something? It's possible that the plane is "in front" of the box based on your image (it's based only on the center coordinates of the object) which could make it look weird. To check, I'd suggest disabling every other transparent object and see if it gets better, as this may not in fact be your problem at all.

If it is your problem, though, you could try adjusting the render order if the box is always going to be in front.

-------------------------

daokoder | 2021-09-25 11:45:09 UTC | #3

Right, there was a second transparent object which normally was used to highlight the block (and its neighbors) below. In certain condition, it would become fully transparent. But due to some recent changes, it didn't become fully transparent.

Just now I disabled this transparent object completely, but the issue remains. I will try to adjust the render order as you suggested, and see how it works.

-------------------------

SirNate0 | 2021-09-25 13:17:25 UTC | #4

If you disabled it completely and it didn't fix it your problem must be something else, so hopefully someone else has some idea what is going on.

-------------------------

daokoder | 2021-09-25 14:15:47 UTC | #5

Yes, it must be something else. Since it looks like a lighting issue, I tried to change the light mode of the alpha pass to per pixel ( the default is per vertex), then the lighting seemed better, but the fading was broken (the object became always transparent, just like before without changing depth write to true). Very strange.

-------------------------

PsychoCircuitry | 2021-09-26 12:59:04 UTC | #6

This does seem odd from your screenshot for sure. I spent a few minutes trying to reproduce it, and couldn't. I got other anomalies with hardware depth texture, but not like what I'm seeing in your pics. I created a new technique from DiffAlpha with depth writing on, and used a value animation on MatDiffColor, fading alpha channel from 0 to 1 and back. Lighting was correct, alpha fading was correct. I checked both forward and deferred render paths with hardware depth texture and without. I didn't mess around too much to try to figure out what wasn't working right on the hardware depth, but lighting and fading were both working correctly on all tests. Any significant deviations from the provided render paths? Adjusting MatDiffColor to handle the opacity change? No other ideas at the moment.

-PsychoCircuitry

-------------------------

daokoder | 2021-09-26 02:52:42 UTC | #7

@PsychoCircuitry Thank you for testing it. I did exactly the same thing. Since it works for you, I will check if it is a problem of my Urho3D fork. Maybe it has something to do with my changes to the fork, or simply because my fork is outdated.

-------------------------

daokoder | 2021-09-26 03:49:39 UTC | #8

Just checked by modifying the material animation sample, the fading and lighting works properly with the revision on which my fork was based. So it must have something to do with my changes. Now knowing where to look for the problem should make it easier.

-------------------------

daokoder | 2021-09-26 12:59:04 UTC | #9

Now the issue is solved. It turned out the technique file had a couple of additional changes that I made some time ago for another effect. I mistook those changes as part of the original file. After removing those changes, the lighting issue is gone.

-------------------------

George1 | 2021-10-01 07:33:56 UTC | #10

Could you post the final image?

-------------------------

daokoder | 2021-10-02 14:36:52 UTC | #11

Sure.

High transparency:
![Screen Shot 2021-10-02 at 10.25.15 PM|690x388](upload://9C4qhPbNnWZjgylyAzo8WjUNYzD.jpeg)

Low transparency:
![Screen Shot 2021-10-02 at 10.17.25 PM|690x388](upload://3uwrvM7P0g54Pgu5LtoNOVUA1OM.jpeg)

-------------------------

