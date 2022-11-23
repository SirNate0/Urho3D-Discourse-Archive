1vanK | 2017-01-02 01:09:58 UTC | #1

[url=http://savepic.ru/8637634.htm][img]http://savepic.ru/8637634m.png[/img][/url]

Old version: [github.com/1vanK/Urho3DOutline](https://github.com/1vanK/Urho3DOutline)

[b]Now with multiple colors and without coping of mesh[/b]

Renderpath
[code]
<renderpath>
    <rendertarget name="outlineMask" sizedivisor="1 1" format="rgba" filter="true" />
    <rendertarget name="outlineBlurredMaskH" sizedivisor="2 2" format="rgba" filter="true" />
    <rendertarget name="outlineBlurredMaskV" sizedivisor="2 2" format="rgba" filter="true" />
    <command type="clear" color="fog" depth="1.0" stencil="0" />
    <command type="clear" color="0 0 0 0" output="outlineMask" />
    <command type="scenepass" pass="base" vertexlights="true" metadata="base" />
    <command type="forwardlights" pass="light" />
    <command type="scenepass" pass="postopaque" />
    <command type="scenepass" pass="refract">
        <texture unit="environment" name="viewport" />
    </command>
    <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" />
    <command type="scenepass" pass="postalpha" sort="backtofront" />
    <command type="scenepass" pass="outline" output="outlineMask" />
    <command type="quad" vs="Outline" ps="Outline" psdefines="BLURH" output="outlineBlurredMaskH">
        <texture unit="diffuse" name="outlineMask" />
    </command>
    <command type="quad" vs="Outline" ps="Outline" psdefines="BLURV" output="outlineBlurredMaskV">
        <texture unit="diffuse" name="outlineBlurredMaskH" />
    </command>
    <command type="quad" vs="Outline" ps="Outline" psdefines="OUTPUT" output="viewport">
        <texture unit="diffuse" name="outlineBlurredMaskV" />
        <texture unit="normal" name="outlineMask" />
        <texture unit="specular" name="viewport" />
    </command>
</renderpath>
[/code]

Outline.glsl
[code]
#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"
#include "ScreenPos.glsl"

varying vec2 vTexCoord;
varying vec2 vScreenPos;

#ifdef COMPILEPS
    uniform vec4 cOutlineColor;
    uniform vec2 cOutlineBlurredMaskHInvSize;
#endif

void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
    gl_Position = GetClipPos(worldPos);
    vTexCoord = GetQuadTexCoord(gl_Position);
    vScreenPos = GetScreenPosPreDiv(gl_Position);
}

void PS()
{
    #ifdef MASK
        gl_FragColor = vec4(cOutlineColor.rgb, 1.0);
    #endif

    #ifdef BLURH
        vec4 rgba = texture2D(sDiffMap, vTexCoord + vec2(0.0, 0.0) * cOutlineBlurredMaskHInvSize) * 0.2;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(-1.0, 0.0) * cOutlineBlurredMaskHInvSize) * 0.2;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(1.0, 0.0) * cOutlineBlurredMaskHInvSize) * 0.2;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(-2.0, 0.0) * cOutlineBlurredMaskHInvSize) * 0.2;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(2.0, 0.0) * cOutlineBlurredMaskHInvSize) * 0.2;
        gl_FragColor = rgba;
    #endif

    #ifdef BLURV
        vec4 rgba = texture2D(sDiffMap, vTexCoord + vec2(0.0, 0.0) * cOutlineBlurredMaskHInvSize) * 0.2;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(0.0, -1.0) * cOutlineBlurredMaskHInvSize) * 0.2;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(0.0, 1.0) * cOutlineBlurredMaskHInvSize) * 0.2;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(0.0, -2.0) * cOutlineBlurredMaskHInvSize) * 0.2;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(0.0, 2.0) * cOutlineBlurredMaskHInvSize) * 0.2;
        gl_FragColor = rgba;
    #endif

    #ifdef OUTPUT
        vec4 blurredMask = texture2D(sDiffMap, vTexCoord);
        vec4 mask = texture2D(sNormalMap, vTexCoord);
        vec4 viewport = texture2D(sSpecMap, vTexCoord);
        blurredMask = clamp(blurredMask - mask.a, 0.0, 1.0);
        blurredMask *= 2.0;
        gl_FragColor = viewport + blurredMask;
    #endif
}
[/code]

Techniques/NoTextureOutline.xml
[code]
<technique vs="LitSolid" ps="LitSolid" vsdefines="NOUV" >
    <pass name="base" />
    <pass name="litbase" psdefines="AMBIENT" />
    <pass name="light" depthtest="equal" depthwrite="false" blend="add" />
    <pass name="prepass" psdefines="PREPASS" />
    <pass name="material" psdefines="MATERIAL" depthtest="equal" depthwrite="false" />
    <pass name="deferred" psdefines="DEFERRED" />
    <pass name="depth" vs="Depth" ps="Depth" />
    <pass name="shadow" vs="Shadow" ps="Shadow" />
    <pass name="outline" vs="Outline" ps="Outline" psdefines="MASK" depthwrite="false" />
</technique>
[/code]

Material
[code]
<material>
	<technique name="Techniques/NoTextureOutline.xml" />
	<parameter name="MatDiffColor" value="1 1 1 1" />
	<parameter name="MatSpecColor" value="1 1 1 300" />
    <parameter name="OutlineColor" value="1 0 0 0" />
</material>
[/code]

[b]EDIT:[/b] Example [topic1840-10.html#p10978](http://urho3d.prophpbb.com/topic1840-10.html#p10978)

-------------------------

Enhex | 2017-01-02 01:09:58 UTC | #2

Nice work!
Can be very useful for highlighting objects for indication.

-------------------------

1vanK | 2017-01-02 01:09:58 UTC | #3

[url=http://savepic.ru/8605934.htm][img]http://savepic.ru/8605934m.png[/img][/url]

[b]Modified version:[/b]
Outline is visible through other objects like Dota 2 and Left 4 Dead 2 (disabled depth test and enabled sorting).
Also some fixes (more correct mixing outline with viewport and more correct blurring).

shader Outline.glsl
[code]
#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"
#include "ScreenPos.glsl"

varying vec2 vTexCoord;
varying vec2 vScreenPos;

#ifdef COMPILEPS
    uniform vec4 cOutlineColor;
    uniform vec2 cOutlineBlurredMaskHInvSize;
#endif

void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
    gl_Position = GetClipPos(worldPos);
    vTexCoord = GetQuadTexCoord(gl_Position);
    vScreenPos = GetScreenPosPreDiv(gl_Position);
}

void PS()
{
    #ifdef MASK
        gl_FragColor = vec4(cOutlineColor.rgb, 1.0);
    #endif

    #ifdef BLURH
        vec4 rgba = texture2D(sDiffMap, vTexCoord + vec2(0.0, 0.0) * cOutlineBlurredMaskHInvSize) * 0.1;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(-1.0, 0.0) * cOutlineBlurredMaskHInvSize) * 0.2;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(1.0, 0.0) * cOutlineBlurredMaskHInvSize) * 0.4;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(-2.0, 0.0) * cOutlineBlurredMaskHInvSize) * 0.2;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(2.0, 0.0) * cOutlineBlurredMaskHInvSize) * 0.1;
        gl_FragColor = rgba;
    #endif

    #ifdef BLURV
        vec4 rgba = texture2D(sDiffMap, vTexCoord + vec2(0.0, 0.0) * cOutlineBlurredMaskHInvSize) * 0.1;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(0.0, -1.0) * cOutlineBlurredMaskHInvSize) * 0.2;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(0.0, 1.0) * cOutlineBlurredMaskHInvSize) * 0.4;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(0.0, -2.0) * cOutlineBlurredMaskHInvSize) * 0.2;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(0.0, 2.0) * cOutlineBlurredMaskHInvSize) * 0.1;
        gl_FragColor = rgba;
    #endif

    #ifdef OUTPUT
        vec4 blurredMask = texture2D(sDiffMap, vTexCoord);
        vec4 mask = texture2D(sNormalMap, vTexCoord);
        vec4 viewport = texture2D(sSpecMap, vTexCoord);
        blurredMask = clamp(blurredMask - mask.a, 0.0, 1.0);
        gl_FragColor = viewport * (1.0 - blurredMask.a) + blurredMask;
    #endif
}
[/code]

renderpath
[code]<renderpath>
    <rendertarget name="outlineMask" sizedivisor="1 1" format="rgba" filter="true" />
    <rendertarget name="outlineBlurredMaskH" sizedivisor="2 2" format="rgba" filter="true" />
    <rendertarget name="outlineBlurredMaskV" sizedivisor="2 2" format="rgba" filter="true" />
    <command type="clear" color="fog" depth="1.0" stencil="0" />
    <command type="clear" color="0 0 0 0" output="outlineMask" />
    <command type="scenepass" pass="base" vertexlights="true" metadata="base" />
    <command type="forwardlights" pass="light" />
    <command type="scenepass" pass="postopaque" />
    <command type="scenepass" pass="refract">
        <texture unit="environment" name="viewport" />
    </command>
    <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" />
    <command type="scenepass" pass="postalpha" sort="backtofront" />
    <command type="scenepass" pass="outline" output="outlineMask" sort="backtofront" />
    <command type="quad" vs="Outline" ps="Outline" psdefines="BLURH" output="outlineBlurredMaskH">
        <texture unit="diffuse" name="outlineMask" />
    </command>
    <command type="quad" vs="Outline" ps="Outline" psdefines="BLURV" output="outlineBlurredMaskV">
        <texture unit="diffuse" name="outlineBlurredMaskH" />
    </command>
    <command type="quad" vs="Outline" ps="Outline" psdefines="OUTPUT" output="viewport">
        <texture unit="diffuse" name="outlineBlurredMaskV" />
        <texture unit="normal" name="outlineMask" />
        <texture unit="specular" name="viewport" />
    </command>
</renderpath>
[/code]

Technique DiffOutline.xml
[code]
<technique vs="LitSolid" ps="LitSolid" psdefines="DIFFMAP">
    <pass name="base" />
    <pass name="litbase" psdefines="AMBIENT" />
    <pass name="light" depthtest="equal" depthwrite="false" blend="add" />
    <pass name="prepass" psdefines="PREPASS" />
    <pass name="material" psdefines="MATERIAL" depthtest="equal" depthwrite="false" />
    <pass name="deferred" psdefines="DEFERRED" />
    <pass name="depth" vs="Depth" ps="Depth" />
    <pass name="shadow" vs="Shadow" ps="Shadow" />
    <pass name="outline" vs="Outline" ps="Outline" psdefines="MASK" depthtest="always" depthwrite="false" />
</technique>
[/code]

material MushroomOutline.xml
[code]
<material>
    <technique name="Techniques/DiffOutline.xml" />
    <texture unit="diffuse" name="Textures/Mushroom.dds" />
    <parameter name="MatSpecColor" value="0.1 0.1 0.1 16" />
    <parameter name="OutlineColor" value="1 0 0 0" />
</material>
[/code]

-------------------------

1vanK | 2017-01-02 01:09:58 UTC | #4

Big size of glow (more samples):

[url=http://savepic.ru/8617207.htm][img]http://savepic.ru/8617207m.png[/img][/url]

Outline.glsl

[code]#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"
#include "ScreenPos.glsl"

varying vec2 vTexCoord;
varying vec2 vScreenPos;

#ifdef COMPILEPS
    uniform vec4 cOutlineColor;
    uniform vec2 cOutlineBlurredMaskHInvSize;
#endif

void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
    gl_Position = GetClipPos(worldPos);
    vTexCoord = GetQuadTexCoord(gl_Position);
    vScreenPos = GetScreenPosPreDiv(gl_Position);
}

void PS()
{
    #ifdef MASK
        gl_FragColor = vec4(cOutlineColor.rgb, 1.0);
    #endif

    #ifdef BLURH
        vec4 rgba = texture2D(sDiffMap, vTexCoord + vec2(0.0, 0.0) * cOutlineBlurredMaskHInvSize) * 0.091;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(-1.0, 0.0) * cOutlineBlurredMaskHInvSize) * 0.091;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(1.0, 0.0) * cOutlineBlurredMaskHInvSize) * 0.091;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(-2.0, 0.0) * cOutlineBlurredMaskHInvSize) * 0.091;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(2.0, 0.0) * cOutlineBlurredMaskHInvSize) * 0.091;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(-3.0, 0.0) * cOutlineBlurredMaskHInvSize) * 0.091;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(3.0, 0.0) * cOutlineBlurredMaskHInvSize) * 0.091;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(-4.0, 0.0) * cOutlineBlurredMaskHInvSize) * 0.091;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(4.0, 0.0) * cOutlineBlurredMaskHInvSize) * 0.091;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(-5.0, 0.0) * cOutlineBlurredMaskHInvSize) * 0.091;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(5.0, 0.0) * cOutlineBlurredMaskHInvSize) * 0.091;
        gl_FragColor = rgba;
    #endif

    #ifdef BLURV
        vec4 rgba = texture2D(sDiffMap, vTexCoord + vec2(0.0, 0.0) * cOutlineBlurredMaskHInvSize) * 0.091;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(0.0, -1.0) * cOutlineBlurredMaskHInvSize) * 0.091;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(0.0, 1.0) * cOutlineBlurredMaskHInvSize) * 0.091;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(0.0, -2.0) * cOutlineBlurredMaskHInvSize) * 0.091;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(0.0, 2.0) * cOutlineBlurredMaskHInvSize) * 0.091;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(0.0, -3.0) * cOutlineBlurredMaskHInvSize) * 0.091;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(0.0, 3.0) * cOutlineBlurredMaskHInvSize) * 0.091;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(0.0, -4.0) * cOutlineBlurredMaskHInvSize) * 0.091;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(0.0, 4.0) * cOutlineBlurredMaskHInvSize) * 0.091;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(0.0, -5.0) * cOutlineBlurredMaskHInvSize) * 0.091;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(0.0, 5.0) * cOutlineBlurredMaskHInvSize) * 0.091;
        gl_FragColor = rgba;
    #endif

    #ifdef OUTPUT
        vec4 blurredMask = texture2D(sDiffMap, vTexCoord);
        vec4 mask = texture2D(sNormalMap, vTexCoord);
        vec4 viewport = texture2D(sSpecMap, vTexCoord);
        blurredMask = clamp(blurredMask - mask.a, 0.0, 1.0);
        gl_FragColor = viewport * (1.0 - blurredMask.a) + blurredMask;
    #endif
}
[/code]

-------------------------

Lumak | 2017-01-02 01:09:58 UTC | #5

Very nice! Thank you for this.

-------------------------

codingmonkey | 2017-01-02 01:09:58 UTC | #6

Great work! :slight_smile:

-------------------------

1vanK | 2017-01-02 01:09:59 UTC | #7

final version of shader

[url=http://savepic.ru/8596286.htm][img]http://savepic.ru/8596286m.png[/img][/url]

[code]#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"
#include "ScreenPos.glsl"

varying vec2 vTexCoord;
varying vec2 vScreenPos;

#ifdef COMPILEPS
    uniform vec4 cOutlineColor;
    uniform vec2 cOutlineBlurredMaskHInvSize;
#endif

void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
    gl_Position = GetClipPos(worldPos);
    vTexCoord = GetQuadTexCoord(gl_Position);
    vScreenPos = GetScreenPosPreDiv(gl_Position);
}

void PS()
{
    #ifdef MASK
        gl_FragColor = vec4(cOutlineColor.rgb, 1.0);
    #endif

    #ifdef BLURH
        vec4 rgba = texture2D(sDiffMap, vTexCoord + vec2(0.0, 0.0) * cOutlineBlurredMaskHInvSize)
                  + texture2D(sDiffMap, vTexCoord + vec2(-1.0, 0.0) * cOutlineBlurredMaskHInvSize)
                  + texture2D(sDiffMap, vTexCoord + vec2(1.0, 0.0) * cOutlineBlurredMaskHInvSize)
                  + texture2D(sDiffMap, vTexCoord + vec2(-2.0, 0.0) * cOutlineBlurredMaskHInvSize)
                  + texture2D(sDiffMap, vTexCoord + vec2(2.0, 0.0) * cOutlineBlurredMaskHInvSize);
        gl_FragColor = rgba * 0.2;
    #endif

    #ifdef BLURV
        vec4 rgba = texture2D(sDiffMap, vTexCoord + vec2(0.0, 0.0) * cOutlineBlurredMaskHInvSize)
                  + texture2D(sDiffMap, vTexCoord + vec2(0.0, -1.0) * cOutlineBlurredMaskHInvSize)
                  + texture2D(sDiffMap, vTexCoord + vec2(0.0, 1.0) * cOutlineBlurredMaskHInvSize)
                  + texture2D(sDiffMap, vTexCoord + vec2(0.0, -2.0) * cOutlineBlurredMaskHInvSize)
                  + texture2D(sDiffMap, vTexCoord + vec2(0.0, 2.0) * cOutlineBlurredMaskHInvSize);
        gl_FragColor = rgba * 0.2;
    #endif

    #ifdef OUTPUT
        vec4 blurredMask = texture2D(sDiffMap, vTexCoord);
        vec4 mask = texture2D(sNormalMap, vTexCoord);
        vec4 viewport = texture2D(sSpecMap, vTexCoord);
        blurredMask = clamp(blurredMask - mask.a, 0.0, 1.0);
        blurredMask *= 3.0;
        gl_FragColor = viewport * (1.0 - blurredMask.a) + blurredMask;
    #endif
}
[/code]

-------------------------

rasteron | 2017-01-02 01:09:59 UTC | #8

This is a great improvement! very nice :slight_smile:

-------------------------

weitjong | 2017-01-02 01:10:00 UTC | #9

Thanks for sharing this. This is something that definitely will come in handy.

-------------------------

Modanung | 2017-01-02 01:10:00 UTC | #10

Awesome!  :mrgreen:
Great improvement over the first version.

-------------------------

Enhex | 2017-01-02 01:10:01 UTC | #11

Since people want to use it, open a repo with permissive license?

-------------------------

1vanK | 2017-01-02 01:10:01 UTC | #12

code license: public domain

-------------------------

yushli | 2017-01-02 01:10:09 UTC | #13

Thank you for sharing this.  Great example to learn glsl in urho3d.
I suggest to put it together in a new github repo. Many people will be interested to try out.

-------------------------

Modanung | 2017-01-02 01:10:09 UTC | #14

Why not update the existing GitHub repo with the new shader? Or are you planning to?

-------------------------

1vanK | 2017-01-02 01:10:09 UTC | #15

[quote="Modanung"]Why not update the existing GitHub repo with the new shader? Or are you planning to?[/quote]

This is a different approach, perhaps the old version will be useful to someone. In any case, I see no point in duplicating the same thing in several places :)

-------------------------

1vanK | 2017-01-02 01:10:20 UTC | #16

Small example how to use it for select/deselect objects [github.com/1vanK/Urho3DOutlineSelectionExample](https://github.com/1vanK/Urho3DOutlineSelectionExample)

EDIT: Press RMB for moving and rotating camera, and LMB for select

-------------------------

codingmonkey | 2017-01-02 01:10:20 UTC | #17

nice! 
Is it possible use this for animated models?
like this :
[spoiler][video]https://youtu.be/d7QoWUSOZPw?t=16m19s[/video][/spoiler]

-------------------------

1vanK | 2017-01-02 01:10:20 UTC | #18

[quote="codingmonkey"]nice! 
Is it possible use this for animated models?
like this :
[spoiler][video]https://youtu.be/d7QoWUSOZPw?t=16m19s[/video][/spoiler][/quote]

It is possible for any material :) just add to technique:

[code]
<pass name="outline" vs="Outline" ps="Outline" psdefines="MASK" depthtest="always" depthwrite="false" />
[/code]

-------------------------

1vanK | 2017-01-02 01:12:22 UTC | #19

Another (and simplest) method was made possible by the patch [github.com/urho3d/Urho3D/commit ... 5eea396080](https://github.com/urho3d/Urho3D/commit/7da8374a3b929168d4919dddd99aa15eea396080)

[url=http://savepic.ru/9780680.htm][img]http://savepic.ru/9780680m.png[/img][/url]

Shader Outline.glsl:
[code]#include "Uniforms.glsl"
#include "Transform.glsl"

#ifdef COMPILEVS
uniform float cOutlineWidth = 0.01;
#endif

#ifdef COMPILEPS
uniform vec4 cOutlineColor = vec4(1.0, 1.0, 1.0, 1.0);
#endif

void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
    vec3 vNormal = GetWorldNormal(modelMatrix);
    // Scale along normal
    worldPos += vNormal * cOutlineWidth;
    gl_Position = GetClipPos(worldPos);
}

void PS()
{
    gl_FragColor = cOutlineColor.rgba;
}
[/code]

Technique DiffOutline.xml:
[code]
<technique vs="LitSolid" ps="LitSolid" psdefines="DIFFMAP">
    <pass name="base" />
    <pass name="litbase" psdefines="AMBIENT" />
    <pass name="light" depthtest="equal" depthwrite="false" blend="add" />
    <pass name="prepass" psdefines="PREPASS" />
    <pass name="material" psdefines="MATERIAL" depthtest="equal" depthwrite="false" />
    <pass name="deferred" psdefines="DEFERRED" />
    <pass name="depth" vs="Depth" ps="Depth" />
    <pass name="shadow" vs="Shadow" ps="Shadow" />
    
    <!-- ADDED -->
    <pass name="postopaque" depthwrite="false" vs="Outline" ps="Outline" cull="cw" />
</technique>
[/code]

Material MushroomOutline.xml:
[code]
<material>
    <technique name="Techniques/DiffOutline.xml" />
    <texture unit="diffuse" name="Textures/Mushroom.dds" />
    <parameter name="MatSpecColor" value="0.1 0.1 0.1 16" />
    
    <!-- ADDED -->
    <parameter name="OutlineWidth" value="0.01" />
    <parameter name="OutlineColor" value="1 1 0 1" />
</material>
[/code]

Note: it works correctly only for models with smooth shading

-------------------------

Scellow | 2017-01-02 01:13:54 UTC | #20

This is really nice, do you think you can make a voxel based one, like this one ? [twitter.com/_chrisro/status/703373120313421825](https://twitter.com/_chrisro/status/703373120313421825)

-------------------------

1vanK | 2017-01-02 01:13:54 UTC | #21

[quote="Scellow"]This is really nice, do you think you can make a voxel based one, like this one ? [twitter.com/_chrisro/status/703373120313421825](https://twitter.com/_chrisro/status/703373120313421825)[/quote]

The author share his shaders [twitter.com/_chrisro/status/759558775657422849](https://twitter.com/_chrisro/status/759558775657422849)

so u can port it to Urho

-------------------------

Miegamicis | 2019-01-25 21:16:17 UTC | #22

I managed to get this to work with DirectX

Code:
```
#include "Uniforms.hlsl"
#include "Samplers.hlsl"
#include "Transform.hlsl"
#include "ScreenPos.hlsl"
#include "PostProcess.hlsl"

uniform float2 vScreenPos;

uniform float4 cOutlineColor;
uniform float2 cOutlineBlurredMaskHInvSize;


void VS(float4 iPos : POSITION,
    out float2 oTexCoord : TEXCOORD0,
    out float2 oScreenPos : TEXCOORD1,
    out float4 oPos : OUTPOSITION)
{
    float4x3 modelMatrix = iModelMatrix;
    float3 worldPos = GetWorldPos(modelMatrix);
    oPos = GetClipPos(worldPos);
    oTexCoord = GetQuadTexCoord(oPos);
    oScreenPos = GetScreenPosPreDiv(oPos);
}

void PS(
    float3 iTexCoord : TEXCOORD0,
    float2 iScreenPos : TEXCOORD1,
    out float4 oColor : OUTCOLOR0)
{
    #ifdef MASK
    oColor = float4(cOutlineColor.rgb, 1);
    #endif

    #ifdef BLURH
        float4 rgba = Sample2D(DiffMap, iScreenPos + float2(0.0, 0.0) * cOutlineBlurredMaskHInvSize);
        oColor = rgba * 0.2;
    #endif

    #ifdef BLURV
        float4 rgba = Sample2D(DiffMap, iScreenPos + float2(0.0, 0.0) * cOutlineBlurredMaskHInvSize);
        oColor = rgba * 0.2;
    #endif


    #ifdef OUTPUT
        float4 blurredMask = Sample2D(DiffMap, iScreenPos);
        float4 mask = Sample2D(NormalMap, iScreenPos);
        float4 viewport = Sample2D(SpecMap, iScreenPos);
        blurredMask = clamp(blurredMask - mask.a, 0.0, 1.0);
        blurredMask *= 200.0;
        oColor = viewport * (1.0 - blurredMask.a) + blurredMask;
    #endif


}
```

Althought I did have to change few things to get it to work correctly. Also my experience with HLSL shaders is really small, but I'm happy with the results.

-------------------------

I3DB | 2019-01-25 21:34:21 UTC | #23

Can you provide a simple working sample with this shader in place?

-------------------------

Miegamicis | 2019-01-25 21:37:14 UTC | #24

See my project here: https://github.com/ArnisLielturks/Urho3D-Project-Template
There are few commits which shows how its done

-------------------------

Miegamicis | 2019-01-25 21:39:00 UTC | #25

January 9th commits to be exact

-------------------------

I3DB | 2019-01-26 18:56:07 UTC | #26

Ok, got three files, the material, the technique and the hlsl shader.

In the feature sample billboards, made the tiles out of stoneoutline.xml rather than stone.xml.

And can't see a difference.  Log output looks fine, but initially I hadn't gotten the technique just the shader and material and found that via the log.

What case is the appropriate use of this material to highlight the effect your work shows?

```
DEBUG: Loading resource Materials/StoneOutline.xml
DEBUG: Loading resource Techniques/DiffOutline.xml
```

-------------------------

Miegamicis | 2019-01-26 19:12:18 UTC | #27

What about render path file? https://github.com/ArnisLielturks/Urho3D-Project-Template/blob/master/bin/CoreData/RenderPaths/Forward.xml 
Also I'm not the author of this so cant take credit for it. Im just the guy who adopted HLSL shader, nothing else

-------------------------

Modanung | 2019-01-26 20:11:07 UTC | #28

I'm not sure the effect would be visible on a billboard. Could you try the material on a different model?

-------------------------

I3DB | 2019-01-26 20:26:16 UTC | #29

[quote="Miegamicis, post:27, topic:1766"]
What about render path file?
[/quote]

Yes, was missing most of the contents of that file, though the file itself was in my RenderPaths folder.

[quote="Modanung, post:28, topic:1766"]
Could you try the material on a different model?
[/quote]

I'm not formally running it on a billboard model, but on a box model. Here's most of the pertinent code, with a change to run forward.xml.

```
var rp = ((StereoApplication)Application).Renderer.DefaultRenderPath.Clone();
            rp.Append(Application.ResourceCache.GetXmlFile("RenderPaths/Forward.xml"));
            ((StereoApplication)Application).Renderer.DefaultRenderPath = rp;

            //working on why no shadows ... but so far have never seen an Urho3D shadow on any hololens app
            Application.Renderer.DrawShadows = true;
            
            var YPos = -50;
            for (int y = -5; y <= 5; ++y)
                for (int x = -5; x <= 5; ++x)
                {
                    var floorNode = billboardNode.CreateChild("FloorTile");
                    floorNode.AddTag("Billboard");
                    floorNode.Position = new Vector3(x * 20.5f, YPos, y * 20.5f);
                    floorNode.Scale = new Vector3(20.0f, 1.0f, 20.0f);
                    var floorObject = floorNode.CreateComponent<Urho.Shapes.Box>();
                    floorObject.Material = cache.GetMaterial("Materials/StoneOutline.xml");
                    //floorObject.Material = cache.GetMaterial("Materials/Stone.xml");
                }
```

After adding in the renderpath to forward.xml, and modifying the contents of that file. Perhaps see some additional blurring, but honestly, not sure what to look for. Somehow I thought it would be readily visible.

-------------------------

I3DB | 2019-01-26 20:41:18 UTC | #30

[quote="Modanung, post:28, topic:1766, full:true"]
I’m not sure the effect would be visible on a billboard. Could you try the material on a different model?
[/quote]

Also converted the animating scene feature sample, and again, see no difference. No errors or warnings, all looks just like it did before the conversion to use StoneOutline.xml. Perhaps a bit of shimmer in the light as they rotate? Meaning, when I decrease the light brightness, they seem to give off a sparkle, like rotating a diamond in the light, as if that face of the cube has been polished.

What is the actual effect?

-------------------------

Modanung | 2019-01-26 21:10:06 UTC | #31

[quote="I3DB, post:30, topic:1766"]
What is the actual effect?
[/quote]
It adds an outline.
![Outline|213x154](upload://4SWuO3uXkjxcVXxSC22nExjGmtR.png)

Be sure to have something like `<parameter name="OutlineWidth" value="0.05" />` and `    <parameter name="OutlineColor" value="0 0 0 1" />` in your material file.

-------------------------

I3DB | 2019-01-26 21:31:00 UTC | #32

Was missing the OutlineWidth parameter, but still no outline seen. I'm using SharpReality and viewing on a hololens.

Here's the material file:
```
<material>
  <technique name="Techniques/DiffOutline.xml" />
  <parameter name="MatDiffColor" value="1 1 1 1" />
  <parameter name="MatSpecColor" value="1 1 1 300" />
 
  <parameter name="OutlineBlurredMaskHInvSize" value="1 1" />
  <parameter name="OutlineWidth" value="0.15" />
  <parameter name="OutlineColor" value=".5 .5 .5" />
  <texture unit="diffuse" name="Textures/StoneDiffuse.dds" />
  <texture unit="normal" name="Textures/StoneNormal.dds" />
</material>
```

Have been modifying values trying to see some change. Black doesn't show up on a hololens unless in front of a colored background like you show.

-------------------------

Modanung | 2019-01-26 21:35:38 UTC | #33

Could you post a screenshot?
Your `OutlineColor` is missing a fourth number (alpha value), btw.

-------------------------

I3DB | 2019-01-26 21:45:10 UTC | #34

It looks identical to what it looks like without StoneOutline.xml, so using Stone.xml produces an identical output. [Using the animatedscene feature sample, in c#](https://github.com/xamarin/urho-samples/tree/master/FeatureSamples/Core/05_AnimatingScene). Just converted to run on hololens are the only changes to it. And changes for stoneoutline, the material, the technique, the hlsl shader, and changes to forward.xml, and the change to render path to use forward.xml.

The urho log runs clean. Added the missing alpha param.

-------------------------

Modanung | 2019-01-26 22:00:11 UTC | #35

1. Could you try the material on a different model?
2. Could you post a screenshot?

-------------------------

I3DB | 2019-01-26 22:22:06 UTC | #36

![MCS_Photo17-01-52|690x388](upload://cGLRohDCOKj4bqvaDAQWuMSTMOY.jpeg)

With cylinder model:
![MCS_Photo17-07-23|690x388](upload://q8c7oyqnABy7t2eVjEdvwHNqdlv.jpeg)

That shimmer sort of shows up on some of the cylinders. They look really nice on hololens.

Finally, here is just the plain Stone.xml picture with cylinder model, there's a bit of sparkle, but it's more pronounced with the StoneOutline.xml, but still very subtle and only visible at times for just a blink of an eye, just like a diamond rotating in the light:
![MCS_Photo17-18-44|690x388](upload://6lXzYmJ3zIGWKcB74BvTaAPOJyI.jpeg)

-------------------------

Modanung | 2019-01-26 22:23:34 UTC | #37

I believe that's the specular reflection.
Did you add the fourth number to your `OutlineColor`?

-------------------------

I3DB | 2019-01-26 22:26:33 UTC | #38

[quote="Modanung, post:37, topic:1766"]
Did you add the fourth number to your `OutlineColor` ?
[/quote]

[quote="I3DB, post:34, topic:1766"]
The urho log runs clean. Added the missing alpha param.
[/quote]

Yes, and to get to 20 chars, I'll say it again, yes.

Edit: here's the material file:
```
<material>
  <technique name="Techniques/DiffOutline.xml" />
  <parameter name="MatDiffColor" value="1 1 1 1" />
  <parameter name="MatSpecColor" value="1 1 1 300" />
 
  <parameter name="OutlineBlurredMaskHInvSize" value="1 1" />
  <parameter name="OutlineWidth" value="0.2" />
  <parameter name="OutlineColor" value=".5 .5 .5 1" />
  <texture unit="diffuse" name="Textures/StoneDiffuse.dds" />
  <texture unit="normal" name="Textures/StoneNormal.dds" />
</material>
```

-------------------------

Modanung | 2019-01-26 22:27:48 UTC | #39

Do you have a repository somewhere?
Also, could you try _removing_ - or commenting out - this line:
`<parameter name="OutlineBlurredMaskHInvSize" value="1 1" />`?

-------------------------

I3DB | 2019-01-26 22:33:04 UTC | #40


[quote="Modanung, post:37, topic:1766"]
I believe that’s the specular reflection.
[/quote]


But why would it be more pronounced with StoneOutline? Subtle but a bit more noticed.

[quote="Modanung, post:39, topic:1766, full:true"]
Do you have a repository somewhere?
Also, could you try *removing* - or commenting out - this line:
`<parameter name="OutlineBlurredMaskHInvSize" value="1 1" />` ?
[/quote]

[The repository is really the C# featured samples.](https://github.com/xamarin/urho-samples/tree/master/FeatureSamples) that run on a number of different platforms. I've copied and modified, but the base is the same. 

Removed that parameter ... no change.

-------------------------

Modanung | 2019-01-26 22:33:17 UTC | #41

[quote="I3DB, post:40, topic:1766"]
But why would it be more pronounced with StoneOutline? Subtle but a bit more noticed.
[/quote]

Does it have a different `MatSpecColor` value?

-------------------------

I3DB | 2019-01-26 23:14:07 UTC | #42

[quote="Modanung, post:41, topic:1766"]
Does it have a different `MatSpecColor` value?
[/quote]

Ahh yes.

Stone.xml
```
<material>
    <technique name="Techniques/DiffNormal.xml" quality="1" />
    <technique name="Techniques/Diff.xml" quality="0" />
    <texture unit="diffuse" name="Textures/StoneDiffuse.dds" />
    <texture unit="normal" name="Textures/StoneNormal.dds" />
    <shader psdefines="PACKEDNORMAL" />
    <parameter name="MatSpecColor" value="0.3 0.3 0.3 16" />
</material>
```

I've got the PBR materials sample working without error ... just wanted to add a bit of hope.

Also tried with jack:

![MCS_Photo18-01-03|690x388](upload://j6hDJZrZ2YyI2xJdVE7wV5uhpR0.jpeg)

```
<material>
    <technique name="Techniques/DiffOutline.xml" />
    <parameter name="MatSpecColor" value="0.5 0.5 0.5 16" />
  <texture unit="diffuse" name="Textures/Smoke.dds" />
  <parameter name="OutlineBlurredMaskHInvSize" value="1 1" />
  <parameter name="OutlineWidth" value="0.2" />
  <parameter name="OutlineColor" value=".5 .5 .5 1" />
</material>
```

And finally, with a cone:
![MCS_Photo18-12-44|690x388](upload://gEV6eBJwytMnQi9NzrwQBomWa0Y.jpeg)

-------------------------

Miegamicis | 2019-01-28 09:52:48 UTC | #43

How this should look with the HLSL shader:
![Screenshot_Mon_Jan_28_11_51_00_2019|666x500](upload://w81IJoEtqm5SPmplLRX5s8SRisQ.png)

-------------------------

I3DB | 2019-02-08 17:33:03 UTC | #44

[quote="Miegamicis, post:22, topic:1766"]
I managed to get this to work with DirectX
[/quote]

[What's checked in looks different. Is the semicolon supposed to be there at the end of the line?](https://github.com/ArnisLielturks/Urho3D-Project-Template/blob/aa5e4d6731159dc58bff45e41d502bf683c39c0d/bin/CoreData/Shaders/HLSL/Outline.hlsl#L35)

I've been trying to figure out why this won't work for me. And getting some errors now:
```
4:)  [Fri Feb  8 12:10:35 2019] ERROR: Failed to compile vertex shader Outline():
..\Shaders\HLSL\Outline.hlsl(1,1): error X3000: Illegal character in shader file

4:)  [Fri Feb  8 12:10:35 2019] ERROR: Failed to compile pixel shader Outline(BLURH):
..\Shaders\HLSL\Outline.hlsl(1,1): error X3000: Illegal character in shader file

4:)  [Fri Feb  8 12:10:35 2019] ERROR: Failed to compile pixel shader Outline(BLURV):
..\Shaders\HLSL\Outline.hlsl(1,1): error X3000: Illegal character in shader file

4:)  [Fri Feb  8 12:10:35 2019] ERROR: Failed to compile pixel shader Outline(OUTPUT):
..\Shaders\HLSL\Outline.hlsl(1,1): error X3000: Illegal character in shader file
```

Those errors were due to creating the file in Visual Studio. So deleted that file, and use VSCode to create and then added into the solution. The compile errors when away.

-------------------------

I3DB | 2019-02-08 18:20:18 UTC | #45

[quote="Miegamicis, post:22, topic:1766"]
Code:

```
#include "Uniforms.hlsl"
#include "Samplers.hlsl"
#include "Transform.hlsl"
#include "ScreenPos.hlsl"
#include "PostProcess.hlsl"

uniform float2 vScreenPos;

uniform float4 cOutlineColor;
uniform float2 cOutlineBlurredMaskHInvSize;


void VS(float4 iPos : POSITION,
    out float2 oTexCoord : TEXCOORD0,
    out float2 oScreenPos : TEXCOORD1,
    out float4 oPos : OUTPOSITION)
{
    float4x3 modelMatrix = iModelMatrix;
    float3 worldPos = GetWorldPos(modelMatrix);
    oPos = GetClipPos(worldPos);
    oTexCoord = GetQuadTexCoord(oPos);
    oScreenPos = GetScreenPosPreDiv(oPos);
}

void PS(
    float3 iTexCoord : TEXCOORD0,
    float2 iScreenPos : TEXCOORD1,
    out float4 oColor : OUTCOLOR0)
{
    #ifdef MASK
    oColor = float4(cOutlineColor.rgb, 1);
    #endif

    #ifdef BLURH
        float4 rgba = Sample2D(DiffMap, iScreenPos + float2(0.0, 0.0) * cOutlineBlurredMaskHInvSize);
        oColor = rgba * 0.2;
    #endif

    #ifdef BLURV
        float4 rgba = Sample2D(DiffMap, iScreenPos + float2(0.0, 0.0) * cOutlineBlurredMaskHInvSize);
        oColor = rgba * 0.2;
    #endif


    #ifdef OUTPUT
        float4 blurredMask = Sample2D(DiffMap, iScreenPos);
        float4 mask = Sample2D(NormalMap, iScreenPos);
        float4 viewport = Sample2D(SpecMap, iScreenPos);
        blurredMask = clamp(blurredMask - mask.a, 0.0, 1.0);
        blurredMask *= 200.0;
        oColor = viewport * (1.0 - blurredMask.a) + blurredMask;
    #endif


}
```
[/quote]

@Miegamicis  What you pasted in there is also not following the glsl shader above it.

[What you have checked in](https://github.com/ArnisLielturks/Urho3D-Project-Template/blob/aa5e4d6731159dc58bff45e41d502bf683c39c0d/bin/CoreData/Shaders/HLSL/Outline.hlsl#L35), has that extra semicolon at the end of the line in two places. Otherwise, it looks like the initial glsl shader except as noted in next posts.

Am referring to this glsl from above:
[quote="1vanK, post:3, topic:1766"]
Modified version:
Outline is visible through other objects like Dota 2 and Left 4 Dead 2 (disabled depth test and enabled sorting).
Also some fixes (more correct mixing outline with viewport and more correct blurring).

shader Outline.glsl

```
#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"
#include "ScreenPos.glsl"

varying vec2 vTexCoord;
varying vec2 vScreenPos;

#ifdef COMPILEPS
    uniform vec4 cOutlineColor;
    uniform vec2 cOutlineBlurredMaskHInvSize;
#endif

void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
    gl_Position = GetClipPos(worldPos);
    vTexCoord = GetQuadTexCoord(gl_Position);
    vScreenPos = GetScreenPosPreDiv(gl_Position);
}

void PS()
{
    #ifdef MASK
        gl_FragColor = vec4(cOutlineColor.rgb, 1.0);
    #endif

    #ifdef BLURH
        vec4 rgba = texture2D(sDiffMap, vTexCoord + vec2(0.0, 0.0) * cOutlineBlurredMaskHInvSize) * 0.1;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(-1.0, 0.0) * cOutlineBlurredMaskHInvSize) * 0.2;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(1.0, 0.0) * cOutlineBlurredMaskHInvSize) * 0.4;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(-2.0, 0.0) * cOutlineBlurredMaskHInvSize) * 0.2;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(2.0, 0.0) * cOutlineBlurredMaskHInvSize) * 0.1;
        gl_FragColor = rgba;
    #endif

    #ifdef BLURV
        vec4 rgba = texture2D(sDiffMap, vTexCoord + vec2(0.0, 0.0) * cOutlineBlurredMaskHInvSize) * 0.1;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(0.0, -1.0) * cOutlineBlurredMaskHInvSize) * 0.2;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(0.0, 1.0) * cOutlineBlurredMaskHInvSize) * 0.4;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(0.0, -2.0) * cOutlineBlurredMaskHInvSize) * 0.2;
        rgba += texture2D(sDiffMap, vTexCoord + vec2(0.0, 2.0) * cOutlineBlurredMaskHInvSize) * 0.1;
        gl_FragColor = rgba;
    #endif

    #ifdef OUTPUT
        vec4 blurredMask = texture2D(sDiffMap, vTexCoord);
        vec4 mask = texture2D(sNormalMap, vTexCoord);
        vec4 viewport = texture2D(sSpecMap, vTexCoord);
        blurredMask = clamp(blurredMask - mask.a, 0.0, 1.0);
        gl_FragColor = viewport * (1.0 - blurredMask.a) + blurredMask;
    #endif
}
```
[/quote]

-------------------------

I3DB | 2019-02-08 18:15:23 UTC | #46

Also, you used iScreenPos, and according to GLSL version, that should be iTexCoord.

[Here](https://github.com/ArnisLielturks/Urho3D-Project-Template/blob/aa5e4d6731159dc58bff45e41d502bf683c39c0d/bin/CoreData/Shaders/HLSL/Outline.hlsl#L54-L56).

[And this line makes it all disappear, when I run it.](https://github.com/ArnisLielturks/Urho3D-Project-Template/blob/aa5e4d6731159dc58bff45e41d502bf683c39c0d/bin/CoreData/Shaders/HLSL/Outline.hlsl#L58)

-------------------------

Miegamicis | 2019-02-08 20:08:07 UTC | #47

I actually tried both, bur iScreenPos looked a lot better when I was running some tests. But maybe my testing was bad, since I'm kinda unexperienced with shaders.

-------------------------

I3DB | 2019-02-08 21:41:03 UTC | #48

[quote="Miegamicis, post:47, topic:1766"]
I’m kinda unexperienced with shaders.
[/quote]

Certainly you're more experienced than I. But I do try ...

I'm making some progress. Have the outline painting now, but when it does, then the main material doesn't paint.

Here's the shader I'm using:
```
#include "Uniforms.hlsl"
#include "Samplers.hlsl"
#include "Transform.hlsl"
#include "ScreenPos.hlsl"
#include "PostProcess.hlsl"

#ifdef COMPILEPS
	uniform float4 cOutlineColor;
	uniform float2 cOutlineBlurredMaskHInvSize;
	uniform bool cOutlineEnable;
#endif

void VS(float4 iPos : POSITION,
	out float2 oTexCoord : TEXCOORD0,
	out float2 oScreenPos : TEXCOORD1,
	out float4 oPos : OUTPOSITION)
{
	float4x3 modelMatrix = iModelMatrix;
	float3 worldPos = GetWorldPos(modelMatrix);
	oPos = GetClipPos(worldPos);
	oTexCoord = GetQuadTexCoord(oPos);
	oScreenPos = GetScreenPosPreDiv(oPos);
}

void PS(
	float3 iTexCoord : TEXCOORD0,
	float2 iScreenPos : TEXCOORD1,
	out float4 oColor : OUTCOLOR0)
{
#ifdef MASK
	if (!cOutlineEnable) discard;
	oColor = float4(cOutlineColor.rgb, 1);
#endif
#ifdef BLURH
	float4 rgba = Sample2D(DiffMap, iTexCoord + float2(0.0, 0.0) * cOutlineBlurredMaskHInvSize);
	rgba += Sample2D(DiffMap, iTexCoord + float2(-1.0, 0.0) * cOutlineBlurredMaskHInvSize);
	rgba += Sample2D(DiffMap, iTexCoord + float2(1.0, 0.0) * cOutlineBlurredMaskHInvSize);
	rgba += Sample2D(DiffMap, iTexCoord + float2(-2.0, 0.0) * cOutlineBlurredMaskHInvSize);
	rgba += Sample2D(DiffMap, iTexCoord + float2(2.0, 0.0) * cOutlineBlurredMaskHInvSize);
	oColor = rgba * 0.2;
#endif

#ifdef BLURV
	float4 rgba = Sample2D(DiffMap, iTexCoord + float2(0.0, 0.0) * cOutlineBlurredMaskHInvSize);
	rgba += Sample2D(DiffMap, iTexCoord + float2(0.0, -1.0) * cOutlineBlurredMaskHInvSize);
	rgba += Sample2D(DiffMap, iTexCoord + float2(0.0, 1.0) * cOutlineBlurredMaskHInvSize);
	rgba += Sample2D(DiffMap, iTexCoord + float2(0.0, -2.0) * cOutlineBlurredMaskHInvSize);
	rgba += Sample2D(DiffMap, iTexCoord + float2(0.0, 2.0) * cOutlineBlurredMaskHInvSize);
	oColor = rgba * 0.2;
#endif
#ifdef OUTPUT
	float4 blurredMask = Sample2D(DiffMap, iTexCoord);
	float4 mask = Sample2D(NormalMap, iTexCoord);
	float4 viewport = Sample2D(SpecMap, iTexCoord);
	blurredMask = clamp(blurredMask - mask.a, 0.0, 1.0);
	blurredMask *= 3.0;
	oColor = viewport * (1.0 - blurredMask.a) + blurredMask;
#endif
}
```

Here's the material being used:
```
<material>
  <technique name="Techniques/DiffOutline.xml" />
  <parameter name="MatDiffColor" value=".5 .5 .5 1" />>
  <parameter name="MatSpecColor" value="0.3 0.3 0.3 16" />
  <texture unit="diffuse" name="Textures/StoneDiffuse.dds" />
  <texture unit="normal" name="Textures/StoneNormal.dds" />
  <parameter name="OutlineWidth" value="0.1" />
  <parameter name="OutlineColor" value=".5 .5 .8 1" />
  <parameter name="OutlineEnable" value="true" />
</material>
```

Here's the technique being used:
```
<technique vs="LitSolid" ps="LitSolid" psdefines="DIFFMAP">
  <pass name="base" />
  <pass name="litbase" psdefines="AMBIENT" />
  <pass name="light" depthtest="equal" depthwrite="false" blend="add" />
  <pass name="prepass" psdefines="PREPASS" />
  <pass name="material" psdefines="MATERIAL" depthtest="equal" depthwrite="false" />
  <pass name="deferred" psdefines="DEFERRED" />
  <pass name="depth" vs="Depth" ps="Depth" />
  <pass name="shadow" vs="Shadow1" ps="Shadow1" />
  <pass name="outline" vs="Outline" ps="Outline" psdefines="MASK" depthtest="always" depthwrite="false" />
</technique>
```

Here's the rendererer, called Outline.xml:
```
<renderpath>
  <rendertarget name="outlineMask" sizedivisor="1 1" format="rgba" filter="true" />
  <rendertarget name="outlineBlurredMaskH" sizedivisor="2 2" format="rgba" filter="true" />
  <rendertarget name="outlineBlurredMaskV" sizedivisor="2 2" format="rgba" filter="true" />
  <command type="clear" color="fog" depth="1.0" stencil="0" />
  <command type="clear" color="0 0 0 0" output="outlineMask" />
  <command type="scenepass" pass="base" vertexlights="true" metadata="base" />
  <command type="forwardlights" pass="light" />
  <command type="scenepass" pass="postopaque" />
  <command type="scenepass" pass="refract">
    <texture unit="environment" name="viewport" />
  </command>
  <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" />
  <command type="scenepass" pass="postalpha" sort="backtofront" />
  <command type="scenepass" pass="outline" output="outlineMask" sort="backtofront" />
  <command type="quad" vs="Outline" ps="Outline" psdefines="BLURH" output="outlineBlurredMaskH">
    <texture unit="diffuse" name="outlineMask" />
  </command>
  <command type="quad" vs="Outline" ps="Outline" psdefines="BLURV" output="outlineBlurredMaskV">
    <texture unit="diffuse" name="outlineBlurredMaskH" />
  </command>
  <command type="quad" vs="Outline" ps="Outline" psdefines="OUTPUT" output="viewport">
    <texture unit="diffuse" name="outlineBlurredMaskV" />
    <texture unit="normal" name="outlineMask" />
    <texture unit="specular" name="viewport" />
  </command>
</renderpath>
```

Here are changes to the default render path, which by default only uses 'Forward'.
```
var rp = ((StereoApplication)Application).Renderer.DefaultRenderPath.Clone();
rp.SetEnabled("Forward", false);
rp.Append(Application.ResourceCache.GetXmlFile("RenderPaths/Outline.xml"));
((StereoApplication)Application).Renderer.GetViewport(0).RenderPath = rp;
((StereoApplication)Application).Renderer.GetViewport(1).RenderPath = rp;
```
The two viewports are for the stereo rendering used by hololens, the platform used here.

Screen shot:
![MCS_Photo15-30-16|690x388](upload://kYYI3QyDc3ciqjXv6C7ykUyqLA.jpeg)

The following log outputs are printed:
```
1:)  [Fri Feb  8 16:39:35 2019] DEBUG: Good cleanup, new GameNode being returned
1:)  [Fri Feb  8 16:39:35 2019] DEBUG: Loading resource RenderPaths/Outline.xml
1:)  [Fri Feb  8 16:39:35 2019] DEBUG: Loading resource Models/Cylinder.mdl
1:)  [Fri Feb  8 16:39:35 2019] DEBUG: Loading resource Materials/StoneOutline.xml
1:)  [Fri Feb  8 16:39:35 2019] DEBUG: Loading resource Techniques/DiffOutline.xml
1:)  [Fri Feb  8 16:39:38 2019] DEBUG: Allocated new screen buffer size 1268x720 format 28
1:)  [Fri Feb  8 16:39:38 2019] DEBUG: Allocated new screen buffer size 1268x720 format 28
1:)  [Fri Feb  8 16:39:38 2019] DEBUG: Allocated new screen buffer size 1268x720 format 28
1:)  [Fri Feb  8 16:39:38 2019] DEBUG: Allocated new screen buffer size 634x360 format 28
1:)  [Fri Feb  8 16:39:38 2019] DEBUG: Allocated new screen buffer size 634x360 format 28
1:)  [Fri Feb  8 16:39:38 2019] DEBUG: Compiled vertex shader LitSolid(DIRLIGHT PERPIXEL)
1:)  [Fri Feb  8 16:39:38 2019] DEBUG: Compiled pixel shader LitSolid(AMBIENT DIFFMAP DIRLIGHT PACKEDNORMAL PERPIXEL SPECULAR)
1:)  [Fri Feb  8 16:39:38 2019] DEBUG: Compiled vertex shader LitSolid(PERPIXEL POINTLIGHT)
1:)  [Fri Feb  8 16:39:38 2019] DEBUG: Compiled pixel shader LitSolid(DIFFMAP PACKEDNORMAL PERPIXEL POINTLIGHT SPECULAR)
1:)  [Fri Feb  8 16:39:38 2019] DEBUG: Compiled vertex shader LitSolid(NOUV PERPIXEL POINTLIGHT)
1:)  [Fri Feb  8 16:39:38 2019] DEBUG: Compiled pixel shader LitSolid(PERPIXEL POINTLIGHT)
1:)  [Fri Feb  8 16:39:38 2019] DEBUG: Allocated new screen buffer size 634x360 format 44
1:)  [Fri Feb  8 16:39:38 2019] DEBUG: Loading resource Shaders/HLSL/Outline.hlsl
1:)  [Fri Feb  8 16:39:38 2019] DEBUG: Loaded cached vertex shader Outline()
1:)  [Fri Feb  8 16:39:38 2019] DEBUG: Loaded cached pixel shader Outline(BLURH)
1:)  [Fri Feb  8 16:39:38 2019] DEBUG: Loaded cached pixel shader Outline(BLURV)
1:)  [Fri Feb  8 16:39:38 2019] DEBUG: Loaded cached pixel shader Outline(OUTPUT)
```

-------------------------

I3DB | 2019-02-08 20:56:04 UTC | #49

[quote="I3DB, post:36, topic:1766"]
![MCS_Photo17-18-44.jpg](https://global.discourse-cdn.com/standard17/uploads/urho3d/original/2X/2/2c888e882ccd4aa509b194ac2040b00568528b3c.jpeg)
[/quote]

This is the way it looked before adding the outline, with files I'm using.

Just comparing the two pics, it sort off looks like the outline coloring is the same as the material coloring in the photo, so it wouldn't be seen. Though it is specified to be different.

In that previous pic above, also note the cursor is no longer visible, the cyan torus.

Also in the previous pic, each cylinder is transparent/black and not see through. Farther cylinders can't be seen when looking through a closer one.

-------------------------

ab4daa | 2019-04-13 14:13:09 UTC | #50

I am copycatting the nice effect to my project, and want to share my 2 cents when integrating it.
Hope it could save you some time.

I didn't try original GLSL version but start with the hlsl by @Miegamicis .
My environment: VS2017 + win10 laptop + D3D11 Urho3D.
Some points you may look into when encounter problem:
1. In `#ifdef BLURH` block in PS(); sample the diffuse, render target "outlineMask", with cOutlineBlurredMaskHInvSize is a bit weird. 
Because render target "outlineMask" is as large as viewport, but render target "outlineBlurredMaskH" is only 1/4 size of viewport.
2. The uniform "cOutlineBlurredMaskHInvSize" should be "coutlineBlurredMaskHInvSize", see the render target name in render path.
3. I as a noob try to set cOutlineBlurredMaskHInvSize parameter in material xml when start to integrate. No, it should be auto set by Urho3D in View.cpp, View::RenderQuad().
4. The final `oColor = viewport * (1.0 - blurredMask.a) + blurredMask;` seems doesn't work for me. 
I eventually do an alpha blending like operation: 
`oColor = float4(viewport.rgb * (1.0 - blurredMask.a) + blurredMask.rgb * blurredMask.a, viewport.a);`

[My current HLSL for reference](https://gist.github.com/ab4daa/424140e3c8a98a7d322af4fc22f06324)

screenshot
![%E5%9C%96%E7%89%87|637x499](upload://qvIDuCqnLjgmPzkkHG33nfQ3OS2.png)

-------------------------

