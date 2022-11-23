evolgames | 2020-08-26 02:15:44 UTC | #1

Hey guys, I've been messing around with glsl bloom and greyscale.
I'm able to get both to work. I can toggle them on which is great.
I want to fade in the greyscale, though, not just toggle it on. I've tried for a while today to do SetShaderParameter but it's just not working.
My use case is fading this in (from full color to full monochrome) and back out in-game.

Below is my xml which is bloom, an unused pixellation effect, and greyscale mashed together. Like I said, it works fine toggling on and off the Grey tag via:
```
effectRenderPath:SetEnabled("Grey", true)
```
But this requires the values (swapping rgb for intensity) to be preset in the GreyScale.glsl file. I need to change those values during gameplay.

BloomGreyScale.xml
```
<renderpath>
	<rendertarget name="buffer" sizedivisor="1 1" filter="false"/> 
    <command type="clear" color="fog" depth="1.0" stencil="0" output="buffer"/>
    <command type="scenepass" pass="base" vertexlights="true" metadata="base" output="buffer" />
    <command type="forwardlights" pass="light" output="buffer" />
    <command type="scenepass" pass="postopaque" output="buffer" />
    <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" output="buffer" />
    <command type="scenepass" pass="postalpha" sort="backtofront" output="buffer" />
	<command type="quad" tag="Grey" vs="CopyFramebuffer" ps="GreyScale" output="viewport">
		<parameter name="Greyness" value="1 1 1" />
		<texture unit="diffuse" name="buffer" />
	</command>
	    <rendertarget name="blurv" tag="Bloom" sizedivisor="6 6" format="rgb" filter="true" />
    <rendertarget name="blurh" tag="Bloom" sizedivisor="6 6" format="rgb" filter="true" />
    <command type="quad" tag="Bloom" vs="Bloom" ps="Bloom" psdefines="BRIGHT" output="blurv">
        <parameter name="BloomThreshold" value="0.3" />
        <texture unit="diffuse" name="viewport" />
    </command>
    <command type="quad" tag="Bloom" vs="Bloom" ps="Bloom" psdefines="BLURH" output="blurh">
        <texture unit="diffuse" name="blurv" />
    </command>
    <command type="quad" tag="Bloom" vs="Bloom" ps="Bloom" psdefines="BLURV" output="blurv">
        <texture unit="diffuse" name="blurh" />
    </command>
    <command type="quad" tag="Bloom" vs="Bloom" ps="Bloom" psdefines="COMBINE" output="viewport">
        <parameter name="BloomMix" value="1 .5" />
        <texture unit="diffuse" name="viewport" />
        <texture unit="normal" name="blurv" />
    </command>
</renderpath>
```

I tried modifying the CoreData/Shaders/GreyScale file:
```
#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"
#include "ScreenPos.glsl"
#include "Lighting.glsl"

varying vec2 vScreenPos;

uniform vec3 cGreyness;

void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
    gl_Position = GetClipPos(worldPos);
    vScreenPos = GetScreenPosPreDiv(gl_Position);
}

void PS()
{

    vec3 rgb = texture2D(sDiffMap, vScreenPos).rgb;
    float intensity = GetIntensity(rgb)-cGreyness.x;
    gl_FragColor = vec4(vec3(cGreyness), 1.0);

}
```
Now, I know the above won't actually make the intended monochrome effect, it'll be a flat color on the whole screen. I can do the math (blending the rgb and intensity values together with the 'greyness' variable) later. I just need to make sure I can send 'greyness' in the first place.

And in game I've tried variations of:
```
effectRenderPath:SetShaderParameter("Greyness",Vector3(1,1,1))
```
But no matter what I try, floats or vectors, I can't seem to actually pass the value to the shader. If I set the value in the shader file manually it works, but to blend the monochrome I need to obviously set it live.

If I set cGreyness vec3 in GreyScale.glsl to Vec3(1,1,1) it'll be flat white, as it should. 0,0,0 would be flat black. However I get a blackscreen no matter what I do with the SetShaderParameter.

Any ideas what it might be?

-------------------------

Eugene | 2020-08-26 09:42:02 UTC | #2

Does it work when you set arbitrary color in renderpath XML?
If yes, try setting color in XML _and_ setting different color in the code. What happens in this scenario?

-------------------------

Avagrande | 2020-08-26 14:59:04 UTC | #3

try 
`    effectRenderPath:SetShaderParameter("Greyness",Variant(Vector3(1,1,1)))`

-------------------------

evolgames | 2020-08-26 15:06:33 UTC | #4

ahhhh that was it, I'm an idiot. The irony is I have that same Variant syntax elsewhere for materials, just overlooked it. Works perfectly.
Usually if I do something like this, like feeding a vector instead of a quarternion, I'll get a segfault or an error. In this case I guess the shader just ignored this value since I didn't get any console messages?

-------------------------

Avagrande | 2020-08-26 15:23:08 UTC | #5

this is the fault of lua wrappers I think. It should work like that but it doesn't and you get no error. Lua as a whole is sadly neglected in urho3d and has many [issues](https://discourse.urho3d.io/t/lua-animated-model-is-not-a-drawable/6322) personally I very rarely get answers to many of these. I often have to delve into tolua++ and just diy parts of it. 

Have you compiled with safe lua? it may help but produce false errors and you often cant trust the lua part anyway since its a second class citizen as far as urho3d is concerned.  kind of sucks :( 

I am not entirely sure what it does if you just pass the vector but I assume it fails to convert it correctly and fails silently. I haven't had a segfault over a variant before though.

-------------------------

evolgames | 2020-08-26 17:51:42 UTC | #6

Ah yeah, I have the same issues but fortunately nothing that has stopped my progress too much. I did SafeLua before but have since reinstalled my OS and I forgot to this time around. I just try not to make any mistakes, lol. I don't recall if safelua helped that much anyway.

-------------------------

