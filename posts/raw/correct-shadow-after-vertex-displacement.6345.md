UrhoIsTheBest | 2020-08-24 05:34:00 UTC | #1

I changed the vertex position in the vertex shader, what should I do to make the shadow correct?
Currently, the shadow does not respect any change in the vertex shader.

-------------------------

Eugene | 2020-08-26 02:24:22 UTC | #2

It may sound like a trivial reply, but you have to change vertex position in shadow shader as well.

-------------------------

UrhoIsTheBest | 2020-08-26 02:24:19 UTC | #3

Thanks @Eugene!
Definitely! A trivial reply from an expert can save a day for a newbie!

I somehow mistakenly thought the shadow map is using the same vertex shader with a light pass predefines, etc. Now I see it uses ```Shadow.glsl``` in the technique pass.
Still learning the Urho3D rendering pipelines.

-------------------------

