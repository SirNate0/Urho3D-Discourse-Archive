stark7 | 2017-11-07 15:52:17 UTC | #1

Hello,

I would like to assemble any road shape from a single section model I made with Blender - could someone please provide some direction on how I could replicate that section over in any curve without getting weird artifacts where the sections join?

A long time ago I wrote an algo to calculate the length of each curb like in the below images based on the radius of curvature of each pair, but that seems a bit overkill and it requires multiple different models to work together - I'm hoping for a simpler solution if it exists. (I also lost that algo and I am not looking forward to recreating it :smiley:  )

![unnamed|690x382](upload://ehFjYAEUfI9HJxpk1ijwrStNAuD.png)![unnamed0|690x331](upload://vVUSZ3MX2YEsSeqBHbr3Pv8LQyb.png)

-------------------------

jmiller | 2017-11-07 19:28:14 UTC | #2

Hello,

There are a few discussion threads and implementations around the forum you may want to check out.
 e.g. https://discourse.urho3d.io/search?q=road

Using mesh/spline
  https://discourse.urho3d.io/t/modifying-mesh-using-spline/2976/4

RibbonTrail
https://discourse.urho3d.io/t/offroad-vehicle/2450

As for prefab meshes, Modular City Kit (FBX) is one I came across, but I'm not sure if/where it's still available for download.

HTH

-------------------------

stark7 | 2017-11-07 19:28:10 UTC | #3

Thanks - for some reason I looked up a bunch of keyword but I didn't think to use the "road" keyword :) - what i'm gathering is that there's no built in default component..

-------------------------

jmiller | 2017-11-08 03:05:39 UTC | #4

:slight_smile:

You mention some algoing... I remember Mesh Generator. It could make procedural geometry more fun (or at least simpler).
https://discourse.urho3d.io/t/a-mesh-generator/2361

-------------------------

