SteveU3D | 2017-03-06 09:28:48 UTC | #1

Hi,
I would like to create an application with Urho3D as engine and Scaleform to make the UI, but I can't find any documentation about that.
Has anybody already tried to use Scaleform with Urho3D? If yes, some help, documentation will be great! :slight_smile:
Thanks

-------------------------

TheSHEEEP | 2017-03-06 13:56:34 UTC | #2

The only thing I tried with Scaleform was registering to use it online. 
It asked for how many million $ the project budget was, so I lol'd and looked for an alternative...

-------------------------

Bananaft | 2017-03-06 14:06:27 UTC | #3

Scaleform is not cool anymore. UE moved from it. Flash is almost dead. And there is a stable decline in number of games using Scaleform since Autodesk bought it in 2011 (what a great investment strategy!): https://en.wikipedia.org/wiki/List_of_games_using_Scaleform

What do you need it for?

-------------------------

rku | 2017-03-06 15:15:35 UTC | #4

But is there alternative for scalable vector graphics UI?

-------------------------

Bananaft | 2017-03-06 15:34:51 UTC | #5

You can import vector graphics as flat 3d mesh. Scaleform does it at some point anyway.

-------------------------

TheSHEEEP | 2017-03-07 06:46:01 UTC | #6

CEF - https://bitbucket.org/chromiumembedded/cef  - It is basically having a browser renderer, which you can then take the results from and use as your UI. I don't think you can have more scalability and power than that. It is quite a lot of work to implement, though, and get it running with an engine. But: it's free and it is definitely doable.

There is also a commercial alternative to that, made specifically for games.
Afaik, they use cef internally, but changed it to have a better performance and be easier to use for games:
http://coherent-labs.com/product-coherent-ui/

-------------------------

rku | 2017-03-07 08:09:19 UTC | #7

CEF is cool, but support hardware-accelerated rendering for offscreen windows is limited. As seen in [this thread](http://www.magpcss.org/ceforum/viewtopic.php?f=8&t=11635&start=20) work was done some time in the past but patch was not maintained and was not merged. CEF without hardware acceleration is rather slow and we miss out on css3 transforms completely. Good example is slow UI of *planetary annihilation*. It really feels that i am browsing a website on IE6 instead of navigating game UI.

-------------------------

SteveU3D | 2017-03-07 08:24:31 UTC | #8

Thanks for your answers.
I want to create a UI for my application using Urho3D, and I found that Scaleform is (was?) used to do that with several game engines, so I decided to test it. And also because, as it uses flash, it seems easy to change animations, ... as you only have to change your swf files.
In fact, I managed to integrate Urho3D in a QML application (in a Window element) via the external window parameter, but the problem is that the Urho3D window appears above all QML elements so I can't create the UI in QML.

-------------------------

TheSHEEEP | 2017-03-07 08:24:18 UTC | #9

Yes, that is the one downside of it.
But if you manage you UI accordingly (not crazily copying an entire screen each frame ;) ), it isn't really much of a problem.
And Planetary Annihilation was confirmed to not be very clever about how they manage it, looking at some Steam complaints.

I would agree it is not the highest speed among UIs, but I'd argue that doesn't matter for the majority of games.

Oh, there is also NoesisGUI - http://www.noesisengine.com/ . I tested it some time go (when it wasn't even version 1).
It is rather quick and powerful, but for some extremely weird reason they chose WPF approach with XAML, which does not have any good editor and almost nobody knows how to code it well. While almost everyone can pull off JS/CSS/HTML ui. 
That and its lack of MinGW support caused me to drop it at the time.
I think it is very powerful, but I just won't commit to learning XAML, which is a world of its own.

-------------------------

SteveU3D | 2017-03-07 08:41:27 UTC | #10

OK! So finally, according to all those answers, I will hardly find documentation, examples, ... of Urho3D applications using Scaleform :sweat_smile:
I saw that it's possible to create basic UI elements in Urho3D (button, line edit, check box, ... https://urho3d.github.io/samples/02_HelloGUI.html) but is it possible (easy?) to really custom those elements as we want, and to add 2D animations as we could do with flash animations in Scaleform?

-------------------------

rku | 2017-03-07 08:55:58 UTC | #11

Sorry for continued offtopic but CEF seems to support hardware-accelerated offscreen rendering after all: https://code.google.com/archive/p/chromiumembedded/issues/1257

> The new implementation supports both GPU compositing and software compositing (used when GPU is not supported or when passing --disable-gpu --disable-gpu-compositing command-line flags). GPU-accelerated **features that did not work with the previous off-screen rendering implementation do work with this implementation when GPU support is available**.

@SteveU3D default UI is not animated. But in case you want to try your luck with CEF @Lumak made example how to integrate it with Urho3D: https://github.com/Lumak/Urho3D-CefIntegration

-------------------------

SteveU3D | 2017-03-07 09:04:53 UTC | #12

OK, I'll have a look at it, thanks!

-------------------------

