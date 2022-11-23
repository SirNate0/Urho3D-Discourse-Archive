DragonSpark | 2017-01-02 01:08:23 UTC | #1

Hello,

I just found out about this project here:
blog.xamarin.com/3d-game-engine-for-android-ios-and-net/

Looks cool. :slight_smile:

Given that the reference came from Xamarin, I was expecting to see Xaml here... but that doesn't appear to be the case.  Is this framework based on Xaml and if not... are there plans to make it so?

Thank you for any insight/assistance,
Michael

-------------------------

jenge | 2017-01-02 01:08:23 UTC | #2

We consulted with Xamarin about Urho3D after they licensed Atomic.

Glad for the additional exposure this has yielded :slight_smile:

- Josh

-------------------------

alexrass | 2017-01-02 01:08:23 UTC | #3

[quote]targeting Android, iOS, Mac, tvOS, and Windows[/quote]
linux not supported  :frowning:

-------------------------

DragonSpark | 2017-01-02 01:08:23 UTC | #4

This is looking like a "no." :stuck_out_tongue:

twitter.com/migueldeicaza/status/672191419075985408

I would be interested in checking this out and maybe helping with make this happen?  Sounds like there is already a UI system, just need to wire it up w/ Xaml serialization? :slight_smile:

-------------------------

DragonSpark | 2017-01-02 01:08:23 UTC | #5

FWIW, I am also interested in this project, which has Xaml UI, but in alpha.  It would be cool to somehow combine the two:

[www.youtube.com/watch?v=NJ9-hnmUbBM](http://www.youtube.com/watch?v=NJ9-hnmUbBM)

-------------------------

1vanK | 2017-01-02 01:08:24 UTC | #6

[quote="alexrass"][quote]targeting Android, iOS, Mac, tvOS, and Windows[/quote]
linux not supported  :([/quote]

[nuget.org/packages/UrhoSharp/](https://www.nuget.org/packages/UrhoSharp/)
UrhoSharp is a lightweight Game Engine suitable for using with C# and F# to create games that run on Android, iOS, Mac, Windows and Unix.

-------------------------

alexrass | 2017-01-02 01:08:24 UTC | #7

I download urhosharp.1.0.237.nupkg and what i see: Android, iOS, Mac, Win64.
Better Urho3D + AngelScript )))

-------------------------

migueldeicaza | 2017-01-02 01:10:08 UTC | #8

[quote="alexrass"][quote]targeting Android, iOS, Mac, tvOS, and Windows[/quote]
linux not supported  :frowning:[/quote]

Linux should work, there is nothing specific about UrhoSharp that limits it.

The NuGet package on the other hand is complicated.   NuGet is not really designed to support native libraries, so we would only be able to produce a single binary that works on a single Linux distribution.

The real fix is to get the upstream NuGet system to support the needs of Linux, that way we could deliver a NuGet that could work on various Linux distributions.

-------------------------

