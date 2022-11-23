GoldenThumbs | 2019-08-22 00:33:47 UTC | #1

I've been considering my options for mapping in Urho3D for a while, my best options are either use an existing software, such as blender, and make maps in that. Maybe make a custom exporter to make the mapping pipeline a bit easier. The other option is to make a custom mapping solution from scratch based in and/or centered around Urho3D. Which one would you find more useful?
Poll: https://www.strawpoll.me/18518368

-------------------------

suppagam | 2019-08-22 02:58:38 UTC | #2

Blender, definitely. You have so much freedom. You could also use something like http://www.doombuilder.com/ or https://kristianduske.com/trenchbroom/ and then export an OBJ.

-------------------------

Modanung | 2019-08-22 08:48:00 UTC | #3

It really depends on the type of game and the associated maps that you are making. You may even want to *create* an editor that understands your game and your game only. If you're working alone it might not even require a graphical interface, you'd just memorize keycuts.
Highways are useful because of their limitations. It's what differentiates them from parking lots.

-------------------------

Modanung | 2019-08-22 09:00:11 UTC | #4

Because a game map is more then a collection of 3D models, it helps if your editor is built around Urho3D. As such it will be familiar with the available components - which could include your own - and using Urho's render pipeline will make it WYSIWYG.

-------------------------

