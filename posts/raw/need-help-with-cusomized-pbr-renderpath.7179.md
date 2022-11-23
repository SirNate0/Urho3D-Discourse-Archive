Dave82 | 2022-02-01 09:12:08 UTC | #1

So the question is quite complex. I tried to play with PBR materials and i really like the result. I decided to replace materials in my game with PBR materials (if all goes well).
As you may know i'm working on a game that uses pre rendered backgrounds that requires very tricky and complex rendering to make it work. Previously (in ForwardHWDepth) i did work out how to render meshes into Depth map ONLY and even succeeded to make these DepthOnly meshes to cast and receive shadows.

So far i managed to do almost the same with PBR (Rendering in depth only and casting shadows by these depth meshes are working) but i just can manage to figure out how to configure my technique to make these "Depth meshes" receive light and shadows.

This is what i got so far.
Modified version of PBRDeferredHWDepth.xml : 

[code]
<renderpath>
    <rendertarget name="specular" sizedivisor="1 1" format="rgba16f" />
    <rendertarget name="albedo" sizedivisor="1 1" format="rgba16f" />
    <rendertarget name="normal" sizedivisor="1 1" format="rgba16f" />
    <rendertarget name="depth" sizedivisor="1 1" format="readabledepth" />
    <command type="clear" color="0 0 0 0" depth="1.0" stencil="0" depthstencil="depth" />
    <command type="clear" color="0.1 0.7 0.1 0.1" output="albedo" depthstencil="depth"/>
    <command type="clear" color="0 0 0 0" output="specular" depthstencil="depth" />
    <command type="clear" color="0 0 0 0" output="normal" depthstencil="depth" />
	
	<command type="quad" tag="PreRendered" vs="PreRendered" ps="PreRendered" output="viewport" >
		<parameter name="DesaturationPower" value="0.2" />
		<parameter name="BlendPassColor" value="0.2 0.22 0.2 1.0" />
		<parameter name="GrainValue" value="1.0" />
		<parameter name="GrainStrength" value="0.08" />
		<parameter name="ScreenSizeOffset" value="1.0 0.937500007" />
		<parameter name="ScreenScrollOffset" value="0.0 0.0" />
		<texture unit="diffuse" name="viewport" />
		<texture unit="normal" name="cathedral_corridor01_CameraZone001.jpg" />
	 </command>	
	
    <command type="clear" color="0 0 0 0" depth="1.0" output="depth" depthstencil="depth" />
	<command type="scenepass" pass="DepthOnly" output="depth"/>
    <command type="scenepass" pass="base" vertexlights="true" metadata="base" depthstencil="depth" />
    <command type="scenepass" pass="deferred" marktostencil="true" vertexlights="true" metadata="gbuffer" depthstencil="depth">
        <output index="0" name="specular" />
        <output index="1" name="albedo" />
        <output index="2" name="normal" />
    </command>
    <command type="lightvolumes" vs="PBRDeferred" ps="PBRDeferred" psdefines="PBRDEFERRED PBR HWDEPTH" vsdefines="PBR" output="viewport" depthstencil="depth">
        <texture unit="specular" name="specular" />
        <texture unit="albedo" name="albedo" />
        <texture unit="normal" name="normal" />
        <texture unit="depth" name="depth" />
    </command>
    <command type="scenepass" pass="postopaque" depthstencil="depth"/>
    <command type="scenepass" pass="refract" depthstencil="depth">
        <texture unit="environment" name="viewport" />
    </command>
    <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" depthstencil="depth" psdefines="HWDEPTH">
        <texture unit="depth" name="depth" />
    </command>
    <command type="scenepass" pass="postalpha" sort="backtofront" depthstencil="depth" />
</renderpath>
[/code]

The rendering works like this : 
-First i render my background (The PReRendered pass above)
-Then i clear the depth
-Then i render the depth meshes (this pass writes only in depth map and leave all the pixel information on the screen untouched)
-Finally render everything else.
 
My TEchnique for depth pass only looks like this

[code]
<technique>
	<pass name="DepthOnly" vs="Depth" ps="Depth"/>
	<pass name="light" vs="PBRLitSolid" ps="PBRLitSolid" psdefines="DIFFMAP PBR IBL" blend="subtract" />
	<pass name="shadow" vs="Shadow" ps="Shadow" />
</technique>
[/code]
The shadow pass is working the invisible Depth meshes cast shadows properly on regular meshes but the light pass is wrong because the depth meshes can't receive lights nor shadows. Any idea how to fix this ? Or is it even possible ?
Thanks !

-------------------------

Dave82 | 2022-02-01 14:25:13 UTC | #2

Found the problem !!! I defined the light pass in the technique but the renderpath had no light pass defined so it never happened. Added and it works as expected.

This is why i still think Urho3d is the best engine out there ! Easy to use , easy to expand and easy to modify.
The creativity ,experience and talent of the developers are amazing !
Keep up the good work !

-------------------------

Dave82 | 2022-02-02 18:33:35 UTC | #3

Some short video of this in action. The background is a 2d image and there is a floor plane that is rendered into depth map only and exists only to receive shadows. PBR looks awesome. Maybe it's not optimized for large complex levels but in my use case with few models per segment will do the job perfectly

https://www.youtube.com/watch?v=C3htGfzdPy0

-------------------------

GodMan | 2022-02-03 17:35:34 UTC | #4

@Dave82 Looks great. I've always wanted to try pbr shaders in a urho3d project. I was always under the impression that they are real demanding on your hardware, and not such great performance.

-------------------------

