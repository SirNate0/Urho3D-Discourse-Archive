najak3d | 2022-02-05 05:00:35 UTC | #1

This is for very crude shadows, to improve on our current rendering of low-poly objects, onto a terrain not setup for shadows.   What we have is "good" for our app/context, but simply want to add the blob to help make the objects set on the ground look a little more realistic.

Here's a screenshot of our Urho App, showing 2 Tower icons sitting on the green terrain.   And so we want to add circular blobs around the base of each tower.   We'll have up to 2000 towers in the scene at once.    As far as blob shadows, we could just apply those to the towers close by, which will only be around 100 towers in close range max, at a time.

So we could have a pool of 100 blob shadows that get swapped to the closest 100 towers, and that would suffice.

Questions:
1. Is Decals the best easy way to do this?  Or should be consider another technique?

2. Can Decals be Pooled and re-positioned easily/efficiently?  Or is it better to destroy and re-create them?

![image|466x500](upload://4YEq7jzMemEHpPRDIMHM3zSEn44.png)

-------------------------

najak3d | 2022-02-05 07:31:37 UTC | #2

Update -  I tried POC for using Decals, and it won't work right now, getting this error:

"Can not add decal, target drawable has no CPU-side geometry data"

I'm dealing with custom/Dynamic Geometry (it's a high efficiency terrain).   I'm creating the Model, Adding Geometry to it, with "SetVertexBuffer()", and then attaching the model to the StaticModel, and setting up the Materials/Textures.   It renders just fine.   But it doesn't have "CPU-side geometry".   

**How does one "create CPU-side geometry" for a custom/dynamic StaticModel?**

Or - should I just implement my own version of Blob Shadows from scratch, doing something similar to blob shadows?

-------------------------

SirNate0 | 2022-02-05 13:31:44 UTC | #3

[quote="najak3d, post:2, topic:7186"]
**How does one “create CPU-side geometry” for a custom/dynamic StaticModel?**
[/quote]
`SetShadowed(true)` when you create the buffers.

[quote="najak3d, post:1, topic:7186"]
Is Decals the best easy way to do this? Or should be consider another technique?
[/quote]

I had a lot of trouble when I tried something similar with Decals, and I never figured out why. As such, I've switched to using a Billboard (I only have 1 shadow at a time following a character around, you could obviously use more than one). But if you already have it working decently, I wouldn't worry about switching.

-------------------------

