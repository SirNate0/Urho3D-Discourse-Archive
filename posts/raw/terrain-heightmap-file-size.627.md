rogerdv | 2017-01-02 01:01:44 UTC | #1

A few days ago, I was making some tests with Scape, it is a very basic terrain editor, which generates a 2046x2046 heightmap. I loaded this file in Editor and noticed it became noticeable slower. So, I scaled the image to 513x513 and Editor recovered its usual perfomance. Is 2Kx2K too large for the engine to manage?

-------------------------

cadaver | 2017-01-02 01:01:44 UTC | #2

It depends on several factors like your computer's power and the view distance you're using, but in general 2k x 2k should not be unmanageable. I committed some editor changes which disables traveling through the terrain child nodes in script each frame whenever the terrain node is selected for drawing the debug geometry, as that was both slow and visually quite useless.

-------------------------

