I3DB | 2018-12-19 22:39:05 UTC | #1

Working through some C# sample code. At this point ...
https://github.com/xamarin/urho-samples/blob/b72d055a424d0e6be825c0239683c225d29ee723/FeatureSamples/Core/43_BasicTechniques/BasicTechniques.cs#L104

When loading the Sample43/MatCustomShader.xml material, which uses the Smple43/TechniqueCustomShader.xml file, an error is thrown:

System.Exception: Could not find resource Shaders/HLSL/Sample43CustomShader.hlsl

This file does not exist, however the file Shaders/GLSL/Sample43CustomShader.glsl file does exist.

MatCustomShader.xml contents ...

https://github.com/xamarin/urho-samples/blob/master/FeatureSamples/Assets/Data/Sample43/MatCustomShader.xml

TechniqueCustomShader.xml contents ...

https://github.com/xamarin/urho-samples/blob/master/FeatureSamples/Assets/Data/Sample43/TechniqueCustomShader.xml

And the comment at the top of that file tends to lead toward the .glsl file being the one desired, yet the engine goes for HLSL.

My own inexperience with materials and shaders leaves me with no help here.

Why does it seek out the .hlsl file and not the .glsl file?

-------------------------

I3DB | 2018-12-18 17:44:22 UTC | #2

Ok, I think the answer is my engine is running D3D and not open GL.

-------------------------

GoldenThumbs | 2018-12-18 17:56:12 UTC | #3

That would explain it lol. You new? Welcome if you are!

-------------------------

