elissa | 2017-04-07 08:24:34 UTC | #1

Hey there, I'm doing a test to see if we can use Urho's rendering engine to replace our existing one.

What we need is be able to render 2D elements to screens within a 3D space.

Obviously, Urho can do this quite fine (and very well - it's so far been a pleasure of an engine to work with) but there's two things left confusing me. I've already scoured the forums but haven't found any help for this specific problem.

For context, I've attached a screenshot of my test scene, and I'll list the code I'm using and what the problems are.

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/5f96f8595c308c2ae5b263fe149f52a8c1e8f395.png" width="690" height="422">

The first thing I'm doing is creating an Ortho camera for the 2D rendering 

    m_rtScene = new Scene(context_);
    m_rtScene->CreateComponent<Octree>();
    
    m_rtCameraNode = m_rtScene->CreateChild("Camera");
    Camera* c = m_rtCameraNode->CreateComponent<Camera>();
    c->SetOrthographic(true);
    c->SetOrthoSize(Vector2(SCREEN_WIDTH * PIXEL_SIZE, SCREEN_HEIGHT * PIXEL_SIZE));
    c->SetAspectRatio(SCREEN_WIDTH/SCREEN_HEIGHT);

In this case it's intended to simulate a nice low res, so SCREEN_WIDTH is 320, and SCREEN_HEIGHT is 320.

Then the actual rendertexture gets created

    SharedPtr<Texture2D> renderTexture(new Texture2D(context_));
    renderTexture->SetSize(SCREEN_WIDTH, SCREEN_HEIGHT, Graphics::GetRGBFormat(), TEXTURE_RENDERTARGET);
    renderTexture->SetFilterMode(FILTER_NEAREST);
    SharedPtr<Material> renderMaterial(new Material(context_));
    renderMaterial->SetTechnique(0, cache->GetResource<Technique>("Techniques/DiffUnlit.xml"));
    renderMaterial->SetTexture(TU_DIFFUSE, renderTexture);
    renderMaterial->SetDepthBias(BiasParameters(-0.001f, 0.0f));
    m_monitorScreen->SetMaterial(renderMaterial);
    m_renderSurface = renderTexture->GetRenderSurface();
    m_renderViewport = new Viewport(context_, m_rtScene, m_rtCameraNode->GetComponent<Camera>());
    m_renderSurface->SetViewport(0, m_renderViewport);

And finally, putting a sprite in there

    Node* spriteNode = m_rtScene->CreateChild("StaticSprite2D");
    StaticSprite2D* sprite = spriteNode->CreateComponent<StaticSprite2D>();
    Sprite2D* sr = cache->GetResource<Sprite2D>("Resources/spr.png");
    sr->SetHotSpot(Vector2(0, 0));
    spriteNode->SetPosition2D(0, 0);
    sprite->SetSprite(sr);

The problem is threefold:

1) The sprite's 0,0 position (as you can see) places it bang in the middle of the "screen" - top-left or bottom-left would be ideal, but I presume I can move the ortho camera around to compensate for this - although it seems less than ideal.
2) positions for objects to go on this screen aren't per-pixel, I presume because I haven't set the ortho size correctly? For instance, the two sprites you see on the screen have the positions 0,0 and 1,0 respectively - and they're very far apart.
and
3) Despite it being a clean sprite set to FILTER_NEAREST, it still does a bit of alpha blending - it's a little fuzzy around the edges there.

Any suggestions as to what I'm doing wrong? It's VERY close to being exactly what we need.

-------------------------

