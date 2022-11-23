TheComet | 2017-01-02 01:14:36 UTC | #1

(I almost feel bad for posting this many questions in such a short time)

In my custom shader I'd like the user to be able to specify the falloff of the light. I thought the most appropriate place to store this value would be in cLightColor.a, but it seems I can't change that value at all (in the editor, that is), it always resets to 1. What is the purpose of cLightColor being a vec4 if I can't change it?

-------------------------

cadaver | 2017-01-02 01:14:36 UTC | #2

The engine is already using the light color uniform's A component for specular intensity, so you need engine changes, another uniform, or both.

-------------------------

