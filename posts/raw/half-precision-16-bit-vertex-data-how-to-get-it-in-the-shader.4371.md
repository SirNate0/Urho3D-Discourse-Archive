Alan | 2018-07-03 04:00:57 UTC | #1

Hello there.

I'm batching some geometry on the CPU and for efficiency I'd like to use `half2` for UV and maybe even `half3` for normals (not sure on this latter yet).

I've managed to create the data appropriately CPU-side and I'm passing it to the GPU and size is correct (positions are OK), however I don't know how I'm supposed to get the halfs in the VS, I was hoping that simply changing the `float` to `half` in the shader was going to work but it still reads 32 bits for each element.

Another problem is that there's no 16-bit `VertexElementType` so I have to use some hacky masking (I'm using `PODVector<VertexElement>` for descs).

Do you guys know how I could do that without having to deal with the internals?

Thank you

-------------------------

Eugene | 2018-07-03 14:17:40 UTC | #2

You may add new `half` type and make PR then. Should be quite easy. Or report issue.

-------------------------

