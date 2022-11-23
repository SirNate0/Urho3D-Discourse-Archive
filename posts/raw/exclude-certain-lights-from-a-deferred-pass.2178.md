krstefan42 | 2017-01-02 01:13:42 UTC | #1

The title is pretty self-explanatory. Is it possible to exclude certain lights from a deferred lightvolumes pass?

-------------------------

cadaver | 2017-01-02 01:13:42 UTC | #2

Not without modifying the engine to add a new attribute to the Light class for example.

You can use the low 8 bits of the light mask to exclude objects from receiving deferred light (uses stencil test), but this will still render the volume.

EDIT: checking the light mask for having all zeroes in the low 8 bits would be an easy way to skip a deferred light completely, without having to add anything to Light class. This would be a rather trivial change.

-------------------------

cadaver | 2017-01-02 01:13:42 UTC | #3

That change is in the master branch now.

-------------------------

krstefan42 | 2017-01-02 01:13:42 UTC | #4

Oh, nice! Thank you so much.  :smiley: 

I'm working on an SSAO filter and I want it to affect only the ambient lighting. Problem is, I like to use 3 directional "fill lights" in addition to an ambient term, to give some more depth to the shadows. So I wanted to render the ambient term and fill lights in one pass, apply SSAO, then render in the direct lights. Which I can do now, thanks to you. But now I have a new problem. It looks like the depth buffer is not being properly cleared with the clear command (those streaking artifacts are the result of leftover data in the depth buffer):

[img]https://s10.postimg.org/a03ocf3x5/Depth_Problem.jpg[/img]

This is my RenderPath XML file.
[code]<renderpath>
    <rendertarget name="albedo" sizedivisor="1 1" format="rgba" />
    <rendertarget name="normal" sizedivisor="1 1" format="rgba" />
    <rendertarget name="depth" sizedivisor="1 1" format="lineardepth" />
    <command type="clear" color="fog" depth="1.0" stencil="0" />
    <command type="scenepass" pass="deferred" marktostencil="true" vertexlights="true" metadata="gbuffer">
        <output index="0" name="viewport" />
        <output index="1" name="albedo" />
        <output index="2" name="normal" />
        <output index="3" name="depth" />
    </command>
    <command type="lightvolumes" vs="DeferredLight" ps="DeferredLight">
        <texture unit="albedo" name="albedo" />
        <texture unit="normal" name="normal" />
        <texture unit="depth" name="depth" />
    </command>
    <command type="scenepass" pass="postopaque" />
    <command type="scenepass" pass="refract">
        <texture unit="environment" name="viewport" />
    </command>
    <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" />
    <command type="scenepass" pass="postalpha" sort="backtofront" />
	<command type="quad" tag="SSAO" vs="SSAO" ps="SSAO" output="viewport">
		<texture unit="diffuse" name="viewport" />
        <texture unit="depth" name="depth" />
		<texture unit="normal" name="normal" />
    </command>
</renderpath>
[/code]
Any idea what the problem could be?

-------------------------

cadaver | 2017-01-02 01:13:42 UTC | #5

You could add an additional clear command in the renderpath (clear only works for the index 0 color target, not for multiple targets) or render a fullscreen quad with a custom shader to initialize the whole G-buffer to the wanted values at once.

-------------------------

