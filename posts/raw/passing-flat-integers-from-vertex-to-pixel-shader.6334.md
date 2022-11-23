Lys0gen | 2020-08-17 19:36:22 UTC | #1

Hello,
can anyone tell me how to correctly pass (non interpolated) Integer values from the vertex shader to pixel shader? I want to pass absolute pixel coordinates to read from a Texture2d with **texelfetch**.

My best attempt so far was this:
Before the VS() I define the variable

	out ivec2 vHexCoordinates;

And set the value inside VS(). I have tried it with something foolproof, setting it to constant values:

	vHexCoordinates = ivec2(37, 23);

But for some reason **inside PS() the value of this array is always (0, 0)**. I thought maybe I need to declare it as **in** instead of **out** for the pixel shader, but that is not possible because the declaration conflicts as both functions/declarations are in the same document.

Alternatively I have tried it with a **flat** float vector

	flat out vec2 vHexCoordinates;

But here it gives me an error

	*error C1311: qualifier "flat/smooth/noperspective" cannot apply to this type*

which is weird because I haven't found any type to which I can apply *flat* and I don't see why this shouldn't be possible.

I would be thankful for any tips.

-------------------------

SirNate0 | 2020-08-18 14:24:06 UTC | #2

I think the right solution may be to do something like
```glsl

#ifdef COMPILEVS
out ivec2 vHexCoordinates;
#endif

#ifdef COMPILEPS
in ivec2 vHexCoordinates;
#endif
```
I have no idea about the flat attribute, but I'm not too familiar with GLSL so that isn't that surprising.

Another solution is to use varying, which you can see done in PBRLitSolid, for example:
```glsl
varying vec4 vTexCoord;
```

-------------------------

Lys0gen | 2020-08-18 14:23:56 UTC | #3

[quote="SirNate0, post:2, topic:6334"]
```
#ifdef COMPILEVS
out ivec2 vHexCoordinates;
#endif

#ifdef COMPILEPS
in ivec2 vHexCoordinates;
#endif
```
[/quote]

Of course! Precompiler statements... That worked, almost. Now it wants the **flat** in front of the in/out, but with that it works perfectly! Thanks a lot!

(About your *varying* suggestion, well that is the opposite of what I wanted because varying interpolates the values in between the vertices, which I don't want for this specific variable :) )

-------------------------

