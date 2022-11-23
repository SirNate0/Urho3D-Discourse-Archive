Jens | 2021-12-07 20:53:49 UTC | #1

Hi - Does anyone know of a way to figure out the world space position of the screen edges, ie top and left, which does not invoke ScreenToWorldPoint()?

-------------------------

Modanung | 2021-12-07 21:06:16 UTC | #2

Why *not* `ScreenToWorldPoint()`?

-------------------------

Jens | 2021-12-07 21:21:42 UTC | #3

Ah, this is where it gets weird. The game starts with a blank screen menu with text. Up until the menu is removed (menu task finished), ScreenToWorldPoint() returns an incorrect x position of -2, when it should be -1.28 (the y position is correct in all cases). Once the startmenu is removed then the correct position is returned. I cannot explain this; there seems to be nothing in startmenu that could cause the error. 

I am developing in C# (sorry!), and this behaviour can be reproduced in the 'SamplyGame' project, which is a Urhosharp example game.

-------------------------

1vanK | 2021-12-08 07:16:49 UTC | #4

 https://github.com/urho3d/Urho3D/issues/1504

-------------------------

Jens | 2021-12-08 10:01:13 UTC | #5

Ok, it seems the ScreenToWorld() works ok. The problem is the camera, specifically the projection matrix is altered from the incorrect (square screen) values (M11=2.41, M22=2.41) to the correct value M11=3.87, M22=2.41.
Why the matrix is altered just by closing the 'menu' task, is a mystery to me. It is also a mystery as to why the correct values are not there from the get go. Maybe not a mystery to someone else?

-------------------------

Jens | 2021-12-08 12:33:52 UTC | #6

A workaround for this was to wait until the camera projection is correct, then build the scene using ScreenToWorld().  This works, so I guess there is no point continuing this topic.

-------------------------

