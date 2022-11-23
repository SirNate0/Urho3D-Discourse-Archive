NiteLordz | 2017-01-02 01:14:23 UTC | #1

I'm playing around with the RenderToTexture sample, and trying to get it to display inside of a sprite, instead of the 3D object.  What can i do, to not show the 3D Box, but get the render texture.

right now, the sprite displays the render texture, but only if the box is displayed as well.

Thanks much

-------------------------

cadaver | 2017-01-02 01:14:23 UTC | #2

See RenderSurface::SetUpdateMode(). The default mode is tied to visibility in a 3D main (backbuffer) viewport. Your other options are to automatically update each frame, or queue each update manually.

-------------------------

