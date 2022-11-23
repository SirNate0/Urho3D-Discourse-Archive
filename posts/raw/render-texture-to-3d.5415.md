codexhound | 2019-08-06 00:06:10 UTC | #1

I am attempting to model a star and want to render the flare png to the 3D renderer. How would I go about doing this? Awhile back I used the particle system in Ogre3D to do pretty much the same thing and it worked fairly well. I created a particle system added a particle the size of the star and gave it the flare material.  Made it so it had an infinite lifespan and turned it on and off when needed. I tried doing a similar thing in Urho3D but can't make it work. Any suggestions? Right now it renders but it is just a flat rectangle, white and no blend. If I give it a lifespan it can only be seen from one angle.

Below is what I want to be able to do
![star|603x451](upload://zGQIP7rUSLgovbJUNT14q6swn4Q.png)

-------------------------

Sinoid | 2019-08-06 01:47:23 UTC | #2

You probably want to use a `BillboardSet` component with a material that uses the `DiffUnlitParticleAdd.xml` technique.

See the `07_Billboards` examples for your language of concern.

Particle systems are derived from BillboardSets, most of the rendering work is in the BillboardSet itself, the particle system just deals with the dynamics.

-------------------------

codexhound | 2019-08-06 00:54:07 UTC | #3

Perfect, thanks. Didn't realize billboards are effectively less dynamic particles. Got it working.

-------------------------

codexhound | 2019-08-06 01:42:31 UTC | #4

![star|690x410](upload://plBY08k7qFpNcZDHSZPLjvS3Eix.jpeg)

-------------------------

