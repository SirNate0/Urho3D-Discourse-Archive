Mike | 2017-01-02 01:05:44 UTC | #1

I'm experimenting an issue with camera farClip on Android.
For example in sample 11_Physics, if I set Z position for the cubes above 130 then the pyramid doesn't show up (farClip is set to 500 in this sample).
Is this a hardware limitation and/or is there a way to fix this?

-------------------------

cadaver | 2017-01-02 01:05:44 UTC | #2

This is possibly limited depth buffer precision.

Right now I believe the OpenGL setup (Graphics::SetMode() in OGLGraphics.cpp) does not force any requirements for the depth buffer with OpenGL ES, due to the fear of failing completely if the hardware doesn't support it. You could try adding some depth bits setting, for example 16 or 24, and recompiling.

The code in question starts at about line 400, note how it's ifdef'd out for GLES:

[code]
        #ifndef GL_ES_VERSION_2_0
        SDL_GL_SetAttribute(SDL_GL_DEPTH_SIZE, 24);
[/code]

-------------------------

Mike | 2017-01-02 01:05:45 UTC | #3

Many thanks for super-fast reply.
I've put the line just before the ndef and tested with 24, 16, 8 and 4 depth size.
Unfortunately it has no effect  :unamused:

-------------------------

gabdab | 2017-01-02 01:07:58 UTC | #4

Did you find a solution so far ?

-------------------------

Mike | 2017-01-02 01:07:58 UTC | #5

EDIT: Fixed by this [url=https://github.com/urho3d/Urho3D/commit/92a080d68b4e69012af074e3d6ee06a35c809460]commit[/url], thanks cadaver.

-------------------------

