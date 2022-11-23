GoldenThumbs | 2021-11-06 02:48:31 UTC | #1

So DDS saving is already in the engine, which is great, but what's not-so-great is not being able to use compression. I've been working on adding filtering reflection probes (zone cubemaps) to the editor, but I'm worried that a lot of cubemaps could take a lot of memory... I'm unsure how well compression would play along with the HDR encoding/decoding method I'm using (simple rgb-alpha-channel-is-a-multiplier stuff) but I'd like to be able to try it out. At the very least it might be useful somewhere else. Thoughts on this idea?

-------------------------

SirNate0 | 2021-11-06 13:04:23 UTC | #2

Here's a list of some image libraries. I believe the Developer's Image Library supports saving compressed DDS files if you want to integrate that into your editor, though there might be one or two others that do as well.

https://www.khronos.org/opengl/wiki/Image_Libraries

Though if you just want to try it out, I'd just use a tool to do the conversion. Save as a bunch of PNGs for one run, find a tool that can batch convert them and convert them all, and then load the compressed files and check how the compression effects the quality in a second run.

-------------------------

GoldenThumbs | 2021-11-06 20:38:53 UTC | #3

> Though if you just want to try it out, I’d just use a tool to do the conversion. Save as a bunch of PNGs for one run, find a tool that can batch convert them and convert them all, and then load the compressed files and check how the compression effects the quality in a second run.

Don't know how I didn't think of that... Well, Gimp doesn't load the mipmaps Urho saves in a DDS file so I'd have to export each mip for each face individually, which would be a pain.

-------------------------

JSandusky | 2021-11-07 02:59:43 UTC | #4

For BC1-3 you can use stb_dxt to compress all of the blocks. Done. There's no BC4 support in urho reading wise.

Of course you have to setup the header to report the right format.

-------------------------

GoldenThumbs | 2021-11-07 03:03:03 UTC | #5

Would be nice if it was properly supported by the engine, which is what I'm suggesting here. I'm competent enough at C++ and reading documentation to add this on my own, I'm trying to get people to discuss the merit of this addition. I think it's a pretty clear improvement with not really any downsides (that I can think of anyway), but I was wondering if there'd be any reasons *not* to make a PR of this.

-------------------------

JSandusky | 2021-11-07 06:14:24 UTC | #6

There's no huge reason not to ... there'll be merits or demerits on the specifics. ie. stb_dxt will get it done, but it's a lot of func-call/mem overhead (to build the 4x4 block at minimum). Other compressors may have different merits.

If you need it, then just do it.

-------------------------

