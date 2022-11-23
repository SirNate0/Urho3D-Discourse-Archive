Modanung | 2019-08-30 11:43:48 UTC | #1

Support for SVG images could also make the UI system more flexible considering scaling. I made the current default UI's theme entirely in Inkscape, but it is read from a PNG. Using the SVG directly could make the default UI more suitable for HDPI, for instance.
Compare:
![PNG|512x256](https://raw.githubusercontent.com/urho3d/Urho3D/master/bin/Data/Textures/UI.png)
...and...
![SVG|512x256](https://luckeyproductions.nl/images/UI.svg)

-------------------------

Miegamicis | 2019-08-30 10:35:29 UTC | #2

SVG basically means that the images would have to be generated on the fly, which I believe is a costly operation. But on the bright side, you would have specific resolution optimized images. Some POC of this would be great tho :slight_smile:

-------------------------

glitch-method | 2019-08-30 10:35:29 UTC | #3

dual support! png for 728- and svg for hdpi?

-------------------------

Modanung | 2019-08-30 10:52:35 UTC | #4

They could be stored; you'd only have to render them when the size of an element changes. Elements of the same size and style could share the rasterized image.

-------------------------

Leith | 2019-08-30 11:12:04 UTC | #5

I'd like to see the enture UI system move toward NDC, but thats just me. Scale that.

-------------------------

Modanung | 2019-08-30 11:12:51 UTC | #6

@Leith What do you mean by NDC?

-------------------------

Leith | 2019-08-30 11:13:57 UTC | #7

NDC coordinates are normalized device coordinates - 0 to 1

-------------------------

Leith | 2019-08-30 11:14:31 UTC | #8

works for any resolution

-------------------------

Leith | 2019-08-30 11:16:02 UTC | #9

we should never specify anything in pixel coords, we should translate image coords to ndc and vice versa

-------------------------

Modanung | 2019-08-30 11:49:56 UTC | #10

For crisp rendering of raster images you _do_ want pixel sizes and coordinates, but I agree it makes sense to have normalized coordinates at your disposal as well.
Maybe some convenience functions could be a start? Like:
```C++
Vector2    UIElement::toNormalizedScreenPos(IntVector2)
IntVector2 UIElement::toPixelCoordinates(Vector2)
float      UIElement::toNormalizedSize(int)
int        UIElement::toPixelSize(float)
```
These would take things into account like parent-child structures and window or screen size.

There's already:
```
IntVector2  UIElement::ScreenToElement(const IntVector2&)
IntVector2  UIElement::ElementToScreen(const IntVector2&);
```

-------------------------

Leith | 2019-08-30 11:26:54 UTC | #11

The conversion is generally simple enough, but it takes some thinking for pixel artists - still, done once, it works on any resolution.

-------------------------

suppagam | 2019-08-30 15:55:46 UTC | #12

Isn't having multiple sizes per platform a better approach? @2x.png, @4x.png, etc. That has the performance benefit. You can still have an SVG and just bake the bitmaps with appropriate sizes, which is what the engine reads. Efficiency first.

-------------------------

Modanung | 2019-08-30 15:58:58 UTC | #13

Maybe there could be an automated form of exactly that. You'd want to prevent anti-aliasing leaks anyway.

-------------------------

GoldenThumbs | 2019-08-31 04:37:41 UTC | #14

Most engine's I've worked with have the option to use both at the same time, why can't we.

-------------------------

Leith | 2019-08-31 12:53:54 UTC | #15

I'll consider writing up some utility methods to convert between NDC and pixel coords, but to change the entire UI system to use NDC as an option? I am optimistic, but I recognize that it's likely to be non-trivial.
Most things that are easy, are not worth doing. Some things that seem hard, are definitely worth the effort.

-------------------------

