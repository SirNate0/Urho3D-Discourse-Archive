russ | 2017-01-02 01:10:13 UTC | #1

Hello,

I have been testing Urho3D for a 2D game that I'm making.  I've been having some strange artifacts that seem to be based on the position of the sprite, which seems really strange to me, since I've configured it with an orthographic camera.  When it's near the origin, the sprite has some slight distortions, which mostly resolve as it moves away from the origin.  I'm using DX9 on Windows, and Urho3D is built from master on github from about a week ago.

The test code is below.  I also have an image gallery showing the issue, but this is my first post and it's not letting me post a link.  I'll try to post it as a reply.

Thanks in advance for any help!

Russ

[gist]https://gist.github.com/russpowers/80ab8485e41e1a8b5923[/gist]

-------------------------

russ | 2017-01-02 01:10:13 UTC | #2

Here are the images: [imgur.com/a/Tyd8H](http://imgur.com/a/Tyd8H)

The first shows the problem when the position is near (0,0).  Once it moves a bit, it resolves to the second image.  The third image is the original.

-------------------------

russ | 2017-01-02 01:10:14 UTC | #3

I've been playing around with it some more, and the distortion does not occur when the texture size is a power of two (my original image was 24x24).

-------------------------

