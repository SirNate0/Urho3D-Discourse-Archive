TikariSakari | 2017-01-02 01:08:37 UTC | #1

I spent this weekend coding on something to draw 3d images, minecraft like.

I do admit that the code itself is terrible and does very little optimizations. Despite it lacks just about everything, I still decided to share the small ugly uncommented code.

[url]https://www.dropbox.com/s/3y3i2bjhovrw3zf/Blockers.cpp?dl=0[/url]
[url]https://www.dropbox.com/s/o20kistka3bkjh2/Blockers.h?dl=0[/url]

white.xml
[code]
<material>
    <technique name="Techniques/NoTexture.xml" />
    <parameter name="MatDiffColor" value="1 1 1 1" />
</material>
[/code]

textured.xml
[code]
<material>
    <technique name="Techniques/Diff.xml" />
</material>
[/code]
Here is some pictures:

14.12.15 [url]http://i.imgur.com/xJEeCWe.png[/url]
27.12.15 [url]http://i.imgur.com/b28a1yq.png[/url]
07.01.16 [url]https://i.imgur.com/WbyDw6v.jpg[/url]

F5 shows some button instructions.

Edit: 27.12.2015 
- added skeletal structures, still missing animations.
- Some minor optimizations of removing missing faces, if there is another face next to it.

5.1.2016
- updated mostly animation things, like ability to add/remove animations

- Still lacking the ability to actually save animations.

7.1.2016
- Animation saving
- Changed the texture to make the blocks have darker edges, so they are much more visible.
- Squashed quite some bugs.

10.1.2016
- Added file-menu
- Added button to try different textures.
- Fixed a bug when the drawing canvas is moved, it was drawing cubes on wrong place.

-------------------------

Kyle00 | 2017-01-02 01:08:44 UTC | #2

this implementation is pretty cool. it reminds me of 3d texts but with boxes

-------------------------

