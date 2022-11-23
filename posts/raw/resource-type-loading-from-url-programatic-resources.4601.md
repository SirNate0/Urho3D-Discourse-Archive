Pencheff | 2018-10-21 16:25:22 UTC | #1

I have successfully implemented a video player inside Urho3D that can play video/audio files from file, url, video capture devices such as webcam or DVB tuners. Everything works fine, however, I am trying to integrate the video player as Resource, so it can be loaded by the ResourceCache, possibly like this:
[code]
auto video = cache->GetResource<Video>("video.avi");
[/code]

This I've done easily by implementing a custom resource which overrides BeginLoad()/EndLoad().

The problem is, when I try to load custom url that the video player supports, for example **"device://camera0"** or **"rtsp://url.../"**, the ResourceCache tries to resolve that as file on the disk and then passes it as Deserializer in BeginLoad() and since such file doesn't exist, loading fails.

**The question**: Am I trying to use the ResourceCache in the wrong way ? Should it be used only for actual file loading and parsing ?

-------------------------

Sinoid | 2018-10-23 03:29:45 UTC | #2

Devil's advocate: isn't a streamed file a bit questionable since a stream is more state than anything else. It's not really a constant resource.

-------------------------

Pencheff | 2018-10-23 21:10:04 UTC | #3

![HJOoPhW|690x334](upload://knxOKZAjvRKOwKF1henpsEZhzMX.png) 
This is fine with me, I can use whatever string in video source.

When playing an audio file, the audio content is provided as Resource. When playing a video file, I assume video could also be a Resource.

When playing video from video capture device (camera), the camera could be viewed as Resource. It does not exist as an actual file on the file system, however it provides content that comes from a constant source.
Is this assumption wrong ?

-------------------------

jmiller | 2018-10-24 09:03:45 UTC | #4

A tangential discussion may shed some light.
https://discourse.urho3d.io/t/resource-path-urls/1440

-------------------------

Pencheff | 2018-10-24 10:24:20 UTC | #5

Thank you for this reference, I've missed that particular thread.

Just some thoughts following ....
In my previous engine implementation which used Ogre3D, I had my own resource cache system called AssetSystem with some interesting features - caching, routing and async loading. It consisted by AssetProviders (file system, pak file system, http). When requesting an asset, every AssetProvider was getting queried if it handles such a request. I was able to do things like this:
[code]
assetsystem->RegisterProvider(new VideoDeviceProvider());
// The VideoDeviceProvider will handle device:// requests
auto camera_asset = assetsystem->Get<CameraAsset>("device://camera0");
[/code]
The VideoDeviceProvider class was handling "device://" requests and returning "programatic assets".
As messy it was, I could load an asset from file, http url and capture device.

I don't want to change the way the current ResourceCache works, I could implement a similar subsystem with Urho3D as an addition. I could also be totally wrong on whole "Resource" idea :)

-------------------------

Modanung | 2018-10-24 11:02:01 UTC | #6

[quote="Pencheff, post:3, topic:4601"]
When playing an audio file, the audio content is provided as Resource. When playing a video file, I assume video could also be a Resource.
[/quote]

But a video _stream_  would be more like a `SoundStream`, which is _not_ a `Resource`.

-------------------------

