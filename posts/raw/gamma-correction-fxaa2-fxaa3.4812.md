I3DB | 2019-01-11 21:10:16 UTC | #1

Where can I find info as to what they are doing?

I think I understand what BloomHDR is doing. It seems to make the emissive material emit. But I'm probably wrong.

-------------------------

jmiller | 2019-01-12 02:54:46 UTC | #2

One can study their programs (Shaders/*.glsl, *.hlsl) and how they work in Urho. 
  https://urho3d.github.io/documentation/HEAD/_shaders.html
Knowledge of the general shading language (GLSL/HLSL) will help.

In general
  https://wikipedia.org/wiki/Gamma_correction
  https://wikipedia.org/wiki/Fast_approximate_anti-aliasing

***edit*** I had not looked at the FXAA2/3 implementations.

-------------------------

I3DB | 2019-01-12 01:39:02 UTC | #3

I've been considering getting volumes 1 and 2 of this series https://foundationsofgameenginedev.com/

-------------------------

