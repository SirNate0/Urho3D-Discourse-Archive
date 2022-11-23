n91 | 2017-01-02 01:13:12 UTC | #1

I want to get more precise shadows on a certain small object (e.g. a part of a wall). I was playing with various shadow parameters (http://urho3d.github.io/documentation/1.5/_lights.html#Lights_ShadowedLights *). Increasing Renderer's ShadowMapSize to e.g. 16384 helped a bit (but rendering was slower). 

My idea was to reduce the area which the shadow map is covering (to get the better shadow resolution even with a small shadow map). I have reduced camera's FarClip. It helped, the shadow was more precise. However, I realized that that not only visible objects were clipped by camera's FarClip, but also objects (e.g. behind the camera) that cast the shadows. (I also tried to set ShadowDistance to a great number.) The light in my case is directional.

My question is:
How to reduce the area covered by the shadow map (e.g. by decreasing camera's FarClip) while using different FarClip for shadow mapping (in order to keep shadows from objects that are far away)?

* I cannot post links; it is my first post.

-------------------------

cadaver | 2017-01-02 01:13:12 UTC | #2

For directional light, the light's CascadeParameters should define the maximum distance, which also indirectly determines the resolution.

Typical setup in AngelScript:

[code]
light.shadowCascade = CascadeParameters(10.0f, 50.0f, 200.0f, 0.0f, 0.8f);
[/code]
which would mean 1st cascade split is at 10 world units, second 50, and shadow max distance is 200 units.

-------------------------

n91 | 2017-01-02 01:13:12 UTC | #3

Works. Thank you!

-------------------------

