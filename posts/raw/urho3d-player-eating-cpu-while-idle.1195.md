sabotage3d | 2017-01-02 01:06:00 UTC | #1

Just a general question but I noticed the Urho3d Player is eating quite bit of my CPU while idle . I am just running the Editor while doing something else and I noticed some slugishness, is that normal ?
[img]http://i.imgur.com/qW1RIjO.png[/img]

-------------------------

friesencr | 2017-01-02 01:06:00 UTC | #2

Yup.  Nothing is caching the ui and nothing is stopping it from running full blast.  You can enable vsync to mitigate some of the problem.

-------------------------

weitjong | 2017-01-02 01:06:01 UTC | #3

This is one of the FAQ. I suppose we need to have FAQ section  :wink:

-------------------------

sabotage3d | 2017-01-02 01:06:01 UTC | #4

Thanks for the info.

-------------------------

jmiller | 2017-01-02 01:06:01 UTC | #5

You can also use the console [F1] to limit the FPS:  engine.maxFps = <FPS>

-------------------------

