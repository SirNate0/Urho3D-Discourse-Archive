GodMan | 2020-03-03 01:00:39 UTC | #1

I'm looking at maybe a quad or trail that has two intersection polygons. Should the be a component or a draw able? I am going to use this with RayCasting. 

Examples:
![](https://i.ytimg.com/vi/c7kztwK3AHE/maxresdefault.jpg)
![](https://teambeyond.net/wp-content/uploads/2014/10/Halo-2-Anniversary-Beam-Rifle.png)
![](https://blogs.agu.org/martianchronicles/files/2010/02/800px-spartan_laser_header.jpg)

-------------------------

evolgames | 2020-03-03 01:42:21 UTC | #2

Look at the 44_RibbonTrail Demo. It's pretty simple for projectiles at least.

-------------------------

George1 | 2020-03-03 01:43:08 UTC | #3

https://discourse.urho3d.io/t/laser-and-laser-prefab/3603/20

Search for laser beam

-------------------------

GodMan | 2020-03-03 03:23:43 UTC | #4

Okay. I did see the laser thread in the past.

-------------------------

Modanung | 2020-03-03 03:24:50 UTC | #5

You'll probably want your 3DLine to be a *simplified* `RibbonTrail`.

Unlike my beamlight...
https://vimeo.com/209327362

-------------------------

GodMan | 2020-03-03 03:29:23 UTC | #6

I looked at the ribbon trail example. All I'm looking for is really a way to create a intersecting quad this helps keep the effect from looking flat. So create one end of the quad at the gun barrel position then raycast and if a hit is detected draw the other end of the polygon to that location. Maybe even add a texture to the quad for the tail effect like the pics above.

-------------------------

SirNate0 | 2020-03-03 04:06:32 UTC | #7

If that's the case why not just make it in blender (or whatever modeling program you use) and then rotate and scale the geometry accordingly?

-------------------------

GodMan | 2020-03-03 04:44:47 UTC | #8

If I have a texture mapped to the quad. Then scale it in the forward direction wont this screw the uvs up?

-------------------------

SirNate0 | 2020-03-03 13:31:23 UTC | #9

It depends on the texture. If the texture is meant to wrap along the length of the laser every 1 meter or the like them yes, but if the texture is meant to scale along it (e.g. If the texture doesn't change with the length direction) then no.

-------------------------

Modanung | 2020-03-03 13:49:15 UTC | #10

With custom geometry you could fade out the start and end individually, together with a *traveling* texture by setting the vertex colors and UVs accordingly during the batch update.

-------------------------

GodMan | 2020-03-03 18:13:49 UTC | #11

So do you guys think I should modify RibbionTrail or make a custom geometry.

-------------------------

GodMan | 2020-03-03 18:15:17 UTC | #12

@SirNate0 This method will work for my bullet contrails. They just use a gradient texture like in the laser post thread.

-------------------------

