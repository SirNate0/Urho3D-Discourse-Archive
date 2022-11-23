najak3d | 2020-04-19 19:00:06 UTC | #1

We have a mapping app written on .NET 4.0 and uses OpenGL for the 3D view only.  The map view is currently all written with 2D graphics calls.   We are about to convert our whole app over to:

1. Xamarin.Forms --- for UWP, iOS, and Android.
2. Plus - something that provides OpenGL support (D3D fine too).

Our two chief alternatives are UrhoSharp or MonoGame.

Which is better and why?   Factors we're considering:
1. Overall Community Support.  Namely which one has more users, who can help "show the way" for various things.
2. Developer support - which one is most likely to be supported for bug fixes.
3. Stability / Reliability - need it near 100%.  No mystery crashes; limited weird behavior.
4. Footprint - light weight is better.  We're only doing simple graphics.
5. Anything else I missed?

So far, my experience with Urho has been spotty.  So much stuff doesn't work out-of-box for UWP. 

The worst part about Uhro so far is the absence of Sample Code projects.   For example, I've spent a couple hours trying to find a downloadable "Custom Shader" example.  The one packaged with the UrhoSharp2019Samples.zip we found:

1. Omits the Custom Shader example for UWP (because it only has GLSL shader in the sample)
2. And the Custom Shader doesn't render for Android (not sure on iOS).

I can't find any working online projects for CustomShader.

I spent a few hours trying to get Anti-Aliasing to work .... and ends up I have to use the FXAA2 post shader, which also DOES NOT WORK on UWP, unless you turn on HDR Lighting (so why didn't the sample code have it set up this way to start with?).

Anyhow -- there have been a lot of landmines from the get-go, and I'm having hard time finding example code online. (where you just download a zip file, and see it run out-of-box, and then tweak the code to learn it)

We were favoring Urho3D so far -- but have been somewhat disappointed with what we're finding, enough so that we're now wondering if we might be better off with MonoGame instead... ?

-------------------------

JTippetts1 | 2020-04-19 21:26:10 UTC | #2

It is my understanding that UrhoSharp is a dead project. At the very least, it is not likely you will find much support for it here. I'd advise you to choose something with official C# support.

-------------------------

najak3d | 2020-04-19 22:33:18 UTC | #3

That is sad.  The only other option I know of is MonoGame.

How about Urho3D (non-Xamarin)?   I know how to wrap C++ to expose it to C# (plus the code that is already there sets a pretty good example).   Our main issue is just with figuring out how to use Urho3D itself.   If there are issues with some of the API not being exposed, we have the ability to update the UrhoSharp wrapper, if needed (so long as there aren't too many instances of this).

-------------------------

adhoc99 | 2020-04-24 17:37:58 UTC | #4

Take a look at [rbfx](https://github.com/rokups/rbfx). It's a Urho3D fork with extensive C# support.

-------------------------

