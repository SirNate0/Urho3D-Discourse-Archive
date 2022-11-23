Xardas | 2017-01-02 00:57:52 UTC | #1

I can't get the ToolTip to work. I added it as a child to an existing sprite, and I also added a new sprite to the ToolTip (so that it shows the new sprite when hovering over the existing sprite). But when I hover over the (parent) sprite, nothing ever happens.

-------------------------

friesencr | 2017-01-02 00:57:52 UTC | #2

Are you setting a height/width set on the tooltip?

Here is how the editor creates tooltips:
[code]
UIElement@ CreateToolTip(UIElement@ parent, const String&in title, const IntVector2&in offset)
{
    ToolTip@ toolTip = parent.CreateChild("ToolTip");
    toolTip.position = offset;

    BorderImage@ textHolder = toolTip.CreateChild("BorderImage");
    textHolder.SetStyle("ToolTipBorderImage");

    Text@ toolTipText = textHolder.CreateChild("Text");
    toolTipText.SetStyle("ToolTipText");
    toolTipText.text = title;

    return toolTip;
}
[/code]

Here are those styles
[code]
    <element type="ToolTipBorderImage" style="BorderImage">
        <attribute name="Layout Mode" value="Horizontal" />
        <attribute name="Layout Border" value="6 2 6 2" />
        <attribute name="Image Rect" value="48 0 64 16" />
        <attribute name="Border" value="6 2 2 2" />
    </element>
    <element type="ToolTipText" style="Text">
        <attribute name="Font" value="Font;Fonts/BlueHighway.ttf" />
        <attribute name="Font Size" value="12" />
    </element>
[/code]

The tooltip in the editor automatically calculates its height/width from the "Layout Mode"

-------------------------

Xardas | 2017-01-02 00:57:52 UTC | #3

Thanks. But I've now tried about a dozen things, and I still can't see my ToolTip. I'm using C++, by the way. I'm also not sure if I'm supposed to call the ToolTip's public Update function? Either way, it still doesn't work.

Maybe someone could post a minimal code example in C++ that works?

-------------------------

Mike | 2017-01-02 00:57:52 UTC | #4

I'll send a pull request tomorrow, adding drag and tooltip to sample#02 HellloGUI.

-------------------------

Xardas | 2017-01-02 00:57:53 UTC | #5

I just took a look at it, thanks. So it turns out ToolTips only work with buttons. That's good to know.

-------------------------

cadaver | 2017-01-02 00:57:53 UTC | #6

Tooltips should work with any element that has input enabled, so that they recognize being hovered on. Sprites and bare UIElements are assumed to be passive decoration by default, so you'll need to enable input by calling SetEnabled(true) on them.

-------------------------

Xardas | 2017-01-02 00:57:54 UTC | #7

Ah, that makes sense!

-------------------------

