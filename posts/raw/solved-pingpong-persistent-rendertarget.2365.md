ghidra | 2017-01-02 01:15:00 UTC | #1

the docs say:
[quote]
It is legal to both write to the destination viewport and sample from it during the same command: pingpong copies of its contents will be made automatically. If the viewport has hardware multisampling on, the multisampled backbuffer will be resolved to a texture before sampling it.
[/quote]

I assume this means only the viewport, not any custom rendertarget?

i want to do this:
[code]
<rendertarget name="advect" tag="LBM" sizedivisor="1 1" format="rgba16f" persistent="true" filter="true" />
<command type="quad" tag="LBM" vs="Quad" ps="LBM_Advect"  output="advect">
	<texture unit="diffuse" name="lbm" />
	<texture unit="1" name="advect" />
</command>
[/code]
But that seems not to work.

But it does work if i do this:
[code]
<rendertarget name="advect1" tag="LBM" sizedivisor="1 1" format="rgba16f" persistent="true" filter="true" />
<rendertarget name="advect2" tag="LBM" sizedivisor="1 1" format="rgba16f" persistent="true" filter="true" />

<command type="quad" tag="LBM" vs="Quad" ps="LBM_Advect" output="advect1">
	<texture unit="diffuse" name="lbm" />
	<texture unit="1" name="advect2" />
</command>
<command type="quad" tag="LBM" vs="Quad" ps="LBM_Advect" output="advect2">
	<texture unit="diffuse" name="lbm" />
	<texture unit="1" name="advect1" />
</command>
[/code]

But now, I am doing this twice per frame... and if I want to do this to more than one target... it starts to inflate pretty fast.
Am i approaching this right? Is there a better approach?

-------------------------

cadaver | 2017-01-02 01:15:00 UTC | #2

Automatic pingpong indeed only happens for the destination rendertarget. Any additional targets you will need to manage yourself by having 2 copies like in your latter approach. From that you see what the viewport pingponging is actually doing behind the scenes.

If you have multiple effects chained together, you can probably share buffers between them (in case their size is compatible), and thus don't need 2 more buffers for each added effect.

-------------------------

