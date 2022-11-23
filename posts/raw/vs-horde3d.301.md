carl | 2017-01-02 00:59:29 UTC | #1

I've read that urho3D is "inspired" in OGRE and Horde3D. As I see it, Horde is just rendering and animation, while urho has a lot more stuff in it.
I would like to know how's the status regarding rendering and animation in urho. Is it based on, similar, better or worse than Horde? Is there any feature missing in urho that Horde has? Is one of them easier to use or has better performance?

-------------------------

boberfly | 2017-01-02 00:59:30 UTC | #2

Hi carl,

I come from Horde3D development and made an early ES2.0 port of it to the Nokia N900 and iPhone/Android. Indeed Horde3D is very nice and it's ideal to use as a drop-in library for rendering and it has an easy to use C-API inspired by OpenGL itself, very polished.

What Horde3D lacks is a robust multi-threaded octree scenegraph and culling system which Urho3D has, it does use GPU occlusion queries while Urho3D favours a CPU occlusion query approach which both have their strengths and weaknesses. Also Urho3D can do instancing while Horde3D does not. I think also blendshape and cpu skinning is multi-threaded in Urho3D as well while Horde3D is single-threaded. Also the licensing is a lot more liberal in Urho3D (MIT) than Horde3D (EPL). Both have a very similar data-driven approach to building shaders/materials, and you can both build your own renderer paths from data too, that can do forward lighting/deferred shading, however deferred lighting (pre-pass) I don't think was standard in Horde3D.

Probably the most important thing to note is that the main developers of Horde3D don't work on it any more, it is only the community which maintains it now.

Arguably Urho3D is quite modular so if you don't need the engine itself you can compile the Renderer part and use the Renderer.h in your own engine and get a perfectly abstracted OpenGL2.0+extensions/Direct3D9 renderer.

Cheers

-------------------------

cadaver | 2017-01-02 00:59:30 UTC | #3

The reason for those "inspired by" statements is that Urho3D started as a pure renderer - in the beginning there was no physics, UI, scripting etc. and at that early time Ogre & Horde3D were invaluable learning sources when designing the API & internals.

-------------------------

carl | 2017-01-02 00:59:31 UTC | #4

Great, I understand it now, thanks!

-------------------------

