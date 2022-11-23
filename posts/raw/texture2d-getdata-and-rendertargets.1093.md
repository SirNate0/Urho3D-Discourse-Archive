cadaver | 2017-01-02 01:05:24 UTC | #1

GetData() likely was never used with rendertargets before, so the case had not been considered. Feel free to add the support. It's a bit iffy function as for example on OpenGL2 ES it's certain *not* to work.

EDIT: I'm checking this now too, if things go smoothly I may commit a fix today. Will verify OpenGL & D3D11 operation at the same time, and add a function to determine the amount of image components required to hold the data (see [topic1112.html](http://discourse.urho3d.io/t/saving-rendertarget-texture-to-image/1080/1))

-------------------------

cadaver | 2017-01-02 01:05:25 UTC | #2

Should be fixed in the master branch now. D3D11 & OpenGL already worked.

-------------------------

