rku | 2017-01-02 01:13:15 UTC | #1

How (if) can i render a stack of scenes one on the other? Having multiple viewports covering entire screen turns out does not do this at all. I think clearing z buffer is needed after each scene is rendered too.

-------------------------

cadaver | 2017-01-02 01:13:15 UTC | #2

Has been discussed a few times on the forum already. Indeed, use another viewport, and a customized renderpath that only clears depth but not color.

-------------------------

jmiller | 2017-01-02 01:13:15 UTC | #3

One such thread with code: [topic1749.html](http://discourse.urho3d.io/t/how-to-best-generate-an-in-game-hud/1684/1)

-------------------------

jmiller | 2017-01-02 01:13:15 UTC | #4

Ah, here's the one I remember:

How to Layer Scenes
[topic756.html](http://discourse.urho3d.io/t/how-to-layer-scenes/740/1)

-------------------------

rku | 2017-01-02 01:13:16 UTC | #5

thank you
[code]<command type="clear" depth="1.0" stencil="0" />[/code]
did just that :wink:

-------------------------

