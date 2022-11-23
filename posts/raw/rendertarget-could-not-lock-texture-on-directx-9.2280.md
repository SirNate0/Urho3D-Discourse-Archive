Absyl | 2017-01-02 01:14:28 UTC | #1

Hello,

I am trying to render a texture which I update every frame in code.

I am creating the rendertarget like so:
[code]
SharedPtr<Texture2D> renderTarget_(new Texture2D(context));
renderTarget_->SetSize(context_->GetSubsystem<Graphics>()->GetWidth(), context_->GetSubsystem<Graphics>()->GetHeight(), Graphics::GetRGBAFormat(), TEXTURE_RENDERTARGET);
renderTarget_->GetRenderSurface()->SetUpdateMode(SURFACE_UPDATEALWAYS);
[/code]

Whenever I receive updated pixels I set the texture data:
[code]
renderTarget_->SetData(0, 
	0,
	0,
	context_->GetSubsystem<Graphics>()->GetWidth(),
	context_->GetSubsystem<Graphics>()->GetHeight(),
	buffer); // buffer is |width| * |height| * 4 bytes in size representing a BGRA image
[/code]

Running this code with DirectX 9 renderer gives the following error at SetData()
[code]ERROR: Could not lock texture (HRESULT 8876086c)[/code]

Running the same code on Urho3D built with DirectX 11 works with no problem.
Other texture types work fine (TEXTURE_DYNAMIC for example).

What am I doing wrong here? I'd like to use DX9 if possible.

-------------------------

cadaver | 2017-01-02 01:14:28 UTC | #2

If you want to SetData() to a texture manually frequently, do not create it as a rendertarget, but as a dynamic texture. Both rendering to a texture and setting its data manually aren't compatible.

-------------------------

Absyl | 2017-01-02 01:14:29 UTC | #3

Alright, I'll use a dynamic texture as per your recommendation. Thanks.

-------------------------

