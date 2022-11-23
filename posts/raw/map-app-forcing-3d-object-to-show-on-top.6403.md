najak3d | 2020-09-26 08:34:51 UTC | #1

We have a 2D map app, that is being rendered by a non-orthographic camera, which means we can't just move things closer to the camera to make it appear 'on top'... because with the perspective projection, if you move things closer, then it's going to make their 2D position skew as you move the camera (to anywhere except directly over top them).  So all objects in our map view will be positioned at Y=0.

For 2D objects, we have them all positioned exactly at Y=0, to avoid the Skew, and then are using "RenderOrder" to set the Z-order.  This is working just great.

However, now we want to employ some 3D models into the mix, but we need the be able to control the Z-Order alongside those 2D graphics.  Since the 3D models have "height", half of the model will be above ground, and half below ground... and it shows.   This is bad.  Instead we want to make sure the entire 3D model shows, and is not occluded by other objects... it needs to appear "fully on top", despite it having parts of the model actually be further from camera that other layers.

What is the easiest way in Urho to do this? (i.e. I *think* this means ignoring the DepthCheck with other objects, but not itself)

-------------------------

SirNate0 | 2020-09-27 01:38:00 UTC | #2

If you don't need the depth information for the 2d objects set them to not write to the depth buffer. You may be able to do it through the material, but if not I know you can do it by modifying the techniques and setting depthwrite="false" (see https://urho3d.github.io/documentation/HEAD/_materials.html).

-------------------------

najak3d | 2020-09-27 01:38:24 UTC | #3

Thank you SirNate0.  I think that sounds like a great solution.

-------------------------

najak3d | 2020-09-27 02:21:00 UTC | #4

Hmmm, Looks like we already had the Plane's DepthWrite set to False for the technique.

Here's the Plane_Image.xml, Techhnique:

<technique vs="Plane_Image" ps="Plane_Image">
  <pass name="alpha"  depthwrite="false" blend="alpha" />
</technique>

Yet here's a close-up of the X-wing rolling - and you can see that it's right wing is behind the Yellow Plane.

![image|224x260](upload://ghQuFgoEO9ELUyAdxNzbho78BWo.jpeg)

-------------------------

najak3d | 2020-09-27 02:35:32 UTC | #5

So I resorted to setting the "depthbias" and now it shows the X-wing always above everything else:

			BiasParameters bp = new BiasParameters() { ConstantBias = -0.9f };
			mat.DepthBias = bp;


I'm not sure why the "depthwrite" set to false isn't working.    

I even set the X-Wing RenderOrder to 255, to make it last to render, just to see if that might help.    This technique of altering "RenderOrder" works great for determining the Z-order for various object on my 2D icon's layer.

-------------------------

SirNate0 | 2020-09-27 02:57:01 UTC | #6

You mentioned using render order earlier - is the yellow down thing rendered after the X-wing, and/or does it use an alpha pass with the same render order? I think either of those could give you the result shown.

I think the default render order is in the middle.

Though if you have it working already maybe don't bother trying to change it.

-------------------------

najak3d | 2020-09-27 06:26:03 UTC | #7

The Yellow image/plane is rendered BEFORE the X-Wing model.   X-Wing Model uses the "NoTexture" material (built-in) and I've set RenderOrder to 255, so that it'll be last.  

I would have thought that if the Yellow Image were rendered with "DepthWrite FALSE" that nothing rendered after it would appear behind it.   Maybe the "pass name" is messing it up.  I'm new to Urho, so might just need to figure that part out.

-------------------------

