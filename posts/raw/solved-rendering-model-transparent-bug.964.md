codingmonkey | 2017-01-02 01:04:28 UTC | #1

Hi folks :slight_smile:
I got the model from DW game, I guess. 
For testing rendering with transparent cloth. 
And there is have some problems.
Look at this short video, 
[video]http://www.youtube.com/watch?v=vmGZal9RMnU[/video]
There i'm trying to change tech one by one.
And it's seems, no one tech no working properly with this model.
and don't know maybe need to do some tweaks to tech in passes?

There is model for test.
[rghost.ru/8HRPRpyKr](http://rghost.ru/8HRPRpyKr)

-------------------------

friesencr | 2017-01-02 01:04:28 UTC | #2

The first thing I would try would be to try a png instead of tga.  Superstitious reasoning :neutral_face:

-------------------------

codingmonkey | 2017-01-02 01:04:29 UTC | #3

>The first thing I would try would be to try a png instead of tga
Why? the diffuse texture (Yuanji_d.tga) is 32 bit (RGBA) I mean it's also store alpha channel in your self.
I think that something wrong with Technique passes (DiffNormalSpecEmissiveAlpha.xml) or maybe with shader ? 
needed special shader for this?
This model works perfectly in other engines, look at this
[url=http://savepic.net/6592569.htm][img]http://savepic.net/6592569m.png[/img][/url]

-------------------------

Mike | 2017-01-02 01:04:29 UTC | #4

In Blender:
- Properties > Data: uncheck "Double Sided"
- Properties > Material: set "Transparency" to "Mask" instead of "Z"
For me it works perfectly.

-------------------------

codingmonkey | 2017-01-02 01:04:29 UTC | #5

how do you setup setting for exporter to export ?
how many part of model do you have in urho ? 
material count is still 2, one for body and one for dress ?
that tech are you using in material ?
any your screenshot from urho editor with this model ?

i'm try turn off double side and Z-transparent change to mask, and actually is they doing any affect to exported materials? I guess that not.
and yeah after this settings I'm still have the same problems with transparent dress in urho

-------------------------

Mike | 2017-01-02 01:04:29 UTC | #6

I didn't noticed that the dress was semi-transparent at first.
In this case:
- use a regular non-transparent material for everything except the dress (DiffNormal technique)
- use a "Z" transparency material for the dress only and adjust transparency to 0.5 for example (DiffNormalAlpha technique)
- you can disable "Double Sided" as the mesh is already "thick"

So for the main mesh you will have 2 materials, one non-transparent and one transparent.
You should end-up with:
[img]http://i.imgur.com/z0ffBXQ.png[/img]

-------------------------

codingmonkey | 2017-01-02 01:04:30 UTC | #7

Thanks, Mike )
[url=http://savepic.net/6583188.htm][img]http://savepic.net/6583188m.png[/img][/url]

>you can disable "Double Sided" as the mesh is already "thick"
They(DW) use a clone geometry everywhere for CCW and CW culling on alpha transparent objects such as hair or bottom part of dress, I guess.

Anyway, i'm just join all submeshes into one mesh, create 3 material (actually one mat is excess) 
1. hair - DiffNormalSpecAlphaTest, (I don't know why, but hair-tips on texture is semi-transparent i'm try to use DiffNormalSpecAlpha instead DiffNormalSpecAlphaTest but got a same transparent bug like before, mb need split hair into two pieces for CCW and CW culling)
2. body - DiffNormalSpecEmissive, 
3. dress - DiffNormalSpecEmissiveAlpha

and reassign they with this new.
[url=http://savepic.net/6578068.htm][img]http://savepic.net/6578068m.png[/img][/url]

-------------------------

