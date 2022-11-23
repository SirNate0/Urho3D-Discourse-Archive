ghidra | 2017-01-02 01:14:59 UTC | #1

I'm having some issue I cant seem to correct.

The docs have this:
[code]
<command type="scenepass" pass="PassName" sort="fronttoback|backtofront" marktostencil="true|false" vertexlights="true|false" metadata="base|alpha|gbuffer" depthstencil="DSName">
        <output index="0" name="RTName1" face="0|1|2|3|4|5" />
        <output index="1" name="RTName2" />
</command>
[/code]

There is an example done up on the forums by 1vanK that does it this way:
[code]
<command type="scenepass" pass="outline" output="outlineMask" sort="backtofront" />
[/code]

However... I have tried using both ways... and I am not getting the results I expect. I also tried to clear the pass with red (1 0 0 0) to see if something is happeneing. I get red... but when the scenepass comes around... it does not write into the target.

Now I know that the scenepass is "rendering" because what I am doing now... is rendering to the viewport, then passing that into a quad
[code]
<command type="scenepass" tag="LBM" pass="lbminjection" sort="backtofront" metadata="base" />
<command type="quad" tag="LBM" vs="Quad" ps="LBM_Injection" output="lbminput" >
	<texture unit="diffuse" name="viewport" />
</command>
[/code]

but i feel like that is not right... i should be able to just go straight to the output?
Can someone tell me what I might be getting wrong..

Here is a trimmed down version of my renderpath:
[code]
<renderpath>
     <rendertarget name="lbminput" tag="LBM" sizedivisor="1 1" format="rgba16f" />
     <command type="clear" color="0 0 0 0" output="lbminput" />
     <command type="scenepass" tag="LBM" pass="lbminjection" sort="backtofront" metadata="base" />
     <command type="quad" tag="LBM" vs="Quad" ps="LBM_Injection" output="lbminput" >
          <texture unit="diffuse" name="viewport" />
     </command>
<!--now add it all together -->
     <command type="quad" tag="LBM" vs="Quad" ps="LBM_Render" output="viewport">
          <texture unit="1" name="lbminput" />
     </command>
[/code]

This is what I would rather do:
[code]
<renderpath>
     <rendertarget name="lbminput" tag="LBM" sizedivisor="1 1" format="rgba16f" />
     <command type="clear" color="0 0 0 0" output="lbminput" />
     <command type="scenepass" tag="LBM" pass="lbminjection" sort="backtofront" metadata="base" output="lbminput" />
<!--now add it all together -->
     <command type="quad" tag="LBM" vs="Quad" ps="LBM_Render" output="viewport">
          <texture unit="1" name="lbminput" />
     </command>
[/code]

-------------------------

