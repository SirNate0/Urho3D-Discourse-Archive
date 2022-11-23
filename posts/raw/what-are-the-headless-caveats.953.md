practicing01 | 2017-01-02 01:04:23 UTC | #1

Hello, my current project runs fine unless I specify -headless at start, then it segfaults at the first SetViewport().  Before I start changing code, I need to know what other possible problems may occur with -headless.  Thanks for any tips.

-------------------------

cadaver | 2017-01-02 01:04:23 UTC | #2

The basics are:

- Graphics subsystem does not exist (nullcheck before use)
- Renderer subsystem does not exist (nullcheck before use)
- Material and texture resources only fake their loading. Model resources will operate in a CPU-only mode so that you can still do raycasts to triangle data.
- Sound sources fake their playback by advancing their time position, but don't actually render any audio
- Because there are no cameras / viewports in use to determine viewing position, LOD distance can't be used in animation, and therefore skeletal animations update each frame and so may take more CPU time. On the other hand it doesn't have to calculate skinning or upload anything to GPU.

-------------------------

