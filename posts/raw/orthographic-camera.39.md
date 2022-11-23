friesencr | 2017-01-02 00:57:33 UTC | #1

I am working on the editor.  I am trying to add orthographic camera support but I the camera is not acting the way i would expect.  

I do something simple like this:
[code]camera.orthographic = !camera.orthographic;[/code]

The camera movement seems very odd.  Is there something else that needs to be set to make it behave more normal?

Thanks,
Chris

-------------------------

cadaver | 2017-01-02 00:57:33 UTC | #2

If you mean that normal backward/forward movement seems to disappear, that is expected, as there's no more perspective, so it only appears as if the near/far clipping planes move through the world.

Possibly the control scheme needs to change so that in ortho mode WASD moves the camera on its local X & Y axes.

-------------------------

