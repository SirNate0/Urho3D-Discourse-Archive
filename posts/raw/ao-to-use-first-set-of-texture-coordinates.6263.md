glebedev | 2020-07-14 08:09:05 UTC | #1

Currently shaders expect AO texture coordinates to be in second texture coordinate channel. This makes sense for lighmap but it doesn't for AO as usually AO is generated or drawn in the same space as diffuse and normals.

Does anyone disagree and use the second texture channel for AO?

-------------------------

cmd | 2020-07-14 20:39:42 UTC | #2

It seems logical to me to at least by default to assume AO texture coordinates are in the first channel. Certainly all the examples I have seen of its usage (which tbh isn't many), have used the same texture coordinates as the albedo and normalmap and metallicmap textures. Although I can imagine examples where it might be useful to use different coordinates for any of the other possible maps, so I guess ideally it should be configurable as to which channel is used for every map. Is that feasible in Urho?

-------------------------

glebedev | 2020-07-14 21:13:13 UTC | #3

Yes but it would add unnecessary complication to the shader. I'm trying to keep it simple and readable.

-------------------------

cmd | 2020-07-14 22:41:26 UTC | #4

Well, I guess (probably obviously) the main problem with only changing AO to use the first texcoord channel is that it would break any existing urho applications that needed a different mapping for AO. So maybe the easiest and safest option would be to provide an easy way to copy first textcoord channel to second channel? Though I suppose that is a bit of an unnecessary waste of vertex buffer.

-------------------------

