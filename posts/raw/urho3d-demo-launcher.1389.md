rasteron | 2017-01-02 01:07:24 UTC | #1

Hey guys,

I thought I'd shared this simple Demo Launcher Utility (Windows Only) to help first-time users conveniently try out all the demos and at the same time a handy utility for regular scripters.

[b][u]What Works:[/u][/b]
- Select and launch a demo script, close, rinse and repeat.
- Player window starts maximized and resizable.
- Resolution dropdown scans your top graphic card resolutions only (starting from 1024px width range, not yet fully operational).

To include Lua at this time, just move it up in Scripts directory. I kept it minimal for this release but obviously there's more to dos.

Just place this where Urho3DPlayer resides. It will scan only the 'Scripts' directory and generate a list and then after selection, it just shell executes this pattern "Urho3DPlayer.exe Scripts/" %selection% " -w -s". 

Some of the options are not yet applicable at the moment because this was originally a game launcher template (UI derived from Unity) that I created a year ago and so have decided to put it to some good use here.

[img]http://i.imgur.com/o7AyZ7y.png[/img]

[b]Download Link:[/b] [b][url=http://rasteron.itch.io/urho3d-demo-launcher]rasteron.itch.io/urho3d-demo-launcher[/url][/b]

Enjoy! :slight_smile:

-------------------------

1vanK | 2017-01-02 01:08:36 UTC | #2

My implementation. The same, but open source xD

[github.com/1vanK/Urho3D-Samples-Launcher](https://github.com/1vanK/Urho3D-Samples-Launcher)

[img]https://cloud.githubusercontent.com/assets/13021826/11763249/b4aa61b8-a11c-11e5-9264-02ac3cd8c868.png[/img]

-------------------------

namic | 2017-01-02 01:08:36 UTC | #3

Very nice! Thank you. Now we can port it to Linux. :slight_smile:

-------------------------

rikorin | 2017-01-02 01:08:37 UTC | #4

I thought Linux users prefer to use terminal instead of gui :slight_smile:

-------------------------

