Per_Hyyrynen | 2017-01-02 01:11:04 UTC | #1

I've been fooling around a bit in Urho3D and am very impressed with it so far. The samples has been very useful.

I have a plane that basically is a billboard with animated content on it. By animated content I mean I rotate and translate them.

I have a bunch of other objects on it that I animate. When the animated objects are partially outside the bounds of the billboard I wish to mask the part of the object that is outside of the billboard.

The way I managed to achieve this is by setting up the billboard and its animated objects in its own scene and then use RenderToTexture to get the content on the actual billboard. It works very well! I've noticed a difference in performance compared to having all the objects on the same scene and having the billboard in its own scene with RenderToTexture. If I start introducing multiple billboards with RenderToTexture it adds up. I've resolved this by decreasing the reslution of RenderToTexture if I have too many billboards.

For my case this is good enough. I still can't help to wonder.

Is there a better way to do this?

-------------------------

cadaver | 2017-01-02 01:11:04 UTC | #2

Can you draw geometry, for example black walls, that mask everything outside?

If you had full control of the rendering you could also use the stencil buffer for masking. Unfortunately Urho already uses the stencil buffer for its own optimizations in the high-level scene rendering (light influence masking) so you would have to go low-level, using the Graphics class directly.

-------------------------

codingmonkey | 2017-01-02 01:11:05 UTC | #3

>I wish to mask the part of the object that is outside of the billboard.

You may try this trick:

1. add for yours billboard technique with additional pass let's say - "bmask"

[code]<technique vs="LitSolid" ps="LitSolid" psdefines="DIFFMAP">
    <pass name="base" />
    <pass name="litbase" psdefines="AMBIENT" />
    <pass name="light" depthtest="equal" depthwrite="false" blend="add" />
    <pass name="prepass" psdefines="PREPASS" />
    <pass name="material" psdefines="MATERIAL" depthtest="equal" depthwrite="false" />
    <pass name="deferred" psdefines="DEFERRED" />
    <pass name="depth" vs="Depth" ps="Depth" />
    <pass name="shadow" vs="Shadow" ps="Shadow" />
    <pass name="bmask" vs="YourShaderToWriteBWColor" ps="YourShaderToWriteBWColor" />
</technique>[/code]

YourShaderToWriteBWColor.glsl
[spoiler][code]#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"
#include "ScreenPos.glsl"

void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
    gl_Position = GetClipPos(worldPos);
}

void PS()
{
    gl_FragColor.rgb = vec3(1.0);
}[/code][/spoiler]

2. add in RenderPath new RTT (with screen size or less) I think 8-bit for mask is enough let's say it named as "bmaskRTT"
So you are add into head of RP: <rendertarget name="bmaskRTT" tag="tagMask" sizedivisor="1 1" format="a" filter="true" />

3. also add scene pass to RenderPath what will be used for billboards with your custom material/technique what have "bmask" material pass
[code]    <command type="scenepass" pass="bmask" output="bmaskRTT" />[/code]

4. at last you have mask and you still do not render your objects what need masking. 
So, at this step you will need tweak shader of this objects(shader) to let use this mask. and add bmask RTT for scenepass into TU where this object are rendered
Prepare workaround for shader with put all needed data in RenderPath pass:
It's may looked like this:
[code]    <command type="scenepass" pass="ThereisWillbeDrawObjectWhatMaskedByBMASKRTT"  output="viewport">
        <texture unit="diffuse" name="bmask" />
    </command>[/code]
so and shader for this will be quite simple it fetch from diffuse(bmask).a < 0.5 you write result color of objects, if not you doing discard.

there maybe needed little fixes/polishing but main concept of using this trick I think simple. 
In this case you do not need second scenes and other stuff, you just works only with RTT and custom shaders/passes in RenderPath.
* also don't forget clear yours custom RTT by clear command for properly rendering working in some cases.

-------------------------

