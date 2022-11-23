freegodsoul | 2017-01-02 01:08:06 UTC | #1

I didn't find any engine parameter ([b]Application::engineParameters_[/b]) responding for maximization/minimization of window,
so I've put this code in begining of my [b]Application::Start()[/b] implementation.

[code]Graphics* gfx = GetSubsystem<Graphics>();
GraphicsImpl* gfximpl = gfx->GetImpl();
SDL_Window* sdlwnd = gfximpl->GetWindow();
SDL_MaximizeWindow( sdlwnd );[/code]

P.S. Out-of-box Editor app already has maximized window, so I'm not sure if this approach is non-redundant. It looks like workaround, but it's working. :wink:

[b][EDIT][/b]

After some research I've found the method [b]Graphics::Maximize()[/b]. Final version:
:smiley:

[code]Graphics* gfx = GetSubsystem<Graphics>();
gfx->Maximize();[/code]

-------------------------

