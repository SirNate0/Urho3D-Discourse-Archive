spwork | 2018-01-20 10:16:56 UTC | #1

When the game window loses focus, I plan to pause the game and suspend the background music. Is there an event that can let me know that the game window has lost focus?

-------------------------

Modanung | 2018-01-23 07:35:08 UTC | #2

`GetSubsystem<Input>()->HasFocus()` should do the trick.

-------------------------

Modanung | 2018-01-20 13:32:19 UTC | #3

If your application runs full screen `GetSubsystem<Engine>()->SetPauseMinimized(true);` should suffice, btw.

-------------------------

spwork | 2018-01-23 07:35:08 UTC | #4

thank you ,i find I`nputFocus` event can slove my problem.

-------------------------

Modanung | 2018-01-20 15:54:13 UTC | #5

Ah, right, there's even an event for that. :slight_smile:

-------------------------

