vivienneanthony | 2017-01-02 01:00:00 UTC | #1

Hello

How do you use spot lights? I tried it and it doesn't seem to work or configured right.

Directional and sun light work but not spot so I am thinking I am setting something wrong.

[sourceforge.net/projects/proteu ... creenshot/](https://sourceforge.net/projects/proteusgameengine/files/Existence/screenshot/)

It's the top screenshoot.

Vivienne

-------------------------

friesencr | 2017-01-02 01:00:00 UTC | #2

The spot lights light a direction by a radius and length by alpha map and attenuation.  The billboards example has a working spotlight.

-------------------------

vivienneanthony | 2017-01-02 01:00:01 UTC | #3

[quote="friesencr"]The spot lights light a direction by a radius and length by alpha map and attenuation.  The billboards example has a working spotlight.[/quote]

Ok. I will look.

A left a message of how to intergrate perlin noise heght map in a thread. I'm not sure if the method is correct but it seems like it. I am judt confused about what exactly is depth and components.

-------------------------

friesencr | 2017-01-02 01:00:01 UTC | #4

I believe the components represents how many 8bit color channels are present.  rgba is 4.

-------------------------

vivienneanthony | 2017-01-02 01:00:01 UTC | #5

[quote="friesencr"]I believe the components represents how many 8bit color channels are present.  rgba is 4.[/quote]

Yup. It is. I think depth deals with the compression level or any numerous of things depending on the image type. For the code purposes, depth is 1 because the noise is not compressed etc.

-------------------------

cadaver | 2017-01-02 01:00:02 UTC | #6

Depth is for 3D images (to be loaded to the GPU as 3D textures). A normal 2D image would have depth 1.

-------------------------

