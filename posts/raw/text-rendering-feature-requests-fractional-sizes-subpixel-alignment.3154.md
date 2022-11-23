iainmerrick | 2017-05-24 17:03:59 UTC | #1

Hi all, I recently started working with Urho on a new project, and I'm trying to figure out how to get the highest quality text rendering. It seems like both Text and Text3D have some issues:

* Text3D gives fuzzier output because it's not pixel-aligned. It also seems like it doesn't use mipmaps, so a large font shown at a small size has aliasing artifacts, regardless of the texture filtering mode.

* Text is pixel-perfect, which is good except at small font sizes, where the pixel alignment leads to ugly uneven character spacing. And it doesn't support fractional font sizes, so you can't arbitrarily scale the UI the way you can with Text3D.

* I haven't tried SDF fonts, but from looking at the demos, I don't think the quality is high enough for my purposes.

I'm interested in the best possible text output, and I don't need text to be positioned arbitrarily in 3D space, so it seems like Text is closest to what I want. And I think a few small tweaks could improve it a lot!

* Allow fractional font sizes -- it looks like FreeType supports 1/64th pixel increments.
* Use subpixel character advances, maybe 1/4 pixel increments.
* Maybe use LCD-optimized subpixel rendering (again, FreeType already supports that). But that's fiddly on phones, which often have funky LCD layouts and are used in both orientations.

I'd like to try implementing these, but I'd appreciate some feedback first. I went ahead and filed a couple of issues on GitHub before I found this forum:

https://github.com/urho3d/Urho3D/issues/1952
https://github.com/urho3d/Urho3D/issues/1953

Happy to discuss either here or there!

I'm using the C# wrapper, which has a pretty complicated build process, so I'd need to get this stuff into the Urho master branch and from there into an official build of the C# wrapper -- I can't easily just hack the C++ for my own project.

-------------------------

iainmerrick | 2017-05-24 17:13:15 UTC | #2

Here's an old article that describes a great approach to font rasterization:

http://www.antigrain.com/research/font_rasterization/

Basically, hint and align the text vertically, but use anti-aliasing and subpixel alignment horizontally. I think this is mostly a matter of setting the right configuration options in FreeType.

-------------------------

