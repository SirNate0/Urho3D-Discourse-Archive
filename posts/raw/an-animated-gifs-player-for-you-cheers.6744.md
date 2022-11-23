DinS | 2021-03-03 03:28:34 UTC | #1

While I am working on a project with Urho3D, I have found there's no built-in way to play animated gifs, so I write my own. Since this is a general problem, I'd like to share my work with the community. 

1. Overview
In the zip file, which can be found at the end of this post, there're 5 files.
The AnimatedGif.h/cpp defines a new type of Resource. It uses [hidefromkgb's gif_load.h](https://github.com/hidefromkgb/gif_load) (public domain C library) to decode the gif. 
The FrameAnimation.h/cpp defines a new type of component. It uses AnimatedGif to play the animation.

2. Usage
(1) copy the files under the same folder and add to your project. If you want to place them separately, change the #include accordingly.
(2) register the types before use, for example in the constructor of your application, write
AnimatedGif::RegisterObject(context);
FrameAnimation::RegisterObject(context);
(3) code as if they are Urho3D built-in types. For example:
//Setup 2D Scene...
auto pPic = _gameScene->CreateChild("test_gif");
pPic->SetPosition2D(0, 0);
auto pFrAni = pPic->CreateComponent< FrameAnimation >();
auto pGif = GetSubsystem< ResourceCache >()->GetResource< AnimatedGif >("Data/Urho2D/test.gif");
pFrAni->SetGif(pGif);

Check this gif for result. Each time I click the button, a new gif will be created.
![DemonGif|690x406](upload://azei6n7EWzqX1m8WF436vQzIDli.gif) 
(browser may show the gif slower than normal)

3. Notice
(1) if the gif is large, consider doing a backgroundloading with resource cache first. 
(2) MSVC user: since it uses a C library, you may need to change IDE grammar check from C++ to C.
(3) MSVC user: there're a lot of comments in CHINESE, which is my mother tongue. They are mostly about background knowledge on the media format, rationale and C library usage. If you just want to play a gif, don't bother. But you need to change the encoding from UTF-8 to UTF-8 BOM, or else MSVC will output strange errors. Personally I think it's a flaw in the compiler. Apple Clang and g++ don't have this issue. Another way is to just remove all comments.

4. Download
The forum doesn't allow zip file uploading, so I have put the file on my website for your access.
https://dins.site/wp-content/uploads/2021/03/gif-addon.zip

The codes are released under MIT license. 
Hope this can help some people in the future.
Cheers! :grinning:

-------------------------

George1 | 2021-03-03 10:12:57 UTC | #2

If I remember correctly, there was a gif texture mapping written by some one..  Maybe see Lumak examples. It might have that.

-------------------------

