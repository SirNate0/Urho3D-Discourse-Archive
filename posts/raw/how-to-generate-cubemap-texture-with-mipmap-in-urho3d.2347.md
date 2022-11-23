dwlcj | 2017-01-02 01:14:53 UTC | #1

in urho3d i use this code to generate cubemap texture,but cant generate mipmap,help me.

[code]SharedPtr<TextureCube> texCube(new TextureCube(context_));
texCube->SetNumLevels(9);
texCube->SetSize(size, Graphics::GetRGBAFloat32Format(), TEXTURE_RENDERTARGET);
texCube->SetFilterMode(FILTER_ANISOTROPIC);
//texCube->SetFilterMode(FILTER_BILINEAR);
//texCube->SetAddressMode(COORD_U, ADDRESS_CLAMP);
//texCube->SetAddressMode(COORD_V, ADDRESS_CLAMP);
//texCube->SetAddressMode(COORD_W, ADDRESS_CLAMP);
GetSubsystem<ResourceCache>()->AddManualResource(texCube);[/code]

-------------------------

cadaver | 2017-01-02 01:14:53 UTC | #2

Mipmaps are not (at least at the moment) supported for rendertargets, since the assumption is that if something is a rendertarget, you'd render to it every frame, and regenerating mipmaps every frame would be costly.

If you only need to render once, you could get around this by creating the rendertarget cubemap, rendering to it once, reading the data from it, then create another cubemap that isn't a rendertarget, get the data from RT, calculate mips, set each mip of non-RT cubemap. You could delete the rendertarget cubemap after you're done.

This could be revised to optionally allow mips in rendertargets, but the default for e.g. the screen buffers allocated by RenderPath would be no mips.

-------------------------

dwlcj | 2017-01-02 01:14:54 UTC | #3

cadaver:Thank you very much. I've tried it.

-------------------------

cadaver | 2017-01-02 01:14:55 UTC | #4

Proper mipmapped rendertarget support is now in the master branch. Rendertarget textures that you create behave now like regular textures, ie. by default they have mips down to 1x1, use SetNumLevels(1) to disable.

However screen buffers allocated by Renderer, as well as shadow maps are not mipmapped, as it's assumed that they will be sampled in the highest precision (ie. to achieve a screenspace effect) and to not waste performance in mip generation.

-------------------------

dwlcj | 2017-01-02 01:14:55 UTC | #5

cadaver:At present, I have used your method to get minmaps in Rendertarget.
thanks,urho3d!

-------------------------

