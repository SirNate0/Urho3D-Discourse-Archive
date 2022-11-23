Ray_Koopa | 2017-08-31 15:12:30 UTC | #1

Hey there,

I'm trying to create a UI which I'd optimally want to be loadable from XML completely, then just get UI children by name in code to attach them to events.

I'm missing some layouting feature. I know that layouts can be set to be horizontal, vertical or free.
When free, children require a specified size which they'll then have fixed.
When horizontal or vertical, all children divide up the total space of the parent amongst themselves so that each is of approx. equivalent size.

I need an option which only requires parents to become as big as their children require it. For example, a button should only be as large as it's Text content (and padding).
Can this only be done in code? I found a piece of code doing something similar in the Editor script (when it resizes the menu buttons), but it didn't work for me - the Text content was reported to be 0 size, so I couldn't scale the parent according to it.

Also, how do I find out the possible `attribute name` strings in XML files?

-------------------------

weitjong | 2017-09-01 09:10:05 UTC | #2

[quote="Ray_Koopa, post:1, topic:3518"]
I’m trying to create a UI which I’d optimally want to be loadable from XML completely, then just get UI children by name in code to attach them to events.
[/quote]

You can name each child and then use C++ API UIElement::GetChild(name) to get it back. This is just one of the way you can get the children back. Check the API documentation for the UIElement class (the base class of all the UI-elements).

[quote="Ray_Koopa, post:1, topic:3518"]
I’m missing some layouting feature. I know that layouts can be set to be horizontal, vertical or free.

When free, children require a specified size which they’ll then have fixed.

When horizontal or vertical, all children divide up the total space of the parent amongst themselves so that each is of approx. equivalent size.
[/quote]

I believe you got it slightly wrong here. As far as I remember, when layout mode is active then the parent UI-element will grow as big as its children required by default (which is what you want). It does not evenly divide the parent width/height equally to the number of children like you have described. For example, if you have vertical layout parent element without any child elements yet then the height of the parent element will be zero initially and the height will be adjusted automatically to accommodate its children as they are being added. When adding big number of children, you may want to disable this auto layout adjustment first and reenable it back after all the children have been added.

On the flip side, you may actually want to limit the parent size to grow to a certain max value, like in a list view. You don't want the view to become as long as the list items it contains. To achieve that you can use the "Max Size" attribute together with "Clip Children" attribute.

[quote="Ray_Koopa, post:1, topic:3518"]
Also, how do I find out the possible attribute name strings in XML files?
[/quote]

You can list and play around with these attributes using the provided Editor. Launch the Editor and use the "UI-layout" menu to open the UI-layout files for the Editor itself as sample. The attributes are listed in the Attribute Inspector when any UI element is being selected. Alternatively, just peek the code to see the attribute list or go to https://urho3d.github.io/documentation/HEAD/_attribute_list.html and scroll to UIElement class or any class you interested in.

-------------------------

Ray_Koopa | 2017-09-01 15:03:47 UTC | #3

Thanks for the detailed reply. I could start over with some correct knowledge in mind, but I still don't understand why the UI behaves like that in the following case:

I have the following code to create UI elements (using Urhosharp, but I guess Xamarin didn't change your internal logic, or did they?):

	UI.Root.SetDefaultStyle(ResourceCache.GetXmlFile("styles/default.xml"));
	
	BorderImage menuBar = new BorderImage();
	menuBar.SetStyle("MenuBar");
	menuBar.LayoutMode = LayoutMode.Horizontal;
	UI.Root.AddChild(menuBar);

	Button button = new Button();
	button.SetStyle("MenuButton");
	menuBar.AddChild(button);

The default.xml style looks as follows:

	<elements>
		<element type="BorderImage">
			<attribute name="Blend Mode" value="alpha" />
			<attribute name="Border" value="4 4 4 4" />
			<attribute name="Image Rect" value="0 0 16 16" />
			<attribute name="Texture" value="Texture2D;textures/ui.png" />
		</element>
		<element type="Button" style="BorderImage">
			<attribute name="Pressed Image Offset" value="32 0" />
			<attribute name="Hover Image Offset" value="16 0" />
			<attribute name="Min Size" value="40 40" />
		</element>
		<element type="MenuBar" style="BorderImage">
			<attribute name="Layout Mode" value="Horizontal" />
			<attribute name="Min Size" value="2147483647 0" />
		</element>
		<element type="MenuButton" style="Button" />
	</elements>

As you can see, I set the maximum possible width for the MinSize of the MenuBar. I did that to keep it fully stretched at the top of the window and not only take up the size the children require.

A button in that menu should be at least 40x40 pixels if it has no other content making it bigger.

However, with this, the button starts to take up the whole size of the MenuBar, basically becoming 2,147,483,647 pixels wide. Why is that? I thought it would only become as big as necessary (40 pixels here, as the minimum size requires).
This is the reason why I originally thought available space is divided up to the children.

-------------------------

lezak | 2017-09-01 16:54:54 UTC | #4

When it comes to layout, You have 2 options: 
1. When parent element has specified size and layout, children (without specified size) will be resized to fit parents space - like You said in first post;
2. When parent element doesn't have specified size and children have, parent will resize itself to the size of its children.

To prevent button from stretching You should specify it's max size, othervise it will be stretched to fit parents size. You can do it in code after adding children, so You can set MaxSize to fit children size.
Other solution to keep MenuBar always stretched at the top of the window, would be using anchors with min x set to 0 and max x to 1.

-------------------------

weitjong | 2017-09-02 02:32:01 UTC | #5

I have not used UrhoSharp on Xamarin, so I don't know the answer. However, one thing for sure, the default behavior of UIElement base class can be modified via the attributes. You could put other UIElement's derived classes as children in many nested level that form a hierarchy. So, what I just said in my earlier post applies recursively, when any of the child uses layout mode or when it inherent size is not fixed.

-------------------------

Ray_Koopa | 2017-09-03 15:42:34 UTC | #6

Thanks for the replies. After a lot of frustration mostly coming from expecting Urho3D to work like WPF or equivalents, I got some kind of menu working without any extra code, loaded purely from XML. I gave up on anchoring the menu to the top, as soon as I do like lezak suggested, it disappears completely including the contents, but that's fine as I think I can live without that.

-------------------------

