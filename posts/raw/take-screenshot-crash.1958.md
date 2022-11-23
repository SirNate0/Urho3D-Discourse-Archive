godan | 2017-01-02 01:11:49 UTC | #1

Will the function:
[code]
 Graphics->TakeScreenShot(*Image);
[/code]
 crash the app if the graphics device is lost?

I'm getting a crash that suggest this, but I can't really test since I'm not sure how manually lose the device.

-------------------------

cadaver | 2017-01-02 01:11:49 UTC | #2

It's very likely to be an overlooked situation. I believe you would be able to reproduce if you constantly save screenshots in the frame loop, then press Alt-Enter to switch fullscreen. Though I think only D3D9 has an actual "device loss" condition which doesn't clear itself immediately. Are you using D3D9?

-------------------------

godan | 2017-01-02 01:11:49 UTC | #3

Yep, D3D9.

I will try the Alt-Enter thing...For now, I've put in a check that calls IsDeviceLost().

-------------------------

cadaver | 2017-01-02 01:11:50 UTC | #4

Also added the IsDeviceLost() check into D3D9Graphics.cpp / OGLGraphics.cpp in the master branch.

-------------------------

