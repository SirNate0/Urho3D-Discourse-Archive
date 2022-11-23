Kyle00 | 2017-01-02 01:08:42 UTC | #1

I've been looking into mobile optimization, specifically how unity does it and was reading this
[url]http://docs.unity3d.com/Manual/MobileOptimizationPracticalRenderingOptimizations.html[/url]

That process seems easy enough, but I was curious as to the textures on the image below. The left is diffuse, but what's the other two images?

[img]http://i.imgur.com/2VRTEcj.jpg?1[/img]

-------------------------

Bananaft | 2017-01-02 01:08:44 UTC | #2

Second one is model space normals. Not sure what is the third, looks like local vertex position. No idea how they use it.

-------------------------

Kyle00 | 2017-01-02 01:08:44 UTC | #3

you're right about the 2nd one being world space normals, the third one is world space positions. both generated during render to texel routine.

I realized this only after implementing it and dumping the two texture maps to png files.

example scene: cube obj to bake and render to texture plane
[img]http://i.imgur.com/3A5gNZe.jpg?1[/img]

generated textures: world space normal texture map and world space position texture map
[img]http://i.imgur.com/YOLuMVc.jpg?1[/img]

baked image
[img]http://i.imgur.com/lplb9W9.png?1[/img]

-------------------------

