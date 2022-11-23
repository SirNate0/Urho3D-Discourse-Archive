Sinoid | 2019-02-06 02:10:10 UTC | #1

Loosely inspired by the Unity-chan shaders with a few extra niceties like MSDF *ink lines* and geometry-shader outline emission.

![Blocks_2019-02-05_16-40-15|406x349](upload://9Igg8NYLIHuX06gppou2ySYSajZ.jpeg) 
Above: MSDF for the black lines inside, 3 step tone-map, white rim-highlight, and GS-emitted outline.

**Requirements**

- Colormap (texture 0)
- ToneMap (texture 7)
     - controls the shade falloff
     - leftmost is perpendicular, rightmost is aligned to the light direction

**Options**

- Hair highlight ring (cylindrical matcap basically)
    - tex 4
- Matcap / Spherical environment map
    - tex 4
- Rim highlight (TOON_RIMLIGHT)
- MSDF Linework map for sharp sketch lines (TOON_LINE_MAP)
    - tex 5
- Control map (force light/dark)
    - tex 3
    - **R**: min allowed shade, **G**: max allowed shade, **B**: unused, **A**: matcap mask
- Vertical shade map
    - Clips maximum possible lighting, like the control map can
         - Nx1 texture is silly quick to update at runtime for changes (hat shadow, etc)
    - provide size coordinates for normalization to `VerticalRampShift` parameter
- Specular is used as per legacy pipeline
    - not toon clipped in any way, it's *special*

`Toon.hlsl` contains documentation at the top.

**Outlines**

- Geometry shader outlines included (if you have GS support)
    - emits flipped winding triangles
- `Toon_Outline.hlsl` can be used in an additional render-path pass (with the culling flipped) to do outlines with the same config
    - `OutlinePower`: **x** = offset along normal, **y** = offset along view-vector

https://gist.github.com/JSandusky/4f9a4f00110691eb45104f69abd32f75

Shouldn't be too much cruft in there. Tessellation (lots of code no one can use) and light-prepass stripped out (not for stock prepass, would be confusing to look at).

I'll probably port to GLES3 and GL3.1 (interface blocks)

-------------------------

I3DB | 2019-02-06 02:31:10 UTC | #2

Do you have a material that uses this you could share? 

Or a simple working sample.

-------------------------

Sinoid | 2019-02-06 02:49:22 UTC | #3

Here's the technique I start with when fiddling with it:

```
<technique vs="Toon" ps="Toon" psdefines="TOON_LINE_MAP" vsdefines="">
    <pass name="base" />
    <pass name="outline" vs="Toon_Outline" ps="Toon_Outline" cull="cw" />
    <pass name="light" depthtest="equal" depthwrite="false" blend="add" />
    <pass name="depth" vs="Depth" ps="Depth" />
    <pass name="shadow" vs="Shadow" ps="Shadow" />
    
    <alias unit="0" name="Color" />
    <alias unit="1" name="Normal Map" />
    <alias unit="2" name="Specular Map" />
    <alias unit="3" name="Control Map" />
    <alias unit="4" name="MatCap / Hair-Ring" />
    <alias unit="5" name="Linework" />
    <alias unit="6" name="Vertical Shade" />
    <alias unit="7" name="Tone Map" />
</technique>
```

I plan to put together a sample scene but I need to write an appropriate environment toon-shader to go with all of this. This shader isn't particularly great for anything that isn't a first-class object (ie. saturation and extinction/inscattering for that cartoon background fade, etc). Probably have one ready by the weekend.

The alias tags up there are for my editor, left them there though because they do a good job of indicating what different samplers do.

MSDFs for the line maps have been generated with https://github.com/Chlumsky/msdfgen

-------------------------

