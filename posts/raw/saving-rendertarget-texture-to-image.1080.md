franck22000 | 2017-01-02 01:05:17 UTC | #1

Hello Guys i am trying to render a model (cube in this example) in a render target and then saving the render target inside an PNG image file like a screenshot. As you can see the image saved is... weird even if you can recognize the cube a little bit :slight_smile: 

[url=http://tof.canardpc.com/view/581367ca-fa30-40d0-a68c-8ec93c77d52c.jpg][img]http://tof.canardpc.com/preview2/581367ca-fa30-40d0-a68c-8ec93c77d52c.jpg[/img][/url]

The nearly same code was working correctly with OpenGL 3.2 and now i am using DirectX11. Can anyone have a solution to render the image correctly in DirectX11 ? 

Viewport, Camera and render target creation code: 

[code]// Create viewport scene 
	m_p3DViewportScene = new Scene(context_);
	m_p3DViewportScene->CreateComponent<Octree>();

	Node* _pZoneAmbientNode = m_p3DViewportScene->CreateChild("Zone");

	if (_pZoneAmbientNode != nullptr)
	{

		Zone* _pZoneAmbient = _pZoneAmbientNode->CreateComponent<Zone>();

		if (_pZoneAmbient != nullptr)
		{
			_pZoneAmbient->SetBoundingBox(BoundingBox(-2048.0f, 2048.0f));
			_pZoneAmbient->SetAmbientColor(Color(1.0f, 1.0f, 1.0f));
			_pZoneAmbient->SetFogColor(Color(1.0f, 0.0f, 0.0f));
			_pZoneAmbient->SetFogStart(0.0f);
			_pZoneAmbient->SetFogEnd(512.0f);
		}

	}

	// Create camera viewport
	 m_p3DViewportCameraNode = m_p3DViewportScene->CreateChild();

	if (m_p3DViewportCameraNode != nullptr)
	{

		Camera* _pCamera = m_p3DViewportCameraNode->CreateComponent<Camera>();

		if (_pCamera != nullptr)
		{
			_pCamera->SetFarClip(512.0f);
			//_pCamera->SetOrthographic(true);
		}

	}

	// Create rendertarget
	m_p3DViewportRenderTexture = new Texture2D(context_);
	m_p3DViewportRenderTexture->SetSize(512, 512, Graphics::GetRGBFormat(), TEXTURE_RENDERTARGET);
	m_p3DViewportRenderTexture->SetFilterMode(FILTER_TRILINEAR);

	RenderSurface* _pRenderSurface = m_p3DViewportRenderTexture->GetRenderSurface();

	if (_pRenderSurface != nullptr)
	{
		SharedPtr<Viewport> _pViewport(new Viewport(context_, m_p3DViewportScene, m_p3DViewportCameraNode->GetComponent<Camera>()));
		_pRenderSurface->SetViewport(0, _pViewport);
		_pRenderSurface->SetUpdateMode(RenderSurfaceUpdateMode::SURFACE_UPDATEALWAYS);
	}
 [/code]

And the rendering and saving of the PNG file:

[code]m_pModelNode = m_p3DViewportScene->CreateChild();
	m_pModelNode->SetPosition(Vector3(0.0f, 0.0f, 5.0f));
	m_pModelNode->SetRotation(Quaternion(0.0f, 0.0f, 0.0f));

	StaticModel* _pStaticModel = m_pModelNode->CreateComponent<StaticModel>();
	_pStaticModel->SetModel(_pResourceLoader->GetResource<Model>(fModelResourcePath));
	_pStaticModel->SetCastShadows(false);
	_pStaticModel->ApplyMaterialList();

	// Render the screen
	GetSubsystem<Renderer>()->Update(1.0f);
	GetSubsystem<Renderer>()->Render();

	// Image saving
	Image* _pImage = new Image(context_);
	_pImage->SetSize(512, 512, 3);

	unsigned char* _ImageData = new unsigned char[m_p3DViewportRenderTexture->GetDataSize(512, 512)];
	m_p3DViewportRenderTexture->GetData(0, _ImageData);

	_pImage->SetData(_ImageData);

	_pImage->SavePNG("test.png");

	delete[] _ImageData; [/code]

Thank you ! :slight_smile:

-------------------------

franck22000 | 2017-01-02 01:05:17 UTC | #2

Someone helped me to fix the issue. 

this make the code crash:

[code]Image* _pImage(new Image(context_));
_pImage->SetSize(512, 512, 3);[/code]

And this is working:

[code]Image* _pImage(new Image(context_));
_pImage->SetSize(512, 512, 4);[/code]

it works ! 

Can someone explain me why i need 4 component instead of 3 ? I just need RGB component :slight_smile:

Do i have found a Urho3D bug here ?

-------------------------

franck22000 | 2017-01-02 01:05:17 UTC | #3

Hello Sinoid (thank you for all your work related to Urho3D by the way).

You mean checking the render target texture format ?

-------------------------

franck22000 | 2017-01-02 01:05:18 UTC | #4

[quote]There should probably be a function for returning the number of components in a format.[/quote]

That fonction would be usefull

-------------------------

cadaver | 2017-01-02 01:05:25 UTC | #5

GetData() from rendertarget texture was not working on D3D9. It should be fixed in the master branch. Also added GetComponents() to Texture class to determine the number of components needed in Image to hold the returned data. Note that it will return 0 (illegal, basically) for compressed formats.

-------------------------

