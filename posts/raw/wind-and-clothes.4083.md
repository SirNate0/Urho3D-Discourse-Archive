maxvi | 2018-03-12 11:04:48 UTC | #1

Hi guys! I played with Urho3D some time ago, but I'm not sure that I can do what I want using it.

1. Can I create wind power that affects to clothes? something like ship sails.
2. How good U3D performance comparing to UE?

-------------------------

Eugene | 2018-03-13 13:37:47 UTC | #2

Hello!

Urho uses Bullet Physics as physical engine.
Urho exposes only basic functionality, but it's pretty easy to expose whatever you want.
So,

> Can I create wind power that affects to clothes? something like ship sails.

Yes, it's possible to create _some_ softbody simulation like clothes and wind (Bullet Physics supports soft bodies).
 https://youtu.be/yLQXmm5Q5zs
 https://youtu.be/aVnHEcFVyp0
No, you can't do it by just dropping some inbuilt component onto your model.
You may find some useful code in our Showcase tho.

> How good U3D performance comparing to UE?

Generic questions about performance are usually meaningless, because performance isn't single metric that could be measured.

Talking about performance of clothes simulation, I suppose that NVidia PhysX is _faster_ (and have better quality) than any open-source physical engine like Bullet Physics. Whether it's important in your particular case or not.. it's open question.

-------------------------

maxvi | 2018-03-13 14:27:17 UTC | #3

Thanks!

Could you provide docs how to expose some new functionality into engine? How can I integrate third libraries?

-------------------------

Eugene | 2018-03-13 15:04:53 UTC | #4

[quote="maxvi, post:3, topic:4083"]
Could you provide docs how to expose some new functionality into engine? How can I integrate third libraries?
[/quote]

If you use static version of Urho, you could access all third-parties directly.
If you use shared version... Well, probably it's better not to use shared version. It may have stripped 3rd-parties off unused functionality.
Alternatively, you could just write whatever you need in your fork of the engine itself.

Here is Lumak's integration of soft body, you can use it as example.
https://discourse.urho3d.io/t/bullets-softbody-physics-example/1319

-------------------------

Modanung | 2018-03-13 23:22:19 UTC | #5

For a changing the shape of a ship's sails I think I'd use morphs (which are called shape keys in Blender).

-------------------------

