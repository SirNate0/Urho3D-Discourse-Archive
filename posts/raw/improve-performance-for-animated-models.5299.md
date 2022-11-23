GodMan | 2019-07-16 01:10:19 UTC | #1

I have an AI that is made of two separate meshes, and two textures. This model is by no means today's level of details in modern games. If I spawn one or two of them and they use a navmesh to walk around the frame-rate is pretty solid at 60fps.  If I spawn lets say eight of them and they navigate to a location the frame rate drops to 40-44.

I used an animated model, because I read that the GPU handles there animations. 

Any suggestions welcomed. I'm not looking for 50 of them on the screen at one time.

-------------------------

Leith | 2019-07-16 07:51:31 UTC | #2

Skinned mesh animation on the GPU is pretty fast (even when animation transforms are blended on the cpu) - but pathfinding on navmeshes is quite slow (typically involving A-Star or similar expanding search algorithm). Most pathfinding algorithms are happy to terminate early after N search steps (without completing the search) but I am not certain that our implementation supports this.
I'd have to see how (often) you're performing your pathfinding, and the resolution of your navmesh, but I bet if you enable profiling that all your frame time is getting sucked up by pathfinding.
Typically, once a path has been found, the AI should be fairly confident that the found path will remain valid, and only check periodically to confirm that nothing has changed to invalidate the path. In terms of periodicity, I typically use delay values between a half-second and one second, and settle on a value that works in the context and requirements of that particular game. Oh - and make sure your AI are not all being created on the same frame, so that the computational load is spread over frames, and does not create spikes when all 50 AI try to perform pathfinding update in the same frame...

-------------------------

jmiller | 2019-07-16 02:45:56 UTC | #3

The profiler is usually valuable in locating specific bottleneck(s).

I am not aware of issues like that with animation itself.
Rendering FPS 'depends' on things..

Navigation mesh tile size can have a big effect (certainly while building).
  https://urho3d.github.io/documentation/HEAD/_navigation.html
  https://github.com/urho3d/Urho3D/blob/master/Source/Samples/15_Navigation/Navigation.cpp

-------------------------

Leith | 2019-07-16 09:33:54 UTC | #4

I like to make my ai tap its foot for a while, while pathfinding runs - I expect pathfinding can terminate early at some costing, so other AI can have some processing time, in the same frame, and not lag the game. This can mean that some AI take longer to "think" than others, but it's better than losing game play quality. All expanding-search algorithms can in theory support early search termination and resume, but not all implementations are equal.

-------------------------

Leith | 2019-07-16 12:18:56 UTC | #5

"Not finished yet" is a real thing in behavior trees, and one reason i am attracted to this design concept

-------------------------

GodMan | 2019-07-16 19:41:48 UTC | #6

I think my frame-rate drop was related to post processing. In the debug info on the screen render quad had the highest value. I had bloom and bloomhdr both on. I disabled bloomhdr and left just bloom, and now the frame-rate is much better. 

I wan't to use hdrbloom instead of bloom, but I can't seem to make it look very good.

-------------------------

Modanung | 2019-07-16 19:48:48 UTC | #7

I don't think they were meant to be used simultaneously. What are your threshold and mix values?

-------------------------

GodMan | 2019-07-16 23:19:02 UTC | #8

I'm not using them simultaneously anymore. Here is the line for the values.
    `effectRenderPath->SetShaderParameter("BloomHDRMix", Vector2(1.0f, 8.0f));`

I was trying to get things that turn bright in the scene to stand out.

-------------------------

GodMan | 2019-07-17 00:03:29 UTC | #9

I removed hdr and just kept bloom. The effect looks nicer, and I don't get crazy frame-rate drops anymore.

-------------------------

Modanung | 2019-07-17 00:47:45 UTC | #10

Did you set the Bloom(HDR)Threshold paramater?

-------------------------

GodMan | 2019-07-17 03:30:17 UTC | #11

You mean the default value in the XML. I believe it is set to 0.8 by default. Yeah I messed around with it. I really removed it due to frame rate issues.

-------------------------

Modanung | 2019-07-17 12:52:25 UTC | #12

[quote="GodMan, post:11, topic:5299"]
I really removed it due to frame rate issues.
[/quote]

Didn't you say that seemed to be due to simultaneous use of HDR and non-HDR bloom?

[quote="GodMan, post:6, topic:5299"]
I had bloom and bloomhdr both on. I disabled bloomhdr and left just bloom, and now the frame-rate is much better.

I wan’t to use hdrbloom instead of bloom, but I can’t seem to make it look very good.
[/quote]

-------------------------

GodMan | 2019-07-17 16:07:43 UTC | #13

Yes I thought it was because of having both enabled. I removed HDR first and left bloom, and everything seem to run okay. After posting I tried HDR by itself. Then the frame-rate drops returned.

-------------------------

GodMan | 2019-07-17 20:54:04 UTC | #14

Is there any way to improve the HDR Post Processing effect? I like it's effects on bright areas especially if you want certain things to glow and stand out.

-------------------------

Leith | 2019-07-18 04:50:47 UTC | #15

Shader Post-Effects like Bloom always have a fixed-size "kernel", which is basically how many neighbour pixels will get sampled during things like blur passes.

You could try playing with the kernel size, both for the regular and hdr shaders.
This will have a very direct impact on both quality and performance - effectively giving you a means to trade one for the other.

-------------------------

GodMan | 2019-07-18 15:58:44 UTC | #16

@Leith If I lower the kernel blur size from 5 to 3. In the stats of my application renderQuad  went from 1450 range down to 950 range. I don't seem to get the massive frame rate drops now. So that is a start.

-------------------------

GodMan | 2019-07-19 23:59:10 UTC | #17

Hey guys how can I set my AI animations to be a fixedupdate instead of the default every frame? I trying to improve things were I can to help out performance.

-------------------------

