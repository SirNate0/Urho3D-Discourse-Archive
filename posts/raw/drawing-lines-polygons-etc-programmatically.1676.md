bmcorser | 2017-01-02 01:09:27 UTC | #1

Does Urho3D provide an API for drawing lines, polygons, circles, etc?

I would like to let the user click to add a point, and draw lines between the points the user added. There is example code for GetMousePosition etc, but can't find anything in the samples that shows drawing programmatically.

-------------------------

rasteron | 2017-01-02 01:09:27 UTC | #2

Yes it does. :slight_smile:

[urho3d.github.io/documentation/1 ... derer.html](http://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_debug_renderer.html)

-------------------------

bmcorser | 2017-01-02 01:09:27 UTC | #3

Ah! I did see that, but thought "oh that's just for debugging".

Are you suggesting that I use the DebugRenderer API directly for my game? (or should I use it as inspiration for writing my own class?)

-------------------------

1vanK | 2017-01-02 01:09:27 UTC | #4

U can use DynamicGeometry or direct Graphics->Draw for any purposes

-------------------------

