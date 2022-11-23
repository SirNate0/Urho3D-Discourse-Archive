rbnpontes | 2017-01-02 01:14:56 UTC | #1

Hello Guys, i have tried to make a Tool for make a Roads and Rivers in my Editor
My Question is, when i generate a Mesh, my code works fine but the faces is show inverse, how to solve this error ?
PS: I tried to invert a Normal but doesn't work
/* Sorry for my english */
[spoiler][img]http://i.imgur.com/rGJsNN7.png[/img][/spoiler]
[spoiler][img]http://i.imgur.com/8utvu2r.png[/img][/spoiler]

-------------------------

1vanK | 2017-01-02 01:14:56 UTC | #2

[quote="rbnpontes"]
PS: I tried to invert a Normal but doesn't work
[/quote]

It is strange...

Another way - you can change order of  vertices from clockwise to counter clokwise (or vice versa, I do not remember) instead change CalcNormal() function

Or just make doublesided material

-------------------------

Dave82 | 2017-01-02 01:14:56 UTC | #3

You could change the indices order to flip the normal.

-------------------------

rbnpontes | 2017-01-02 01:14:57 UTC | #4

Thank's Guys, i have changed order of Faces, instead of Clockwise, i'm put in Counter Clockwise

-------------------------

