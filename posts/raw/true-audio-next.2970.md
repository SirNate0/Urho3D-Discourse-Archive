godan | 2017-03-29 16:33:21 UTC | #1

I was just at (yet) another talk about VR. This one was from AMD, and they are developing a new immersive audio platform, called True Audio Next. The thing I found interesting is that it does to audio what PBR did to pixels... Also it is open source and MIT:

https://github.com/GPUOpen-LibrariesAndSDKs/TAN

-------------------------

Sinoid | 2017-03-31 03:05:45 UTC | #2

So, on VR where the GPU is getting hit harder than usual we should give up GPU resources to audio that isn't an application of modal analysis?

My beef would be that this doesn't actually deal with the problems. Solving wave propogation for VR would be worthwhile to do on the GPU, but this is just a bunch of DSP helpers, and SSE2+ is more than sufficient for accelerating that. This is a much better job for an OpenCL CPU profile IMO.

Am I missing something?

-------------------------

godan | 2017-03-31 13:09:52 UTC | #3

Yes, after my initial excitement, I was also a bit let down by how they actually deal with the audio from a theoretical point of view.There is no wave propagation, no ambient medium, etc... And what about music tracks that already have reverb, compression, high pass,etc already baked in? Doesn't seem like this will fit in to the production pipeline very well.

However, I think a cool application of this would be letting designers change room/level geometry "by ear", based on how the audio responds.

-------------------------

Sinoid | 2017-04-02 04:06:16 UTC | #4

Yeah, it's definitely cool. Bonus points for being readable compared to most DSP code which is often arcane pure C witchcraft.

Knowing ATI/AMD it'll get better over time. TressFX started sketchy, but is pretty awesome now.

-------------------------

