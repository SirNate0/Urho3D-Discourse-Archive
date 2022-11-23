Bananaft | 2017-01-02 01:11:44 UTC | #1

I'm using AngelScript. I build upon render to texture exampe.

In every frame I'm changing size of a viewport, so it draws on different parts of texture. Works great, but now I need to erase parts of texture (best), or whole texture (worst, but still ok).

How to do it?

Digging docs I found this one:

[code]Texture2D.SetData (unsigned level, int x, int y, int width, int height, const void *data)[/code]

Looks like what I need, but i'm confused by "const void *data" . What I should put in there, to draw black rectangle?

Or maybe there is other way to flush whole texture?

Thanks in advance.

-------------------------

cadaver | 2017-01-02 01:11:44 UTC | #2

The function taking a void pointer is for C++ only. In AngelScript you can SetData() an image to a texture, but this overwrites the entire texture.

Another possibility is to have a dummy scene for clearing purposes and render it to the texture on one frame.

In C++ you could also use the Graphics subsystem directly (SetRenderTarget, Clear etc.)

-------------------------

Bananaft | 2017-01-02 01:11:44 UTC | #3

Thank you very much for clarification. I will try dummy scene approach. It also appears that I'm not reading documintaion right.

-------------------------

