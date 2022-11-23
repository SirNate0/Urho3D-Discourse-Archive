mohamed.chit | 2020-09-29 23:09:08 UTC | #1

I have a material instance with a parameter, which should be updated during the game each frame.

To do so, i have to pass the name of the shader parameter (a string) to "SetShaderParameter". Therefore update this parameter in the material.

isn't that very costly? why there is not a function to pass simply the "parameter id"? as these parameters have specific IDs usually when shaders are compiled.

is it possible to have that, that would be i think a lot faster than passing the name of the parameter (string).

I think one of you would suggest to use animation, i cannot do that, since the values are actually coming from different library, i can only update the material parameter each frame.

I would be very glad to get a reply from you.

Best regards.

-------------------------

Eugene | 2020-09-30 09:03:42 UTC | #2

[quote="mohamed.chit, post:1, topic:6408"]
isn’t that very costly? why there is not a function to pass simply the “parameter id”? as these parameters have specific IDs usually when shaders are compiled.
[/quote]
The issue is that `Material` is `Resource` that can be loaded and _saved_.
And you cannot really save shader parameter to XML if you have only ID, you need full name.

This dichotomy between "strings as text" and "strings as hashes" is deep architectural issue that appears in different places of the engine. I don't think there's easy and nice solution that lets `Material` accept shader parameters by hash instead of name.

`Scene` has somewhat similar (or, to be precise, opposite) issue -- if you add variables to `Node`, their names are stored as hash. So when we changed hash function for string (it happened once a few years ago), actual `Scene` files became corrupted.

-------------------------

mohamed.chit | 2020-09-30 16:23:11 UTC | #3

Why not to use the same concept in java, there are some fields marked as transient, you could have a transient parameter id in material class, it is not part of the Material (Resource) save/load, but it exists only at runtime, in-memory and can be used to speed-up finding the parameter, i think that would be great.

I may have 100s of materials in a scene, I need to update theirs material parameters each frame, using material parameter ID would really enhance perfomance.

it is just a suggestion, I am not even sure that it can be implemented.

-------------------------

Eugene | 2020-09-30 16:51:23 UTC | #4

[quote="mohamed.chit, post:3, topic:6408"]
there are some fields marked as transient, you could have a transient parameter id in material class, it is not part of the Material (Resource) save/load, but it exists only at runtime, in-memory and can be used to speed-up finding the parameter
[/quote]
Shader parameters are _already_ part of save/load.
You may add new shader parameter via `SetShaderParameter`, therefore you must provide full name and not hash.

The best thing you can do is to extend `Material` API so it lets you find _existing_ parameter and modify its value. Nothing prevents you from doing so, it's simple change.
All you need to do is to update `shaderParameters_` and refresh some cached values...
 https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/Material.cpp#L979

-------------------------

mohamed.chit | 2020-10-14 17:54:42 UTC | #5

I thought about your suggestion, even if it is simple, I would not do it, because I would not like to compile Urho3D for each platform, I simply download binaries, which are supported.
Or If i make changes, they become part of Urho3D itself.
It would be great to have such feature, to pass an ID instead of a name, this would improve the perfomance a lot.

-------------------------

Modanung | 2020-10-15 13:07:04 UTC | #6

This seems like it could make for a welcome and easily digestible PR?

Also, welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

