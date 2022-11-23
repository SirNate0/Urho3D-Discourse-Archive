entretoize | 2019-06-08 08:36:35 UTC | #1

Hello, I'm using urhosharp with xamarin, and trying to build an Android app, but my problem is that I don't find a method to set the orientation to portrait. I can turn the camera but, for example the debug text is still in landscape mode.
Is it something in Urho3d or android side ?

Thanks

-------------------------

Leith | 2019-06-08 10:57:59 UTC | #2

hi! unfortunately this is the wrong forum to ask questions about the c# fork - thats a separate project and although i would love to help you, I'm yet to build one android project on Urho so I am utterly unqualified, other than to tell you that you are barking up the wrong tree for help with c# stuff here. This forum is dedicated to the master fork, which has no C# support. Still happy to help if there is any crossover but it looks like you are asking in the wrong place.

-------------------------

entretoize | 2019-06-08 11:41:54 UTC | #3

Ok, sorry I'm a bit lost each time to find where I can find help.
Thank you anyway.

-------------------------

weitjong | 2019-06-08 12:06:39 UTC | #4

Never use Xamarin before but otherwise the default orientation for Android app in general is set in the Android manifest file.

-------------------------

entretoize | 2019-06-09 07:59:57 UTC | #5

Yes you're true, I needed to change `ScreenOrientation = ScreenOrientation.Landscape` to `ScreenOrientation = ScreenOrientation.Portrait` in `MainActivity.cs` :

-------------------------

Modanung | 2019-06-10 07:46:04 UTC | #6

To me it seems the choice is as follows:
Use Urho3D and get help whenever you like here _or_ use UrhoSharp and wander the realm of ignorance.

-------------------------

