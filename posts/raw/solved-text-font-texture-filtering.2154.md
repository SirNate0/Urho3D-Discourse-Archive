Enhex | 2017-01-02 01:13:31 UTC | #1

Is there a way to set a fixed size Text3D or its font to render using FILTER_NEAREST, to avoid blur with some fonts that suppose to be pixel perfect?
SDF fonts could be used as a workaround?

-------------------------

cadaver | 2017-01-02 01:13:31 UTC | #2

If you don't want Text3D to change its screen size due to perspective, you can use SetFixedScreenSize() on it.

To access a font's textures for changing the filtering: first get the face of a certain size (Font::GetFace) then access the texture(s) with FontFace::GetTextures().

-------------------------

Enhex | 2017-01-02 01:13:31 UTC | #3

Thanks! FontFace was the missing piece.

-------------------------

