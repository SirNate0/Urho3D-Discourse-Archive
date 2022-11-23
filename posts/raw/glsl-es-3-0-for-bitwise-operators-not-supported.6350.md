najak3d | 2020-08-27 14:57:25 UTC | #1

We've gotten creative with shaders and are packing information into bits of the vertex position's Y component (since for us Y == 0, always for these objects).   So we're using the Y as a 16-bit integer value, and are wanting to extract information from these bits.

But bitwise operators are only supported in OpenGL ES 3.0 and above.   When we use UrhoSharp (based on Urho3D 1.9.67) - it gives us an error for all bitwise ops saying "bit-wise operator supported in GLSL ES 3.00 and above" and won't allow it.

Is there a way to enable GLSL 3.0 mode with UrhoSharp?

EDIT: Eugene provided the actual answer to my question, which is that GLSL ES 3 is not supported via UrhoSharp (or even Urho3D at this point).     And then Lysogen's answer is marked as solution, because this is the algorithm that we needed to use in lieu of the bitwise operators.

-------------------------

Lys0gen | 2020-08-27 14:55:40 UTC | #2

Not sure about that, but if all you want to do is use a single float to store two values then you can do that with simple multiplication as well.

Packing the value:

	float encodeFloat(int valX, int valY)
	{
	   return valX + ((valY+0.49) * 0.00390625);//+0.49 because of possible rounding inaccuracies
	}

Unpacking it in the shader:

	float packedXY = [YOURINPUTVARIABLE] * 256.0;
	float nX = floor(packedXY * 0.00390625);
	float nY = floor(packedXY - nX * 256.0);

Pretty sure this also works with floats but I just needed integers.

-------------------------

Eugene | 2020-08-27 14:55:39 UTC | #3

[quote="najak3d, post:1, topic:6350"]
Is there a way to enable GLSL 3.0 mode with UrhoSharp?
[/quote]
I can say for sure that it can be done in C++ code with certain amount of work.
Therefore, it's impossible to do in C# interface alone.

Also, I heard that GL ES 3.0 is not the stablest thing in the world, so I would be cautious about hard-locking app onto GL ES 3.0. Maybe these concerns are outdated tho.

-------------------------

najak3d | 2020-08-27 14:54:21 UTC | #4

Lysogen - thanks for the algorithm suggestion.  That's what we're going to have to go with.

Eugene - thanks for the confirmation of what I was suspecting.  Before abandoning our bitwise operators, wanted to confirm that we had to use the more awkward math, as shown by Lysogen.

-------------------------

