QBkGames | 2018-12-28 03:20:42 UTC | #1

I'm trying to show a crosshair in the middle of the screen.
I'm using a modified version of the default Urho UI.png:
![EscapeUI|256x256](upload://mMJnSx7Yi1BasO2gouLnFml2q2u.png) 

And this is the XML block that's creating the crosshair:
>      <element type="BorderImage">
> 		<attribute name="Name" value="CrossHair" />
> 		<attribute name="Position" value="0 0" />
> 		<attribute name="Size" value="32 32" />
> 		<attribute name="Max Size" value="32 32" />
> 		<attribute name="Horiz Alignment" value="Center" />
> 		<attribute name="Image Rect" value="200, 128, 232, 160" />
> 	   </element>

After hours of searching on forums, in the documentation, etc, I still cannot figure out why Urho is showing me this (instead of the crosshair):
![CrossHair%20Issue|690x388](upload://hdWI35MaHt4VvYoRocYYelB1rz8.jpeg) 

It looks like Y coordinates of the Image Rect is totally ignored and set to 0.
Any assistance is appreciated.

-------------------------

Dave82 | 2018-12-27 01:05:28 UTC | #2

[quote="QBkGames, post:1, topic:4777"]
&lt;attribute name="Image Rect" value="200, 128, 232, 160" /&gt;
[/quote]

Try removing the commas.

-------------------------

QBkGames | 2018-12-27 03:37:04 UTC | #3

Thanks mate.
I never saw that coming. That will teach me to mess around with xml files manually and not use the editor :stuck_out_tongue:.

-------------------------

