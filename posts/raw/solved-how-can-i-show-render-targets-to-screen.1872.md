Shylon | 2017-01-02 01:10:58 UTC | #1

Hi, 
I am new to Urho3d :slight_smile:, and would like to know how can I show specific render-target to the screen? for example depth or G-Buffers, I know some opengl and I am learning OpenGL beside using Urho3d for my future Desktop game, I would like to focus also on Opengl 4.x (using its feature like tessellation, handling large amount of meshes on GPU & ..) for my game too, but for me for now Urho3d custom shader pipeline is confusing, so any guide would help me and new users also might the urho3d dev progress.

-------------------------

1vanK | 2017-01-02 01:10:58 UTC | #2

Append to renderpath
[code]
    <command type="quad" vs="CopyFramebuffer" ps="CopyFramebuffer" output="viewport">
        <texture unit="diffuse" name="RENDER TARGET" />
    </command>
[/code]

-------------------------

cadaver | 2017-01-02 01:10:58 UTC | #3

Another way is via a UI-element (BorderImage for example) to which you assign the rendertarget as the texture. 

However rendertargets defined in the renderpath can even be a different texture on successive frames / views as they are auto-allocated, so in that case 1vanK's approach is practically the only workable.

-------------------------

Shylon | 2017-01-02 01:10:58 UTC | #4

Thanks @1vanK 
but it is not working for me, I used as xml and added to viewport

[code] Renderer *renderer = GetSubsystem<Renderer>();
    //NOTE: this must be enabled so that HDR works
    renderer->SetHDRRendering(true);

    //Setup view
    SharedPtr<Viewport> viewport(new Viewport(context_, scene_, cameraNode_->GetComponent<Camera>()));
    renderer->SetViewport(0, viewport);

    //post-process
    ResourceCache* effectCache = GetSubsystem<ResourceCache>();
    //Note the clone
    SharedPtr<RenderPath> effectRenderPath = viewport->GetRenderPath()->Clone();
//    effectRenderPath->Append(effectCache->GetResource<XMLFile>("PostProcess/FXAA3.xml"));
//    effectRenderPath->Append(effectCache->GetResource<XMLFile>("PostProcess/AutoExposure.xml"));
//    effectRenderPath->Append(effectCache->GetResource<XMLFile>("PostProcess/BloomHDR.xml"));
    effectRenderPath->Append(effectCache->GetResource<XMLFile>("PostProcess/ShowPass.xml"));
//    effectRenderPath->SetShaderParameter("BloomHDRThreshold", 0.2f);
//    effectRenderPath->SetEnabled("FXAA3", true);
//    effectRenderPath->SetEnabled("AutoExposure", true);
//    effectRenderPath->SetEnabled("BloomHDR", true);
    effectRenderPath->SetEnabled("ShowPass", true);

    //now set to the effect render path
    viewport->SetRenderPath(effectRenderPath);[/code]

in xml named ShowPass.xml

[code]<renderpath>
    <command type="quad" vs="CopyFramebuffer" ps="CopyFramebuffer" output="viewport">
		<texture unit="diffuse" name="Depth" />
	</command>
</renderpath>[/code]

Thanks @cadaver
I was also thinking about using a ui image and add rendered texture to the ui image, like getting the Depth and using as image on UI like camera using in Editor I need it for debugging shaders, I should dig more into Urho3d, however I should say today I was testing using LogicComponent for character animation update and it is really nice, one of the advantage of it is easily pausing the game by scene.

-------------------------

1vanK | 2017-01-02 01:10:58 UTC | #5

Forward has no Depth pass by default

-------------------------

1vanK | 2017-01-02 01:10:58 UTC | #6

U need use RenderPaths\ForfardDepth.xml or RenderPaths\ForfardHWDepth.xml

-------------------------

Shylon | 2017-01-02 01:10:59 UTC | #7

I am sorry for asking again, can you please clarify, How can I set Urho3d to use Deferred Rendering, in documentation as I understand its says Urho3d uses both Deferred and forward at same time.

-------------------------

1vanK | 2017-01-02 01:10:59 UTC | #8

one of the methods

[code]void Game::SetupViewport()
{
    Renderer* renderer = GetSubsystem<Renderer>();
    auto cache = GetSubsystem<ResourceCache>();
    renderer->SetDefaultRenderPath(cache->GetResource<XMLFile>("RenderPaths/MyForward.xml"));
    SharedPtr<Viewport> viewport(new Viewport(context_, scene_, cameraNode_->GetComponent<Camera>()));
    renderer->SetViewport(0, viewport);
    viewport->GetRenderPath()->Append(cache->GetResource<XMLFile>("PostProcess/FXAA3.xml"));
}
[/code]

-------------------------

Shylon | 2017-01-02 01:10:59 UTC | #9

Thank you so much, now it is working, also I should point out that setting Default Render Path should be before setting view as I had mistake in my code.
 :smiley:

-------------------------

