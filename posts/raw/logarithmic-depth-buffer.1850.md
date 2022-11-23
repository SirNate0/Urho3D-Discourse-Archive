apat | 2017-01-02 01:10:42 UTC | #1

Hi!

Anyone tried to use a logarithmic depth buffer? 

I tried by adding the following in the shader (terrainblend.glsl), but it doesn't work. Stuff is rendered in wrong order.  

const float C = 1.0;
const float far = 1000000.0;
const float offset = 1.0;
gl_FragDepth = (log(C * vWorldPos.z + offset) / log(C * far + offset));

-------------------------

1vanK | 2017-01-02 01:10:42 UTC | #2

Maybe need to add same to another shaders?

-------------------------

apat | 2017-01-02 01:10:42 UTC | #3

I've looked through the shaders and I think terrainblend.glsl is the only one that put out fragment data (gl_FragColor and such) for the material/technique. But maybe I need to alter some shaders functions that deal with depth?

-------------------------

codingmonkey | 2017-01-02 01:10:42 UTC | #4

Hi, maybe you better try to use the [b]Reversed Depth Buffer[/b] ? instead log zbuff
there is some examples of it (scroll topic almost to bottom) till words - Reversed Depth Buffer: [habrahabr.ru/company/mailru/blog/248873/](https://habrahabr.ru/company/mailru/blog/248873/)

-------------------------

1vanK | 2017-01-02 01:10:42 UTC | #5

Try to change GetDepth in Transform.glsl. This function is using everywhere.

-------------------------

1vanK | 2017-01-02 01:10:42 UTC | #6

Only it seems to me that this would cause problems when applying shadows

-------------------------

