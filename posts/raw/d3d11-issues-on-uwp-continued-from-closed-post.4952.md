I3DB | 2019-02-22 18:53:28 UTC | #1

[This is a follow on to a prior post that was locked](https://discourse.urho3d.io/t/urhosharp-hlsl-shader-issue-for-water-on-d3d11-paints-water-black/4944/15). Just wanted to provide a followup.


The solution from that post had no effect on my situation, where water paints black in the water feature sample.

Still don't know the root cause, but do think it is in the urhosharp implementation, and not related to urho3d engine specifically.

Here's how to get clear water in that feature sample ...

In the water feature sample, if the waterMat is changed from TextureUnit.Diffuse to TextureUnit.Environment, and both reflectionplane and clippplane are commented out, then UWP water sample paints water clear, as shown:

![PNG|645x500](upload://8aLANlfWjFA8wnmkULkxhApIQTi.jpeg) 

With those same changes, running on otherwise working platforms (opengl) will cause the water to reflect the environment as if it is a mirror. Very different behavior from the UWP behavior on D3D11 which isn't showing the environment at all.

The water painting clear for UWP uses the nuget download of urhosharp, which uses a slightly modified urho3d 1.7 release, which doesn't have the bug fix for #2232 in it.

I'm not planning to do more with this, I've exceeded my experience level on what to do or how to approach this to find the underlying cause.

But if the goal is clear water ... this workaround provides it on UWP.

-------------------------

cosar | 2019-02-22 21:24:24 UTC | #2

@I3DB
If your goal is to remove water reflections, modifying the water shader is probably a better approach.
The way the water shader works is combining reflection (obtain by sampling diffuse texture) with the refraction (obtain by sampling environment texture). By not setting the diffuse texture with the generated reflection, the behavior will be undefined.

-------------------------

I3DB | 2019-02-22 23:52:50 UTC | #3

[quote="cosar, post:2, topic:4952"]
If your goal is to remove water reflections
[/quote]

The goal is for similar or identical behavior to the water feature sample.

Getting the water to paint clear instead of black is a positive change. Starting from painting black but with reflection. There's something wrong in the shader/texture path for UWP and this issue is but one of several. My comment above is only useful for someone who is looking to get the water clear, not as a final solution.

-------------------------

