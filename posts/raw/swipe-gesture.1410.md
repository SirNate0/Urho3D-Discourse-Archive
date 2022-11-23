sabotage3d | 2017-01-02 01:07:33 UTC | #1

Hi guys,
Is there a way to recocgnize a swipe gesture with Urho3d ? Ideally I want to use it for character movement to recognize forward, backward, left and right movement.

-------------------------

friesencr | 2017-01-02 01:07:33 UTC | #2

SDL has support for some runtime configurable gestures.

[hg.libsdl.org/SDL/file/default/ ... gesture.md](https://hg.libsdl.org/SDL/file/default/docs/README-gesture.md)

Our SDL might be too old for that api.  I have never been interested in mobile so i don't have lots of info.

-------------------------

Mike | 2017-01-02 01:07:33 UTC | #3

Check Touch input / gestures [url=http://urho3d.github.io/documentation/1.4/_input.html]documentation[/url].
It works great  :slight_smile:

-------------------------

