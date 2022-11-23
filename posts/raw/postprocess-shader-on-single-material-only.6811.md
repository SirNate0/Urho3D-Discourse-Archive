evolgames | 2021-04-16 05:22:19 UTC | #1

So I've got this edge detection that I really like. It's done with a ForwardDepth render path and a shader. Currently (in the screenshot), I've appended the viewport with the renderpath that calls the edge detection shader. No techniques or special materials needed.

However, I don't want it to apply to everything. I've tried to reimplement this as a technique called from a material but I'm not sure if I leave the renderpath as is or put that in the technique? This is what I've tried, I feel like I'm close.

**ForwardDepth.xml**
```
<renderpath>
    <rendertarget name="depth" sizedivisor="1 1" format="readabledepth" />
    <command type="clear" color="fog" depth="1.0" stencil="0" depthstencil="depth" />
    <command type="scenepass" pass="base" vertexlights="true" metadata="base" depthstencil="depth" />
    <command type="forwardlights" pass="light" depthstencil="depth" />
    <command type="scenepass" pass="postopaque" depthstencil="depth" />
    <command type="scenepass" pass="refract" depthstencil="depth">
        <texture unit="environment" name="viewport" />
    </command>
	<command type="quad" tag="edge_detect" vs="edge_detect" ps="edge_detect">
		<parameter name="EdgeThreshold" value="0.0002" />
        <parameter name="EdgeColor" value="0 0 0 1" />
        <texture unit="diffuse" name="viewport" />
        <texture unit="emissive" name="depth" />
    </command>
</renderpath>
```
I tried this as a Technique (doesn't do anything, though):
**Outliner.xml**
```
<technique vs="edge_detect" ps="edge_detect" >
    	<pass name="EdgeThreshold" value="0.0001" />
        <pass name="EdgeColor" value="0 0 0 1" />
        <texture unit="diffuse" name="viewport" />
        <texture unit="emissive" name="depth" />
</technique>
```
And the color palette material calls it here:
**Palette.xml**
```
<?xml version="1.0"?>
<material>
		<technique name="Techniques/Diff.xml" />
		<technique name="Techniques/Outliner.xml" />
			<texture unit="diffuse" name="Textures/palette.png" />
</material>
```

Shader applied to everything:
![Screenshot_2021-04-16_00-10-19|690x388](upload://gqMKzdTmwOCJgKEFEpgOY5ptF55.png)

-------------------------

JSandusky | 2021-04-18 21:55:00 UTC | #2

If you can do your effect as in-painting (within the confines of the drawn geometry) then just use another scene-pass with depthtest set to equal that'll only draw things with a material containing your postfx technique. You'll have to modify your shader too as it's no longer going to be a simple postfx pixel shader.

If you can't do it with in-painting then you have to modify the engine itself (and data-formats for materials/render-paths) to support stencil refs.

-------------------------

evolgames | 2021-04-18 23:40:33 UTC | #3

Oh okay, hmm. I'll give that a try, thanks. If not I guess I'll just settle for the edge detection on everything.

-------------------------

JSandusky | 2021-04-19 07:19:00 UTC | #4

The other alternative is setting up another target to render your edge-detection stuff into as a mask and then have your postfx shader refer to that.

That's more expensive then either using stencil for masking or in-painting but does have more you can do.

-------------------------

