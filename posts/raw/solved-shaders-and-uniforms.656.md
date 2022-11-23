hdunderscore | 2017-01-02 01:01:55 UTC | #1

I am working on a shader and I'd like to use 2 environment cubemaps (hlsl pixel shader, forward render path). I've got the first one in using the regular sEnvCubeMap, but I can't seem to figure out how to either add a new cube map uniform or how to use an existing one. 

This is what my technique looks like:
[code]<?xml version="1.0" encoding="utf-8"?>
<technique vs="Lux" ps="Lux" psdefines="DIFFMAP ENVCUBEMAP">
    <pass name="base" />
    <pass name="litbase" />
    <pass name="light" depthtest="equal" depthwrite="false" blend="add" />
    <pass name="prepass" psdefines="PREPASS" />
    <pass name="material" psdefines="MATERIAL" depthtest="equal" depthwrite="false" />
    <pass name="deferred" psdefines="DEFERRED" />
    <pass name="depth" vs="Depth" ps="Depth" />
    <pass name="shadow" vs="Shadow" ps="Shadow" />
</technique>
[/code]

This is what my material looks like:
[code]<?xml version="1.0"?>
<material>
	<technique name="Techniques/Lux/BumpedDiffuse.xml" quality="0" loddistance="0" />
	<texture unit="diffuse" name="Textures/Cloth_Unity_Immortal_diffuse.tga" />
	<texture unit="normal" name="Textures/Cloth_Unity_Immortal_normal.tga" />
	<texture unit="specular" name="Textures/Cloth_Unity_Immortal_specular.tga" />
	<texture unit="environment" name="Textures/diffcube.dds" />
	<texture unit="13" name="Textures/speccube.dds" />
	<parameter name="UOffset" value="10 0 0 0" />
	<parameter name="VOffset" value="0 10 0 0" />
	<parameter name="MatDiffColor" value="1 1 1 1" />
	<parameter name="MatEmissiveColor" value="0 0 0" />
	<parameter name="MatEnvMapColor" value="1 1 1" />
	<parameter name="MatSpecColor" value="0 0 0 1" />
	<cull value="ccw" />
	<shadowcull value="ccw" />
	<depthbias constant="0" slopescaled="0" />
</material>
[/code]

-------------------------

cadaver | 2017-01-02 01:01:55 UTC | #2

Materials are currently limited to the first 5 texture units. This is a limitation that stems from some OpenGL ES devices only having 8 texture units, so first 5 are material, 5-7 are light properties and 8- are deferred buffers. It should be doable, however, to allow a material to assign any texture unit, with the risk that you may mess up the render state in ways the Renderer / View classes are not prepared for.

-------------------------

codingmonkey | 2017-01-02 01:01:55 UTC | #3

>I am working on a shader and I'd like to use 2 environment cubemaps 

and second cubemap for what ?
you're trying to do something like this ?:
see part @Reflection system in:
[fxguide.com/featured/game-en ... rendering/](http://www.fxguide.com/featured/game-environments-parta-remember-me-rendering/)
it's some like an the blending cubemap system, in video currently blended cubemaps shown as green lines.

-------------------------

cadaver | 2017-01-02 01:01:55 UTC | #4

If you pull latest master, now material can assign to any texture unit. The units that aren't named can be referred to with numbers, like you were already doing.

-------------------------

hdunderscore | 2017-01-02 01:01:56 UTC | #5

Thanks for that -- I can now continue with the shader when I switch to texture unit 14 and declare a sampler like this:
[code]samplerCUBE sSpecEnvMap : register(S14);[/code]However like you say, I don't necessarily want to break the 8 texture unit limit -- if I wanted to replace the existing samplers, would it be enough to make the change in Samplers .hlsl/glsl and other shaders, or would I have to make changes in engine ?

[quote="codingmonkey"]>I am working on a shader and I'd like to use 2 environment cubemaps 

and second cubemap for what ?
you're trying to do something like this ?:
see part @Reflection system in: -link-
it's some like an the blending cubemap system, in video currently blended cubemaps shown as green lines.[/quote]I am porting over these shaders: [github.com/larsbertram69/Lux](https://github.com/larsbertram69/Lux)

Maybe later I will reduce to one cube map, but those shaders use two (one for diffuse ibl, one for specular ibl).

-------------------------

cadaver | 2017-01-02 01:01:57 UTC | #6

If you want the engine to assign some of the inbuilt texture units differently, like the light ramp or shadow map, then you have to modify GraphicsDefs.h, otherwise you can just keep using samplers like you want.

Actually we could do that change in master, for example to assign the light textures to the bottom of 16 units on desktops, and bottom of 8 on mobiles. That way we'd have a nice continuous space for material texture units. The only downside is that some symbols for scripting would change value depending on platform, and if you eg. precompiled AngelScript and used the texture unit symbolic names (though in general script shouldn't be messing with engine reserved texture units) then precompiled AngelScript would have wrong values on mobiles.

-------------------------

hdunderscore | 2017-01-02 01:01:58 UTC | #7

Ok, looks like it's simple to change the in-built texture units via GraphicsDefs.h so I'll go with that option.

Maybe that suggested change is a good idea, although even then I'll probably still change GraphicsDefs.h as I think I'll be using the zone texture for this second cubemap. It makes it that slight bit harder to distribute these shaders (and maintain compatibility with existing shaders), but again no big deal.

-------------------------

