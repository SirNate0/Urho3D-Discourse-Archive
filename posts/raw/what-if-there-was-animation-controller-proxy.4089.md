Lumak | 2018-03-15 02:07:35 UTC | #1

Just another one of those processes that I was curious about and wanted to see if it made any difference to create an animation controller proxy for all other characters to use the same animation.

**Tested with 400 characters.**
**Release build:**
w/o proxy
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/8/8080724b76d1b3dade99474919982142fd67f7b8.png[/img]

w/ proxy
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/5/5d8afe793b1a56225de5740326297a46d0dcd500.png[/img]

**Debug build:**
w/o proxy
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/a/a127984ce9d56265c734030a9418b47e50a9be6d.png[/img]

w/ proxy
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/8/82653c70fdec0083d0c3b0708753a1f9fd43f4d0.png[/img]

Makes a slight difference in Release and more significant in Debug.  Any thoughts?

-------------------------

Lumak | 2018-03-15 02:35:36 UTC | #2

I can conclude that the animation system is pretty optimized and there's no need to create a proxy controller, even if you have a ton of chars in the scene.

-------------------------

weitjong | 2018-03-15 08:08:32 UTC | #3

Have you disabled the max frame limit in your tests?

-------------------------

johnnycable | 2018-03-15 08:42:10 UTC | #4

What of those number shall I check exactly? Update Avg?

-------------------------

Lumak | 2018-03-15 20:55:14 UTC | #5

Thanks, weitjong. I didn't expect "no limit" would make a difference since the char animation control update is in physics fixed update cycle but, wow, a huge difference. I'm not going to repost pics of every setup but the release build ran at around 470 fps for both conditions and 210 for debug - both conditions. 
Our current character demo calls animation update every frame, e.g. PlayExclusive() update of Idle anim. And by removing that call, the release frame rate shot up to 470, dbg frame rate shot up to ~210.

johnnycable, you want to look at sceneupdate and physicsupdate.

Frame capture of debug, non-proxy animation, no constant call to PlayExclusive() in physics fixed update.
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/d/dee05cb7556359044e73f03732e09cf67b9fff18.png[/img]

-------------------------

Lumak | 2018-03-15 21:23:58 UTC | #6

So, my conclusion still remains the same, animation system is pretty optimized and using a proxy animation controller will not boost performance.
For a large body count, however, you should look into (some things I can think of):
* lod geom
* lod shadows
* lod animation - *err, this feature is there but not sure if it'll help much because of how optimized anim system is.
* limit draw distance

-------------------------

Sinoid | 2018-03-16 00:54:38 UTC | #7

> For a large body count, however, you should look into (some things I can think of):

Other than LOD, time would be better spent on more aggressive batching and applying AZDO principles to instance the characters. On DX11 that scene can get chopped down to < 15 draw calls with minimal hassle.

Once you get lights and shadows in there the cost of drawing all of those individually is going to get really high fast.

-------------------------

