victorfence | 2017-01-02 01:05:31 UTC | #1

I am busy integrate vuforia with urho3d (only for android by now)

This is so hard for me as a new bee. But I desired to see them working together.

I try to draw vuforia's camera background in urho3d's update event listener.

As below:

[code]
void Player::Start() {
  ...
  SubscribeToEvent(E_UPDATE, HANDLER(Player, HandleUpdate));
  ...
}

void Player::HandleUpdate(StringHash eventType, VariantMap& eventData) {
  QCAR::State state = QCAR::Renderer::getInstance().begin();

  //** 
  QCAR::CameraDevice& cameraDevice = QCAR::CameraDevice::getInstance();
  QCAR::VideoMode videoMode = cameraDevice. getVideoMode(QCAR::CameraDevice::MODE_DEFAULT);
  
  //**  Configure the video background
  QCAR::VideoBackgroundConfig config;
  config.mEnabled = true;
  config.mSynchronous = true;
  config.mPosition.data[0] = 0.0f;
  config.mPosition.data[1] = 0.0f;
  config.mSize.data[0] = 720;
  config.mSize.data[1] =1280;
  QCAR::Renderer::getInstance().setVideoBackgroundConfig(config);

  //** dont work, black window, dont't know why
  // QCAR::Renderer::getInstance().drawVideoBackground();

  //** get frame image
  QCAR::State state = QCAR::Renderer::getInstance().begin();
  ///QCAR::setFrameFormat( QCAR::RGB565, true );
  QCAR::setFrameFormat( QCAR::RGB888, true );
  QCAR::Frame qcarframe = state.getFrame();
  const QCAR::Image *imageRGB888 = NULL;
  for(int i=0; i<qcarframe.getNumImages();i++) {
    const QCAR::Image *pimg  = qcarframe.getImage(i);
    if (pimg->getFormat() == QCAR::RGB888) {
      imageRGB888 = pimg;
      break;
    }
  }

  //** found image, this works!!
  if (imageRGB888 != NULL) {
    __android_log_print(ANDROID_LOG_INFO, "Player", "found imageRGB888");
    const short* pixels = (const short*) imageRGB888->getPixels();
    int width = imageRGB888->getWidth();
    int height = imageRGB888->getHeight();
    int numPixels = width * height;

    //*** todo: draw image
    
    __android_log_print(ANDROID_LOG_INFO, "Player","888image size: %d %d", width, height);
  }

  QCAR::Renderer::getInstance().end();
}
[/code]

Some explain:
"drawVideoBackground" never working as offical demo, I saw only a black window.
google again and again, I found the camera frame image can be fetched.
So, my current question is:
how to display the buffered image as urho3d's background? (I wish that no need to modify urho3d's source code)

By the way, I'd like to see urho3d engine integerate vuforia in future :slight_smile:

-------------------------

cadaver | 2017-01-02 01:05:32 UTC | #2

You can insert a quad rendering command in the renderpath after clear and before the rendering commands, to make it draw a texture each frame before rendering the 3D scene. 

For example, a modified Forward.xml renderpath that would draw the mushroom texture:

[code]
<renderpath>
    <command type="clear" color="fog" depth="1.0" stencil="0" />
    <command type="quad" vs="CopyFramebuffer" ps="CopyFramebuffer">
        <texture unit="diff" name="Textures/Mushroom.dds" />
    </command>
    <command type="scenepass" pass="base" vertexlights="true" metadata="base" />
    <command type="forwardlights" pass="light" />
    ...
[/code]

To replace this with the video texture, you must create a Texture2D, set a name for it, for example "VideoTexture", add it to the resource cache as a manual resource (ResourceCache::AddManualResource()) so the renderpath can find it, and set the texture unit in the quad command as follows:

[code]
      <texture unit="diff" name="VideoTexture" />
[/code]

Now you can use SetData() on the Texture2D to upload the camera image data. I have no idea however what the performance will be on Android, when modifying (reuploading) the video texture every frame.

As for Vuforia integration, we only integrate fully permissive open source libraries with BSD / zlib -like licensing into the Urho3D base, so that rather falls for an external contributor, who creates a separate project ("Urho Vuforia integration" or something like that), and people can then use it if they agree with the licensing.

-------------------------

weitjong | 2017-01-02 01:05:32 UTC | #3

I have tried this integration before. The performance on Android is acceptable. My approach is similar to what have been outlined by cadaver.

-------------------------

victorfence | 2017-01-02 01:05:32 UTC | #4

Thanks for your reply, this saved me!!!
Followed cadaver's idea, I saw the camera video as background(seems good performance), it's so exciting :slight_smile:
And it's a very elegance idea I think. I like it.

The only problem is the video is 90 degree rotated, can you point me how to solve this?
Can I rotate the texture mapping or something else? How?

Code for uploading the camera image data:
[code]
  if (imageRGB888 != NULL) {
    const unsigned char* pixels = (const unsigned char*) imageRGB888->getPixels();
    int width = imageRGB888->getWidth();
    int height = imageRGB888->getHeight();
    //*** draw image
    image->SetData(pixels);
    bool result=mTexture->SetData(image);
  }
[/code]

-------------------------

cadaver | 2017-01-02 01:05:32 UTC | #5

You could make a copy of the CopyFramebuffer shader that samples the texture in a rotated fashion (faster), or make a rotated pixel buffer on the CPU before you SetData() to the texture (slower).

Normally texture scrolling / scaling / rotation would be controlled from material but renderpath quad commands don't use materials, only textures.

-------------------------

victorfence | 2017-01-02 01:05:35 UTC | #6

[quote]..make a copy of the CopyFramebuffer shader that samples the texture in a rotated fashion (faster)..[/quote]

I'v made my own CopyFramebuffer shader, this work like a charm, thanks :slight_smile:

-------------------------

