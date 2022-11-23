GoldenThumbs | 2020-01-25 10:02:24 UTC | #1

Is there already a built-in shader uniform for seeing if a given face is front-facing or back-facing? It's useful to have materials with no culling for things like wire fences or strips of cloth, but the lighting calculations aren't correct for the backfaces because it's using the front facing normals. This can be fixed in the shader but I need access to some sort of uniform that lets the shader know if a face is backfacing or not,

-------------------------

SirNate0 | 2020-01-25 20:18:31 UTC | #2

If it's OpenGL does `gl_FrontFacing` meet your needs?

-------------------------

1vanK | 2020-01-25 14:02:09 UTC | #3

u can analize dot product view direction and face normal

-------------------------

Lumak | 2020-01-25 14:05:55 UTC | #4

You can specify that In the material setting:
>     <material>
>     . . .
>         <cull value="none" />
>         <shadowcull value="none" />
>     </material>
Is that what you're looking for?

Nvm, I think 1vank answers your question.

-------------------------

GoldenThumbs | 2020-01-25 20:19:38 UTC | #5

Thanks for the suggestion, as I am using OpenGL I'm just going to use gl_FrontFacing (Should have probably known about that before lol). This is a good thing to know for DirectX shaders though.

-------------------------

