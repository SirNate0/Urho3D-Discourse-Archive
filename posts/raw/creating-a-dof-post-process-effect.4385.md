HaeferlKaffee | 2018-07-08 21:40:09 UTC | #1

I'm trying to create a depth-dependent blur effect in post, using GLSL and the technique XML system that the other Post FX use.

My XML code is as follows (It's located in bin/Data/PostProcess, and the GLSL code is located in bin/CoreData/Shaders/GLSL)

    <renderpath>
    <rendertarget name="dofblur" tag="DoF" sizedivisor="2 2" format="rgba" filter="true" />
    <command type="quad" tag="DoF" vs="DepthOfFieldNew" ps="DepthOfFieldNew" output="dofblur">
        <parameter name="BlurClamp" value="1.0" />
        <parameter name="Bias" value="1.0" />
        <parameter name="Focus" value="0.10" />
        <texture unit="diffuse" name="viewport" />
    </command>
    <command type="quad" tag="DoF" vs="CopyFramebuffer" ps="CopyFramebuffer" output="viewport">
        <texture unit="diffuse" name="dofblur" />
    </command>
</renderpath>

The GLSL code I'm currently trying to work with is taken from this post: https://discourse.urho3d.io/t/depth-of-field-glsl/3097

Other Post-effects work fine when appended to the RenderPath I have currently, and I'm adding this technique in the exact same way in the C++ code, yet I get a black screen at runtime.

What am I doing wrong? Have I misunderstood RenderPath entirely?

-------------------------

HaeferlKaffee | 2018-07-08 22:35:45 UTC | #2

This has since been fixed - I mistakenly used the GLSL shaders in the XML, because I hadn't written any HLSL shaders and I'd discovered that my particular build was the default, DirectX, rather than OpenGL.

It's been a problem for me before, because Urho3D is very silent on asset loading issues which is something I'd like to see changed in a future update - instead of allowing us to continue if assets don't load, throw an error and allow us to manage that with our own system, ideally.

-------------------------

