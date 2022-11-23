rogerdv | 2017-01-02 01:01:53 UTC | #1

How can I define and use my own cursors? I tried creating one in Editor, but when I checked the xml I found that it has several Shapes, which I cant access from the Editor. Seems that I have to manually edit the xml and set the shapes manually, am I right?

-------------------------

weitjong | 2017-01-02 01:01:53 UTC | #2

There are two types of cursor "modes" supported by the Cursor class: 1) OS (operating system) shapes or 2) custom shapes. At the moment in our master branch, both modes has a predefined maximum of shapes in an enum. There is a PR from Alex which attempts to remove this limit (I think perhaps only in custom shapes mode). Anyway, you can define a custom shape for cursor or any UI elements for that matter in a custom texture of your own. Of course, it has to be accompanied with a matching XML file (similar to DefaultStyle.xml or OldStyle.xml) that defines the "image rect" to be used for each UI element, among other attributes. Our current UI editor does not yet support editing the UI "stylesheet" or "skin" or whatever you want to call it, so yes, you have to manually edit it for now.

But to answer your question directly. You can also define a custom shape for a single CursorShape enum by using Cursor::DefineShape() method. The caveat is, you have to use one of the predefined enum (until the above PR has been merged).

-------------------------

Azalrion | 2017-01-02 01:01:59 UTC | #3

Just to let you know rogerdv, the PR which allows further customization of cursors was merged today and is available in master, but be warned it does change the xml. You can see more under Cursor Shapes at the bottom of: [urho3d.github.io/documentation/HEAD/_u_i.html](http://urho3d.github.io/documentation/HEAD/_u_i.html).

-------------------------

rogerdv | 2017-01-02 01:02:00 UTC | #4

Thank you!

-------------------------

