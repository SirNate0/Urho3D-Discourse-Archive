Pencheff | 2019-02-28 19:09:57 UTC | #1

This is what I notice so far, experiment is done with both Text3D and RichText3D components, both work similar when rendering text.
![edges|690x388](upload://iJWYhdlU4yNW4yMsTLao5Q0pv8q.jpeg) 
![screenshot0167|690x388](upload://vKeHR8l8JYe57cuxMhwO9Q5jGxw.jpeg) 
The second screenshot shows the problem a bit more - the glyphs are cut off on the edges, very noticeable on the small letter "e".

-------------------------

lezak | 2019-02-28 22:21:27 UTC | #2

You should use signed distance field fonts (ones with .sdf extension in Data/Fonts folder). For reference see sample 35.

-------------------------

Pencheff | 2019-02-28 23:20:01 UTC | #3

I need to use TrueType fonts for my project...

-------------------------

I3DB | 2019-03-01 02:21:04 UTC | #4

[quote="lezak, post:2, topic:4980"]
For reference see sample 35.
[/quote]

[Fonts aren't showing up in the sample.](https://urho3d.github.io/samples/Urho3DPlayer.html?LuaScripts/35_SignedDistanceFieldText.lua)

-------------------------

