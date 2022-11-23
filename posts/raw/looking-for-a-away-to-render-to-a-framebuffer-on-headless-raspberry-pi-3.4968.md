thejoggeli | 2019-02-26 18:33:23 UTC | #1

First, great work and big thank you to the developers of Urho3D. This engine is amazing. 

My question - is there a way to run this engine on a headless Raspberry Pi and render to buffer instead of a window? My plan is to use this engine to render different (2D and 3D) animations to an LED matrix. For which I have found that I absolutely have to run the Raspberry in headless mode, otherwise there is a ton of flickering on the matrix. I'm currently using GLE + OpenGL ES 2.0 to accomplish this. I render to a pbuffer and then simply copy its contents to the matrix. Now I want to add some more complicated things that requires collision detection, physics, etc. Which is why I have found this engine. But I couldn't find a way to run Urho3d without a window. Is there a way to accomplish this?

-------------------------

weitjong | 2019-02-27 00:48:29 UTC | #2

Have you checked render to texture? I recall someone else in the past try similar thing as you but using AWS cloud. There is RTT sample in the repo.

-------------------------

