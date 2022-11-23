k7x | 2022-04-13 17:12:15 UTC | #1

There is something that I do not understand and cause misunderstanding. 
Please explain how to use open source software. 

Here is my project page : [mgs3r](https://github.com/flcl8193/mgs3r) 

Where do I put the urho3d license files for this to be correct? 
Same thing with the ffmpeg codec license.

-------------------------

1vanK | 2022-04-13 18:39:28 UTC | #2

I didn't find Urho3D sources in your repository. If you are not copying files from the Urho3D project into your project, then you do not need to place Urho3D license in your repository.

-------------------------

k7x | 2022-04-13 20:37:23 UTC | #3

Yes, it is more convenient to compile Urho3D separately. In the source code, of course, the API is used. But for the release section, what should I do when urho3d is statically linked? Should I copy the LICENSE file to the root or ... And yet, I beg you to clarify about ffmpeg. I read the license and come to the conclusion that it is better not to use it at all. It is not very clear what, where and why. Need to play mpeg-2 game video. It's also important to ask. Here's a situation where I don't need all the source code. And even that doesn't suit me. Let it be Urho3D and its resource manager (for example). Here I take a certain part of the code, change it, and embed it in the project. That is, there is only a certain meaning. How can I be in such a situation. Thank you.

-------------------------

1vanK | 2022-04-13 23:28:31 UTC | #4

Game "Notia" for example just have folder with licenses of all used libraries

![1|626x500](upload://smbjZiG9XEGJ70WEKpOWP4pjFOG.png)

-------------------------

SirNate0 | 2022-04-14 13:27:49 UTC | #5

Another fairly common approach is to have a section in an About section of the menu. For example, this is the section in Shattered Pixel Dungeon
![Screenshot_20220414-092236|234x500](upload://cPxI22BgPJe9HiVBrayTnewVIHR.png)
and you'll find Android's under About phone > Legal information > Open source of the system settings.

If you don't want to deal with a viewer in the game, though, I would say distributing it in a zip file or installer that adds a licenses folder would be sufficient. Or even just list them in the license file for your game.

-------------------------

Nerrik | 2022-04-14 14:16:17 UTC | #6

Firefox is a good sample too. "about:license" in firefox adresstab or "help->over firefox"

-------------------------

k7x | 2022-04-14 14:36:05 UTC | #7

Thank you. 
I will definitely add a license to the game menu, mention uhro3d and gratitude. 
But there is a question. 
I read about the GPLv2 license (it licenses the mpeg2 decoder that I need). 
And it says that my project must be open source and that it must be under the same license. 
And I, like Urho3d, already have MIT. 
I understand correctly that I can not use this library? 
Or without distributing the source code in my project (the user has to download and copy it himself) can I do it with libmpeg2 ?

-------------------------

S.L.C | 2022-04-14 15:21:46 UTC | #8

With GPL you only need to release the source if you link statically. But if you use dynamic linking (DLL/SO) and the user can replace that DLL with their own then you don't need to release your sources.

The other case is when you modify the GPL protected code. In that case, even if you release a dynamic library (DLL/SO) you have to also distribute (*or at least open source and probably mark them*) your changes to the GPL protected code. At least that's what I recall reading on it.

You can do static linking with Urho and only use dynamic linking with the library that has the more strict license. But IIRC Urho itself does not include any third-party library that is not compatible with the MIT license.

-------------------------

1vanK | 2022-04-14 16:15:25 UTC | #9

[quote="k7x, post:7, topic:7234"]
I will definitely add a license to the game menu, mention uhro3d and gratitude.
[/quote]

urho3d also uses many libraries <https://github.com/urho3d/Urho3D/blob/master/Source/ThirdParty/LICENSES>

-------------------------

