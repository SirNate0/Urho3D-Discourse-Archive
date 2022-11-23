Bananaft | 2017-01-02 01:04:59 UTC | #1

So, here is my special testing textures. Heightmap and TexBlendingMap:
[img]http://i.imgur.com/RTrkqjw.png[/img] [img]http://i.imgur.com/2tewSk0.png[/img]

As you can see, they are coincidental. And I'm expecting to see one texture in the lowlands, and another on the hills.

But if i'm creating terrain in editor, using this two textures, here is how it comes out:
[url=http://i.imgur.com/Kosd92b.png][img]http://i.imgur.com/Kosd92bm.png[/img][/url]

Height map appears larger and cropped on two sides. It cropped by <Patch size>, and changing it will scale this effect.

And to make both textures match, I end up with adding 32 pixels to each side to my heightmap, making it 288x288 instead of 256x256. And that way Urho makes perfect 256x256 terrain:
[url=http://i.imgur.com/7XlSbfJ.png][img]http://i.imgur.com/7XlSbfJm.jpg[/img][/url]

Why terrain does that? Is it a bug?

-------------------------

cadaver | 2017-01-02 01:04:59 UTC | #2

Terrain heightmap needs an odd number of points so that the mipmapping works properly while the patch edges remain in place. For example 129 x 129, 257 x 257.

-------------------------

Bananaft | 2017-01-02 01:05:00 UTC | #3

Aaaah, of course! Thank you for clarifying that.

Aren't power of two +1 tex size not cool for memory usage? or that's true only for textures that used on GPU, and heightmap is not.

-------------------------

cadaver | 2017-01-02 01:05:00 UTC | #4

Heightmap itself does not get loaded to GPU by default (unless you use it in a material), so there the limitation doesn't matter. Otherwise it's true that power of two is preferred.

-------------------------

