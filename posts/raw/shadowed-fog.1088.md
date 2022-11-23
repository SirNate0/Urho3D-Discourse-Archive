szamq | 2017-01-02 01:05:22 UTC | #1

I have a height fog in my scene which is set just above the ground. I have ambient color in zone set to 0,0,0. How can I achieve effect that shadowed areas on the ground are black, because now the fog color is just added to the blackness. Tried modifing the litSolid shader but with no good effects. If I could get the shadow factor(calculated from all the lights on the scene) then I could just multyply fog color by this shadow factor. 
Is this possible?

-------------------------

cadaver | 2017-01-02 01:05:22 UTC | #2

Without modifying the light/shadow rendering quite extensively (it's a bit same problem as the lightmap + shadows mixing) it's not possible to know a global shadow occlusion value when rendering. Instead light is added per-light and that light's shadow (= absence of light) is evaluated at the same time.

What could possibly work is if you don't add the fog in the base pass at all, but only in the light pass(es). Think of the fog as a part of the material's diffuse color, which modulates the lighting.

-------------------------

szamq | 2017-01-02 01:05:22 UTC | #3

Thanks, it makes sense. But what if i'm using deferred renderpath? Then the only active pass in the material technique description is just deferred, so there is no really possibility to differ between base and lighting pass. Am I right?

Edit:
Ok I think I got that. I need to remove the fog from deferred pass/shader, and instead add it to the DeferredLight pass/shader.

-------------------------

cadaver | 2017-01-02 01:05:22 UTC | #4

In deferred rendering you just have the albedo buffer color to play with, which is the diffuse value that all lights are going to use when adding themselves. 

Fog parameters are supposed to be per-object (based on zone) so you can't move them reliably to the deferred light volume rendering.

-------------------------

