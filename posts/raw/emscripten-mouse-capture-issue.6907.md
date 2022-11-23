nickwebha | 2021-07-04 19:51:48 UTC | #1

Urho3D is having trouble keeping the mouse locked in Emscripten builds. When the (invisible) mouse cursor reaches the edge of the screen it just stops moving further. The result is, in my 3D game, the user can only turn so far in either direction or look up or down so far in either direction.

I have tried the different mouse modes with different results, none of them allowing complete free look.

Here is [an example](https://simpletanks.lifebloodnetworks.com/) (only works in Chrome right now).

I am using Emscripten 2.0.8 because anything newer will not compile Urho3D.

-------------------------

Miegamicis | 2021-07-04 20:12:45 UTC | #2

https://github.com/urho3d/Urho3D/pull/2634 Mouse capture improvements can be found in this PR but there are still some minor issues with it.

-------------------------

