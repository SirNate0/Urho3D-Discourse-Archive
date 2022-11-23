Modanung | 2021-12-13 05:37:30 UTC | #1

I've implemented some classes for polynomials and harmonics, which I think might be useful to others as well. It's still unpolished, but functional. Should also work well as `ValueAnimation` interpolation mode, with key frame time used as scalars.

https://gitlab.com/luckeyproductions/dry/-/blob/master/Source/Dry/Math/Polynomial.h

Feel free to provide feedback on the implementation.
Here's a little demo of what it can do, and a preview of what's to come:

https://gitlab.com/Modanung/powerparticles

For the particle system I intend to add some extremity pruning, which should - for the most part - replace particle lifetime limitations.

-------------------------

Modanung | 2021-12-16 13:07:33 UTC | #3

Driven by one `TypedPolynomial<Vector3>`:

https://luckeyproductions.nl/videos/orb2.gif

Constructed from these `Polynomial`s:
```
{ { 0.f,  1.f,  1.f },        { 0.f, .8f, }, PT_HARMONIC_SIN }
{ { .5f, -.2f, 1.5f, -0.5f }, { .5f, .2f, }, PT_HARMONIC_SIN }
{ { 0.f,  1.f,  1.f },        { 0.f, .8f, }, PT_HARMONIC_COS }
```

-------------------------

Modanung | 2021-12-16 22:04:58 UTC | #4

One simple usecase for the `TypedPolynomial` might be calculating the trajectory of a projectile:
```
typedPolynomial.SetCoefficient(0, node_->GetWorldPosition());
typedPolynomial.SetCoefficient(1, rigidBody_->GetLinearVelocity());
typedPolynomial.SetCoefficient(2, gravity);
```

-------------------------

Modanung | 2021-12-25 22:54:40 UTC | #5

And of course they lend themselves well for sound synthesis.

https://gitlab.com/LucKeyProductions/Tools/Orgol

-------------------------

Modanung | 2021-12-27 03:41:59 UTC | #6

https://luckeyproductions.nl/videos/orgol3.mp4
https://luckeyproductions.nl/videos/orgol4.mp4
https://luckeyproductions.nl/videos/orgol5.mp4

-------------------------

Modanung | 2021-12-27 23:27:39 UTC | #7

https://luckeyproductions.nl/videos/orgol6.mp4

-------------------------

