vivienneanthony | 2017-04-17 13:55:35 UTC | #1

Hi,

I'm trying to save a image of the viewport. I'm using this code. The format of the screen would be RGBA. I think I have the right code but something is missing.


// Set to the active camera
	Image * OutputImage(new Image(context_));
	Texture2D * pRenderTexture(new Texture2D(context_));
	Texture2D * pDepthTexture(new Texture2D(context_));

	// Set width and height
	const unsigned int outputHeight = 900;
	const unsigned int outputWidth = 1440;

	// Set Image
	OutputImage->SetSize(outputWidth, outputHeight,  4);

	// Create necessary texture
	pRenderTexture->SetSize(outputHeight, outputWidth, m_textureFormat, TEXTURE_RENDERTARGET);
	pDepthTexture->SetSize(outputHeight, outputWidth, Graphics::GetDepthStencilFormat(), TEXTURE_DEPTHSTENCIL);

	// Set parameneters
	pRenderTexture->SetFilterMode(FILTER_NEAREST);
	pDepthTexture->SetFilterMode(FILTER_NEAREST);

	RenderSurface * pRenderSurface = pRenderTexture->GetRenderSurface();

	// Set Render Surface
	pRenderSurface->SetViewport(0, m_pCameraViewport);
	pRenderSurface->SetUpdateMode(SURFACE_UPDATEALWAYS);
	pRenderSurface->SetLinkedDepthStencil(pDepthTexture->GetRenderSurface());

	// Queue Update
	pRenderSurface->QueueUpdate();

	unsigned char* _ImageData = new unsigned char[outputWidth*outputHeight*4];
	pRenderTexture->GetData(0, _ImageData);

	OutputImage->SetData(_ImageData);

	OutputImage->SaveTGA("snapshoot.tga");

	pRenderTexture->SaveTGA("test.tga");

Vivienne

-------------------------

jmiller | 2017-04-17 15:17:10 UTC | #2

Hi Viv,

Maybe try RenderSurface::GetParentTexture() ?

ProcSky gets it from a TextureCube face, but I assume it works similarly.
[code]
     Texture2D* faceTex(static_cast<Texture2D*>(texCube->GetRenderSurface((CubeMapFace)faceIndex)->GetParentTexture()));
[/code]

General Texture2D save
[code]
bool App::SaveTexturePNG(Texture2D* texture, const String& filePath) const {
  SharedPtr<Image> image(new Image(context_));
  image->SetSize(texture->GetWidth(), texture->GetHeight(), texture->GetComponents());

  if (texture->GetData(0, image->GetData())) {
    if (image->SavePNG(filePath)) {
      URHO3D_LOGINFO("Save texture: " + filePath);
      return true;
    }
  } else {
    URHO3D_LOGERROR("Save texture: " + filePath + " : failed GetData().");
  }
  return false;
}
[/code]

-------------------------

SirNate0 | 2017-04-18 02:48:48 UTC | #3

It could also be that the render target hadn't been written to by the time you fetch it's data (I ran into that problem with some textures I only wanted for one frame - you could only read the data after the update during the next frame, but I also constructed everything in that scene solely for that one frame, I wasn't saving an already present view port).

-------------------------

vivienneanthony | 2017-04-18 04:42:30 UTC | #4

Hmmm. That might be the problem.

-------------------------

