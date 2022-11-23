Haukinger | 2022-01-30 10:05:50 UTC | #1

I'm rendering a flat, tiled world with an orthographic camera in OpenGL. While testing, I have just 5x5 unit-sized, flat textured tiles with ortho size 1 and zoom starting at 1.

When zooming out, frame time increases drastically (100s of milliseconds for just 25 quads at zoom 0.02 on my gtx 980) even though the rendered scene becomes smaller and smaller.

Is this a known problem or am I doing something completely wrong?

-------------------------

