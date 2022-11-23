rbnpontes | 2017-01-02 01:14:20 UTC | #1

I need to get RenderSurface created in RenderPath, if i'm trying to get Texture from [b]View[/b] the texture only return null

-------------------------

cadaver | 2017-01-02 01:14:20 UTC | #2

If you mean using View::FindNamedTexture() be aware that it's only valid during view rendering, as the textures are pooled and reused. Actually there's right now not a good event that would fire after the textures have been reserved; that should be added, but right now you could send an event from the beginning of the renderpath (CMD_SENDEVENT).

If you need to reliably get to the texture during any time within the frame you should turn it around by creating the texture yourself, giving it a name and storing it to the resource cache as a manual resource. E.g. "MyTexture". Then you can refer to "MyTexture" in the renderpath and it will use your texture instead of allocating a pooled texture.

-------------------------

rbnpontes | 2017-01-02 01:14:21 UTC | #3

Thank's for the explanation, but exist one mean to set a Created RenderSurface in gpu and transfer to RenderPath ?

-------------------------

cadaver | 2017-01-02 01:14:21 UTC | #4

Can't understand what you're asking, sorry.

-------------------------

rbnpontes | 2017-01-02 01:14:21 UTC | #5

Ok, i have a RenderSurface created in CPU, i need transfer this RenderSurface to RenderPath
I working to implement HBAO+ from Nvidia Gameworks, the process off render HBAO is working normaly, but i need clean RenderSurface in GPU
[code]
Texture2D* tex = new Texture2D(context_);
RenderSurface* _renderTarget = tex->GetRenderSurface();
// I need upload _renderTarget to GPU
[/code]

-------------------------

franck22000 | 2017-01-02 01:14:21 UTC | #6

I have tried to add nvidia HBAO+ a month ago but did not succeeded. If you get it working could you share your code ?

-------------------------

cadaver | 2017-01-02 01:14:21 UTC | #7

The SetSize() function for a rendertarget Texture2D creates the GPU-side representation. After that you can render to it, or sample it.

tex->SetSize(width, height, Graphics::GetRGBAFormat(), TEXTURE_RENDERTARGET);

Replace format with what you actually need.

-------------------------

rbnpontes | 2017-01-02 01:14:21 UTC | #8

[quote="franck22000"]I have tried to add nvidia HBAO+ a month ago but did not succeeded. If you get it working could you share your code ?[/quote]
Yep, i Will share the code, i have sucess for execute HBAO, but my problem is for clean render buffer

-------------------------

rbnpontes | 2017-01-02 01:14:21 UTC | #9

Thank's cadaver for the help

-------------------------

cadaver | 2017-01-02 01:14:22 UTC | #10

In master branch, a new event was added (E_VIEWBUFFERSREADY) which is sent when a view's screen buffers have been allocated and are valid to query with FindNamedTexture().

-------------------------

