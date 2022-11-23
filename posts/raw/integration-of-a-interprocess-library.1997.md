christianclavet | 2017-01-02 01:12:10 UTC | #1

Hi, It would be really nice to have applications or games running on multiple windows/screens. Since URHO can only support one context per application, the only solution that I would see fit would be to integrate ways to have a main application launch client application and interact between these process.

We could use the network as a start, but I would prefer to have a direct communication between apps.

I've seen there are some interprocess libraries that could facilitate the work a lot (cppremote, boost, d-bus). I know barely nothing on this, I will look how its done and will try to seek for a tutorial about this, but it would be nice that URHO would have this ability and a little example (could be similar as the network example). This would also help the EDITOR have sub-editor modules to expand its capability. (Model Editor, Particle/FX editor in separate windows that communicate with the main window)

Thanks.

-------------------------

cadaver | 2017-01-02 01:12:10 UTC | #2

Probably the easiest would be to add a cross-platform (separate Windows and Unix implementations) named pipe class, that could be read and written to like a file. Adding a new library could be overkill.

However note that in case of a "sub-editor" you would be loading the resources multiple times, resulting in heavy memory use, so in an ideal case I wouldn't recommend that approach.

Moving a graphics context between windows might not be impossible, however Urho's frame loop is not well-fitting to multiple window rendering, since it does first a separate render update, then a render later. Unifying the render-update and render operations would be preferable for this (also to prevent situations like scene destruction between update & render resulting to a crash), however it could lead to performance loss or subtly break applications which rely on the current behavior.

Also, if we had actual multiple windows support, then we'd also have to consider multiple window input, which could cause larger scale API changes, so the IPC approach (though wasteful) is still the easiest to get running.

-------------------------

christianclavet | 2017-01-02 01:12:11 UTC | #3

Thanks for the inputs about this. I'll do a check on how I could create and use a [b][i]pipe class[/i][/b] myself. One of my friend mentioned also using [b][i]signals[/i][/b] is there advantage using one from the other or they are completely different things?

-------------------------

cadaver | 2017-01-02 01:12:11 UTC | #4

Signal means just "something happened", so using a pipe gives more possibilities to implement an arbitrary communication protocol.

-------------------------

cadaver | 2017-01-02 01:12:29 UTC | #5

Simple nonblocking birectional named pipe class has been added to master branch.

-------------------------

