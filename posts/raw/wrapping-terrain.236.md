maninblack | 2017-01-02 00:59:04 UTC | #1

I'm trying to implement terrain wrapping, so that you can continuously scroll horizontally around the world.  I found a description that describes doing this with two render passes.  The first pass renders the camera at it's normal position, and the second pass renders the camera at an offset.

I've got this working using 2 offset cameras (2 overlapping viewports with different renderpaths).  The first one is the normal Forward renderpath.  The second one is the same, except the clear command is removed.  

The issue is that lighting won't work properly at the edge where the world wraps around.  What is the right approach to deal with that?

-------------------------

