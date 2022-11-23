evolgames | 2021-02-25 22:52:26 UTC | #1

Using directional lights produces shadows fine, but they seem to light up the sides of primitive 3d shapes in one flat illumination. If there are no textures, two sides of a cube can be lit exactly the same.
Point lights do not do this. I had an indoor scene with a spot light that worked out well. But for outdoor stuff I'm getting poor lighting results. Is there a better approach for soft sun lighting? I dont need light bounces or anything, just something that'll look better.
Bloom and effects help a bit.
Is it dumb to just make multiple suns at slightly different angles or have a giant point light?

-------------------------

Eugene | 2021-02-26 07:17:32 UTC | #2

[quote="evolgames, post:1, topic:6731"]
Is it dumb to just make multiple suns at slightly different angles or have a giant point light?
[/quote]
I did this. I mean, both. I added point light stuck to camera to add gradients, and I added a couple of directional lights to lit objects well from different sides.

Actually this is one of problems that inspired me to implement propper spherical harmonics, because ambilent SH are the real solution here.

-------------------------

