zombiegonsdude | 2017-01-02 01:14:55 UTC | #1

Was wondering if someone could provide an example of how to use the ListView class.

I've been trying to get what I can from the file list view in the editors resource browser, but no luck with getting the text elements to layout vertically and the scroll bars to show up.

What I have so far.

[code]
ListView@ list = levelsWindow.GetChild("ListContainer", true);

if (list !is null)
{
    Text@ content = Text();
    content.layoutMode = LM_HORIZONTAL;
    list.InsertItem(list.numItems, content);

    for (uint i = 0; i < 15; ++i)
    {
        Text@ text = Text();
        content.AddChild(text);

        text.text = "Foobars and Stuff";
        text.style = "FileSelectorListText";
    }
}
[/code]

-------------------------

zombiegonsdude | 2017-01-02 01:14:56 UTC | #2

Got it working, looked at the particle editor for reference. It's a bit confusing in the UI editor with the elements that have the internal="true" property. Makes sense though, there's some ScrollBar elements, a BorderImage element and then another UI element that's a child of the BorderImage element that are all hidden in the UI editor because they're created by the ListView itself it seems.

Also the parent window element needs to have its layout options set for the list view to be fitted.

Also you have to use "InsertItem" and not "AddChild". AddChild is inherited from UIElement and AddItem / InsertItem are defined on the ListView class. I guess this is because these calls will manage adding and removing elements from the child UIElement container that is hidden.

Here's what I have for the angelscript.

[code]
ListView@ list = levelsWindow.GetChild("ListContainer", true);

if (list !is null)
{
    for (uint i = 0; i < 15; ++i)
    {
        Text@ text = Text();
        list.InsertItem(list.numItems, text);

        text.text = ("Dynamic Text Element " + i);
        text.style = "FileSelectorListText";
    }
}
[/code]

Here is what I have for the XML file that is loaded.

[code]
<?xml version="1.0"?>
<element type="Window">
	<attribute name="Position" value="548 260" />
	<attribute name="Size" value="549 312" />
	<attribute name="Pivot" value="0 0" />
	<attribute name="Layout Mode" value="Vertical" />
	<attribute name="Layout Border" value="15 15 15 15" />
	<attribute name="Is Movable" value="true" />
	<attribute name="Is Resizable" value="true" />
	<element>
		<attribute name="Pivot" value="0 0" />
		<attribute name="Layout Mode" value="Vertical" />
		<element type="ListView" style="PanelView">
			<attribute name="Name" value="ListContainer" />
			<attribute name="Min Size" value="100 50" />
			<attribute name="Pivot" value="0 0" />
			<element type="ScrollBar" internal="true" style="none">
				<attribute name="Size" value="519 16" />
				<attribute name="Min Anchor" value="0 1" />
				<attribute name="Max Anchor" value="0 1" />
				<attribute name="Pivot" value="0 1" />
				<attribute name="Color" value="0 0 0 0" />
				<attribute name="Top Left Color" value="0 0 0 0" />
				<attribute name="Top Right Color" value="0 0 0 0" />
				<attribute name="Bottom Left Color" value="0 0 0 0" />
				<attribute name="Bottom Right Color" value="0 0 0 0" />
				<element type="Button" internal="true" style="none">
					<attribute name="Pivot" value="0 0" />
				</element>
				<element type="Slider" internal="true" style="none">
					<attribute name="Position" value="16 0" />
					<attribute name="Size" value="487 16" />
					<attribute name="Pivot" value="0 0" />
					<element type="BorderImage" internal="true" style="none">
						<attribute name="Pivot" value="0 0" />
					</element>
				</element>
				<element type="Button" internal="true" style="none">
					<attribute name="Position" value="503 0" />
					<attribute name="Pivot" value="0 0" />
				</element>
			</element>
			<element type="ScrollBar" internal="true" style="none">
				<attribute name="Size" value="16 282" />
				<attribute name="Min Anchor" value="1 0" />
				<attribute name="Max Anchor" value="1 0" />
				<attribute name="Pivot" value="1 0" />
				<attribute name="Color" value="0 0 0 0" />
				<attribute name="Top Left Color" value="0 0 0 0" />
				<attribute name="Top Right Color" value="0 0 0 0" />
				<attribute name="Bottom Left Color" value="0 0 0 0" />
				<attribute name="Bottom Right Color" value="0 0 0 0" />
				<element type="Button" internal="true" style="none">
					<attribute name="Pivot" value="0 0" />
				</element>
				<element type="Slider" internal="true" style="none">
					<attribute name="Position" value="0 16" />
					<attribute name="Size" value="16 250" />
					<attribute name="Pivot" value="0 0" />
					<element type="BorderImage" internal="true" style="none">
						<attribute name="Pivot" value="0 0" />
					</element>
				</element>
				<element type="Button" internal="true" style="none">
					<attribute name="Position" value="0 266" />
					<attribute name="Pivot" value="0 0" />
				</element>
			</element>
			<element type="BorderImage" internal="true" style="none">
				<attribute name="Pivot" value="0 0" />
				<element internal="true" style="none">
					<attribute name="Pivot" value="0 0" />
					<element type="Text" style="EditorAttributeText">
						<attribute name="Pivot" value="0 0" />
						<attribute name="Text" value="Static Text Element 01" />
					</element>
					<element type="Text" style="EditorAttributeText">
						<attribute name="Pivot" value="0 0" />
						<attribute name="Text" value="Static Text Element 02" />
					</element>
					<element type="Text" style="EditorAttributeText">
						<attribute name="Pivot" value="0 0" />
						<attribute name="Text" value="Static Text Element 03" />
					</element>
				</element>
			</element>
		</element>
	</element>
</element>
[/code]

-------------------------

zombiegonsdude | 2017-01-02 01:14:57 UTC | #3

Just another quick follow up. Depending on the UI element your adding you might need an additional container to layout the child elements.

Here's another example of a container with BorderImage elements.

[code]
ListView@ list = levelsWindow.GetChild("ListContainer", true);

if (list !is null)
{
    UIElement@ container = UIElement();
    container.layoutMode = LM_VERTICAL;
    container.layoutSpacing = 5;

    list.InsertItem(list.numItems, container);

    for (uint i = 0; i < 15; ++i)
    {
        BorderImage@ bimage = BorderImage();

        bimage.minHeight = 50;
        bimage.texture = null;
        bimage.color = Color(0.5f, 0.5f, 0.5f);

        container.AddChild(bimage);
    }
}
[/code]

-------------------------

