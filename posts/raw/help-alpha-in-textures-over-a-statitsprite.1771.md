Kanfor | 2017-01-02 01:10:00 UTC | #1

Hi, urhofans.

I have a scene with a Static Sprite and a Plane with a material with alpha.

If I put the Plane over the Static Sprite I can't see the Plane.
I use DiffNormalAlpha as Technic in the material.
If I use DiffNormalAlphaMask I solve the problem, but the shadow in the texture is is completely opaque.
Is it a bug?

How do i solve this problem?

Thank you very much!  :slight_smile:

-------------------------

gawag | 2017-01-02 01:10:13 UTC | #2

Oh I may have the solution: The sprite has to have its blend mode set to alpha:
[code]sprite->SetBlendMode(Urho3D::BlendMode::BLEND_ALPHA);[/code]
If this is not set, the default of alpha masking is used, which means either full opaque or not opaque at all.

-------------------------

