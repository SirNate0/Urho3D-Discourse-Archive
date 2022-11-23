DragonSpark | 2017-01-02 01:10:03 UTC | #1

Hello all,

I see that Urho3D runs on "Windows" but it would be nice to get clarification on this either in the info page and/or here:

Does this support mean traditional/legacy/non-store Windows?  Windows Store (Windows 8+) or both?

Thank you,
Michael

-------------------------

Calinou | 2017-01-02 01:10:03 UTC | #2

I guess it means traditional Windows (x86 and x86_64) support. I don't know whether Windows XP is supported, but Windows Vista and later should all work.

-------------------------

Stinkfist | 2017-01-02 01:10:04 UTC | #3

XP should also be still supported AFAIK.

-------------------------

globus | 2017-01-02 01:10:04 UTC | #4

Yes, Windows XP is still supported.
My workspace - XP, MinGW, OpenGL

-------------------------

DragonSpark | 2017-01-02 01:10:09 UTC | #5

WOW... XP is supported?!  Does this only use pre-.NET 4.5 or something?  Sorry, I'm being lazy and haven't actually checked it out yet... so many things to do before then. :slight_smile:

Also, it sounds like this isn't Windows Store-compatible, then?  It would be nice to have this as well.  Anyways, when I finally get the chance to check it out I will update this thread with my official findings.  :smiley:

-------------------------

Stinkfist | 2017-01-02 01:10:09 UTC | #6

Supporting XP and Windows Store are not mutually exclusive. However, I don't think Store build is supported currently out of the box. Urho is implemented in C++ so it has no .NET requirements whatsoever. For UWP information, see [topic1724.html](http://discourse.urho3d.io/t/windows-10-uwp-support/1659/1).

-------------------------

