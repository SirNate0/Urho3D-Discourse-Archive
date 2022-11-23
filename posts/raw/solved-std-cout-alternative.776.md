syjgin | 2017-01-02 01:02:49 UTC | #1

I want to show some debug info to OS console during the application run. But, when I was trying it with std:cout, text appears only after the engine shutdown. But Log class is for file log, not console. How can I print debug message in Urho3D?

-------------------------

Mike | 2017-01-02 01:02:49 UTC | #2

You can use LOGINFO() or LOGWARNING() for this.

-------------------------

weitjong | 2017-01-02 01:02:49 UTC | #3

If you are following Urho3D development from master branch, it now supports a new build option to build Windows executable as console application. As console application, any log outputs and errors are flushed to the console immediately as the executable runs.

-------------------------

syjgin | 2017-01-02 01:02:55 UTC | #4

[quote="Mike"]You can use LOGINFO() or LOGWARNING() for this.[/quote]
Thanks, it works perfectly

-------------------------

