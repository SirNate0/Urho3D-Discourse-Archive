Dave82 | 2019-01-28 05:55:02 UTC | #1

Is it possible ? I want to render completely black objects but still affected by lights but render objects which will receive ambient light too. The problem is the ambient light is controlled by zones. so every object within this zone will receive the same ambient light. Tried removing the AMBIENT pass from Diff technique but that didn't worked.

-------------------------

Leith | 2019-01-28 06:26:51 UTC | #2

I can't really talk as any kind of expert on Urho3D, but here is my experience:
Typically, ambient lighting defines the base amount of light that objects receive, even in the absence of a light source - its not the one you are looking for, usually the one you want per object is called diffuse lighting (a material property, since each object can have a unique copy of a material), typically its an intensity, a float, or a rgb triple/ vec3 (for colour) that we can set per object.
It is always possible. Everything is possible. Some things are not likely, or are not typical, but everything you can imagine is possible. Even if it means getting your hands dirty and writing your own shaders.
Wait, you said completely black? Completely black objects will always show up completely black - there is no diffuse colour on the materials? Then the result of shading them, even with lighting, will be completely black.

-------------------------

Leith | 2019-01-28 06:14:34 UTC | #3

Assuming there was a perfect black colour, and indeed something near to it does exist in the real world, it would reflect no energy from photons, and appears black in the daytime, and black at night

-------------------------

Leith | 2019-01-28 06:20:14 UTC | #4

The basic lighting equation usually says something like, output pixel colour = diffuse pixel colour (sampled from a texture) * diffuse lighting + ambient lighting
this is wrong, I know, its not accurate, but it shows how the thinking behind lighting works - ambient lighting is added to whatever else we computed

-------------------------

Dave82 | 2019-01-28 06:45:21 UTC | #5

It is perfectly ok to render completely black objects by using black ambient light. The only problem is that the ambient light is determined by zones and not by constants in the LitSolid shader

-------------------------

Leith | 2019-01-28 06:53:30 UTC | #6

I see your point, zones describe ambient lighting, and without any zones, there is no ambient lighing, am I right? So make one zone and set the ambient lighting. I agree the system is not easy to learn or sometimes easy to use, but we can generally find a way (and not talk about it) or ask for help (and yell loudly)
I have permission from the original author, to advocate for ripping out or changing stuff that is in my way, so if you can convince me of your use case, perhaps i can change the engine to suit you, without breaking stuff. I am happy to advocate for change, but I need to understand how that change breaks things. and why we would go this way.

-------------------------

Dave82 | 2019-01-28 07:04:39 UTC | #7

[quote="Leith, post:6, topic:4874"]
I see your point, zones describe ambient lighting, and without any zones, there is no ambient lighing, am I right?
[/quote]
Not really. There is always ambient lighting in the scene. If it is not specified by a zone the engine uses the default ambient color. I don't think we need to change the engine for this. What could do it is a simple shader (perhaps the modified version of litSolid) to discard the ambient pass. Unfortunatelly i can't find which parameter to change.

-------------------------

Leith | 2019-01-28 09:50:09 UTC | #8

I classify this as a trick question: if the diffuse material texture is true black, then no amount of ambient lighting should make it appear as any other colour, because it is true black.

-------------------------

Dave82 | 2019-01-28 10:09:40 UTC | #9

[quote="Leith, post:8, topic:4874"]
if the diffuse material texture is true black
[/quote]

The diffuse color is white. The ambient is black

-------------------------

guk_alex | 2019-01-28 10:39:28 UTC | #10

https://urho3d.github.io/documentation/HEAD/_zones.html
[quote]
For the case of multiple overlapping zones, zones also have an integer priority value, and objects will choose the highest priority zone they touch.

Like lights, zones also define a lightmask and a shadowmask (with all bits set by default.) An object's final lightmask for light culling is determined by ANDing the object lightmask and the zone lightmask. The final shadowmask is also calculated in the same way.
[/quote]

Did you play with priority and masks, can it affect the way you desire?

-------------------------

Dave82 | 2019-01-28 11:14:42 UTC | #11

Thanks. I tried using masks but it just doesn't work. Priority is not something i was looking for.
If someone could tell me where is the ambient light applied in LitSolid shader

-------------------------

Dave82 | 2019-01-28 18:34:09 UTC | #12

So it was so trivial... The documentation doesn't mention this feature for some reason. If you need a custom ambient light just set the "AmbientColor" shader parameter in the material.

[code]
material->SetShaderParameter("AmbientColor" , Urho3D::Vector4(0 , 0 , 0 , 0));
[/code]

-------------------------

