suppagam | 2019-09-19 16:01:38 UTC | #1

I was looking at this free package for UE4: http://www.supergrid.io/

And I've noticed one interesting feature: the textures auto-adjust to the mesh scaling. Check this:

![grid_scale|400x225](upload://3GfLnvx6PYq9fJvvoLTcXQ0MXnr.gif) 

Instead of stretching the texture, it looks like it creates an UV in realtime. How is that done?

-------------------------

SirNate0 | 2019-09-19 16:18:16 UTC | #2

My guess is that it uses tiling textures and a shader that constructs UV coordinates from the world position of the vertex and probably it's normal instead of using UV coordinates in the model.

-------------------------

Modanung | 2019-09-19 16:29:08 UTC | #3

Something like this - what the gif demonstrates - would not be very hard to make. Take a look at the [dynamic geometry sample (34)](https://github.com/urho3d/Urho3D/blob/master/Source/Samples/34_DynamicGeometry/DynamicGeometry.cpp) and maybe try to add some interactivity to it. If you have any experience with mouse rays it should be clear after that how you could recreate this snapping box that writes UV coordinates together with any changes in the vertex coordinates.

-------------------------

suppagam | 2019-09-19 21:00:04 UTC | #4

Thanks for the tips, guys! I'll take a chance on this.

-------------------------

