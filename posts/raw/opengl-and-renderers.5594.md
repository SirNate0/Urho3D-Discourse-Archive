kapsloki | 2019-09-18 08:12:15 UTC | #1

The selection and solution of the renderer depends on the target, right? OpenGL for Desktops and OpenGL ES for mobiles, it's automatic, right?

Is there any way to use OpenGL ES for Desktop just like in Godot? I need to specify on window creation or i do this modyfing some part of the code?

And what about Vulkan, is already in the process of being implemented to the engine?

-------------------------

kapsloki | 2019-09-19 20:09:17 UTC | #2

uh................. bump?

-------------------------

suppagam | 2019-09-19 20:59:15 UTC | #3

There are limitations on how you draw: https://urho3d.github.io/documentation/1.7.1/_a_p_i_differences.html

-------------------------

SirNate0 | 2019-09-20 01:21:46 UTC | #4

Pretty sure to use OpenGL ES you'd need to modify the build system. It may be just modifying CMake/Modules/UrhoCommon.cmake (around line 925), or though it may be more complicated than that. What happens if you try to build for arm but use the native toolchain to do so?
Regarding Vulkan there's been a bit of discussion in a few threads, but I don't think there's been anything concrete (I also haven't searched to look, though).

-------------------------

