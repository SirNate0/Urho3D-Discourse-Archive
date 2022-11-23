suppagam | 2019-08-26 21:30:13 UTC | #1

I'm trying to replicate the effect number 35 of this Unity pack: https://jeanmoreno.com/unity/warfx/

The bullet impact goes towards one direction, the one opposite to where the bullet hole decal was placed. I started using the Decal example in Urho and got the bullet hole to work, but I can't get to spawn a particle system "aimed" at the opposite direction.

-------------------------

urnenfeld | 2019-08-26 22:54:22 UTC | #2

**NOOB ADVICE ALERT:**

I see at least 2 sets of emitters/particle effects in there:

- Sparks(Concrete Falling) (Material -> Burst.xml)
- Smoke (Material -> Smoke.xml)

I think the key parameters inside **each** particle effect would be:

    <particleeffect>
    [...]
     	<direction min="-1 -25 -1" max="1 0 1" />
	    <constantforce value="0 -35 0" />
    [...]
    </particleeffect>

These 2 symbolize like 2 vectors, *where particles go initially* and *the force that is applied to them*.

So in your case:

Smoke effect won't have a clear direction(direction should describe like a ball, and force should not play a key role), I bet you can get the same as the Vehicle example.

But the concrete particles will do have tendency to be similar to a Vector3::DOWN(in fact similar to the example I wrote)...

-------------------------

Sinoid | 2019-08-27 03:03:40 UTC | #3

The above is basically true.

You'll want to align particle effect's direction to be in a cone around the +Z or +Y axes (Forward or Up respectively) and be sure the emitter is marked as `relative`.

Just orient the node containing your emitter so that it's +Z or +Y axis aligns with the normal / incident / reflection vector of the surface where you put the decal (it's whichever vector[s] you pick). +Z is the ideal axis to use for particle effects since you can just use the LookAt function to look the right direction.

For that #35 effect you'd probably want to align the puff to normal and the chips to the reflection vector of the ray so that the chips appear to be following elasticity from compression properly.

-------------------------

suppagam | 2019-08-27 15:50:17 UTC | #5

The "relative" thing did make a difference! Thank you. I also didn't know I could use the LookAt function, thanks for the tip.

-------------------------

Sinoid | 2019-08-27 18:05:22 UTC | #6

I had actually intended to say `make sure it's not marked relative`, because ConstantForce (ie. gravity, cares about that flag) while start direction behaves differently depending on that flag and it's meaning here is a little odd.

Regardless, knowing about that flag is important because it changes behaviour pretty substantially.

-------------------------

