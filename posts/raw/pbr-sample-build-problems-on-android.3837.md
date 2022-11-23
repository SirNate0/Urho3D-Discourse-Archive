AlexS32 | 2017-12-12 16:04:37 UTC | #1

Hello!
I tried to build the PBR sample on Android and got some errors on shaders compilation.
For example: some float variables are declared with suffix 'f'. But this one is used only in GLSL 3.x, e.g. OpenGL ES 3.x. 
Another error was found in global variables declarations in PBRLitSolid shader:

#if defined(NORMALMAP) || defined(IBL)
    varying vec4 vTexCoord;
    varying vec4 vTangent;
#else
    varying vec2 vTexCoord;
#endif

The IBL doesn't defined for VS shader for some techniqe (PBRDiffAlpha for example), so we have a conflict of vTexCoord type. I've added the IBLVS define for the VS shader in the technique and changed shader code:
#if defined(NORMALMAP) || defined(IBL) || defined(IBLVS)
    varying vec4 vTexCoord;
    varying vec4 vTangent;
#else
    varying vec2 vTexCoord;
#endif

After all, PBR sample began to launch. But now I have another problems:
1. The zone's texture is black.
2. Only lights are reflected on metalic surfaces.
3. There aren't any reflections on the wall mirror.
![2|690x388](upload://bfMqVgPDzGmQRESgzg5vrsVZH1o.jpg)

![1|690x388](upload://xl8JrxzU4eroGdcFEX7CsDu3fUK.jpg)

I haven't got any ideas, what I have to do for correction this errors.
Can somebody help me?

-------------------------

dragonCASTjosh | 2017-12-12 17:42:46 UTC | #2

I believe this was reported before and if i remember correctly it was something to do with the way we sample cubemaps for PBR that is not supoprted on GLES 2.0. There are also the other issues you have raised, honestly PBR was not tested or targeted for mobile usage as at the time of development i didnt have access to test hardware. if someone wants to take it on im happy to provide support.

-------------------------

AlexS32 | 2017-12-13 13:06:05 UTC | #3

So in other words,there isn't solution to this problem?

-------------------------

