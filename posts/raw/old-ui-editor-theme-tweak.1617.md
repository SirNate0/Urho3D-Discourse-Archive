rasteron | 2017-01-02 01:08:57 UTC | #1

Better late than never so I thought I'd share this old UI tweak that I did when I got started with the engine and playing around with it. This was done a couple of years ago with Urho 1.3 and during Google Group days. The interface was still simple back then with just the menu bar and a couple of windows. I did not bother to share it because it was not fully completed and was just meant for my own personal use. I also could not obtain the copy anymore because I recently found out that this was included with my failed hard drive, along with other old dev stuff but fortunately I found these 2 screenshots that I got inside my docs folder while I was doing my monthly file cleanup routine. The theme was inspired by dark theme engine editors like Unity Pro, CrySDK, UE4, etc.

If I have the time I would definitely redo this with an updated version, but I'm currently busy in completing a demo right now. I hope this should give you guys added motivation on what can be done with Urho3D's flexible UI system, though I would still prefer a C++ Qt library version for a solid editor and have the builtin UI just for in-game stuff.  :wink: 

cheers.  :smiley: 

[url=http://i.imgur.com/QyWXt87.jpg][img]http://i.imgur.com/QyWXt87l.jpg[/img][/url]

[url=http://i.imgur.com/0DslKtH.png][img]http://i.imgur.com/0DslKtHl.png[/img][/url]

-------------------------

Enhex | 2017-01-02 01:09:01 UTC | #2

Looks good.

BTW Qt isn't standard C++, and has awful requirements to build from source.

-------------------------

umen | 2017-01-02 01:09:01 UTC | #3

How do you embed SDL2 into Qt 5 widget ? and event loop this is a problem .

-------------------------

rasteron | 2017-01-02 01:09:03 UTC | #4

[b]@Enhex[/b]

[quote]Looks good.
BTW Qt isn't standard C++, and has awful requirements to build from source.[/quote]

Thanks. I'm not sure about Qt not being standard C++ and how it would relate in creating a replacement game editor, but any framework and libraries has pros and cons. You don't need to build Qt from source to create a decent working prototype and there's a lot of opensource Qt widgets that you won't find anywhere else or would take some time to develop.

As mentioned many times, Aster already created a Qt based Particle Editor for Urho3D..
[github.com/aster2013/ParticleEditor2D](https://github.com/aster2013/ParticleEditor2D)

[b]@umen[/b]

[quote]How do you embed SDL2 into Qt 5 widget ? and event loop this is a problem.[/quote]

[topic124.html](http://discourse.urho3d.io/t/urho3d-in-qt-hello-world/143/1)

-------------------------

