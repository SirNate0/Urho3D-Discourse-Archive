lassademus | 2017-09-02 09:34:43 UTC | #1

Hello Guys. I'm trying to render a scene and then saving it as 2D texture like a screenshot. In my test scene there is a simple model. That's what I see:

[https://i.imgur.com/JF8iPdQ.png](https://i.imgur.com/JF8iPdQ.png)

but when I trying to save the texture in .png file it looks like emply scene:

[https://i.imgur.com/8ti8vKw.png](https://i.imgur.com/8ti8vKw.png)

Here is my code:

    	void Start()
    	{
    		scene_ = new Scene(context_); //главное - сцена
    		scene_->CreateComponent<Octree>();

    		//-------------------------------------
    		//Здесь описываем глобальные настройки рендеринга

    		Node* _pZoneAmbientNode = scene_->CreateChild("Zone");
    		if (_pZoneAmbientNode != nullptr) {
    			Zone* _pZoneAmbient = _pZoneAmbientNode->CreateComponent<Zone>();
    			if (_pZoneAmbient != nullptr) {
    				_pZoneAmbient->SetBoundingBox(BoundingBox(-2048.0f, 2048.0f));
    				_pZoneAmbient->SetAmbientColor(Color(1.0f, 1.0f, 1.0f, 1.0f));
    				//_pZoneAmbient->SetFogColor(Color(1.0f, 1.0f, 1.0f, 1.0f));
    				//_pZoneAmbient->SetFogStart(0.0f);
    				//_pZoneAmbient->SetFogEnd(512.0f);
    			}
    		}

    		//-------------------------------

    		// здесь добавляем ноду для камеры и саму камеру
    		/*auto cameraNode = scene_->CreateChild("MyCamera");
    		cameraNode->CreateComponent<Camera>();
    		cameraNode->SetFarClip(512.0f);
    		cameraNode->SetPosition(Vector3(0.0f, 0.0f, -5.0f)); //положение камеры
    		auto viewport = new Viewport(context_, scene_, cameraNode->GetComponent<Camera>()); //какая камера отображается на экране
    		*/
    		auto cameraNode = scene_->CreateChild("MyCamera");
    		if (cameraNode != nullptr){
    			Camera* _pCamera = cameraNode->CreateComponent<Camera>();
    			if (_pCamera != nullptr) {
    				_pCamera->SetFarClip(512.0f);
    			}
    		}
    		auto viewport = new Viewport(context_, scene_, cameraNode->GetComponent<Camera>());
    		GetSubsystem<Renderer>()->SetViewport(0, viewport);

    		//----------------------------------------------------------
    		// здесь создаем текстуру для экспорта в приложение

    		Texture2D* screenTexture = new Texture2D(context_); 
    		screenTexture->SetSize(512, 512, Graphics::GetRGBFormat(), TEXTURE_RENDERTARGET);
    		//screenTexture->SetFilterMode(FILTER_TRILINEAR);
    		RenderSurface* _pRenderSurface = screenTexture->GetRenderSurface();
    		if (_pRenderSurface != nullptr){
    			SharedPtr<Viewport> _pViewport(new Viewport(context_, scene_, cameraNode->GetComponent<Camera>()));
    			_pRenderSurface->SetViewport(0, _pViewport);
    			_pRenderSurface->SetUpdateMode(RenderSurfaceUpdateMode::SURFACE_UPDATEALWAYS);
    		}

    		//---------------------------------------------------------------
    		//Здесь добавляем куб на сцену

    		auto boxNode = scene_->CreateChild("MyBox");
    		auto boxObject = boxNode->CreateComponent<StaticModel>();
    		auto cache = GetSubsystem<ResourceCache>();
    		boxObject->SetModel(cache->GetResource<Model>("Models/cat.mdl"));
    		boxNode->SetPosition(Vector3(0.0f, -50.0f, 250.0f));
    		boxNode->SetRotation(Quaternion(0.0f, 90.0f, -90.0f));
    		boxObject->SetMaterial(cache->GetResource<Material>("Materials/Skybox.xml"));

    		//---------------------------------------------------------
    		// добавляем источник освещения

    		auto lightNode = scene_->CreateChild("MyLight");
    		auto light = lightNode->CreateComponent<Light>();
    		light->SetLightType(LIGHT_DIRECTIONAL);
    		lightNode->SetDirection(Vector3(0.6f, -0.6f, 0.8f));

    		//----------------------------------
    		//здесь пишем текстуру в файл (игрушечный код)

    		GetSubsystem<Renderer>()->Update(1.0f);
    		GetSubsystem<Renderer>()->Render();

    		Image* _pImage = new Image(context_);
    		_pImage->SetSize(512, 512, 3);
    		unsigned char* _ImageData = new unsigned char[screenTexture->GetDataSize(512, 512)];
    		screenTexture->GetData(0, _ImageData); //отсюда буфер изображения можно забрать, минуя файл
    		_pImage->SetData(_ImageData);
    		_pImage->SavePNG("test.png");
    		//scene_->TakeScreenShot(_ImageData);

    		delete[] _ImageData;
    	}



Thank you !

-------------------------

jmiller | 2017-09-02 15:59:22 UTC | #2

Hi lassademus.

Saving a screenshot is easier in current master; e.g.: https://github.com/urho3d/Urho3D/blob/master/Source/Samples/Sample.inl#L340

Here is a bit of my code with added functionality.
'cfg_' is the [url=https://discourse.urho3d.io/t/a-more-advanced-ini-parser/1449]most useful ini/config Manager by thebluefish[/url]. Here it is just setting the path from .cfg file.

```
bool App::SaveScreenshot(String dir /* = String::EMPTY */) const {
  if (dir.Empty()) {
    if (cfg_->Has("engine", "ScreenshotDirectory")) {
      dir = cfg_->GetString("engine", "ScreenshotDirectory", "./");
    } else {
      dir = GetSubsystem<FileSystem>()->GetProgramDir();
    }
  }

  String filePath(dir + "screenshot_");
  filePath += UTCTime();
  filePath += ".png";

  URHO3D_LOGINFO("Screenshot: " + filePath);

  bool dirValid = GetSubsystem<FileSystem>()->CreateDir(dir);
  if (dirValid) {

    Graphics* graphics = GetSubsystem<Graphics>();
    Image screenshot(context_);
    graphics->TakeScreenShot(screenshot);
    screenshot.SavePNG(filePath);

  } else {
    URHO3D_LOGERROR("Screenshot error: invalid ScreenshotDirectory '" + dir + "'");
    return false;
  }
  return true;
}

const String App::UTCTime(bool local /* = true */) const {
  std::time_t now(std::time(nullptr));
  std::tm* ptm(nullptr);
  if (local)
    ptm = std::localtime(&now);
  else
    ptm = std::gmtime(&now);

  char buffer[32];
  std::strftime(buffer, 32, "%Y-%m-%d_%H%M%S", ptm);
  return String(buffer);
}
```

HTH

-------------------------

lassademus | 2017-09-03 08:19:12 UTC | #3

Thanks for reply, it works, but I'm still have a problem with transparency. Is there a way to save the scene with transparent background?

-------------------------

jmiller | 2017-09-09 16:58:48 UTC | #4

The OpenGL Takescreenshot() is normally RGB (except on mobile):
  https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/OpenGL/OGLGraphics.cpp#L608

Like your original function, this one reads Texture components directly -- but for RGBA, passed Texture must already be RGBA (4 components) so problem is the same.

```
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
```

-------------------------

