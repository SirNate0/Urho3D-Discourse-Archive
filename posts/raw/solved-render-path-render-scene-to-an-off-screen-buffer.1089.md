thatonejonguy | 2017-01-02 01:05:23 UTC | #1

I'm trying to achieve a lower resolution "fake" full screen by using the desktop's native resolution for a full screen window and copying a lower resolution FBO of the scene render to it.

I'm wondering if this is possible? and if so, how to set this up in a render path? So that the targets of the scenepass(es) are going to the FBO at a lower resolution.

Thanks,
-Jon

-------------------------

thatonejonguy | 2017-01-02 01:05:23 UTC | #2

I got it figured out. Just needed to specify the "output" for each pass.

-Jon

-------------------------

