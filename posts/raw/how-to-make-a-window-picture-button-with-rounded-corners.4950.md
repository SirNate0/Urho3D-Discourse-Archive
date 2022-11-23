majhong | 2019-02-21 10:29:23 UTC | #1

How to make a window/picture/button with rounded corners?

-------------------------

dertom | 2019-02-21 10:39:49 UTC | #2

Not sure that will fit 100% to your question but maybe use can use  [Urho2DStretchableSprite](https://urho3d.github.io/samples/51_Urho2DStretchableSprite.html)  for your case.
Code here: https://github.com/urho3d/Urho3D/tree/master/Source/Samples/51_Urho2DStretchableSprite

-------------------------

Leith | 2019-02-21 10:59:48 UTC | #3

you can hack the default style ui texture

-------------------------

dertom | 2019-02-21 11:11:20 UTC | #4

Yes, I guess what @Leith said is much simpler. Just make your own version of https://github.com/urho3d/Urho3D/blob/master/bin/Data/Textures/UI.png and use it in your style instead of the default one.

Look here to find out where exactly the rectangles are defined: https://github.com/urho3d/Urho3D/blob/master/bin/Data/UI/DefaultStyle.xml
Without knowing I guess:
```
    <element type="Button" style="BorderImage">
        <attribute name="Image Rect" value="16 0 32 16" />
        <attribute name="Border" value="4 4 4 4" />
        <attribute name="Pressed Image Offset" value="16 0" />
        <attribute name="Hover Image Offset" value="0 16" />
        <attribute name="Pressed Child Offset" value="-1 1" />
    </element>
...
    <element type="Window" style="BorderImage">
        <attribute name="Image Rect" value="48 0 64 16" />
        <attribute name="Border" value="4 4 4 4" />
        <attribute name="Resize Border" value="8 8 8 8" />
    </element>

```

-------------------------

Leith | 2019-02-21 11:09:52 UTC | #5

relax dude, take your time lol, I'm pretty easy to talk to

-------------------------

Leith | 2019-02-21 11:16:24 UTC | #6

when I was 8, I won a scholarship to a private school, it had ethernet 1.0, and computers were talking to each other, so I hacked the network, demoted all the staff, and they kicked me out without any proof. This was a milestone for me, and a millstone, you know? The one that hangs around your neck for life.

-------------------------

Sinoid | 2019-02-22 02:42:10 UTC | #7

There are no markers indicating edited text that would make that even tangentially related ... maybe don't derail so much?

Tangent derails no one cares ... but this is off in *"I've been bird-watching for 10 years, was subjected to a plagiarism inquiry writing about a subject I'm as knowledgeable as experts because my paper was too good"* in response to "*I'm struggling with finding the volume of my closed quadratic patch shapes*" land. Too much derail, use gitter or IRC for that.

-------------------------

Leith | 2019-02-22 07:44:39 UTC | #8

yeah my bad, I apologize profusely

-------------------------

