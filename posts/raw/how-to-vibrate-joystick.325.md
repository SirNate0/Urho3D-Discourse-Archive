rifai | 2017-01-02 00:59:38 UTC | #1

My game requires joystick controller.  I need my joystick vibrate when my character hit something. 
Does Urho3D have this feature?

-------------------------

rasteron | 2017-01-02 00:59:38 UTC | #2

Hey rifai,

Yes, it is possible since the engine uses SDL, you can use SDL functions to incorporate your own vibrate functions in your code then extend it by Scripting API.

Reference here:

[wiki.libsdl.org/CategoryForceFeedback](https://wiki.libsdl.org/CategoryForceFeedback)

Hope that helps.

-------------------------

