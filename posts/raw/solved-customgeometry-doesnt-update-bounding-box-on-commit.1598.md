TikariSakari | 2017-01-02 01:08:49 UTC | #1

Hello, I am having troubles with CustomGeometry. When I add more vertices to a customgeometry, and do commit, I get to see the new updated mesh, but the bounding box from debugrenderer doesn't seem to be changed from the initial commit. I tried checking the boundingbox from the CustomGeometry and that does seem to get updated, but the worldbounding doesn't. I tried modifying the worldbound but that didn't seem to affect the culling of the object, even tho the debug geometry did change.

I also noticed that if I do several commits on same frame as the CustomGeometry is added, this does seem to update the bounding box, but if I add a cube on a click of a button to the customgeometry, it doesn't seem to actually update the bounding box, when it happens on different frames and thus the CustomGeometry doesn't show unless the boundingbox from debug geometry is visible.

edit: and as usual, the moment I write something I find somewhat solution, well at least it updates the bounding box if I re set the position of the node that it was attached into, which is what I happened to do on the doing several commits thing. I set the position of the node after doing multiple commits, and that is the reason why the worldboundingbox got updated. Still though I think this is actually a bug in somewhere that it doesn't update the objects world bounding box automatically after calling commit-function.

-------------------------

cadaver | 2017-01-02 01:08:50 UTC | #2

Yes, this sounds like a bug. The world bounding box should be marked as dirty on commit. Should be simple to fix.

-------------------------

cadaver | 2017-01-02 01:08:51 UTC | #3

Should be fixed now in the master branch.

-------------------------

TikariSakari | 2017-01-02 01:08:51 UTC | #4

thank you, this does indeed fix the bug and adjust the bounding box on commit.

-------------------------

