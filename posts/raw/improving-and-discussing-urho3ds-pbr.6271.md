dertom | 2020-07-16 14:31:41 UTC | #1

EDIT(*removed the request to move discussion from another topic here so this won't get lost*):
Discussion about PBR:

-------------------------

Eugene | 2020-07-16 14:39:57 UTC | #2

Agreed. Nope, I cannot, I'm just a regular user. ~~Modanung, can you please clean up project shots topic a bit? It's really getting off-topic.~~ Thanks Wei Tjong.

-------------------------

GodMan | 2020-07-16 13:04:43 UTC | #3

Too bad you can't really use PBR for real-time aside from just simple renders.

-------------------------

Eugene | 2020-07-16 13:04:43 UTC | #4

What do you mean?.. In Unity PBR is literally default shader, and thousands of games use it.
Any (or almost any) 3D AAA game for last 5+ years is using PBR is one form or another.

-------------------------

GodMan | 2020-07-16 13:04:43 UTC | #5

@Eugene  I meant Urho3d not other engines.

-------------------------

extobias | 2020-07-16 13:04:43 UTC | #6

@GodMan and why is that? why isn't usable in real time?

-------------------------

GodMan | 2020-07-16 13:04:43 UTC | #7

From everything I have read on the forums. If you tried to make a game using PBR that it was to slow.

-------------------------

dertom | 2020-07-16 13:07:19 UTC | #8

Is it possible to discuss on other topics than 'Random project shots'?

Edit by weitjong: Moved here as per your request.

-------------------------

JSandusky | 2020-07-16 13:04:43 UTC | #9

@GodMan regarding PBR, on IBL cube textures turn off anisotropy (Urho's default is 4) and set the filter mode to linear.

Other costs include:

- Doesn't use a split-sum LUT-texture which is cheaper on PC than the approximation used (which is meant for mobile where texture reads hurt much more than ALU). It doesn't use one because the BRDF isn't set in stone (see final word)
- Redundancies in calculations (roughness * roughness over and over again, once you settle pack your data once into a struct and pass that around instead) depending which BRDF parts you're using
- poor format support in Urho3D (RGBA16_F should be used for IBL cubes or use RGBM8), hardware sRGB has spotty performance from GPU to GPU (even of the same vendors)
- shader IBL defaults expect an unreasonably large texture (if you're using more 256x256x6 for an IBL cube you're probably a moron). 
- Legacy lighting systems incur significant costs due to repeated setup math compared to tiled or clustered shading, there's no debate on whether one nDotV or 64 nDotV's is cheaper.
- That Urho3D default of 4x anistropic filtering hurts (mostly because of all of the above), seriously consider DDS and pre-generating your mips instead for your usage

PBR is a base for an environment where no one can agree on even the tiniest thing about how it should be, tweak it to be what you need it to be. Lock down how you want to do it, then tweak and it should be comparable to everything else. Sure you could have it fast out of the box, but then your luck you'd be the guy that can't stand having to deal with DDS/KTX and the delay while your new textures are being Toksvig'ed.

-------------------------

GodMan | 2020-07-16 13:04:43 UTC | #10

@JSandusky so basically it is implemented poorly.

-------------------------

GoldenThumbs | 2020-07-16 13:04:43 UTC | #11

I'm pretty sure rgba16f textures are supported in Urho3d. Am I mistaken, or misunderstanding what you mean?

-------------------------

GoldenThumbs | 2020-07-16 13:04:43 UTC | #12

@JSandusky 
After looking up some stuff I think I figured out what you meant. You mean that Urho can't save to any file format that saves to something with that sort of precision, correct?

-------------------------

Eugene | 2020-07-16 13:04:43 UTC | #13

[quote="GoldenThumbs, post:12, topic:6271"]
You mean that Urho can’t save to any file format that saves to something with that sort of precision, correct?
[/quote]
As far as I remember, Urho cannot _load from_ any floating-point format either.
This is so annoying. I cannot even properly store baked lightmaps, I have to use RGBA8.

-------------------------

SirNate0 | 2020-07-16 14:29:05 UTC | #14

Would adding OpenEXR support alleviate the problem? I haven't looked in detail but it looks like it would be pretty straightforward and I believe the license would be compatible.

-------------------------

Eugene | 2020-07-16 14:39:23 UTC | #15

[quote="SirNate0, post:14, topic:6271"]
Would adding OpenEXR support alleviate the problem?
[/quote]
Not in the slightest, sadly.
Format is not an issue, DDS is perfectly capable of handling basically any uncompressed (and some compressed) image formats.

The issue is that Urho handles all images via `Image` class, which is hardcoded to RBG(A)8 layout.
Exception are compressed formats, but they are read-only.

The only realistic option (=that doesn't involve screwing the interface of `Image`) I see is to add artificial "compressed" formats for RGBA16 and so on.
And teach `SaveDDS` how to save compressed formats.

-------------------------

GoldenThumbs | 2020-07-16 15:11:55 UTC | #16

Also BMP should be able to save any uncompressed format too. So the issue is entirely with the image class? Perhaps one could overhaul the image class? That probably entails way more than it initially sounds. Why is the image class locked to 8 bit precision anyway? Is this an issue with the engine being as old as it is?

-------------------------

GoldenThumbs | 2020-07-16 15:22:46 UTC | #17

Frankly I think the best option would be to overhaul the Image class. Weird workarounds are great for a short term solution but as an open source project we should probably think about longevity. Using a workaround instead of fixing the problem itself just doesn't sound like the best option in the long run.

-------------------------

Eugene | 2020-07-16 15:58:19 UTC | #18

Compressed formats are good because `Image` already offers limited support for it.
For "normal" images `Image` offers a lot of utility functions that have to be refactored or extended.

These ones will require separate implementation for each image component type:

- `Image::SetPixelInt`
- `Image::Resize`
- `Image::ClearInt`
- `Image::GetPixel`
- `Image::GetPixelInt`
- `Image::GetNextLevel`
- `Image::ConvertToRGBA`

And I'm not really sure how to make some functions work for generic pixel type.
I mean, how `GetPixelInt` is even supposed to work for float texture? Probably we want error message in these cases.

-------------------------

SirNate0 | 2020-07-16 16:07:32 UTC | #19

Not having looked at where GetPixelInt and similar are used, my intuition is that it should actually return the same thing that the function `Color::ToUInt()` even if it's a floating point texture just as GetPixel returns a floating point representation of the color.

-------------------------

SirNate0 | 2020-07-16 16:32:23 UTC | #20

We would also need to add the necessary formats to the Graphics class. I think my preference would be to add an argument to the functions:
```
unsigned GetRGBAFormat();
```
would become 
```
enum GRAPHICS_NUMBER_FORMAT {
    GNF_INT8=0,
    GNF_FLOAT16,
    GNF_FLOAT32
}

...

unsigned GetRGBAFormat(GRAPHICS_NUMBER_FORMAT fmt = GNF_INT8);
```

so that the switch statements on the number of components can be updated just by adding an image->GetNumberFormat() or the like to the calls. Though that switch statement to get the graphics format for the image could also be moved from the 4 texture kind implementations to the Texture or Image or Graphics classes.

-------------------------

GoldenThumbs | 2020-07-23 01:07:06 UTC | #21

I like that idea. Has anyone actually started working on this yet? We should probably also open an issue on GitHub.

-------------------------

GodMan | 2020-07-24 21:25:51 UTC | #22

well this is a step in the right direction.

-------------------------

JSandusky | 2020-07-25 00:16:11 UTC | #23

@GodMan yea, pretty much. It'd probably be for the best if someone stripped most of the existing PBR out and replaced it with a port of Google's Filament. Back then Filament didn't exist, I'd probably have just ported it over if it had ... hell, IIRC Lux was the only permissively licensed reference available at the time.

--- 

I mashed 2 things together at once when I said all that. The first being perf and the second being the very common *"It's not only slow, but it also looks off*" ... headaches with higher-precision textures is a big part of why things look off as well as the stupid decision to use the mobile env-approx on PC instead of split-sum.

RGBA16 (unorm) read is the only thing that's needed for getting things looking right, writing it only matters if implementing filtering Urho3D side, assuming you want to save them and not just render them as needed. See https://github.com/rokups/rbfx/pull/203 regarding OGL + D3D11 compute and cubemap filtering.

Read support for RGBA16 in Image.cpp for DDS is pretty much just adding `ddsd.ddpfPixelFormat_.dwRGBBitCount_ == 64` and `CF_RGBA16`, CF_RGBA16 doesn't have to do the last conversion step (that mentions RGB565) - now you can load CMFT RGBA16 cubemaps.

```
if (ddsd.ddpfPixelFormat_.dwRGBBitCount_ != 64 && ddsd.ddpfPixelFormat_.dwRGBBitCount_ != 32 && 
    ddsd.ddpfPixelFormat_.dwRGBBitCount_ != 24 && ddsd.ddpfPixelFormat_.dwRGBBitCount_ != 16)
{
    URHO3D_LOGERROR("Unsupported DDS pixel byte size");
    return false;
}
if (ddsd.ddpfPixelFormat_.dwRGBBitCount_ == 64)
    compressedFormat_ = CF_RGBA16;
else
    compressedFormat_ = CF_RGBA;
components_ = 4;
break;

... a little further down ...

// Calculate the size of the data
unsigned dataSize = 0;
if (compressedFormat_ != CF_RGBA && compressedFormat_ != CF_RGBA16)
```

update `Graphics::GetFormat` to map CF_RGBA16 to DXGI_FORMAT_R16G16B16A16_UNORM and GL_RGBA16

But yes, more format support is a godsend since BC4 and BC5 are pretty much purpose built for PBR (and normals).

---

**Back to perf:**

Scrap what's there, port to Filament.

Low hanging fruit is to rework `View` to support packing up to N pure analytic point+spot lights found in the frustum into a cbuffer that a `scenepass` can receive (`use_analytic_lights="true"` or w/e). The pass can then march through N lights in one go instead of multipassing it. Obviously those analytic lights have to be ignored if any pass asked for analytic lights.

That'll save a lot of redundancy while chewing through fill-lights, though it realistically caps out at 16-64 lights depending on your desired cap - no different than tiled-shading with 1-giant-tile.

I used this for my clustered-shading to decide whether the light goes in the cluster grid or is multi-passed:

```
bool Light::IsAnalytic() const
{
    if (auto renderer = GetSubsystem<Renderer>())
    {
        // must use defaults, which we can reproduce with math in the shader
        // I don't want to bother with managing texture arrays and their mappings
        if (renderer->GetDefaultLightRamp() != rampTexture_ ||
            renderer->GetDefaultLightSpot() != shapeTexture_)
            return false;
    }

    // Although analytic it doesn't make sense for a directional light to not cast-shadows except
    // in some really odd situations (non-photoreal)
    if (lightType_ == LIGHT_DIRECTIONAL)
        return false;

    // Must not cast shadows to be analytic ... because shadows aren't atlased
    return !GetCastShadows();
}
```
Atlasing shadowmaps opens up more modern options but it turns View into even more of a mess.

-------------------------

Eugene | 2020-07-25 09:42:31 UTC | #24

[quote="JSandusky, post:23, topic:6271"]
Low hanging fruit is to rework `View`
[/quote]
~~Phrases “rework View” and “low hanging fruit” cannot coexist in the same sentence.~~ 
I have tried to add stuff into View three times and I have failed miserably in two of there attempts. Did you have any success in implementing your suggestion? I mean, I know it’s possible to do if you need just this once scenario to work. However, is it possible to do without messing up any of existing use cases of View? Every time I’m trying to work inside View, I have to deal with hundreds of supported tiny features that tend to break off when I push too hard.

-------------------------

JSandusky | 2020-07-25 17:18:36 UTC | #25

Previous View guttings:
- Clustered shading
- Zone texture mixing (octahedral maps instead of cubes)
- Ditching the stored forward and deferred light passes
- Some compute for GPU culling
- Single-pass stereo


It's at most 2 hours of work, even less if hacked into  `CheckVisibilityWork(...)` and stored in a seperate "AnalyticLights" list in `PerThreadSceneResult` while ignored from the other. The rest of it is setting a shader-define (HAS_ANALYTIC_LIGHTS or w/e) and shader-constants.

Done more correctly a blob of analytic lights pretty much just follows along the existing vertex-lights doing nothing remarkable that isn't already done. The only real wierdness is if there's a need for analytic lights to also be included as regular lights in some other lighting pass .. that might get weird.

-------------------------

GodMan | 2020-07-25 18:09:26 UTC | #26

I have no idea what you guys are talking about 🤣🤣.

-------------------------

GodMan | 2020-07-26 19:16:29 UTC | #27

Does anyone have any screenshots of PBR in a game setting with urho3d? 

Just curious of the results.

-------------------------

glebedev | 2020-07-26 21:59:15 UTC | #28

https://discourse.urho3d.io/t/random-projects-shots/2431/220

-------------------------

GodMan | 2020-07-27 01:46:03 UTC | #29

looks like forward rendering without PBR.

-------------------------

glebedev | 2020-07-27 07:52:32 UTC | #30

Well, it's forward rendering with pbr shaders...

-------------------------

glebedev | 2020-07-27 08:29:14 UTC | #31

What exactly are you looking for? My unity 2 urho exporter converts unity pbr setup into urho pbr so I can easily make a sample scene to demonstrate Urho3D pbr capabilities.

-------------------------

Dave82 | 2020-07-27 13:05:54 UTC | #32

I think what he was trying to say is that the scene doesn't look pbr-ish. The materials are very bland. They look like a simple Diff.xml technique. I don't think it's worth overheating your GPU for results like this. You can achieve similar results with a simple DiffNormalSpec technique with no impact on GPU. Also the SSAO is not very noticable.

Maybe you could make a scene with more metal and stone materials to have more reflections and specular mapping

-------------------------

Modanung | 2020-07-28 00:14:52 UTC | #33

I have little experience with PBR, but it seems to me like HDRIs would be a requirement for realistic results. Use of normal-range images could explain the bland lighting.

-------------------------

GoldenThumbs | 2020-07-28 01:02:00 UTC | #34

Yeah, we have been talking about adding support for loading HDR image formats. Like, currently [Radiance HDR images](https://en.wikipedia.org/wiki/RGBE_image_format) can be loaded in Urho (thanks to stb_image) but are loaded loaded as rgba8 due to how the image loading functions work.

-------------------------

Modanung | 2020-07-28 01:16:32 UTC | #35

The ability to use resources straight from [HDRI Haven](https://hdrihaven.com/hdris/) would be logicool. :sunglasses:

-------------------------

glebedev | 2020-07-28 09:22:39 UTC | #36

If you have an asset with such scene I can import it into Urho. A gltf from sketchfab or a link to free Unity asset will suffice.

-------------------------

glebedev | 2020-07-28 09:24:00 UTC | #37

I've imported a HDRI Haven sky previously into Urho using spehere mesh and skydome shader... Is there anything else to it beside internal 8 bit rgb representation?

-------------------------

Modanung | 2020-07-28 11:07:49 UTC | #38

[quote="glebedev, post:37, topic:6271"]
Is there anything else to it beside internal 8 bit rgb representation?
[/quote]


Maybe not. :upside_down_face:

-------------------------

glebedev | 2020-07-28 12:27:24 UTC | #39

![image|690x393](upload://zXhSqE1R47jIVzOjsvgp3CXZh9k.jpeg)

-------------------------

extobias | 2020-07-28 14:05:42 UTC | #40

That looks gorgeous! 
Any chance of a video?

-------------------------

glebedev | 2020-07-28 15:28:31 UTC | #41

I'm not sure if a video is better than a screenshot in this case...
https://gyazo.com/fcfb29d8e4cba6041703ceefa1bd4e34

-------------------------

GodMan | 2020-07-28 17:41:36 UTC | #42

Yeah that looks alot better. Is that all PBR shaders?

-------------------------

glebedev | 2020-07-28 18:19:57 UTC | #43

Yep. I've added support for HDRP/Lit shader. The scene is supplied in HDRP setup. I've switched off all light sources but directional (sun) and added fog similar to the original scene.

-------------------------

GoldenThumbs | 2020-07-28 23:05:52 UTC | #44

Not really internally, it's more just how the image is loaded by the engine. RGBE images have use the E channel as an exponent for a given pixel so you can get high dynamic range without needing higher precision. I'd have to look at the internal workings of both stb_image and the image class but I don't think that the texture you wind up getting in Urho3D is HDR. The image class doesn't support that. I'll give an update after I check.

-------------------------

Dave82 | 2020-08-18 07:49:21 UTC | #45

I think PBR rendering is already past... Just saw the UDK 5 demo and i was completely blown away. This technology is just ublievable ! No normal maps , no baked lights no specular maps no worries about poly count just focus on creativity and art ! Also the extreme procedural intelligent animation system will save enormous time so you don't need to waste time on hunting/cleaning mocap files. I hope new open source engines will be based on this sort of technology...

https://www.youtube.com/watch?v=qC5KtatMcUw

-------------------------

glebedev | 2020-08-18 08:22:17 UTC | #46

I'm quite sure PBR is still there. Also the "Nanite" tech isn't for characters.

Procedural animation... What Urho needs is a IK character setup (at least similar to Unity) to do this: https://www.youtube.com/watch?v=KLjTU0yKS00

At least this way you won't need a set of animations for bipedal characters as it could be calculated in runtime.

-------------------------

GoldenThumbs | 2020-08-18 20:43:59 UTC | #47

It's amazing tech, but some of their claims are a tad misleading. They actually still use normalmaps in quite a few of those assets, but they are more just scratches and stuff, super small detail that's harder to be carried by geometry even if it's a super dense mesh. Pretty sure they are still use gloss/roughness maps because they aren't simulating light bounces at a microscopic level. I think Urho could really benefit from some form of realtime bounced lighting, but that's not exactly something that most indie devs will need. Most people are totally fine with baked GI. (that being said, Godot is getting a neat new RT GI in addition to updates to their existing system.)
I really think there needs to be a good look and evaluate some of the more basic aspects of the renderer. The already mentioned HDR texture loading is an issue, I think I saw someone mention the possibility of clustered lighting. I see a lot of people complain about the current Urho UI, perhaps we can evaluate the idea of either overhauling or replacing the UI functionality.

-------------------------

jmiller | 2020-08-21 13:56:36 UTC | #48

12 posts were split to a new topic: [UI - discussion](/t/ui-discussion/6338)

-------------------------

GoldenThumbs | 2020-09-21 22:56:19 UTC | #60

Forgot to give an update on this. stb_image converts radiance images to HDR automatically, which means that once you actually get the image in Urho it's still LDR *and* you don't even have access to the E channel to do the HDR conversion manually in a shader.

-------------------------

