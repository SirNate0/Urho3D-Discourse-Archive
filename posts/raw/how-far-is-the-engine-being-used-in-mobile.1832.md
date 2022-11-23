mcosta | 2017-01-02 01:10:30 UTC | #1

Hi guys

we are starting to use Urho and it looks great! 
As we move on we our tests we are stumbling in a few things, tough. For example, Galaxy S6 is rendering black, which is a bit weird for a top device that is out for more than 1 year. Another thing, we were trying to copy texture bytes to a buffer and it seems it is not possible. GetData complains "with not support" error

cheers
Manuel

-------------------------

cadaver | 2017-01-02 01:10:31 UTC | #2

Getting texture data back to CPU is not supported in the same way on OpenGL ES 2 as on desktop GL. Haven't fully investigated workarounds for that though.

Urho has certainly been used for mobile projects, but especially in Android mobile use, which is generally regarded as a nightmare of hardware compatibility or driver issues even by professional devs, it's safest to interpret the MIT license pessimistically regarding what it says of warranties for fitness of purpose (= there are none.) We may not have means to debug a bug on a specific device unlike commercial engines, which have their test farms. So in practice it works best if a user encountering a problem on specific device can contribute a fix, then everyone benefits.

-------------------------

mcosta | 2017-01-02 01:10:31 UTC | #3

Guys 

after UrhoSharp announcement, Urho3d immediately jumped into our radars. We are working on version 2.0 of Storyo, a mobile app developed in c# through Xamarin. We can find following links two possible outputs that we have today:

1 - 2D like - [vimeo.com/102913389](https://vimeo.com/102913389)

2 - 3D - [vimeo.com/157421323](https://vimeo.com/157421323)

We are currently trying to build a 3D player of stories based on Urho and, of course, getting texture data is crucial to encode videos.
As for Android and hw compatibility, yes we know it well! :slight_smile:

cheers
Manuel

-------------------------

boberfly | 2017-01-02 01:10:32 UTC | #4

Hello,

A possible workaround is to use glReadPixels, it'll cause a massive bubble in the CPU/GPU pipeline though. I had a mode where you can take a photo of the screen and it paused the screen for a solid 1 second on Android and iOS (probably because the GPUs on there are heavily pipelined, more so than desktop GPUs).

There are extensions and EGL ones too which can get around this, but it's all different on every hardware, I don't recommend that rabbit hole... :slight_smile: ES 3.x fortunately supports Pixel Buffer Objects which can probably get around this quite well.

I'm rendering to an S6 here, I've found that it renders for like 2 seconds and freezes the frame, and I need to use the task manager to go to another app, then back to Urho and then it works fine. I recommend you try this (I haven't investigated the solution yet). Once SDL 2.0.4 lands I also have ES 3.x patches to apply, which I've tested on an S6.

-------------------------

mcosta | 2017-01-02 01:10:32 UTC | #5

cadavar just implemented it [url]https://github.com/urho3d/Urho3D/commit/6538f3bb4a6ae6906b9f52d01bed8317102db709[/url]
To have a better notion of what can be causing issues like the one we've been experiencing in Galaxy S6 (rendering black), can you guys give us a direction where to search for it? It "smells" to an issue with a shader used by the engine.

-------------------------

Modanung | 2017-01-02 01:10:33 UTC | #6

[quote="mcosta"]To have a better notion of what can be causing issues like the one we've been experiencing in Galaxy S6 (rendering black), can you guys give us a direction where to search for it? It "smells" to an issue with a shader used by the engine.[/quote]
I've run into Linux machines where the FXAA3 shader wouldn't compile. Which caused a black screen (except for 2D UI elements). Not appending it to the effect RenderPath solved the problem then.

-------------------------

Vincentwx | 2017-01-02 01:10:41 UTC | #7

I am learning game programing using UrhoSharp(C# wrapper library from Xamarin). So far everything worked great on Android for me.

-------------------------

