Angramme | 2019-02-24 00:06:55 UTC | #1

I tried to apply some pbr materials to the box under the tree but for some reason the material appears REALLY DARK, I used the material from here: https://freepbr.com/materials/rocky-dirt/,
And my xml file looks like this:

\<material>
\<technique name="Techniques/PBR/PBRDiffNormal.xml" quality="1" />
\<!--\<technique name="Techniques/Diff.xml" quality="0" />-->
\<texture unit="diffuse" name="Textures/dirt/albedo.png" />
\<texture unit="normal" name="Textures/dirt/normal.png" />
\<texture unit="roughness" name="Textures/dirt/roughness.png" />
\<parameter name="Metallic" value="0"/>
\</material>

I used just the albedo and normal for now
btw it looks the same witchout the roughness

Here are some screenshots:
before:
![PNG|351x500](upload://w4yxhD4P39dIE7fweklTK6UAl48.jpeg) 
I used default Stone.xml material

after:
![screen2|330x500](upload://maJtYSg8wM0wVJq0TMqJjFqH3XO.png) 
![screen3|639x500](upload://sPBsSES8p11gKUnzVEFE2ttURzW.png) 
As you can see these are really dark!

What could be the problem? Is it something with render path? I tried adjusting the intensity of the light but no big effect on my material when other non-PBR materials are white!

Thanks for help in advance.

-------------------------

I3DB | 2019-02-24 00:42:23 UTC | #2

Maybe you could get some of the provided pbr materials working, and then once comfortable with how it works start importing more.

The output you show looks like it didn't work properly.

[One of the feature samples uses pbr materials.](https://github.com/urho3d/Urho3D/tree/master/Source/Samples/42_PBRMaterials).

-------------------------

lezak | 2019-02-24 01:16:01 UTC | #3

1. Add gamma correction postproc to the render path;
2. Set some cubemap as zone texture;

-------------------------

Modanung | 2019-02-24 07:00:19 UTC | #4

I think you may be missing _tangent_ information required by normal maps. When exporting from Blender this is simply a checkbox. I'm not sure how to add tangents to custom geometry, though.

-------------------------

Angramme | 2019-02-24 13:15:30 UTC | #5

[quote="Modanung, post:4, topic:4958"]
missing *tangent* information
[/quote]
For now I'm just trying it on the box.mdl provided by Urho3D by default. I thing it has tangent information, but it might not have, will try just the albedo map to see the results, thanks for  the suggestion.

[quote="lezak, post:3, topic:4958"]
gamma correction
[/quote]
Shouldn't it work without it? Or is it required for PBR? 
[quote="lezak, post:3, topic:4958"]
cubemap
[/quote]
Is it black by default or something? is that why it's dark?
Also how would I add the postproc and the cubemap? could you point me to some ressources ?

-------------------------

I3DB | 2019-02-24 13:45:36 UTC | #6

[quote="Angramme, post:5, topic:4958"]
could you point me to some ressources
[/quote]

You mean like in the sample code

[quote="I3DB, post:2, topic:4958"]
[One of the feature samples uses pbr materials. ](https://github.com/urho3d/Urho3D/tree/master/Source/Samples/42_PBRMaterials).
[/quote]

 I pointed out?

-------------------------

Sinoid | 2019-02-25 04:25:54 UTC | #7

[quote="Angramme, post:5, topic:4958"]
Is it black by default or something? is that why it’s dark?
Also how would I add the postproc and the cubemap? could you point me to some ressources ?
[/quote]

The actual color will depend on your GPU/drivers, it's usually black though if nothing is set.

PBR is **very very** strongly dependent on having a `Zone` with a properly prefiltered cubemap present. Shouldn't be 100% dependent though IIRC, just that without `Zone`s setup correctly it turns into a nightmare to juggle light.

Ideally it's an RGBA16 cubemap as well (also makes the tooling easier, the ideal CMFT output works then), which ... Urho3D master still doesn't support RGBA16 in DDS load so I'll prep a pull-request to add that since it really isn't optional to not have it today.

-------------------------

Angramme | 2019-02-25 14:31:49 UTC | #8

Thank you for your reply! Good to know that:

[quote="Sinoid, post:7, topic:4958"]
PBR is **very very** strongly dependent on having a `Zone` with a properly prefiltered cubemap present
[/quote]

And also looking forward to your pull request, it's really nice of you taking your time to implement it, how can I see when it's there btw? I'm not really familiar with GitHub

-------------------------

kidinashell | 2021-07-10 00:10:12 UTC | #9

I know it has been a while, but I wanted to ask about the same thing. I'm not really sure how to work with convential materials combined with pbr materials in the same scene.

So far what I've found out is when I use a PBR Material the brightness of the lights has to be upped quite a bit to actually see the models. But when using both (convential and PBR) in one scene (two different meshes of course) either one will be too dark or too bright.
I've looked at the 42_PBRMaterials sample and there it is actually done that way: cranking the brightness up (even to 800) when I only need brightness of around 1 or 2 when using convential materials.

Here's what I mean about the difference I mentioned:
**Lights brightness around 50 (cranked up to see PBR material)**
![light_pbr_fin|569x393](upload://mX9j07LFdF7IDTLmjJhs2TQXZBn.png)

**Lights brightness kept at 1 (enough for conventional materials)**
![light_diffuse_fin|564x357](upload://jne7YW7T1PItX4bPPfsVasP57EW.png)

I use the following Techniques and Settings:
* Editor render path: `Forward.xml`
* PBRMaterial: `PBRDiffNormal.xml`
* Conventional Material: `DiffNormal.xml`

Is it actually possible at the moment to have both in the same scene?

-------------------------

Eugene | 2021-07-10 07:29:09 UTC | #10

[quote="kidinashell, post:9, topic:4958"]
I’m not really sure how to work with convential materials combined with pbr materials in the same scene.
[/quote]
TL;DR: You cannot xD
Unless you go and fix shaders... which may or may not be challenging.

It's just one of many issues of PBR implementation in Urho, so I just consider it unfeasible.
I know when I can recommend classic rendering of Urho, but I cannot imagine recommending Urho PBR. Just assume that Urho does not support PBR.

-------------------------

kidinashell | 2021-07-10 12:32:23 UTC | #11

Oh okay. That's too bad. So no roughness/metallic maps for me? xD

-------------------------

SirNate0 | 2021-07-10 12:49:44 UTC | #12

I've never used PBR, so this is purely speculation, but I imagine the difference in lighting is effectively a units issue. If the PBR is expecting lumens or candela or something like that for the light strength, then I would expect you would need around 50 to have details visible, whereas the traditional lighting would just have 1 be normal full strength. The fix is probably just multiplying by 0.01 or something like that in the shader.

-------------------------

