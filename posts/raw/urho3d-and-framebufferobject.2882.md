SteveU3D | 2017-03-17 19:51:02 UTC | #1

Hi,
I would like to know if it's possible to render Urho3D to the frame buffer, to get it back in qml opengl, in order to get the same result as https://advancingusability.wordpress.com/2013/03/30/how-to-integrate-ogre3d-into-a-qt5-qml-scene/ .
In fact, I already integrated a Urho3D window in a qml item via external window but it appears above all qml items. So, by using the frame buffer, it will be possible to put the qml items above the Urho3D window.

Thanks.

-------------------------

cadaver | 2017-03-17 19:51:16 UTC | #2

If you create a Texture2D as a rendertarget, and render to it (see the RenderToTexture sample), you are then able to call GetGPUObjectName() on the Texture2D to get its OpenGL texture handle, assuming Urho has been compiled for OpenGL.

Framebuffer objects are used and reused internally by the engine and are not available publicly (one FBO does not necessarily correspond to one texture), but you should be able to construct your own FBO into which the texture is attached, if you really need an FBO and the texture handle is not enough.

-------------------------

SteveU3D | 2017-03-15 08:07:53 UTC | #3

I did it with a Texture2D as a render target but without GetGPUObjectName().

In Urho3D code (I started from the RenderToTexture sample) : 

    renderTexture = new Texture2D(context_);
    renderTexture->SetSize(URHO_WIDTH, URHO_HEIGHT, Graphics::GetRGBAFormat(), TEXTURE_RENDERTARGET);
    renderTexture->SetFilterMode(FILTER_BILINEAR);

    // Create a new material ...
    ...
    mGPUObjectName = renderTexture->GetGPUObjectName();
    mRenderTextureData = new unsigned char[renderTexture->GetDataSize(URHO_WIDTH, URHO_HEIGHT)];

    // Get the texture's RenderSurface object (exists when the texture has been created in rendertarget mode) ...
    RenderSurface* surface = renderTexture->GetRenderSurface();
    SharedPtr<Viewport> rttViewport(new Viewport(context_, rttScene_, rttCameraNode_->GetComponent<Camera>()));
    surface->SetViewport(0, rttViewport);

    renderTexture->GetData(0, mRenderTextureData);
    emit signalUrho3DToQML(mGPUObjectName, mRenderTextureData, URHO_WIDTH, URHO_HEIGHT);

And in the QML code : 

    glEnable(GL_TEXTURE_2D);
    glBindTexture(GL_TEXTURE_2D, textureNum);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA , URHO_WIDTH, URHO_HEIGHT, 0, GL_RGBA , GL_UNSIGNED_BYTE, mRenderTextureData);
    glBegin(GL_QUADS);
        glTexCoord2d(0,0); glVertex3f(-1.f, -1.f, 0.0f);
        glTexCoord2d(1,0); glVertex3f(1.f, -1.f, 0.0f);
        glTexCoord2d(1,1); glVertex3f(1.f, 1.f, 0.0f);
        glTexCoord2d(0,1); glVertex3f(-1.f, 1.f, 0.0f);
    glEnd();
    glDisable(GL_TEXTURE_2D);

I can use the mGPUObjectName for textureNum but it doesn't change anything. Maybe I do something wrong :confused: . However it works as I want, except that the QML texture has aliasing as you can see on the image below (on the left QML openGL, on the right Urho3D) :confounded: . Some settings to do in openGL?

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/9cccabade2246b22a33a1eecbc71386726447acd.png" width="690" height="375">

-------------------------

Eugene | 2017-03-15 08:33:45 UTC | #4

Your RT at Urho side shall be anti-aliased. I don't know whether the Urho expose such functionality.

-------------------------

cadaver | 2017-03-15 14:59:54 UTC | #5

Texture2D::SetSize() has multisampling options when used for rendertargets.

-------------------------

SteveU3D | 2017-03-16 09:05:25 UTC | #6

One last question to finalize this post :slight_smile:.
So now, having integrated Urho3D in a QML window, I don't need the Urho3D default window anymore. Indeed, as I get the render texture displayed in QML, it's useless to have a second window, the Urho3D one. So I would like to run only Urho3D engine, without the window.
But after some researches, I found this post https://urho3d.prophpbb.com/topic1365.html in which you say, cadaver, that it's not possible to run a scene without a window, and you suggest to just create a small window without rendering to it, as the scene is rendered to a texture.

So, is this post still topical or is there a new solution in Urho3D to really not open a window?
Thanks!

-------------------------

Eugene | 2017-03-16 09:10:52 UTC | #7

Why not to make invisible window and pass it as 'external window'?

-------------------------

SteveU3D | 2017-03-16 09:38:57 UTC | #8

I don't use the external window because I need to put QML items over the 3D scene, which doesn't work over an external window :slight_smile:.

-------------------------

Eugene | 2017-03-16 09:45:38 UTC | #9

I don't understand how does the invisible external window disturb anything that you do.

-------------------------

SteveU3D | 2017-03-16 10:32:48 UTC | #10

Sorry, I didn't understand your answer well, but it's ok now. Indeed, I just need to hide that external window : 

        hwndNative = CreateWindow(L"STATIC", L"Test native window", 0, 0, 0, 10, 10, 0, 0, 0, 0);
        ShowWindow(hwndNative,SW_HIDE);

and in Urho3D : 

    engineParameters_["ExternalWindow"] = hwndNative;

-------------------------

