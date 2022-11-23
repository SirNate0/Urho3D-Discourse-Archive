AlexS32 | 2017-08-28 18:24:15 UTC | #1

Hello.

Is any way to call  a method in Urho3D main thread from Android?
I try to change plane objects texture, but I can't do it in non main thread.
As result I've got log message:
com.github.urho3d E/libEGL: call to OpenGL ES API with no current context (logged once per thread)

-------------------------

johnnycable | 2017-08-28 20:01:41 UTC | #2

Better if you add some code...

-------------------------

AlexS32 | 2017-08-29 12:16:25 UTC | #3

ok
My project is experemental. Basic project is RenderToTexture from Urho3d samples.

Java code:

    native void setTexture();

    @Override
     public void onClick(View view) {
         setTexture();
     }

C++ code:

    class EngineGateway {

    protected:
    Urho3D::Application* application;

    public:
    Urho3D::Application *getApplication() const;
    void setApplication(Urho3D::Application *application);
    };

    /////////////////////////////////////

    EngineGateway *engineGateway;

    /////////////////////////////////////
        extern "C"{

      JNIEXPORT void JNICALL
      Java_com_mydomen_test2_BasicFragment_setTexture(JNIEnv *env, jobject instance) {

        RenderToTexture *app = dynamic_cast<RenderToTexture*>(engineGateway->getApplication());
        app->setTexture();
     }

    }

    /////////////////////////////////////

     void RenderToTexture::CreateScene() {

    ...

      StaticModel *boxObject = screenNode->CreateComponent<StaticModel>();
        boxObject->SetModel(cache->GetResource<Model>("Models/Plane.mdl"));

        SharedPtr<Material> renderMaterial(new Material(context_));
        renderMaterial->SetTechnique(0, cache->GetResource<Technique>("Techniques/Diff.xml"));
        renderTexture = SharedPtr<Texture2D>(new Texture2D(context_));

        renderTexture->SetNumLevels(1);
        renderTexture->SetSize(1024, 768, Graphics::GetRGBFormat(), TEXTURE_DYNAMIC);

        int textureWidth = renderTexture->GetWidth();
        int textureHeight = renderTexture->GetHeight();

        SharedPtr<Image> texImg = SharedPtr<Image>(new Image(context_));
        texImg->SetSize(textureWidth, textureHeight, 3);
        for (int i = 0; i < width; ++i) {
            for (int j = 0; j < height; ++j) {
                texImg->SetPixel(i, j, Color(0, 0, 1));
            }
        }
        renderTexture->SetData(texImg);

        renderMaterial->SetTexture(TU_DIFFUSE, renderTexture);  
        boxObject->SetMaterial(renderMaterial);   // It works, so it is colled in engine main thread
       ...
    }

    void RenderToTexture::setImage() {

    const int width = renderTexture->GetWidth();
    const int height = renderTexture->GetHeight();

    Image* texImg = new Image(context_);
    texImg->SetSize(width, height, 3);
    for (int i = 0; i < width; ++i) {
        for (int j = 0; j < height; ++j) {
            texImg->SetPixel(i, j, Color(1, 1, 1));
        }
    }
    renderTexture->SetData(texImg);		// It dosn't work, so it is colled in Android MainUI thread
    }

-------------------------

johnnycable | 2017-08-29 13:39:08 UTC | #4

It doesn't look like the 10_RenderToTexture sample... did you tried that?

-------------------------

AlexS32 | 2017-08-29 14:06:15 UTC | #5

This sample has a good model - a screen is above the floor. I've made some changes in  the 10_RenderToTexture sample.  For example I use color fill as a texture. 
I  try to change a texture on this screen.

-------------------------

