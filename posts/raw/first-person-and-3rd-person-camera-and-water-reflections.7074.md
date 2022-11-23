GodMan | 2021-12-01 18:37:28 UTC | #1

So a little on what I am doing is this. I have two cameras in my scene. One if first-person, and the other is 3rd person. The first-person camera is going to use a ViewMask to hide 3rd person character meshes, and vice-versa for the 3rd person camera. 

I noticed that since I have water in my scene that uses the render to texture from the reflection camera that is a child node of the main camera if I toggle the 3rd person camera "main scene camera" to first-person camera everything works fine except the water in the scenes reflection texture will then follow any rotation of the first-person camera. The reflection texture will not stay in it's place. 

What I'm doing now is to toggle to the first-person camera is `viewport->SetCamera(cameraNode2_->GetComponent<Camera>());`
obviously this bug is because I'm not using the main camera anymore. What are some solutions to this?

Thanks

-------------------------

Eugene | 2021-12-01 20:19:52 UTC | #2

You probably should manually handle reflection camera as well.
It should be glued to the node of actually used camera.
https://github.com/urho3d/Urho3D/blob/master/Source/Samples/23_Water/Water.cpp#L203-L227

-------------------------

GodMan | 2021-12-01 20:40:18 UTC | #3

Okay so I think I figured this out before you posted this. What I did was I create 2 reflection cameras. One for each of my scene cameras. Then when toggled between either 3rd or first person. I set the water rtt texture to the active cameras child reflection camera.

	reflectionCameraNode_ = cameraNode_->CreateChild();
	reflectionCamera = reflectionCameraNode_->CreateComponent<Camera>();
	reflectionCamera->SetFarClip(750.0);
	reflectionCamera->SetViewMask(0x7fffffff); // Hide objects with only bit 31 in the viewmask (the water plane)
	reflectionCamera->SetAutoAspectRatio(true);
	reflectionCamera->SetUseReflection(true);
	reflectionCamera->SetReflectionPlane(waterPlane_);
	reflectionCamera->SetUseClipping(true); // Enable clipping of geometry behind water plane
	reflectionCamera->SetClipPlane(waterClipPlane_);
	reflectionCamera->SetAspectRatio((float)graphics->GetWidth() / (float)graphics->GetHeight());
	reflectionCamera->SetViewOverrideFlags(VO_DISABLE_SHADOWS);

	int texSize = 2048;
	renderTexture = (new Texture2D(context_));
	renderTexture->SetSize(texSize, texSize, Graphics::GetRGBFormat(), TEXTURE_RENDERTARGET);
	renderTexture->SetFilterMode(FILTER_BILINEAR);
	RenderSurface* surface = renderTexture->GetRenderSurface();
	SharedPtr<Viewport> rttViewport(new Viewport(context_, scene_, reflectionCamera));
	surface->SetViewport(0, rttViewport);
	waterMat = cache->GetResource<Material>("Materials/relic_water.xml");
	waterMat->SetTexture(TU_DIFFUSE, renderTexture);

	reflectionCameraNode2_ = cameraNode2_->CreateChild();
	reflectionCameraFP = reflectionCameraNode2_->CreateComponent<Camera>();
	reflectionCameraFP->SetFarClip(750.0);
	reflectionCameraFP->SetViewMask(0x7fffffff); // Hide objects with only bit 31 in the viewmask (the water plane)
	reflectionCameraFP->SetAutoAspectRatio(true);
	reflectionCameraFP->SetUseReflection(true);
	reflectionCameraFP->SetReflectionPlane(waterPlane_);
	reflectionCameraFP->SetUseClipping(true); // Enable clipping of geometry behind water plane
	reflectionCameraFP->SetClipPlane(waterClipPlane_);
	reflectionCameraFP->SetAspectRatio((float)graphics->GetWidth() / (float)graphics->GetHeight());
	reflectionCameraFP->SetViewOverrideFlags(VO_DISABLE_SHADOWS);

	renderTextureFP = (new Texture2D(context_));
	renderTextureFP->SetSize(texSize, texSize, Graphics::GetRGBFormat(), TEXTURE_RENDERTARGET);
	renderTextureFP->SetFilterMode(FILTER_BILINEAR);
	RenderSurface* surfaceFP = renderTextureFP->GetRenderSurface();
	SharedPtr<Viewport> rttViewportFP(new Viewport(context_, scene_, reflectionCameraFP));
	surfaceFP->SetViewport(0, rttViewportFP);

This may not be the most performant way to handle this though.

-------------------------

GodMan | 2021-12-01 21:20:58 UTC | #4

Improved code. This will only use the original rtt texture for the water. No need for a second one.

	reflectionCameraNode_ = cameraNode_->CreateChild();
	reflectionCamera = reflectionCameraNode_->CreateComponent<Camera>();
	reflectionCamera->SetFarClip(750.0);
	reflectionCamera->SetViewMask(0x7fffffff);
	reflectionCamera->SetAutoAspectRatio(true);
	reflectionCamera->SetUseReflection(true);
	reflectionCamera->SetReflectionPlane(waterPlane_);
	reflectionCamera->SetUseClipping(true); 
	reflectionCamera->SetClipPlane(waterClipPlane_);
	reflectionCamera->SetAspectRatio((float)graphics->GetWidth() / (float)graphics->GetHeight());
	reflectionCamera->SetViewOverrideFlags(VO_DISABLE_SHADOWS);

	int texSize = 2048;
	renderTexture = (new Texture2D(context_));
	renderTexture->SetSize(texSize, texSize, Graphics::GetRGBFormat(), TEXTURE_RENDERTARGET);
	renderTexture->SetFilterMode(FILTER_BILINEAR);
	surface = renderTexture->GetRenderSurface();
	rttViewport = (new Viewport(context_, scene_, reflectionCamera));
	surface->SetViewport(0, rttViewport);
	waterMat = cache->GetResource<Material>("Materials/relic_water.xml");
	waterMat->SetTexture(TU_DIFFUSE, renderTexture);

	reflectionCameraNode2_ = cameraNode2_->CreateChild();
	reflectionCameraFP = reflectionCameraNode2_->CreateComponent<Camera>();
	reflectionCameraFP->SetFarClip(750.0);
	reflectionCameraFP->SetViewMask(0x7fffffff);
	reflectionCameraFP->SetAutoAspectRatio(true);
	reflectionCameraFP->SetUseReflection(true);
	reflectionCameraFP->SetReflectionPlane(waterPlane_);
	reflectionCameraFP->SetUseClipping(true);
	reflectionCameraFP->SetClipPlane(waterClipPlane_);
	reflectionCameraFP->SetAspectRatio((float)graphics->GetWidth() / (float)graphics->GetHeight());
	reflectionCameraFP->SetViewOverrideFlags(VO_DISABLE_SHADOWS);

Then you can just pass the 1st of 2nd reflection camera to the active viewport based on which camera is active in the scene.

|||rttViewport = (new Viewport(context_, scene_, reflectionCameraFP));|
|---|---|---|
|||surface->SetViewport(0, rttViewport);|
|||viewport->SetCamera(cameraNode2_->GetComponent<Camera>(CameraFP));|

Leaving the code for anyone in the future.

-------------------------

