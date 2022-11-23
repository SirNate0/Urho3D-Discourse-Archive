sabotage3d | 2017-05-28 20:52:47 UTC | #1

Hi,
I am having some problems with alpha sorting when depthwrite is false. I am using the technique below with two ribbon trails. They are sorted correctly on their own but not together. Is there anyway to fix this or manually sort them? The only way I found to move each point slightly in Z enable the depthwrite, but that at some point would make it too close to the camera.

    <technique vs="Unlit" ps="Unlit" vsdefines="VERTEXCOLOR" psdefines="DIFFMAP VERTEXCOLOR">
        <pass name="alpha" depthwrite="false" blend="alpha" />
    </technique>

https://www.youtube.com/watch?v=MHSIm2dhutA

-------------------------

Sinoid | 2017-05-29 17:35:04 UTC | #2

That's not doable without depth write+test. Rendering is always by triangle order in the index buffer in both GL and DX, depth-test is the only 'sorting' mechanism.

Your options:

- k-Buffers (probably not implementable right now)
- Order Independent Transparency
- Batch all of them with overlapping bounds together and sort the triangles/quads

-------------------------

sabotage3d | 2017-05-29 21:06:05 UTC | #3

Thank you. I am trying to switch to using depth-test and add offset in the GLSL shader, but it doesn't seem to work with `gl_Position`.
I added the offset below to the Unlit shader:
`gl_Position.z *= 0.99;`
And I changed the technique to use depth test.

    <technique vs="Unlit" ps="Unlit" vsdefines="VERTEXCOLOR" psdefines="DIFFMAP VERTEXCOLOR">
        <pass name="alpha" depthwrite="true" blend="alpha" />
    </technique>
Another option as you suggested is the Order Independent Transparency. How applicable would be in this case and would it be hard to implement?

-------------------------

Modanung | 2017-05-30 09:36:13 UTC | #4

[quote="sabotage3d, post:3, topic:3172"]
gl_Position.z *= 0.99;
[/quote]

If their z position is equal, multiplying it by the same scalar would _keep_ them equal, right?

-------------------------

sabotage3d | 2017-05-30 09:45:15 UTC | #5

Sorry what I meant is that I have set one batch to: `gl_Position.z *= 0.99` and kept the other as it is. But I got similar problems to the video above. Any other ways of sorting manually or disabling anything else that might affect the sorting of the batches other than the depth. It looks like something else might be overwriting the sorting.

-------------------------

Sinoid | 2017-05-30 17:59:44 UTC | #6

For clarification are you trying to sort them into a specific order as a whole-strips (red strip below green strip below blue strip, etc) or as a complete whole like they're tangled up in a knot?

-------------------------

sabotage3d | 2017-05-30 18:06:19 UTC | #7

The default sorting of the Ribbon Trail is correct when the depth test is disabled but only for the same batch. I would like to sort multiple batches of Ribbon Trail as if they were one the same batch in order of placement. Any new polygon should be on top of the previous polygons no matter which batch they are from.

-------------------------

Sinoid | 2017-05-30 20:08:49 UTC | #8

Then you still have mostly the same problem with your shader.

If you multiply Z by 0.99 for the whole batch it's going to move the whole batch, not parts of it, so it will be impossible for them to tangle/intermix as the whole thing is moving instead of specific segments (unless there's some selection code you didn't show).

Try multiplying Z by the output of any 2d noise function (keyed on X and Y) and see if that gets you at least somewhere.

-------------------------

sabotage3d | 2017-05-30 20:38:18 UTC | #9

I was just testing one batch with 0.99 the other with 1.0. I also tried some negative on one batch and positive on another. This is just to test if this approach would work at all. If I can get this to work I will add an attribute to each polygon and multiply it as an offset in the shader. What works for sure if just moving the actual point position before creating the polygon in the update loop, but at some point it would get too close to the camera.

-------------------------

sabotage3d | 2017-05-31 00:11:58 UTC | #10

Ok this seems to be working. I have added an index attribute on my polygons as they are already sorted sending it as iObjectIndex in the GLSL shader:

    int index = int(iObjectIndex);
    gl_Position.z = -index * 0.001;

If anyone has better ideas let me know. This method has some problems due to the precision of the depth buffer.

-------------------------

sabotage3d | 2017-05-31 20:47:44 UTC | #11

If I change the alpha to 0.5 there are lot of glitches. Do I need custom pass in order to fix it?
This test is with `depthtest="less"`
https://www.youtube.com/watch?v=5wra6nIqMtI

-------------------------

