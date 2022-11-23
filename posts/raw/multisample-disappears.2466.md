artgolf1000 | 2017-01-02 01:15:35 UTC | #1

Hi,

I use multisample feature on iOS devices, it works well.

But if I define a render target in the render path file and use quad command, the multisample feature disappears, I have to append the FXAA2 post effect instead.

I notice the multisample feature always works well on desktop.

Is it not supported or it is just an issue?

-------------------------

cadaver | 2017-01-02 01:15:35 UTC | #2

Backbuffer multisample is different than render texture multisample. The latter is unsupported on mobiles (GLES2) due to lacking functionality.

The limitations are documented at [urho3d.github.io/documentation/ ... ences.html](https://urho3d.github.io/documentation/HEAD/_a_p_i_differences.html)

-------------------------

