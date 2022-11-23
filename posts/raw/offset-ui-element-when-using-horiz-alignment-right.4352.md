arpo | 2018-06-26 08:03:53 UTC | #1

Im adding a arrow to a dropdown element. It's positioned to the right of it's parent container. But I want to offset it some pixels to the left. How do I do this? I tried border but without luck. 

![27|231x87](upload://mUmngbMQZlYceAQMLlxuLXfPQgw.png)

Here's my XML

    <element type="DropDownList" style="dropDownWrapper">
		<attribute name="Name" value="ModelPreview" />
		<element type="BorderImage">
			<attribute name="Image Rect" value="194 3 206 11" />
			<attribute name="Min Size" value="12 8" />
			<attribute name="Max Size" value="12 8" />
			<attribute name="Horiz Alignment" value="Right" />
			<attribute name="Vert Alignment" value="Center" />
			<attribute name="Border" value="0 0 10 0" />
		</element>
		<element type="Window" internal="true" popup="true" style="none">
			<element type="ListView" internal="true" style="none">
				<element type="BorderImage" internal="true" style="none">
					<element internal="true" style="none">
						<element type="Text" style="dropDownOption">
							<attribute name="Text" value="Box" />
						</element>
					</element>
				</element>
			</element>
		</element>
	</element>

-------------------------

dev4fun | 2018-06-26 17:34:37 UTC | #2

If I remember just to change the Position. Btw I recommend you to use Urho editor instead of editing manually by xml. This way you will can see whats happening. :slight_smile:

-------------------------

arpo | 2018-06-27 08:43:53 UTC | #3

Changing position doesn't seem to work when you use:

	<attribute name="Horiz Alignment" value="Right" />

And since I want the arrow to always be aligned to the right no matter what the width of the dropdown is I ended up making the the Image Rect broader so that the right margin I wanter is included in the image. 

	<attribute name="Image Rect" value="144 3 164 16" />
	<attribute name="Min Size" value="20 13" />
	<attribute name="Max Size" value="20 13" />

-------------------------

