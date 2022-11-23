Askhento | 2022-05-15 23:19:30 UTC | #1

I have a mesh with shape keys, aka morph target, aka blend shape. I would like to have both base and morphed position in vertex shader. Maybe they are accessible as a vertex attribute?

-------------------------

JSandusky | 2022-05-16 00:36:22 UTC | #2

Morph targets are applied on the CPU to a mirror of the vertex data, so it's not available to the shader.

You could rework the morph-target application to write data into a different type of vertex-buffer that instead of containing just the transformed vertices contains extra attributes for the original position - or with the morph data as deltas instead if you wanted to go whole hog.

-------------------------

Askhento | 2022-05-16 00:36:12 UTC | #3

Do you have an example on how to set custom vertex attribute?

-------------------------

JSandusky | 2022-05-16 01:05:42 UTC | #4

You add a new semantic to `enum VertexElementSemantic` then `ShaderVariation::elementSemanticNames[]` and I'm pretty sure that's it as long it's only a semantic. Obviously you have to then go and actually use those in a shader.

The morph target transforms are done in `AnimatedModel::UpdateMorphs` for the actual update that writes the cloned vertex-buffers (which is where you'll inject your original position) and `AnimatedModel::CloneGeometries` is where those clones are produced, it's these copy buffers you have to inject your additional semantics/vertexelementinfo into so that things can be mapped correctly.

---

It should also be possible to do through extra-vertex-buffers reusing the original buffers and just mapping that differently, but I'm unsure of what you'd need to do for that because you'd have to basically have the same vertex-buffer twice, but represented with a different vertex-element information (and only partial information at that) ... and there's been no case of that being a thing so far.

Realistically to go the extra-buffers route, you'd still need the custom semantic, and you'd have to copy just the original positions into a new set of cloned buffers that are put into the cloned geometries. (you wouldn't need to track them, you'd just pump them right in and the Geometry class will clean it up as dtor's fire)

Doing that you wouldn't have to muck around in the morph update, it'd just work, so you'd only be dealing with the CloneGeometries method.

**Edit**: if I were implementing I'd go with the extra-buffers. Should be a ton easier. Also if skinning, you'll need to add an overload for GetWorldPos (Transform.hlsl/glsl) to accept a position instead of getting it by itself (though that's just `mul(iPos, iModelMatrix)` so not a big deal to get the bone transformed original position.

You'd also need a helper to function to call CloneGeometries (ie. `void ForceMorphTargetsAlwaysOn() { CloneGeometries(); }`) to force the clone so your model is always setup as your shader expects to get that added semantic. Otherwise there'll be a lot of plumbing involved to setup a new shader #define that says "*yo, I've got original position data too*".

-------------------------

Eugene | 2022-05-16 01:34:45 UTC | #5

You can just write your base position e.g. like texcoord2 in your model on the disk, or during the load. I have some helpers to edit buffer contents, you can port them to your codebase if you wish.

-------------------------

Askhento | 2022-05-16 01:46:49 UTC | #6

Where could I find helpers?

-------------------------

JSandusky | 2022-05-16 03:02:59 UTC | #7

Wow, that's so stupidly obvious I didn't think about it.

-------------------------

Eugene | 2022-05-16 06:23:56 UTC | #8

In my fork I just modified `VertexBuffer` itself, but you can have these helpers as free functions, it shouldn't be hard to copy-paste and adjust this code.

You can try to make something from scratch, but I don't think it would be faster. Also these helpers may just help you build your `Model`s easier in other scenarios.

With this code you can easily read and write buffer data as array of Vector4-s, with `ShuffleUnpackedVertexData` you can "insert" or "remove" any vertex elements from these arrays.

So the pseudocode would be:

```
buf = vb->GetUnpackedData()
// modify layout
vertexElements = vb->GetElements()
vertexElementsWithTexcoord2 = vertexElements + {TEXCOORD, 2};
// make room for the new element
Vector<Vector4> buf2;
ShuffleUnpackedVertexData(buf, vertexElements, buf2, vertexElementsWithTexcoord2)
// copy positions to newly allocated element Texcoord2
buf2[...] = buf[...]
// store results back
vb->SetSize(..., vertexElementsWithTexcoord2)
vb->SetUnpackedData(buf2)
```
https://github.com/rbfx/rbfx/blob/master/Source/Urho3D/Graphics/VertexBuffer.cpp#L307-L342

-------------------------

