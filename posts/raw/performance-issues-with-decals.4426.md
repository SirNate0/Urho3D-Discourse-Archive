smellymumbler | 2018-07-31 15:13:40 UTC | #1

I've used the Decals demo as a base reference for a simple bullet hole implementation. I'm checking the object that was hit and based on it's material, I use a different texture (wood, metal, etc.). So far, so good! However, after a good shooting session, I'm noticing a decline in FPS caused by the decals.

Is there any efficient way of doing this, before I resort to my lazy solution of just making the bullet holes disappear after X seconds?

-------------------------

Moe | 2018-09-21 08:53:10 UTC | #2

The last time i made Bulletholes was on the n3ds:D Mentioning that because it's _not that powerfull_ - so i had to optimize everything.

What i did was, additionally to having a _lifetime variable_ fading the bullet holes out, i also had a maximum limit and measures to deal with overflow.

Keep your bullet holes in a list, once you surpass your desired upper limit (let's say 100) you take the oldest in the list (new one are added on top, so oldest are the last entries) and artificially decrease their _lifetime variable_ that is responsible for fading and getting rid of them.

Basically as you pass the max limit the oldest holes are forced to instantly fade faster. I had it set up to take away 10% of the _starting livetime variabe_, so that i had 110 max holes - the last 10 being subjected to the forced faster fading, getting faded 1/10th with each additional decal created. 

You can of course play with how high your max decals should be, how many get forced to fade faster and how much each of those gets reduced (all the same? linear, older ones more? etc.)

Hope that gives you some idea ;)

-------------------------

Modanung | 2018-09-21 14:03:09 UTC | #3

...and I guess this fading would be best handled through vertex colours? To not have a material clone for every decal. It would be nice if `Decal`s had a variable for this.

-------------------------

guk_alex | 2018-09-21 13:57:43 UTC | #4

If you need a really big amount of the holes to be permanently saved I would recommend you to draw holes into the original texture. `Texture2D::SetData()` (look https://discourse.urho3d.io/t/dynamically-change-texture-or-paint-on-texture/2372). Also, I tried decal example and it needs about 10000 fish decals to make itself laggy (and it only affects frames if you look at all of them at once, if you move camera in different direction frames are fine).

By the way, DecalSet have own limit of objects if you put a bunch of them at once (if you need to keep larger amount of decals you need to have create several DecalSets).

And yes, its better to have count limit (as Moe suggested), then the time limit.

-------------------------

smellymumbler | 2018-09-21 18:55:56 UTC | #5

The SetData idea is amazing. Do you have any example on how to get the raycast hit position and translate to the texture position? How would you read the decal info to apply the data? Is transparency handled automatically?

-------------------------

Moe | 2018-09-22 08:34:58 UTC | #6

@smellymumbler 
Now i am not sure how you do that in Urho3D - since i am new to it, but you can usually get the hit face and it's vertices. Then you read out the vertices uv coords (if that is not returned as well) and from that you can get the textures pixel pretty easily using Barycentrics.
Found an example for Unity (C#) - the math should be the same ;)
https://answers.unity.com/questions/1105729/find-uv-coordinates-of-mesh-without-a-raycast.html

Since uvs are normalized it should be as simple as rounding VU*texture dimensions. Use modulo or fraction if you, go beyond uv1,1.

If you draw to a texture you would lerp texture.rgb to decal.rgb by decal.alpha. That should handle transparency if it is not automatic...

One concern that i'd have with that approach though would be the (v)ram consumption.
If i am not missing a unknown technique, that would mean you either use a 2nd world space mapped set of uvs and a second texture (empty, transparent except for decals - overdraw²). Or you would have to make sure you have no tiling or otherwise overlapping/repeating textures and copy textures for each hit object. That sounds like the ram usage will explode during fire fight, not come down afterwards and highly depend on player behavior and situation. That makes predictions about performance impossible and basically limits what graphics card can even sustain fire fights to begin with... I'm sure you can make it work by cleverly using an atlas and whatnot - sounds super not easy/fun though - maybe i work too much on hand held devices :stuck_out_tongue:

@Modanung
Yeah absolutely right, i use Vertex alpha and Shaders for blending.

-------------------------

Sinoid | 2018-10-05 01:54:46 UTC | #7

@modanung, could just write the time into an integer attribute of the vertices. The shader can reference that time against a `CurrentTime` and deal with the fade. It would need to be in sync with the existing decal removal over time though, which might make it easier or harder.

---

I kind of have a hard time seeing the decals becoming a performance problem as they're implemented. The main scenario I can picture is one where considerably large single-geometry environments are used and the other is not setting a reasonable cap on the number per DecalBatch.

If I personally saw it become a problem I would probably do an additional crude test against the DecalBatch itself to see if I could `promote` a decal into a different decal to keep the decal count low, similar to what you see in the first 3 FEAR titles (I'm counting Extraction-Point) where the pit gets bigger and bigger.

Tangentially, the engine isn't too far from being able to do deferred decals. IIRC the only problem is that the light-passes have to be identified up-front which makes 100% generalized lighting passes not doable at present (deferred decals are basically special lights). I do remember trying to fix that and falling flat on my face.

**Edit:** after I reread the point I highlighted to modanung it hit me that the DecalBatch sucks at batching (how could it not given what it is), each batch is a unique geometry.

-------------------------

