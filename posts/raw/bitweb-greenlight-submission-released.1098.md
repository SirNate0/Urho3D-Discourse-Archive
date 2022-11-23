practicing01 | 2017-01-02 01:05:27 UTC | #1

[store.steampowered.com//app/375220?beta=0](http://store.steampowered.com//app/375220?beta=0)

Feel free to report any bugs (especially on windows, I didn't test there).

-------------------------

rasteron | 2017-01-02 01:05:27 UTC | #2

Hey, congrats practicing01!

-------------------------

weitjong | 2017-01-02 01:05:27 UTC | #3

Congrats!

-------------------------

GoogleBot42 | 2017-01-02 01:05:28 UTC | #4

:smiley: Great! I will be sure to check it out. :wink:

-------------------------

cadaver | 2017-01-02 01:05:28 UTC | #5

Congrats on getting to Steam! On Windows, the game started in a quite small window in windowed mode, don't know if that was the intention (there was no title / option screen)

-------------------------

vivienneanthony | 2017-01-02 01:05:28 UTC | #6

It looks nice. Congrat.

-------------------------

thebluefish | 2017-01-02 01:05:28 UTC | #7

[quote="cadaver"]Congrats on getting to Steam! On Windows, the game started in a quite small window in windowed mode, don't know if that was the intention (there was no title / option screen)[/quote]

The parameters when I built the Windows build:
[code]
engineParameters_["WindowWidth"] = 800;
engineParameters_["WindowHeight"] = 600;
engineParameters_["WindowResizable"] = true;
[/code]

Maybe we could have a little more polished system for easy setup, like the Ogre3D examples.

-------------------------

cadaver | 2017-01-02 01:05:29 UTC | #8

A resolution dialog like in Ogre examples needs native (operating system) UI widgets, which e.g. SDL doesn't provide, so it would not be "cost-effective" to implement: Ogre for instance has an implementation for each desktop OS. Furthermore, just like the Unity resolution dialog, it would look "cheap" if you started seeing it in multiple games. I'd suggest making a proper in-game resolution menu, though it's a bit of work.

-------------------------

