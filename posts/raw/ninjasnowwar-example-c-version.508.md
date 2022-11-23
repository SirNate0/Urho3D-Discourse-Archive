sabotage3d | 2017-01-02 01:00:56 UTC | #1

Hello,
Is there NinjaSnowWar example in C++ ? 
I think the example is really good but I am am more comfortable with C++ rather than using scripting language. 

Thanks,

Alex

-------------------------

thebluefish | 2017-01-02 01:00:56 UTC | #2

Currently, NinjaSnowWar is only done through the scripting. Angelscript-to-C++ conversion is very straight-forward, so I can whip up an example sometime this week if you would like.

-------------------------

Mike | 2017-01-02 01:00:57 UTC | #3

In the meantime you can check scorvi's port at [url]https://github.com/scorvi/Urho3dNinjaGameExample[/url].

-------------------------

sabotage3d | 2017-01-02 01:00:58 UTC | #4

Awesome thanks a lot :slight_smile:

-------------------------

thebluefish | 2017-01-02 01:00:58 UTC | #5

I have most of it translated from Angelscript to C++. I'll have a completed example for you sometime tomorrow, and I'll make sure it's playable with people using the Angelscript version, too.

-------------------------

sabotage3d | 2017-01-02 01:01:00 UTC | #6

Is it going to work on mobile ?

-------------------------

thebluefish | 2017-01-02 01:01:00 UTC | #7

It is a direct port, so whatever mobile support exists in the original NinjaSnowWar will be ported too. However I am unfamiliar with the Android build process, so it will be untested.

Had an unexpected problem with my work PC. Took all day to get a new one, and it's going to take me the better part of tomorrow morning to get it ready for development. I'm aiming for tomorrow, though it might be Monday when I am able to finish it up.

-------------------------

sabotage3d | 2017-01-02 01:01:00 UTC | #8

Thanks , I am working only on IOS for the moment.

This one kind of works [github.com/scorvi/Urho3dNinjaGameExample](https://github.com/scorvi/Urho3dNinjaGameExample) but it has a lot of bugs.
And I cannot get the Urho3d logging and debug information for some reason.

-------------------------

scorvi | 2017-01-02 01:01:12 UTC | #9

hey, 
sorry for my bad and incomplete implementation :-/ i lost my interest and did not finish it ... 

how is it going with your implementation thebluefish?

-------------------------

thebluefish | 2017-01-02 01:01:13 UTC | #10

We moved to a new office and my computer somehow died in the process. It's going to be a pain to setup my build environment before we're settled in, so all of my projects have been halted (not just Urho3D related, but my source of income on the side as well). This has not been a good week for me unfortunately.

Most of the base is there. There are several event handlers that have not yet been converted, but everything except the Ninja (aka the player) is mostly functioning. When my system is back up and running, it will only take me another day or two.

-------------------------

