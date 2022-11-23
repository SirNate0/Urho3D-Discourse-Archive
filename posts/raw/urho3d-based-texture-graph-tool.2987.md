Sinoid | 2017-04-07 05:25:34 UTC | #1

An older build based on the Urho3D Qt based editing code I released just recently has been published.

Requirements: Windows 7+ and OpenCL capable CPU or GPU drivers.

https://github.com/SprueKit/TexGraph/releases/tag/0.1

This build is quite old (February 2nd) and is either from just before the end of commercial testing or shortly after it (might have been last response), so it should be reasonably stable - though some things like Art-Noise still don't work correctly. So much has changed since then.

Yes, compared to Substance the graph evaluation is quite slow. Unfortunately, they have a patent on every sane approach to speeding it up, including shared CPU/GPU memory.

Newer builds will be released periodically, probably as soon as a few days and I'll update this thread with a basic walkthrough of how to use the tool.

It is based on the same framework I pushed to github recently (using some still unpublished elements, though it's actually quite out of date). This will also help anyone trying to use that code on showing what they need in their output directories.

---

Next build adds Uber-Noise (per No Man's Sky), Polar->Cartesian, Cartesian->Polar, and other helpful nodes.

---

Code release is on hold, it's intended to be used as a galvanizing point on funding SprueKit's part library. Builds will come through still though. Report bugs either to this thread or as issues to the github project where the code will eventually land.

-------------------------

Sinoid | 2017-04-07 05:35:20 UTC | #2

Correction, this build lies - it's PBR Rough-Metal only and uses sRGB textures, so all of the PBR shading is off by ^2. I'll push a newer build soon.

-------------------------

smellymumbler | 2017-04-08 00:12:52 UTC | #3

Can the final textures be saved as a JSON, or other serialized format, and executed during runtime? This way, a game can be packaged with 100% procedural textures, instead of a bunch of bitmaps.

-------------------------

Sinoid | 2017-04-08 04:30:00 UTC | #4

Yes. Though one would have to be mindful of their target resolutions. Generating 4k or 8k textures is quite slow - as nodes incrementally get OpenCL support it should get much better.

They can be saved as XML or binary. Binary is only recommended for executing at runtime to skip parsing text.

-------------------------

Sinoid | 2017-04-09 05:04:50 UTC | #5

I've pushed a new build that now exposes permutations. Historically, permutations are what I was really after when I started this tool, I wanted a texture graphing tool that let me architect my color schemes without resorting to palettes and tag things based on abstract notions, I was also bothered that there are no MIT'd or similarly liberal licensed texture graphing libraries out there - so I made my own tool and it grew into a monster.

PBR works for rough/metal and gloss/specular-color, also HOM displacement mapping works for height as well. The more expensive HOM shader is only used if there is a height texture output and if it is not a constant value, so pure white height is "free."

https://github.com/SprueKit/TexGraph/releases/tag/0.2

You can access permutations using the "ticket" buttons in the property editor. For those hard of sight - the left-most button (ticket and pencil) quickly records your current setting as a permutation without a name or flags, and the second button (ticket) opens the permutation editing window where you can add, edit, and delete permutations. Or set the value to match a permutation (ticket and arrow button, below trashcan).

Special thanks to JTippets, I'm using his noise library for the FBM and Perlin noises. As well as to Aster, his Qt scroller widget from that particle editor is used almost everywhere.

-------------------------

johnnycable | 2017-04-17 16:32:25 UTC | #6

Hello, can you share some examples? I've tried the first release (second one gave me a dll error on win) but I've been stuck about the workflow...

-------------------------

Sinoid | 2017-04-18 03:46:39 UTC | #7

Next build will have a few sample textures and a tutorial/walkthrough (1 - 2 days out).

Could you open an issue with the DLL message on Github (https://github.com/SprueKit/TexGraph/issues). I'd assume that you're just missing the MSVC2015-x64 runtime if the older build runs but the new one does not, compilers were changed recently.

-------------------------

