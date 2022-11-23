Alan | 2017-08-30 12:15:24 UTC | #1

Hey there :slight_smile:

I'd like to know what's the best approach to render pixel-art pixel-perfectly :stuck_out_tongue_closed_eyes:, with some simple math it's easy to map texture pixels into pixels on screen, or into 4 pixels and so on, but when your geometry isn't perfectly aligned to the pixels, you get different results depending on the position of them, I guess mostly due to rounding error in the sampler (with vertex imprecision accumulated). I've seen two different approaches for that, possibly the simplest one is snapping the nodes themselves to pixel-perfect positions, that's what Nez does, but it obviously impacts the game logic, the other approach is using some kind of visual-only pixel snapping technique, which you could do in the GPU by snapping solely the vertices in the VS, but depending on the situation, if you're dealing with imprecise numbers (far from zero), you may get floating point precision problems like some vertices rounding down and some rounding up. I've also seen snapping on the PS on top of that, what sounds more complicated than it should to solve such a simple problem.

The idea here is to render a rather low-res texture and display it on screen, mapped proportionally to the screen pixels so pixel art looks good and is cheap to render.

Any help on this? Thanks in advance! :blush:

-------------------------

