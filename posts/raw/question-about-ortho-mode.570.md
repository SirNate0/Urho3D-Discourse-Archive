rogerdv | 2017-01-02 01:01:26 UTC | #1

In the 2D tile map sample I see this in the camera creation:
[code]camera->SetOrthoSize((float)graphics->GetHeight() * PIXEL_SIZE);[/code]

I tested my code with, and without that line. It looks the same, except that using that, the camera start closer to "ground". So, I guess this is not mandatory, but I would like to know whats the effect of this line.

-------------------------

Mike | 2017-01-02 01:01:26 UTC | #2

This is used to auto-adjust 2D camera aspect ratio based on screen resolution.
In this way aspect ratio is also preserved when rotating a mobile device.

-------------------------

