jijingLiu | 2017-01-02 01:15:26 UTC | #1

Hi.
I update Urho3D to version 1.6 and  i found RenderToTexture have no effect on iOS .
How can i fix it?

-------------------------

cadaver | 2017-01-02 01:15:26 UTC | #2

I just tested and saw it myself too. Have to track the latest changes. Could be related to mipmap support. The RTT sample seems now funky even on desktops, as the aspect ratio of the texture is off, though it should be square (1024x768, and plane has scale 20x15)

-------------------------

cadaver | 2017-01-02 01:15:26 UTC | #3

Master branch has now rendertarget mipmaps automatically disabled on iOS, similarly to Emscripten. On Android they worked at least on my phone so left them on for now. You can also always do SetNumLevels(1) to a texture to explicitly disable mipmapping.

-------------------------

jijingLiu | 2017-01-02 01:15:27 UTC | #4

Thanks

-------------------------

