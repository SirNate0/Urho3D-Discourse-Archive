AlexS32 | 2017-08-22 13:01:31 UTC | #1

Hello.
I'm interesting in how to transfer the stream from the smartphone's video camera to Urho3d for processing and displaying in the texture.
OS Android. MinSdk 21
P.S.  Sorry for my bad English.

-------------------------

simonsch | 2018-03-09 10:54:41 UTC | #2

Would be also interested in the possibilities of taking a texture stream from a camera through a renderpass in urho3d.

-------------------------

johnnycable | 2018-03-09 13:01:18 UTC | #3

What's wrong with Android [camera2 api](https://developer.android.com/reference/android/hardware/camera2/package-summary.html) that prevents you from using it directly without going the extra effort and complicacies of going thru sdl2, urho3d and then back?
Except that is in Java, of course...

-------------------------

AlexS32 | 2018-03-12 12:03:38 UTC | #4

Android camera2 API is good. I try to use Urho3d as some variant of AR engine.

-------------------------

simonsch | 2018-03-13 08:28:55 UTC | #5

Okay that sounds valid, but my problem is more complex. I have a certain framework which delivers me data i want to process. Over a callback in c++ i get a camera image, as i was able to provide the same opengl context there i bind a glTexture2D.

This texture i want to visualize via a separate render path. Now the problem is normally i would use a glGetUniformLocation for creating a unique identifier for that texture which can be used by my shader program. But i don't understand how to do this with urho3d. So when i bind a texture with opengl how can i tell the urho shader where to find it?

-------------------------

johnnycable | 2018-03-13 08:44:36 UTC | #6

I'm not very expert about those low level details, but I guess you need to do st. like your framework context -> memory -> urho context. Don't think you can have those context exchange data some other way, in a easy way at least...

-------------------------

simonsch | 2018-03-13 09:52:22 UTC | #7

I'm not an expert my self ;). 2 context at the same time are not allowed so i tryed to have one egl context via one SDLSurface View. The problem with the camera api is also that i would need to create a second surface view where to render the camera stream, and the urho surface would overlay this surface view. But on Android a surface view cant blend with its underlying view. So i thought the right way would be defining multiple viewports in urho3d and define a renderpath for using the bound texture. 
I managed to do this with a texture from the assets but i don't know if it is even possible to use a gltexture bind out of urho3d.

-------------------------

Egorbo | 2018-03-15 06:53:03 UTC | #8

You can use an external opengl texture (you create one in Urho3D and provide it to Camera API). I did something similar to that in UrhoSharp for ARCore (it required a dirty hack in urho3d as it doesn't support OES target yet).
See https://github.com/xamarin/urho/blob/master/Extensions/Urho.Extensions.Droid.ARCore/ARCore.cs#L55
and https://github.com/xamarin/urho/blob/master/Urho3D/CoreData/Shaders/GLSL/ARCore.glsl#L10 (should not be difficult to port to C++).
https://github.com/xamarin/urho-samples/blob/master/ARCore/Screenshots/Screenshot.png

-------------------------

simonsch | 2018-03-15 14:54:20 UTC | #9

Hi :),

yeah that is exactly what i wanted to implement. Already had something similiar before switching from pure opengl through urho3d. I looked up your code (btw excellent work), the problem i have with c++ is setting SetCustomTarget for my texture it seems that this function does not exist in urho3d 1.7....

I looked up the binding from P/Invoke where this function is wrapped i see you added SetCustomTarget to Graphics/Texture2D.cpp. I think there is no way without this hack, right? :see_no_evil::sob:

And i see you are using ArCores 	
> session.SetCameraTextureName((int)CameraTexture.AsGPUObject().GPUObjectName);

Any chance you have corresponding OpenGL calls when data is bind through that id?

For better understanding, i forked urho3d and added the mentioned function. In Scene creation of urho i create a texture and add it to the chache

    
    cameraTexture = new Texture2D(context_);
    cameraTexture->SetNumLevels(1);
    cameraTexture->SetName("videooverlay");
    cameraTexture->SetSize(1620, 1920, Urho3D::Graphics::GetFloat32Format(), TextureUsage::TEXTURE_DYNAMIC);
    cameraTexture->SetFilterMode(TextureFilterMode::FILTER_BILINEAR);
    cameraTexture->SetAddressMode(TextureCoordinate::COORD_U, TextureAddressMode::ADDRESS_CLAMP);
    cameraTexture->SetAddressMode(TextureCoordinate::COORD_V, TextureAddressMode::ADDRESS_CLAMP);
    cameraTexture->SetCustomTarget(GL_TEXTURE_EXTERNAL_OES);
    cache->AddManualResource(cameraTexture);

In my renderpath i added the quad render command
        
    <command output="viewport" ps="VrQuad" type="quad" vs="VrQuad">
        <texture unit="diffuse" name="videooverlay"/>
    </command>

In my shader code
    
    
    #extension GL_OES_EGL_image_external : require
    varying vec2 vScreenPos;
    uniform samplerExternalOES sTexture0;
    void VS()
    {
        mat4 modelMatrix = iModelMatrix;
        vec3 worldPos = GetWorldPos(modelMatrix);
        gl_Position = GetClipPos(worldPos);
        vScreenPos = GetScreenPosPreDiv(gl_Position);
    }

    void PS()
    {
        gl_FragColor = texture2D(sTexture0, vScreenPos);
    }

So i can also bind a texture to the diffuse texture unit then the shader output and quad rendering command of my renderpath are working as expected. 

What i want now is to bind my data through that texture created with GL_TEXTURE_EXTERNAL_OES, have the data and tryed 
                cameraTexture->SetData(0, 0, 0, overlay.rows, overlay.cols, overlay.data);
which results in 'Failed to create texture' issues.

-------------------------

Egorbo | 2018-03-21 13:00:56 UTC | #10

Yeah, the SetCustomTarget was a hack.
What do you mean by

> What i want now is to bind my data through that texture created with GL_TEXTURE_EXTERNAL_OES

?
In ARCore I just do
`var externalTextureId = (int)CameraTexture.AsGPUObject().GPUObjectName;`
and now I can tell android camera to which texture it should render by providing this id.

-------------------------

simonsch | 2018-03-21 15:04:40 UTC | #11

Hey man! I finally did it! :) Thy for the help you provided. It was much simpler then i thought even the hack is not necessary anymore, you can even create a default urho3d texture just with the default target. Important is the #extension for GL_TEXTURE_EXTERNAL_OES in your shader code. 

Yeah you use ARCore i don't, that makes a huge difference. Because ARCore only wants you to provide the mentioned textureID. First, i wanted to create this kind of binding by myself, but now i figured out how to do this with my framework. Again your code example really helped me a lot, thy! :slight_smile:

-------------------------

Egorbo | 2018-03-21 16:42:27 UTC | #12

AFAIR, in Android there is SurfaceTexture that does the same - so you can ask Android camera to render to your texture without ARCore ;-)

-------------------------

