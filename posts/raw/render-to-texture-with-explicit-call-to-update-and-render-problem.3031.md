ganibc | 2017-04-21 01:43:37 UTC | #1

Hi all,

I'm trying to generate images for thumbnails and minimaps.
I have 2 different questions:
1. Can we render a scene to texture and save to image file using headless mode? From what I found, it seems it's not possible.
2. I rendered my scene using the sample code (in sample.inl)
>         // Take screenshot
>         else if (key == '9')
>         {
>             Graphics* graphics = GetSubsystem<Graphics>();
>             Image screenshot(context_);
>             graphics->TakeScreenShot(screenshot);
>             // Here we save in the Data folder with date and time appended
>             screenshot.SavePNG(GetSubsystem<FileSystem>()->GetProgramDir() + "Data/Screenshot_" +
>                 Time::GetTimeStamp().Replaced(':', '_').Replaced('.', '_').Replaced(' ', '_') + ".png");
>         }

This code is working just fine. But I have to wait until the scene is rendered and I don't know when the scene will be rendered. I have to wait for few update loops before it actually drawing the scene.
So I tried calling Renderer's Update and Render function and then take the screenshot.
This is working but it gives me weird result.
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/5e3a537f2c5d120c036d8b98195efc34778c1227.png" width="666" height="500">

(I'll post the expected image later because I cannot post 2 images)

It seems to me the there's a problem with the depth test.
Any idea what's wrong?
This is my code:



>     SharedPtr<Viewport> viewport(new Viewport(context_, scene_, cameraNode_->GetComponent<Camera>()));
>     m_textureOut = new Texture2D(context_);
>     m_textureOut->SetSize(width, height, Graphics::GetRGBFormat(), TEXTURE_RENDERTARGET);
>     m_textureOut->SetFilterMode(FILTER_BILINEAR);
>     RenderSurface* renderSurface = m_textureOut->GetRenderSurface();

>     renderSurface->SetViewport(0, viewport);
>     renderSurface->SetUpdateMode(SURFACE_UPDATEALWAYS);
>     GetSubsystem<Renderer>()->Update(1.0f);
>     GetSubsystem<Renderer>()->Render();

>     unsigned char* _ImageData = new unsigned char[m_textureOut->GetDataSize(width, height)];
>     m_textureOut->GetData(0, _ImageData);
>     Image* pImage = new Image(context_);
>     pImage->SetSize(width, height, 3);
>     pImage->SetData(_ImageData);
>     pImage->SavePNG("./test.png");

>     engine_->Exit();

-------------------------

ganibc | 2017-04-21 01:31:26 UTC | #2

This is the expected result:
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/2d2b23697848247023b146ff68a7e15368f47a89.png" width="666" height="500">

-------------------------

SirNate0 | 2017-04-22 05:33:40 UTC | #4

Could it be that you are culling the wrong faces? You could try adding `<cull value="none" />` to the material and see if that changes it (unless you are certain that it is not the cause -- I've never experimented with Headless mode so I have nothing to offer if it is something specific to that).

-------------------------

ganibc | 2017-04-24 09:35:43 UTC | #5

Thanks for the reply.
I tried changing the cullmode, it's still give the same result.
But I found the problem.

I just need to replace these:
> GetSubsystem< Renderer>()->Update(1.0f);
> GetSubsystem< Renderer>()->Render();

to
> engine_->Update();
> engine_->Render();

-------------------------

Sinoid | 2017-04-24 03:11:28 UTC | #6

As far as I'm aware that's still sane.

This is the code I use for rendering from a lumel for lightmapping:

    renderNode_->SetWorldPosition(worldPosition);
    Quaternion rotation;
    rotation.FromLookRotation(normal);
    renderNode_->SetWorldRotation(rotation);

    Graphics* graphics = scene->GetSubsystem<Graphics>();
    Renderer* renderer = scene->GetSubsystem<Renderer>();

    surface_->GetRenderSurface()->QueueUpdate();
    graphics->Clear(-1, Color(0, 0, 0));
    surface_->GetRenderSurface()->SetViewport(0, viewport_.Get());
    renderer->Update();
    graphics->SetRenderTarget(0, surface_);
    renderer->Render();

-------------------------

