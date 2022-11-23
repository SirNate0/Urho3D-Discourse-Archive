Sunc | 2022-04-11 06:02:42 UTC | #1

Is multithreading supported on web platform?

-------------------------

SirNate0 | 2022-04-11 14:48:52 UTC | #2

Yes, though I'm not sure the engine takes advantage of it (though there's not much Urho code that can take advantage of it because the graphics related code has to be done on the main thread).

Here's some information about how to get it working:
https://emscripten.org/docs/porting/pthreads.html

-------------------------

