GoogleBot42 | 2017-01-02 01:03:02 UTC | #1

Hello!  I am new to urho3d coming from irrlicht.  For the game that I am making it is critical that meshes can be combined and/or batched.  Does this already exist?  I looked through the forums and I couldn't find anything. I am looking for something like this: http:// urho3d.prophpbb.com/ucp.php?mode=activate&u=254&k=37P5AER  (Remove space after "http://" to go to link as I cannot post a link in my first post.)

Thanks!  :smiley:

-------------------------

weitjong | 2017-01-02 01:03:02 UTC | #2

Welcome to our forum.

Before answering your question, may I suggest you to rename your account so that we don't confuse you with the "real" Google bot which crawls in our forums quite frequently. The Bing and Yahoo bots too, so I would not use "BingBot" or "YahooBot" too  :wink: .  It also looks like you have pasted a wrong link URL in your first post.

About the question. If you are referring to "draw call batching" then yes, it is already supported by the Urho3D engine.

-------------------------

GoogleBot42 | 2017-01-02 01:03:03 UTC | #3

Whoops... here is the link... I feel stupid for not checking the link. =P   [url]http://irrlicht.sourceforge.net/forum/viewtopic.php?t=21971[/url]

Is there a good example for batching?  Thanks!

-------------------------

cadaver | 2017-01-02 01:03:03 UTC | #4

Urho instances static models of same geometry automatically (using hardware instancing), but it doesn't combine 3D models on the vertex buffer level on its own. So you would have to implement this yourself similarly as the OP in the thread had done for Irrlicht.

The 2D rendering system (StaticSprite2D and AnimatedSprite2D etc.) is fully based on combining everything into the same vertex buffer for efficient drawing, and it does this dynamically each frame. But it's only dealing with sprites (quads), not 3D models.

-------------------------

GoogleBot42 | 2017-01-02 01:03:15 UTC | #5

Would performance increase if I combined the meshes and materials together?

The documentation suggests that it would not because meshes with the same material and mesh will be automatically batched.  ([url]http://urho3d.github.io/documentation/1.32/_rendering.html[/url])  If I understand correctly irrlicht doesn't do this automatically which is why the person wrote the helper class for irrlicht.

I will be writing a minecraft clone.  Thus, is it practically guaranteed that each "combined" mesh (16x16x16 blocks; maybe more) will be unique.  To reduce triangles there will be a model for every possible simple block configuration (eg. block mesh missing top, right, and left side) except a block that has no sides.  This way sides of a block that cannot be seen to not waste cpu/gpu time.  So there are 2^6 -1 different basic block meshes.  Also I will be writing a custom shader to calculate lighting because it can be simplified.  So there could be hundreds of instances of a single mesh using the same material.  Is it worth writing the equivalent of what this person did for irrlicht for urho3d?

-------------------------

cadaver | 2017-01-02 01:03:15 UTC | #6

You can try to start with the inbuilt static model rendering but I'm quite sure in a Minecraft like scenario you will eventually hit performance problems, as there's overhead for culling a lot of drawables and adding them to the render queue. Urho is faster in that respect than eg. Ogre 1.x or Unity, but not limitlessly powerful. So the final approach will likely be to implement a custom world geometry combining, possibly dynamic based on the observer position / rotation.

-------------------------

GoogleBot42 | 2017-01-02 01:03:16 UTC | #7

All right thanks!  I will see what happens.  One of my goals is for this to run with minimal overhead.  Is there any place you can point me to about learning to create meshes on the fly in urho?

-------------------------

OvermindDL1 | 2017-01-02 01:03:16 UTC | #8

[quote="GoogleBot"]All right thanks!  I will see what happens.  One of my goals is for this to run with minimal overhead.  Is there any place you can point me to about learning to create meshes on the fly in urho?[/quote]
Example 34:
[url]https://github.com/urho3d/Urho3D/blob/master/Source/Samples/34_DynamicGeometry/DynamicGeometry.cpp[/url]

-------------------------

codingmonkey | 2017-01-02 01:03:16 UTC | #9

I think that you need to use a texture atlas (with several types of tilable images in one texture - ground, water, rocks...)
And to make your class based drawable, where you will generate a mesh for cubes(16x16x16) in a single batch, and assign a material as shifting the uv (change face texture from texture atlas) for cube faces. Because the batch may have only one material. And then you change world with some instrument you just call your_class.rebuild().

-------------------------

