Gnollrunner | 2018-05-07 19:43:34 UTC | #1

Hi, I've been running around trying to figure out what game engine I should use, or if I should use one at all. Here's where I stand. I'm a C++ programmer and a few years back I wrote a fairly crude fractal planet generator. It worked OK though. It had collision detection and you could run around on the surface.  There was no data on disk. It just used the fractal functions directly and generated a height mapped meshes wrapped around a big sphere. As a result the planets could be very large (like a few thousand kilometers) since the only data that ever existed was what you could see and it had a decent LOD algorithm to keep the size down. The main problem with it was, it only supported height mapping style functions. 

Recently I have updated it (actually completely rewrote most of it) to use octrees of prism shaped voxels which generates it's terrain something akin to the way marching cubes does it, but with variable sized chunks of different resolutions. To make all of this work I generate stuff in double precision on the CPU side and then convert it to single precision for the GPU and then transform each chunk to it's location. I currently do this part in DirectX but I'd like to see if I can make it work with a real game engine and make a game out of it.  

What I'm unsure of is if it's compatible. I really don't know anything about game engines except for what I've read, and I'm worried that the fact that I'm generating all the geometry at run time, is going to be too strange for a normal game engine to handle. 

To fill in some details I currently use two threads. One kind of runs the program in the normal way from the current meshes, and the other updates the octrees and builds new meshes for the next iteration. One key thing that I alluded to above, is that I always have to keep the camera near zero to avoid loss of precision on the graphics cards, so I have to be able to transform all the terrain around the player not the other way around. This has to also happen with any other objects I add to the world (buildings, trees, etc).

Finally my main concern is that I'm building all the meshes in C++ myself and then sending them to the card, which is OK using DirectX. However if I go through urho3d is it required that it store the meshes itself in it's own format, or is there a way to still send data straight to the card? I'm tying to avoid having three copies of the data but I'd like it to run platforms other than windows. Thanks in advance.

-------------------------

johnnycable | 2018-05-07 21:09:21 UTC | #2

Anyway I think you can skip intermediate artifact generation if you need to go low level with creating and painting your world... but probably need to adapt things someway. Maybe this discussion can be of help:
https://discourse.urho3d.io/t/directly-loading-a-model/641

Or you may want to use Custom Geometry:

https://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_custom_geometry.html

-------------------------

Gnollrunner | 2018-05-08 04:37:18 UTC | #3

OK thanks a lot. It looks promising. I see buffer locking and stuff which leads me to believe I can more or less write straight to the card thorough the interface.  I think I'll give it a shot and see how it goes.

-------------------------

simonsch | 2018-05-08 07:24:25 UTC | #4

[quote="Gnollrunner, post:1, topic:4227"]
Finally my main concern is that I’m building all the meshes in C++ myself and then sending them to the card, which is OK using DirectX. However if I go through urho3d is it required that it store the meshes itself in it’s own format, or is there a way to still send data straight to the card? I’m tying to avoid having three copies of the data but I’d like it to run platforms other than windows. Thanks in advance.
[/quote]

I am using urho3d from c++ as well and can tell you there should be no problem. It is absolutely possible to use a vertexbuffer you can combine with some vertex element structure which defines, which data you are sending to the GPU. You can then easily paste millions of points through your GPU.

-------------------------

