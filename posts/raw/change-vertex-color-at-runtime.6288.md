josuemnb | 2020-07-28 18:43:46 UTC | #1

good day.
I'm using PositionNormalColor to load a model with technique 'NoTextureVCol'.
i'm trying to change the vertex colors, but that is not possible through SetShaderParameter since the material is the same for all colored vertexes even when them have different colors.
How could this be overcome?

Thanks in advance.

-------------------------

Dave82 | 2020-07-28 18:45:38 UTC | #2

You need to lock your vertex buffer , then apply changes to vertex color in your vertex data and then unlock it. See example 34 for how dynamic vertex buffers work.

-------------------------

josuemnb | 2020-07-27 13:59:32 UTC | #3

Thanks.
 i'll try it
:smiley:

-------------------------

josuemnb | 2020-07-28 15:27:28 UTC | #4

It worked.
thanks.
Just another thing.
How can i alter the alpha when NoTextureVCol is applied?

-------------------------

Modanung | 2020-07-28 18:41:07 UTC | #5

I think you may have to create a custom technique for that purpose by adding an alpha pass to the NoTextureVCol technique, turning it into NoTextureVColAlpha:
```
<pass name="alpha" depthwrite="false" blend="alpha" />
```

-------------------------

josuemnb | 2020-12-13 15:21:01 UTC | #6

thanks for your help.

-------------------------

