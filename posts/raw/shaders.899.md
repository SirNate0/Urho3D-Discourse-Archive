hdunderscore | 2017-01-02 01:03:57 UTC | #1

For a while I was working on some physically based shaders, however I don't have so much time for them at the moment and I've noticed there are probably serious fundamental issues with the current work (not conservative? ouch), the work can be found here:

[github.com/hdunderscore/Urho3D/tree/shaders](https://github.com/hdunderscore/Urho3D/tree/shaders)

No need to recompile urho, just run Erun.bat in Bin/ to view a test scene (Press T and U to toggle between forward and deferred). Here's what you'll see:
[url=http://imgur.com/t2AcqtA][img]http://i.imgur.com/t2AcqtAl.jpg[/img][/url]

The work started off from: [github.com/larsbertram69/Lux](https://github.com/larsbertram69/Lux) 

Things that work:
[ul][li]HDR decoding from rgbm / rgbd generated with: [github.com/hdunderscore/cmft](https://github.com/hdunderscore/cmft)[/li]
[li]Forward and deferred (not prepass).[/li]
[li]GLSL and HLSL with hacktastic macros.[/li]
[li]IBL[/li][/ul]

There may be some other things hidden in there that could be salvaged.

If I had time I would:
[ul][li]Re-write the lux related source into a something more like what Epic demonstrated in their presentation (have brdf and specular contribution code separated so that they could be easily swapped out), and probably pick up some other things such as metalness-roughness and the optimisations they highlighted. Ideally during this process conservativeness would be achieved.[/li]
[li]Rework the lights, adding support for more variety[/li]
[li]Fix the parallax corrected cubemapping to not be locked to axis-aligned (and maybe pick up more generic shapes described here: [seblagarde.wordpress.com/2012/0 ... d-cubemap/](https://seblagarde.wordpress.com/2012/09/29/image-based-lighting-approaches-and-parallax-corrected-cubemap/) )[/li]
[li]Determine performance impact of structs.[/li][/ul]

Micro-tutorial:
[ul][li]You'll need to make your own techniques/dive through the shaders for most things..[/li]
[li]Author using specular-glossiness workflow: In the specular texture: RGB = specular, A = glossiness[/li]
[li]Check your sRGB and HDR settings everywhere.[/li][/ul]

There are also many other things but the list would be very long.. Since I noticed in the Editor topic that we had so many individuals working on the same issue, I thought perhaps I'll share what I've got in hopes others interested in the same goal might step in to add to/salvage from/scrap the work here !

Good luck o>

-------------------------

cadaver | 2017-01-02 01:03:57 UTC | #2

Looking very nice!

Note that in the render-refactor branch, I've added some additional macros to make the same shaders work on D3D9 & D3D11. Mostly the changes have to do with VS / PS output variables, and texture sampling. But that shouldn't be too much of a change for your shaders once the branch is merged to master.

-------------------------

sabotage3d | 2017-01-02 01:04:00 UTC | #3

Looks great ! Do we have linear workflow in Urho3d, if we do these shaders will look even better: [renderman.pixar.com/view/LinearWorkflow](http://renderman.pixar.com/view/LinearWorkflow)

And some additional stuff for physically based shading: [renderwonk.com/publications/s201 ... ressed.pdf](http://renderwonk.com/publications/s2010-shading-course/snow/sigg2010_physhadcourse_ILM_slides.compressed.pdf)

-------------------------

rasteron | 2017-01-02 01:04:01 UTC | #4

This looks awesome hd_ !! keep it up :slight_smile:

-------------------------

Bananaft | 2017-09-09 10:06:45 UTC | #5

Hi, pardon me bumping this thread, but I'm having hard time following your steps.

I compiled your cmft fork, but dds cubemap I generated with it can not be opened by Urho or dds viewer or XNview. CmftStudio can open it, but saving it again doesn't help. Cubemaps from your source however are loading in Urho and viewers just fine.

Can you recall what format you used as input and settings you used to generate your cubemaps?

-------------------------

hdunderscore | 2017-09-09 14:24:06 UTC | #6

One of the weaknesses in the Urho workflow is the inability to directly load formats exported by cmft/cubemapgen etc. It's been a while since I've looked, but back then I had to use another program to load the exported cubemap and re-export it so Urho could load it.

I always thought it would be a good idea to make use of cmft's image loading/saving code in Urho3D, as it appears to be very well written and comprehensive in formats covered. I never got around to making it happen though. After that, it would be a natural step to include cmft as a tool for cubemap convolution.

-------------------------

Bananaft | 2017-09-09 19:40:43 UTC | #7

Thank you, I was able to do it, with gimp plugin, but only with dxt5 compression. Without compression it still does not work.
But I discovered, that after cmft I can covert dds to png and let Urho load it as cubemap and generate mipmaps. Which is kinda cool, becase it is lossless, and I thought, that rgbm mipmaps has to be precalculated in a special way, turns out, they are not. (no brdf mips though)

[quote="hdunderscore, post:6, topic:899"]
as it appears to be very well written and comprehensive in formats covered.
[/quote]
Well, apart from output, I also having quite some troubles with input formats, it does't support PNG or TIFF, wont open my EXRs, and TGA  does not have 16bit support. Leaving me only with HDR, which works but has some weird artifacts.

Boy, what a great and fun weekend I'm having! :slight_smile: .   .   .   .    :confounded:.   .   .   .    :sob:

-------------------------

