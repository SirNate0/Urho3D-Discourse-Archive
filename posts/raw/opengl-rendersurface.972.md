thebluefish | 2017-01-02 01:04:32 UTC | #1

I'm trying to figure out this crash. I recently got scorvi's editor re-integrated into my project, and made several changes after that. Since I'm running under windows, DirectX is the default renderer. When I specify URHO3D_OPENGL in the preprocessor, my initial stuff works. The mainmenu GUI and everything else appears to be fine. However when trying to use scorvi's editor, it crashes. This occurs with a build before the render-refactor branch, and after. The issue seems to come from the following bit:

[code]
Urho3D::RenderSurface* surface = renderTexture_->GetRenderSurface();
surface->SetViewport(0, viewport_);
[/code]

Under DX, surface is a valid pointer. However under OpenGL, it is null. Under OpenGL, renderTexture_ is valid, and there doesn't appear to be any other null pointers or invalid data.

Digging into Urho3D, I see that Texture2D::SetSize creates the RenderSurface in DX but not OpenGL. How should this be properly handled for OpenGL?

-------------------------

cadaver | 2017-01-02 01:04:32 UTC | #2

If you specify usage of TEXTURE_RENDERTARGET or TEXTURE_DEPTHSTENCIL, both D3D and OpenGL should create the RenderSurface during SetSize().

-------------------------

dvan | 2017-01-02 01:12:33 UTC | #3

This just solved the problem I was having with SetSize while testing under OpenGL. Thanks.

Not sure what these TextureUsage settings are without a lot of digging. Anyone explain what the real differences / ramifications are between the default and various other setting options?  (pre-emptive trouble avoidance)

PS. This did not work when I switched back to VS2015 / D3D. Had to go back to default setting. (was testing with MinGW / OpenGL)

-------------------------

