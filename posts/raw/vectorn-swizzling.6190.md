SirNate0 | 2020-06-03 18:42:55 UTC | #1

What would you think of adding swizzling to Vector2/3/4 through something like this?

https://kiorisyshen.github.io/2018/08/27/Vector%20Swizzling%20and%20Parameter%20Pack%20in%20C++/

or

http://jojendersie.de/performance-optimal-vector-swizzling-in-c/

-------------------------

Eugene | 2020-06-03 23:13:10 UTC | #2

I think every person (me included) who knows shader languages (at least a bit) get this idea at some point: "I want swizzling in my C++ math library!". At the end of the day tho, I don't believe it's that useful.

Swizzling exists in HLSL/GLSL out of necessity. One has to write efficient and readable code with optimal memory layout. Swizzling helps there a lot, I won't argue.

In C++ tho? When one have good optimizer and much less restrictions (e.g. functional stack instead of registers)... I don't believe it's needed. Maybe it's just my biased experience, but I know only _one_ place that will benefit from it -- converting (x, y, z) to (x, z). Does this syntax simplification really worth having a huge chunk of template magic in math code? Don't think so. I'm asking myself: "how will it help a person to make a game", and I fail to find an answer.

-------------------------

