Ray_Koopa | 2017-09-07 11:40:50 UTC | #1

I want to dock a menubar-like control to the top of the window.
For that I gave it a style which enables anchors and set the max anchor to (1|0), like this:

**menubar.xml**

    <element type="BorderImage" style="MenuBar">
    </element>

**style.xml**

    <element type="BorderImage">
        <attribute name="Blend Mode" value="Alpha" />
        <attribute name="Border" value="8 8 8 8" />
        <attribute name="Texture" value="Texture2D;textures/ui.png" />
    </element>
    <element type="MenuBar" style="BorderImage">
        <attribute name="Image Rect" value="0 40 40 80" />
        <attribute name="Min Size" value="40 40" />
        <attribute name="Enable Anchor" value="true" />
        <attribute name="Max Anchor" value="1 0" />
    </element>

I then add the element to the UI.Root as follows:

    // _defaultStyle has been set as DefaultStyle of UI.Root and represents "style.xml"
    XmlFile layoutFile = ResourceCache.GetXmlFile("menubar.xml");
    UIElement menuBar = UI.LoadLayout(layoutFile, _defaultStyle);
    UI.Root.AddChild(menuBar);

However, the control is not visible when running this.

I noticed that when I remove `Enable Anchor` and `Max Anchor` in the menu bar style, and set it manually _after_ adding the UIElement to the UI.Root, it works as expected and how I saw it in the Urho3D editor:

    <element type="MenuBar" style="BorderImage">
        <attribute name="Image Rect" value="0 40 40 80" />
        <attribute name="Min Size" value="40 40" />
    </element>

    XmlFile layoutFile = ResourceCache.GetXmlFile("menubar.xml");
    UIElement menuBar = UI.LoadLayout(layoutFile, _defaultStyle);
    UI.Root.AddChild(menuBar);
    // Bleh
    menuBar.UIElement.EnableAnchor = true;
    menuBar.UIElement.MaxAnchor = new Vector2(1, 0);

That's a very cheesy solution; is there no way to load anchors correctly from an XML style / layout or am I doing something wrong here or in a bad order?

-------------------------

lezak | 2017-09-07 15:17:47 UTC | #2

You don't see Your uielement because anchor on y axis is set to 0. Attributes for min/max anchor are x (width), y (height). In Your style change max anchor to 1, 0.1 (put there acctual part of screen that it should cover vertically) and add minimal anchor (0, 0 for left-top corner of the screen).

-------------------------

Ray_Koopa | 2017-09-12 18:12:05 UTC | #3

The problem is: I don't have a percentual height it covers, but 40 pixels. Which is why I set the Min Size to 40 40. That should prevent a 0,0 max anchor from making it invisible.

-------------------------

