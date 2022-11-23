suppagam | 2019-09-16 19:02:18 UTC | #1

I've been trying to implement the following in Urho: https://developer.nvidia.com/gpugems/GPUGems3/gpugems3_ch18.html

But I'm a little lost when it mentions pre-process shader? Do I need to create a map temporarily and then apply it's rules to the final texture? Does anyone know any raw OpenGL samples with this technique?

-------------------------

Leith | 2019-09-17 05:38:44 UTC | #2

I've bookmarked this one to review later today / tonight, I will reply once I've had a chance to properly digest it

-------------------------

Leith | 2019-09-19 04:13:13 UTC | #3

The pre-process shader is an offline process that crafts the textures that this approach requires at runtime... you need to pre-process your input textures using a specialized shader, the resulting textures reduce the amount of computation required at runtime, its basically an optimization.

-------------------------

