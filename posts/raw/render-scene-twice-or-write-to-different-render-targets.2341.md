TheComet | 2017-01-02 01:14:50 UTC | #1

In my game, objects have an emissive map. I want to render all objects just with emissive maps to a separate render target in addition to rendering the scene "normally".

How do I do this?

Here is my render path:
[code]<renderpath>
    <!-- The emissive maps are rendered to this target -->
    <rendertarget name="RTEmissive" sizedivisor="1 1" format="rgba16f" />

    <command type="clear" color="fog" depth="1.0" stencil="0" output="viewport" />
    <command type="clear" color="fog" depth="1.0" output="RTEmissive" />

    <!-- Render scene normally, then do a pass for every light -->
    <command type="scenepass" pass="base">
        <output index="0" name="viewport" />
        <output index="1" name="RTEmissive" />
    </command>
    <command type="forwardlights" pass="light" />

    <!-- Alpha is currently not needed
    <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" />
    <command type="scenepass" pass="postalpha" sort="backtofront" />
    -->

    <command type="scenepass" pass="refract">
        <texture unit="environment" name="viewport" />
    </command>

    <!--  -->
    <command type="quad" vs="BloomEmissive" ps="BloomEmissive" output="viewport">
        <texture unit="diffuse" name="RTEmissive" />
    </command>
</renderpath>
[/code]

I'm trying to write to gl_FragData[1] (which, from what I understand, would be RTEmissive in the base scene pass), but then the viewport just goes black.

My glsl code is pretty much this:
[code]void PS()
{
     /* a whole bunch of shit */

    gl_FragData[0] = finalColor;
#if defined(PREPASS)
    gl_FragData[1] = emissiveMap;
#endif
}[/code]

And my BloomEmissive shader is currently this (copy RTEmissive framebuffer to viewport):
[code]void PS()
{
    gl_FragColor = vec4(texture2D(sDiffMap, vScreenPos).rgb, 1);
}[/code]

-------------------------

artgolf1000 | 2017-01-02 01:14:51 UTC | #2

You may refer to [url]https://github.com/MonkeyFirst/urho3d-light-scattering[/url], there are lot of things to setup correctly.

-------------------------

