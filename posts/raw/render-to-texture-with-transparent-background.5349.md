techel | 2019-07-25 22:05:38 UTC | #1

Hey there,
I'm trying to render to a texture that has it's background color set to (0, 0, 0, 0).
My code looks like this: 

        RenderTexture = MakeShared<Texture2D>(parent.GetContext());
        RenderTexture->SetSize(500, 500, Graphics::GetRGBAFormat(), TEXTURE_RENDERTARGET);
        RenderTexture->SetFilterMode(FILTER_BILINEAR);

        RenderMaterial = MakeShared<Material>(parent.GetContext());
        RenderMaterial->SetTechnique(0, cache->GetResource<Technique>("Techniques/DiffUnlitAlpha.xml"));
        RenderMaterial->SetTexture(TU_DIFFUSE, RenderTexture);
        RenderMaterial->SetCullMode(CullMode::CULL_NONE);
        
        OrthoScene = MakeShared<Scene>(parent.GetContext());
        //setup a scene with an orthographic camera here

        auto *surface = RenderTexture->GetRenderSurface();
        auto vp = MakeShared<Viewport>(parent.GetContext(), OrthoScene, camera);
        surface->SetViewport(0, vp);

        auto *rp = vp->GetRenderPath();
        for(unsigned i = 0; i < rp->GetNumCommands(); i++)
        {
            RenderPathCommand *cmd = rp->GetCommand(i);
            if(cmd->type_ == RenderCommandType::CMD_CLEAR)
            {
                cmd->useFogColor_ = false;
                cmd->clearColor_ = Color(0, 0, 0, 0);
            }
        }

        auto *quad = SceneNode->CreateComponent<CustomGeometry>();
        quad->SetMaterial(RenderMaterial);
        //setup quad here

I've been able to set the background color to a custom value by modifying clearColor_, but setting the alpha value has no effect.

Am I missing something?
Thanks!

-------------------------

Modanung | 2019-07-26 08:22:25 UTC | #2

*I* see no faults in your code.
What happens when you change the color to `(1, 1, 1, 0)`; is the resulting background black or white?

...and welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

techel | 2019-07-26 08:15:03 UTC | #3

> …and welcome to the forums!

Thanks!

> What happens when you change the color to  `(1, 1, 1, 0)` ; is the resulting background black or white?

The resulting background is white. Setting the RGB actually gives the desired color, but setting the alpha has no effect.

-------------------------

techel | 2019-07-26 12:12:56 UTC | #4

I figured out that D3D by default doesn't write alpha values and must be enabled with `SetRenderState ( D3DRS_COLORWRITEENABLE, D3DCOLORWRITEENABLE_RED | D3DCOLORWRITEENABLE_GREEN | D3DCOLORWRITEENABLE_BLUE | D3DCOLORWRITEENABLE_ALPHA );`. Urho3D apparently doesn't do this. Maybe that's worth to implement properly.

Afaik OpenGL does write alpha values, so I'll switch to it.

-------------------------

Modanung | 2019-07-26 12:12:53 UTC | #5

I'm glad you figured it out. It's been years since I touched a Windows machine.

-------------------------

