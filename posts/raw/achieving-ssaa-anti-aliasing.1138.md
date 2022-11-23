franck22000 | 2017-01-02 01:05:39 UTC | #1

Hello, 

Im looking to add SSAA anti aliasing technique in my game which consist to render the screen (GBuffer since i am using deffered rendering) at for example 2 times the normal display resolution and then then put it back in normal size.
Just like the Nvidia DSR technology.

I would like to know where the GBuffer is created / defined in Urho3D source code so i can try to add this feature (DirectX 11 desktop). It is a quite common feature in game engines now.

The deferred renderer in Urho3D need some anti-aliasing love i think :slight_smile: 

Thank you !

-------------------------

cadaver | 2017-01-02 01:05:40 UTC | #2

G-buffer setup in deferred rendering is not defined in source code, but in renderpath files

CoreData/RenderPaths/Deferred.xml

Though you can also define renderpaths programmatically. 

With luck what you're aiming to do may even be supported without code changes, you need to create an extra buffer (double size like the albedo/normal/depth) and use it as the output index 0 in all renderpath commands that render the scene and lights. Then, as a final step you blit that into the "viewport" output (backbuffer) with a quad command.

-------------------------

franck22000 | 2017-01-02 01:05:40 UTC | #3

Thank you for the answer Cadaver :slight_smile:

Is it possible to set float sizes for render targets like 0.5 instead of just 1, 2, 4... ?

-------------------------

cadaver | 2017-01-02 01:05:40 UTC | #4

Yes, you can use "size", "sizedivisor" or "sizemultiplier" when defining a target's size in the renderpath, and the last two accept floats.

-------------------------

franck22000 | 2017-01-02 01:05:40 UTC | #5

Alright i think i will need some help here since i am not familiar at all with renderpath handling at the moment :slight_smile: 

I have just created the SSAA render target with a size multiplier of two.

What do i need to do next ? Can you provide me the code if you can please ? :slight_smile: 

[code]<renderpath>

    <rendertarget name="albedo" sizedivisor="1 1" format="rgba" />
    <rendertarget name="normal" sizedivisor="1 1" format="rgba" />
    <rendertarget name="depth" sizedivisor="1 1" format="lineardepth" />
	<rendertarget name="SSAA" sizemultiplier="2 2" format="rgba" />	
	
    <command type="clear" color="fog" depth="1.0" stencil="0" />
	<command type="clear" color="0 0 0 0" output="depth" /> <!-- Fill depth inside skybox area  -->
	
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
	
</renderpath>[/code]

-------------------------

cadaver | 2017-01-02 01:05:41 UTC | #6

This renderpath should work. Note how every command except the final copy is routed to the "ssaa" rendertarget, and both it and the other G-buffer targets are resized to 2x size. The "ssaa" target also needs bilinear filtering enabled so that the CopyFramebuffer shader is able to read it nicely.

[code]
<renderpath>
    <rendertarget name="ssaa" sizemultiplier="2 2" format="rgba" filter="true" />
    <rendertarget name="albedo" sizemultiplier="2 2" format="rgba" />
    <rendertarget name="normal" sizemultiplier="2 2" format="rgba" />
    <rendertarget name="depth" sizemultiplier="2 2" format="lineardepth" />
    <command type="clear" color="fog" depth="1.0" stencil="0" output="ssaa" />
    <command type="scenepass" pass="deferred" marktostencil="true" vertexlights="true" metadata="gbuffer">
        <output index="0" name="ssaa" />
        <output index="1" name="albedo" />
        <output index="2" name="normal" />
        <output index="3" name="depth" />
    </command>
    <command type="lightvolumes" vs="DeferredLight" ps="DeferredLight" output="ssaa">
        <texture unit="albedo" name="albedo" />
        <texture unit="normal" name="normal" />
        <texture unit="depth" name="depth" />
    </command>
    <command type="scenepass" pass="postopaque" output="ssaa" />
    <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" output="ssaa" />
    <command type="scenepass" pass="postalpha" sort="backtofront" output="ssaa" />
    <command type="quad" vs="CopyFramebuffer" ps="CopyFramebuffer" output="viewport">
        <texture unit="diffuse" name="ssaa" />
    </command>
</renderpath>
[/code]

Be prepared for quite a hefty framerate drop, since it's pushing 4x the amount of pixels during rendering.

-------------------------

franck22000 | 2017-01-02 01:05:41 UTC | #7

Thanks a lot ! I really like your support ! 

Of course there is a performance hit. But not so much worse compared to regular MSAA for example. And the SSAA quality is awesome.

-------------------------

