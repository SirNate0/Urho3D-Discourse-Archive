najak3d | 2020-04-24 19:58:33 UTC | #1

First off, we are loving UrhoSharp.  Thank you to everyone who developed it.

Our needs are fairly basic (it's a GPS mapping app, that we're porting to 3D presentation).   So we're mostly drawing map images, satellite images, and a lot of vector data (lines, water, roads, pins, route, traffic, etc).

Our whole app is in C#, and so of course we're using UrhoSharp inside Xamarin forms.  It's working very well.  UWP had a few issues, but we've already worked around it.

Xamarin itself is a hugely popular application development platform pushed by Microsoft, and UrhoSharp is still Microsoft's recommendation.  It's working well, with a special thanks to "slango0513" who recently ported UrhoSharp back to Visual Studio 2019.  It works out-of-box.

[https://github.com/slango0513/UrhoSamples2019](https://github.com/slango0513/UrhoSamples2019)

The only thing lacking in UrhoSharp (and probably Urho too) is support for Geometry Shaders.  We only need this for a single shader -- "SmoothLines".   Since we deal with thousands of dynamic line points at a time, it seems prudent to give these lines their thickness inside the geometry shader, instead of creating 3 triangles per line segment, with UV coordinates.   Those triangles could/should be created inside the geometry shader, IMO.   However, it's working fine without it too, so it's not a big loss.   As you zoom in/out on the map, we dynamically change the width of these lines -- which makes us need to alter the geometry dynamically, so that their thickness generally stays same size on screen.

===
Since we're just getting started -- there is time for us to switch to "Rbfx", as it appears to be more advanced and have more momentum than vanilla Urho.   However, there appears to be no good "Xamarin" integration with Rbfx, and the C# support is labeled as "experimental".

If you want to bring in a whole host of C#/Xamarin developers to Rbfx, you should finish up the C# wrappers and make it work out-of-box with Xaramin (same as UrhoSharp).   Currently there is NO GOOD SOLUTION FOR XAMARIN to do 3D, other than UrhoSharp.

I'd like to see more options for 3D support for Xamarin besides UrhoSharp.  What are the chances?

-------------------------

adhoc99 | 2020-04-24 20:36:44 UTC | #2

I would strongly suggest going for rbfx. As you said, development has a lot more momentum there.

Their Github repository has a link to their Gitter. Maybe you could ask about the Xamarin integration there. Or maybe post a question on their issue tracker.

-------------------------

throwawayerino | 2020-04-24 22:00:10 UTC | #3

rbfx has more of a game oriented approach than Urho3D. You seem to be doing a map program and moving to rbfx would require you to redo all your data storage declarations since that uses something different from Urho3D.

-------------------------

