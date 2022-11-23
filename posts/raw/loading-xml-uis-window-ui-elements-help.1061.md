vivienneanthony | 2017-01-02 01:05:08 UTC | #1

Hi

Have anyone tried loading a UI into a scene with Window UIElements? I tried to in the past pre-1.40 and Urho couldn't do it. So, I removed the Window elements because it was being assigned correctly display wise.

I'm starting to load UI  interfaces like configuration,   player info,  panels. I just want to create the interfaces in the editor and load them in the code with the right actions after... I am not sure how it's going be all managed specifically the events.

Vivienne

The  latest test of 

[code]<?xml version="1.0"?>
<element>
	<attribute name="Name" value="PlayerWindowUIElement" />
	<attribute name="Size" value="600 460" />
	<attribute name="Is Enabled" value="true" />
	<element type="Window">
		<attribute name="Name" value="PlayerWindow" />
		<attribute name="Size" value="600 460" />
		<attribute name="Opacity" value="0.9" />
		<attribute name="Use Derived Opacity" value="false" />
		<attribute name="Blend Mode" value="add" />
		<attribute name="Is Movable" value="true" />
		<attribute name="Is Resizable" value="true" />
		<element type="Window">
			<attribute name="Name" value="PlayerWindowMenuArea" />
			<attribute name="Position" value="16 3" />
			<attribute name="Size" value="500 32" />
			<element type="Button">
				<attribute name="Size" value="32 32" />
			</element>
			<element type="Button">
				<attribute name="Position" value="48 0" />
				<attribute name="Size" value="32 32" />
			</element>
		</element>
		<element type="Window">
			<attribute name="Name" value="PlayerWindowContext" />
			<attribute name="Position" value="16 56" />
			<attribute name="Size" value="568 400" />
		</element>
	</element>
	<element>
		<attribute name="Name" value="CloseButtonUIElement" />
		<attribute name="Position" value="566 18" />
		<attribute name="Is Enabled" value="true" />
		<element type="Button">
			<attribute name="Name" value="closeButton" />
			<attribute name="Blend Mode" value="add" />
		</element>
	</element>
</element>[/code]

Gave me attribute errors specifically the stuff relating to window resize and sizing.

-------------------------

weitjong | 2017-01-02 01:05:09 UTC | #2

I don't think at the moment you can create nested Window UI-element in the manner you have constructed. The only nested Window UI-element that actually works that I know of is only when it is being nested in a DropDownList UI-element. Although in theory you can nest any UI-element inside another UI-element, in practice I believe you only need one top level Window UI-element as the container of all your UI-elements which can be nested in any way you like.

-------------------------

vivienneanthony | 2017-01-02 01:05:10 UTC | #3

[quote="weitjong"]I don't think at the moment you can create nested Window UI-element in the manner you have constructed. The only nested Window UI-element that actually works that I know of is only when it is being nested in a DropDownList UI-element. Although in theory you can nest any UI-element inside another UI-element, in practice I believe you only need one top level Window UI-element as the container of all your UI-elements which can be nested in any way you like.[/quote]

So, what do I do if I want a multi-layer window like. Just a example.

[web.ccpgamescdn.com/communityass ... Larger.jpg](http://web.ccpgamescdn.com/communityassets/img/releases/rhea/New_UI_1_Larger.jpg)


Vivienne

-------------------------

weitjong | 2017-01-02 01:05:10 UTC | #4

You can have a look at how the Editor's attribute inspector window or the material editor window are being constructed. Basically, it is a single Window UI-element containing multiple "panels" or "panes" or whatever you want to call them. The panel itself is an UI-element which is being used as container to further nest more child UI-elements. In your example, you can construct a left panel and a right panel first then subdivide the panel with even more panels before ""filling" the subpanels accordingly with other nested UI-elements (divide et impera). You can control whether the panels should be layered out horizontally or vertically (See LayoutMode). If you look at the UI subsystem class diagram ([urho3d.github.io/documentation/1 ... ph_org.svg](http://urho3d.github.io/documentation/1.4/class_urho3_d_1_1_u_i_element__inherit__graph_org.svg)), you may think that only the concrete descendant classes of UIElement are usable in the UI layout construction. However, actually the base UIElement class itself is an invaluable class in constructing complex UI layout. I usually think of it as a generic "container". This is how the the "panels" in our Editor are being implemented by the way. I am sorry I can only give you this pointer instead of providing the actual UI layout XML file.

-------------------------

vivienneanthony | 2017-01-02 01:05:10 UTC | #5

It's fine. The way I'm thinking of it is basicaly some of UI class keeping tabs or names of each panel/window/UIElement whatever you call it. Keeping track of that info so each individually one can be enabled or disabled if need be..

-------------------------

vivienneanthony | 2017-01-02 01:05:11 UTC | #6

[quote="weitjong"]You can have a look at how the Editor's attribute inspector window or the material editor window are being constructed. Basically, it is a single Window UI-element containing multiple "panels" or "panes" or whatever you want to call them. The panel itself is an UI-element which is being used as container to further nest more child UI-elements. In your example, you can construct a left panel and a right panel first then subdivide the panel with even more panels before ""filling" the subpanels accordingly with other nested UI-elements (divide et impera). You can control whether the panels should be layered out horizontally or vertically (See LayoutMode). If you look at the UI subsystem class diagram ([urho3d.github.io/documentation/1 ... ph_org.svg](http://urho3d.github.io/documentation/1.4/class_urho3_d_1_1_u_i_element__inherit__graph_org.svg)), you may think that only the concrete descendant classes of UIElement are usable in the UI layout construction. However, actually the base UIElement class itself is an invaluable class in constructing complex UI layout. I usually think of it as a generic "container". This is how the the "panels" in our Editor are being implemented by the way. I am sorry I can only give you this pointer instead of providing the actual UI layout XML file.[/quote]

I tried something like this. I just can't get a border to show or the close button.

[code]<?xml version="1.0"?>
<element>
	<attribute name="Name" value="PlayerWindowUIElement" />
	<attribute name="Size" value="640 400" />
	<attribute name="Opacity" value="0.5" />
	<attribute name="Is Enabled" value="true" />
	<attribute name="Focus Mode" value="Focusable" />
	<element type="Window">
		<attribute name="Size" value="640 400" />
		<attribute name="Bring To Front" value="false" />
		<attribute name="Texture" value="Texture2D;Textures/Buttons/darkgrey.png" />
		<attribute name="Is Movable" value="true" />
		<attribute name="Is Resizable" value="true" />
		<element>
			<attribute name="Name" value="CloseButtonUIElement" />
			<attribute name="Position" value="16 16" />
			<attribute name="Size" value="16 16" />
			<attribute name="Is Enabled" value="true" />
			<attribute name="Bring To Front" value="true" />
			<attribute name="Bring To Back" value="false" />
			<element type="Button" style="CloseButton">
				<attribute name="Name" value="closeButton" />
				<attribute name="Bring To Front" value="true" />
				<attribute name="Bring To Back" value="false" />
				<attribute name="Focus Mode" value="Focusable" />
			</element>
		</element>
	</element>
</element>[/code]

and

[code]<?xml version="1.0"?>
<element>
	<attribute name="Name" value="PlayerWindowUIElement" />
	<attribute name="Size" value="640 400" />
	<attribute name="Opacity" value="0.5" />
	<attribute name="Is Enabled" value="true" />
	<attribute name="Bring To Front" value="true" />
	<attribute name="Focus Mode" value="Focusable" />
	<element type="Window">
		<attribute name="Position" value="0 0" />
		<attribute name="Size" value="640 400" />
		<attribute name="Texture" value="Texture2D;Textures/Buttons/darkgrey.png" />
		<attribute name="Is Movable" value="true" />
		<attribute name="Is Resizable" value="true" />
		<element type="Button" style="CloseButton">
			<attribute name="Name" value="closeButton" />
			<attribute name="Focus Mode" value="Focusable" />
		</element>
		<element type="Text">
			<attribute name="Position" value="100 100" />
			<attribute name="Top Left Color" value="0.85 0.85 0.85 1" />
			<attribute name="Top Right Color" value="0.85 0.85 0.85 1" />
			<attribute name="Bottom Left Color" value="0.85 0.85 0.85 1" />
			<attribute name="Bottom Right Color" value="0.85 0.85 0.85 1" />
			<attribute name="Is Enabled" value="true" />
			<attribute name="Text" value="testing" />
		</element>
	</element>
</element>[/code]
So, for example hitting F10 loads this specific panel.  The panel is stored so if F10 is hit again and that specific UIElement panel exist. It's not created again.

Along those lines.

-------------------------

Mike | 2017-01-02 01:05:12 UTC | #7

Sometimes it's good to have nested Windows to cleanly layout your UIElements.

-------------------------

vivienneanthony | 2017-01-02 01:05:12 UTC | #8

[quote="Mike"]Sometimes it's good to have nested Windows to cleanly layout your UIElements.[/quote]

I would like that also but maybe in the future.

Im just not sure why the closebutton or text appear from the latter xml. I think it matches the layout format of the editor window/panel.

-------------------------

