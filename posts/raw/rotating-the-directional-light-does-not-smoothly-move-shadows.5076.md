Giacom | 2019-04-04 19:58:07 UTC | #1

Hi, I've been experimenting with the engine for a few days now and I wanted to try creating a scene with a rotating skybox and sun.

I've set the scene up in the editor so that the directional light has a Rotator.as script which rotates and moves all the lighting and shadows with it.

I then noticed that the shadows do not move smoothly, which you can see here:

https://gfycat.com/ShamelessSolidAiredale

I tried messing around with many shadow related settings on the light and subsystems themselves but I couldn't figureit out and I don't know much about cascaded shadowmaps to tell what the problem is.

-------------------------

Leith | 2019-04-05 02:23:28 UTC | #2

The relative scale of the shadowcaster and shadow receiver can be a cause for inaccuracy when using shadowmaps - I'd start by making the ground plane mesh a lot smaller, and see if that improves the shadow quality - if you need your groundplane to be really big, then use several smaller ones (which is good for frustum and occlusion culling), or alternatively, import a ground mesh with a higher degree of tesselation / more vertices than just the four corners (not good for culling purposes, but should still improve shadow quality).

-------------------------

Giacom | 2019-04-05 12:23:46 UTC | #3

Thanks for the help. I was able to get the shadows working by replacing the floor and wall with more complex models. I replaced the floor with a Terrain heightmap and the wall with a teapot model from the built in assets. The shadows are moving much smoother now though I do get some artifacts on the shadows if I start looking upwards, not sure why.

https://gfycat.com/likablelinedbass

(If you focus on the shadows in the video, you can see it lose quality when I look up)

I also noticed that Terrain causes a lot of batches, in the batch counter, is that normal because I thought it would all be mostly batched together.

**Edit:** I was able to fix the artifacts on the shadows by tweaking the CSM splits in the Directional Light. 50 / 2000 / 0 is what I'm currently using, for anyone else who needs help with this.

-------------------------

Leith | 2019-04-06 10:42:30 UTC | #4

Typically, the terrain object internally cuts up your surface into terrain patches - smaller objects, as I hinted, are good for culling purposes, as well as avoiding numerical precision issues in shaders. One downside of chopping up geometry into smaller pieces, is that it will affect batching, unless the renderer is clever enough to use render buckets to catch piecemeal the results from high level rendering objects. It appears that Urho may have some room for improvement in terms of batching, but I am no expert in Urho, I speak from experience across a bunch of engines, and noting that the batch count went up, and all the low level renderables share the same properties, I am stating that we could probably do better on the batch count.

-------------------------

I3DB | 2019-04-06 15:07:37 UTC | #5

Everyone struggles with shadows it seems ..

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/2/2e9913efc2760c38fc7e453dbefdfb4590f902c9.jpeg'>

Can't get them working on hololens at all, some issue with the uwp implementation in urhosharp.

-------------------------

Leith | 2019-04-07 03:23:37 UTC | #6

Unfortunately, the consensus on this forum appears to be that "we don't answer questions relating to UrhoSharp - they have their own forum."

Hint: If you can reproduce the issue using Urho3D, and using the master branch on github, you're more likely to receive help, because that makes it a core issue, and not an issue in the Sharp Wrapper.

-------------------------

