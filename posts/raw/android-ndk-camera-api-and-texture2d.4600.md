simonsch | 2018-10-19 12:43:08 UTC | #1

Hello community it is me again, 

and again i bother you with camera texture stuff. As some of you know i used a Texture2D for displaying a camera stream from my androids color camera, this was working well as i used googles project tango where i did only need to bind via GLuint
    TangoService_updateTextureExternalOes(
                TANGO_CAMERA_COLOR, textureID,
                &ts)

Now i found this useful tutorial 
https://www.sisik.eu/blog/android/ndk/camera
https://github.com/sixo/native-camera/blob/master/app/src/main/cpp/native-lib.cpp
https://github.com/googlesamples/android-ndk/tree/master/camera

it allowed me to capture the camera stream myself and now i want to get rid off this Tango function.

The important part building a camera capturing session with the ndk is the following code, assume that surface is of type jobject, passed via jni from GLSurfaceView.

      // Prepare surface
    textureId = texId;
    textureWindow = ANativeWindow_fromSurface(env, surface);

    // Prepare outputs for session
    ACaptureSessionOutput_create(textureWindow, &textureOutput);
    ACaptureSessionOutputContainer_create(&outputs);
    ACaptureSessionOutputContainer_add(outputs, textureOutput);

    // Create the session
    ACameraDevice_createCaptureSession(cameraDevice, outputs, &sessionStateCallbacks, &textureSession);

    // Prepare request for texture target
    ACameraDevice_createCaptureRequest(cameraDevice, TEMPLATE_PREVIEW, &textureRequest);

    ANativeWindow_acquire(textureWindow);
    ACameraOutputTarget_create(textureWindow, &textureTarget);
    ACaptureRequest_addTarget(textureRequest, textureTarget);

    // Start capturing continuously
    ACameraCaptureSession_setRepeatingRequest(textureSession, &captureCallbacks, 1,   &textureRequest, nullptr);

So now my question does anyone know how i can add the urho Texture2D into the output container?

    auto surface = cameraTexture->GetRenderSurface()->GetSurface();
    auto target = cameraTexture->GetRenderSurface()->GetTarget();
    auto id = (int)cameraTexture->GetGPUObjectName();

Above are some parameter i can extract but i don't know how to add this texture through the camera capture session output. Maybe anyone already did work with ndk camera api.

Best Regards

-------------------------

simonsch | 2018-10-23 07:08:41 UTC | #2

Still a open task, if you need more details feel free to ask. :wink:

-------------------------

Pencheff | 2018-10-23 12:32:54 UTC | #3

You could hack Texture2D to be able to receive texture from int. It also seems possible to subclass Texture2D and access the texture_ member without modifying the engine code.
I would probably have done this the other way around, copying the contents of that cameraTexture to a texture from Urho3D by using glReadPixels. That however will be a bit CPU intensive depending on the resolution of the camera.

-------------------------

simonsch | 2018-10-24 07:12:05 UTC | #4

Thank you for your answer going through CPU is something which should be avoided under all circumstances. The cpu has to do a lot of other things in my case ;). I already did a fork for myself where i adjusted things like that, but i believe this is just not documented or well explored. The fact that we can access the Surface, Target as well as the RenderSurface of a Texture2D should provide us with enough information to give this ndk api a proper texture target for its output container. I just can't figure out exactly how :D

-------------------------

