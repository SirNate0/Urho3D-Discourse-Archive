spwork | 2018-04-12 03:06:35 UTC | #1

![timg|448x252](upload://yTXvxGdPaLy3wgUzfydexvPNedd.jpg)

-------------------------

Leith | 2019-02-10 05:40:10 UTC | #2

This is usually done by alpha-blending a 2D sprite to represent the lit area, similar to a smoke particle.
In your case, it appears that there are two passes, one is using subtractive blending to darken large areas, and the other is using additive blending to lighten smaller areas within the dark areas. I've recently brought up the possibility of testing, and possibly adding support for "dark lighting" to our 3D lighting scheme, which is as simple as making the light intensity be a signed value, so should "just work" with no real changes to the engine.

-------------------------

Sinoid | 2019-02-11 04:11:20 UTC | #3

[quote="Leith, post:2, topic:4169"]
I’ve recently brought up the possibility of testing, and possibly adding support for “dark lighting” to our 3D lighting scheme, which is as simple as making the light intensity be a signed value, so should “just work” with no real changes to the engine.
[/quote]

When lights are rendered the blend-mode is set according to the sign of the brightness value. If negative the light be applied as subtraction, otherwise it'll be applied as the usual additive pass.

-------------------------

Leith | 2019-02-11 06:10:39 UTC | #4

I was so hoping to hear that! In this case, subtractive lighting is trivial :) I can start experimenting with that as soon as my player character animations are properly dealt with!

-------------------------

