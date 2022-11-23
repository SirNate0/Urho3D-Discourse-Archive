codingmonkey | 2017-01-02 01:08:08 UTC | #1

hi
I try to add vertex paint ability with separated channels to exporter:
the Vcol channels are stored one of colors:
R - store red
G - store green
B - store blue
A - alpha
and when model going to export this channels are joined into one final color.
But before this action, this abbility just gives you very handy to tweak each channel in personal manner.
And thing is - what I have a problem with this. I have strange bug with it.
look at this original channels:
[url=http://savepic.su/6530482.htm][img]http://savepic.su/6530482m.png[/img][/url]

and that I got after export:
[url=http://savepic.su/6522290.htm][img]http://savepic.su/6522290m.png[/img][/url]

it is almoust the same but this green quad(on top) it's everywhere on cube. but actually it must be placed on top's center of this white cube.
this is my changes that I done :https://github.com/MonkeyFirst/Urho3D-Blender/commit/a5fafd816b79f56e3596e6f01ee167f791ad6af3

this ability of exporter in future allows to me doing such things: [http.developer.nvidia.com/GPUGem ... _ch16.html](http://http.developer.nvidia.com/GPUGems3/gpugems3_ch16.html)
[quote]
Artists paint one RGB color per-vertex, using a common 3D modeling software. This color gives us extra information about the detail bending. As shown in Figure 16-2, the red channel is used for the stiffness of leaves' edges, the green channel for per-leaf phase variation, and the blue channel for the overall stiffness of the leaves.
[/quote]

-------------------------

Modanung | 2017-01-02 01:08:17 UTC | #2

Try splitting the edges of the green square before exporting.
Either mark them as sharp and add an edge split modifier OR select the edges, hit space and search for "Edge Split".

-------------------------

codingmonkey | 2017-01-02 01:08:17 UTC | #3

>Try splitting the edges of the green square before exporting.
Thanks, but this is no working in this case.

I think, after some new fixes it's working properly.
this branch: [github.com/MonkeyFirst/Urho3D-B ... exPaint4Ch](https://github.com/MonkeyFirst/Urho3D-Blender/tree/VertexPaint4Ch)
[video]https://www.youtube.com/watch?v=FvMtFGLXoaU[/video]

-------------------------

Modanung | 2017-01-02 01:08:18 UTC | #4

Tried it; works fine here too. Pretty cool!  :slight_smile:

-------------------------

