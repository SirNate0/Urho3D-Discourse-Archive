joculator | 2017-01-02 01:13:52 UTC | #1

I'm new to Urho and to the community, and let me just say I really like Urho so far and hope it will get me over the C++ graphics programming hump - I've spent most of my programming life in higher-level languages, so thanks in advance for your patience with my future questions.

I'm trying to draw shapes with LINE_STRIPs, specifically circles, regular polygons and so on. I'm able to render shapes but I was wondering whether there is a way in Urho3D's API to modify the glLineWidth of a CustomGeometry instance? My use case is as follows, if it helps: I'm working on a card game which utilizes geometry as a mechanic, so there will be a field of play which is a circle, and many regular polygons inscribed within that circle. Ultimately I'd like to be able to vary the width of the various lines or polygons on the play field. Whether it is easier and better to do this by modifying glLineWidth on a per-geometry basis, or whether I should just use actual models for things like volumetric lines and the circular play-field itself, I am unsure.

Apologies if this question is unclear, and thanks in advance for your help.

Joculator

-------------------------

cadaver | 2017-01-02 01:13:52 UTC | #2

Welcome! Naturally you can modify the engine to add glLineWidth control, however it's unlikely to become a part of the official feature set since it's not supported on Direct3D or OpenGL ES. My recommendation is to use actual geometry for wide lines.

-------------------------

joculator | 2017-01-02 01:13:52 UTC | #3

Thanks, I believe that is the correct way to go as well, certainly at this stage. Thanks for your input!

-------------------------

najak3d | 2021-02-20 03:22:30 UTC | #4

The issue with using geometry to model the lines fails if your goal is for a fixed screenwidth line...  with geometry, how do you "face the line at the camera" (age old problem with drawing nice lines, that have fixed screen width).   And so the standard LineStrip solution fixes this... it draws lines with fixed screen-width, no matter the angle-of-incidence for your camera.

We really need to be able to control the LineWidth. - which does seem to be supported in OpenGL ES (we've been doing this for years, working directly with OpenGL ES).

Maybe I'm missing something, is there some new technique out that the enables you to produce the "exact same effect" as the LineStrip method?  (fixed width on screen, regardless of your viewing angle?)

-------------------------

1vanK | 2021-02-20 07:39:50 UTC | #5

may be helped <https://github.com/memononen/nanovg>

-------------------------

JSandusky | 2021-02-20 18:47:38 UTC | #6

[quote="najak3d, post:4, topic:2198"]
Maybe I’m missing something, is there some new technique out that the enables you to produce the “exact same effect” as the LineStrip method? (fixed width on screen, regardless of your viewing angle?)
[/quote]

Not really "new" but after transform you can perform further adjustments in clipspace to maintain near-pixel perfect sizing since the -1 to 1 ranges map to the whole target-size so the inverse-size * 2 is a pixel in clipspace.

Individual lines aren't really a problem/challenge, the problem is lines with nice corners between them. So either fat-vertices w/ redundant info (geom-shader adjacency won't save you on a closed loop) or pull the data from an SSBO/tex-buffer.

-------------------------

