rogerdv | 2017-01-02 01:01:42 UTC | #1

I have noticde something while working with the UI layout editor: if I have a hierarchy of elements and I save a child element, it erases the whole hierarchy in the file. I have to select the parent element and save, otherwise, the work is lost. Is this a feature or a bug?

-------------------------

weitjong | 2017-01-02 01:01:42 UTC | #2

To save the whole hierarchy, you should choose the "Save UI-layout" menu item and not the "Save child element".

-------------------------

rogerdv | 2017-01-02 01:01:42 UTC | #3

Well, seems that I cant reproduce the problem right now. But I have found myself with all my work erased a couple of times, and I thouth it was because I was pressing Alt-S while child element was selected (never used Save child element, actually, didnt knew it existed until you mentioned).

-------------------------

friesencr | 2017-01-02 01:01:42 UTC | #4

I reported this kind of thing a couple weeks ago.  The layout editor does make a backup of the old file when you hit the save button behind the scenes now.

-------------------------

