rbnpontes | 2017-01-02 01:14:41 UTC | #1

Hello Guys, i have a questionar, it's Possible to use tesselation in HLSL shaders ?, I searched in the reference  and forum, but i did not find answers on the subject.
I would like to create a Water Effect Using Displace and Tesselator.

-------------------------

cadaver | 2017-01-02 01:14:41 UTC | #2

No, currently only vertex & pixel shaders are exposed. You would need to modify the Graphics class API (+ other relevant classes) to add support for the required shader types. There have been community efforts to add shader types (e.g. geometry shaders) but none of them has materialized as a pull request yet.

-------------------------

rbnpontes | 2017-01-02 01:14:42 UTC | #3

Could you tell me which class i start ?

-------------------------

cadaver | 2017-01-02 01:14:42 UTC | #4

- Shader, ShaderVariation, Graphics (to add shader type in the low level graphics API; take a look how vertex/pixel shaders are set)
- Pass, Technique, View, Renderer, Batch (actually make use of the new shader types in scene rendering, again take a look how vertex/pixel shaders are used)

-------------------------

rbnpontes | 2017-01-02 01:14:42 UTC | #5

Thank's for the help, it's very usefull

-------------------------

