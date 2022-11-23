esak | 2017-01-02 01:09:54 UTC | #1

When I run my game on iOS (iPad Mini) the objects (nodes) that are receiving shadows are distorted, the material is kind of flickering (with really small black points).
This doesn't happen when I run on my Android devices, nor on Windows/OSX.
But on the other hand, it does happen on my Nvidia Shield Android TV also.
If I turn off the shadows it displays as expected.
Any ideas what could be wrong here and how to overcome this?

-------------------------

esak | 2017-01-02 01:09:57 UTC | #2

I think my problem is with the material/texture.
When I changed the material's technique from Diff to DiffAlpha it displays correctly with shadows on.
But the problem I get then is that the models/nodes are not displayed in the right order (nodes that should be in front off some other nodes are placed back).
Any ideas how I could overcome this?

-------------------------

esak | 2017-01-02 01:10:01 UTC | #3

After some more investigation I found out that the problem is "self-shadowing".
With this in mind I experimented with different values for the light's BiasParameters and got it to look much better, but not 100% accurate (since some part of the shadows got some glitches now).

-------------------------

