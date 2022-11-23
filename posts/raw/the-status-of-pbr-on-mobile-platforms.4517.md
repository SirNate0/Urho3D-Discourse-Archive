WangKai | 2018-09-03 06:06:16 UTC | #1

What's the status of PBR on mobile platforms (Android & iOS)? Does it usable? How about the performance?
As we know UE4 and Unity has pretty good support of PBR on mobile.

Thanks!

-------------------------

jmiller | 2018-09-03 09:50:43 UTC | #2

Hello,

42_PBRMaterials sample demonstrates PBR and should provide some answers.
Also there are some semi-active threads/posts on [url=https://discourse.urho3d.io/search?q=PBR]PBR[/url]/IBL with more specific information.
..and others can probably offer more info on this.

-------------------------

smellymumbler | 2018-09-03 16:41:24 UTC | #3

I don't think it works well even on desktop. I would stick to the standard rendering mode if you really want performance. Not really a big deal, to be honest.

-------------------------

WangKai | 2018-09-05 02:44:43 UTC | #4

Urho is great and it needs roadmap. Instead of C++ new features, it needs solid features. Something like better editor, better scripting, graphics features, compatibility... otherwise it's fading though nobody likes to see.

-------------------------

smellymumbler | 2018-09-05 14:01:36 UTC | #5

Why do you think the engine needs a better editor? The current editor is easy to use, written in a scripting language, and you can easily extend to add game-specific stuff in there.

Or better scripting? You have AS and Lua. What would be better? JS? Why?

-------------------------

Modanung | 2018-09-05 14:16:10 UTC | #6

@WangKai For that the project would need more developers with enough expertise and knowledge of the engine and those fields to implement and maintain these features. Also things take time, especially when done well.
In it's current state I'd prefer Urho staying stable (and lightweight) instead of moving fast. But then again, I don't miss anything in its features. Also, with about 1.5 new topics a day (in the last seven days) and the constant activity on GitHub - which is naturally dwarfed by @cadaver's contributions - I don't see this project fading any time soon. To me it registers as glowing steadily.

-------------------------

Modanung | 2018-09-05 19:43:01 UTC | #7

There's several editor projects running separately from the engine development, btw. Maybe some day there will be official/qualified editors for Urho3D listed on its website (like the [ParticleEditor2D](https://urho3d.github.io/documentation/1.7/_external_links.html)) instead of a single all-purpose one. The editor you want depends on the game you are making. [Edddy](https://gitlab.com/luckeyproductions/Edddy), for instance, focuses on worlds that are (mainly) based on reused gridlocked blocks. If you're making a 2D game and are working with tiles, you'd probably use [Tiled](https://www.mapeditor.org/) for most of your world creation.

-------------------------

WangKai | 2018-09-05 14:32:53 UTC | #8

Yes, the current editor is good, but should be better. The workflow is just not that right. That's why so many ppl are reinventing the wheels. As for the scripting, we need IDE, at least a debugger, auto-completion, however, different ppl have different opnions about these and I'm OK with that. It's about how high you put the standard bar.

I love Urho, it has very great foundation and clean code. I'm also trying to make the things around it better, though my spare time is so limited.

-------------------------

Modanung | 2018-09-05 14:38:21 UTC | #9

Have you tried [CodeLite](https://en.wikipedia.org/wiki/CodeLite) as scripting IDE?
I have not. I use QtCreator to write C++ in, and see no reason to write in a second language with similar functionality.

[quote="WangKai, post:8, topic:4517"]
...though my spare time is so limited
[/quote]
And such is the life of many.

-------------------------

WangKai | 2018-09-05 14:52:51 UTC | #10

One of the most important purpose of scripting is to make development faster, however, IMHO, AS is not every fast for me, especially if there is no debugger and IDE. For C++, we have very powerful and familiar IDEs and debuggers, so, basically, AS is not as good as C++ in real world just as you mentioned. So, we need to improve scripting of Urho.

Edit: the best part of Urho's scripting is hot reload. We can even sent script file via networking or adb to the device and make the iteration super fast!

-------------------------

Modanung | 2018-09-05 15:08:45 UTC | #11

I see you're already improving the editor, btw. So I guess it's just a matter of time before your entire wish list is implemented. ;)

-------------------------

smellymumbler | 2018-09-05 17:41:48 UTC | #12

The workflow doesn't feel right because it's not yours. That's what @Modanung meant by saying that the editor depends on the game you are making. You can't have a general purpose editor that checks all the boxes. Since Urho is not a commercial engine, there's very little benefit in trying to be something like Unity and make something that is "good enough" for 80% of the people.

People are not reinventing wheels, they making the wheels that make them more productive on their field. What they need are stable, efficient and mature building blocks to create as many wheels as they want.

-------------------------

dragonCASTjosh | 2018-09-06 21:11:30 UTC | #13

So back to the original topic. When I first implemented PBR into Urho I didn't have access to any mobile devices outside of a Windows phone. Since then I have gone out and brought myself a tablet dedicated to mobile testing. If I remember right there was some issues with cubemap filtering on gles2. I plan to look into gles3 support for the engine as a priority over getting it working on gles2, maybe after the that I can look into bringing it to gles2 if there is demand. Because of this the features likely won't get merged to master as it breaks the philosophy of device compatibility.

-------------------------

WangKai | 2018-09-09 02:07:32 UTC | #14

Thank you! I understand all the wonderful contributions and as well as difficulties. Urho's PBR till now is very cool and hope one day it can be stable and stunning out of box. It's always harder to do than to complain.

-------------------------

Sinoid | 2018-09-11 03:18:39 UTC | #15

On mobile you might want to consider some heavy tweaks:

- Pack your roughness, metalness, etc into RGB565
     - Requires adding that in engine though, you really want it to stay as rgb565 at upload
     - DDS path might already cope with it though
- Use 32x32 normalized LUTs for the BRDF (ie. min roughness is 0.3 and max is 0.7, here's your LUT)
    - You'll notice the bit-depth of RGB565_UNORM is just barely more than enough to perfectly hit a 32x32 LUT by roughness
- You have to rewrite the shaders to account for the LUT
    - This will probably make them cleaner
- You have to introduce some tooling to do that quantize
- There are better options, but this is the easiest one

If you need to see what that actually looks like in action then look at *Shin Megami Tensei: Liberation Dx2* which uses this method.

IBL is the big problem, drop the mip-access for diffuse IBL and instead use a lerp of two-hemispheres. Leave specular IBL as is but drop the roughness correction.

Also, on mobile/hand-held you want to turn off `Reuse Shadowmaps` as those platforms hate switching rendertargets so you want to get your shadowmaps done first (ideally you don't even use shadows). You have to judge that though, not reusing them eats memory which might not be there.

---

What really needs to happen is a *render performance test* to automatically configure how Urho3D should run and at what resolution. Sounds easy ... isn't easy.

-------------------------

