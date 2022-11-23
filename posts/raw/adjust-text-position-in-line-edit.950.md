godan | 2017-01-02 01:04:22 UTC | #1

I'm currently creating a little UI and I was wondering how to adjust the text position in the LineEdit element. The default places the user entered text too close to the boundary of the UIElement:
[img]https://dl.dropboxusercontent.com/u/69779082/Text_pos.PNG[/img]

Is there a way to adjust the borders of this element? Here is the XML that I'm using...

[code]
<element type="LineEdit">
			<attribute name="Name" value="CCFInput" />
			<attribute name="Min Size" value="74 24" />
			<attribute name="Max Size" value="2147483647 24" />	
			<attribute name="Layout Border" value="5 0 5 0" />
</element>
[/code]

-------------------------

cadaver | 2017-01-02 01:04:22 UTC | #2

It's slightly non-intuitive, you can adjust the line edit's Clip Border attribute (left + top values) to make it push the text right & downward.

-------------------------

godan | 2017-01-02 01:04:24 UTC | #3

Ah, that works great (would not have figured that out on my own). Thanks!

-------------------------

