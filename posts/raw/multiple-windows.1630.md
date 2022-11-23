atai | 2017-01-02 01:09:05 UTC | #1

Hi, does Urho3d 1.5 support rendering into multiple OS-level windows (for example, multiple X11 Windows on GNU/Linux)?

-------------------------

thebluefish | 2017-01-02 01:09:05 UTC | #2

I dabbled in this a bit ago. [url=https://github.com/urho3d/Urho3D/pull/765]Even submitted a PR t[/url]o support everything you need.

Basically you need to keep the GL context current to your new window. For example:

[code]SDL_GL_MakeCurrent(graphicsImpl->GetWindow(), graphicsImpl->GetGLContext());[/code]

Will switch the context to the current Window as set in the Urho3D graphics subsystem.

I do not know how to support multiple windows from the same Urho3D context. Most likely you will need to add support into Urho3D::Graphics to create and support multiple GL contexts. Alternatively you could try to get multiple Graphics systems working, but I'm not sure how much would need to change for it to properly work. Additionally, I was not able to get everything perfectly without digging into which events do what. With the GL stuff going on, the SDL_GL_MakeCurrent needs to be called in the right places.

-------------------------

atai | 2017-01-02 01:09:07 UTC | #3

Thanks.  Sharing the same context between multiple windows is beyond what I need... a single unique context for an OS-level window is the normal use case.  Thank you very much!

-------------------------

