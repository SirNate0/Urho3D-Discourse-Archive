GoldenThumbs | 2019-06-29 23:23:24 UTC | #1

I noticed that there is a ViewProjection matrix and a normal View matrix, but no normal Projection matrix. How do I separate ViewProjection to only get the Projection?

-------------------------

ab4daa | 2019-07-01 12:36:35 UTC | #2

My first attempt may be

	mul(cViewInv, cViewProj);

-------------------------

GoldenThumbs | 2019-07-01 12:36:31 UTC | #3

That was it. Thought I already tried it but turns out I tried doing it the GLSL way... In HLSL... Yeah...

-------------------------

