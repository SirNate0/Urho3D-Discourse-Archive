xalinou | 2017-01-02 01:12:51 UTC | #1

I've been looking for an Urho3D example showcasing the graphical features of the engine, but unfortunately, there's no such thing. It would be nice to have another example with things like:

[ul]
[li]SSAO[/li]
[li]MSAA, FXAA[/li]
[li]Parallax mapping[/li][/ul]

-------------------------

rasteron | 2017-01-02 01:12:52 UTC | #2

Krstefan42 already did an opengl version of Parallax Mapping, see here: [topic1196.html](http://discourse.urho3d.io/t/parallax-mapping-opengl-only-for-now/1158/1)

For FXAA, you can just enable it by checking the multiple viewports example. [post3416.html?hilit=fxaa#p3416](http://discourse.urho3d.io/t/how-to-use-post-effects/617/3).

-------------------------

1vanK | 2017-01-02 01:12:52 UTC | #3

msaa: set engine parameter "MultiSample" > 1

ssao:
[github.com/reattiva/r](https://github.com/reattiva/r)
another version [bitbucket.org/reattiva/sao-as/downloads](https://bitbucket.org/reattiva/sao-as/downloads)
[post3985.html](http://discourse.urho3d.io/t/ssao-on-ios/619/17)
but probably need to adapt for current version of engine

-------------------------

