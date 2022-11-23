DinS | 2021-03-03 03:37:14 UTC | #1

While I am working on a project with Urho3D, I have found there’s no built-in way to play video, so I write my own. Since this is a general problem, I’d like to share my work with the community.

1. Overview
In the zip file, which can be found at the end of this post, there’re 5 files.
The MpgVideo.h/cpp defines a new type of Resource. It uses [plmpeg](https://github.com/phoboslab/pl_mpeg) (MIT license C library) to decode the mpg.
The VideoPlayer.h/cpp defines a new type of component. It uses MpgVideo to play the video.

The problem with video playback is that decoding takes a lot of time and memory space.
For a 1280 X 900 mpg video that lasts 18 seconds, which is pretty common, it will take several seconds to fully decode, and the fully decoded video frames will take 1280x900x3x30x18 = 1780MB! :scream:
So here comes the idea of streaming. Only decode when we need a new frame, aka decode as you watch(`). Throw out played frames to keep memory small, aka discard as you watch(``). Streaming makes the code neat and keeps performance high. 

` This is true ONLY IF you have a powerful CPU. the CPU needs to decode video frame to raw pixel, format it to Urho3D::Sprite2D, and show it on screen within one Urho3D::Update. The good news is that you can expect it to work for modern CPU.
`` The code achieves this by not keeping the Sprite2D in resource cache. BUT after rendering on screen, the render will hold a SharedPtr to the resource, so it can't be released automatically. To solve this check this [post](https://discourse.urho3d.io/t/dynamic-loaded-sprite-leaks-memory/6149/3). Also see discussion below.

2. Usage
(1) copy the files under the same folder and add to your project. If you want to place them separately, change the #include accordingly.
(2) register the types before use, for example in the constructor of your application, write
MpgVideo::RegisterObject(context);
VideoPlayer::RegisterObject(context);
(3) code as if they are Urho3D built-in types. For example:
//Setup 2D Scene…
auto pPic = _gameScene->CreateChild(“test_mpg”);
pPic->SetPosition2D(0, 0);
auto pCom = pPic->CreateComponent< VideoPlayer >();
auto pMpg = GetSubsystem< ResourceCache >()->GetResource< MpgVideo >("Data/video/test1.mpg");
pCom->SetMpg(pMpg, 1.0f);

Check this demon video.
https://dins.site/wp-content/uploads/2021/03/DemonVideo.mp4
On the left side, you can see that before the video, CPU is about 30%, memory is about 40MB. While playing video CPU goes up to 80%, memory stays at 60MB. Using the code directly won't get you there. The memory will not be freed. See discussion below.


3. Discussion
To completely remove a rendered resource from memory, I changed the Render2D class. As pointed out in this [post](https://discourse.urho3d.io/t/dynamic-loaded-sprite-leaks-memory/6149/3),  I added an UncacheTexture method, and remove cachedMaterials_ accordingly. But from my experience I found this is not enough. Also need to call viewBatchInfos_.Clear() to completely wipe out SharePtr< Material >. 
But I'm not sure if this is the proper way to do this. I hope someone can answer my doubt. That is how to completely remove a rendered resource from memory?
Since this modification is not standard Urho3D, I commented out the codes in VideoPlayer. And that's the reason you will not see memory released if you use the code directly.

4.Notice
(1) if you want to predecode the video and save in cache, you need to come up with your own way.
(2) the mpg file needs to be MPEG1 video and MP2 audio. You can use ffmpeg to convert file format. check pl_mpeg site for detail.
(3) MSVC user: since it uses a C library, you may need to change IDE grammar check from C++ to C.
(4) MSVC user: there’re a lot of comments in CHINESE, which is my mother tongue. They are mostly about background knowledge on the media format, rationale and C library usage. If you just want to play an mpg, don’t bother. But you need to change the encoding from UTF-8 to UTF-8 BOM, or else MSVC will output strange errors. Personally I think it’s a flaw in the compiler. Apple Clang and g++ don’t have this issue. Another way is to just remove all comments.

5.Download
The forum doesn’t allow zip file uploading, so I have put the file on my website for your access.
https://dins.site/wp-content/uploads/2021/03/mpg-addon.zip

The codes are released under MIT license.
Hope this can help some people in the future.
Cheers!

-------------------------

vmost | 2021-03-03 04:06:07 UTC | #2

Could you get new frames in a separate thread? Then sync the video frame rate with game frame rate by matching frame expected-time with real-time. Seems like a fun project.

-------------------------

SirNate0 | 2021-03-03 05:20:37 UTC | #3

Thanks for the contribution!
Also, I thought I'd point out that there is a way to play Theora videos with code here, though it certainly isn't part of the engine itself.

https://discourse.urho3d.io/t/theora-video-playback/2144/14?u=sirnate0

-------------------------

DinS | 2021-03-03 14:42:45 UTC | #4

The code here is a lightweight version. In fact what I am using in my project is a smart video player. That is it can determine how many frames to decode in advance according to CPU powerful, decode in a different thread and sync with the engine. But that uses std::thread and std::chrono. So I'd like to keep things simple here.

-------------------------

