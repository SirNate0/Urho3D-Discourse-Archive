Enhex | 2017-01-02 01:11:55 UTC | #1

The black noise thing happens when When I have a light attached to the camera's node.
Lights are cut in half and seems to have a red tint.

with Forward only the PBR model is affected.
With PBRDeferred it happens on everything.

In the editor it shows up fine, I'm not sure what's the difference (editor is forward?).

Images (only the rifle model is PBR):
PBRDeferred, camera light:
[img]http://i.imgur.com/4EzDTd8.jpg[/img]
(The clean part at the far away  ramp is out of the camera light's range)
[img]http://i.imgur.com/5HEDcZo.jpg[/img]

PBRDeferred:
[img]http://i.imgur.com/FFIxJix.jpg[/img]
[img]http://i.imgur.com/KcoMhmD.jpg[/img]

Forward:
[img]http://i.imgur.com/9ycl0JX.jpg[/img]
[img]http://i.imgur.com/PDUI8Tg.jpg[/img]
[img]http://i.imgur.com/tlbG813.jpg[/img]


Note that while forward handles lights correctly (except camera light), it isn't an option for projects that use many lights.

-------------------------

hdunderscore | 2017-01-02 01:11:56 UTC | #2

Thanks for the report, I have pushed a fix. Let me know if it works for you.

Just FYI, deferred GL3 has an issue atm that is causing the specular spot from lights not to render (at least on my machine?), you might want to test with GL2 if you aren't already.

-------------------------

Enhex | 2017-01-02 01:11:56 UTC | #3

Tested it. The black noise from light in camera's node is gone.
Red tint and half lights are the same.

Tested OGL2 too, it doesn't have red tint, but lights are still cut in half. Also there's this black strip (a shine thing?), in OGL3 it appears in the right color but still stretched like that:
[img]http://i.imgur.com/XSlUay0.jpg[/img]
[img]http://i.imgur.com/8kNJctx.jpg[/img]
[img]http://i.imgur.com/cVag2lK.jpg[/img]

-------------------------

dragonCASTjosh | 2017-01-02 01:11:56 UTC | #4

That seams a little odd as nothing within the lighting was changed only materials. Can you test opening the BRDF shader and change line 48 ([url]https://github.com/urho3d/Urho3D/blob/master/bin/CoreData/Shaders/GLSL/BRDF.glsl#L48[/url]) to be Lambert instead of Burley.

[code] return LambertianDiffuse(diffuseColor, roughness, NdotV, NdotL, VdotH);[/code]

-------------------------

Enhex | 2017-01-02 01:11:56 UTC | #5

Tried it and it doesn't seem to fix the problems.

-------------------------

dragonCASTjosh | 2017-01-02 01:11:56 UTC | #6

try change it here [url]https://github.com/urho3d/Urho3D/blob/master/bin/CoreData/Shaders/GLSL/PBRLitSolid.glsl#L189[/url] looks like the diffuse method was not used in forward rendering

-------------------------

Enhex | 2017-01-02 01:11:56 UTC | #7

Didn't seem to help either.

The the red tint is reproducible with Urho's samples when using PBRDeferred, by adding:
[code]engineParameters_["RenderPath"] = "RenderPaths/PBRDeferred.xml";[/code]
to Sample::Setup() in Sample.inl

[img]http://i.imgur.com/fIn7OnZ.jpg[/img]
[img]http://i.imgur.com/CQcx8fA.jpg[/img]
[img]http://i.imgur.com/xLaaPXG.jpg[/img]
[img]http://i.imgur.com/hch9jFl.jpg[/img]

The "half lights" problem doesn't seem to happen with the Urho samples. I am constructing the level models manually from a custom format, so it might be related.
EDIT:
half lights also happen with regular models.

-------------------------

1vanK | 2017-01-02 01:11:57 UTC | #8

by the way Skybox has no miplevels, u need use Skybox2 for PBR

-------------------------

1vanK | 2017-01-02 01:11:57 UTC | #9

hmm, a also have problem with deferred (OpenGL)

[url=http://savepic.ru/9418526.htm][img]http://savepic.ru/9418526m.png[/img][/url]
[url=http://savepic.ru/9398046.htm][img]http://savepic.ru/9398046m.png[/img][/url]

-------------------------

hdunderscore | 2017-01-02 01:11:57 UTC | #10

What are you using for your zone texture? Could it be introducing the red tint ?

-------------------------

Enhex | 2017-01-02 01:11:57 UTC | #11

[quote="hd_"]What are you using for your zone texture? Could it be introducing the red tint ?[/quote]
I don't use anything, and neither do the Urho samples

Another weird thing with my models, shotgun gets a yellow barrel and minigun becomes purple:
[img]http://i.imgur.com/HKdis1c.jpg[/img]
[img]http://i.imgur.com/7mR8xuo.jpg[/img]

-------------------------

hdunderscore | 2017-01-02 01:11:57 UTC | #12

Oh I see, you are trying to use PBRDeferred on materials that don't use PBR techniques?

-------------------------

dragonCASTjosh | 2017-01-02 01:11:57 UTC | #13

Im surprised non-PBR materials even display in PBR as from initial development they displayed invisible.

-------------------------

Enhex | 2017-01-02 01:11:57 UTC | #14

[quote="hd_"]Oh I see, you are trying to use PBRDeferred on materials that don't use PBR techniques?[/quote]
Yes.
Everything has to be converted to PBR? That's a big constraint for me.
I only have 3 PBR models, the rest are regular diffuse/normal/specular.

-------------------------

dragonCASTjosh | 2017-01-02 01:11:57 UTC | #15

[quote="Enhex"][quote="hd_"]Oh I see, you are trying to use PBRDeferred on materials that don't use PBR techniques?[/quote]
Yes.
Everything has to be converted to PBR? That's a big constraint for me.
I only have 3 PBR models, the rest are regular diffuse/normal/specular.[/quote]
We  didnt do a full conversion as requested by core developers. Instead we made PBR alongside the legacy renderer. it includes separate techniques. they only thing they have in common is they both work on the default forward render path.
materials that are Diff/Normal/Spec need to be converted into a PBR format where the texture for the spec map contains Roughness in the red color channel and Metallic in the green

-------------------------

hdunderscore | 2017-01-02 01:11:57 UTC | #16

Yeah the new deferred shaders use the gbuffers quite a bit differently to the old ones, so that's probably a big part of the issue.

If you are lucky you can get away with getting a basic result by switching to the PBR shaders using your specmap (if it's a greyscale image?), by playing with the roughness and metallic values (eg, setting roughness to -1). Ideally you would author materials with PBR in mind though.

-------------------------

dragonCASTjosh | 2017-01-02 01:11:57 UTC | #17

you may be able to get away with using the forward render path and both legacy and PBR materials may display correctly

-------------------------

hdunderscore | 2017-01-02 01:11:57 UTC | #18

The issue with deferred + GL3 that I mentioned should be resolved in master now.

-------------------------

hicup_82017 | 2017-09-05 11:59:48 UTC | #19

Hello,
A bit of off topic. I could not find any other relevant thread.

I could not get the PBR demo example to work on my Android. I could get it to work in my Linux PC.
After some home work on the forums, I could find the following issue is still open,
https://github.com/urho3d/Urho3D/issues/1545

Is this issue is still relevant? Or am I the only one, who could not get this to work.
**Additional information:**
1. My Mobile is Android 4.4.2  HTC one M8.
2. I could get every other example to work on mobile.
3. Example not working =
        1. I could see only a grey plane being displayed after nearly 8 seconds of launching PBR example.
         2. I could see some text like Metallic, Low roughness being displayed but no materials as such.

-------------------------

johnnycable | 2017-09-05 14:01:36 UTC | #20

The example starts (after a very long loading, has a lot of data) on my galaxy note 4.
Artifacts: no background, fails on full metallic, looks like plastic on steroids...

![Screenshot_2017-09-05-15-40-37|690x393](upload://16MrcUffRvdKssYAg0zUssXFsXq.jpg)

-------------------------

dragonCASTjosh | 2017-09-05 14:45:28 UTC | #21

It looks like IBL filtering fails on mobile platforms, i recently got a new android phone so hopefully ill be able to test on there

-------------------------

hicup_82017 | 2017-09-07 08:19:44 UTC | #22

here is mine, after 8seconds, waited for 1min, even then same observation..
Urho3d version 1.7 release code.
HTC one M8 with Android 4.4
![Screenshot_2017-09-05-21-43-03|690x388](upload://txnzAfJzYWbeCFgNYUsjcayehFn.png)

-------------------------

1vanK | 2017-09-05 19:53:54 UTC | #23

Also (in order not to create a new topic) is it normal, that reflections is fully visible in shadows?

![2|634x500](upload://j2gdZ8TaLn570dSGE76GT2m3NX6.jpg)
![1|634x500](upload://i9J3fgzZ98xplijewRm7soR6FYk.png)

-------------------------

George1 | 2017-09-06 08:05:43 UTC | #24

Unless there is total blackout, in real life, reflection also shown under shadows.

Try to cover  your hand on reflected surface in a room. There is still reflection.

-------------------------

1vanK | 2017-09-06 10:06:23 UTC | #25

Things in the shadow are illuminated by indirect lighting. Indirect lighting has the same physical laws as direct light. You will never see a reflection on a rusted metal even in the shadow

-------------------------

dragonCASTjosh | 2017-09-06 11:49:53 UTC | #26

The IBL showing in shadows is more just a lmitations of IBL, its a static cubemap the is filtered outside of the engine. although i feel it may not be filtering correctly as the roughness in shadows doesnt look to change.

-------------------------

Modanung | 2017-09-06 18:12:04 UTC | #27

Could something like @godan's reflection probe be what you're looking for?

https://discourse.urho3d.io/t/use-skybox-material-as-reflection-source/3016/4?u=modanung

-------------------------

johnnycable | 2017-09-07 05:27:53 UTC | #28

Test on my ipad air 4 2014:

![IMG_0580|666x500](upload://s6SWlHBqxWEP6rDNP4OMmErZx2F.jpg)

this is serious.

It's not working at all.
Could it be something related to opengl version used?
Both devices I'm testing (the other is galaxy note 4) are open gl es 3.
Is there a way to check if they are using the right opengl version in the urho logs?
I must add I'm on urho 1.6 version... going to test 1.7 next.

-------------------------

dragonCASTjosh | 2017-09-07 09:43:30 UTC | #29

im going to look into it tonight, there are also a few other PBR mobile improvements i have in mind

-------------------------

George1 | 2017-09-08 14:15:10 UTC | #30

Sorry! I missed understand you. I didn't look at the first picture at first.
There is definitely not right in the second picture, as the glossiness seems high. Definitely a cube map issue.

-------------------------

