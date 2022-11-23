lebrewer | 2021-11-10 17:45:16 UTC | #1

Right now, Oceans / Water in Urho are mostly made with a plane. I'm trying to come up with a way to create an infinite ocean within the engine. So far, I have created 9 big planes: 1 at the center, where the player/camera is, and 8 around it. Whenever the player moves towards a certain area of the 9-tile-patch, I move the opposing tiles towards that direction, never deleting any tile, just shifting them and hoping the player does not notice. 

Is this a good technique? What would you guys do in this situation?

-------------------------

evolgames | 2021-11-11 05:24:46 UTC | #3

Sounds good to me as long as the tile area are bigger than player view. I'd do the same

-------------------------

GodMan | 2021-11-14 18:36:20 UTC | #4

How does this differ from just using a big plane? I am working on a water shader that does not use render to texture.

-------------------------

Naros | 2022-01-26 17:30:56 UTC | #5

The best way to avoid the player noticing the shift in the tiles is to actually have more Ocean tiles than what you render.  This way you can transition from "not visible" to "visible" and "visible" to "not visible" and then when the ones that are "not visible" are outside the load radius, they're free to be re-used.

-------------------------

Nerrik | 2022-01-30 08:40:58 UTC | #6

Iam using the https://github.com/anthonix/ffts library for ocean, inspired by https://github.com/jiasli/OceanSurface. Its tileable an i have 9 tiles loadet at once at the playerposition. I generate a Heightmap (128x128) not a model and sample it in VS (reposit the verts from a plane) / PS (Mixing 2 Textures / Colors with Heightmapinfo).

Fast and very impressive Results (already postet a Video from my Terrain, but you can see the Ocean also) 

[http://wyrdan.de/terrain.mp4](http://wyrdan.de/terrain.mp4)

-------------------------

lebrewer | 2022-01-27 16:42:55 UTC | #7

Found a few Urho-based approaches, but unfortunately none of them are "infinite". I can still cheat by using the camera tricks though:

https://github.com/Lumak/Urho3D-Ocean-Simulation
https://github.com/Gentle22/Urho3D-Ocean

-------------------------

lebrewer | 2022-01-27 16:44:05 UTC | #8

Also, for anyone else going down this rabbit hole, I found Unigine's approach to be very creative:

https://unigine.com/blog/2013/06/05/procedural-content-generation/


And this looks surreal: https://liris.cnrs.fr/Documents/Liris-5812.pdf

So much to learn. :open_mouth:

-------------------------

