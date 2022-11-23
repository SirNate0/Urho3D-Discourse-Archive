thatonejonguy | 2017-01-02 01:05:25 UTC | #1

If possible, what would be the best approach for rendering a shadow *only* scenepass?

Thanks,
-Jon

-------------------------

cadaver | 2017-01-02 01:05:26 UTC | #2

It's pretty much hardcoded in the engine that shadows are calculated during additive per-pixel lighting. So you'll need to look into patching the View / RenderPath classes to support that scenario (as well as modifying shaders). Maybe make a new renderpath command, or add parameters to the existing ones (FORWARDLIGHTS in forward rendering and LIGHTVOLUMES in deferred)

-------------------------

thatonejonguy | 2017-01-02 01:05:27 UTC | #3

After looking through the shaders, I pretty much figured this to be the case. My goal was to get cheap softer shadows (shadow only pass to a bilateral blur pass), but I opted instead for extending the PCF to a user definable set of samples, which works ok for now. At some point, I might try to integrate PCSS, but that appears it will be no small task. Thanks for your reply.

-Jon

-------------------------

