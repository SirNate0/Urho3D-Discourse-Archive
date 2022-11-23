godan | 2017-03-28 15:52:55 UTC | #1

I'm working on a volume renderer for 3D textures (that start life as a bunch of 2D textures). Here is what I've got so far, using the Stanford Volume dataset. Super creepy :slight_smile:

 <img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/bed175ad9291db0db1babb84f84acd11c1927425.jpg" width="690" height="370">

[Here is the source](https://gist.github.com/danhambleton/f318a91405c36aef15dc4cda4e93c451) (for Urho OpenGL) and [here is my reference](http://prideout.net/blog/?tag=volume-rendering#raycasting). I think the biggest challenge is how to integrate it with the rest of the scene...

-------------------------

dragonCASTjosh | 2017-03-29 06:19:47 UTC | #2

Im not sure your intention with making this but it would be cool to extend this out into fog and other volumetric based effect. Ill have to look deeper into your implementation out of a pure curiosity POV as i was looking to implement volume rendering as part of my graphics additions, I was intending to base it mainly from frostbites publication as i loved the results. This may also be interesting for you to look at: [https://www.shadertoy.com/view/MdlyDs](https://www.shadertoy.com/view/MdlyDs)

Your solution looks to be more of the data visualisation side. For example medical scans but that may just be from the images.

-------------------------

godan | 2017-03-29 12:50:57 UTC | #3

So, yes, I wrote this with a more data-viz/science application in mind. However, I think the approach is general enough for wider applications. Although this particular implementation is not super polished, there are a couple good tricks in there:

1. The shader operates through a material applied to bounding box. This means that apart from some occlusion stuff, it should "fit" in to the rest of the scene.
2. Again, since it is a material applied to a box, textures, lighting, and (possibly) shadows should be pretty simple to integrate.
3. It has a couple fancy moves to reduce slice artifacts (half stepping, and some ray jitter).

Would be interesting to hear what use cases there might out there. I guess smoke/liquids is an obvious one...

-------------------------

Sinoid | 2017-03-31 04:06:31 UTC | #4

How dense is your volume? Looks quite nice, pretty jealous that I can't get away with raytracing volumes as I have to merge poly-soup via CSG and smooth the seams.

-------------------------

