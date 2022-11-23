TheComet | 2017-01-02 01:14:34 UTC | #1

In an effort to understand Urho3D's rendering, I've decided to try and write my own custom renderpath, technique and shader. My aim right now is to implement simple phong shading with parallax mapping using forward rendering.

Everything works, except that it only works for one light. If my scene has 2 (or more) lights, how do I tell Urho to render the scene as many times as there are lights, use a different light every pass, then blend them together?

[b]Custom.xml[/b]
[code]<renderpath>
    <command type="clear" color="fog" depth="1.0" stencil="0" />
    <command type="scenepass" pass="base" />
    <command type="forwardlights" pass="light" />
</renderpath>[/code]

[b]Parallax.xml[/b]
[code]<technique vs="Phong_VS" ps="Phong_PS">
    <pass name="light" />
</technique>[/code]

I don't think there's any need to post Phong_VS.glsl and Phong_PS.glsl at this point, but I should note that I am using [b]cLightPosPS[/b] and [b]cLightDirPS[/b] for my lighting calculations, and I am [b]not[/b] using [i]GetVertexLight()[/i].

-------------------------

cadaver | 2017-01-02 01:14:35 UTC | #2

Your minimal technique for forward lighting with multi lights should look like this:

[code]
<technique vs="MyShader" ps="MyShader">
    <pass name="base" />
    <pass name="light" depthtest="equal" depthwrite="false" blend="add" />
</technique>
[/code]
The light pass will be called for each light by the forwardlights command, and you need to manually configure additive blending for it. Otherwise each light overwrites the previous.
You also need the base pass for the ambient light / absence of any light.

The rendering will use the shader defines PERPIXEL and DIRLIGHT / SPOTLIGHT / POINTLIGHT for the light pass; you can use the absence of these to detect that it should render ambient instead.

-------------------------

TheComet | 2017-01-02 01:14:37 UTC | #3

Ok cool, got that to work.

What about multiple passes of the same type in a single technique? For instance, a fur shader will typically render the same object 10-30 times and move each vertex along its normal further every pass. Something like this:

[code]<technique vs="Fur_VS" ps="Fur_PS">
    <pass name="base" vsdefines="FUR_HEIGHT=0" />
    <pass name="litalpha" depthtest="lessequal" depthwrite="true" blend="addalpha" vsdefines="FUR_HEIGHT=1" />
    <pass name="litalpha" depthtest="lessequal" depthwrite="true" blend="addalpha" vsdefines="FUR_HEIGHT=2" />
    <pass name="litalpha" depthtest="lessequal" depthwrite="true" blend="addalpha" vsdefines="FUR_HEIGHT=3" />
    <pass name="litalpha" depthtest="lessequal" depthwrite="true" blend="addalpha" vsdefines="FUR_HEIGHT=4" />
    <pass name="litalpha" depthtest="lessequal" depthwrite="true" blend="addalpha" vsdefines="FUR_HEIGHT=5" />
    <pass name="litalpha" depthtest="lessequal" depthwrite="true" blend="addalpha" vsdefines="FUR_HEIGHT=6" />
    <pass name="litalpha" depthtest="lessequal" depthwrite="true" blend="addalpha" vsdefines="FUR_HEIGHT=7" />
    <pass name="litalpha" depthtest="lessequal" depthwrite="true" blend="addalpha" vsdefines="FUR_HEIGHT=8" />
</technique>[/code]

As far as I can tell, only the last pass and the base pass is being executed and the 7 passes in between are overwritten.

-------------------------

cadaver | 2017-01-02 01:14:37 UTC | #4

You can't define a pass with the same name multiple times, as it's going to get overwritten. Also, alpha rendering is kind of hardcoded to first render the base pass and then the litalpha pass immediately after, in the objects' back-to-front order, so I'm afraid multiple alpha passes with an increasing parameter are not going to work satisfactorily. You could look into the rendering code (View / Batch classes) to see if you can make a tweak into the logic, but I'm not certain it will be feasible.

-------------------------

