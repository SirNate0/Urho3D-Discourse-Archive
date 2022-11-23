desolator | 2017-01-02 01:09:15 UTC | #1

Hello everyone!
Can i in Urho3D use spritebatch drawing on texture or on a sprite?
I need draw some geometrics on layers with alphablending. Maybe Urho3D have some another methods to do this ? Thanks a lot.

-------------------------

1vanK | 2017-01-02 01:09:15 UTC | #2

See 10_RenderToTexture example

-------------------------

desolator | 2017-01-02 01:09:15 UTC | #3

Thanx a lot. A saw that example, but i havn't any idea how to draw lines jn surface of texture for example. 
I'm try to found some examples in documentation, but didn't found, maybe i was looking bad, i don't know.

-------------------------

TikariSakari | 2017-01-02 01:09:15 UTC | #4

Probably not something you wanna see, since the code is very horrible to look at and there are about 4000 lines of it, but I used sprite to draw on for trying to create voxel character creator. It is still quite a work in a progress thing, but basically you can create image and then just use x,y coordinates on the image to set the color value. Then when done on drawing the image just use setdata-function from texture to transfer the data from image to texture. The bad side doing this way is, that if you lose context, you have to recreate the textures. Also you need to figure out what kind of filter you wanna use for the texture.

To draw lines on the image, you should probably look normal line drawing algorithms such as Bresenham's line algorithm: [url]https://en.wikipedia.org/wiki/Bresenham's_line_algorithm[/url] 

The terrible code I wrote, which I mentioned residents at:
[url]http://discourse.urho3d.io/t/painting-3d-thingies/1577/1[/url]

-------------------------

desolator | 2017-01-02 01:09:15 UTC | #5

Wow, it's too colmplicated method.
I hoped to see method similar to [b]Graphics.SpriteBatch()[/b] like in Mono.
BTW thanks a lot. Thread closed.

-------------------------

1vanK | 2017-01-02 01:09:15 UTC | #6

[quote="desolator"]Wow, it's too colmplicated method.
I hoped to see method similar to [b]Graphics.SpriteBatch()[/b] like in Mono.
BTW thanks a lot. Thread closed.[/quote]

[topic596.html](http://discourse.urho3d.io/t/spritebatch-beta-same-like-in-xna-or-d3dxsprite/591/1)

-------------------------

desolator | 2017-01-02 01:09:15 UTC | #7

[quote="1vanK"][quote="desolator"]Wow, it's too colmplicated method.
I hoped to see method similar to [b]Graphics.SpriteBatch()[/b] like in Mono.
BTW thanks a lot. Thread closed.[/quote]

[topic596.html](http://discourse.urho3d.io/t/spritebatch-beta-same-like-in-xna-or-d3dxsprite/591/1)[/quote]

Yes, i saw this topic. Trying to find realisation in C# in UrhoSharp. I use C# importer port of Urho3D.
Thanks again.

-------------------------

