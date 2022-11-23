Taqer | 2020-03-01 23:15:26 UTC | #1

Hi, is there some tutorial/info about using PBR Materials? I want to use them in my project, but they doesn't look right when I'm using my custom textures (no sun reflections after many tweaks in materials) following the way of demo project. Models are also very dark (I needed to set high zone ambient color to even see them). What are requirements of textures / scenes to get PBR right?

-------------------------

GodMan | 2020-03-02 00:34:14 UTC | #2

I read somewhere on the forums that their are still issues with PBR. Last time I messed with PBR it was extremely slow. I don't know if any of this has been resolved though.

-------------------------

Eugene | 2020-03-02 12:41:38 UTC | #3

The fact is that PBR in Urho is not properly supported.
There are some shaders, but they are not really usable.
Few issues I remember:

1) Urho doesn't have inbuilt gamma correction, so PBR textures may look too ~~dark~~ bright unless you pre-convert them to linear space.

2) Urho doesn't have reflection probes, so there's no way to smoothly render metallic materials in real scenes.

3) Shaders are suboptimal and missing some features supported in standard shaders.

-------------------------

Bananaft | 2020-03-02 12:22:56 UTC | #4

[quote="Eugene, post:3, topic:5959"]
Urho doesn’t have inbuilt gamma correction, so PBR textures may look too dark unless you pre-convert them to linear space.
[/quote]

It does.` <srgb enable="true" />` in texture metadata.

-------------------------

Eugene | 2020-03-02 12:42:41 UTC | #5

[quote="Bananaft, post:4, topic:5959"]
It does. ` <srgb enable="true" />` in texture metadata.
[/quote]
This is only one aspect of gamma correction.
Things like material diffuse color still go as-is without any conversion.
Texture sRGB also requites manual configuration for each texture instead of working out of the box.

I'm also not sure that sRGB is supported on all platforms.

Moreover, Urho's PBR uses post-processing to finalize gamma correction and this is suboptimal approach. IIRC it is recommended to render directly into sRGB texture.

-------------------------

Eugene | 2020-03-02 12:56:27 UTC | #6

Oh, I've just remembered two more issues.

PBR in Urho does not and cannot easily support emission lighting (and therefore lightmaps and/or vertex lights).

PBR in Urho is deferred-only, so forget about ~~transparent PBR materials~~ nice antialiasing.

Upd: Maybe transparent PBR materials actually work, I never tested it. There is forward branch in shaders, but I don't think it's used in our PBR sample.

-------------------------

Bananaft | 2020-03-02 13:00:33 UTC | #7

There is  **GammaCorrection** postEffect, that does simple `pow(color , 1./2.2 ))` conversion, which is good enough.

My project uses linear pipeline. I believe stock Urho have everything to set it up.

[quote="Eugene, post:5, topic:5959"]
Things like material diffuse color still go as-is without any conversion.
[/quote]
True. Not as much of a problem IMO, just have to be taken into account. I may even want to set them up in linear space.

[quote="Eugene, post:5, topic:5959"]
Texture sRGB also requites manual configuration for each texture instead of working out of the box.
[/quote]
What do you mean, by working out of the box? You still need a way to specify which textures to convert or not.

-------------------------

Eugene | 2020-03-02 13:08:18 UTC | #8

[quote="Bananaft, post:7, topic:5959"]
What do you mean, by working out of the box? You still need a way to specify which textures to convert or not.
[/quote]
It's safe to assume that input textures for diffuse texture slot in Material are by default in gamma space and need to be converted to linear. And deviation from this rule may require manual configuration.
It could have been automatic, in perfect world.

-------------------------

Bananaft | 2020-03-02 13:15:41 UTC | #9

too perfect :slight_smile:

-------------------------

lezak | 2020-03-02 14:11:58 UTC | #10

[quote="Eugene, post:6, topic:5959"]
Upd: Maybe transparent PBR materials actually work, I never tested it. There is forward branch in shaders, but I don’t think it’s used in our PBR sample.
[/quote]

HoverBike glass have transparent material.

-------------------------

Eugene | 2020-03-02 15:46:19 UTC | #11

Oh, didn't notice this part, thanks!

-------------------------

Modanung | 2020-03-02 20:00:24 UTC | #12

@Taqer Maybe you could add a brief tutorial to the [wiki](https://github.com/urho3d/Urho3D/wiki) based on these answers?

-------------------------

