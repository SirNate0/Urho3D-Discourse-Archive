slapin | 2017-03-08 08:41:41 UTC | #1

Hi, all!

While struggling with GUI system I found several  major problems I'm unable to solve for very long time.

1. In windowed mode, when window is controlled by window manager in X11
I try to put simple menu (out of default buttons) in the center. For some strange reason, regardless of window
size I see resolution reported to be 1024x768, so menu is offset and not really adequate. There's no such
problem with full screen, but I need windowed mode to be working right.

2. In many cases I want widgets to be automatically placed on screen. I know how to do it by hand,
but is it possible to set some default for some container so everything there is autoplaced?

3. When Adding items to container dynamically, containers often break and display items one over another.
It doesn't happen when I just set up them once via xml.

4. I can't make drop-down list work. Whatever I try I can't see any items inside. I know it works in editor,
but when I copy-paste it breaks.

I try this all with AngelScript.

Also I have additional question - is it possible to create custom widget using AnglScript? Most
important widget I need it a button, and i can represent everything with buttons and windows,
except for input boxes (which work too, so no problem here) but I'd like to have some changes on layout and
style (I don't need this GUI-system look, just clickable pic is fine), but I need widget-relative coordinates
from mouse clicks, is it possible to implement with AngelScript-only?

Thanks!

-------------------------

