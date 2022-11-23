rogerdv | 2017-01-02 01:01:35 UTC | #1

Im playing with terrain materials, but seems that I have some mistake somewhere. This is what I see if I enable Per Vertex, in the directional light:

[url=http://s249.photobucket.com/user/rogerdv/media/terrain-prob.jpg.html][img]http://i249.photobucket.com/albums/gg237/rogerdv/terrain-prob.jpg[/img][/url]

If I disable Per Vertex, then I just get colors, not textures: light green where there should be grass, brown in the rocky zones and gray in the floor area.

-------------------------

rogerdv | 2017-01-02 01:01:37 UTC | #2

I solved it manually editing the xml and removing everything, except the lines matching another in the original terrain sample  material file. Perhaps we need an specific Material Editor for terrain materials?

-------------------------

