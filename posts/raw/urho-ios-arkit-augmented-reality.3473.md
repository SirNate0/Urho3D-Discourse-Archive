Egorbo | 2019-05-23 13:20:02 UTC | #1

Apple introduced a very powerful AR toolkit in iOS11 called ARKit. So I'd love to share my sample using UrhoSharp and ARKit :slight_smile: 
The code is simple and can be easily "backported" to C++ if you want: https://github.com/EgorBo/ARKitXamarinDemo
![D2zxJC4|300x202](upload://3JikXrfGrp1jz4iJNBEAiiFtIH4.jpg)
Videos:
https://www.youtube.com/watch?v=KSZtvq_iGoE
and
https://www.youtube.com/watch?v=BdEIetc4rHU

ARKit is able to detect movements and planes (I will add "plane (ARPlaneAnchors) visualization" later).
There were some challenges:
1) NPOT textures on iOS (hey guys, let's add ES3 support together :slight_smile) 
2) YUV to RGB
3) Render video instead of clear color 
4) Shadows on a transparent surface

-------------------------

godan | 2017-08-22 00:49:24 UTC | #2

Thanks for this! Do you have any thoughts on how one would go about writing the C++ version? I'm pretty comfortable with the Urho side of things, but how does ARKit fit in? How do I go about linking in ARKit and getting, say, the registered surfaces?

-------------------------

Egorbo | 2017-08-22 01:07:28 UTC | #3

it should be strait forward.
1) Add ARKit framework (just like other frameworks such as AVFoundation are added somewhere in makefiles)
2) Create an ARSession, run and listen to events (didUpdateFrame, etc..) Here is how it looks like in C#: https://gist.github.com/EgorBo/71d66993e40fec32987b7f00e2ff734c 
translate code from C# to C++ in [ArkitApp.cs](https://github.com/EgorBo/ARKitXamarinDemo/blob/master/ARKitXamarinDemo/ArkitApp.cs#L125-L204) - should not be difficult

And don't forget you will need:
1) A9 ios device (iphone 6s or better)
2) iOS 11
3) XCode 9
both iOS11 and XCode 9 are betas.

-------------------------

