Victor | 2017-06-26 12:32:36 UTC | #1

I've been working on a few modifications to my foliage system and started to add multiple foliage types to it. I've also removed the StaticModelGroup and I'm only using StaticModel now, grouping the triangles into large batches of my CustomMesh class for performance.

My next goal is to load the different foliage patches onto another thread to save on memory resources. I've done this before, but I need to rewrite my class since I've refactored a bunch of stuff.

https://youtu.be/bZnO0qLi3bY

-------------------------

Don | 2017-06-27 03:09:56 UTC | #2

The performance here is really great! Would you mind sharing the code to your CustomMesh class and what hardware you're running on? I'm looking to implement something similar.

-------------------------

Victor | 2017-06-27 03:43:00 UTC | #3

Here's the updated version of the CustomMesh class. It's originally based off of this post: http://discourse.urho3d.io/t/a-mesh-generator/2361 by @rbnpontes.

The key factors right now for the foliage to render as a single mesh are the Rotate()/RotateFace() method. I'm still working on adding wind and making a better shader. I have noticed that if you push too many tris to the CustomMesh class you can run into some issues where the vertices are misplaced. There's a SetUseLargeIndices() for large meshes, however sometimes you still end up having REALLY large set of vertices to render (which can mess up the render). In those cases I create multiple CustomMesh objects if that makes sense... :)

https://gist.github.com/victorholt/5913777922c61549f9d9bce9487a750f

https://gist.github.com/victorholt/955ae2f76173d1a5d3b9f65fefcbb47e

-------------------------

Victor | 2017-06-27 03:56:11 UTC | #4

Oh, in terms of hardware..., I don't think I run an incredibly powerful machine, just one I built a couple of years ago.

Windows 10 64bit
i5-4690K (3.5 GHz) no overclock
Nvidia GeForce GTX 760

-------------------------

TheSHEEEP | 2017-06-27 05:32:36 UTC | #5

Not bad!
How would you go about rendering distant environments with this approach (think maybe a forest from the distance)?

Or would you use something else for that?

-------------------------

Victor | 2017-06-27 06:45:21 UTC | #6

I'm not sure to be honest. This is all just experimental heh. Also, this approach makes it harder to do wind animation, which might not even be worth it. Instead, this might be a good approach to render distant foliage with no animation, while close up foliage can use the StaticModelGroup approach to handle wind animation.

For very large terrains, I used a multi-threaded approach to load up foliage files when you got close enough to save on resources.

-------------------------

