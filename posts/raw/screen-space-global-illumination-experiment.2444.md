artgolf1000 | 2017-01-02 01:15:25 UTC | #1

Hi,

I have put it on Github, it can run on mobile devices now, enjoy it!

[url]https://github.com/meshonline/Screen-Space-Global-Illumination[/url]

[img]http://www.mesh-online.net/ssgi800x600.jpg[/img]

-------------------------

sabotage3d | 2017-01-02 01:15:25 UTC | #2

Nice! Do you have video?

-------------------------

Lumak | 2017-01-02 01:15:26 UTC | #3

Is it only the floor lighting? That's the only difference that I see between SSGI and ORIGIN pics.  Maybe I'm just blind.

Edit: well now that you've replaced your original screenshots, my previous comment is kind of moot.

-------------------------

codingmonkey | 2017-01-02 02:11:19 UTC | #4

Nice feature! 
But I guess it's broken because in Editor's viewport it's not working properly
I even try to increase among of GI by commenting line : //gi /= float(GRID_COUNT * GRID_COUNT);

[url=http://savepic.net/8687260.htm][img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/6ab3bbe397e68bd6257c4e1424ad2197c217bc99.png[/img][/url]

-------------------------

sabotage3d | 2017-01-02 01:15:39 UTC | #5

Roughly what FPS can you achieve on mobile with this technique?

-------------------------

artgolf1000 | 2017-01-02 01:15:40 UTC | #6

It does not support Editor at present, since the render path is special.

To get best result, please set FarClip to smaller value, and only set material of 'DiffCull.xml' to front objects.

I just tested the performance, Running in Xcode, 60 FPS on my iPad Mini Retina in debug mode.

The video is recorded from my iPad Mini Retina:
[youtu.be/M9cXRAHMhXY](https://youtu.be/M9cXRAHMhXY)
[video]https://youtu.be/M9cXRAHMhXY[/video]

-------------------------

