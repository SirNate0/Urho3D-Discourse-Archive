Vincentwx | 2017-01-02 01:09:19 UTC | #1

I learned this great 3D game engine from project UrhoSharp by Xamarin. I had zero game programming experience, but I am very impressed after I tried those samples in C# (I do LOB application, moved from C++, MFC to C# a long time ago). I am just wondering if the team has a plan to support Windows 10 UWP platform. Personally, I think UWP has a great potential for this game engine.

-------------------------

cadaver | 2017-01-02 01:09:19 UTC | #2

Welcome to the forums.

Urho uses SDL2 as the operating system abstraction layer, so Urho can use whatever it supports. There is a pull request in the pipeline for SDL2.0.4 update. That said, we don't have a  specific Windows RT maintainer, so I wouldn't count on things necessarily working out of the box, once the SDL update is in.

-------------------------

migueldeicaza | 2017-01-02 01:09:20 UTC | #3

I just checked, and it looks like SDL is getting UWP support.

We might be able to assist with some issues that crop up with UWP.

-------------------------

NiteLordz | 2017-01-02 01:09:20 UTC | #4

i have been using Urho3D for a while on UWP, although required a few tweaks to the system.  First off, if you wish to use the XAML swap chain panel, you need to create an abi abstraction layer to pass the platform window to urho3d.

SDL 2.0 out of the box does not support the XAML swap chain, however, it does support native c++ application.  Utilizing the XAML swap chain, you can create a Windows 10 application, and have Direct3D rendering in the background or whatever you want.  

If you have any issues/questions with the UWP system, i can also assist on it.

-------------------------

DragonSpark | 2020-04-21 22:56:08 UTC | #5

[quote="NiteLordz"]
i have been using Urho3D for a while on UWP, although required a few tweaks to the system.  First off, if you wish to use the XAML swap chain panel, you need to create an abi abstraction layer to pass the platform window to urho3d.
[/quote]


Awesome!  This is encouraging.  I am definitely interested in exploring this further.  To be sure, I am interested in hosting in both legacy Windows and UWP, ensuring maximum market reach.  To start with, can you expand on what you mean by Xaml Swap Chain Panel (link would be great)?  Is there a Xaml system for Urho3D?  From what I understand, [url=http://discourse.urho3d.io/t/xaml/1544/1]there is no Xaml support[/url], so it would be nice to see that there is one. :slight_smile:

-------------------------

NiteLordz | 2017-01-02 01:10:16 UTC | #6

Concerning the SwapChainPanel, it is a XAML control just like Button, or TextBlock, but it handles Direct3D HW rendering, link to class object is here [msdn.microsoft.com/library/wind ... s/hh702626](https://msdn.microsoft.com/library/windows/apps/hh702626)

Currently, i use an extended version with the AccuWeather - Weather for Life application on the WIndows 8/10 platforms.  That is where the weather animations take place, however, it is not integrated with Urho3D, as i have a few things to do before i complete phase.

As for the integration with Urho3D, i removed use of SDL, and handle the windowing system on my own, since this was a big issue involving the Windows Store ecosystem, since they handle input in a different manner.  So there is a wrapper class, the main template application from VS, and the wrapper class, written in .NET takes the swap chain panel, and wraps all the input methods, so when invoked, send messages to the input subsystem, similar to the win32 system.  

Since the engine had already abstracted much of the input, all that was needed was to send those messages from each platform subsystem, to the input system.  

Hope this helps, if you need to see some code, let me know, and we can discuss further.

-------------------------

Vincentwx | 2020-04-21 22:56:24 UTC | #7

[quote="migueldeicaza"]
I just checked, and it looks like SDL is getting UWP support.

We might be able to assist with some issues that crop up with UWP.
[/quote]

With today's Xamarin + Microsoft great news, I truly believe UWP support, including C# binding, is coming soon....

-------------------------

weitjong | 2017-01-02 01:10:22 UTC | #8

Sorry for being off topic. But I would rather see a Swift binding than C# binding  :wink: . C# for UWP and Swift for the rest of world.

-------------------------

Vincentwx | 2017-01-02 01:10:24 UTC | #9

[quote="weitjong"]Sorry for being off topic. But I would rather see a Swift binding than C# binding  :wink: . C# for UWP and Swift for the rest of world.[/quote]

I am OK with "C# for UWP and Swift for the rest of world" since C# got the rest of the world already  :slight_smile: I am a Windows phone(Lumia 640XL) user, but cannot try this engine on my own phone. To learn and play with it, I had picked up an android phone to use. BTW, I published my learning game project "Jet Show"  to google play store.

[play.google.com/store/apps/deta ... wx.JetShow](https://play.google.com/store/apps/details?id=com.vincentwx.JetShow)

It's a very simple one, may not even be a game to anyone else except myself.

Anyway, thanks for the great engine, good job, well done.

-------------------------

gwald | 2020-04-21 22:58:03 UTC | #10

Hi gang,
I just found out about the Xbox One Dev Mode
https://www.youtube.com/watch?v=PNJYw4jEwhA
[wakeupandcode.com/build2016-xbox/](http://wakeupandcode.com/build2016-xbox/)

It basically, turns any retail XBox One into a UWP device and you can target it via VS 2015 community edition.
info:
[developer.microsoft.com/en-us/w ... getstarted](https://developer.microsoft.com/en-us/windows/games/getstarted)
[developer.microsoft.com/en-us/w ... wp-on-xbox](https://developer.microsoft.com/en-us/windows/windows-apps/uwp-on-xbox)


You need a DevCenter license (19USD once off) and the xbox is limited in UWP dev mode.
IMO still it's pretty good of MS to do this!
[img]https://pbs.twimg.com/media/CiLJAeYWwAAsZe6.jpg[/img]

I"m not interested in using C#, but good to know others have gotten UWP working  :mrgreen:

TMK, Sony doesn't have an 'indie' friendly platform, requiring a business to apply for indie  :smiling_imp:  :unamused:

-------------------------

JimSEOW | 2017-07-07 11:31:56 UTC | #11

Hi @Vincentwx  we are rebooting Win 10 ARM and Win 64 in preparation for WinOnArm Q4 2017. Stay tune

-------------------------

JimSEOW | 2017-07-07 16:04:20 UTC | #12

@NiteLordz I am comparing UWP XAML interop options for C# using SwapchainPanel for SharpDX, OpenGLES (Angle.WindowStore) and UrhoSharp. 

In your view, what need to be done to bring the official Urho3D to be compatible FIRST with Win 10 X64 and Win10 ARM (since WinOnARM is coming Q4 2017). 

Great you seems to make difficult thing works.

-------------------------

NiteLordz | 2017-07-07 16:26:06 UTC | #13

The way i implemented UWP supported for Urho3D (C++) was not using SDL, as SDL did not support swap chain panel, it only supported it as a native direct3d application (which is fine, if you don't want to integrate it into an actual application). To bring support to urho3D using swap chain panel, the SDL library needs to be updated to support it, OR, you have to create a seperate method for handling input from the UWP side (not difficult, most is already supported within SDL).  Other tweaks, are inside Urho3D, in Direct3D 11 pipeline, need to add support for creating a swap chain that uses SwapChainPanel (not difficult).  These modifications, will enable Urho3D to render inside a UWP application. Now, to get full support for UWP, the AngelScript library needs to enable support for W10M ARM, which it currently does not support.  I have worked with Angel on multiple occasions, but we have not been able to crack that egg to get it working yet. If you want to see the Urho3D player i created for UWP, i can package them up in a zip file, is nothing special, just a wrapper for the most part.

-------------------------

JimSEOW | 2017-07-07 16:36:19 UTC | #14

@NiteLordz Thanks for sharing. I have read many of your mails on AngelScript and why it is blocking Win10M ARM.

I am kind of die hard W10M user and the coming WinOnARm give me hope. 3D for me is key to visualization of complex data for AR, more than just game. 

There are not many options for C# .NET XAML interop. I have tested SharpDX UWP XAML interop. (porting from C++ template), the existing SharpDX nuget is not compatible with the Insider Biuld 10.0. 15086. Without enough people having interest, it is very slow to sort out challenges as a community. 

I also looked at OpenGLES UWP XAML interop using Nuget Angle.WindowStore. It seems fine, but again, it will be great to have more people using it. 

====> thanks for your feedback. Now I understand better the challenges XAMRIN has to do to Make UrhoSharp works in Xamarin.Forms (XAML) for UWP. 

=> I wish there are many like you to push these challenges. I guess XAML is of no priority to game communities. Wrong place to ask these requests :-(

-------------------------

JimSEOW | 2017-07-07 16:38:07 UTC | #15

Thanks for a deeper insight, I have to read more to fully get a clearer idea. thanks for the offer.

-------------------------

Vincentwx | 2017-07-07 17:24:13 UTC | #16

Hi @JimSEOW , so sad to say that I have left Window phone and moved on to Android. Without so many actions and announcements from Microsoft in the past year, I don't hold any hope for Win Mobile on ARM any more.

-------------------------

JimSEOW | 2017-08-22 13:43:41 UTC | #17

There is now renew interest for Andromeda OS from Microsoft. It is expected to address multiple mobility form factors (for Ultramobile PC).

The release 1.7 now fixes RPi and ARM build and also support C++ 11 and 64 bit for MinGW.
https://urho3d.github.io/releases/2017/08/19/urho3d-1.7-release.html

DO you think, the limitation you encountered before is addressed in the release 1.7?

-------------------------

smellymumbler | 2017-10-29 17:02:27 UTC | #18

Has anyone managed to get Urho3D running on UWP?

-------------------------

