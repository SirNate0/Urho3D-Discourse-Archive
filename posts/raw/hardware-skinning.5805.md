GodMan | 2020-01-04 18:03:41 UTC | #1

I made a hardware skinning shader in hlsl for irrlicht years ago. After reading the urho3d docs. Am I correct that urho3d does the automatically on the gpu?

Or would a hardware skinning shader improve character performance?

I'm asking because if I render lets say 10 ai that all use the same model and animations. Framerate drops quite a bit. I solved this in irrlicht with the HS shader.

-------------------------

Sinoid | 2020-01-05 00:18:05 UTC | #2

Skinning is already done on the GPU. 

The bone tree (just the matrices themselves) and morph-targets are done on the CPU (have to be without stream-out for morphs and compute for the bone-tree).

You really shouldn't be having trouble with only 10.

-------------------------

GodMan | 2020-01-05 01:32:33 UTC | #3

Well they are low poly by today's standards. Maybe it is the crown navigation that is kill the frame rate.

-------------------------

Sinoid | 2020-01-05 05:35:41 UTC | #4

The `CrowdAgentReposition` / `E_CROWD_AGENT_REPOSITION` event is generally where crowd performance problems are, and it's usually really obvious in the profiler.

Mashing the 39_CrowdNavigation (at 300 agents), 07_Billboards, and 12_PhysicsStressTest samples into one, I still get a stable 30 fps on an old Intel HD4000 @ 720p:
![CrowdPerf|690x388](upload://pBU70OmXNYfHsN7eoEE8BYsasuC.png) 

Highlighted the region to look at to observe how much time crowd is eating.

-------------------------

GodMan | 2020-01-05 17:38:20 UTC | #5

![Screenshot_Sun_Jan_05_11_32_16_2020|690x291](upload://vAr4MOLqTeXtQumxEcMJB8MXiIk.jpeg) 

Hmm mine seem to be always Renderquad and RenderScenePass. I can only assume it is because of the HDR PostProcessing. I'm not to sure. When the AI's get to there destination that is usually when the frame rate starts to drop.

-------------------------

Sinoid | 2020-01-06 02:57:47 UTC | #6

21:9 aspect ratio is huge. You've got a stable 5ms going into `Present` which is the basically GPU command flush + VSync (if it's on). Render-doc is your friend here to be sure but I'd think you're chewing fill-rate.

A `LQ-HDR` can be done by copying the PostProcess file and changing the divisors (something other than 2->4->8->16, like 4->8->16->32 or 8->16->32->64). The #ifdefs in that shader are mostly just for using the right auto-uniforms (target size and inv-size). But you shouldn't save more than a handful of frames from doing that. It'll get more Oblivion-bloom-hell-esque the more you divide though - it's easy to check though to see if it makes a meaningful difference. It isn't that meaningful for me, but 1080p is the largest res I have.

---

3 - 4 ms going to occlusion drawing is probably the upper limit that you want to see. Might want to see if terrain really needs to be an occluder and if maybe an LOD set to an enormous LOD distance for the cliff meshes helps that. Occlusion drawing uses the lowest LOD available for both terrain and meshes, so in the case of a mesh if you set the LOD distance to something like `FLT_MAX` that will actually pass tests then the LOD will be used solely by the occlusion software renderer.

See the [asset importer docs](https://urho3d.github.io/documentation/1.7/_tools.html) on how to use it to merge seperate meshes into 1 with LOD. It can also be done in code with [something like IGL + Eigen](https://github.com/JSandusky/Urho3DProcGeom/blob/master/ProcGeom/LODGen.cpp) which is more work code-side instead of content-side.

-------------------------

GodMan | 2020-01-06 23:58:47 UTC | #7

Thanks for the post @Sinoid. I will try some of your suggestions. I will post back later.

Thanks

-------------------------

GodMan | 2020-01-07 04:00:29 UTC | #8

Okay so I fixed the frame rate drop. I was using the map as an occluder which I'd imagine did not perform well. I also removed some things from always being updated. I also set the screen resolution to 1920x1080 for the fill rate you mentioned. I made some other changes that I can't remember, but it seems pretty solid.

-------------------------

Sinoid | 2020-01-10 01:49:27 UTC | #9

Not a whole lot you can do about fill-rate costs except work with lower resolution requirements in post-fx, checkerboard, YCoCg if deferred, etc.

Occluders are a pain to tune. It's a bit involved but you can write your own `Drawable` derived component that has no Batches but is still an Occluder that emits Occlusion triangles. It's kind of odd that there isn't one already there for even a basic Box shape occluder.

-------------------------

GodMan | 2020-01-11 03:17:19 UTC | #10

I was thinking of something like portal rendering. Would it be possible to create some simple planes that don't render, but can be used for occluding? 

I suppose this would not work since the planes do need to be visible.

Also on the Crowd Navigation once the AI's reach there destination is there a way to keep them from always check or updating their path? I did not see an option for this. I noticed that once the AI's that use the navigation mesh reach there target destination. The update stats in the debugger seem to climb alot. I think they may be checking things to often. If this makes sense.

-------------------------

Modanung | 2020-01-11 12:18:20 UTC | #11

[quote="GodMan, post:10, topic:5805"]
I suppose this would not work since the planes do need to be visible.
[/quote]
You could assign them an invisible material.

-------------------------

GodMan | 2020-01-11 17:54:44 UTC | #12

You mean like completely transparent.

Does urho3d already have a material for this?

-------------------------

Modanung | 2020-01-12 03:33:09 UTC | #13

    <material>
        <technique name="Techniques/NoTextureAlpha.xml" />
        <parameter name="MatDiffColor" value="0 0 0 0" />
        <parameter name="MatSpecColor" value="0 0 0 0" />
    </material>

-------------------------

GodMan | 2020-01-12 19:44:47 UTC | #14

@Modanung Thanks for the post I will try it out later.

On using navigation or crowd navigation is there not an option to set how often the ai or agent checks their path? I have noticed that once the ai or agent reaches there destination and they stand around that point. The update stats seem to climb a good amount. I'm thinking maybe because they keep updating something.

If that makes sense.

-------------------------

Sinoid | 2020-01-17 05:45:24 UTC | #15

It's probably more complicated than just standing still. 

It'll be a pain to hunt down but I'm betting that it's because the agent's are in the same polygon as their destination and that causes heavier calculations (regardless of whether they're on the actual point or not) than the polygon->polygon routing where they're just selecting corner points and running their crowd corridor.

It's tough to tell but it might be an Urho event raising issue or it might be a DetourCrowd issue. I'm betting that it's a bit of both where DetourCrowd is eating juice as I described above and Urho is sending events that it has no business sending.

Crowds really has no business being bound to scripting to begin with ... oh it's just a big mess.

-------------------------

GodMan | 2020-01-17 17:20:34 UTC | #16

Well that's unfortunate. What do you suggest? Not using crowd navigation?

-------------------------

weitjong | 2020-01-18 03:44:33 UTC | #17

Just wondering were you instructing all the agents to move to a single target point, which they cannot reach once one of the agent is already there? Also, may I suggest you to keep on the topic or change the title of the topic or raise a separate topic for your crowd navigation question.

-------------------------

GodMan | 2020-01-18 05:00:41 UTC | #18

Yes I do send them to the same point. I thought they would all crowd around a point if there is more than one agent. They do not appear to keep trying to reach the exact point. I thought by looking at the code they would just try to achieve a radius close to the point if their is more than one agent. Do you think this is the issue?

-------------------------

weitjong | 2020-01-18 05:18:03 UTC | #19

Most probably. You can try by having one agent first to see whether it "settled down"; or try to set a group of agents to a target area within a certain radius. I believe the crowd navigation demo does the latter. I could be wrong, not looking at the sample code right now.

-------------------------

