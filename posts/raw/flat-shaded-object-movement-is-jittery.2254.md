rku | 2017-01-02 01:14:17 UTC | #1

Picture worth a thousand words: [youtube.com/watch?v=t5uI_6J ... e=youtu.be](https://www.youtube.com/watch?v=t5uI_6JEswM&feature=youtu.be)
Notice that micro-shaking when object moves. This apparently is because object is flat-shaded. Is there any way to make it look smooth while keeping flat shading? If i set faces of object to be smooth-shaded then movement is also silky smooth, however shading effect is gone.

-------------------------

cadaver | 2017-01-02 01:14:17 UTC | #2

It's caused by triangle rasterization. Without antialiasing triangles have to fall on whole pixels, which may lead to 1-pixel jitter of their size when they move.

If the shading effect was a texture instead of geometry, then it would be interpolated/filtered across the object face and would appear less jittery.

-------------------------

rku | 2017-01-02 01:14:17 UTC | #3

[quote]shading effect was a texture instead of geometry[/quote]

What does this mean exactly? If you mean baking effect into texture then it is not ideal as it would not take into account lighting when rotating.

-------------------------

cadaver | 2017-01-02 01:14:18 UTC | #4

Yes, I mean baking.

For other solutions, you could try if antialiasing helps. Or determining the world unit distance of one pixel, and snapping all object positioning to that, so that you don't get sub-pixel rasterization artifacts. Otherwise than that, you can't really change how rasterization happens.

-------------------------

rku | 2017-01-02 01:14:23 UTC | #5

Thank you cadaver, snapping movement to pixel did the trick.

For the poor souls reading this in the future this is what i did:

First i set up orthographic camera size properly:
[code]_pixels_per_unit = round((float)graphics.GetHeight() / PLAY_FIELD_HEIGHT_UNITS);
camera_object->SetOrthoSize(graphics.GetHeight() / _pixels_per_unit);[/code]

And then setting position of object x y and z have to be snapped to pixels using this:
[code]inline float SnapToPixel(float x) { return round(x * _pixels_per_unit) / _pixels_per_unit; }[/code]

-------------------------

