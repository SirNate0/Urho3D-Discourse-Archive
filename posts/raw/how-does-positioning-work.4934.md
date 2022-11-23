Jbonavita | 2019-02-16 18:02:32 UTC | #1

I'm trying to layout sprites in a simple 2D scene. I was able to get the background image and the top HUD image. Although, I don't know if I'm doing it right.

It seems the screen range is 5 to -5 and the width is 10 to -10 (in landscape). Is this accurate?

When trying to place a sprite a long the bottom, I can't seem to get it right. Is there a way to change the anchor point on the sprite to the left bottom?

-------------------------

Leith | 2019-02-17 03:24:05 UTC | #2

Typically, 2D screen range depends on the orthographic Projection transform of the camera... if you set it to Identity, the coordinates will range from -1 to +1 in both directions, which causes a square object to appear stretched horizontally / aspect ration is being ignored. If you play with the ortho projection, you can make your screen range be anything you want.
(I'm pretty sure its -1 to +1, but it may be +/- 0.5 ... been a while since I worked in 2D)

-------------------------

