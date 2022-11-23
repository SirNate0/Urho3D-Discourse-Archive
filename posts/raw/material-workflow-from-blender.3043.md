slapin | 2017-04-25 06:55:29 UTC | #1

Hi all!

What is material workflow when the material is created in Cycles in Blender to look the same (or similar) in Urho3D?
For PBR and non-PBR?

-------------------------

Modanung | 2017-04-25 09:57:07 UTC | #2

I'm inclined to say none.
Have you seen [godan's work](http://discourse.urho3d.io/t/use-skybox-material-as-reflection-source/3016/4) on reflection probes?

-------------------------

suncaller | 2017-04-26 15:40:33 UTC | #3

The answer is baking, but the final result is less than stellar in my experience. I'm still experimenting with this, however.

-------------------------

Modanung | 2017-04-26 16:48:03 UTC | #4

[quote="suncaller, post:3, topic:3043"]
but the final result is less than stellar in my experience
[/quote]
Also this only works for static lights _and_ geometry. Unless you're after generated textures or an ambient occlusion map.
But still might be the answer @slapin was looking for.

-------------------------

