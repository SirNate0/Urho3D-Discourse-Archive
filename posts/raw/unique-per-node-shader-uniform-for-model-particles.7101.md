SirNate0 | 2021-12-16 03:16:09 UTC | #1

I am currently working on doing some more advanced visual effects than Urho supports out-of-the-box, and one such thing would be having what are effectively particle systems that spawn models rather than billboards. For this, though, it would be nice to be able to set some shader parameters on each Node that would be spawned by the particle system that would control the coloration or UV offset, for example. 

One way I thought of achieving the effect is to have the Node/Component ID set as a shader parameter, since those are guaranteed to be unique, and then I can generate a pseudo-random number as the color/UV offset based on that.

What do you think of the feasibility of implementing such a thing, and would it even be worth doing versus just creating and assigning 100s of copies of a material for each effect?

-------------------------

Modanung | 2021-12-16 09:40:41 UTC | #2

I'm no shady person, but... maybe store the values in a texture, or turn vertices into models somehow?

-------------------------

