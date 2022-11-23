TheComet | 2017-01-02 01:13:03 UTC | #1

I haven't tried this yet, but for a multi-player game I'm hoping to be able to start a second Urho3D context in headless mode to act as the server, to which the currently running Urho3D context can connect to as a client (all in the same process).

Is this possible? Are there any potential pitfalls that I will run into? E.g. what happens when both try writing to the log file? Are the worker threads shared or will there be 2x more worker threads? etc.

Another idea I had was to start the server in a child process.

-------------------------

cadaver | 2017-01-02 01:13:03 UTC | #2

There once was support for multi contexts, but some snags were always encountered (I think this was window event handling related) so now there is no official effort or promise that it works.

However you don't need that just for running a local server. The client and server parts of Network subsystem are logically separated and it should be possible to run and use both at the same time. Just have a strong separation in your own application code, have separate client / server scenes etc. and remember you only have 1 main thread for both server & client. Since multi contexts could never share resources or worker threads you will actually save on memory and CPU use this way.

-------------------------

