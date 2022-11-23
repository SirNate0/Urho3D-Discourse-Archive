NemesisFS | 2017-01-02 00:57:39 UTC | #1

Hi,

the "game" I want to try and develop will have 2D Gameplay. Nevertheless I`d like to use Urho3D as the engine, for learning purposes.
Should I expect to run into problems because of rounding (ie after normalizing vectors) which could get bigger and bigger? If that is the case what would possible solutions be?

EDIT: I just recognized the Urho2D branch, I guess there is being worked on 2D physics. Do you know when it will be merged in the master branch?

-------------------------

cadaver | 2017-01-02 00:57:39 UTC | #2

You will get about 6 significant digits of precision from floats, so in very large game worlds the accuracy problem will manifest as you go further away from the origin.

For rock solid 2D physics calculations (tiled platformer etc.) for arbitrarily sized worlds you could use integers or fixed point internally and only convert to float for rendering.

-------------------------

