Lumak | 2017-01-02 01:11:34 UTC | #1

Reading this document, [url]http://www.research.scea.com/gdc2003/spherical-harmonic-lighting.pdf[/url], for the 1st time was confusing, but once I started coding what was in the doc it made more sense.
I'm also using [url]https://code.google.com/archive/p/understanding-the-efficiency-of-ray-traversal-on-gpus/[/url] for a little bit of speed up.

I've been working on this for a less than a week and still got a lot of work remaining, but would like to show my progress anyway.

My sample scene - normal lighting
[img]http://i.imgur.com/EstJMaC.png?1[/img]

Sample scene - SH lighting tech: diffused unshadowed transfer
[img]http://i.imgur.com/3RXYHNp.png?1[/img]

Close up, normal lighting
[img]http://i.imgur.com/UWBrdNs.png?1[/img]

Close up, SH lighting: diffused unshadowed transfer
[img]http://i.imgur.com/j8QV3zh.png?1[/img]

I hope you can see the shading on the SH lighting images.

To do next:
-shadowed diffuse transfer
-interreflective transfer

Edit: added SH lighting technique for images.

-

-------------------------

sabotage3d | 2017-01-02 01:11:34 UTC | #2

This is awesome! I have tried something similar before. Have you captured the shadows in addition to the diffuse lighting? It is also possible to capture Ambient Occlusion and Color Bleeding.

-------------------------

Lumak | 2017-01-02 01:11:36 UTC | #3

[quote="sabotage3d"]This is awesome! I have tried something similar before. Have you captured the shadows in addition to the diffuse lighting? It is also possible to capture Ambient Occlusion and Color Bleeding.[/quote]

I have completed the "shadowed diffuse transfer" which is essentially AO and currently working on "diffuse interreflected transfer" which does color bleeding.

I might have some more images in a day or two.

-------------------------

sabotage3d | 2017-01-02 01:11:36 UTC | #4

Nice. How is the FPS?

-------------------------

Lumak | 2017-01-02 01:11:37 UTC | #5

[quote="sabotage3d"]Nice. How is the FPS?[/quote]

No change in the frame rate. SH is written to vertex color and rendered using DiffVCol technique.

-------------------------

Lumak | 2017-01-02 01:11:39 UTC | #6

Update - all images using 100 SH samples and rendered using diffVCol
Huge limitation using vertex color, especially if the mesh are not high quality.

normal lighting
[img]http://i.imgur.com/ktM4da5.png?1[/img]

diffused unshadowed transfer 
[img]http://i.imgur.com/9PbX4Kj.png?1[/img]

shadowed diffuse transfer
[img]http://i.imgur.com/H2UCO6t.png?1[/img]

diffuse interreflect transfer
[img]http://i.imgur.com/8B9iWNl.png?1[/img]

-------------------------

Lumak | 2017-01-02 01:11:41 UTC | #7

Created a repository - [url]https://github.com/Lumak/Urho3D-1.4-SphericalHarmonicLighting/[/url] if anyone is also interested in this topic.

-------------------------

sabotage3d | 2017-01-02 01:11:42 UTC | #8

Thanks a lot Lumak. Using SH as vertex color is quite limited, it looks a lot better if used as multiple light probes: [url]http://blogs.unity3d.com/2011/03/09/light-probes/[/url]

-------------------------

