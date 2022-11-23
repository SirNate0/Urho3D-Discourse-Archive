arpo | 2018-06-29 07:59:23 UTC | #1

In my UI I want to mark a thumb nail, a button, as selected. I do this by adding  a BorderImage as a child of the thumb button. How can I make this BorderImage have a width and height of 100% of it's parent container? 

![40|484x196](upload://v8XDd5OuF8wVMO5YuBhjmiiIclk.png)

My code looks like this

	<element type="Button" style="gridButton">
			<attribute name="Name" value="BridgeWood1" />
			<attribute name="Texture" value="Texture2D;Textures/BridgeWood_DIFFUSE.256.jpg" />
			<element type="Text" style="gridButtonText">
					<attribute name="Text" value="Bridge Wood" />
			</element>
			<element type="BorderImage">
					<attribute name="Min Size" value="100 100" />
					<attribute name="Max Size" value="100 100" />
					<attribute name="Border" value="4 4 4 4" />
					<attribute name="Image Rect" value="32 64 48 80" />
					<attribute name="Texture" value="Texture2D;Textures/HiberUI.png" />
			</element>
	</element>

-------------------------

