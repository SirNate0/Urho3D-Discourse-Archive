lostintime | 2017-01-02 00:59:41 UTC | #1

Hi! 
I want to implement BPCEM reflections via Zone objects. Is there a way to pass cubemap from current Zone to shader, for example, like fog parameters?
Thanks in advance.

-------------------------

cadaver | 2017-01-02 00:59:42 UTC | #2

You will need to add a texture attribute to the Zone (look at Light's attenuation and shape textures for an example) and insert code to Batch::Prepare() to assign the texture to some predefined texture unit when it's also setting the other zone parameters (fog color, etc.)

-------------------------

cadaver | 2017-01-02 00:59:47 UTC | #3

This feature (Zone optionally defining a cube or 3D texture) is now in the master branch. There's a new texture unit (TU_ZONE) that shaders can use, and it's automatically assigned during rendering. But naturally none of the inbuilt shaders use it.

-------------------------

