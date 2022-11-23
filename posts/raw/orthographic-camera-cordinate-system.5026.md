zoot70 | 2019-03-13 13:06:43 UTC | #1

Is it possible to set up the orthographic camera such that 0,0 is in the top left of the screen, positive Y is down and sprite2d instances are positioned in pixel values?

Thanks

-------------------------

Leith | 2019-03-14 04:34:31 UTC | #2

Welcome to the community! :confetti_ball:

I have done hardly any work in 2D on Urho (I tend to work mainly in 3D, and avoid the 2D world when I can), but the UI system uses the top left corner for the origin.
Higher Y values are lower down the screen.

-------------------------

guk_alex | 2019-03-14 08:23:01 UTC | #3

Look at the Urho2DSprite sample if you didn't (and other Urho's 2D examples as well), there's a call:

`camera->SetOrthoSize((float)graphics->GetHeight() * PIXEL_SIZE);`

This call seems to set a range of coordinates of the viewport, with combination of SetAspectRatio you'll get close to what your desired  (but with 0,0 being the middle). This allows you to use pixel coords relative to the centre (you can map them with one simple function to your desired range).

`float halfWidth = graphics->GetWidth() * 0.5f * PIXEL_SIZE;`
`float halfHeight = graphics->GetHeight() * 0.5f * PIXEL_SIZE;`
`spriteNode->SetPosition(Vector3(Random(-halfWidth, halfWidth), Random(-halfHeight, halfHeight), 0.0f));`

But truly saying the approach of mapping the viewport to the exact screen coordinates isn't really flexible - your game will look right only on one supported resolution. It's better to optimise to the specific aspect ratio and pixel density, if you interesting in it you'll better to read more on how gamedevs usually work with coordinates and different resolutions. But if you aim to only one resolution for own tests it's fine, but don't get too deep in it!

-------------------------

