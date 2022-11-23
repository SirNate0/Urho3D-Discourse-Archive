cosar | 2019-12-15 18:05:35 UTC | #1

HI,

I created a new rendertarget (named layer) for base scenepass and I'm setting the perpixel values in a custom shader. My renderpath looks like this:
```
<renderpath>
    <rendertarget name="layer" sizedivisor="1 1" format="rgb" />
    <command type="clear" color="1 0 0 0" output="layer" />
    <command type="clear" color="fog" depth="1.0" stencil="0" />
    <command type="scenepass" pass="base" vertexlights="true" metadata="base">
        <output index="0" name="viewport" />
        <output index="1" name="layer" />
    </command>
    <command type="forwardlights" pass="light"/>
    <command type="scenepass" pass="postopaque" />
    <command type="scenepass" pass="refract">
        <texture unit="environment" name="viewport" />
        <texture unit="5" name="layer" />
    </command>
    <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" />
    <command type="scenepass" pass="postalpha" sort="backtofront" />
</renderpath>
```
I removed litbase from the technique, so It's always using base scenepass.
The issue is that everything works as expected on a Nvidia RTX 2060 card, but it does not work properly on Nvidia GTX 960M.
On GTX 960M, the changes made in base scenepath for layer rendertarget looks like they are ignored.
I'm using DirectX 11.

Thank you!

-------------------------

