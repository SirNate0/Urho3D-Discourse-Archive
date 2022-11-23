1vanK | 2017-01-02 01:09:33 UTC | #1

Ultra big and ultra fast tiled worlds with 3D objects

[github.com/1vanK/Urho3DTerraria](https://github.com/1vanK/Urho3DTerraria)

Left mouse - deleting tiles
A, D - moving
W - jumping

[url=http://savepic.ru/8422789.htm][img]http://savepic.ru/8422789m.png[/img][/url]

It uses [topic596.html](http://discourse.urho3d.io/t/spritebatch-beta-same-like-in-xna-or-d3dxsprite/591/1) for drawing of the world

-------------------------

codingmonkey | 2017-01-02 01:09:33 UTC | #2

~4-5 Batch, nice )
and if we try to use more various textures blocks is still batches will be in low count ?

-------------------------

rasteron | 2017-01-02 01:09:33 UTC | #3

Looks good, this reminds me of Solomon's Key. :slight_smile:

-------------------------

1vanK | 2017-01-02 01:09:33 UTC | #4

[quote="codingmonkey"]~4-5 Batch, nice )
and if we try to use more various textures blocks is still batches will be in low count ?[/quote]

1) u can merge all tiles in one big texture (atlas)
2) drawed only visible on screen tiles, so that count of batches will be small in any case

-------------------------

Enhex | 2017-01-02 01:09:34 UTC | #5

Are you merging the tiles to an atlas in real time?

I'd imagine something like texture array would be handy in this case.

-------------------------

thebluefish | 2017-01-02 01:09:34 UTC | #6

Awesome work man!

-------------------------

