halcyonx | 2017-06-14 19:19:44 UTC | #1

What kind of formats U3D supports? Can I load and show webp fromats or smth other as Sprite2D or as SpriterAnimation?

-------------------------

ppsychrite | 2017-06-14 21:37:00 UTC | #2

According to http://urho3d.wikia.com/wiki/Texture
Urho3D Supports .dds, .png, .jpg, .gif, .tga and .bmp
Not sure about webp.

-------------------------

S.L.C | 2017-06-15 09:22:01 UTC | #3

For reading, I'm pretty sure is whatever [stb_image](https://github.com/nothings/stb/blob/master/stb_image.h) supports and dds. And for writing, whatever [stb_image_write] (https://github.com/nothings/stb/blob/master/stb_image_write.h) supports plus jpeg with the [jo_jpeg](http://www.jonolick.com/uploads/7/9/2/1/7921194/jo_jpeg.cpp) libray.

-------------------------

halcyonx | 2017-06-15 11:57:31 UTC | #4

Unfortunately, png format has large size, webp has best compression, I tried convert all pngs to webp in U3D sample SpriterAnimation, run sample, but hero did not appear in window

-------------------------

