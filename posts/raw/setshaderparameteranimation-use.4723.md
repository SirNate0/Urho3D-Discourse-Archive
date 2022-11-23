I3DB | 2018-12-11 10:08:41 UTC | #1

In the UrhoSharp.SharpReality sample Advanced Earth, the shader is misplaced from the others using the Update call. https://github.com/xamarin/urho-samples/blob/b72d055a424d0e6be825c0239683c225d29ee723/HoloLens/02_HelloWorldAdvanced/Program.cs#L85 

Just below that line, there is a code comment that the same could be done using SetShaderParameterAnimation.

How is this routine used? Any sample code available showing use?

-------------------------

Sinoid | 2018-12-10 18:36:02 UTC | #2

You create a `ValueAnimation` and then pass that into `Material::SetShaderParameterAnimation`, you'll need to look up how UrhoSharp has that bound to C#.

-------------------------

I3DB | 2018-12-10 19:12:29 UTC | #3

Are there any C++ code samples, for either? ValueAnimation or SetShaderParameterAnimation.

Going from C++ to C# is much easier than starting with nothing in C#.

A bit of sample code goes a long way.

-------------------------

I3DB | 2018-12-11 10:10:05 UTC | #4

https://github.com/xamarin/urho-samples/blob/b72d055a424d0e6be825c0239683c225d29ee723/FeatureSamples/Core/31_MaterialAnimation/MaterialAnimation.cs#L105

-------------------------

Sinoid | 2018-12-10 21:45:22 UTC | #5

Yeah you found it. That's nice that the UrhoSharp folks ported all of the examples - didn't know they did that.

-------------------------

