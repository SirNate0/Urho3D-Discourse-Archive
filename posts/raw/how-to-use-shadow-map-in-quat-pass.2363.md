artgolf1000 | 2017-01-02 01:14:59 UTC | #1

Hi,

I'm studying volumetric lighting, and I want to make it a post process.

As post processes are implemented by QUAT passes, when writing the GLSL shader, I find that the shadow map does not work, but it works in all sorts of scene paths.

How can I use shadow map in a QUAT pass?

Thanks!

-------------------------

cadaver | 2017-01-02 01:14:59 UTC | #2

The shadow map is specific to a light, and QUAD commands (or any renderpath commands in general) can't refer to a light. If shadow map reuse is enabled (default), the shadow map won't even exist after rendering a certain light, as it may have been overwritten by another light's map. You'll need to look at engine changes / custom C++ code to accomplish this.

-------------------------

artgolf1000 | 2017-01-02 01:14:59 UTC | #3

Find it, View.cpp ---> ExecuteRenderPathCommands() function, the QUAT command does not bind texture for shadow map.

-------------------------

