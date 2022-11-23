najak3d | 2022-03-07 00:05:32 UTC | #1

I'm rendering the same Plane, same models, same shadow settings, same scale, same directional light direction, etc...   But in our scene, there is this gap between the model's feet and the plane/floor, as shown here:

![image|690x462](upload://jC0yJEqPF20WheDMtP2elkD0jwH.jpeg)


What could be causing this gap?   I can't seem to get rid of it, after toying around for an hour, comparing it to the Samples project for Skeletal Animations, where the shadows meet the ground perfectly.

-------------------------

najak3d | 2022-03-07 00:17:57 UTC | #2

SOLVED!
It was just the light.ShadowBias settings.  Not sure why for my scene they were "too high" while for a similarly scaled Samples scene, these same settings worked just fine.  But that seemed to be it.

I changed:
light.ShadowBias = new BiasParameters(0.00025f, 0.5f);

to:
light.ShadowBias = new BiasParameters(0.0000025f, 0.5f);

and now my models are grounded again! 

And there was much rejoicing... .   yay...

-------------------------

