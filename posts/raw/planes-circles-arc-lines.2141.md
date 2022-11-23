Simce | 2017-01-02 01:13:26 UTC | #1

I?m just starting with Urho3D.
Working on 3D visualization of my 2D graphs.

On classic 2D plane, I used to draw simple shapes with commands for arcs, circles, lines etc. What is equivalent of creating models programmatically with Urho 3d Approach?
I don?t want to convert 2D pictures to 3D models with some kind of alpha mapping. 

Can you please how to start? Link to tutorial, or help file?

-------------------------

rku | 2017-01-02 01:13:26 UTC | #2

[quote="Simce"]I?m just starting with Urho3D.
What is equivalent of creating models programmatically with Urho 3d Approach?
[/quote]
Check out this sample: [url=https://github.com/urho3d/Urho3D/tree/master/Source/Samples/34_DynamicGeometry]34_DynamicGeometry[/url]

-------------------------

Simce | 2017-01-02 01:13:26 UTC | #3

Isn?t that just geometry from box.mdl?
Pyramid shape is from scratch, however, I need circles and arcs.
If it?s possible I would not like to create them manually from points.

-------------------------

Egorbo | 2017-01-02 01:13:26 UTC | #4

Take a look at this thread: [post3161.html#p3161](http://discourse.urho3d.io/t/solved-how-to-simple-graphing/559/2)

-------------------------

Simce | 2017-01-02 01:13:28 UTC | #5

Thank you.

I have decided to write everything from scratch.
It will take some time, and serious thinking about geometry, but it will be perfect fit.

-------------------------

godan | 2017-01-02 01:13:29 UTC | #6

Although it's not quite ready for the big time, check out Iogram -> [topic2173.html](http://discourse.urho3d.io/t/iogram-wip/2072/1). We've got a pretty good geometry core written in C++ and specifically for Urho. The plan is to open source the whole core library (geometry, graphs, nodes, other components, etc).

-------------------------

