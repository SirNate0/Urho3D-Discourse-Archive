noMad1717 | 2017-01-02 01:12:00 UTC | #1

Hi, I'm trying to capture the screen on each frame update and I find that the first frame will always be a black picture when this is not expected.
The texture is created as such:
[code]
SharedPtr<Viewport> viewport(new Viewport(context, scene, camera);
tex = new Texture2D(context);
tex->SetSize(width, height, Graphics::GetRGBFormat(), TEXTURE_RENDERTARGET);
tex->GetRenderSurface()->SetViewport(0, viewport);
tex->GetRenderSurface()->SetUpdateMode(SURFACE_UPDATEALWAYS);
[/code]

Then I've subscribed to the EndFrame-event in which I try to fetch the data from my texture:
[code]
int len = tex->GetDataSize(width, height);
unsigned char* buf = new unsigned char[len];
tex->GetData(0, buf);
[/code]

I've been reading the documentation and some other topics on this forum that were slightly relevant and tried to make sure that the rendertarget is current by doing:
[code]
Graphics* graphics = GetSubsystem<Graphics>();
graphics->SetRenderTarget(0, tex);
graphics->SetViewport(IntRect(0, 0, width, height));
[/code]
both in the texture-creation-block and prior to any call to GetData() without success.

I've also tried using glReadPixels() but if I use my rendertarget-texture all I get is junk. 
If I try just using a Urho3D::Renderer instead of the texture I do indeed get what should be visible on my screen. 
However, the images are rotated 180 degrees and are mirrored.

I greatly appreciate any input. What am I missing here?

-------------------------

cadaver | 2017-01-02 01:12:00 UTC | #2

If you just need to capture the screen as it's shown (and don't actually require an extra texture rendertarget), you could use Graphics::TakeScreenShot(). On OpenGL this maps to using glReadPixels().

If you are already showing stuff on the screen (= have defined a viewport to Renderer) and you then setup an extra texture rendertarget, you'd be rendering your scene twice, which is probably not what you want.

Graphics::SetRenderTarget() / SetViewport() don't likely have the effect you want, as Renderer will be overwriting those anyway when it's doing its per-frame rendering. You'd only need to use those if you are using the Graphics class directly for rendering.

-------------------------

noMad1717 | 2017-01-02 01:12:00 UTC | #3

Thank you for your reply.

I fear that I may have been a bit unclear with my description.
I'm not using a Renderer and a rendertarget-texture simultaneously.

I tried using Graphics::TakeScreenShot() as well but then every picture would be black rather than just the initial frame.

[b]Edit:[/b]

I had previously only tried TakeScreenShot() while using the rendertarget-texture. I now thought of trying it while using the Renderer instead and now I don't get any black pictures.
The first two frames are however identical which is not something I had expected. It is however an improvement.

Thank you for your help, if you have any further input feel free to share it :slight_smile:

-------------------------

