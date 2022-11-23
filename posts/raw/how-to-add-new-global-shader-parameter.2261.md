Eugene | 2017-01-02 01:14:20 UTC | #1

I know how to add per-materal parameter. How to add the global one?
I am going to just add new cbuffer and set uniform through Graphics.

-------------------------

cadaver | 2017-01-02 01:14:21 UTC | #2

You can't be sure that cbuffers will be used (D3D9, OpenGL ES, or even OpenGL 3 when cbuffer use is intentionally disabled)

Currently view-global shader parameters are hardcoded to be set in the View class.

Maybe you should add a new event to the engine that is sent during View::SetGlobalShaderParameters(), which would allow code outside the engine to set shader parameters. The issue here is that you need to be able to re-assign the global parameter whenever new shaders are set into use, as (without cbuffers) the uniform/register index can change.

-------------------------

cadaver | 2017-01-02 01:14:22 UTC | #3

Since I needed to add another new event too, there's now an event E_VIEWGLOBALSHADERPARAMETERS in the master branch that's sent when the global parameters are set. Additional parameters can be set at this point.

-------------------------

