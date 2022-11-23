Sean221 | 2017-12-26 23:46:01 UTC | #1

I'm still very new to this and i was wondering how do you change UI elements such as the window and buttons to be my own texture

-------------------------

jmiller | 2017-12-27 04:21:38 UTC | #2

Check out [url=https://github.com/urho3d/Urho3D/blob/master/bin/Data/UI/DefaultStyle.xml]Data/UI/DefaultStyle.xml[/url] with text editor; it references Textures/UI.png.
The 'User interface' section goes into more detail:  https://urho3d.github.io/documentation/HEAD/_u_i.html

-------------------------

JTippetts | 2017-12-27 16:36:04 UTC | #3

If your UI texture doesn't align exactly with the default texture (size and placement of elements) then you'll need to edit the DefaultStyle.xml definitions to suit, or write a new style sheet for it that includes accurate image rectangles and suchlike.

-------------------------

