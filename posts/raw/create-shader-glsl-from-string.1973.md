vrivotti | 2017-01-02 01:11:59 UTC | #1

Is it possible to create a shader and associate it with a technique pass directly from code?
Thank you.

-------------------------

cadaver | 2017-01-02 01:11:59 UTC | #2

It should be possible, but isn't very straightforward. Create a shader resource, "load" it from a VectorBuffer or MemoryBuffer that contains the source code (both VS & PS, like the files) then store it to the ResourceCache as a "manual resource" (AddManualResource). You must set a fake filename for the resource so that the Renderer will eventually find it properly, for example "Shaders/GLSL/MyShader.glsl"

-------------------------

vrivotti | 2017-01-02 01:12:00 UTC | #3

Ok, thank you cadaver.

-------------------------

