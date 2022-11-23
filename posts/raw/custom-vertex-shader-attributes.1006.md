friesencr | 2017-01-02 01:04:45 UTC | #1

How do you get custom vertex shader attributes into the system?

Thanks,
Chris

-------------------------

cadaver | 2017-01-02 01:04:45 UTC | #2

You mean vertex stream attributes, like normals, tangents, color?

Currently you don't, without modifying the engine. You could repurpose unused elements like texture coords (right now there's just 2 channels though), cube texture coords or vertex colors. Probably need some hacking of the import/export chain for this.

-------------------------

sabotage3d | 2017-01-02 01:04:45 UTC | #3

Any chance for adding dynamically custom attributes ? Or predefined custom attributes if it is easier. At the moment it is a bit of headache to send custom data to the shader.

-------------------------

cadaver | 2017-01-02 01:04:45 UTC | #4

Turso3D has custom vertex declarations; the code to support that could possibly be lifted to Urho3D. But no firm promises, as this breaks / changes the model format. It's hard to support truly arbitrary attributes as usually the "semantic" of the attribute has to be known somewhere, especially on D3D. However, there could be a convention that the additional data would be in additional texcoord channels.

-------------------------

sabotage3d | 2017-01-02 01:04:45 UTC | #5

There could be just predefined slots for Vector3f, Vector2f, Matrix4x4 or single float. Or we just read all the vertex attributes from the geometry and create appropriate slots. That is similar to the behaviour in most 3d packages today. We could have a convention for naming the attributes, for easier parsing.

-------------------------

gawag | 2017-01-02 01:04:48 UTC | #6

Not sure what you mean by "custom vertex shader attributes". Do you mean normal shader parameters like colors, positions or directions? Sounds a bitt too simple but: [urho3d.wikia.com/wiki/HowTos#Cus ... parameters](http://urho3d.wikia.com/wiki/HowTos#Custom_shader_parameters)
If you mean attributes per vertex: cadaver's suggestion of "missusing" things like vertex normals, vertex colors, UV coordinates or vertex weights should work. But I don't think that can be done as dynamically as normal shader parameters.

-------------------------

