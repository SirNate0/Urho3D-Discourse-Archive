btschumy | 2020-10-27 21:35:35 UTC | #1

I need to display a "degree" character in a Label in UrhoSharp.

On iOS, the character º works fine (type Option-0).  When the app is run on Windows I get a "?" in its place.  

The Windows degree character is /00B0 but that also displays a "?" in UrhoSharp.  I tried using the Windows "Character Map" application and copied the degree character from there.  It also displays "?" when the app is run.

Anyone know how to do this on Windows?

-------------------------

Modanung | 2020-10-26 19:23:29 UTC | #3

Could it be font-related? It should be the same character when using the same font, right?

-------------------------

btschumy | 2020-10-26 19:14:42 UTC | #4

I think that should be the character code for all fonts that have the glyph.  I'm using Helvetica so that should be pretty standard.

-------------------------

Modanung | 2020-10-26 21:35:29 UTC | #5

Well, there's also things like ASCII/bitmap fonts.

I guess it's a matter of the - usual - blaming Windows and using a superscripted o.<sup>o</sup>

-------------------------

btschumy | 2020-10-26 23:13:56 UTC | #6

Ugh!  But Urho3D should handle arbitrary Unicode strings when creating Labels, right?

-------------------------

Modanung | 2020-10-27 02:08:34 UTC | #7

Well, it does - or does it? (Not sure about the technical reach of "arbitrary unicode") - just not on Windows.

I know Urho *can* display Arabic, but does it bad; it requires string reversing and character map pasting for it to form words. Have you tried [Klingon](https://www.evertype.com/standards/csur/klingon.html)? That's should be about as *arbitrary* as it gets.

-------------------------

btschumy | 2020-10-27 14:17:12 UTC | #9

Is there any markup for superscripting, or do you have to display two labels appropriately placed, one with the number and one with the raised "o".

-------------------------

weitjong | 2020-10-27 14:39:54 UTC | #10

[quote="btschumy, post:6, topic:6460"]
But Urho3D should handle arbitrary Unicode strings when creating Labels, right?
[/quote]

Yes, it is. But whether a glyph is rendered correctly or not depends on the TTF you use. Have you tried with other TTF? On Linux I have tried the TTF that is used in the HelloWorld example, changing the last exclamation character to the degree (U+00B0), and it is rendered correctly. I know it is not tested on Windows, but I just don't see it will make any difference in this case.

-------------------------

btschumy | 2020-10-27 16:43:03 UTC | #11

What TTF is used in the HelloWorld example?

I have tried using the built-in CoreAssets.Fonts.AnonymousPro
I've copied the following .ttf files from my c:\Windows\Fonts directory.  arial.ttf, symbol.ttf

None of these seem to work.  Only ASCII characters can be displayed (0x7E is the last that works).  Anything above it yields a ?

This may be a Windows glitch.  On iOS, I have no problem displaying it's degree symbol.

-------------------------

Modanung | 2020-10-27 17:38:22 UTC | #12

[quote="btschumy, post:11, topic:6460"]
What TTF is used in the HelloWorld example?
[/quote]

It think it would be more helpful if you taught yourself how to deduce this. :fishing_pole_and_fish:

[quote="btschumy, post:11, topic:6460"]
On iOS, I have no problem displaying it’s degree symbol.
[/quote]
How about other characters that would otherwise produce ?s?

I don't use proprietary software, with the exception of [nVidia drivers](https://www.youtube-nocookie.com/embed/iYWzMvlj2RQ?autoplay=true); I'm not the one to dive into this issue.

-------------------------

btschumy | 2020-10-27 18:08:25 UTC | #13

Although I'm relatively new to Urho3D, I've spent a huge amount of time rummaging in the code trying to figure out how to do things do to the meager documentation.  I'm well aware how to find this out.  Here's the relevant code from HelloWorld

    // Set String to display
    helloText->SetText("Hello World from Urho3D!");

    // Set font and text color
    helloText->SetFont(cache->GetResource<Font>("Fonts/Anonymous Pro.ttf"), 30);
    helloText->SetColor(Color(0.0f, 1.0f, 0.0f));

So as I mentioned above, I have tried CoreAssets.Fonts.AnonymousPro.  It does not work.  Using the same code on iOS, it does.  So it seems to be a Windows problem.

-------------------------

1vanK | 2020-10-27 18:31:05 UTC | #14

No problems on Windows

![Рисунок|641x500](upload://pLFNGOsIFwTbOgld8eMf1SSOG6w.png) 

P.s. Use UTF-8 encoding for your source files

-------------------------

btschumy | 2020-10-27 18:55:42 UTC | #15

The files already are UTF-8 but that shouldn't matter in this case.  I'm encoding the character as "\u00B0" rather than typing it in directly.

I'm surprised it is working for you.  That might implicate UrhoSharp as the problem.  Perhaps something is lost in the bindings.

-------------------------

1vanK | 2020-10-27 21:34:53 UTC | #16

[quote="btschumy, post:15, topic:6460"]
UrhoSharp
[/quote]

UrhoSharp is dead. Try rbfx

-------------------------

btschumy | 2020-10-27 19:04:22 UTC | #17

Microsoft doesn't think it is dead.  It is the basis of their HoloSharp effort.  I have 4 months of work with UrhoSharp.  It will take more than a faulty degree character to make me switch.

I have looked into rbfx and it doesn't integrate well with Xamarin Forms.

-------------------------

1vanK | 2020-10-27 19:06:33 UTC | #18

The last commit was two years ago https://github.com/xamarin/urho

-------------------------

Modanung | 2020-10-27 19:24:55 UTC | #19

[quote="btschumy, post:17, topic:6460"]
Microsoft doesn’t think it is dead.
[/quote]

Ok... *undead* maybe. :zombie: 

https://discourse.urho3d.io/t/urhosharp-community/5388

-------------------------

Modanung | 2020-10-27 19:44:57 UTC | #20

It'll be stuck in the past as long as you do not revive it yourself.

And taking _Microsoft_ for their word? *How?* :confused:

-------------------------

Modanung | 2020-10-27 21:35:50 UTC | #21



-------------------------

