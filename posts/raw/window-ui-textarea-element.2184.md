MikeDX | 2017-01-02 01:13:45 UTC | #1

Hello everyone

I am trying to put some small UI example together using Urho3D, and have a few questions.

Is there a multi-line (notepad) style widget/element available to use? I'm guessing not - as opening a script in the editor opens an external text editor.


*edit* the questions below I originally asked, but have found answers since - leaving them here in case anyone else finds them useful in future.

Is there a working example somewhere of resizing a window element in the UI? I've been trying various things but nothing so far has worked.

Taking the 02_HelloUI.as example, I've made the window movable by adding some extra callbacks (the fish drag callback wasnt compatible for some reason).

Setting the window.resizable = true doesnt seem to show any "ears" to resize the window from, so I'm a little confused.

I've tried to RTFM, but it's all a bit confusing at this stage.

*edit* I think I've found an example as part of Editor.as - so I'll look into that!


Is it possible to have a child element of a window that is a pixel buffer?
* edit* This seems doable with the Image class and setData() so I'll use that!

Many thanks in advance for your help / input! :slight_smile:

-------------------------

Mike | 2017-01-02 01:13:46 UTC | #2

A Window becomes movable when its alignment is free (and of course window.movable = true).

So in sample #2:
[code]
// window.SetAlignment(HA_CENTER, VA_CENTER); ~ line is commented to free the alignment
window.resizable = true;
[/code]

You won't see "ears" for resizing when resizable is set to true, just grab the borders and you'll be able to resize your window.
Note that you can control the size of the borders using resizeBorder.

-------------------------

MikeDX | 2017-01-02 01:13:46 UTC | #3

[quote="Mike"]A Window becomes movable when its alignment is free (and of course window.movable = true).

So in sample #2:
[code]
// window.SetAlignment(HA_CENTER, VA_CENTER); ~ line is commented to free the alignment
window.resizable = true;
[/code]

You won't see "ears" for resizing when resizable is set to true, just grab the borders and you'll be able to resize your window.
Note that you can control the size of the borders using resizeBorder.[/quote]

I tried this before, and it didn't work. What is confusing is the Editor.as windows all have those positions you can grab to stretch / resize each window.
[code]
//    window.SetAlignment(HA_CENTER, VA_CENTER);
    window.name = "Window";
    window.resizable = true;
[/code]

commenting the setalignment window just shoved the window to top left.

Do you know what settings / flags / callbacks I need to make the cursor change to the arrows so that resize can be done?

Ideally I want to place an Image buffer in one of these windows but so far not been able to - window.AddChild(Image) doesnt work, so I'm going to try with BorderImage, but that means plotting the pixels to an image, then rendering to a texture, then putting the texture in the borderimage, which seems like a lot of effort!

-------------------------

Mike | 2017-01-02 01:13:46 UTC | #4

[quote]commenting the setalignment window just shoved the window to top left.[/quote]
Commenting this line:
- sets the window at position (0,0) with a free alignment
- as the alignment is free, you need to set its position on your own
- alows to freely resize the window when resizable is set to true
- allows to freely move the window when movable is set to true

[quote]I tried this before, and it didn't work.[/quote]
Did you both set window.resizable [b]and [/b]disabled auto alignment ? Currently they are exclusive.

[quote]Do you know what settings / flags / callbacks I need to make the cursor change to the arrows so that resize can be done?[/quote]
You will need to create a cursor UI over your OS cursor, as it is done in a few other samples (#8, #15, #39...):
[code]
XMLFile@ style = cache.GetResource("XMLFile", "UI/DefaultStyle.xml");
Cursor@ cursor = Cursor();
cursor.SetStyleAuto(style);
ui.cursor = cursor;[/code]
This allows the cursor to display the arrows when hovering a resizable border.

-------------------------

MikeDX | 2017-01-02 01:13:46 UTC | #5

Perfect. Thank you very much :slight_smile:

-------------------------

