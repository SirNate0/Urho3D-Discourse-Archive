NiteLordz | 2017-01-02 01:03:50 UTC | #1

Right now, when i run anything involving the inbuilt UI system, it has to be customized per resolution.  Meaning, if i have a text element that is size 20 pt, and run it on a 800x400 window and a 1024x768 window, the font size doesn't show appropriately on them. On one not all the text is displayed. 

I was checking, and i didnt see any setting that would allow the UI to scale.

So do i have to provide different UI layouts based on the resolution of the application?

-------------------------

cadaver | 2017-01-02 01:03:50 UTC | #2

Everything is done in pixels, so it doesn't scale. As an alternative you can scale the UI layout in code (ie. go through all elements, resize them)

-------------------------

