GIMB4L | 2017-01-02 00:58:07 UTC | #1

Hey guys,

I've noticed that when running two copies of the same thing, whichever one is in focus gets more updates. I'm aware this might be a Windows thing, but does Urho have some sort of throttling when it's not in focus?

-------------------------

cadaver | 2017-01-02 00:58:07 UTC | #2

See Engine::SetMaxInactiveFps(). It's separate from the main FPS limiter setting (Engine::SetMaxFps()). Set both to 0 for no FPS limiting either way.

-------------------------

GIMB4L | 2017-01-02 00:58:07 UTC | #3

Alright, thanks!

-------------------------

