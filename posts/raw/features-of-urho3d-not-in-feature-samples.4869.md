I3DB | 2019-01-25 21:28:18 UTC | #1

Have worked through the feature samples, and starting to get a basic understanding of Urho3D's capabilities.

Are there other features or things the Urho3D platform does, things not exhibited in the feature samples?

You know, the guts of the engine on display? Some 3rd party library already integrated that isn't used in those samples?

Or are the FeatureSamples relatively good coverage of Urho3D?

In  the course of working through those samples, put them all into a single voice driven application along with a scene manager and an automated demo mode to display them. Also worked in additional features native to hololens and windows UWP, including the hololens samples done by @Egorbo. There's no mouse with hololens (but there is a clicker, which I don't use), so needed a different method of input.

Then added a series of actions that work across all the samples, such as scene controls and basic first person shooter. So you can throw things at the pyramid, or shoot ragdolls en masse or individually, or paint decals or flowers on any object. 

Worked through numerous issues, not all of which are solved, such as lack of shadows. Got most of the materials and models, including the PBR materials and water working. Though had to use some workarounds due to the SharpReality binding implementation using StereoApplication as the base application interface. Will put up a project showcase in the next couple weeks. Want to see if I can work through some of the remaining issues, and maybe put a little bit of lipstick on the pig that it is.

But anyway, some of those feature samples viewed via the hololens are really stunning. When new users see the automated demo, most of them stand there with their mouths open and don't know what to say, their brains are overstimulated. Experienced VR users seem rather non-plussed, but note the difference between VR and AR immediately. Various researchers put AR as a smaller subset of VR, but after viewing these demos, it would seem most agree VR is a smaller subset of AR.

-------------------------

Leith | 2019-01-27 04:22:16 UTC | #2

There appears to be mountains of stuff that is either not well documented, not displayed in existing samples, or both.
I'm quite new to Urho3D, but not to game engines, or engine development.
I've personally struggled to absorb the entire codebase in response to the lack of information in the public domain, but the local inhabitants of this forum are generally quick to respond with useful information for any use-case I have put forward.
I have to note, I do not use SharpReality, and tend not to use scripting in general.
To me, learning script bindings is just another layer of complexity on top of learning how the engine works - a separate API, with different naming conventions and different limitations.
I'm happy that I can work with a data-driven scenario, for most use-cases.
Just yell if you need help with something specific, but I suggest you do be specific, otherwise your generic question will receive a generic response.

-------------------------

I3DB | 2019-01-27 04:31:30 UTC | #3

[quote="Leith, post:2, topic:4869"]
There appears to be mountains of stuff that is either not well documented, not displayed in existing samples
[/quote]

Could you be more specific, just one or two items or features that aren't in the Feature Samples?

I'm not so much asking for help for some problem in this thread, as I am asking if there are features I'm still unaware of, and that I can dig into and work into a demo. My working knowledge is mostly around the Feature Samples.

I wrote too much above, but here is the short version

[quote="I3DB, post:1, topic:4869"]
Are there other features or things the Urho3D platform does, things not exhibited in the feature samples?

You know, the guts of the engine on display? Some 3rd party library already integrated that isn’t used in those samples?

Or are the FeatureSamples relatively good coverage of Urho3D? [And these are the samples referred to.](https://github.com/xamarin/urho-samples)
[/quote]

-------------------------

Leith | 2019-01-27 04:36:10 UTC | #4

How about the Wind Mushroom for starters?
We have no demo of using decals for splats, because Particles don't have collision testing.
There's a lot more I can think of, but I tend to wander into my own use-cases and not generic ones - for example, we can perform various queries on the octree, and get really nice results for example we can get the UV on a triangle of a model we raycasted, but we can't convert the UV easily back into barycentric coordinates which I presume yielded that UV result.

I add that our PBR sample has insufficient error checking, as it appears black most (but not all) of the time on multiple target platforms.

-------------------------

Leith | 2019-01-27 04:57:28 UTC | #5

Hell I am not even sure if we even accepted stb_perlin (MIT licensed) and implemented on it or not. And there are zero examples of custom render pipes, given we can.

-------------------------

I3DB | 2019-01-27 05:18:42 UTC | #6

[quote="Leith, post:4, topic:4869"]
We have no demo of using decals for splats
[/quote]

I've worked this into my demos using raycasting. Works nicely. 

When the splat also gives impulse, say like with a bullet shot, there are interesting effects that can be done. Works really nicely with ragdolls, the pyramid physics samples and physics stress test test. Ragdolls are fun to shoot, and the impulses are rotational around an axis.

I've got the pbr sample running nicely. It's not perfect but fairly close. Most of my issues were in reading the scene file, and missing materials/techniques, etc. Once I figured out how to load the scene file (needed edited for hololens which can't digest scene elements) the rest was easy just finding files and adjusting to make it look good in AR on the hololens.

Also the basic techniques sample offers a custom material (which is missing the hlsl shader), and a custom render pipeline. Adds in bloom and fxaa, and hdr for emissive, if I'm understanding you correctly.

I'll look into the wind mushroom. Sounds sort of interesting, assume it's a mushroom in strong wind?

Edit: Actually had that model ready to go, and stuck it into the billboards sample.

The mushrooms sort of wave in a large circle. More like in a vertex than in strong wind.

I think it will look better with some stationary shrooms and some blowing around like that.

-------------------------

Leith | 2019-01-27 05:14:48 UTC | #7

I implemented decal splats in Unity, but I was never happy with them. I am considering rewriting splatting based on my old terrain painting demo.

-------------------------

Leith | 2019-01-27 05:16:45 UTC | #8

The wind mushroom material is a mushroom in a wind zone, which we don't have - it needs to take influence from a texture and is implemented as a vertex shader.

-------------------------

I3DB | 2019-01-27 05:21:13 UTC | #9

[quote="Leith, post:8, topic:4869"]
The wind mushroom material is a mushroom in a wind zone, which we don’t have
[/quote]

Apparently I have it because they're moving.

-------------------------

Leith | 2019-01-27 05:31:31 UTC | #10

Issue PR!
We need to see this stuff in the samples.

The samples are not good enough to learn the engine alone, but each sample helps a new user to understand the workflow and gear toward it.
The sample are worth ten times the comments in headers that make it into the doxygen.

Before I was a 'proper coder', the best way I could learn was from example.

-------------------------

Modanung | 2019-01-27 11:49:20 UTC | #11

Note that instead of adding to the list of samples it is also possible to extend Ninja Snow War.
@I3DB Please keep in mind that UrhoSharp and Xamarin are _not_ affiliated with Urho3D. Urho3D does not support C#. If there's samples missing from UrhoSharp, Xamarin should fix that, not the Urho3D community. Honestly you're lucky to have your questions answered _here_, since UrhoSharp is a derivative with its [own forums](https://forums.xamarin.com/).

-------------------------

I3DB | 2019-01-27 15:17:29 UTC | #12

[quote="Modanung, post:11, topic:4869"]
Honestly you’re lucky to have your questions answered *here* , since UrhoSharp is a derivative with its [own forums ](https://forums.xamarin.com/).
[/quote]

Yes, I understand my luck by getting help on these forums. 

The reason for posting here is posting on the xamarin forms is by and large a waste of time. Yet, overall, the c# integration is well done. Most of the people that do post there have no idea what Urho3D even is, and cannot provide assistance. Every now and then something useful happens, rarely.

My goal is a bit different, I'm not really trying to fill in xamarin's missing samples. That is not what this thread is about. Not what my work is about.

I'm trying to exploit all the features available from Urho3D, and put those features on display in a hololens. 

**This thread is about finding features that aren't on display currently in the Urho3D samples whether in c++ or c#.**

What does Urho3D do that no one is familiar with? Maybe some rarely used library that ends up being a real gem when used in AR?

There is a Shooty Skies game also, that appears as the Samply game in the c# samples, and I've got it running stand alone just not fully integrated to work with my samples demo. 

I'll check into the Ninja Snow War, though have been writing code that runs on the hololens platform and Ninja Snow War may not, though am already using the model from that game in one of my demos without any problems.

Also, this is good advice ...
[quote="slapin, post:55, topic:3261"]
Also, I’d suggest making own technique demos. So if you want some feature in your game,
make a small demo for that feature, with everything as simple as possible. That will make your
learning less frustrating.
[/quote]

This more or less, is what I've been doing.

-------------------------

Leith | 2019-01-28 05:08:26 UTC | #13

We could use some more UI examples - I struggled to learn about the Menu element today.
I had to resort to poking around in the Editor Scripts to figure stuff out.
The editor itself is currently highly unstable on Linux, and not a useful tool for me (unless I dualboot into Windows, just to be able to use the editor for stuff, which is not very likely - have not used Windows in some time now)

-------------------------

Modanung | 2019-01-28 09:37:24 UTC | #14

[quote="Leith, post:13, topic:4869"]
The editor itself is currently highly unstable on Linux
[/quote]

I believe this is a relatively fresh issue: You should be able build an earlier version and use its stable editor.

-------------------------

I3DB | 2019-02-12 16:56:15 UTC | #15

[quote="I3DB, post:12, topic:4869"]
This thread is about finding features that aren’t on display currently in the Urho3D samples whether in c++ or c#.
[/quote]

Here are two resources I found by reading various comments:

https://github.com/Lumak?utf8=%E2%9C%93&tab=repositories&q=urho&type=&language=

https://github.com/Enhex?utf8=%E2%9C%93&tab=repositories&q=urho&type=&language=

-------------------------

