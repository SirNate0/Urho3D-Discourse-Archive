Lumak | 2017-11-14 08:33:51 UTC | #1

repo: https://github.com/Lumak/Urho3D-LightProbe

Below is a pic of lightprobe implementation - there's no light in the shot, glow on the char is based on SH coeff.
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/a/a71bb0517fd63dbcadd57d5afb141332f68be33b.png[/img]

-------------------------

artgolf1000 | 2017-11-14 09:00:48 UTC | #2

Global illumination? Looks so cool!

-------------------------

johnnycable | 2017-11-14 09:05:10 UTC | #3

@Lumak good job as usual.

-------------------------

stark7 | 2017-11-14 17:35:26 UTC | #4

Oh man.. there are only so many repos I can fork :slight_smile: . One of these days I need to spend time converting everything to C# - or does anyone have a cloning machine for Lumak? A C# coding clone? :smiley:

-------------------------

Lumak | 2017-11-14 19:43:20 UTC | #5

Repo updated: optimization and some clean up.

@artgolf1000 Currently, just a light probe which illuminates the char. But I guess it could be possible to use it for GI, I don't have knowledge on how, though.

@johnnycable thanks and enjoy.

@stark7 unfortunately I'm not touching C# atm.

-------------------------

Lumak | 2017-11-17 16:27:43 UTC | #6

Repo updated: code and shaders. I think I nitpicked enough.

-------------------------

artgolf1000 | 2017-12-16 10:32:40 UTC | #7

I have noticed that the Godot engine use GIProbe technology to achieve realtime GI on desktop, you may get some brief from their blog.

Though my screen space global illumination shader runs smoothly on mobile devices, but the result is not good in all cases.

I wonder if the GIProbe is similar to Lumak's LightProbe?

-------------------------

Lumak | 2017-12-16 19:16:59 UTC | #8

I briefly reviewed the code and, no, they're not the same. My work is based on "_An Efficient Representation for Irradiance Environment Maps_," ref: http://graphics.stanford.edu/papers/envmap/, and they're using some kind of magic.

-------------------------

GodMan | 2017-12-18 20:26:52 UTC | #9

Looks great I was needing to look into this in the future as I use lightmaps for my projects and I'm currently converting my directional lightmap shader I made 3 years ago for Irrlicht to Urho3d.

This will help me out a lot for integrating my dynamic objects with the scene thanks.

Do I just download this from github and place in my urho3d folder and build it the same?

-------------------------

GodMan | 2017-12-27 22:28:54 UTC | #10

I see lightprobe uses a cubemap. What would be a good solution if my character already has a cubemap being used in the enviorment slot for there materials?

-------------------------

Lumak | 2017-12-28 22:38:00 UTC | #11

You might try the other tex from the list: https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/Material.cpp#L53

Or encode the data in diffuse tex, if your uv map has space.

-------------------------

TheComet | 2018-05-29 13:38:49 UTC | #12

Neat! I'll have to try this out. Does it support dynamic lights (that's the whole point of GI right?)

-------------------------

Lumak | 2018-05-29 14:00:23 UTC | #13

I didn't write GI, although, there was a paper written about using precomputed lightprobes to achieve GI - http://research.nvidia.com/publication/real-time-global-illumination-using-precomputed-light-field-probes

-------------------------

Lumak | 2018-05-29 14:27:54 UTC | #14

Answer to this question, https://computergraphics.stackexchange.com/questions/233/how-is-a-light-probe-different-than-an-environmental-cube-map provides a good description of types of lightprobes used. Personally, my use case for this was to remove lights in a mobile platform that couldn't support many light sources - replacement of light.

-------------------------

Eugene | 2018-05-29 14:33:00 UTC | #15

Huh. I missed this thread for some reason.
As I'm experimenting with Urho renderer, I thought about integrating SH into Urho...

I've just looked into your implementation. Unsure if SH texture is viable. In perfect world there shall be per-object uniforms, shan't they?

-------------------------

Lumak | 2018-05-29 14:53:03 UTC | #16

I think that would be a personal preference. You can choose to write 3-3x3 matrix of SH for each lightprobe or encode the entire stream of it onto a texture. If given a choice I'd write the SH data onto a diffuse texture that's already used by the model for each level/scene to avoid loading extra texture.

-------------------------

Eugene | 2018-05-29 15:03:55 UTC | #17

What about light probes blending and SH from dynamic lights?
It's hard to do in shader but easy on CPU.

-------------------------

Lumak | 2018-05-29 15:15:09 UTC | #18

If you're using dynamic lightprobes then you probably don't need to store any precomputed.

-------------------------

TheComet | 2018-06-15 23:55:27 UTC | #19

Your github link is 404'ing
https://github.com/Lumak/Urho3D-LightProbe

-------------------------

smellymumbler | 2018-06-18 01:21:23 UTC | #20

Lumak apparently removed all his repos.

-------------------------

elix22 | 2018-06-18 03:56:50 UTC | #21

Another link
https://github.com/elix22/Urho3D-LightProbe

I am not sure if it’s updated but you can have something to start with.

-------------------------

weitjong | 2018-06-18 06:49:59 UTC | #22

It’s a knowledge lost for the community. I wonder why.

-------------------------

rku | 2018-06-19 07:04:49 UTC | #23

@Lumak is there any reason why you deleted your urho3d samples? Maybe you would be willing to share them back to community?

-------------------------

Lumak | 2018-06-19 15:44:08 UTC | #24

I will not recreate any of my repos but will collaborate with elix22 to make sure everything he has is up to date.

-------------------------

rku | 2018-06-19 15:52:56 UTC | #25

If you still have the code but do not want to deal with it you can always zip it up and drop here.

Thank you for all that work and not letting it die, all your samples are superb :)

-------------------------

