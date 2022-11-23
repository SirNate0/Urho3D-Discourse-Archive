cosar | 2018-09-25 18:24:33 UTC | #1

Hi,

Can any one please explain why HLSL shaders (Basic.hlsl for example) have unused parameters listed?
For Basic.hlsl I see that most of the VS parameters are unused, and iClip in the PS is unused.
I'm looking into having one shader file that will be used to generate both GLSL and HLSL shaders.

-------------------------

JTippetts | 2018-09-26 03:36:21 UTC | #2

The parameters are enclosed in defines, so they are used only in permutations of the shader whose techniques or materials define those. Otherwise, they are simply omitted from the compilation step. If you look in the various Technique definitions, you can see which techniques define the various constants for the shaders.

As for iClip, I believe that it is used internally by D3D11, you might look at LitSolid.hlsl for a better example of how it is used.

Bear in mind that the included shaders are intended to act as examples for how to construct a shader, and while they do work well it is also possible to write your own shaders. You are not necessarily required to go with the 'uber shader' approach if you don't want to.

-------------------------

cosar | 2018-09-26 03:55:02 UTC | #3

I understand that they are omitted for the techniques that don't use them, but for those techniques that have the macros defined do the parameters need to be there? For example if INSTANCED is defined for a technique that uses LitSolid.hlsl, does iModelInstance need to be there?

-------------------------

JTippetts | 2018-09-26 04:03:08 UTC | #4

Well, yeah, if you want to use instancing then you need iModelInstance. A lot of those parameters may not be used in the shader code inside LitSolid.hlsl, but are used in the various shader code included by LitSolid.hlsl. For instance, iModelInstance is used inside Transform.hlsl, which is included by LitSolid.hlsl.

-------------------------

cosar | 2018-09-26 04:22:17 UTC | #5

Thank you so much!
I missed that #define in Transform.hlsl

About the shaders, wouldn't be beneficial to have both glsl and hlsl be generated from a single shader source? I see that there are some differences, but for the most part they are similar.

-------------------------

JTippetts | 2018-09-26 11:13:01 UTC | #6

Yes, having unified shaders would be a good thing, and is something that has been discussed. If you manage to come up with a quality solution, I'm sure the maintainers would appreciate a pull request.

-------------------------

