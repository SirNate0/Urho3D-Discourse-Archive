Taqer | 2019-07-08 22:11:19 UTC | #1

Hello, I wonder how I could optimize rendering big count of objects with the same model, but different material parameters?

I was trying to use StaticModelGroup, but I guess it doesn't support modifying materials per instance?

What different approach could I try?

Thanks.

-------------------------

S.L.C | 2019-07-09 05:49:54 UTC | #2

Is this a Minecraft-like project? If so, just mention that. Because there are other methods for optimizing that case.

-------------------------

Modanung | 2019-07-09 08:04:47 UTC | #3

You can still use a `StaticModelGroup` if you manage to incorporate the variation within the *shader*.

-------------------------

Taqer | 2019-07-09 12:15:10 UTC | #4

@S.L.C no, its isometrical 3D flat tile map, where tiles blend with each other. I will try @Modanung way, and see how it will help.

-------------------------

Taqer | 2019-07-09 12:49:17 UTC | #5

@Modanung but what do you mean by `within the shader`?
There is how my blending works:
![obraz|313x283](upload://dxyoJr3JgP2erbAt75ViwaSRH71.png) 
It blends with all neighbour, by setting appropriate flags in material, then shader according to those flags applies specified masks and paints those masks with specified texture.

I think if I would use `StaticModelGroup` I would need to have instance for every combination, now I have 3 terrain types so I would need to have `3 * 2^8 = 768` groups, more if I will add new terrains, and I plan to.

How much will it optimize then?

-------------------------

Modanung | 2019-07-09 12:59:04 UTC | #6

[quote="Taqer, post:5, topic:5289"]
what do you mean by `within the shader` ?
[/quote]

That the GLSL/HLSL code would handle this instead of a material attribute. I'm no expert on this at all, maybe someone else could provide more clarity. I just know it's a technical possibility that I would like to explore someday.

-------------------------

SirNate0 | 2019-07-09 16:08:50 UTC | #7

I think if you look into tri-planar mapping it might give you some insights in how to approach the problem. Maybe encode the terrain type in the vertex color or normal, and then blend between those in the shader, in a way similar to the tri-planar approach.
Potentially there are some further simplifications that you could make so that a bunch of static model groups would also work: if the tile down is orange, then divide that time into 9 squares. The center one is fully the color of the tile. The outer ones in the center only have to blend between 2 squares (the top center one blends neighbor 2 and the tile itself). The corner ones then blend 4 tiles (top right would blend 4 tiles: 2, 3, 5, and self). Ignoring rotations, I believe that should be 3 + 3^2 + 3^4 = 93 different sets. If you optimize for rotations and such you can probably reduce the result further (e.g if we're blending between the same tile types, that is really the same as being fully that tile). One thing to note, you need to decide how you will handle ambiguities - if you have orange on 2 diagonal corners and red on the other two

> o r
> r o

then which of them will connect in the middle, red or orange?

Also, look into the [marching squares](https://en.m.wikipedia.org/wiki/Marching_squares) algorithm, perhaps it will give you additional insight into possible approaches

-------------------------

