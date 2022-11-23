Lunarovich | 2021-06-04 11:18:34 UTC | #1

Hello! I've been toying around with shaders and I'm trying to understand these two functions:

vec4 GetScreenPos(vec4 clipPos)

```
{
    return vec4(
        clipPos.x * cGBufferOffsets.z + cGBufferOffsets.x * clipPos.w,
        clipPos.y * cGBufferOffsets.w + cGBufferOffsets.y * clipPos.w,
        0.0,
        clipPos.w);
}

vec2 GetScreenPosPreDiv(vec4 clipPos)
{
    return vec2(
        clipPos.x / clipPos.w * cGBufferOffsets.z + cGBufferOffsets.x,
        clipPos.y / clipPos.w * cGBufferOffsets.w + cGBufferOffsets.y);
}
```

Can somebody tell me what does `cGBufferOffsets` stands for? Also, any help on this "wierd" looking multiplactions and divisions by its components in both of the upper functions would be more than welcome :)

-------------------------

throwawayerino | 2021-06-04 19:58:05 UTC | #2

Disclaimer: I'm not an expert and this is just from reading the shaders + renderpaths xmls. I might be wrong so I recommend waiting for someone other than me (^:

https://urho3d.io/documentation/HEAD/_render_paths.html
The link above talks a bit about these functions. Tl;dr they're to access G-Buffers correctly.

----
A G-Buffer is used when deferred lighting is specified by the render path. `cGBufferOffset` a shader parameter used to know where to fetch data from the G-Buffer. It's usually used via a call to these two functions above, which tell where on the rendertarget the shader is at and from where to sample data from the G-Buffers. See `DeferredLight.glsl` for an example usage.

-------------------------

Eugene | 2021-06-08 16:21:10 UTC | #3

[quote="Lunarovich, post:1, topic:6872"]
does `cGBufferOffsets` stands for?
[/quote]
In this particular case, cGBufferOffsets is an (xy_offset, xy_scale) that transforms from viewport space [-1,1]x[-1,1] to UV space [0,1]x[0,1] (or arbitrary subregion of UV space). Used to sample all display textures, including but not limited to GBuffers.

Also, the following vectors in homogeneous coordinates are equivalent: (x, y, 0, w) ~ (x/w, y/w, 0, 1). First function makes first vector, second one makes second.

-------------------------

Lunarovich | 2021-06-09 17:11:02 UTC | #4

Thanks! Now it's a bit clearer now.

-------------------------

