Pellucas | 2017-01-02 01:13:29 UTC | #1

Hi guys. Is it possible to create an Image/Texture2D from a file with an indexed color palette? I mean, I already have the file(with the palette included) and I want to create an Image or Texture2D object by loading that file.

In case it is not possible, how would you do it for your U3D project?

Thanks in advance.

-------------------------

cadaver | 2017-01-02 01:13:29 UTC | #2

In general we don't go out of our way to support palettized images or textures since those formats are deprecated from the GPU's perspective and require a conversion on load. If it's not a format that the stb_image library will load directly (like indexed color .gif) then you can resort to manually setting an Image's size and then filling the data yourself, see Image's SetSize() and SetData() or GetData() functions. After that you can use the Image to populate a Texture2D.

-------------------------

Pellucas | 2017-01-02 01:13:29 UTC | #3

ok, I solved it by using [b]Image::SetSize()[/b] and [b]Image::SetPixel()[/b], but, one more question: what does it mean the parameter "depth" in the function Image::SetSize? bits per pixel or bits per channel?

-------------------------

cadaver | 2017-01-02 01:13:30 UTC | #4

It is depth dimension for 3D images. Actual bitdepth is always 8bit for now. You can use the version Image::SetSize(int width, int height, unsigned components) for standard 2D images.

-------------------------

Pellucas | 2017-01-02 01:13:30 UTC | #5

Thanks again, Cadaver.

-------------------------

