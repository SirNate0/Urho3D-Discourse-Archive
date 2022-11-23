slapin | 2017-03-27 03:42:21 UTC | #1

Hi, all!

I want to merge a few small tiled textures into one to save on batches. These are quite small and all
of them merged are under 512x512. A problem is that they are tiled, and I want to
them to still have this feature.
with current 512x512 atlas I try to use top-left 256x256 part as tiled texture.
I try to do Vector2(u % 0.5f, v % 0.5f) to avoid problems but I get messed-up image with these.
When I use original 256x256  texture, and not using % operation everything is textured very well.
Any ideas?

-------------------------

SirNate0 | 2017-04-13 06:22:23 UTC | #2

I'm not sure you actually can do it that way - perhaps with a custom shader to do the wrapping to a subsection of the atlas, but I've never tried it, so I can't say for sure. I would suggest seeing if you can to it with an array texture, add I think that should have the same benefits you want. Preferably someone else has a suggestion, as I've wanted to do the same thing, but haven't thought of a way to do it (nor had the will to sit down and try).

I will say, you likely have to multiply the original UV cord by 0.5 first. And this is probably something you'd have to do in the pixel shader...

-------------------------

