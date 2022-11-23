sabotage3d | 2017-01-02 01:02:13 UTC | #1

Hi is it currently possible to create a new shader uniform for OpenGL ES 2.0 .
I looked into the code but I can't understand how it works.
For example for the depthBuffer and the normalBuffer I found only these:

[code] engine->RegisterEnumValue("TextureUnit", "TU_NORMALBUFFER", TU_NORMALBUFFER);
 engine->RegisterEnumValue("TextureUnit", "TU_DEPTHBUFFER", TU_DEPTHBUFFER);[/code]

[code]textureUnits_["NormalBuffer"] = TU_NORMALBUFFER;
textureUnits_["DepthBuffer"] = TU_DEPTHBUFFER;[/code]

Where are the OpenGL calls for these guys ?
How are these translated to these samplers : 

[code]uniform sampler2D sNormalBuffer;
uniform sampler2D sDepthBuffer;[/code]


Thanks in advance,
Alex

-------------------------

