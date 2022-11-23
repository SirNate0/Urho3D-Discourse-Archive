rogerdv | 2017-01-02 01:02:09 UTC | #1

A few days ago I decided to try the latest AMD drivers (Omega).  I wanted to see if I actually had some improvement, so I tested 14.9 with Unigine Heaven, then modified my Urho game to display FPS. Then I tested my program with mesa drivers after uninstalling Catalyst 14.9, and last, tested 14.12 Omega with Heaven and my Urho app. The result was quite similar with both Catalyst drivers, confirming that Omega is not an essential update at all. The surprising result was that my Urho3d project reached up to 200 FPS with mesa, but no more than 194 FPS with 14.9 and 198 with 14.12. 
Im really curious about this and Im even thinking about implementing a dedicated benchmark mode and scene in my game for future tests.

-------------------------

alexrass | 2017-01-02 01:02:10 UTC | #2

My experiment on Half-Life 2:
opensource driver > 80 fps
proprietary driver 20-40 fps

-------------------------

boberfly | 2017-01-02 01:02:14 UTC | #3

Which GPU are you using? The test is most likely CPU-bound I'd say so perhaps the open source driver has slightly less overhead in the driver? FPS is never a good indicator, need to see ms.

You could also test Gallium-nine by building Urho3D with mingw and DX9 enabled instead of GL and running wine. Long ago I built Urho3D like this but just running the WineD3D GL wrapper not Gallium-nine over the Nvidia proprietary driver and it worked perfectly, but I didn't really look at the performance, it was more or less to see if I could do it and keep development in Linux while making Windows builds at the same time. Having said that I don't really use the DX9 backend of Urho3D anymore for Windows. :slight_smile:

-------------------------

rogerdv | 2017-01-02 01:02:15 UTC | #4

The GPU was an R7 250. I was only interested in testing Linux ATM, but yesterday looked at DX perfomance in Windows and the framerate keeps around 200-201, with Catalyst 14.9.

-------------------------

Stinkfist | 2017-01-02 01:02:21 UTC | #5

Note that FPS is capped at 200 by default on desktop builds. You might want to disable it while testing the performance using -nolimit command-line switch.

-------------------------

rogerdv | 2017-01-02 01:02:23 UTC | #6

Ah, I was blaming Fraps on windows for that weird 200 FPS, but then noticed it on Linux too. Whats the reason for such limit?

-------------------------

Stinkfist | 2017-01-02 01:02:23 UTC | #7

This was actually discussed recently on the issue tracker: [github.com/urho3d/Urho3D/issues/578](https://github.com/urho3d/Urho3D/issues/578)

-------------------------

