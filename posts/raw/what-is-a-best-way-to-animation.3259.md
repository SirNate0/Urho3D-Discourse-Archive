halcyonx | 2017-06-19 09:40:01 UTC | #1

Hi, everyone! 33_Urho2DSpriterAnimation sample with folder of **imp** animation sized ~0.5mb, I packed separated images by SpritePacker to image atlas, now in sized 180kb, but it is large for this simply animation! I converted atlas image to webp format and its sized just 50kb! But there is a problem - Urho does not support webp. Size has matter for mobile platforms, I think webp is good format for this. But I'm new in Urho. May be there is a way to make good little sized?

-------------------------

jmiller | 2017-06-19 03:26:53 UTC | #2

Hi halcyonx,

Urho supports lossless PNG, which may be the best current alternative. Size with [url=http://www.advsys.net/ken/utils.htm]pngout[/url] or similar utility is not much larger than webp, with slower de/compression.

Of course we are also welcome to contribute support for other formats.
One library I would consider, BSD-licensed: https://sites.google.com/site/openimageio/home

-------------------------

