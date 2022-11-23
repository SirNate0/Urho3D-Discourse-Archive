artgolf1000 | 2017-01-02 01:14:49 UTC | #1

Hi,

I want to set 2d texture on BorderImage, but non-square 2d texture doesn't work on iOS device, if I resize the non-square image to square image, BorderImage becomes blurred on the edge.

Art

-------------------------

1vanK | 2017-01-02 01:14:50 UTC | #2

Try to create xml file with settings for texture, like Data\Textures\UI.xml for Data\Textures\UI.png

-------------------------

artgolf1000 | 2017-01-02 01:14:50 UTC | #3

I find that iOS support non-square texture if its size is 512x256, 512x128, etc. so I need not resize all images to squares.
All UI controls look clearly after I apply default UI style to the UI root.

-------------------------

