btschumy | 2020-10-05 15:29:11 UTC | #1

What is the recommended way to detect double clicks (or taps) in the ViewPort?  Currently I'm detecting touch begin, moved and ended like this (sorry, this is in C#)

			Input.TouchBegin += OnTouchBegan;
			Input.TouchMove += OnTouchMoved;
			Input.TouchEnd += OnTouchEnded;

Do I have roll my own looking at the time of the TouchBegan events?

-------------------------

Lys0gen | 2020-10-05 16:25:20 UTC | #2

UI elements have the *E_UIMOUSEDOUBLECLICK* event that you could utilize, for everything else you would probably have to code the handling yourself.

-------------------------

btschumy | 2020-10-05 23:24:42 UTC | #3

I have no UI elements in the app.  So unless anyone else has a suggestion, I will code it myself.

I suppose I could place a transparent UI element in the positions where I want to detect the double click.  Seems kind of hokey though.

-------------------------

dev4fun | 2020-10-05 23:08:52 UTC | #4

https://github.com/urho3d/Urho3D/pull/2566

-------------------------

