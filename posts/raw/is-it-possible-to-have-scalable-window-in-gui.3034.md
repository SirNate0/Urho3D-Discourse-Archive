slapin | 2017-04-21 15:43:37 UTC | #1

Hi, all!

I have a GUI written in AS. I want to display in window, I can use -w option of player for that.
But I want to scale the window size using window manager, but I'm not allowed to. Any ideas?

-------------------------

KonstantTom | 2017-04-21 18:29:08 UTC | #2

The simplest way is to check the size of the window each frame ('graphics.width' and 'graphics.height' in AS), and, if it was changed, resize your user interface.
Also you can use `UIElement`'s anchors.

-------------------------

