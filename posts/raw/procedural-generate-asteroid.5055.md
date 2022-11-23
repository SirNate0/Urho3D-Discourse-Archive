ab4daa | 2019-05-23 13:20:03 UTC | #1

Hi,

I'm trying to procedural generate asteroids recently.

It seems there is no detailed implementation I can copycat.

So far I try to implement it by description in those internet discussions.

I think you veterans definitely have different insight, please take a look and give me some comments or advice if you have time/interested, thank you!

[code](https://github.com/ab4daa/procedural_asteroid)

Some sample images:
![](upload://qnuKprIt9neDgqw23XlL4fHqT48.png)

![](upload://iyuQG7uMQWWXH8qyZhdZngfycr5.png)

## Approach:

Mesh:

1. Generate a subdivided cube or sphere mesh in 1x1x1 bounding box
2. Random scale the mesh
3. Cut the mesh by random planes. Cut means project the vertices behind the plane onto the plane.
4. Displace vertices along normal by noise.

For texturing, there are 2 ways:

1. UV mapping (drawback: there will be seams)
   i. Cut the mesh to two half, use [auto_uv_map](https://github.com/silky/auto_uv_map) to generate UV.
   ii. Use Urho3D built-in function GenerateTangents() to generate tangent.
2. Triplanar mapping (drawback: the bumpness is not as clear as method 1)
   i. Modify LitSolid shader to LitSolidTriplanar by referencing internet articles.

Normal map:

1. Generate height map by placing some random craters and white noise.
2. Port [NormalMap-Online](https://github.com/cpetry/NormalMap-Online) shader to c++ to generate normal map from height map.

-------------------------

QBkGames | 2019-03-31 04:11:11 UTC | #2

I think the reason you cannot find much material on this topic is because nobody bothers with procedural generated asteroids. If you create at least 5 different asteroid models in Blender (or another 3D modelling software), and bring them in Urho and then position them randomly with random rotations and scale, you can get a pretty convincing looking asteroid field (with the added benefit of being able to use instancing to render them fast).

Sorry this doesn't answer your question, but it might be helpful in the long run :slight_smile:.

-------------------------

ab4daa | 2019-03-31 05:08:54 UTC | #3

Fair point.
There is also much voice of pre-made model in those discussion.
Just want to give it a try since I can't guarantee I can do better with my crap art skill. :sweat_smile:

-------------------------

Leith | 2019-03-31 06:58:01 UTC | #4

One of my teachers, in his Masters Thesis, developed a procedural cave system (essentially, a network of connected subspaces, and tunnels), which is very similar to your work. The time it takes to generate a bunch of procedural shapes, and connect them, is very low and can be done offline (that is to say, we generate and save our shapes, and load them back in at runtime). His system could add and remove detail based on the camera view using geometry shaders to mess with the tesselation.
Another guy used this for generating entire planets, again using a DLOD approach, at runtime, not in advance (his method is entirely based on the fact that RNG's are predictable for a given random seed).
Don't give up on procedural geometry - but do recognize the fact that you are making your life more difficult to get your game up and running. Procedural geometry can wait until the game mechanics work well for a small set of test objects.

-------------------------

ab4daa | 2019-03-31 09:26:45 UTC | #5

Yeah, time to go back to game logic.:upside_down_face:

So far I have no idea howto improve it....
Or, it doesn't need to improve much as unnoticeable background object.

-------------------------

johnnycable | 2019-03-31 11:39:13 UTC | #6

ditto on @QBkGames
just take some ready-made rock stuff out there
but if you really want to enjoy some proc gen, you may try with some... how was that... voronoi rock generation?
https://www.youtube.com/watch?v=dwuBFZp6Bs0

Ah, there's this old site about auto-gen:
http://pcg.wikidot.com/category-pcg-algorithms

-------------------------

ab4daa | 2019-03-31 12:56:31 UTC | #7

The video reminds me how powerful blender is.
Seems blender is the right way to go, thanks!

-------------------------

johnnycable | 2019-04-02 20:26:40 UTC | #8

Something funny that maybe in order...

https://www.youtube.com/watch?v=e5GUJ4NwgiI

switch the monkey for a big rock shape, cut with random node, and crash it down. Then collect pieces... :laughing:

-------------------------

