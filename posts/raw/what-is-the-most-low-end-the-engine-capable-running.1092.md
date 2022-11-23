umen | 2017-01-02 01:05:24 UTC | #1

Hello all
im testing 3d engines for low end computers , the best results i had so far are with irrlicht 3d  the demos could run smoothly of really low p4 1 core pc with 1 giga ram .
the problem is that the engine is unsupported ..
 i wander what experience do you have with low end pc using this engine . 
Thanks

-------------------------

cadaver | 2017-01-02 01:05:24 UTC | #2

Performance depends on the content you're running, so the examples of different engines are often not comparable, and an absolute minimum is hard to give. The hard system requirement minimums are Shader Model 3 (AMD / Nvidia GPU's from 2005-2006 onwards), a CPU that can support SSE, and at least WinXP for Windows OSes. With some hacking you can downgrade the requirements to SM2 and no SSE.

I have no doubt that Irrlicht is better for very low-end machines and very old GPU's, as it can render in fixed-function (no shaders). Urho was never targeted for this.

-------------------------

umen | 2017-01-02 01:05:24 UTC | #3

Thank you very much for the answer.
do you have other ideas of engines that is targeting for low end pc's?

-------------------------

cadaver | 2017-01-02 01:05:24 UTC | #4

To get good performance on a low-end machine you most likely need an engine that is targeted for the game genre you want to be making, and that uses same techniques as the games of the era you want to be targeting as the minimum spec. For example: a FPS with lightmapped levels and no shaders, you could take the Quake3 source code (with GPL license limitations, obviously). 

EDIT: you'll also need to produce the content similarly as they did back then, as the old engines likely will not scale up well for more detailed levels & objects, or even higher powered machines (I recently replayed Unreal 2 and didn't get much above 100fps in most places, as the engine probably is single-threaded and almost completely CPU bound)

-------------------------

globus | 2017-01-02 01:05:24 UTC | #5

This comment (not answer or question):

a 2 month ago i look to "Legend of zelda: spirit tracks"
[img]http://i.piccy.info/i9/59fe67113cc1775dc474725d92a950ac/1433085011/108126/912050/zelda.jpg[/img]

I was very surprised and pleased
when look to spec of Nintendo DS game console:

Two ARM processors: 
32 bit main CPU 67 MHz
32 bit coprocessor 33 MHz

Memory: [u]4 MB, 656 KB of video memory, 512KB of memory for textures[/u]

-------------------------

GoogleBot42 | 2017-01-02 01:05:24 UTC | #6

I am not sure I would want to be the devs that had to work on that project. :laughing:  At least that only had to worry about targeting one very specific set of hardware.

The Nintendo 64 has some pretty sad specs too.  While the processors were just a bit faster I don't think it was actually faster at actually rendering due to the nature of the rendering system.
[url]http://en.wikipedia.org/wiki/Nintendo_64_technical_specifications[/url]

But the two are similar enough that a few games made for the Nintendo 64 have been ported by Nintendo for the DS.

-------------------------

globus | 2017-01-02 01:05:24 UTC | #7

Nevertheless, the developers managed to make interesting and popular game.

It's like Minecraft. Intresting gameplay does everything.

-------------------------

rogerdv | 2017-01-02 01:05:29 UTC | #8

I achieved around 20 fps in a GMA 4000, thats an old intel gpu (G41 chipset). Scene had a few buildings, animated models, a test particle system and two lights. Enabling FXAA2 cut 2-3 frames, FXAA3 didnt worked.

-------------------------

