snkar | 2019-02-08 15:00:22 UTC | #1

I need to be able to render some text in a Text3D component which will have a defined max width and max height. So with a predefined font type and font size, if the rendered text exceeds the assigned width and height, it should truncate the text and render with ellipsis. Something like a windows forms Graphics.MeasureString custom algorithm would be the target.

I tried with setting the Width and WordWrap property and then examining the NumChars, NumRows, RowHeight and RowSpacing to come up with some custom logic to find the number of characters that can be fit in the assigned width and then using the NumRows, RowHeight and RowSpacing to calculate the height requirement and truncate as required. But the issue is that the  **Width property is an integer**  and the max width will always be in float resulting in the logic to fail(0.019 results in width being set as 0).  **Why is Width for Text3D in Integer?**

Does anyone has any ideas around this? Maybe I am over complicating things and it would be as simple as setting some property but I cannot figure out how.

-------------------------

Leith | 2019-02-09 09:32:58 UTC | #2

I am sorry, I have been wrapped up with 3d skinned mesh animation details, like foot planting, so sorry i cant answer your ui question but i promise to look into it

-------------------------

Leith | 2019-02-10 09:56:10 UTC | #3

The reason that Width is integer, is that internally, Text3D is using a Text object (2D) which has integer width because it was designed for pixel coordinates (which I despise, personally, as they are not a good fit with a window that can be resized - I prefer to use Normalized Coordinates, which are scalars that are applied to the window width and height at runtime, so your UI works in any window size).
See the Text3D::text_ member...
[code]
void Text3D::SetWidth(int width)
{
    text_.SetMinWidth(width);
    text_.SetWidth(width);

    MarkTextDirty();
}
[/code]

As for truncating your 3D text, I would have thought that enabling WordWrap, but not providing enough vertical Height for a second line of text, should do the job.

In one of my previous engines, we did use floating point NDC screen coordinates for UI, and even used pixel subsampling in shaders, based on our ability to provide a subpixel screen location.

-------------------------

snkar | 2019-02-11 04:58:49 UTC | #4

Only enabling WordWrap = true without specifying the Width does not work. As is specified in the documentation, the WordWrap and Width property has to be set together for the control to respect the width setting. Only specifying WordWrap = true removes the text assigned.
The issue is that since the Width property of Text3D is an integer and I am getting the MaxWidth and MaxHeight settings from the parent control in which the Text3D component is attached, the width and height values are coming in the form of floats. As an example, the MaxWidth and MaxHeight that is allowed for the Text rendering component is lets say 0.4f and 0.02f. I was wondering is there a way to convert the 0.4f value to the pixel coordinate based integer value?

-------------------------

Leith | 2019-02-11 05:00:27 UTC | #5

I figured setting the width on wordwrap was obvious - my apologies for not being more specific.

-------------------------

snkar | 2019-02-11 05:11:29 UTC | #6

I think I might have also misinterpreted your suggestion. But the primary issue here is how do I set the Width property of the Text3D component based on the Maximum Width that is allowed when these values are in different units and data types. The max width that this text component can have based on my application logic is in floats while the Width property is itself in Integers. So either some way to convert the float value to the equivalent pixel coordinate based integer value is required or maybe some completely different approach. Any ideas?

-------------------------

Leith | 2019-02-11 07:10:09 UTC | #7

From what I understand, your 3D text exists on a theoretical 2D rectangle, of given width and height - I know, pixel coordinates make no sense in 3D, unless we assume a scale of 1, and a billboard camera view - I think it's just meant to provide a baseline set of values, and I am not sure exactly how the mapping works. The integer width is related to the size of your font, which I am not certain is given in pixels either, to add more mud to the water. I'm afraid I'm not going to be a lot of help with this issue, unless I was to implement something in my current project that actually uses 3D text. I understand font glyphs and such, but what you're asking for is a proper mapping between the 2D text rectangle, and the 3D oriented text rectangle, which I believe is undocumented. I'm willing to look into it more, of course. One would hope that a transform between 3D space and texture space is well defined, and we can just use that transform and its inverse to transform between those spaces.
[EDIT]
There is a 3D UI sample, that maps a 2D UI to a 3D oriented rectangle. Surely this sample has some clues about the appropriate mapping.

-------------------------

snkar | 2019-02-12 04:26:17 UTC | #8

Can you specify the location for the 3D UI sample that you talk about. Maybe I can take a look and find something interesting.

-------------------------

snkar | 2019-05-23 13:20:03 UTC | #9

I just created a couple of sample sketches to explain the target solution better.

**Sample 1**: A panel with two buttons and the middle portion is the text label which has a fixed width and height and the text assigned fits nicely inside the dimensions: 
![](upload://cKyP86Lxc5I5zoxm7K8lx6gMU2T.png)

**Sample 2**: The same panel with a text of larger length assigned and since Text3D will resize freely to accommodate the text, it expands beyond the specified max width and max height:
![](upload://cbbKJ72lzIy5p1zjnHSdfck6Uph.png)

**Sample 3**: This is the target solution where the larger length text is split across multiple lines to fit the max allowed width and since it still does not fit the max height, the text is truncated at the appropriate position and indicated by specifying ellipsis.
![](upload://phFyZqas2fUxzyc7wmtyvUMkXQ9.png)

I hope the above three samples and the images will make the issue easier to understand.

-------------------------

Leith | 2019-02-12 10:03:38 UTC | #10

The sample I mentioned, is called 48_Hello3DUI
You're saying that due to resizing, the limits you specified for width and height on 3D text are not being observed? Interesting - I might have to implement something just so I can properly look into this - seems like a bug to me!

-------------------------

snkar | 2019-02-12 10:40:21 UTC | #11

I guess my explanation was not clear or maybe it was too detailed and lost the essence. What I am saying, that if I was able to set the limits for Width and Height on 3DText, I am sure the issue would have been solved. But I cannot set the limits as the Width and Height limits that I have are in floats and the properties that I have to set on Text3D are in integers. So it will not work.

-------------------------

Leith | 2019-02-13 05:30:23 UTC | #12

Just cast the floats to integers, and accept that their values will lose precision as integers.
eg my3DText->SetWidth( (int) fWidth );

-------------------------

snkar | 2019-02-13 06:10:22 UTC | #13

Yes, I was trying in a similar way. But what if my max allowed width is 0.76. In that case, when I cast, it reduces to 0, which defeats the purpose.

-------------------------

Leith | 2019-02-13 06:23:35 UTC | #14

Typically, we define our 3D canvas dimensions much larger than that, and then scale the canvas back down to the 3D dimensions we prefer. For example, make the canvas 100 x 32 in size, and set its parent node's scale to (.01, .01) and you'll have a rectangle that internally "thinks" it has a 2D size of 100x32, but in 3D it will be 1.0 x 0.32 3D units in size.
I'm not certain this is the correct way to "map" your text size from 2D to 3D, but it appears to be how Unity deals with this - in their editor, their UI canvases look enormous, and can often span your entire 3D scene! Ideally, what you want is a matrix that performs this mapping for you, and not using node scaling, since Urho3D UI is not part of the regular scenegraph - there is a SetScale method in UIElement base class I believe, and another in the UI subsystem itself.

-------------------------

Modanung | 2019-02-13 10:43:38 UTC | #15

[quote="snkar, post:13, topic:4906"]
But what if my max allowed width is 0.76. In that case, when I cast, it reduces to 0, which defeats the purpose.
[/quote]

You may be looking to `RoundToInt(T)` or `CeilToInt(T)` in that case.

And welcome to the forums, btw. :confetti_ball: :slightly_smiling_face:

-------------------------

Leith | 2019-02-13 12:26:27 UTC | #16

you can set w and h on your 3d text object, whats the actual problem?

-------------------------

Leith | 2019-02-13 12:27:32 UTC | #17

ok, so your font is size 16, but you want to print it into what area? 0.76 isnt going to cut it man, not in any space

-------------------------

Leith | 2019-02-13 12:28:28 UTC | #18

see what i mean? you need to at least respect your font size

-------------------------

