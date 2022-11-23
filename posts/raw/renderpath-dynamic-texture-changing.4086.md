simonsch | 2018-03-14 10:17:56 UTC | #1

I have a RenderPath which is responsible for rendering a quad with a texture. So far i created a command for using a texture from disk.

    <renderpath>
        <command output="viewport" ps="Quad" type="quad" vs="Quad"
            <texture unit="diffuse" name="Textures/Mushroom.dds"/>
        </command>
    </renderpath>



This works fine, now i want to change this texture programmatically in each new frame. How can i achieve this with c++? The texture is ready and i can grab the render path via the viewport in an eventcallback for begin_frame. But i am only able to change texture name.

    Viewport* overlayViewport = renderer->GetViewport(1);
    RenderPath * rp = overlayViewport->GetRenderPath();

    for ( int i = 0; i < rp->GetNumCommands(); i++ ) {
        RenderPathCommand *cmd = rp->GetCommand(i);
        if (cmd->type_ == RenderCommandType::CMD_QUAD) {
            cmd->SetTextureName(TextureUnit::TU_DIFFUSE, "texturename");
        }
    }

-------------------------

Eugene | 2018-03-14 10:59:29 UTC | #2

Add your texture as manual resource with some synthetic name to `ResourceCache`.

-------------------------

simonsch | 2018-03-14 11:00:51 UTC | #3

Thank you, you are an hero :). It is really hard to get into this, but for those who want some code
 
     auto *cache = GetSubsystem<ResourceCache>();
     cache->AddManualResource(yourtexture);

-------------------------

simonsch | 2018-03-14 14:20:34 UTC | #4

I have an additional problem now, i want to update that texture in each frame. Therefore i use the ->SetData() method and pass in the data of a opencv Mat. The texture gets updated, but it is flickering, i already tried different event callback. 

Is there any fast way to update the content of this texture in each frame?

-------------------------

Eugene | 2018-03-14 14:34:26 UTC | #5

Where do you call SetData?

-------------------------

simonsch | 2018-03-14 14:39:19 UTC | #6

I call

> cameraTexture->SetData(0, 0, 0, overlay.cols, overlay.rows, overlay.data);

in
> SubscribeToEvent(E_UPDATE, URHO3D_HANDLER(HelloGUI, HandleUpdate));

but also tried
> E_BEGINFRAME
> E_ENDFRAME

with same flickering result, texture resolution is fullscreen 1920 x 1080.

-------------------------

Eugene | 2018-03-14 14:57:44 UTC | #7

1. What's exactly "flickering"? I suppose 1/2 of all possible graphical bugs are "flickering".
2. Texture data is perfectly valid, isn't it? So if you e.g."dump" the texture somewhere, all images are fine.
3. What framerate do you have? If you reduce framerate (e.g. to 10 FPS via Sleep(100)), do you see this flickering?

-------------------------

simonsch | 2018-03-14 15:19:37 UTC | #8

@ 1. I know, i try to describe. It seems that the frames are not valid, like the frame is not complete as the next one appears.
@ 2. Maybe it will help you if i give you more context. I get a texture stream from a framework it is in an YUV NV21 format, i convert this to RGB via opencv and make the texture ready for rendering. So i think the error is there, i have this code
     
    cv::cvtColor(yuv, rgb, CV_YUV2RGB_NV21);
    cv::transpose(rgb, result);
    cv::flip(result, result, 0);
    cv::flip(result, result, 1);

It converts color space, rotates and vertically flips the image so it fits the screen. When i remove this conversion the flickering between the frames is gone, but of course the image itself is wrong. I don't understand how this conversion can cause this issues while rendering, as i only update the cv::Mat with the 'result' when everything is done. I should also say that i am in a different thread and head to set a mutex lock when writing to 'result'.

@3. Lowering the framerate had no effect, like said i think the error is caused by the conversion. 

Easiest way would be if i can directly push YUV through the texture, but as i saw only RGB formats are supported aren't they?

                cameraTexture->SetSize(overlay.cols, overlay.rows, Urho3D::Graphics::GetRGBFormat(), 
                                       TextureUsage::TEXTURE_STATIC);

Because this conversion could also be done in glsl shadercode.

EDIT:
I tryed a bit and moved the cv conversion part into the HandleUpdate() method, and now the flickering is gone, the but the fps dropped down noticeable. I think getting that YUV through shader would be great.

-------------------------

Sinoid | 2018-03-14 15:20:56 UTC | #9

If you don't need the pixel data yourself I'd flip your UV coordinates where you access the surface. Material param `VOffset` 0, -1, 0, 0.

-------------------------

Eugene | 2018-03-14 15:31:18 UTC | #10

[quote="simonsch, post:8, topic:4086"]
I think getting that YUV through shader would be great.
[/quote]

You could always write your own shader that do whatever you want.

Regarding your issue, you cannot call SetData while you are touching passed data, so they both shall be mutexed. Is it valid for you? OFC it's better to move everything into shader.

-------------------------

Sinoid | 2018-03-14 15:39:31 UTC | #11

If you move it into the shader you have to first figure out what type of YUV you're getting - YUV422, interleaved, U odd V quad, two-channel 16-bit interleaved, NvRG16, etc? As well as what you might get if cv is just giving you *raw* device data.

You can pass whatever through Texture::SetData as long as it fits the constraints of the texture format. It doesn't care about the *meaning* of the data, just that the layout is correct - so feeding it YUV that's 8-bits per components is okay if you're decoding in the shader.

-------------------------

simonsch | 2018-03-15 08:24:48 UTC | #12

Yeah i think that was issue, it now runs stable but slow. I know that about the shader but i need to get YUV into it as far as is saw i only can tell the urho texture to use an rgb format like -> Urho3D::Graphics::GetRGBFormat(). I am not sure how to create a texture sampler which holds that kind of data.

-------------------------

simonsch | 2018-03-15 09:49:11 UTC | #13

Hi :),

i think the exact format ist YUV NV21 (420sp) i am not sure how to handle these. So you say, that i should you use something like Urho3D::Graphics::GetFloat16Format() for YUV for the texture binding? 

In relation to your previous post

     flip your UV coordinates

i have only a texture no material and no xml. Any way to set this programmatically. I don't see a corresponding field in the documentation. Is there a way to use GL_TEXTURE_EXTERNAL_OES as target when urho calls glTexImage2D? I read this would make things easy with YUV.

-------------------------

Sinoid | 2018-03-15 16:52:24 UTC | #14

> i think the exact format ist YUV NV21 (420sp) i am not sure how to handle these. So you say, that i should you use something like Urho3D::Graphics::GetFloat16Format() for YUV for the texture binding?

NV21 is an 8-bit per component interleave. That requires an R8G8 format, which currently isn't supported so you'd have to modify the engine to support R8G8 formats. Because it's interleaved you're going to need to pass the texture size off to your shaders or through the vertex data you draw (ie. setting the uv coords there) so you know the domain for sampling - blame GLES2 for that (lacking `textureSize`).

> i have only a texture no material and no xml

You need a material even if it doesn't come from XML. If you're using your own shader through some explicit means then you have to do the UV coordinate transform in your shader.

VOffset and UOffset are shader parameters the material picks up. You set them through `void Material::SetShaderParameter(const String& name, const Variant& value)` so:

    material->SetShaderParamater("UOffset", Vector4(-1,0,0,0));
    material->SetShaderParamater("VOffset", Vector4(0, -1,0,0));

> Is there a way to use GL_TEXTURE_EXTERNAL_OES as target when urho calls glTexImage2D? I read this would make things easy with YUV.

No not easily. You'll have to modify the engine to hack it in. Since OpenGL is a bizarre mess it treats GL_TEXTURE_EXTERNAL_OES as a texture-type so that's probably going to be *fun*.

-------------------------

simonsch | 2018-03-21 15:14:34 UTC | #15

Hi
i finally was able to get this working. It was even more easy then i thought.
After creating the texture in cache i fetched the textureID. The framework i use was able to directly bind the camera image to this texture then.
In my shader code it was necessary to enable the extension for GL_TEXTURE_EXTERNAL_OES and then in was able to directly read rgb pixels from that sampler :slight_smile:.

Thy all for your great support!

-------------------------

Pencheff | 2019-08-19 13:01:12 UTC | #16

I just finished porting my video player to Android using MediaCodec, which also needs GL_TEXTURE_EXTERNAL_OES to render directly to surface (instead of having to copy the texture through CPU). 

For anyone who needs such texture in Urho3D in the future without hacking Urho's code:
[code]
class Texture2D_ExternalOES: public Texture2D {
  URHO3D_OBJECT(Texture2D_ExternalOES, Texture2D)
public:
  explicit Texture2D_ExternalOES(Context* context): Texture2D(context) {
    target_ = GL_TEXTURE_EXTERNAL_OES;
    autoResolve_ = false;
    multiSample_ = 0;
  }
  ~Texture2D_ExternalOES() override = default;
protected:
  // NOTE: Works fine without this but you will get an error 
  // "Failed to create texture" because Urho3D will try to glTexImage2D
  bool Create() override {
    Release();
    if (!graphics_ || !width_ || !height_)
      return false;

    if (graphics_->IsDeviceLost()) {
      URHO3D_LOGWARNING("Texture creation while device is lost");
      return true;
    }

    GLuint texture_id;
    glGenTextures(1, &texture_id);
    glBindTexture(GL_TEXTURE_EXTERNAL_OES, texture_id);
    glBindTexture(GL_TEXTURE_EXTERNAL_OES, 0);

    object_.name_ = texture_id;
    levels_ = 1;
    levelsDirty_ = false;
    parametersDirty_ = false;
    return true;
  }
};

// Example usage (same as Texture2D):
auto graphics = context->GetSubsystem<Graphics>();
texture_ = new Texture2D_ExternalOES(context);
texture_->SetNumLevels(1);
texture_->SetSize(graphics->GetWidth(), graphics->GetHeight(), Graphics::GetFloat32Format(), TEXTURE_DYNAMIC);
texture_->SetAddressMode(COORD_U, ADDRESS_CLAMP);
texture_->SetAddressMode(COORD_V, ADDRESS_CLAMP);
texture_->SetFilterMode(FILTER_ANISOTROPIC);
[/code]

-------------------------

