Askhento | 2020-12-13 22:45:58 UTC | #1

I want to make freeze frame effect. Idea is to mix current frame with previous frame which I save to renderTarget. 
Trying to use CopyFrameBuffer.xml renderPath, but it is always black. 

```
<renderpath>
    <rendertarget  name="freezeFrame" sizedivisor="1 1" format="rgba" filter="true" />
    <command type="quad" vs="MyCopyFramebuffer" ps="MyCopyFramebuffer" output="freezeFrame" tag="freezeFrame">
        <texture unit="diffuse" name="viewport" />
        <texture unit="normal" name="freezeFrame"/>
    </command>
    <command type="quad" vs="CopyFramebuffer" ps="CopyFramebuffer" output="viewport">
        <texture unit="diffuse" name="freezeFrame" />
    </command>
</renderpath>    
```

-------------------------

Eugene | 2020-12-14 10:22:47 UTC | #2

AutoExposure post process does pretty much what you need, check it out.
You need persistent RT, otherwise it's not preserved between frames.

-------------------------

Askhento | 2020-12-15 20:22:12 UTC | #3

Ok, now I set renderTarget to persistent and get the result, kind of. Now everything is gray). MyCopyFrameBuffer just use mix with ratio 0.5.
```
<renderpath>
    <rendertarget  name="freezeFrame" tag="FreezeFrame"  sizedivisor="1 1" format="rgba" filter="false" persistent="true"/>
    <rendertarget  name="prevFreezeFrame" tag="FreezeFrame"  sizedivisor="1 1" format="rgba" filter="false"/>

    <command type="quad" tag="FreezeFrame" vs="CopyFramebuffer" ps="CopyFramebuffer" output="prevFreezeFrame">
        <texture unit="diffuse" name="freezeFrame" />
    </command>

    <command type="quad" tag="FreezeFrame" vs="MyCopyFramebuffer" ps="MyCopyFramebuffer" output="viewport">
        <texture unit="diffuse" name="viewport" />
        <texture unit="diffuse" name="prevFreezeFrame" />
    </command>

    <command type="quad" tag="FreezeFrame" vs="CopyFramebuffer" ps="CopyFramebuffer" output="freezeFrame">
        <texture unit="diffuse" name="viewport" />
    </command>

</renderpath>    
```

-------------------------

SirNate0 | 2020-12-15 21:35:06 UTC | #4

This looks suspicious to me
[quote="Askhento, post:3, topic:6615"]
```
<command type="quad" tag="FreezeFrame" vs="MyCopyFramebuffer" ps="MyCopyFramebuffer" output="viewport">
        <texture unit="diffuse" name="viewport" />
        <texture unit="diffuse" name="prevFreezeFrame" />
    </command>
```
[/quote]
You have two things that are both claiming to be the diffuse texture unit.

-------------------------

Askhento | 2020-12-15 22:25:13 UTC | #5

Changed to normal. 
You saved me)

-------------------------

