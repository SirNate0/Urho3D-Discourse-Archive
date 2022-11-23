nergal | 2017-12-18 14:28:37 UTC | #1

I'm using OSX and I got some strange issues with keyboard/mouse capture. Totally random, they are captured or not. When they are not captured my application doesn't get any inputs.
I bind to events such as this:

    SubscribeToEvent(E_KEYDOWN, URHO3D_HANDLER(Game, HandleKeyDown));

I'm don't have much to go on, but it works from time to time with just restarting the application without recompiling.

Perhaps some issues with OSX? Perhaps others have equal issues?

-------------------------

Victor | 2017-12-18 14:45:17 UTC | #2

I've had a similar issue with OSX where if I move the mouse, or interact with other apps before the application loads, all input doesn't seem to work until I select another window and then go back to the game window. I've seen this happen outside of Urho as well, which leads me to believe it's an OSX issue. Not really random, just seems like Mac doesn't register input for the app until you re-select the window.

-------------------------

nergal | 2017-12-18 14:46:24 UTC | #3

Ah I see, I will test a bit more if that's the case.

-------------------------

